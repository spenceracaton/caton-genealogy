# S01 — Resolve the Fauquier Thomas identities

**For:** a ChatGPT research agent with a FamilySearch sign-in. **Prepared:** 18 Sep 2026. **Coordinator:** Spencer Caton via Claude Code.

**Target of every stream:** Aaron Caton, b. 16 May 1820, Virginia; m. Sarah Ann Gardner, Delaware Co., Ohio, Aug 1841; tailor; d. Boonville, Mo., 17 Jan 1878. Parents unknown. Nothing in this file is a proved relationship.

## Question

Which Fauquier records concern the same Thomas Caton and which concern different men? Specifically: is William's consenting father (Thomas Caton Jr., 6 Dec 1828, C092) the same man as the 1830 census head "Thomas Caton Jun" read as 20–30 (C082), the 1810/1820 household head, or the 6 Dec 1828 groom of Elizabeth Lawrey (C173)? A man 20–30 cannot father a man 20–30 (C193). Either the 1830 bracket is misread or a third adult Thomas existed. This is the repo's §0 test; everything Fauquier sits on it.

Use observation labels, not a tree: `TH-FQ1810`, `TH-FQ1820`, `TH-FQ1830-SEN`, `TH-FQ1830-JUN`, `TH-CONSENT1828`, `TH-GROOM1828`, `TH-CONSENT1835`, `TH-TAX1836`, `TH-TAX1837a`, `TH-TAX1837b`. Labels do not assert distinct men.

## What is already in hand — do not re-acquire

- Marriage-bond typescripts, both packets, image-verified 15 Sep: `evidence/2026-09-15_T17_fauquier-marriage-bonds_Jr-Sr-reread.md` and the four `2026-09-15_Fauquier_MarriageBonds_*` images. Volumes 1–6 are 1933 typed transcripts; the FS catalog (koha:363669) says **volume 7 is the original-record volume**. The `Jr`/`Senr` suffixes are typeset, not autograph.
- Fauquier personal-property tax 1836–1839 (film 2024534, DGS 007849111): `evidence/2026-09-15_T18_fauquier-tax_Cayton-1836-1839.md`. 1836 img 192: `Cayton Thomas`, `Cayton William`. 1837 img 263: `Cayton Thomas`, `Cayton William`, `Cayton Thos.` — three rows. 1838–39: none. **This contradicts C196's premise that Thomas left after Apr 1835** and shows two adult Thomases taxed in 1837.
- 1810 and 1820 published transcriptions checked 18 Sep (derivative only): 1810 Thomas p. 263B line 11, handwritten p. 398, M252 roll 68 — 1 male 45+, 1 female 16–26, 1 female 45+. 1820 Thomas p. 46, after William Cockrill, M33 roll 136 — two males under 10, no male 26–45, and the anomalous `16–18 = 1; 16–26 = none`. Preserve the anomaly; do not repair it.
- The 1830 online transcription (us-census.org, Fauquier 1830) omits p. 471. No county negative is justified from it.

## Sequence

1. **Fauquier 1830, p. 471 — the decisive page.** FamilySearch "United States Census, 1830" images (NARA M19; Virginia, Fauquier). Establish the roll from the viewer; do not trust a remembered roll number. Retain the full names/ages page, the printed column header, all three Caton rows, the rows above and below, and the facing continuation if the age columns run across two pages. Read, column by column against the header: the adult-male bracket of `Thomas Caton Jun`; every male column of both Thomas households; the female columns of the older household (C082 reports two females under 5 with a wife 40–50). Offset error is real in this county (C159 reconstructed the 1810 page by a one-line-down argument), so check row alignment against neighbours. On the stated birthdates Aaron is 10 and Joseph 6 on 1 Jun 1830 — they belong in 10–14 and 5–9; do not call Joseph seven.
2. **Retain the 1810 and 1820 manuscripts.** Same collection routes for M252 roll 68 (p. 398) and M33 roll 136 (p. 46). Read against the actual printed headings and neighbouring rows.
3. **Open C156's seventeen tax hits.** FamilySearch Full-Text Search, keyword `Caton`, place Fauquier, record type tax. Never opened. Retain every hit page with its year/title header. Needed: `Caton Thomas 2` in the 1809–1819 volume (two tithables — when does it start?); `Thomas` and `Thomas Jr` in the 1820–1832 volume (first year `Jr` appears as a separate tithable). Then fill 1833–1835 from DGS 007849111 (the 1836–39 images exist). Two tithables do not identify two sons; a first appearance does not prove a young man just came of age.
4. **Check volume 7 for the loose originals.** FS catalog koha:363669, Fauquier marriage bonds and returns 1759–1854. If volume 7 holds the 1828–29 or 1835 originals, retain them: the only way a `Jr`/`Senr` suffix becomes autograph evidence.

## Analysis

One row per observation: exact name and suffix, date, locality, age data, spouse named, children named, occupation, associates, original/copy status, locator, competing identities. Then one row per proposed equivalence with evidence for and against. Keep a conflicting age visible even when other features match.

## Pre-registered outcomes

- `TH-FQ1830-JUN` adult male reads **40–50** → C082 was an adjacent-column slip; the man is compatible with William's father (C194 stays C — this does not prove it). 
- Reads **20–30** → C082 stands; William's father heads no identified 1830 household; the 1837 `Thos.` row becomes the leading locator for him.
- 1820 shows a male 26–45 → the two boys under 10 may be grandsons; do not make them sons or grandsons by default.
- 1810 and 1820 heads prove distinct → the wife/mother reconstruction (C159) must be rebuilt, not patched.

## Boundaries

You own Fauquier census, tax, and marriage originals. S03 owns Missouri Thomases; S08 owns wife/Lawrey kinship; S04 owns the elder Aaron. Return an identity matrix, not a genealogy. Fewer unsupported equivalences is success whether or not Thomas gets stronger. Stop after one bounded access session per item; a page that will not load is `blocked` with its route.

## Locators

- FS 1830 census collection: https://www.familysearch.org/search/collection/1803958
- FS 1820 census collection: https://www.familysearch.org/search/collection/1803955 · 1810: https://www.familysearch.org/search/collection/1803765
- Fauquier tax 1833–1845, DGS 007849111: https://www.familysearch.org/ark:/61903/3:1:3Q9M-CSQK-TS8S-R?view=explore
- Marriage packets: https://www.familysearch.org/ark:/61903/3:1:3QS7-89XF-K9SG-S?view=fullText (v4 img 149) · https://www.familysearch.org/ark:/61903/3:1:3QS7-L9XF-K9SX-V?view=fullText (v5 img 45)
- 1810 transcription: https://www.us-census.org/pub/usgenweb/census/va/fauquier/1810/pg0262a.txt · 1820: https://www.us-census.org/pub/usgenweb/census/va/fauquier/1820/pg0039.txt · 1830 (partial): https://www.us-census.org/pub/usgenweb/census/va/fauquier/1830/
- LVA Fauquier microfilm inventory: https://www.lva.virginia.gov/collections/ccmf/VA/VA083

## Repository, rules, and what to return

**Repo:** https://github.com/spenceracaton/caton-genealogy (private). Branch from `main`.

**Read first, in order:** `BRIEF.md`, `METHOD.md`, `tasks/README.md`, then only the evidence files named in this handoff. Do not load `archive/`, other `tasks/T*.md`, or other handoffs.

**Precondition:** confirm `evidence/2026-09-15_T24_pension-card.md` exists on `main`. If it does not, the coordinator has not pushed the 15 Sep evidence set. Stop and report `blocked: main is stale`. Do not proceed.

**Namespace.** Claude Code writes `C###`. ChatGPT writes `G###`. Never write a `C` id. For this pass do not allocate `G` numbers either: write `G-PENDING` and the coordinator assigns on merge (several agents run concurrently and the local branch already holds G001–G019). Every proposed claim carries `kind` ∈ {fact, hypothesis, negative, do-not-merge, method, moot, void} and `grade` ∈ {A, B, C}. A is primary/near-primary; B is strong identified secondary; C is a lead. Ungraded = C.

**Write exactly one new file** `evidence/2026-09-DD_<STREAM>_<slug>.md`, plus retained images as `evidence/2026-09-DD_<STREAM>_<description>.jpg|png|pdf`. Full page plus crop for every image-based reading. Nothing else. Do not edit `BRIEF.md`, `claims.jsonl`, `PARENTAGE-TESTS.md`, `NEXT-SESSION.md`, `tasks/*`, or any existing evidence file. Do not append to `claims.jsonl`; put proposed claims in the evidence file.

**PR.** Branch `chatgpt/<STREAM>-<slug>`. Title `<STREAM> <status>: <one line>`. Body = the return block below, verbatim from the evidence file. One PR per stream. Touch `evidence/` only.

**Conduct.** Do not send email, submit forms, order records, pay fees, or recommend DNA. Any message you draft is labelled `UNSENT DRAFT` and left for Spencer. Do not put restricted archival scans, private correspondence, or living persons' details in the repo. A page that will not load is `blocked` with the exact route tried, not `not-found`. Do not repeat a search recorded in `claims.jsonl` or `searches.jsonl` unless this handoff names a new variant, window, or record class. Read a census cell without first deciding which answer helps; treat blank, zero, and illegible as three different states. Transcribe verbatim; use `[illegible]`; do not silently repair. A transcription outranks a low-resolution image reading except where the cell is damaged, blotted, or split by a page break — there go to the image and prefer an independent second record.

**Return block** (top of the evidence file and the PR body):

```text
STREAM:
STATUS: found | not-found | partial | blocked
QUESTION TESTED:
RECORD: repository / collection / book / page / image — stable URL
DATES: event | execution | acknowledgment or recording | retrieved
SOURCE FORM: original | contemporary copy | later typescript | abstract | index | compilation
IMAGES RETAINED: paths, or the rights/access reason none were
TRANSCRIPTION: verbatim
STATES DIRECTLY:
INFERRED:
SOURCE GRADE: A|B|C — reason
INFERENCE GRADE: A|B|C — reason
IDENTITY MATCH: evidence for / against; competing same-name person
CONFLICTS: claim id — exact difference
WHAT WOULD WEAKEN THIS:
NEXT DISCRIMINATING RECORD:
NEGATIVES: one line each — source | jurisdiction | dates covered | pages or images read | variants tested | control hit proving the search worked | gaps
PROPOSED CLAIMS: one JSON row each — {"id":"G-PENDING","person":"","fact":"","date":"","place":"","grade":"","kind":"","source":"","url":"","evidence":""}
```
