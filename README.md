# Caton genealogy

**Question:** Who were the parents of Aaron Caton, born 16 May 1820 in Virginia?
They remain unknown. "Wheeling" is unsourced (C075). As of 15 Sep 2026 the answer
is a **fork** between Fauquier Co., VA and the Maryland–Pennsylvania/Wheeling line,
now unequal: the Fauquier Catons trace to three brothers on Broad Run, Prince William
Co., in the 1790s, one of them an Aaron (C153–C157). Read BRIEF §1 first. DNA testing
is off the table. **FamilySearch Full-Text Search is the working tool.**

## Canonical records and authority

Read [DATA_MODEL.md](DATA_MODEL.md) for ownership, schemas, and ID rules. The
canonical layers are `CATON_CENSUS_LEDGER.md` (census observations), `sources.jsonl`
(citation bundles), `people.jsonl` (identity boundaries), `claims.jsonl`
(assertions), `searches.jsonl` (search scope/outcomes), and `discrepancies.jsonl`
(competing readings). `BRIEF.md` is the current synthesis. Dated handoffs and
`NEXT-SESSION.md` are context/action records, not competing evidence stores.

## Active research set

- `BRIEF.md` — corrected working state. Read first.
- `NEXT-SESSION.md` — concise next-session action queue; full 15 Sep snapshot is archived.
- `PARENTAGE-TESTS.md` — every remaining test that could name or exclude Aaron's father, ranked.
- CATON_CENSUS_LEDGER.md — canonical row-level census households and bounded coverage checks.
- `claims.jsonl` — established facts, sources, grades, and worthwhile negatives.
- `sources.jsonl` — stable source/citation-bundle IDs linked to claims.
- `people.jsonl` — stable identity IDs for disambiguation; not a kinship tree.
- `searches.jsonl` — structured search coverage; legacy unparsed entries are explicit.
- `discrepancies.jsonl` — alternatives, claim/source links, and resolution state.
- `DATA_MODEL.md` — schema, authority, and migration rules.
- `tasks/` — one scoped lead per file; see `tasks/README.md` for execution and
  merge rules.
- `evidence/` — record artifacts and task returns; `evidence/README.md` is a
  generated manifest (file → citing claims → note).
- `claims-index.md` — generated one-line index of every claim with status and grade.
- `tools/` — generators and validators; run `python3 tools/check-project.py` after a merge.
- After changing claims or discrepancy records, regenerate the index with
  `python3 tools/make-claims-index.py`, then run `python3 tools/check-project.py`.
- `TREE.md`, `tree.html` — a 10 Sep draft, now **stale** (see banner); regenerate before use.
- `FAUQUIER-HANDOFF-2026-09-11.md`, `CATON-VA-CHANCERY-LINKS.md` — dated working documents.

## Census source rule

CATON_CENSUS_LEDGER.md is canonical for census composition. Narrative files cite
its stable census IDs and carry interpretation or next actions; they do not create
second household transcriptions. Raw evidence remains unchanged. Run
tools/check-census-ledger.py after ledger edits.

## Archive

`archive/` preserves superseded pass notes and imported packages for provenance.
It is not research context. Read it only to reconstruct a specific decision.
`archive/imports/` retains the original package for each import; its manifest
records what was reconciled or deduplicated.

## Start a local pass

Read `BRIEF.md`, `DATA_MODEL.md`, and `tasks/README.md`, then select work from task frontmatter.
Never infer Aaron's parentage from a same-name record. Evidence, claims, and task
status are merged only after returned records are checked.
