"""Dump the built page's data as markdown "tag views" for reviewers.

Usage: python make_views.py FACETS_HTML OUT_DIR
Writes OUT_DIR/items.md (every post, all tags) and OUT_DIR/by_<facet>.md
(posts grouped under each tag of that facet), plus OUT_DIR/items.json.
"""
import json, os, re, sys, collections

html_p, out = sys.argv[1:3]
os.makedirs(out, exist_ok=True)
s = open(html_p).read()
data = json.loads(re.search(r"const DATA = (\{.*?\});\n", s, re.S).group(1).replace("<\\/", "</"))
items, names = data["items"], data["agendaNames"]
json.dump(items, open(f"{out}/items.json", "w"), indent=1, ensure_ascii=False)

FACETS = ["scientific", "meta", "concept", "phenomenon", "method", "substrate", "agenda", "org", "about"]
def vals(it, f):
    if f == "scientific":
        return [it["mp"]] + [f"{m} (secondary)" for m in it["ms"]]
    if f == "agenda":
        return [names.get(a, a) for a in it["agenda"]]
    if f == "org":
        return [f'{o} [evidence: "{it["ev"].get(o, "")}"]' for o in it["org"]]
    return it[f]

def line(it):
    tags = "; ".join(f"{f}: {', '.join(vals(it, f)) or '—'}" for f in FACETS)
    flag = "" if it["scope"] == "include" else f" **[scope: {it['scope']}]**"
    return (f"- `{it['id']}` **{it['t']}**{flag} — {it['a'][:80]} · {it['k']} karma · {it['u']}\n"
            f"  - what it does: {it['why']}\n  - tags: {tags}")

with open(f"{out}/items.md", "w") as f:
    f.write(f"# All {len(items)} posts with tags\n\n")
    for it in sorted(items, key=lambda i: -i["k"]):
        f.write(line(it) + "\n")

for fac in FACETS:
    groups = collections.defaultdict(list)
    for it in items:
        vs = [v.split(" [evidence")[0].replace(" (secondary)", "") for v in vals(it, fac)] or ["(none)"]
        for v in vs:
            groups[v].append(it)
    with open(f"{out}/by_{fac}.md", "w") as f:
        f.write(f"# Posts grouped by {fac}\n\n")
        for g, its in sorted(groups.items(), key=lambda kv: -len(kv[1])):
            f.write(f"\n## {g} ({len(its)})\n\n")
            for it in sorted(its, key=lambda i: -i["k"]):
                f.write(line(it) + "\n")
print("views in", out, ":", sorted(os.listdir(out)))
