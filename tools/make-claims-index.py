#!/usr/bin/env python3
"""Regenerate the claims index from explicit claim fields and registries."""
import collections
import datetime
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent


def read_jsonl(path):
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


rows = read_jsonl(ROOT / "claims.jsonl")
discrepancies = read_jsonl(ROOT / "discrepancies.jsonl")


def short(text, n=110):
    text = re.sub(r"^\[RENUMBERED[^\]]*\]\s*", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return (text[:n] + "…") if len(text) > n else text


kind_labels = {
    "observation": "fact",
    "hypothesis": "hypothesis",
    "negative_search": "negative",
    "identity_constraint": "do-not-merge",
    "method": "method",
    "other": "other",
}
kind_order = ["observation", "hypothesis", "negative_search", "identity_constraint", "method", "other"]
status_order = ["active", "superseded", "reversed", "void", "moot", "review"]
kind_counts = collections.Counter(row.get("claim_type", "other") for row in rows)
status_counts = collections.Counter(row.get("status", "review") for row in rows)
grade_counts = collections.Counter(row.get("grade", "?") for row in rows)

out = [
    f"# Claims index — generated {datetime.date.today().isoformat()} from `claims.jsonl` ({len(rows)} claims)\n",
    "Census household composition is canonical in `CATON_CENSUS_LEDGER.md`; use its stable IDs for row-level readings.\n",
    "Regenerate with `python3 tools/make-claims-index.py`. **Do not edit by hand.**\n",
    "Type and lifecycle are read from explicit `claim_type` and `status` fields. Legacy classifications marked `legacy_text_migration` require source-level review; no status is inferred here.\n",
    "| claim type | n | | lifecycle | n |\n|---|---:|---|---|---:|",
]
for index in range(max(len(kind_order), len(status_order))):
    kind = kind_order[index] if index < len(kind_order) else None
    status = status_order[index] if index < len(status_order) else None
    left = f"{kind_labels[kind]} | {kind_counts.get(kind, 0)}" if kind else " | "
    right = f"{status} | {status_counts.get(status, 0)}" if status else " | "
    out.append(f"| {left} | | {right} |")
out.append("")
out.append("| evidence grade | n |\n|---|---:|")
for grade in ("A", "B", "C"):
    out.append(f"| {grade} | {grade_counts.get(grade, 0)} |")
out.append("")

out.append("## The load-bearing ones\n")
key = ["C075", "C107", "C099", "C110", "C062", "C077", "C098", "C108", "C038", "C069", "C058"]
out.append("| id | grade | type | lifecycle | what |\n|---|---|---|---|---|")
for row in rows:
    if row["id"] in key:
        out.append(f"| **{row['id']}** | {row['grade']} | {kind_labels.get(row['claim_type'], row['claim_type'])} | {row['status']} | {short(row['fact'], 150)} |")
out.append("")

out.append("## All claims\n")
out.append("| id | grade | type | lifecycle | pass | person | summary |\n|---|---|---|---|---|---|---|")
retired = {"superseded", "reversed", "void"}
for row in rows:
    claim_id = f"~~{row['id']}~~" if row["status"] in retired else row["id"]
    out.append(f"| {claim_id} | {row['grade']} | {kind_labels.get(row['claim_type'], row['claim_type'])} | {row['status']} | {row.get('pass', '')} | {row['person'][:34]} | {short(row['fact'])} |")

out.append("\n## Unresolved discrepancies and identity checks\n")
out.append("Alternatives and claim/source links are canonical in `discrepancies.jsonl`. Identity checks are not automatically conflicts between one person's records.\n")
out.append("| id | status | record type | topic | next action |\n|---|---|---|---|---|")
for item in discrepancies:
    if item["status"] != "resolved":
        next_action = re.sub(r"\s+", " ", item.get("next_action") or "—")
        out.append(f"| {item['discrepancy_id']} | {item['status']} | {item['record_type']} | {item['topic']} | {next_action} |")

(ROOT / "claims-index.md").write_text("\n".join(out) + "\n", encoding="utf-8")
print(f"claims-index.md: {len(rows)} claims; explicit lifecycle {dict(status_counts)}; types {dict(kind_counts)}")
