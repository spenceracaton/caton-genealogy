# Agents working in this repository

Read `METHOD.md` before your first edit. It is the only home for operational rules. This file just points to the rules that are broken most often.

1. **Commit your output.** When you work in a worktree, commit your new files to a branch named `agent/<stream-or-task>-<yyyy-mm-dd>` before you report done. Uncommitted files are lost when the worktree is pruned (METHOD.md §5). Do not push, open PRs or edit canonical files unless the coordinator told you to.
2. **Do not write in the main checkout** (`~/Desktop/claude/personal/genealogy`) unless you are the coordinator.
3. **Claim ids:** Claude writes `C###`. ChatGPT and Codex write `G###`, or `G-PENDING` when dispatched as a task. See `tasks/README.md`.
4. **Evidence files are provenance.** Add new dated files to `evidence/` and never edit an original.
5. **Before committing:** run `python3 tools/check-project.py`.
6. **Coordinator only:** run `python3 tools/reconcile.py` at the start and end of a session.
