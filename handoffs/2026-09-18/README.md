# Investigative streams S01–S08 — review, priority, and agent handoffs

**Reviewed:** 18 September 2026, against the package `Caton_Investigative_Streams_2026-09-18.zip` (8 stream briefs, coordination note, source register, return template) and the repository at `origin/main` (8af46cc, 16 Sep, C197) plus the local unpushed branch (a7f1c55).

## Verdict

The package is legitimate. It contains no new evidence and claims none. It correctly retracts three earlier overstatements (the Thomas Jr./Jun merger, the "convincingly separated" 1828 groom, the pension-card inference in C184), maps onto the repo's own ranking in `PARENTAGE-TESTS.md` §0/A1/A2/A3/A5/A8, respects the C/G namespace and evidence-file-only rule, and pre-registers kill conditions per stream. It should be used.

Its one defect is staleness: it was built against `origin/main`, which does not carry the 15 Sep evidence set sitting in the local unpushed commit `a7f1c55` (≈95 files). Several stream "first acquisitions" are already done there:

| Already retrieved locally (not on GitHub) | Stream that assumes it is not |
|---|---|
| T288 pension card image, read: `Caten, Aaron`, Co. C 3rd Mo. Cav., invalid app. 233783, filed 12 Jun 1876 (`evidence/2026-09-15_T24_pension-card.md`) | S05 step 1 |
| Both marriage-bond typescript images, v4 img 149 and v5 img 45 (`evidence/2026-09-15_T17_…`) | S01 step 3, S08 step 1 |
| Rappahannock Deed Book A img 192: 8 Apr 1834 White→Thorn reciting "Aaron Caton Decd was Trustee"; earlier deed date illegible (`evidence/2026-09-15_T15_rappahannock-deedbookA_…`) | S04 step 1 |
| Fauquier personal-property tax 1836–1839 C-pages: `Cayton Thomas` + `Cayton William` 1836; `Cayton Thomas`, `Cayton William`, `Cayton Thos.` 1837; none 1838–39 (`evidence/2026-09-15_T18_…`) | S01 step 4; contradicts C196's "gone after Apr 1835" |
| Boulder catalog: both 1932 objects return HTTP 403; diaries 279-1-1 inscribed by Joseph 1888 (`evidence/2026-09-15_T27_…`) | S06 step 2 |
| Delaware Co. 1835–38 bounded pass, no hit (`evidence/2026-09-15_T28_…`) | S07 step 3 |
| 1840 Cooper p.145 N. Laurie household, no male 70–80 (`evidence/2026-09-15_1840_cooper_laurie_household_check.md`) | S03 |

**Precondition before any agent is dispatched:** resolve the in-progress merge in the local repo (`BRIEF.md`, `NEXT-SESSION.md`, `PARENTAGE-TESTS.md`, `README.md`, `claims-index.md`, `claims.jsonl`, `evidence/README.md`, `tools/check-claims.py` are all `UU`), then push. Each handoff file tells the agent to verify `evidence/2026-09-15_T24_pension-card.md` exists on `main` and to stop if it does not.

## Priority

Ordered by (chance the record exists) × (what it proves) ÷ (agent effort). "Agent-doable" means a ChatGPT agent with FamilySearch sign-in can finish the first pass without Spencer sending mail or paying.

| Rank | Stream | Pursue | Why | Agent-doable first pass |
|---|---|---|---|---|
| 1 | S01 Thomas identities | Yes | Repo's own §0; every other Fauquier inference sits on the unretained 1830 p.471 and 1820 readings; C156's 17 tax hits never opened; 1837 tax shows two Thomases still present | Yes — census images, tax pages, FS catalog for original bond volume |
| 2 | S03 Boonville tailor, 77 | Yes | Only elderly Virginia-born tailor Thomas in the record, in the town Aaron died in; fully testable from 1850/1860 images, Cooper probate, Maddex household | Yes |
| 3 | S02 Apprenticeship / Overseers of the Poor | Yes, bounded | Only record class that names a living father outright; Reel 116 is film-only, so the agent's job is to find a digitised copy, run the never-run Full-Text sweep, and hand Spencer a precise request | Partly — register read needs film or a Gott contact |
| 4 | S05 Aaron's own records | Yes, bounded | Independent of the Fauquier model; the card is already read and contradicts C184 — one cheap discriminator (T289 organisation index, both units) settles it; widow's card never searched | Yes for index work; NARA orders and Poulin contact are Spencer's |
| 5 | S06 Joseph / Dumm | Yes, bounded | The 1898 niece notice has no retained citation; recovering it is a one-newspaper job. Boulder reply is Spencer's inbox, not an agent task | Yes for the notice; no for Boulder |
| 6 | S04 Older Aaron control | Yes, small | Deed already retrieved; the remaining question is the recited trust deed (Culpeper before 1833) and a death interval. One Full-Text pass. Park if it names no kin | Yes |
| 7 | S07 Ohio bridge | Defer | Explains route, unlikely to name a parent; T28 already ran the 1835–38 pass; the only new class is the unindexed appearance dockets (DGS 7710150). Run after S01/S03 return a named associate | — |
| 8 | S08 Women / Lawrey | Defer | Almost entirely re-analysis of packets already in hand plus one SHSMO request (C4669 folder 2) that Spencer must send. Coordinator task, not an agent task | — |

Run three at a time with disjoint repositories, per `tasks/README.md`: **S01 + S03 + S05** first; **S02 + S06 + S04** second.

## Handoff files

One per stream, self-contained, written for a ChatGPT agent that will open a PR against `main`:

- `S01_thomas-identities.md`
- `S02_virginia-childhood-records.md`
- `S03_boonville-thomas.md`
- `S04_older-aaron-control.md`
- `S05_aaron-personal-records.md`
- `S06_joseph-and-dumm.md`

Two deliberate deviations from `tasks/README.md`, stated in every file:

1. **Agents do not allocate G ids.** Six agents allocating G### concurrently will collide, and the local branch already holds G001–G019. Agents write `G-PENDING`; the coordinator assigns on merge.
2. **Agents do not append to `claims.jsonl`.** Proposed claims go in a "Proposed claims" section of the evidence file. The PR touches `evidence/` only.

## Source register carried over

The package's `09_SOURCE_REGISTER.md` (A1–A23) is the locator authority for these handoffs. Relevant locators are copied into each file so the agent needs nothing from the zip.
