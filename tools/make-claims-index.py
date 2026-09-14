#!/usr/bin/env python3
"""Regenerate claims-index.md from claims.jsonl. Run after any merge.
   python3 tools/make-claims-index.py"""
import json, re, pathlib, datetime
root = pathlib.Path(__file__).resolve().parent.parent
rows = [json.loads(l) for l in (root/"claims.jsonl").open() if l.strip()]

def status(f):
    F = re.sub(r"^\[RENUMBERED[^\]]*\]\s*", "", f.upper())
    # superseded claims carry their marker at the START of the text (set by the merge session)
    if re.match(r"(REVERSED|SUPERSEDED|WRONG, SEE|DOWNGRADED|EXCLUSION WITHDRAWN|PREDICTION FAILED|VOID)\b", F):
        return "VOID/REVERSED"
    if re.match(r"MOOT\b", F): return "moot"
    if re.match(r"(NEGATIVE|BOUNDED NEGATIVE|DEAD END|WEAK NEGATIVE)\b", F) or re.search(r"\bNEGATIVE, SCOPED\b|\bNEGATIVE, WEAK\b|\bNEGATIVE, LIMITED\b", F):
        return "negative"
    if re.match(r"DO NOT MERGE\b", F) or re.search(r"\bDO NOT MERGE - (IDENTIFIED|RULED OUT)\b", F):
        return "do-not-merge"
    if re.match(r"(HYPOTHESIS|LEAD ONLY|LEAD FOR|LEAD, C-LEVEL|POSSIBLE COUNTY|STRATEGIC REFRAME|CONVERGENCE|REFRAMED QUESTION|THE FORK|STRONGEST (SIBLING|STRUCTURAL)|BEST CANDIDATE|MIGRATION LEAD|CORROBORATED - UPGRADED|UNSOURCED ASSERTION|POSSIBLE)\b", F):
        return "hypothesis"
    if re.match(r"(TOOLING|METHOD|CAUSED A FALSE|GAP CLOSED|SECOND STRUCTURAL|ACCESS ROUTE|CLUSTER MAP|COMPLETE STATEWIDE|FULL SWEEP|THE LARGEST UNEXAMINED|CLAUDE-IN-CHROME|1840 DELAWARE CO., OHIO \(T11\) - ALL|ASSESSED AND FOUND|THE CHATGPT HANDOFF|THREE DISCREPANCIES|COLLATERAL)", F):
        return "method"
    return "fact"

def short(f, n=110):
    f = re.sub(r"^\[RENUMBERED[^\]]*\]\s*", "", f)
    f = re.sub(r"\s+", " ", f).strip()
    return (f[:n] + "…") if len(f) > n else f

out = []
out.append(f"# Claims index — generated {datetime.date.today().isoformat()} from `claims.jsonl` ({len(rows)} claims)\n")
out.append("Regenerate with `python3 tools/make-claims-index.py`. **Do not edit by hand.**\n")
out.append("Status is inferred from the claim text: `fact` · `hypothesis` · `negative` · `do-not-merge` · `method` · `moot` · `VOID/REVERSED` (retained as the record of an error — do not cite as fact).\n")

# summary counts
from collections import Counter
c = Counter(status(r["fact"]) for r in rows)
g = Counter(r["grade"] for r in rows)
out.append("| status | n | | grade | n |\n|---|---:|---|---|---:|")
sk = ["fact","hypothesis","negative","do-not-merge","method","moot","VOID/REVERSED"]
gk = ["A","B","C"]
for i in range(max(len(sk),len(gk))):
    a = f"{sk[i]} | {c.get(sk[i],0)}" if i < len(sk) else " | "
    b = f"{gk[i]} | {g.get(gk[i],0)}" if i < len(gk) else " | "
    out.append(f"| {a} | | {b} |")
out.append("")

out.append("## The load-bearing ones\n")
key = ["C075","C107","C099","C110","C062","C077","C098","C108","C038","C069","C058"]
out.append("| id | grade | what |\n|---|---|---|")
for r in rows:
    if r["id"] in key:
        out.append(f"| **{r['id']}** | {r['grade']} | {short(r['fact'],150)} |")
out.append("")

out.append("## All claims\n")
out.append("| id | grade | status | pass | person | summary |\n|---|---|---|---|---|---|")
for r in rows:
    st = status(r["fact"])
    idc = f"~~{r['id']}~~" if st == "VOID/REVERSED" else r["id"]
    out.append(f"| {idc} | {r['grade']} | {st} | {r.get('pass','')} | {r['person'][:34]} | {short(r['fact'])} |")

out.append("\n## Open discrepancies (from C115)\n")
out.append("- 1860 Livingston township: **Jackson** (page image + FS index) vs Richland (ChatGPT handoff)")
out.append("- Aaron's age 1870: **55** (page image) vs ~53 (handoff)")
out.append("- Aaron F. Caton's 1886 death: Otterville burial, b.1842 (C052/C096) vs Pacific MO, ~50, ten children (handoff)")
out.append("- Julia's mother's birthplace: Ohio (C037 and censuses) vs New Hampshire (1900 census, C111 — treated as the error)")
out.append("- William Caton's birth state: Virginia (Cooper 1850, C096) vs Maryland (Bates 1860, C055)")
(root/"claims-index.md").write_text("\n".join(out)+"\n")
print(f"claims-index.md: {len(rows)} claims; statuses {dict(c)}")
