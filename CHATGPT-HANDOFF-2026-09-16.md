# Caton Genealogy — handoff to the ChatGPT thread
**From the Claude Code session · 16 Sep 2026 · claims C192–C197 · branch `claude/aarons-parents-research-g8ihkp`**

Read `BRIEF.md`, then `evidence/C192-C197_1820-1830_Fauquier_recheck_and_apprenticeship_2026-09-16.md`,
then the revised `PARENTAGE-TESTS.md` and `NEXT-SESSION.md`. Everything below is already in
the repo; this file only says what is yours to pursue and what is not.

**You allocate `G###` ids. Never write `C###`.** Do not edit `BRIEF.md`, `claims.jsonl`, or
task frontmatter — write findings to a new file under `evidence/` and let the Claude session
merge. Grade every claim A/B/C; an ungraded claim is treated as C.

**Schema change, 16 Sep 2026 — every claim now needs a `kind`.** One of `fact` ·
`hypothesis` · `negative` · `do-not-merge` · `method` · `moot` · `void`, alongside `grade`.
`tools/check-claims.py` fails the commit without it. Include it in the claims you return so
the merge session does not have to guess. It replaces classification-by-prose, which read
the first words of a claim's text and silently reclassified on a reword — see `METHOD.md`
§1. And note **`person` is a subject, not a category**: categories belong in `kind`.

**`METHOD.md` at the repo root is new** and is the canonical home for operational rules —
what to verify, what this project cannot reach, and how it has misled itself before. Read
it before your first edit.

---

## Why this pass is being handed over

**No record was retrieved.** The Claude sandbox's egress policy blocked every record host —
archive.org (including the `be-api` full-text endpoint that worked on 14 Sep), FamilySearch,
loc.gov, HathiTrust, Find a Grave, lva.virginia.gov, ead.lib.virginia.edu, usgenwebsites.org,
glorecords.blm.gov. Web *search* worked; web *fetch* did not.

**If you can reach those hosts, that is the entire reason this is yours.** Findings 1 and 3
in the memo are derived from the repo's own claims and need nothing external. Finding 2 is a
record-survival survey built from search snippets and is graded B for exactly that reason.

## What changed, in one paragraph

C092 (grade A, primary marriage papers) makes **Thomas Caton Jr.** William's father, while
C082 reads both men 20–30 in 1830 — a man 20–30 cannot father a man 20–30. That
identification is load-bearing in **C101, C124, C128, C180 and C183**, so it is a structural
error in the Fauquier reconstruction, not one slip. **C080 and C082 are consequently graded
down A → B**; neither has a retained image. A third candidate father follows (**C194**,
Thomas Jr.) but is **C-level and pre-registered with a kill condition** — it dies if Fauquier
1830 p.471 reads the adult male as 20–30. The former top-ranked test (Fauquier tax 1833–40)
is demoted: Aaron turned 16 in May 1836 and Thomas left the county after Apr 1835, so the
decisive years are the years he is absent (**C196**).

## Yours to pursue, in order — all of it blocked to Claude

1. **Open the LVA finding aid** (`ead.lib.virginia.edu/vivaxtf/view?docId=lva/vi02514.xml`)
   and transcribe it verbatim. C195 rests on snippets; confirm or correct the reel number
   (116), barcode (1125621), the 1804–1845 span, and the "binding children as apprentices"
   wording. Same for **APA 739** (`lva/vi04679`), Fauquier holdings 1829–51.
2. **Find whether that volume exists anywhere but LVA reel 116** — a FamilySearch film/DGS
   number, a digitised copy, any online scan. **Highest-value question you can answer.** If
   FamilySearch filmed it, Spencer reads it tonight instead of ordering film.
3. **Open `usgenwebsites.org/vagenweb/fauquier/poorhouse.html`** — free, blocked to Claude.
   Any transcribed names? Any Caton / Caten / Cayton / Katon?
4. **archive.org full-text API sweep** (it worked for you on 14 Sep): `Caton` in any Fauquier
   Overseers-of-the-Poor or apprentice abstract; the Fauquier Historical Society / AAHA
   "Fauquier tithables" series for 1833–40; `"Caton Branch"`; `"Thomas Caton" Fauquier`.
5. **Prince William Reliquary (RELIC) cumulative index for `Caton`** — listed as untried in
   `PARENTAGE-TESTS.md` §C and still untried.
6. **The family-split hypothesis (T03, new 16 Sep).** Compiled: Nancy Roseman Caton d.
   **5 Dec 1865, Ohio**, aged 16; Sarah Ann d. **abt 19 Oct 1886, Ohio** (C072). If both hold,
   Sarah and at least one child stayed in Ohio while Aaron went to Missouri — which would
   explain the wifeless June 1870 Boonville household without a death, and would revise
   BRIEF §3. Cheapest test of the whole thing: **the 1870 census for Sarah A. Caton in
   Delaware Co., Ohio — never searched.** Then Powell Cemetery and other Delaware Co. burials
   for a Nancy Caton d. Dec 1865 (a stone also fixes her middle name and closes T09 step 1).

## Do not

- **Do not use LVA's "Virginia Untold: Indentures of Apprenticeship, 1777–1893"** (free,
  indexed, and the wrong index — it is LVA's African American narrative project and covers
  free Black and mixed-race children only, C195).
- **Do not chase a Roseman family** before the middle name is fixed from a primary record.
  The 1850 census gives only "Nancy" (C017). Note Roseman is a German/Ashkenazi surname of
  Pennsylvania and North Carolina, absent from the Virginia Piedmont — if it *is* a surname it
  points at story B — and it may simply be **Rosamond/Rosanna**, a forename.
- **Do not promote C194** past C on reasoning alone. It is a pre-registered prediction; record
  the 1830 bracket **either way**, including if it kills the hypothesis. (Precedent: C081 was
  an explicit prediction, it failed, and it is marked `PREDICTION FAILED` / VOID. That is the
  pattern to follow.)
- **Do not re-run** anything in the `Closed (do not repeat)` list at the foot of
  `PARENTAGE-TESTS.md`.

## Leave for Spencer's FamilySearch login — don't duplicate

- Re-reading **Fauquier 1830 p.471** and the **Fauquier 1820 alphabetical C page** from the
  reel, retaining both images. This is item 1 in `NEXT-SESSION.md` and it outranks everything.
- Opening **C156's 17 already-located Fauquier tax hits** (never opened) — they test whether
  Thomas was poor, which is the premise of the apprenticeship theory.
- **Full-Text `Caton`, Fauquier, 1823–1840, all record types, filters cleared** — never run.

## Calibration note, offered in good faith

The Claude session overstated two things in this pass and had to retract both: it called
C080's `16–18 = 1; 16–26 = none` *impossible* on the 1820 form when uneven enumerator
compliance makes it merely anomalous, and it claimed C080/C082 were the only imageless census
claims in the file when ten others are. Both errors leaned toward its own conclusion. Treat
C194, C195 and C197 with that in mind — the reasoning may be good and the confidence was not
earned. Contradict any of it if the records say otherwise; that is the point of two writers.
