## THREAD 1 — Fauquier apprenticeship, guardianship, and childhood-placement records

### Shared execution and evidence rules

This revised prompt governs the assignment; older handoffs supply locators and prior findings, not authority to restore superseded conclusions or widen scope. Read `evidence/2026-09-24_parentage-strategy-review.md`, `DATA_MODEL.md`, `CATON_CENSUS_LEDGER.md`, and the files listed below. Check `claims.jsonl`, `sources.jsonl`, `searches.jsonl`, and `discrepancies.jsonl` for the specific target. Do not repeat completed searches without a new source, coverage gap, variant, or reason.

The reported birth date is 16 May 1820; preserve the service-card age conflict (C023, approximately 1817) and search plausible age variation. Exact age agreement is not mandatory for identity; a same-name match alone is insufficient. No DNA.

Separate source quality, information quality, identity, and relationship inference. A primary document can contain uncertain ages or hearsay. Record dates of execution, recording, and later transcription separately. Distinguish father/mother from guardian, master, surety, creditor, and administrator. The latter roles do not establish parentage or parental death.

Use at most two sub-agents for independent, bounded sources when useful; do not recursively fan out. Faster agents may locate records and make preliminary transcriptions. The lead verifies every identity-critical name, suffix, age, and relationship against the image, using retained high-resolution crops. Give each worker exclusive output/source ownership; workers are not alone in the repository and must not revert others' edits. Avoid simultaneous control of one authenticated browser session. Finish the narrow task before widening it.

Write one new dated evidence note per stream and retain permitted source images and crops. Propose claims as `G-PENDING` in that note; do not allocate IDs, edit canonical claims/brief/tasks, or alter another stream's evidence. Protect dirty shared checkouts with an isolated worktree if needed. Creating or publishing PRs is outside this research assignment unless separately requested.

Do not send messages, submit forms, order records, or incur fees. Where acquisition is required, return the precise repository/item/page or scope and an UNSENT DRAFT if useful. A documented access barrier is a blocked result, not evidence of absence. Do not continue catalog hunting after the surviving source and acquisition route are established unless there is a specific untested route.

For negatives record repository, collection, actual dates/pages examined, variants, index versus manuscript coverage, a control showing the search function worked where applicable, and all gaps. Do not infer absence from OCR alone. Conclude with the single record most likely to discriminate between surviving explanations, and state what result would weaken your favored identification.

You are the lead research agent on one tightly scoped genealogy problem.

### Objective

Find a record from Aaron Caton’s childhood or adolescence that names his father, mother, guardian, master, or close family relationship.

Target:

- Aaron Caton
- born 16 May 1820, Virginia
- married Sarah Ann Gardner, Delaware County, Ohio, August 1841
- occupation: tailor
- later Missouri
- parents unknown

This is documentary research only. Do not use DNA.

### Current state

The leading hypothesis is that Aaron belonged to the Fauquier / Prince William Caton family and may have been a son of the older Thomas Caton of Fauquier County, but this is NOT proved.

Important evidence:

- Thomas Caton’s 1820 Fauquier household contained two males under 10. Aaron fits one slot, but nobody is named.
- The reviewed 1830 Caton-headed households in these counties do not supply an identified placement for Aaron or Joseph. Pre-1850 tallies do not name them; do not call them identified missing sons.
- Joseph Caton, born 1823 Virginia and possibly related to Aaron, is a separate search target. His relationship to Aaron remains unproved.
- Aaron and Joseph both became tailors.
- Fauquier County Board of Overseers of the Poor Minutes survive for 1804–1845, LVA Reel 116, barcode 1125621.
- Fauquier County Court Minute Books cover the relevant period.
- Private apprenticeship indentures may also appear in deeds or court orders.
- The project has located no Prince William Overseers minute series covering the relevant years. That record-series gap does not establish that all childhood-placement evidence there is lost.

Repo:
https://github.com/spenceracaton/caton-genealogy

Read BRIEF.md, METHOD.md, tasks/README.md, and handoffs/2026-09-18/S02_virginia-childhood-records.md before researching. Check claims/search logs so you do not unknowingly repeat completed work.

### Research strategy

Your highest-value target is an apprenticeship, guardianship, poor-relief, or court entry naming Aaron directly.

Do NOT require proof that Thomas was poor before pursuing Overseers records. The direct record has much higher evidentiary value than a tax-property proxy.

Work in this order:

1. Run one bounded FamilySearch Full-Text locator pass across ALL Fauquier record types, 1820–1841; verify actual document dates. Search surname-only variants before adding terms, since restrictive combinations can miss terse entries:
   - Caton
   - Caten
   - Cayton
   - Catton
   - Katon
   - Aaron with surname variants
   - combinations with apprentice, bound, indenture, orphan, guardian, poor, overseer, tailor

2. Determine the usable access route to Fauquier Overseers of the Poor Minutes, Reel 116. This is the main manuscript target, not merely a catalog-discovery task. If accessible, read 1826–1838 first, with an explicit page coverage log. Record 1820–1825 and 1839–1841 as unexamined until reviewed; extend to those periods if the first pass is negative and access permits. Check plausible alternate copies through:
   - FamilySearch
   - Library of Virginia
   - Internet Archive
   - published abstracts
   - Gott Library / Fauquier historical resources
   - other legitimate repositories

3. Search Fauquier County Court Minute / Order Books, especially 1826–1838, for:
   - Aaron or surname variants
   - children being bound out
   - guardianship appointments
   - apprenticeship releases/reassignments
   - references to Thomas Caton’s children

4. Search relevant deed books for privately recorded apprenticeship indentures.

5. Check John K. Gott’s guardian-bond work and follow relevant entries to originals. The existing S02 handoff also identifies loose fiduciary papers (vi05624) and APA 739 poor-board reports. Use these to follow a named child, guardian, or master or fill a defined gap; do not launch unrestricted box searches.


### Evidence standard

A negative search is only useful if you record:
- repository
- collection/book
- date span actually examined
- surname variants
- pages/images/index range
- access limitations

An index hit is not proof. Open the underlying record whenever possible.

For every important record, capture:
- exact transcription
- date
- volume/page/image
- stable URL
- original vs abstract/index
- people named
- relationship actually stated
- competing identity explanation

### Success criteria

Best outcome:
A contemporary record explicitly naming Aaron’s father or mother.

Very strong outcome:
An apprenticeship or guardianship explicitly identifying a parent, with enough identity evidence to link the child to the adult Aaron. Thomas appearing only as master, guardian, or surety is an association, not fatherhood.

Useful outcome:
A record giving Aaron’s exact age/birth date, guardian, master, trade, or prior residence that materially narrows his family.

Negative outcome:
A genuinely exhaustive, well-documented search of a high-value surviving record set.

Do not turn circumstantial compatibility into parentage.

At the end, report:

1. HEADLINE RESULT
2. RECORDS FOUND
3. WHAT THEY STATE DIRECTLY
4. WHAT CAN BE INFERRED
5. WHAT REMAINS UNPROVED
6. NEGATIVE SEARCHES
7. NEXT SINGLE HIGHEST-LEVERAGE RECORD
8. Any repo-ready evidence notes or proposed claims
