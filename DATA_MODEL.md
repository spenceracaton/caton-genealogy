# Genealogy record model

This file defines which artifact owns each kind of information. The goal is to
keep observations, source references, identity decisions, interpretations, and
search limits linkable without making narrative prose the database.

## Authority by record type

| Record type | Canonical artifact | What it owns |
|---|---|---|
| Census household observations | `CATON_CENSUS_LEDGER.md` | Source reading, schedule-normalized values, image status, and separate interpretation |
| Citation bundles | `sources.jsonl` | Stable `source_id`, citation as originally recorded, URL, local evidence paths, linked claims |
| Person identity boundaries | `people.jsonl` | Stable `person_id`, aliases, provisional identity status, and explicit non-merge boundaries |
| Assertions | `claims.jsonl` | One assertion or bounded research result, grade, lifecycle, and links to people and sources |
| Search coverage | `searches.jsonl` | Repository, query, jurisdiction, dates, inspected coverage, access, outcome, and limitations |
| Competing readings / identity questions | `discrepancies.jsonl` | Alternatives, source/claim links, adjudication state, and next resolving test |
| Current synthesis | `BRIEF.md` | Current interpretation and research state; cites canonical IDs rather than duplicating record details |
| Next action | `NEXT-SESSION.md` and active task files | Work queue only; not an alternate evidence store |
| Captured records and transcripts | `evidence/` | Preserved artifacts; never silently overwritten during normalization |

`claims.jsonl` retains its legacy `source`, `url`, `evidence`, and `person`
display fields. New and migrated records also use stable references. A source
record with `review_status: "legacy_bundle"` preserves a citation field exactly
as entered; it may contain multiple citations and has not yet been atomized.
Do not infer missing bibliographic metadata from those bundles.

## Controlled fields

`claims.jsonl` rows retain their original fields and add:

- `claim_type`: `observation`, `hypothesis`, `negative_search`, `identity_constraint`, `method`, or `other`.
- `status`: `active`, `superseded`, `reversed`, `void`, `moot`, or `review`.
- `source_ids`, `person_ids`, and `related_claim_ids`: arrays of stable IDs.
- `classification_basis`: `legacy_text_migration` for one-time labels inferred from legacy prefixes; review these before treating classification as independently adjudicated.

The old text is preserved. The generated claims index reads these explicit fields
and never infers lifecycle from the beginning of `fact`.

`people.jsonl` uses `identity_status` values `identified`, `candidate`, or
`unresolved`. A person ID distinguishes a working identity; it does not prove
parentage or kinship. `distinguish_from` means keep the records separate unless
new evidence justifies a merge.

`searches.jsonl` has one legacy bundle for each negative-search claim. These are
marked `record_status: "legacy_unstructured"` and `outcome: "unparsed"` until the
actual scope can be safely decomposed. New records use `record_status:
"structured"`, `outcome` in `no_hit`, `hit`, `partial`, `inaccessible`, or
`not_searched`, and explicit jurisdiction, date range, query terms, access
result, examined/unexamined coverage, and limitations. A legacy bundle is not a
claim that those fields are known.

For a structured search, `date_range` is an object with `start`, `end`, and
`precision`; use explicit `null` bounds with a precision such as `unknown` when
dates cannot be bounded. Use explicit values such as `unknown` or `none recorded`
for unavailable repository, collection, jurisdiction, or coverage details. Never
leave a search-level unknown implicit.

`discrepancies.jsonl` records explicit alternatives and links each alternative
to claim and source IDs. `record_type` is `discrepancy` or `identity_check`;
`status` is `open`, `provisional`, `resolved`, or `unresolved`. An
`identity_check` is not to be rewritten as a conflict between two facts unless
the records are first shown to concern the same person. `census_ids` links any
arithmetic or reading exception to the census ledger record it qualifies; an
unresolved exception remains visible in validation output.

## Editing and validation

- Never reuse an ID. Preserve historical claim IDs; add links instead of renumbering.
- Keep raw source readings unchanged. Put normalization and interpretation in their own fields.
- Leave unknown values empty or null and label legacy material explicitly; do not fill gaps by inference.
- When adding a claim, create or reuse its source/person IDs and set classification fields directly.
- Run `python3 tools/check-project.py` after a merge. It checks the registries,
  claims, tasks, census ledger, paths, and cross-references. The focused
  `check-claims.py` and `check-census-ledger.py` remain available for local edits.
