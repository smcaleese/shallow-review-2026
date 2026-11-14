#!/usr/bin/env python3
"""Recurring agendas: leaf categories that several methods form from largely the same items.

Usage (from taxonomy-discovery/): uv run python consensus.py [jaccard threshold, default 0.3]
Writes results/consensus-agendas.json; recurring-agendas.md is written from it.
"""
# Match leaf categories across the six methods by the items they share (Jaccard), link mutual best
# matches above a threshold, and take connected components. No names or judgement involved in the matching.
import json, sys
from collections import Counter, defaultdict
from itertools import combinations
sys.path.insert(0, ".")
from shared.taxonomy import OTHER, level_assignments
from shared.data import load_items

THRESH = float(sys.argv[1]) if len(sys.argv) > 1 else 0.3
METHODS = ["1-llm-taxonomy", "2-llm-knn-graph", "3-embedding-knn-graph", "4-human-taxonomy", "5-semantic-map", "6-map-taxonomy"]
items = {i["pid"]: i for i in load_items()}
leaves = {}  # (method, leaf id) -> set of pids
names = {}
for m in METHODS:
    res = json.load(open(f"{m}/output/clusters.json"))
    cname = {c["id"]: c["name"] for c in res["categories"]}
    for pid, leaf in level_assignments(res, "leaf").items():
        if leaf != OTHER:
            leaves.setdefault((m, leaf), set()).add(pid)
            names[(m, leaf)] = cname[leaf]
J = lambda a, b: len(a & b) / len(a | b)
best = {}
for k in leaves:
    for m in METHODS:
        if m == k[0]: continue
        cands = [(J(leaves[k], leaves[o]), o) for o in leaves if o[0] == m]
        best[(k, m)] = max(cands)
# edges: mutual best matches with Jaccard >= THRESH
adj = defaultdict(set)
for (k, m), (j, o) in best.items():
    if j >= THRESH and best[(o, k[0])][1] == k:
        adj[k].add(o); adj[o].add(k)
seen, comps = set(), []
for k in leaves:
    if k in seen or k not in adj: continue
    stack, comp = [k], set()
    while stack:
        x = stack.pop()
        if x in comp: continue
        comp.add(x); stack.extend(adj[x])
    seen |= comp; comps.append(comp)
out = []
for comp in comps:
    ms = sorted({m for m, _ in comp})
    votes = Counter(p for k in comp for p in leaves[k])
    core = [p for p, v in votes.items() if v >= max(2, (len(ms) + 1) // 2)]
    sizes = sorted(len(leaves[k]) for k in comp)
    out.append({"methods": ms, "n_methods": len(ms), "leaves": [[k[0][0], names[k], len(leaves[k])] for k in sorted(comp)],
                "core": sorted(core, key=lambda p: -votes[p]), "median_size": sizes[len(sizes)//2],
                "votes": {p: votes[p] for p in core}})
out.sort(key=lambda c: (-c["n_methods"], -len(c["core"])))
json.dump(out, open("results/consensus-agendas.json", "w"), indent=1)
print(f"threshold {THRESH}: {len(out)} components; leaves matched {sum(len(c['leaves']) for c in out)}/{len(leaves)}")
for c in out:
    print(f"\n[{c['n_methods']}/6, core {len(c['core'])}, median {c['median_size']}] methods {''.join(m[0] for m in c['methods'])}")
    for m, n, s in c["leaves"]: print(f"   {m}: {n} ({s})")
