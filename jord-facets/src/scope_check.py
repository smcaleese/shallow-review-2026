"""Strict technical-AI-safety scope check on post excerpts (cheap first pass).

Usage: python scope_check.py RAW_CSV RATED_CSV OUT_JSONL
Pool: posts Stephen's filter rated highly or moderately relevant.
Needs ANTHROPIC_API_KEY. Resumes from OUT_JSONL.
"""
import csv, json, os, sys, time, concurrent.futures as cf
import anthropic

raw_p, rated_p, out_p = sys.argv[1:4]
MODEL = "claude-sonnet-5-5"

SYSTEM = """You screen posts for the Shallow Review of Technical AI Safety 2026, a map of technical AI safety research.
Decide whether the post is technical AI safety work.
IN scope: empirical results, theory, conceptual arguments about alignment problems, threat models, metascience of safety research (replications, critiques of evals/methods), technical research agendas, benchmarks, tools, incident analyses with technical content.
OUT of scope: governance and policy, forecasting and timelines, AI strategy/plans that are not about technical research (e.g. coordinated slowdowns, "Plan A"-style geopolitics), careers and personal stories, community/field news, fiction, general rationality, capabilities without safety content, opinion pieces without technical substance.
Use "borderline" only when a reasonable reviewer could go either way.
Always respond by calling the scope tool exactly once."""

TOOL = {"name": "scope", "description": "Record the scope decision.",
        "input_schema": {"type": "object", "properties": {
            "scope": {"type": "string", "enum": ["include", "exclude", "borderline"]},
            "reason": {"type": "string", "description": "One short sentence."}},
            "required": ["scope", "reason"]}}

client = anthropic.Anthropic()

def check(row):
    user = f"Title: {row['title']}\nAuthors: {row['authors']}\nForum tags: {row['tags']}\n\nExcerpt:\n{row['excerpt'][:2500]}"
    err = None
    for attempt in range(5):
        try:
            r = client.messages.create(model=MODEL, max_tokens=200, system=SYSTEM, tools=[TOOL],
                                       messages=[{"role": "user", "content": user}])
            out = next((b.input for b in r.content if b.type == "tool_use"), None)
            if out:
                return {"id": row["id"], "title": row["title"], **out}
            err = "no tool call"
        except Exception as e:
            err = str(e)
            time.sleep(20 * (attempt + 1) if "429" in err else 2)
    return {"id": row["id"], "title": row["title"], "error": err}

rated = {r["id"]: r["relevance"] for r in csv.DictReader(open(rated_p))}
done = set()
if os.path.exists(out_p):
    good = [json.loads(l) for l in open(out_p) if '"error"' not in l]
    done = {g["id"] for g in good}
    with open(out_p, "w") as f:
        f.writelines(json.dumps(g) + "\n" for g in good)
rows = [r for r in csv.DictReader(open(raw_p))
        if rated.get(r["id"]) in ("highly relevant", "moderately relevant") and r["id"] not in done]
print("to check:", len(rows), flush=True)
with cf.ThreadPoolExecutor(6) as ex, open(out_p, "a") as f:
    for i, res in enumerate(ex.map(check, rows)):
        f.write(json.dumps(res) + "\n"); f.flush()
        if i % 200 == 0:
            print(i, flush=True)
