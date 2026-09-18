#!/usr/bin/env python3
"""Validate claim schema, IDs, source/person links, and evidence paths."""
import collections
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent


def load(path):
    rows = []
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError as exc:
            print(f"ERROR: {path.name}:{line_no}: invalid JSON: {exc}")
            raise SystemExit(1)
    return rows


claims = load(ROOT / "claims.jsonl")
sources = load(ROOT / "sources.jsonl")
people = load(ROOT / "people.jsonl")
errors = []


def duplicates(rows, field, label):
    counts = collections.Counter(row.get(field) for row in rows)
    for value, count in counts.items():
        if not value or count > 1:
            errors.append(f"{label}: invalid or duplicate {field} {value!r} x{count}")


duplicates(claims, "id", "claims")
duplicates(sources, "source_id", "sources")
duplicates(people, "person_id", "people")
claim_ids = {row.get("id") for row in claims}
source_ids = {row.get("source_id") for row in sources}
person_ids = {row.get("person_id") for row in people}
claim_by_id = {row.get("id"): row for row in claims}
source_by_id = {row.get("source_id"): row for row in sources}
person_by_id = {row.get("person_id"): row for row in people}

claim_types = {"observation", "hypothesis", "negative_search", "identity_constraint", "method", "other"}
claim_statuses = {"active", "superseded", "reversed", "void", "moot", "review"}
# `kind` is the single-field classification the ChatGPT line introduced (METHOD.md s.4).
# It is kept in step with claim_type + status so both validators and both agents agree.
KINDS = {"fact", "hypothesis", "negative", "do-not-merge", "method", "moot", "void"}


def expected_kind(claim_type, status):
    if status in {"reversed", "superseded", "void"}:
        return "void"
    if status == "moot":
        return "moot"
    return {"observation": "fact", "negative_search": "negative", "method": "method", "hypothesis": "hypothesis",
            "identity_constraint": "do-not-merge", "other": "fact"}.get(claim_type)


required = {"id", "person", "fact", "date", "place", "grade", "kind", "source", "url", "evidence", "pass",
            "claim_type", "status", "classification_basis", "source_ids", "person_ids", "related_claim_ids"}

for row in claims:
    cid = row.get("id", "<missing-id>")
    missing = required - row.keys()
    if missing:
        errors.append(f"{cid}: missing claim fields {sorted(missing)}")
    if not re.fullmatch(r"[CG]\d{3}", str(row.get("id", ""))):
        errors.append(f"{cid}: claim ID must use C### or G###")
    if row.get("grade") not in {"A", "B", "C"}:
        errors.append(f"{cid}: invalid grade {row.get('grade')!r}")
    if row.get("claim_type") not in claim_types:
        errors.append(f"{cid}: invalid claim_type {row.get('claim_type')!r}")
    if row.get("status") not in claim_statuses:
        errors.append(f"{cid}: invalid status {row.get('status')!r}")
    if row.get("classification_basis") not in {"legacy_text_migration", "manual", "imported", "kind_field_at_merge_2026-09-17"}:
        errors.append(f"{cid}: invalid classification_basis {row.get('classification_basis')!r}")
    if "kind" not in row:
        errors.append(f"{cid}: no 'kind' field - set one of {sorted(KINDS)} (see METHOD.md s.4)")
    elif row["kind"] not in KINDS:
        errors.append(f"{cid}: kind {row['kind']!r} not in {sorted(KINDS)}")
    elif row["kind"] != expected_kind(row.get("claim_type"), row.get("status")):
        errors.append(f"{cid}: kind {row['kind']!r} disagrees with claim_type/status "
                      f"{row.get('claim_type')!r}/{row.get('status')!r} (expected {expected_kind(row.get('claim_type'), row.get('status'))!r})")
    for field, known_ids in (("source_ids", source_ids), ("person_ids", person_ids), ("related_claim_ids", claim_ids)):
        refs = row.get(field)
        if not isinstance(refs, list):
            errors.append(f"{cid}: {field} must be an array")
            continue
        if field == "source_ids" and not refs:
            errors.append(f"{cid}: at least one source bundle ID is required")
        for ref in refs:
            if ref not in known_ids:
                errors.append(f"{cid}: unknown {field} reference {ref!r}")
    for raw_path in [part.strip() for part in (row.get("evidence") or "").split(";") if part.strip()]:
        if not (ROOT / raw_path).exists():
            errors.append(f"{cid}: missing evidence path {raw_path}")

for source in sources:
    sid = source.get("source_id", "<missing-source-id>")
    if not re.fullmatch(r"SRC-\d{4,}", str(source.get("source_id", ""))):
        errors.append(f"{sid}: source ID must use SRC-####")
    for field in ("citation_as_written", "url_as_written", "evidence_paths", "claim_ids", "review_status"):
        if field not in source:
            errors.append(f"{sid}: missing source field {field}")
    for claim_id in source.get("claim_ids", []):
        if claim_id not in claim_ids:
            errors.append(f"{sid}: unknown claim {claim_id}")
        elif sid not in claim_by_id[claim_id].get("source_ids", []):
            errors.append(f"{sid}: claim {claim_id} does not link back to this source")
    for raw_path in source.get("evidence_paths", []):
        if not (ROOT / raw_path).exists():
            errors.append(f"{sid}: missing evidence path {raw_path}")

for person in people:
    pid = person.get("person_id", "<missing-person-id>")
    if person.get("identity_status") not in {"identified", "candidate", "unresolved"}:
        errors.append(f"{pid}: invalid identity_status {person.get('identity_status')!r}")
    for claim_id in person.get("claim_ids", []):
        if claim_id not in claim_ids:
            errors.append(f"{pid}: unknown claim {claim_id}")
        elif pid not in claim_by_id[claim_id].get("person_ids", []):
            errors.append(f"{pid}: claim {claim_id} does not link back to this person")
    for other in person.get("distinguish_from", []):
        if other not in person_ids:
            errors.append(f"{pid}: unknown distinguish_from person {other}")
        elif other == pid:
            errors.append(f"{pid}: cannot distinguish a person from itself")

if errors:
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    print(f"{len(claims)} claims checked; FAIL")
    raise SystemExit(1)

print(f"{len(claims)} claims, {len(sources)} source bundles, and {len(people)} people checked; references and evidence paths ok")
