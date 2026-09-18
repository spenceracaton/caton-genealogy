# Coordinator research memo — 16 Sep 2026

**Two findings, one of them structural.** Written after a review of `BRIEF.md`,
`PARENTAGE-TESTS.md`, `NEXT-SESSION.md` and all 191 claims.

**Tooling note.** This session's egress policy blocked every record host —
archive.org (including the `be-api` full-text endpoint used on 14 Sep),
familysearch.org, loc.gov, hathitrust.org, findagrave.com, lva.virginia.gov,
ead.lib.virginia.edu, usgenwebsites.org, glorecords.blm.gov. Web *search* worked;
web *fetch* did not. So no image was opened and no record was retrieved. Finding 1
is derived entirely from claims already in this repository; finding 2 is a
record-availability survey from search snippets, graded accordingly.

---

## Finding 1 — C080 is internally inconsistent, and C080/C082/C092 cannot all be true

This is the important one. It is checkable without leaving the repo.

### 1a. C080 is anomalous on the 1820 schedule

> **CORRECTED 16 Sep, same day.** This section first said C080 was *impossible* on the
> 1820 form. Too strong — see the third resolution below. And §1d first said C080 and C082
> were the only imageless census claims in the file; that is false, and the corrected,
> narrower statement is in §1d.


C080 records the 1820 Fauquier household of Thos. Caton as:

> males under 10 = 2; 10–16 = 1; **16–18 = 1**; **16–26 = none**; 26–45 = NONE;
> 45 and up = 1. Females under 10 = 1; 26–45 = 1.

On the 1820 federal schedule **"free white males 16–18" is a subset of "16–26,"
not a separate age band** — a youth of 17 was to be tallied in both columns. This
project already knows that: C165 reads the Fairfax page correctly as
"16–18 = 1 (**a subset of 16–26**); 16–26 = 2."

So C080 as written is impossible. `16–18 = 1` with `16–26 = none` cannot both be
right. Two resolutions:

- **(i) benign** — the overlapping 16–26 mark was simply missed in transcription,
  and C080's substance stands (one adult male 45+, no man 26–45).
- **(ii) offset** — the tallies are shifted a column, in which case the
  household's *adult male composition is wrong*.

Only the image decides. And (ii) is not a hypothetical error class here: C159 had
to reconstruct the **1810** Fauquier page through an explicit one-line-down offset
argument, because that enumerator entered tallies on the ruled line *below* the
name. Same county, same clerical era, same failure mode.

**This matters because the adult-male column is the whole question.** C080 itself
raises the alternative and nobody pursued it: *"the head is 45+ with NO male
26–45, so a father of Aaron would have been at least 45 at his birth; the two
young boys may equally be GRANDSONS."* Whether a man 26–45 stood in that house is
precisely what separates "Aaron is Thomas Sr.'s son" from "Aaron is Thomas Sr.'s
grandson."

### 1b. C092 and C082 are mutually inconsistent

- **C092 (grade A, primary marriage papers):** Thomas Caton **Jr.**'s written
  consent, 6 Dec 1828 — *"I hereby consent to the intermarriage of my son William
  Caton with Ann F. Lawrey."* Thomas Jr. is **William's father**.
- **C082 (grade A):** in 1830 Fauquier, *Thomas Caton Jun* is a male **20–30** and
  *William Caton* is a male **20–30**.

A man aged 20–30 in 1830 cannot be the father of a man aged 20–30 in 1830.

**And this is not a two-claim clash.** Verified 16 Sep: the identification of 1830's
"Thomas Caton Jun" with the 1828 consent's "Thomas Caton Jr." is load-bearing in at least
five claims — C101 ("his 1820 household held four boys, two of whom are Thomas Jr. and
William"), C128, C180 ("Thomas Sr. (60–70) and Thomas Jr. (20–30) were both enumerated in
Fauquier in 1830"), C183, and C124, which makes Thomas Jr. a *son* of Thomas Sr. and so
carries the same defect. It is a structural error running through the whole Fauquier
reconstruction.

Note also that Thomas [Jr.] married **Elizabeth Lawrey on 6 Dec 1828** (C173) —
the same month, the same family, as his son William's consent. A man marrying at
the same time as his adult son is a **widower remarrying**.

### 1c. C159 and C082 are mutually inconsistent

- **C159 reading (4):** the 1820 males 10–16 and 16–18 (b. 1802–10) are *not*
  Thomas's sons — they are the second wife's sons by an earlier husband, so she
  was a widow.
- **C082:** those same two males *are* Thomas's sons, and they are the Thomas Jun
  and William who head their own Fauquier households in 1830.

Both cannot hold. C082 is the more economical reading (two Caton men of exactly
those ages, with Lawrey marriages five weeks apart in Dec 1828/Jan 1829). If C082
is right, **the "second wife was a widow with stepsons" premise collapses** — and
with it the framing that currently justifies the second-marriage-bond hunt. (The
bond is still worth finding: it names Aaron's probable mother either way.)

### 1d. The audit gap: the two load-bearing pages are the only ones not retained

Every negative Caton census claim in the Virginia belt has its image in
`evidence/`: C155 (PW 1820), C167 (PW 1830), C188 (Culpeper and Stafford 1820).
So do the Fairfax positives, C165 and C166. So does the 1810 Fauquier page (C159).

**CORRECTED.** This first read "the only census claims in the chain with an empty
`evidence` field." That is false: C057, C059, C074, C081, C090, C100, C101, C135, C143 and
C169 are imageless too. The true and narrower statement: **within the Virginia-belt
1820/1830 set, C080 (1820 Fauquier) and C082 (1830 Fauquier) are the only positives with no
retained image** — and they are the two the story rests on. C080 was "supplied"; C082 came
from a FamilySearch index search. Neither reading can be re-checked.

### 1e. What follows: a third candidate father, never evaluated

The project has been choosing between **Thomas Sr.** and **Moses**. The
contradictions above point at a man who is already documented in a grade-A claim
and has never been assessed as a candidate:

> **Thomas Caton Jr. — William's father (C092), a widower who remarried Elizabeth
> Lawrey in Dec 1828, and who appears in no Fauquier, Prince William or Fairfax
> census household that this project has correctly identified.**

What the model explains that the current one does not:

| Fact | Thomas Sr. as father | Thomas Jr. as father |
| --- | --- | --- |
| 1820 head is 45+ with no male 26–45 (C080) | father aged 45+ at Aaron's birth | boys are the head's **grandsons** — C080's own alternative |
| Aaron (10) and Joseph (7) absent from every Caton house in 1830 (C082, C166, C167) | unexplained; Sr.'s house still holds **two girls under 5** | father widowed and remarrying Dec 1828 — boys placed out |
| Both brothers became **tailors** (C076, C191, 1850) | unexplained | consistent with being bound to a trade |
| Aaron dies 1878 in Boonville among **William's** family, on the Laurie lot (C108, C149) | Aaron is William's uncle | Aaron is William's **brother** |
| William names a son **Aaron** in 1842 (C149) | named for the elder Aaron, two generations up | named for his own living brother |
| Joseph b. Fauquier July 1823 (C076) | fits | fits |

I am **not** asserting this. It is a C-level hypothesis. The point is that it is
*at least as economical* as the current leading model, it was generated by the
file's own contradictions, and the test that separates the three candidates is one
page of microfilm.

### 1f. The test

**Re-read Fauquier 1830, p.471 (C082) and the Fauquier 1820 alphabetical C page
(C080) from the reel, column by column against the printed header, and retain
both images.** Specifically:

1. **1830 p.471, "Thomas Caton Jun" — which bracket is the adult male in?** If
   **40–50**, he is Thomas Jr., William's father, newly remarried, and the leading
   candidate father for Aaron and Joseph. If **20–30**, C082 stands and there were
   three Thomas Catons in Fauquier, of whom William's father appears on no census.
2. **1820 C page — is there a male 26–45, and what is the true 16–26 count?** A man
   26–45 in that house makes the two boys under ten grandsons, not sons.
3. Confirm whether the 1830 page shows Thomas Sen's two females under 5 (a wife
   40–50 still bearing) while both sons are gone — the anomaly to be explained.

Cost: one page, twice. It is the cheapest test in the project and it sits under
everything else.

---

## Finding 2 — the untried record class: Virginia apprenticeship / Overseers of the Poor

The argument. Aaron (10) and Joseph (7) are in **no** Caton household in Fauquier,
Fairfax or Prince William in 1830 (C082, C166, C167), while small daughters remain
in Thomas Sen's house (C082). Both brothers ended in the **same trade** — Aaron a
tailor in 1850, Joseph a tailor by his own biography and the 1883 county history
(C076, C191). Two brothers gone from home at 7 and 10 and both trained to one
trade is the signature of a **bound apprenticeship**.

This class has never been searched on the Virginia side. In 191 claims the word
"overseer" appears once (C154) and unrelated; C141/C142 searched *Ohio*
indentures and closed as far as the indexes allow.

### What exists

- **Fauquier County (Va.) Board of Overseers of the Poor Minutes, 1804–1845** —
  **one volume**, Local Government Records Collection, Fauquier County Court
  Records, Library of Virginia, Richmond. Barcode **1125621**, **Fauquier County
  Reel 116**; filmed by Backstage Library Works under LVA's Circuit Court Records
  Preservation Program. The minutes "give the names of people receiving financial
  support, food, and clothing, as well as **binding children as apprentices**, and
  the burial of the deceased." Covers 1828–1836 exactly. **Grade B** (LVA finding
  aid, via search snippet — the finding aid itself was unreachable this session).
- **Virginia Auditor of Public Accounts, Overseer of the Poor Annual Reports and
  Checklists (APA 739)** — a second, independent state-level series; **Fauquier
  holdings 1829–1851**. LVA. **Grade B.**
- **Fauquier County Minute Books** survive from 1759 (microfilm and index books,
  Virginiana Room, Warrenton Library). Fauquier is *not* a lost-records county, so
  a court-ordered indenture 1823–40 should be there. **Grade B.**

### What such a record yields

Under the supervision of the County Court the Overseers indentured children to
masters to learn a trade; the entry gives **the names of the overseers, the child,
the master, the date, and the trade to be taught**. Virginia bound out orphans
*and* "children whose parents could not support them or who failed to educate or
instruct them" — so **a living father is normally named**. That is a
parent-naming record. **Grade B.**

### Two cautions, both of which save an evening

1. **Prince William is dead ground for this.** Its Overseers of the Poor minutes
   survive only for **1788–1802** (Dettingen Parish; published by Historic
   Dumfries, 1976). Prince William is an LVA **Lost Records Locality** — much
   pre-1863 material was destroyed. There is no Prince William OP volume for the
   relevant years. **Fauquier is the only candidate county where this record
   survives for 1828–36 — and it is also the county where the family demonstrably
   was in 1823–35.** That makes the test cheap and bounded. **Grade B.**
2. **Do not use LVA's "Virginia Untold: Indentures of Apprenticeship, 1777–1893."**
   It is free and indexed and it is the wrong index: Virginia Untold is LVA's
   African American narrative project, and that series covers indentures of free
   Black and mixed-race children. White apprenticeships stay in the OP minutes and
   the county court order books, **unindexed**. **Grade B.**
3. No published abstract covers the target years. The Sparacio/Heritage Books
   *Fauquier County Minute Book Abstracts* series stops in the 1780s. Reel 116
   must be read directly. **Grade B.**

### The premise this test depends on — already half-located

OP binding presupposes a **destitute or dead** father. Thomas Caton Sr. was a
taxpaying householder in 1830 with a wife and four daughters, so the theory needs
him poor. That is testable from pages **already located and never opened**: C156
reports 17 Full-Text hits for `Caton`, Fauquier, tax records, including
`Caton Thomas 2` in the 1809–19 volume and both *Thomas* and *Thomas Jr* in the
1820–32 volume — "pages not yet opened." The property columns on those pages
(horses, slaves, tax paid) say whether Thomas was poor. The same run dates when
"Thomas Jr" first appears as a separate tithable, which independently tests §1b.

Also note: a father could bind a son **privately**, by indenture recorded in the
Deed Books or Minute Books rather than by the Overseers. Search both.

---

## Finding 3 — the current top-ranked test has a window problem

`PARENTAGE-TESTS` A1 and the `NEXT-SESSION` header rank first the **Fauquier
personal-property tax 1833–1840**, to catch Thomas Caton's tithable count when
Aaron turned 16 (May 1836) and Joseph 16 (1839).

- Thomas Sr. signed Ann's marriage permission **7 Apr 1835** (C092) and the cluster
  left Fauquier for Ohio **c.1835** (C098, C189). **The years in which Aaron is a
  countable tithable are the years Thomas is gone from the county.**
- In 1833–35 Aaron is 13–15 — below the threshold, invisible by construction.
- C156's Full-Text run covered the **1800–1819 and 1820–1832** volumes. Nothing
  indicates the 1833–40 Fauquier lists are in the indexed corpus at all.

Keep it — as a **departure-dating** exercise, which is genuinely useful. It is not
the parentage test it is billed as, and it should not outrank §1f or Finding 2.

---

## Finding 4 — the Roseman clue needs re-founding before it is chased

T09 rests on the compiled middle name of **Nancy Roseman Caton** (b. 10 Nov 1849).
C017 corroborates a Nancy born c. Nov 1849 from the 1850 census — **the census
gives only "Nancy."** The middle name's only support is compiled (the WikiTree
GEDCOM family of C072). Two points:

- **Roseman is not a Virginia Piedmont surname.** It is an Americanised German
  (Rosemann/Rosmann) and Ashkenazi name, historically concentrated in Pennsylvania
  and North Carolina. If the middle name is genuine *and* is a surname, it points
  away from Fauquier and — weakly — toward the Pennsylvania/Maryland Kitten line
  of story B, which is the opposite of how T09 is currently framed. **Grade C**
  (surname-reference sites).
- It may not be a surname at all. **"Roseman" may be Rosamond / Rosanna**, a
  female given name, in which case the natural reading is a granddaughter named
  for a grandmother — and the target becomes the forename Rosanna/Rosamond among
  Caton women of the Fauquier–Prince William belt, not a Roseman family. Note
  **Rosana Caton**, Reading Twp, Perry Co., Ohio, 1840 (C174), dismissed on other
  grounds but bearing exactly that name. **Grade C, hypothesis only.**

**So T09 step 1 should be: fix the middle name from a primary record**, not find
the family. New lead for that, and for the family's chronology:

- **Nancy Roseman Caton, d. 5 Dec 1865, Ohio**, aged 16 — compiled, **grade C**,
  but a specific day-month-year is the signature of a stone or a bible. If true it
  is new to this project, and it bears on §3 of the brief: a daughter dying in
  **Ohio** in Dec 1865, with Sarah Ann also reported dying in Ohio in 1886 (C072),
  says the family **split** — Aaron to Missouri, Sarah and children left in Ohio.
  That would explain the 1870 Boonville household with "no wife present." Test:
  Delaware Co., Ohio cemetery and probate 1865–66, and Ohio death records.

---

## Recommended order

1. **Re-read Fauquier 1830 p.471 and Fauquier 1820 C page from the reel; retain
   both images.** (§1f) Resolves three contradictions and decides among three
   candidate fathers. Cheapest test in the project.
2. **Open the Fauquier tax pages already located in C156** (1809–19 and 1820–32
   volumes, 17 hits, never opened). Dates Thomas Jr.'s emergence as a separate
   tithable; reads Thomas's property level, which is the premise of Finding 2.
3. **Fauquier Overseers of the Poor Minutes 1804–1845, LVA reel 116** — read
   1826–1838 for a Caton binding. (Finding 2) The only untried class that both
   explains the 1830 absence and names a parent. Then Fauquier Minute Books and
   Deed Books 1823–40 for a private indenture, and APA 739 (Fauquier 1829–51).
4. **Full-Text `Caton`, Fauquier, 1823–1840, all record types, filters cleared** —
   never run. C156 was filtered to tax records; C153's addendum was the phrase
   `"Aaron Caton"`. This is the cheap way to reach an apprenticeship order if the
   volume is in the digitised corpus.
5. Second-marriage bond (Prince William register 1794–1850, then Fairfax,
   Stafford, Culpeper 1816–19) — unchanged in value, but note §1c: the "widow with
   stepsons" framing may be wrong even though the bond still names the mother.
6. Fauquier personal-property tax 1833–1840 — **demoted**, as a departure-dating
   exercise. (Finding 3)
7. T09 — **re-pointed**: verify the middle name first. (Finding 4)

## Proposed downgrade

**C080 and C082 should be marked provisional (B) until their images are in
`evidence/`.** C080 is internally inconsistent with the 1820 form (§1a); C082
contradicts grade-A C092 (§1b). Both are currently graded A and neither can be
re-checked. The repo's own merge rule covers this case: *"where the cell is
damaged, blotted, or split by a page break … go to the image."*
