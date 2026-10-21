"""Export the curated LW/AF posts and their tags as one CSV row per post.

Reads the data embedded in the built page (site/index.html), so the CSV always matches what the site shows.
Column names follow Stephen's taxonomy/output/arxiv-papers-tagged.csv where the meaning is the same
(title, authors, published, url, summary, evidence, contribution_primary, contribution_secondary,
paper_type, concept, method, agenda_2025, new_agenda, tags), with `source = lesswrong`. LW-only columns
come after. Multi-valued cells are joined with "; " as in Stephen's CSV.

NOTE: tag VALUES use this folder's vocabulary (vocab.yaml), not taxonomy/facets.yaml. The column names
line up, but values need mapping before the two CSVs share one facet.

Usage: python src/export_csv.py site/index.html data/lw-posts-tagged.csv [--all]
  --all also writes excluded posts (scope column says which).
"""
import csv, json, re, sys

html_p, out_p = sys.argv[1:3]
include_all = "--all" in sys.argv
s = open(html_p).read()
data = json.loads(re.search(r"const DATA = (\{.*?\});\n", s, re.S).group(1).replace("<\\/", "</"))
names = data["agendaNames"]

def j(xs):
    return "; ".join(x.replace("_", " ") for x in xs)

rows = []
for it in sorted(data["items"], key=lambda i: -i["k"]):
    if it["scope"] != "include" and not include_all:
        continue
    old = [names.get(a, a) for a in it["agenda"] if not a.startswith("new:")]
    new = [a[4:].replace("_", " ") for a in it["agenda"] if a.startswith("new:")]
    row = {
        "source": "lesswrong",
        "id": it["id"],
        "title": it["t"],
        "authors": it["a"],
        "published": it["d"],
        "url": it["u"],
        "summary": it["why"],
        "evidence": j(it.get("evidence", [])),
        "contribution_primary": it["mp"].replace("_", " "),
        "contribution_secondary": j(it["ms"]),
        "paper_type": j(it["meta"]),
        "concept": j(it["concept"]),
        "phenomenon": j(it["phenomenon"]),
        "method": j(it["method"]),
        "substrate": j(it["substrate"]),
        "agenda_2025": "; ".join(old),
        "new_agenda": "; ".join(new),
        "by_org": "; ".join(it["org"]),
        "by_org_basis": "; ".join(f'{o}: {(it["ev"].get(o) or {}).get("b", "")}' for o in it["org"]),
        "by_org_evidence": " | ".join(f'{o}: {(it["ev"].get(o) or {}).get("e", "")}' for o in it["org"]),
        "about": "; ".join(it["about"]),
        "karma": it["k"],
        "alignment_forum": it["af"],
        "scope": it["scope"],
        "rule_changes": " | ".join(it.get("pp", [])),
    }
    tags = [row["evidence"], row["contribution_primary"], row["contribution_secondary"], row["paper_type"],
            row["concept"], row["phenomenon"], row["method"], row["substrate"], row["agenda_2025"],
            row["new_agenda"], row["by_org"]]
    row["tags"] = "; ".join(t for t in "; ".join(tags).split("; ") if t)
    rows.append(row)

with open(out_p, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0]))
    w.writeheader(); w.writerows(rows)
print(f"{len(rows)} posts -> {out_p}")
