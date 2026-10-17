"""Targeted corrections: for posts with reviewer findings, ask the tagger to fix
ONLY the fields the findings concern, checking each against the post text.
Unflagged posts are left untouched, so fixed tags stop regressing between rounds.

Usage: python patch_pass.py BASE_JSONL FINDINGS_GLOB BODIES_JSON VOCAB_YAML OUT_PATCHES_JSONL
Writes one {"id", "changes": {field: new_value}, "notes"} per flagged post.
Apply patches with apply_patches.py.
"""
import glob, json, sys, time, concurrent.futures as cf
import anthropic

base_p, fglob, bodies_p, vocab_p, out_p = sys.argv[1:6]
MODEL = "claude-sonnet-5-5"
base = {json.loads(l)["id"]: json.loads(l) for l in open(base_p)}
bodies = json.load(open(bodies_p))
vocab = open(vocab_p).read()

findings = {}
for p in glob.glob(fglob):
    for l in open(p):
        l = l.strip()
        if not l:
            continue
        try:
            f = json.loads(l)
        except Exception:
            continue
        pid = str(f.get("id", ""))
        if pid in base and f.get("type") != "scope":
            findings.setdefault(pid, []).append(f)

FIELDS = ["meta", "scientific_primary", "scientific_secondary", "concept", "phenomenon", "method", "substrate",
          "agenda_2025", "by", "about"]
SYSTEM = f"""You correct tags in a reviewed index of AI safety posts. You get the post's current tags, reviewer findings, and the post text.
For each finding, check it against the text. If the text supports it, fix that field; if not, leave the field alone.
Change ONLY fields that a supported finding concerns. Return the full corrected value for each changed field.
Use only ids from this vocabulary (definitions and rules included):

{vocab}

Field formats: meta, scientific_secondary, concept, phenomenon, method, substrate, agenda_2025, about are arrays of ids
(agenda_2025 uses 2025 leaf ids or "new:<id>"). scientific_primary is one id. by is an array of
{{"org", "basis": "stated"|"author_roster", "evidence": "<verbatim snippet from the post, or 'roster: <author>'>"}}.
Always respond by calling patch exactly once; `changes` may be empty."""

TOOL = {"name": "patch", "description": "Corrections for one post.", "input_schema": {"type": "object", "properties": {
    "changes": {"type": "object", "description": "field -> corrected full value; only changed fields"},
    "rejected": {"type": "array", "items": {"type": "string"}, "description": "short reasons for findings not applied"}},
    "required": ["changes", "rejected"]}}

client = anthropic.Anthropic()

def run(pid):
    rec = base[pid]
    cur = {k: rec.get(k) for k in FIELDS}
    fs = "\n".join(f"- [{f.get('facet')}] {f.get('type')}: current={f.get('current')} -> proposed={f.get('proposed')}. {f.get('reason')}"
                   for f in findings[pid])
    user = (f"Title: {rec['title']}\nAuthors: {rec['authors']}\n\nCurrent tags:\n{json.dumps(cur, ensure_ascii=False)}\n\n"
            f"Reviewer findings:\n{fs}\n\nPost text (start and end):\n{bodies.get(pid, '')}")
    err = None
    for attempt in range(5):
        try:
            r = client.messages.create(model=MODEL, max_tokens=1500, system=SYSTEM, tools=[TOOL],
                                       messages=[{"role": "user", "content": user}])
            out = next((b.input for b in r.content if b.type == "tool_use"), None)
            if out:
                ch = out.get("changes") or {}
                if isinstance(ch, str):
                    ch = json.loads(ch)
                ch = {k: v for k, v in ch.items() if k in FIELDS}
                return {"id": pid, "changes": ch, "rejected": out.get("rejected", []), "n_findings": len(findings[pid])}
            err = "no tool call"
        except Exception as e:
            err = str(e)
            time.sleep(20 * (attempt + 1) if "429" in err else 2)
    return {"id": pid, "error": err}

with cf.ThreadPoolExecutor(4) as ex, open(out_p, "w") as f:
    for res in ex.map(run, sorted(findings)):
        f.write(json.dumps(res, ensure_ascii=False) + "\n")
print(len(findings), "posts patched; errors:", sum('"error"' in l for l in open(out_p)))
