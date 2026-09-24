# Caton genealogy: agent instructions

This repository holds research on the parentage of Aaron Caton (b. c.1820, Virginia; d. Boonville, Missouri). It is not code. The repo is **public**: anything pushed is published.

This file is the one instruction file for every agent. Claude Code loads it through `CLAUDE.md`, and Codex reads it directly. ChatGPT on the web gets it through its launch prompt. The rules below are complete on their own. `METHOD.md` explains the reasons behind them.

## Read first

`BRIEF.md` (current state), `METHOD.md` (operational rules), and the one `tasks/T*.md` you were given. Read `DATA_MODEL.md` before touching any `*.jsonl` record. Never load `archive/` as research context.

## Roles

- **Worker:** any agent given a task.
  - Work in your own worktree, never in the main checkout (`~/Desktop/claude/personal/genealogy`).
  - Add new dated files under `evidence/` only.
  - Propose claims as `G-PENDING` inside your evidence note.
  - Do not edit `BRIEF.md`, `claims.jsonl`, the other `*.jsonl` registries, `CATON_CENSUS_LEDGER.md` or task frontmatter.
  - Do not push or open PRs.
- **Coordinator:** one at a time.
  - The only session that writes in the main checkout or edits the canonical files listed above.
  - Merges worker branches with `git merge --no-ff`. Never copies worker files over by hand.
  - Pushes to `main`.
  - Before importing or merging anything, runs `python3 tools/reconcile.py` to check that no other session is already doing it.
- **ChatGPT web (no repo access):** return one evidence note, following the template in the launch prompt. The coordinator commits it.

## Finishing a worker task (required)

```bash
git switch -c agent/<task>-<yyyy-mm-dd>
git add evidence/<your new files>
python3 tools/check-project.py
git commit -m "<task>: <one-line result>"
```

Report the branch name and the paths of the files you added. Untracked files are lost when a worktree is pruned.

Older launch prompts say "no commits" (for example `handoffs/` before 25 Sep 2026). There it means no commits to `main` and no pushing. Still commit to your own `agent/` branch.

## Claim ids

- Claude Code allocates `C###`.
- ChatGPT and Codex allocate `G###`.
- Dispatched workers write `G-PENDING`, and the coordinator assigns the id on merge.
- Never reuse or renumber another writer's id.
- Re-read `claims.jsonl` right before any in-place rewrite.

## Evidence

- Files in `evidence/` are provenance. Never edit an original. Record a correction in a new dated file.
- Retain the image for any reading you grade A.
- A blocked or unsearched source is recorded as incomplete, never as a negative.

### Transcriptions before OCR

- Check for a FamilySearch or repository-supplied transcription/index before running OCR. Use it to locate candidates and capture the exact collection, film/DGS, volume, page, and image identifiers.
- Distinguish a full transcription from extracted index fields. An index may omit relationship language, marginal notes, witnesses, headings, surname spelling, and adjacent entries.
- Verify every material claim against the original image. Inspect the heading and nearby entries whenever they affect column alignment, identity, or meaning.
- If the image is unavailable, label the transcription/index as unverified derivative evidence and preserve the access boundary. Do not promote it to image-verified proof.
- Use OCR only when no usable transcription/index exists, when the source is unindexed, or to filter a large image set. Manually verify every OCR candidate against the image.
- Stop repeated OCR or enhancement attempts once the target is located or the image remains unreadable. Preserve the source handle and mark the reading unresolved.

## Checks

- Before every commit, `python3 tools/check-project.py` must end with `Project validation ok`.
- The coordinator runs `python3 tools/reconcile.py --downloads` at session start and end. The session ends at exit 0, or with every remaining item named in the handoff.
- Never delete a worktree or `refs/codex/*` ref that was touched in the last 15 minutes. Codex prunes its own.

## Public repository

Ask Spencer before committing records about living people or personal family documents. Once a commit is pushed, it is published.
