"""Normalise tagger output: list fields sometimes come back as strings
("a, b" or '["a","b"]'). Coerce to lists and drop values outside the schema.

Usage: python normalize.py IN_JSONL SCHEMA_YAML OUT_JSONL
"""
import json, sys, yaml

inp, schema_p, out_p = sys.argv[1:4]
schema = yaml.safe_load(open(schema_p))
allowed = {
    "motivation_secondary": set(schema["motivation"]),
    "object": set(schema["object"]),
    "method": set(schema["method"]),
    "substrate": set(schema["substrate"]),
}

def as_list(v):
    if isinstance(v, list):
        return [str(x).strip() for x in v if str(x).strip()]
    if not v:
        return []
    v = str(v).strip()
    if v.startswith("["):
        try:
            return as_list(json.loads(v))
        except Exception:
            pass
    return [x.strip().strip('"\'') for x in v.split(",") if x.strip()]

dropped = 0
with open(out_p, "w") as f:
    for line in open(inp):
        r = json.loads(line)
        if "error" in r:
            continue
        for k in ["motivation_secondary", "object", "method", "substrate", "agenda", "orgs"]:
            vals = as_list(r.get(k))
            if k in allowed:
                keep = [x for x in vals if x in allowed[k]]
                dropped += len(vals) - len(keep)
                vals = keep
            r[k] = list(dict.fromkeys(vals))
        r["motivation_secondary"] = [m for m in r["motivation_secondary"] if m != r["motivation_primary"]]
        f.write(json.dumps(r) + "\n")
print("dropped out-of-schema values:", dropped)
