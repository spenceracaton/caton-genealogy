#!/usr/bin/env python3
"""One-time additive migration of legacy claims into the linked record model.

Preserves every existing claim field and ID. Citation IDs represent the exact
legacy citation bundle (not necessarily one fully normalized archival source).
Safe to rerun: existing IDs and explicit claim labels are preserved.
"""
import collections
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent


def read_jsonl(path):
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def write_jsonl(path, rows):
    path.write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows), encoding="utf-8")


def old_index_kind(fact):
    """Frozen compatibility classifier used only to label old rows once."""
    f = re.sub(r"^\[RENUMBERED[^\]]*\]\s*", "", fact.upper())
    if re.match(r"(REVERSED|SUPERSEDED|WRONG, SEE|DOWNGRADED|EXCLUSION WITHDRAWN|PREDICTION FAILED|VOID)\b", f):
        return "VOID/REVERSED"
    if re.match(r"MOOT\b", f):
        return "moot"
    if re.match(r"(NEGATIVE|BOUNDED NEGATIVE|DEAD END|WEAK NEGATIVE)\b", f) or re.search(r"\bNEGATIVE, SCOPED\b|\bNEGATIVE, WEAK\b|\bNEGATIVE, LIMITED\b", f):
        return "negative"
    if re.match(r"DO NOT MERGE\b", f) or re.search(r"\bDO NOT MERGE - (IDENTIFIED|RULED OUT)\b", f):
        return "do-not-merge"
    if re.match(r"(HYPOTHESIS|LEAD ONLY|LEAD FOR|LEAD, C-LEVEL|POSSIBLE COUNTY|STRATEGIC REFRAME|CONVERGENCE|REFRAMED QUESTION|THE FORK|STRONGEST (SIBLING|STRUCTURAL)|BEST CANDIDATE|MIGRATION LEAD|CORROBORATED - UPGRADED|UNSOURCED ASSERTION|POSSIBLE)\b", f):
        return "hypothesis"
    if re.match(r"(TOOLING|METHOD|CAUSED A FALSE|GAP CLOSED|SECOND STRUCTURAL|ACCESS ROUTE|CLUSTER MAP|COMPLETE STATEWIDE|FULL SWEEP|THE LARGEST UNEXAMINED|CLAUDE-IN-CHROME|1840 DELAWARE CO., OHIO \(T11\) - ALL|ASSESSED AND FOUND|THE CHATGPT HANDOFF|THREE DISCREPANCIES|COLLATERAL)", f):
        return "method"
    return "fact"


def claim_type(old_kind):
    return {
        "fact": "observation",
        "hypothesis": "hypothesis",
        "negative": "negative_search",
        "do-not-merge": "identity_constraint",
        "method": "method",
        "moot": "other",
        "VOID/REVERSED": "observation",
    }[old_kind]


def lifecycle(fact, old_kind):
    if old_kind == "moot":
        return "moot"
    if old_kind != "VOID/REVERSED":
        return "active"
    f = re.sub(r"^\[RENUMBERED[^\]]*\]\s*", "", fact.upper())
    if re.match(r"VOID\b", f):
        return "void"
    if re.match(r"(SUPERSEDED|DOWNGRADED|PREDICTION FAILED)\b", f):
        return "superseded"
    return "reversed"


claims_path = ROOT / "claims.jsonl"
claims = read_jsonl(claims_path)
people = read_jsonl(ROOT / "people.jsonl")
sources_path = ROOT / "sources.jsonl"
sources = read_jsonl(sources_path)

source_key_to_id = {}
source_by_id = {}
for source in sources:
    key = (source.get("citation_as_written", ""), source.get("url_as_written", ""), tuple(source.get("evidence_paths", [])))
    source_key_to_id[key] = source["source_id"]
    source_by_id[source["source_id"]] = source

next_source_num = max((int(re.search(r"(\d+)$", s["source_id"]).group(1)) for s in sources if re.search(r"(\d+)$", s.get("source_id", ""))), default=0) + 1
person_claims = collections.defaultdict(list)
for person in people:
    for claim_id in person.get("claim_ids", []):
        person_claims[claim_id].append(person["person_id"])

for claim in claims:
    raw_evidence = claim.get("evidence") or ""
    evidence_paths = [part.strip() for part in raw_evidence.split(";") if part.strip()]
    key = (claim.get("source", ""), claim.get("url", ""), tuple(evidence_paths))
    source_id = source_key_to_id.get(key)
    if source_id is None:
        source_id = f"SRC-{next_source_num:04d}"
        next_source_num += 1
        source_key_to_id[key] = source_id
        record = {
            "source_id": source_id,
            "citation_as_written": claim.get("source", ""),
            "url_as_written": claim.get("url", ""),
            "evidence_paths": evidence_paths,
            "claim_ids": [],
            "review_status": "legacy_bundle",
            "notes": "Citation fields preserved verbatim from claims.jsonl; bundle may combine sources and is not yet atomized.",
        }
        sources.append(record)
        source_by_id[source_id] = record
    record = source_by_id[source_id]
    if claim["id"] not in record.setdefault("claim_ids", []):
        record["claim_ids"].append(claim["id"])

    old_kind = old_index_kind(claim.get("fact", ""))
    claim.setdefault("claim_type", claim_type(old_kind))
    claim.setdefault("status", lifecycle(claim.get("fact", ""), old_kind))
    claim.setdefault("classification_basis", "legacy_text_migration")
    claim.setdefault("source_ids", [source_id])
    claim.setdefault("person_ids", sorted(person_claims.get(claim["id"], [])))
    refs = [ref for ref in re.findall(r"\b[CG]\d{3}\b", claim.get("fact", "")) if ref != claim["id"]]
    claim.setdefault("related_claim_ids", list(dict.fromkeys(refs)))

for record in sources:
    record["claim_ids"] = list(dict.fromkeys(record.get("claim_ids", [])))
sources.sort(key=lambda row: int(re.search(r"(\d+)$", row["source_id"]).group(1)))

# One explicit backfill item per legacy negative-search claim. The prose remains
# intact in claims.jsonl; unknown search scope is deliberately not guessed here.
searches_path = ROOT / "searches.jsonl"
searches = read_jsonl(searches_path)
existing_search_ids = {row["search_id"] for row in searches}
for claim in claims:
    if claim.get("claim_type") != "negative_search":
        continue
    search_id = f"SRCH-{claim['id']}"
    if search_id in existing_search_ids:
        continue
    searches.append({
        "search_id": search_id,
        "claim_id": claim["id"],
        "source_ids": claim.get("source_ids", []),
        "person_ids": claim.get("person_ids", []),
        "record_status": "legacy_unstructured",
        "repository": None,
        "collection": None,
        "query_terms": [],
        "jurisdiction": None,
        "date_range": None,
        "examined_coverage": None,
        "unexamined_coverage": None,
        "access_level": "unknown",
        "outcome": "unparsed",
        "target_as_written": claim.get("person", ""),
        "date_scope_as_written": claim.get("date", ""),
        "place_scope_as_written": claim.get("place", ""),
        "summary_as_written": claim.get("fact", ""),
        "limitations": "Legacy negative claim not yet decomposed into a precise query and coverage statement; consult its linked claim and evidence note.",
    })
searches.sort(key=lambda row: row["search_id"])

# Enrich each alternative with the citation IDs already attached to its claims.
claim_by_id = {claim["id"]: claim for claim in claims}
discrepancies_path = ROOT / "discrepancies.jsonl"
discrepancies = read_jsonl(discrepancies_path)
for item in discrepancies:
    for alternative in item.get("alternatives", []):
        ids = []
        for claim_id in alternative.get("claim_ids", []):
            ids.extend(claim_by_id.get(claim_id, {}).get("source_ids", []))
        if not alternative.get("source_ids"):
            alternative["source_ids"] = list(dict.fromkeys(ids))

# Keep the claims file's current ordering and existing field values. This is a
# mechanical additive rewrite; no fact, grade, date, person label, or ID changes.
write_jsonl(claims_path, claims)
write_jsonl(sources_path, sources)
write_jsonl(searches_path, searches)
write_jsonl(discrepancies_path, discrepancies)
print(f"Migrated {len(claims)} claims; registered {len(sources)} citation bundles, {len(people)} people, {len(searches)} search records, and {len(discrepancies)} discrepancy records.")
