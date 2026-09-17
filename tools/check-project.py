#!/usr/bin/env python3
"""Run project-wide schema, path, task, and cross-reference validation."""
import json
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
ERRORS = []


def load_jsonl(name):
    path = ROOT / name
    rows = []
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError as exc:
            ERRORS.append(f"{name}:{line_no}: invalid JSON: {exc}")
    return rows


claims = load_jsonl("claims.jsonl")
people = load_jsonl("people.jsonl")
sources = load_jsonl("sources.jsonl")
searches = load_jsonl("searches.jsonl")
discrepancies = load_jsonl("discrepancies.jsonl")
claim_by_id = {row.get("id"): row for row in claims}
person_by_id = {row.get("person_id"): row for row in people}
source_by_id = {row.get("source_id"): row for row in sources}
census_ids = set(re.findall(r"^### (US-[A-Z0-9-]+)$", (ROOT / "CATON_CENSUS_LEDGER.md").read_text(encoding="utf-8"), re.MULTILINE))


def require_unique(rows, field, label):
    seen = set()
    for row in rows:
        value = row.get(field)
        if not value:
            ERRORS.append(f"{label}: missing {field}")
        elif value in seen:
            ERRORS.append(f"{label}: duplicate {field} {value}")
        seen.add(value)


require_unique(people, "person_id", "people.jsonl")
require_unique(sources, "source_id", "sources.jsonl")
require_unique(searches, "search_id", "searches.jsonl")
require_unique(discrepancies, "discrepancy_id", "discrepancies.jsonl")

for person in people:
    pid = person.get("person_id", "<missing-person-id>")
    for census_id in person.get("census_ids", []):
        if census_id not in census_ids:
            ERRORS.append(f"{pid}: unknown census_id {census_id}")

valid_outcomes = {"no_hit", "hit", "partial", "inaccessible", "not_searched", "unparsed"}
valid_access = {"open", "authenticated", "subscription", "restricted", "inaccessible", "unknown"}
negative_claim_ids = {row["id"] for row in claims if row.get("claim_type") == "negative_search"}
searches_by_claim = {}
for search in searches:
    sid = search.get("search_id", "<missing-search-id>")
    claim_id = search.get("claim_id")
    claim = claim_by_id.get(claim_id)
    if not claim:
        ERRORS.append(f"{sid}: unknown claim_id {claim_id!r}")
    elif claim.get("claim_type") != "negative_search":
        ERRORS.append(f"{sid}: linked claim {claim_id} is not a negative_search")
    searches_by_claim.setdefault(claim_id, []).append(search)
    if search.get("record_status") not in {"legacy_unstructured", "structured"}:
        ERRORS.append(f"{sid}: invalid record_status {search.get('record_status')!r}")
    if search.get("outcome") not in valid_outcomes:
        ERRORS.append(f"{sid}: invalid outcome {search.get('outcome')!r}")
    for source_id in search.get("source_ids", []):
        if source_id not in source_by_id:
            ERRORS.append(f"{sid}: unknown source_id {source_id}")
        elif claim and source_id not in claim.get("source_ids", []):
            ERRORS.append(f"{sid}: source_id {source_id} is not linked by claim {claim_id}")
    for person_id in search.get("person_ids", []):
        if person_id not in person_by_id:
            ERRORS.append(f"{sid}: unknown person_id {person_id}")
    if search.get("record_status") == "legacy_unstructured":
        if search.get("outcome") != "unparsed" or not search.get("summary_as_written"):
            ERRORS.append(f"{sid}: legacy searches must preserve summary_as_written and use outcome=unparsed")
    else:
        required = ("repository", "collection", "query_terms", "jurisdiction", "date_range",
                    "examined_coverage", "unexamined_coverage", "access_level", "outcome", "limitations")
        for field in required:
            if search.get(field) in (None, "", []):
                ERRORS.append(f"{sid}: structured search missing {field}; use an explicit unknown/none value")
        if search.get("access_level") not in valid_access:
            ERRORS.append(f"{sid}: invalid access_level {search.get('access_level')!r}")
        if not isinstance(search.get("date_range"), dict) or not {"start", "end", "precision"} <= search.get("date_range", {}).keys():
            ERRORS.append(f"{sid}: date_range must contain start, end, and precision")
for claim_id in sorted(negative_claim_ids):
    if claim_id not in searches_by_claim:
        ERRORS.append(f"{claim_id}: negative-search claim has no searches.jsonl record")

valid_discrepancy_status = {"open", "provisional", "resolved", "unresolved"}
for item in discrepancies:
    did = item.get("discrepancy_id", "<missing-discrepancy-id>")
    if item.get("record_type") not in {"discrepancy", "identity_check"}:
        ERRORS.append(f"{did}: invalid record_type {item.get('record_type')!r}")
    if item.get("status") not in valid_discrepancy_status:
        ERRORS.append(f"{did}: invalid status {item.get('status')!r}")
    alternatives = item.get("alternatives", [])
    if len(alternatives) < 2:
        ERRORS.append(f"{did}: at least two alternatives are required")
    if item.get("status") == "resolved" and not item.get("accepted_value"):
        ERRORS.append(f"{did}: resolved record must state accepted_value")
    for census_id in item.get("census_ids", []):
        if census_id not in census_ids:
            ERRORS.append(f"{did}: unknown census_id {census_id}")
    for alternative in alternatives:
        if not alternative.get("label") or not alternative.get("value"):
            ERRORS.append(f"{did}: each alternative needs a label and value")
        for claim_id in alternative.get("claim_ids", []):
            if claim_id not in claim_by_id:
                ERRORS.append(f"{did}: alternative has unknown claim_id {claim_id}")
        for source_id in alternative.get("source_ids", []):
            if source_id not in source_by_id:
                ERRORS.append(f"{did}: alternative has unknown source_id {source_id}")
            elif not any(source_id in claim_by_id.get(claim_id, {}).get("source_ids", [])
                         for claim_id in alternative.get("claim_ids", [])):
                ERRORS.append(f"{did}: alternative source {source_id} is not linked to its claims")

allowed_modes = {"agent", "human", "script", "relay"}
allowed_task_statuses = {"open", "active", "partial", "blocked", "reopened", "done", "closed", "void"}
for path in sorted((ROOT / "tasks").glob("T*.md")):
    text = path.read_text(encoding="utf-8")
    sections = re.split(r"^---\s*$", text, maxsplit=2, flags=re.MULTILINE)
    if len(sections) < 3:
        ERRORS.append(f"{path.relative_to(ROOT)}: missing YAML frontmatter")
        continue
    frontmatter = sections[1]
    fields = {}
    for line in frontmatter.splitlines():
        match = re.match(r"^([a-z_]+):\s*(.*?)\s*$", line)
        if match:
            fields[match.group(1)] = match.group(2).strip("'\"")
    for required_field in ("id", "priority", "mode", "status"):
        if not fields.get(required_field):
            ERRORS.append(f"{path.relative_to(ROOT)}: missing frontmatter {required_field}")
    if fields.get("mode") and fields["mode"] not in allowed_modes:
        ERRORS.append(f"{path.relative_to(ROOT)}: invalid mode {fields['mode']!r}")
    if fields.get("status") and fields["status"] not in allowed_task_statuses:
        ERRORS.append(f"{path.relative_to(ROOT)}: invalid status {fields['status']!r}")
    if fields.get("priority") and not fields["priority"].isdigit():
        ERRORS.append(f"{path.relative_to(ROOT)}: priority must be an integer")
    expected_id = path.name.split("_", 1)[0]
    if fields.get("id") and fields["id"] != expected_id:
        ERRORS.append(f"{path.relative_to(ROOT)}: frontmatter id {fields['id']} does not match filename {expected_id}")

child_failed = False
for script in ("check-claims.py", "check-census-ledger.py"):
    result = subprocess.run([sys.executable, str(ROOT / "tools" / script)], cwd=ROOT, text=True, capture_output=True)
    if result.stdout:
        print(result.stdout, end="")
    if result.stderr:
        print(result.stderr, end="", file=sys.stderr)
    if result.returncode:
        child_failed = True

if ERRORS:
    for error in ERRORS:
        print(f"ERROR: {error}", file=sys.stderr)
if child_failed or ERRORS:
    print("Project validation failed")
    raise SystemExit(1)
print(f"Project validation ok: {len(people)} people, {len(searches)} search records, {len(discrepancies)} discrepancy records, and {len(list((ROOT / 'tasks').glob('T*.md')))} tasks")
