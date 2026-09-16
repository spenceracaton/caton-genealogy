# METHOD — operational rules for agents on this project

**This file is about how to work, not about the Catons.** Genealogical evidence lives in
`claims.jsonl`; the research plan lives in `BRIEF.md`, `PARENTAGE-TESTS.md` and `tasks/`.
Everything here is a rule that already cost this project a pass.

**It is the single canonical home for these rules.** `BRIEF.md` §9 and `tasks/README.md`
point here rather than restating, because three copies of a rule become three different
rules — which is the failure C117 records.

---

## 1. Verify the effect, not the invocation

Every entry in this section produced a **false report**, not a visible error. That is what
makes the class dangerous: the tool succeeds at doing nothing.

**An unverified string replacement is a silent failure, and a printed "ok" is not
evidence.** `str.replace` returns the string unchanged on a miss and raises nothing, so a
script that prints its own success message will report an edit it never made. On 16 Sep
2026 three replacements against `PARENTAGE-TESTS.md` no-matched on a one-word line-wrap
difference; the file was written back identical, and Spencer was told two retractions had
been applied everywhere when one whole file still carried both. It was caught only because
the harness happened to display the file's real text afterwards.

- Assert the pattern is present **before** replacing: `assert old in s, old[:120]`.
- Assert the result is present **after** writing; re-read the file.
- Never print a success message that is not conditional on the edit having landed.
- Check `git diff --stat` against what you expected to change. **A file missing from the
  diff, or a suspiciously small line count, is the signature.**

**`grep` in Spencer's shell silently skips ISO-8859 files (C036).** It wraps `ugrep -I`,
which classifies the USGenWeb transcriptions in `evidence/` as binary: empty output, exit
1, indistinguishable from a genuine no-match. Two findings were nearly recorded from this.

- Use `command grep -a` on anything in `evidence/`.
- Verify any such search with a control term **known to be present**.

**Run `python3 tools/check-claims.py` before every commit.** It catches duplicate ids,
missing grades, and `evidence:` paths that do not exist.

**Do not prefix a claim's `fact` with `REVERSED`, `SUPERSEDED`, `DOWNGRADED`, `WRONG, SEE`,
`EXCLUSION WITHDRAWN`, `PREDICTION FAILED` or `VOID` unless you mean it.**
`tools/make-claims-index.py` matches those words at the start of the text and classifies
the claim VOID/REVERSED. To mark a claim provisional rather than dead, use
`[PROVISIONAL …]` — as C080 and C082 now do.

## 2. Say the narrowest thing that is true

On 16 Sep 2026 this project's Claude session overstated twice in one pass, **both times in
the direction of its own new finding**, and both errors reached `BRIEF.md` before being
caught. It called an anomalous 1820 census reading *impossible* when uneven enumerator
compliance explains it, and it claimed two claims were *the only* imageless census claims
in the file when ten others are. Neither strong form was needed; the narrow versions were
already decisive.

- **If a finding needs "only", "never", "impossible", "all" or "every" to land, test that
  word against the file with a script before writing it.** These are cheap to check and
  expensive to retract.
- **Grade reasoning and citation separately.** An argument can be sound while its
  bibliographic detail is unverified — C195's case for the apprenticeship record is good,
  but its reel number and barcode came from search snippets, not the finding aid.
  Conflating the two would have sent Spencer to Richmond on an unchecked citation.
- **Pre-register the kill condition for a hypothesis you generated**, in writing, before
  the record is read. A hypothesis an agent produced is the one it will be least able to
  read fairly. C194 carries "it dies if the 1830 bracket reads 20–30" for this reason.
  Precedent that it works: C081 was an explicit prediction, it failed, and it is marked
  `PREDICTION FAILED` / VOID rather than quietly reinterpreted.
- **Correct in place, visibly.** A retraction rewritten into silence is worse than the
  error. C192 quotes its own false statement in order to retract it.

## 3. Know what you can actually reach before you promise it

**Egress policy is per-session, and it can be total.** On 16 Sep 2026 an agent could reach
**no** genealogical host at all: archive.org *and* `be-api.us.archive.org` (the full-text
API that carried the entire 14 Sep pass), FamilySearch, Chronicling America and loc.gov,
HathiTrust, Find a Grave, lva.virginia.gov, `ead.lib.virginia.edu`, Virginia Chronicle,
usgenwebsites.org, GLO records. Web **search** worked — snippets and result lists only.
Web **fetch** was blocked for every domain tried, including Wikipedia, so it was blanket
policy rather than a per-site block; the failure mode is a 403 to CONNECT, not a timeout.

That agent could audit the repo and survey what records exist and where, but could not
retrieve, transcribe or verify anything. C195 is graded B purely for that reason.

- **Probe two or three target hosts and report reachability before starting a retrieval
  task.** A pass spent discovering it cannot read is a pass wasted.
- **Re-test rather than assuming either way** — a later session may differ.
- Known-closed routes, recorded so they are not re-derived: C085 (all free text routes to
  the 1840 Delaware Co., Ohio census), C086 (Claude-in-Chrome is not a FamilySearch route
  on this machine).

## 4. Structural rules that have already caught errors

- **Two writers, two namespaces: Claude allocates `C###`, ChatGPT allocates `G###`.** They
  collided four times on 10–11 Sep 2026. Reading the max id before writing does not
  prevent it. Never reuse or renumber another writer's id. Full protocol in
  `tasks/README.md`.
- **Before any in-place rewrite of `claims.jsonl`, re-read the file** — an append by the
  other writer between your read and your write is silently lost.
- **A proofread transcription outranks an uncertain reading of a low-resolution image —
  except where the cell is damaged, blotted, or split by a page break.** There a
  transcriber normalises rather than reads: go to the image, and prefer an independent
  second record over either. Ignoring this cost the priority-1 task on 10 Sep 2026
  (C016 → C038).
- **A claim whose image was never retained cannot be re-checked, and should not carry an
  A.** This is why C080 and C082 were downgraded on 16 Sep 2026.
- **Audit for what the project has never done, not just for what it got wrong.** Two of
  the largest gaps found so far were whole untouched record classes: no 1840 census work
  through eight passes (C058), and no probate, guardianship, deed or tax record in Aaron's
  generation or the one above it (C069). A third — Virginia apprenticeship records — was
  found the same way on 16 Sep (C195).
- **A handoff written without reading the current file is worse than none** (C117). Read
  `BRIEF.md` and `claims.jsonl` before writing to another thread.
- **A finding with no task home does not get worked.** The dispatcher reads task
  frontmatter; put the target in a `tasks/T*.md` note or it is invisible.

---

*Started 16 Sep 2026, pass 13. The rules above with a `C###` reference are also recorded as
method-class claims in `claims.jsonl` (C036, C058, C069, C085, C086, C117, C120) and are
cited by id from other claims, so they stay there as well; this file is where to look for
them. Rules added from pass 13 onward live here only — `claims.jsonl` is for evidence about
the family.*
