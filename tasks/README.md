**CLAIM IDS: Claude Code writes `C###`. ChatGPT writes `G###`. Never the other. Collisions on 10, 11, 12 AND 13 Sep 2026 (C055, C070, C076, C086, C120, C133–C135) — the fourth time ChatGPT wrote C-ids after this rule was posted. Read this line before writing to `claims.jsonl`.**

# Task protocol

Each `T*.md` is one open lead. Its YAML frontmatter is the task index:
`id`, `priority`, `mode`, `status`, `repository`, `blocked_on`, and `note`.
Read `BRIEF.md` plus one task file when executing a lead. Do not load `archive/`
or another task file.

## Local dispatch

The coordinator reads task frontmatter, then:

1. Excludes `mode: human`, `status: done`, and blocked tasks whose prerequisite
   is still unmet. Report an open human task in the initial pass status.
2. Sorts eligible tasks by ascending priority.
3. Selects at most three with disjoint `repository` values. Respect every
   `COLLIDES WITH` note.
4. Runs `mode: script` locally. It does not need a research agent.
5. Gives each research agent only `BRIEF.md` and its task file.

Each agent writes exactly one new `evidence/<task-id>_<slug>.md` file and returns:

```
STATUS: found | not-found | partial | blocked
RECORD: <what was retrieved>
URL: <stable link>
TRANSCRIPTION: <verbatim; no paraphrase>
GRADE: A | B | C
NEW FACTS: <one line each: person | fact | date | place>
CONFLICTS: <anything contradicting claims.jsonl, with the claim id>
NEGATIVE RESULTS: <one line each, only if worth recording>
```

Do not narrate the search, speculate about parentage, or substitute a compiled
tree for an unavailable record. A paywalled record returns `blocked` with its
exact access route.

## Claim IDs — two writers, two namespaces

Two assistants write to `claims.jsonl` (a Claude Code session and a ChatGPT session).
On 10–11 Sep 2026 they allocated from the same C-sequence at different times and
collided four times (C055, C070, C076, C086 — resolved by renumbering the later
copies to C089–C092). Reading the max ID before writing does not prevent this.

**Rule, effective 11 Sep 2026:**
- **Claude Code** allocates `C###` ids.
- **ChatGPT** allocates `G###` ids, starting at `G001`.
- Never reuse or renumber another writer's id. Cross-reference by id freely.
- Before any **in-place rewrite** of `claims.jsonl`, re-read the file first — an append
  by the other writer between your read and your write is silently lost.

## Merge

Only the coordinator edits `BRIEF.md`, `claims.jsonl`, or task frontmatter.

1. Read each returned evidence file and check all facts against `claims.jsonl`.
2. Report conflicts by claim ID before resolving them. Higher-grade evidence wins;
   a proofread transcription outranks an uncertain reading of a low-resolution
   image — **except where the cell is damaged, blotted, or split by a page break.
   There a transcriber normalises rather than reads, so go to the image, and prefer
   an independent second record over either.** This exception is not hypothetical:
   ignoring it cost the priority-1 task on 10 Sep 2026 (C016 → C038).
3. Show the proposed `BRIEF.md` diff before writing it. Keep the brief below
   roughly 1,500 words; detailed history belongs in claims or the archive.
4. Append durable facts and worthwhile negatives to `claims.jsonl`, update each
   completed task's status, and place a concise pass note in `archive/`.

Evidence grades: **A** is primary or near-primary; **B** is strong, identified
secondary work; **C** is a lead only. An ungraded item is C. Never promote a
C-level relationship into the working tree without A/B corroboration.

## Method traps that have already cost this project a pass

Each of these produced a **false report**, not a visible error. They are in
`claims.jsonl` so they can be cited; they are here because that file is not read
cover to cover.

1. **An unverified string replacement is a silent failure (C198).** `str.replace`
   returns the string unchanged on a miss and raises nothing, so a script that
   prints its own success message will report an edit it never made. On 16 Sep 2026
   three replacements against `PARENTAGE-TESTS.md` no-matched on a line-wrap
   difference and a whole file kept two statements the session had just retracted —
   after Spencer had been told they were fixed everywhere. **Assert the pattern is
   present before replacing and assert the result is present after writing, and
   check `git diff --stat` against what you expected to change.** A file missing
   from the diff is the signature.
2. **`grep` in Spencer's shell silently skips ISO-8859 files (C036).** It wraps
   `ugrep -I`, which classifies the USGenWeb transcriptions in `evidence/` as
   binary: empty output, exit 1, indistinguishable from a genuine no-match. **Use
   `command grep -a`, and verify any such search with a control term known to be
   present.**
3. **State the narrowest true version (C199).** If a finding needs "only",
   "never", "impossible" or "all" to land, test that word against the file with a
   script before writing it. On 16 Sep the strong forms of two claims were both
   wrong and neither was needed — the narrow versions were already decisive.
4. **Grade reasoning and citation separately (C199).** C195's argument is sound
   while its reel number and barcode came from search snippets. Conflating them
   would have sent Spencer to Richmond on an unverified citation.
5. **Pre-register the kill condition for a hypothesis you generated (C199).**
   Write down what result would falsify it *before* the record is read. C194
   carries "it dies if the 1830 bracket reads 20–30". Precedent that this works:
   C081 was an explicit prediction, it failed, and it is marked `PREDICTION
   FAILED` / VOID rather than quietly reinterpreted.
6. **Probe reachability before dispatching a retrieval task (C200).** Egress
   policy is per-session. On 16 Sep 2026 an agent could reach no record host at
   all — archive.org, FamilySearch, LoC, HathiTrust, LVA, Find a Grave, all
   refused — and spent the pass discovering it. Have the agent test two or three
   target hosts and report, then re-test in a later session rather than assuming.

## Outside this workspace

Attach `BRIEF.md` and one task file to one conversation. Attach `claims.jsonl`
only when the system can search it. Require the same return block above. Do not
attach `archive/`. Bring the returned block back here for reconciliation before
any working-state file is changed.
