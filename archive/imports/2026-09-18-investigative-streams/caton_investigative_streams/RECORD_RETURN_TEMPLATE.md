# Record return and acquisition templates

## One record or linked case return

```text
STREAM: S01-S08
STATUS: found | not-found | partial | blocked
QUESTION TESTED:
REPOSITORY / COLLECTION:
AUTHOR OR CREATING OFFICE:
BOOK / BOX / FOLDER / PAGE / IMAGE:
STABLE URL:
EVENT DATE:
DOCUMENT EXECUTION DATE:
ACKNOWLEDGMENT / FILING / RECORDING DATE:
RETRIEVED DATE:
SOURCE FORM: original | contemporary copy | later typescript | abstract | index | compilation
IMAGE RETAINED: exact path, or explanation/rights limitation
TRANSCRIPTION: exact pertinent wording; use [illegible], do not silently repair
NAMED PEOPLE AND DOCUMENT ROLES:
WHAT THE RECORD DIRECTLY STATES:
WHAT IS INFERRED:
SOURCE GRADE: A | B | C, with reason
INFERENCE GRADE: A | B | C, with reason
KIND: fact | hypothesis | negative | do-not-merge | method | moot | void
IDENTITY MATCH: evidence for/against; competing same-name person
CONFLICTS: ledger IDs and precise differences
SOURCE DEPENDENCE: original underlying account; possible copies/reprints
WHAT WOULD WEAKEN THE INTERPRETATION:
NEXT DISCRIMINATING RECORD:
```

## Negative/coverage return

```text
SOURCE AND EXACT JURISDICTION:
DATES ACTUALLY COVERED:
PAGES/IMAGES/BOXES ACTUALLY READ:
INDEX OR FULL TEXT OR MANUAL PAGE REVIEW:
VARIANTS / PARTIES TESTED:
CONTROL ENTRY CONFIRMING SEARCH WORKED:
KNOWN GAPS / RESTRICTIONS / IMAGE DEFECTS:
NARROW RESULT:
WHAT THE RESULT DOES NOT EXCLUDE:
WHY A REPEAT WOULD OR WOULD NOT BE JUSTIFIED:
```

## Acquisition register

| Stream owner | Repository and exact item | Existing request checked? | Request actually sent/date | Reply/status checked date | Cost approved? | Access/reuse terms | Next action |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

Do not expose personal email content or restricted images in a public repository. Do not infer that an old request is still unanswered. Label draft messages explicitly as unsent.

## Census observation schema

Use a record-observation ID, not an assumed person ID. Preserve the printed and transcribed headings separately; record overlapping columns and any local enumerator variation. Do not calculate a total by adding overlapping1820 columns.

```json
{
  "observation_id": "jurisdiction-year-page-row",
  "named_head_verbatim": "",
  "census_reference_date": "",
  "enumeration_date_if_stated": null,
  "locality_verbatim": "",
  "roll_page_frame": {},
  "source_form": "original or identified transcription",
  "raw_headers": [],
  "raw_cells": [],
  "cell_states": "distinguish blank, zero, illegible, not_applicable",
  "household_total_as_written": null,
  "unnamed_member_relationships": null,
  "proposed_identity_links": [],
  "conflicts": [],
  "images": [],
  "source_url": ""
}
```

## Identity comparison

| Observation A | Observation B | Proposed equivalence | Independent linking evidence | Conflicting evidence | Still needed | Current status |
|---|---|---|---|---|---|---|
| | | | | | | |

Two observation labels do not assert two different people. Conversely, a repeated suffix or name does not prove one person. Preserve alternatives until the evidence distinguishes them.
