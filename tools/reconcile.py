#!/usr/bin/env python3
"""Report agent output that is not yet on origin/main. Read-only: changes nothing.

   python3 tools/reconcile.py              # repo, branches, worktrees, snapshot refs
   python3 tools/reconcile.py --downloads  # also hash-check recent ~/Downloads images

A file counts as preserved when its exact bytes exist anywhere in origin/main's history,
whatever its path, or when an evidence/*manifest*.json on origin/main records its SHA-256
as `source_sha256` (an import that normalized whitespace). Deliberate exclusions go in
IGNORE with a reason. Exit status 1 means something is unpreserved; 0 means clean."""
import hashlib
import json
import os
import pathlib
import subprocess
import sys
import time

ROOT = pathlib.Path(__file__).resolve().parent.parent
BASE = "origin/main"
DOWNLOAD_DAYS = 14
DOWNLOAD_PATTERNS = ("image*.jp*g", "image*.png", "DGS*.jp*g", "*[Cc]aton*")
# SHA-256 of files deliberately left out of the repo -> reason
IGNORE = {
    "c700dbe592c76c43eabb12e4bbfd27c9f3035f4f18297682dba61194daff9c0a":
        "~/Downloads/image (26).jpg: Warwick Co. Overseers of the Poor 1788, wrong county "
        "(evidence/spencer-captures-2026-09-16-17/README.md)",
    "299eb4d4afc2dca8c89d26714e05ac1659138dc63a01dcaa7b6dfd06f59cec62":
        "Codex snapshot draft of evidence/T15_prince-william-1782-1796-public-tax-route.md; "
        "superseded by the edited version on main (two NEGATIVE/RECORD lines reworded)",
    "5159001577572611f3c88cdddc61f22790061f4b715d22efcd5213a7f932d7cd":
        "Codex snapshot draft of evidence/T15_fauquier_post1835_record_test.md; main drops one line",
}
problems = []


def git(*args, cwd=ROOT, check=True):
    return subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True, check=check).stdout


def report(section, lines):
    print(f"\n## {section}")
    if not lines:
        print("   ok")
    for line in lines:
        print(f"   {line}")
    problems.extend(lines)


# A stalled network fetch once hung an unattended run for 10+ minutes; never block on it.
fetch_env = {**os.environ, "GIT_TERMINAL_PROMPT": "0", "GIT_HTTP_LOW_SPEED_LIMIT": "1000", "GIT_HTTP_LOW_SPEED_TIME": "30"}
try:
    fetch = subprocess.run(["git", "fetch", "--quiet", "origin"], cwd=ROOT, capture_output=True, text=True,
                           env=fetch_env, timeout=90)
    if fetch.returncode:
        print(f"warning: git fetch failed, comparing against a stale {BASE}: {fetch.stderr.strip()}")
except subprocess.TimeoutExpired:
    print(f"warning: git fetch timed out after 90 s, comparing against a stale {BASE}")

known = {line.split()[0] for line in git("rev-list", "--objects", BASE).splitlines()}


manifest_sha = set()
for name in git("ls-tree", "-r", "--name-only", BASE, "evidence/").split():
    if "manifest" in name and name.endswith(".json"):
        for row in json.loads(git("show", f"{BASE}:{name}")):
            manifest_sha.add(row.get("source_sha256"))


def blob(path):
    return git("hash-object", str(path)).strip()


def preserved(path):
    if blob(path) in known:
        return True
    sha = hashlib.sha256(pathlib.Path(path).read_bytes()).hexdigest()
    return sha in manifest_sha or sha in IGNORE


def unpreserved(checkout):
    """Untracked or modified files in a checkout whose bytes are not on BASE."""
    out = git("status", "--porcelain", "--untracked-files=all", cwd=checkout, check=False)
    missing = []
    for line in out.splitlines():
        state, name = line[:2], line[3:].strip('"')
        path = pathlib.Path(checkout) / name
        if "D" in state or not path.is_file():
            continue
        if not preserved(path):
            missing.append(f"{state.strip() or '??'} {name}")
    return missing


# 1. This checkout
ahead, behind = git("rev-list", "--left-right", "--count", f"HEAD...{BASE}").split()
lines = []
if ahead != "0":
    lines.append(f"HEAD is {ahead} commit(s) ahead of {BASE}: push or merge")
if behind != "0":
    print(f"note: HEAD is {behind} commit(s) behind {BASE}; pull before writing")
lines += [f"uncommitted: {f}" for f in unpreserved(ROOT)]
report(f"This checkout ({git('branch', '--show-current').strip() or 'detached'})", lines)

# 2. Branches not merged into BASE
lines = []
for ref in git("for-each-ref", "--format=%(refname:short)", "refs/heads", "refs/remotes/origin").split():
    if ref in ("origin", "origin/HEAD", BASE):
        continue
    count = git("rev-list", "--count", f"{BASE}..{ref}").strip()
    if count != "0":
        subject = git("log", "-1", "--format=%cs %s", ref).strip()
        lines.append(f"{ref}: {count} unmerged commit(s), last {subject[:90]}")
report(f"Branches not merged into {BASE}", lines)

# 3. Worktrees (Codex, Claude scratchpads, /tmp)
lines = []
for block in git("worktree", "list", "--porcelain").split("\n\n"):
    fields = dict(l.split(" ", 1) if " " in l else (l, "") for l in block.splitlines())
    path = fields.get("worktree")
    if not path or pathlib.Path(path) == ROOT:
        continue
    if "prunable" in fields or not pathlib.Path(path).exists():
        lines.append(f"stale entry (run `git worktree prune`): {path}")
        continue
    missing = unpreserved(path)
    if missing:
        age = (time.time() - max(pathlib.Path(path, m.split(" ", 1)[1]).stat().st_mtime for m in missing)) / 60
        lines.append(f"{path}  [{fields.get('branch', 'detached').replace('refs/heads/', '')}; newest {age:.0f} min ago]")
        lines += [f"    {m}" for m in missing]
report("Worktrees with files not on origin/main", lines)

# 4. Codex snapshot refs
lines = []
for ref in git("for-each-ref", "--format=%(refname)", "refs/codex/snapshots").split():
    unique = [l.split("\t", 1)[1] for l in git("ls-tree", "-r", ref).splitlines()
              if l.split()[2] not in known
              and hashlib.sha256(subprocess.run(["git", "cat-file", "blob", l.split()[2]], cwd=ROOT,
                                               capture_output=True, check=True).stdout).hexdigest() not in IGNORE]
    if unique:
        lines.append(f"{ref.rsplit('/', 1)[1][:12]} ({git('log', '-1', '--format=%cs', ref).strip()}): " + ", ".join(unique))
report("Codex snapshot refs holding files not on origin/main", lines)

# 5. Spencer's FamilySearch downloads
if "--downloads" in sys.argv:
    cutoff = time.time() - DOWNLOAD_DAYS * 86400
    downloads = pathlib.Path.home() / "Downloads"
    seen = {p for pattern in DOWNLOAD_PATTERNS for p in downloads.glob(pattern) if p.is_file() and p.stat().st_mtime > cutoff}
    report(f"~/Downloads images from the last {DOWNLOAD_DAYS} days not in the repo",
           sorted(p.name for p in seen if not preserved(p)))

print(f"\n{'UNPRESERVED: ' + str(len(problems)) + ' item(s)' if problems else 'Everything is on ' + BASE}")
sys.exit(1 if problems else 0)
