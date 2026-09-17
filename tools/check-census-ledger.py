#!/usr/bin/env python3
"""Validate the canonical census ledger without changing any files."""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LEDGER = ROOT / "CATON_CENSUS_LEDGER.md"
CLAIMS = ROOT / "claims.jsonl"

REQUIRED = (
    "claim_ids:",
    "year:",
    "reference_date:",
    "state:",
    "county:",
    "locality:",
    "head_as_written:",
    "source_citation:",
    "page_or_image:",
    "source_image:",
    "image_inspected:",
    "source_layer:",
    "transcription_confidence:",
    "raw_observation:",
    "normalized_observation:",
    "interpretation:",
    "identity_status:",
    "evidence_status:",
    "last_verified:",
)
LAYERS = {
    "primary_image",
    "primary_image_plus_index",
    "derivative_transcription",
    "index_only",
    "claim_summary",
}
SCHEDULE_1810_1820 = {
    "males": {"under_10", "10_16", "16_18", "16_26", "26_45", "45_plus"},
    "females": {"under_10", "10_16", "16_26", "26_45", "45_plus"},
}
SCHEDULE_1830_1840 = {"under_5", "5_10", "10_15", "15_20", "20_30", "30_40", "40_50",
                      "50_60", "60_70", "70_80", "80_90", "90_100", "100_plus"}


def fail(message):
    print(f"ERROR: {message}", file=sys.stderr)
    return 1


text = LEDGER.read_text()
blocks = re.split(r"(?=^### US-)", text, flags=re.MULTILINE)[1:]
if not blocks:
    raise SystemExit(fail("no household records found"))

ids = []
errors = []
warnings = []
known_count_discrepancies = {}
discrepancy_path = ROOT / "discrepancies.jsonl"
if discrepancy_path.exists():
    for line in discrepancy_path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        item = json.loads(line)
        if item.get("status") in {"open", "provisional", "unresolved"}:
            for census_id in item.get("census_ids", []):
                known_count_discrepancies[census_id] = item.get("discrepancy_id", "unlinked discrepancy")
claim_rows = [json.loads(line) for line in CLAIMS.read_text().splitlines() if line.strip()]
claim_ids = {row["id"] for row in claim_rows}

for block in blocks:
    heading = block.splitlines()[0].strip()
    census_id = heading.removeprefix("### ").strip()
    ids.append(census_id)
    for field in REQUIRED:
        if field not in block:
            errors.append(f"{census_id}: missing {field}")

    refs = re.search(r"^- claim_ids: (.+)$", block, flags=re.MULTILINE)
    if refs:
        for claim_id in re.findall(r"C\d{3}|G\d{3}", refs.group(1)):
            if claim_id not in claim_ids:
                errors.append(f"{census_id}: unknown claim {claim_id}")

    layers = re.search(r"^- source_layer: (.+)$", block, flags=re.MULTILINE)
    if layers:
        for layer in re.findall(r"primary_image(?:_plus_index)?|derivative_transcription|index_only|claim_summary", layers.group(1)):
            if layer not in LAYERS:
                errors.append(f"{census_id}: invalid source layer {layer}")

    for path in re.findall(r"evidence/[A-Za-z0-9_.-]+", block):
        if not (ROOT / path).exists():
            errors.append(f"{census_id}: missing evidence path {path}")

    year_match = re.search(r"^- year: (\d{4})", block, flags=re.MULTILINE)
    normalized = re.search(r"^- normalized_observation: (.*)$", block, flags=re.MULTILINE)
    if year_match and normalized:
        year = int(year_match.group(1))
        value = normalized.group(1)
        expected_by_sex = None
        if year in (1810, 1820):
            expected_by_sex = SCHEDULE_1810_1820
        elif year in (1830, 1840):
            expected_by_sex = {"males": SCHEDULE_1830_1840, "females": SCHEDULE_1830_1840}

        if expected_by_sex:
            maps = {}
            for sex, contents in re.findall(r"\b(males|females)\s*\{([^}]*)\}", value):
                counts = {}
                for category, count in re.findall(r"([a-z0-9_]+)\s*:\s*(-?\d+)", contents):
                    counts[category] = int(count)
                maps[sex] = counts
            for sex, counts in maps.items():
                allowed = expected_by_sex[sex]
                unexpected = sorted(set(counts) - allowed)
                if unexpected:
                    errors.append(f"{census_id}: {year} {sex} has invalid categories {unexpected}")
                for category, count in counts.items():
                    if count < 0:
                        errors.append(f"{census_id}: negative count for {sex}.{category}")
                missing_categories = sorted(allowed - set(counts))
                if missing_categories:
                    warnings.append(f"{census_id}: normalized {sex} categories omit {', '.join(missing_categories)}; completeness not established")

            if maps and set(maps) != {"males", "females"}:
                warnings.append(f"{census_id}: only one sex has normalized category counts")

            total_match = re.search(r"\bhousehold_total\s+(\d+)\b", value)
            if total_match and set(maps) == {"males", "females"}:
                complete = all(set(maps[sex]) == set(expected_by_sex[sex]) for sex in ("males", "females"))
                if complete:
                    male_total = sum(maps["males"].values())
                    if year in (1810, 1820):
                        male_total -= maps["males"].get("16_18", 0)  # 16-18 overlaps 16-26.
                    calculated = male_total + sum(maps["females"].values())
                    recorded = int(total_match.group(1))
                    if calculated != recorded:
                        message = f"{census_id}: household_total {recorded} does not match normalized counts ({calculated})"
                        if census_id in known_count_discrepancies:
                            warnings.append(f"{message}; tracked in {known_count_discrepancies[census_id]}")
                        else:
                            errors.append(message)

duplicates = sorted(census_id for census_id in set(ids) if ids.count(census_id) > 1)
errors.extend(f"duplicate census_id {census_id}" for census_id in duplicates)

def report_warnings():
    if warnings:
        print(f"{len(warnings)} census normalization-completeness warning(s):")
        for warning in warnings[:12]:
            print(f"WARNING: {warning}")
        if len(warnings) > 12:
            print(f"WARNING: {len(warnings) - 12} additional warnings omitted")


if errors:
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    report_warnings()
    raise SystemExit(1)

print(f"{len(ids)} census household records checked; schema, references, and available count arithmetic ok")
report_warnings()
