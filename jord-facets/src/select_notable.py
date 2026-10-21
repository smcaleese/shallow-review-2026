"""Pick notable posts from the raw LW scrape.

Pool: posts tagged "AI", tagged with an AI-specific subtag (a tag where
>=80% of its posts also carry "AI"), or with no tags yet.
Notable: union of the top-N by karma, AF karma, comment count and karma per
month (corrects for recent posts having had less time to collect votes).

Usage: python select_notable.py RAW_CSV OUT_CSV [AS_OF=2026-10-10] [SCOPE_JSONL]
With SCOPE_JSONL, the pool is restricted to posts scoped include/borderline.
"""
import csv, json, sys, collections, datetime as dt

raw_p, out_p = sys.argv[1:3]
as_of = dt.date.fromisoformat(sys.argv[3] if len(sys.argv) > 3 else "2026-10-10")
TOP = {"karma": 100, "af_karma": 100, "comment_count": 75, "karma_per_month": 75}

rows = list(csv.DictReader(open(raw_p)))
tags = lambda r: [t.strip() for t in r["tags"].split(",") if t.strip()]

with_ai, total = collections.Counter(), collections.Counter()
for r in rows:
    ts = tags(r)
    for t in ts:
        total[t] += 1
        with_ai[t] += "AI" in ts
ai_tags = {t for t in total if t == "AI" or (total[t] >= 3 and with_ai[t] / total[t] >= 0.8)}

pool = [r for r in rows if not tags(r) or ai_tags & set(tags(r))]
if len(sys.argv) > 4:
    sc = {}
    for line in open(sys.argv[4]):
        d = json.loads(line)
        sc[d["id"]] = d if "scope" in d else {"scope": "borderline", "reason": "first-pass check failed; needs a look"}
    pool = [r for r in pool if sc.get(r["id"], {}).get("scope") in ("include", "borderline")]
    for r in pool:
        r["scope_first_pass"] = sc[r["id"]]["scope"]; r["scope_reason"] = sc[r["id"]].get("reason", "")
for r in pool:
    months = max((as_of - dt.date.fromisoformat(r["posted"])).days / 30.4, 0.5)
    r["karma_per_month"] = round(int(r["karma"] or 0) / months, 1)

picked = {}
for key, n in TOP.items():
    ranked = sorted(pool, key=lambda r: -float(r[key] or 0))[:n]
    for r in ranked:
        picked.setdefault(r["id"], {**r, "picked_by": []})["picked_by"].append(key)

out = sorted(picked.values(), key=lambda r: -int(r["karma"] or 0))
for r in out:
    r["picked_by"] = "|".join(r["picked_by"])
with open(out_p, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(out[0].keys()))
    w.writeheader(); w.writerows(out)

print(f"pool {len(pool)} of {len(rows)} posts; {len(ai_tags)} AI tags; picked {len(out)}")
print("picked by:", collections.Counter(k for r in out for k in r["picked_by"].split("|")))
print("only via one metric:", collections.Counter(r["picked_by"] for r in out if "|" not in r["picked_by"]))
print("min karma among picked:", min(int(r["karma"]) for r in out))
