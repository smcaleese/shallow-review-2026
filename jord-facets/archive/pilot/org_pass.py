"""Attribution pass: who produced each post (`by`, with evidence) vs whose
models/practices it is about (`about`).

Usage: python org_pass.py IN_CSV BODIES_JSON VOCAB_YAML OUT_JSONL
Needs ANTHROPIC_API_KEY. Resumes from OUT_JSONL.
"""
import csv, json, os, sys, time, yaml, concurrent.futures as cf
import anthropic

inp, bodies_p, vocab_p, out_p = sys.argv[1:5]
MODEL = "claude-sonnet-5-5"
V = yaml.safe_load(open(vocab_p))
bodies = json.load(open(bodies_p))
ORGS = list(V["org"])
LABS = ["Anthropic", "OpenAI", "Google DeepMind", "Meta", "xAI", "Alibaba (Qwen)", "DeepSeek", "Moonshot",
        "Ai2 (OLMo)", "Mistral", "Microsoft", "Amazon"]

SYSTEM = f"""You attribute AI safety forum posts to organisations, for a literature review. Two separate questions.

BY — which organisations PRODUCED this work. Only tag an org when the post itself shows it:
- an affiliation line or author list with affiliations,
- first-person institutional voice ("at Redwood we", "our team at METR", "this is an Anthropic Fellows project"),
- "this work was done as part of MATS / SPAR / MARS / a fellowship" (tag the programme),
- the post is an official org announcement or org account.
NOT sufficient: the post studies that org's models; criticises or discusses the org; the author is famous for working there but the post does not say the work is from there; thanks to an org; funding acknowledgements; citing the org's papers. A linkpost of someone else's paper: tag the paper's org only if the post states it.
Personal blog-style posts by people who work at a lab, with no institutional framing, get NO by-tag.
For each by-tag, give `evidence`: a short verbatim snippet (under 20 words) from the post that shows it.
Canonical names to use when they match: {", ".join(ORGS)}. Other orgs are allowed with their usual name.

ABOUT — which AI developers' models or practices the post substantially studies or discusses (not passing mentions). Use: {", ".join(LABS)}, or another developer's name. Empty if the work is model-agnostic or about no specific developer.

Always respond by calling attribute exactly once."""

TOOL = {"name": "attribute", "description": "Record attribution.", "input_schema": {"type": "object", "properties": {
    "by": {"type": "array", "items": {"type": "object", "properties": {
        "org": {"type": "string"}, "evidence": {"type": "string"}}, "required": ["org", "evidence"]}},
    "about": {"type": "array", "items": {"type": "string"}}},
    "required": ["by", "about"]}}

client = anthropic.Anthropic()

def run(row):
    user = f"Title: {row['title']}\nAuthors (forum usernames): {row['authors']}\n\nPost text:\n{bodies.get(row['id'], '')}"
    err = None
    for attempt in range(5):
        try:
            r = client.messages.create(model=MODEL, max_tokens=600, system=SYSTEM, tools=[TOOL],
                                       messages=[{"role": "user", "content": user}])
            out = next((b.input for b in r.content if b.type == "tool_use"), None)
            if out:
                return {"id": row["id"], "title": row["title"], **out}
            err = "no tool call"
        except Exception as e:
            err = str(e)
            time.sleep(20 * (attempt + 1) if "429" in err else 2)
    return {"id": row["id"], "title": row["title"], "error": err}

done = set()
if os.path.exists(out_p):
    good = [json.loads(l) for l in open(out_p) if '"error"' not in l]
    done = {g["id"] for g in good}
    with open(out_p, "w") as f:
        f.writelines(json.dumps(g) + "\n" for g in good)
rows = [r for r in csv.DictReader(open(inp)) if r["id"] not in done]
with cf.ThreadPoolExecutor(4) as ex, open(out_p, "a") as f:
    for res in ex.map(run, rows):
        f.write(json.dumps(res) + "\n"); f.flush()
print("done; errors:", sum('"error"' in l for l in open(out_p)))
