"""Build the facets page from tag_v2 output.

Usage: python build_v2.py IN_JSONL VOCAB_YAML TAXONOMY_YAML TEMPLATE_HTML OUT_HTML [OVERRIDES_YAML]
OVERRIDES_YAML (optional): {post_id: {field: value}} manual corrections applied last.
"""
import json, sys, yaml

inp, vocab_p, tax_p, tpl_p, out_p = sys.argv[1:6]
OV = yaml.safe_load(open(sys.argv[6])) if len(sys.argv) > 6 else {}
OV = OV or {}
V = yaml.safe_load(open(vocab_p))

org_alias = {}
for name, meta in V["org"].items():
    org_alias[name.lower()] = name
    for a in (meta or {}).get("aliases", []):
        org_alias[str(a).lower()] = name
dev_alias = {d.lower(): d for d in V["developers"]}
dev_alias.update({"nvidia (nemotron)": "NVIDIA", "nvidia": "NVIDIA", "qwen": "Alibaba (Qwen)", "alibaba": "Alibaba (Qwen)",
                  "olmo": "Ai2 (OLMo)", "ai2": "Ai2 (OLMo)", "gdm": "Google DeepMind", "deepmind": "Google DeepMind"})

names = {}
def walk(nodes):
    for n in nodes:
        names[n["id"]] = n["name"]; walk(n.get("children", []))
walk(yaml.safe_load(open(tax_p))["taxonomy"])
new_agendas = set(V.get("agenda_new_2026", {}))

def L(v):
    if isinstance(v, list):
        return [x if isinstance(x, dict) else str(x).strip() for x in v if (isinstance(x, dict) or str(x).strip())]
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

def norm_agenda(a):
    a = a.strip()
    if a.startswith("new:"):
        k = a[4:].strip().lower().replace(" ", "_").replace("-", "_")
        for canon, meta in V.get("agenda_new_2026", {}).items():
            al = [canon] + [str(x).lower().replace(" ", "_").replace("-", "_") for x in (meta or {}).get("aliases", [])]
            if k in al or k.startswith(canon) or canon in k:
                return "new:" + canon
        return "new:" + k
    return a

items = []
for line in open(inp):
    r = json.loads(line)
    if "error" in r:
        continue
    for k, v in (OV.get(r["id"]) or {}).items():
        r[k] = v
    mp = r["scientific_primary"] if r["scientific_primary"] in V["scientific"] else "synthesis"
    by, ev = [], {}
    for b in L(r["by"]):
        if not isinstance(b, dict):
            continue
        o = org_alias.get(b["org"].lower(), b["org"])
        by.append(o); ev[o] = {"e": b.get("evidence", ""), "b": b.get("basis", "stated")}
    items.append({
        "id": r["id"], "t": r["title"].strip(), "u": r["url"], "a": r["authors"], "d": r["posted"],
        "k": int(r["karma"] or 0), "af": r["af"] == "True", "s": r["why"], "why": r["why"],
        "scope": r["scope"], "scope_reason": r.get("scope_reason", ""),
        "mp": mp, "ms": [m for m in keep("scientific", L(r["scientific_secondary"])) if m != mp],
        "meta": keep("meta", L(r["meta"])), "concept": keep("concept", L(r["concept"])),
        "phenomenon": keep("phenomenon", L(r["phenomenon"])), "method": keep("method", L(r["method"])),
        "substrate": keep("substrate", L(r["substrate"])),
        "agenda": list(dict.fromkeys(norm_agenda(a) for a in L(r["agenda_2025"]))),
        "org": list(dict.fromkeys(by)), "ev": ev,
        "about": list(dict.fromkeys(dev_alias.get(a.lower(), a) for a in L(r["about"]))),
        "suggest": L(r.get("suggest")), "evidence": [r["evidence"]] if r.get("evidence") else [], "pp": r.get("pp", []),
    })

data = {"items": items, "agendaNames": names}
html = open(tpl_p).read().replace("/*__DATA__*/null", json.dumps(data, ensure_ascii=False).replace("</", "<\\/"))
open(out_p, "w").write(html)
print(len(items), "items;", sum(i["scope"] == "include" for i in items), "include; dropped off-vocab:", dropped)
