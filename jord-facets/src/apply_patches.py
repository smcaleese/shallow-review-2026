"""Apply accumulated patch files (in order) and scope overrides to tagger output.

Usage: python apply_patches.py BASE_JSONL OUT_JSONL SCOPE_OVERRIDES_JSON PATCHES_JSONL [PATCHES_JSONL ...]
"""
import json, sys

base_p, out_p, scope_p, *patch_ps = sys.argv[1:]
recs = [json.loads(l) for l in open(base_p)]
by_id = {r["id"]: r for r in recs}
n = 0
for p in patch_ps:
    for l in open(p):
        d = json.loads(l)
        if "error" in d or d["id"] not in by_id:
            continue
        for k, v in d["changes"].items():
            by_id[d["id"]][k] = v; n += 1
        by_id[d["id"]].setdefault("patched_by", []).append(p.split("/")[-1])
scope = json.load(open(scope_p))
for pid, s in scope.items():
    if pid in by_id:
        by_id[pid]["scope"] = s
with open(out_p, "w") as f:
    f.writelines(json.dumps(r, ensure_ascii=False) + "\n" for r in recs)
print(f"applied {n} field changes from {len(patch_ps)} patch file(s); {len(scope)} scope overrides")
