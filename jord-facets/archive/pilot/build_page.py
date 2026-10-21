"""Build the faceted-view prototype page from normalised tagger output.

Usage: python build_page.py IN_JSONL TAXONOMY_YAML TEMPLATE_HTML OUT_HTML
"""
import json, sys, yaml

inp, tax_p, tpl_p, out_p = sys.argv[1:5]

ORG_ALIASES = {
    "UK AI Security Institute": "UK AISI",
    "AISI": "UK AISI",
    "Google Deepmind": "Google DeepMind",
    "DeepMind": "Google DeepMind",
    "GDM": "Google DeepMind",
}

names = {}
def walk(nodes):
    for n in nodes:
        names[n["id"]] = n["name"]
        walk(n.get("children", []))
walk(yaml.safe_load(open(tax_p))["taxonomy"])

items = []
for line in open(inp):
    r = json.loads(line)
    items.append({
        "t": r["title"].strip(), "u": r["url"], "a": r["authors"], "d": r["posted"],
        "k": int(r["karma"] or 0), "af": r["af"] == "True", "s": r["summary"], "why": r["why"],
        "mp": r["motivation_primary"], "ms": r["motivation_secondary"], "mc": r["motivation_confidence"],
        "object": r["object"], "method": r["method"], "substrate": r["substrate"],
        "agenda": r["agenda"],
        "org": list(dict.fromkeys(ORG_ALIASES.get(o, o) for o in r["orgs"])),
    })

data = {"items": items, "agendaNames": names}
html = open(tpl_p).read().replace("/*__DATA__*/null", json.dumps(data, ensure_ascii=False).replace("</", "<\\/"))
open(out_p, "w").write(html)
print(len(items), "items ->", out_p)
