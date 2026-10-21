"""Build the v1 facets page from tag_v1 output.

Usage: python build_v1.py IN_JSONL VOCAB_YAML TAXONOMY_YAML TEMPLATE_HTML OUT_HTML [ORGS_JSONL]
"""
import json, sys, yaml

inp, vocab_p, tax_p, tpl_p, out_p = sys.argv[1:6]
ORGS = {}
if len(sys.argv) > 6:
    for line in open(sys.argv[6]):
        d = json.loads(line)
        if "error" not in d:
            ORGS[d["id"]] = d
V = yaml.safe_load(open(vocab_p))

org_alias = {}
for name, meta in V["org"].items():
    org_alias[name.lower()] = name
    for a in (meta or {}).get("aliases", []):
        org_alias[str(a).lower()] = name
org_alias.update({"huggingface": "Hugging Face", "arcadia": "Arcadia Impact",
                  "geodesic": "Geodesic Research", "aether": "Aether Research"})

names = {}
def walk(nodes):
    for n in nodes:
        names[n["id"]] = n["name"]; walk(n.get("children", []))
walk(yaml.safe_load(open(tax_p))["taxonomy"])

def L(v):
    if isinstance(v, list):
        return [str(x).strip() for x in v if str(x).strip()]
    if not v:
        return []
    v = str(v).strip()
    if v.startswith("["):
        try:
            return L(json.loads(v))
        except Exception:
            pass
    return [x.strip().strip("'\"") for x in v.split(",") if x.strip()]

dropped = []
def keep(facet, vals):
    ok = [v for v in vals if v in V[facet]]
    dropped.extend(f"{facet}:{v}" for v in vals if v not in V[facet])
    return list(dict.fromkeys(ok))

items = []
for line in open(inp):
    r = json.loads(line)
    if "error" in r:
        continue
    sci = list(V["scientific"])
    mp = r["scientific_primary"] if r["scientific_primary"] in sci else "conceptual"
    if r["id"] in ORGS:
        by = ORGS[r["id"]]["by"]
        by = json.loads(by) if isinstance(by, str) else by
        orgs = [org_alias.get(x["org"].lower(), x["org"]) for x in by if isinstance(x, dict)]
        evid = {org_alias.get(x["org"].lower(), x["org"]): x.get("evidence", "") for x in by if isinstance(x, dict)}
        about = L(ORGS[r["id"]]["about"])
    else:
        orgs = [org_alias.get(o.lower(), o) for o in L(r["org"]) + L(r["org_other"])]
        evid, about = {}, []
    items.append({
        "t": r["title"].strip(), "u": r["url"], "a": r["authors"], "d": r["posted"],
        "k": int(r["karma"] or 0), "af": r["af"] == "True", "s": r["why"], "why": r["why"],
        "scope": r["scope"], "mp": mp, "ms": [m for m in keep("scientific", L(r["scientific_secondary"])) if m != mp],
        "meta": keep("meta", L(r["meta"])), "concept": keep("concept", L(r["concept"])),
        "phenomenon": keep("phenomenon", L(r["phenomenon"])), "method": keep("method", L(r["method"])),
        "substrate": keep("substrate", L(r["substrate"])), "agenda": L(r["agenda_2025"]),
        "org": list(dict.fromkeys(orgs)), "ev": evid, "about": list(dict.fromkeys(about)), "suggest": L(r["suggest"]), "id": r["id"],
    })

data = {"items": items, "agendaNames": names}
html = open(tpl_p).read().replace("/*__DATA__*/null", json.dumps(data, ensure_ascii=False).replace("</", "<\\/"))
open(out_p, "w").write(html)
print(len(items), "items;", sum(i["scope"] == "include" for i in items), "include; dropped off-vocab:", dropped)
