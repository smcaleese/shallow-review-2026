"""Scope-check and facet-tag forum posts for the Shallow Review 2026.

Usage: python tag_posts.py IN_CSV BODIES_JSON SCHEMA_YAML TAXONOMY_YAML OUT_JSONL
Needs ANTHROPIC_API_KEY. Resumes: ids already in OUT_JSONL (without error) are skipped.
"""
import csv, json, os, sys, time, yaml, concurrent.futures as cf
import anthropic

inp, bodies_p, schema_p, tax_p, out_p = sys.argv[1:6]
MODEL = "claude-sonnet-5-5"

schema = yaml.safe_load(open(schema_p))
bodies = json.load(open(bodies_p)) if bodies_p != "-" else {}
tax = yaml.safe_load(open(tax_p))["taxonomy"]
leaves = []
def walk(nodes, path=()):
    for n in nodes:
        kids = n.get("children", [])
        if kids:
            walk(kids, path + (n["name"],))
        else:
            leaves.append(f'{n["id"]} ({" > ".join(path + (n["name"],))})')
walk(tax)

mot = schema["motivation"]
mot_txt = "\n".join(f'- {k}: {v["def"]}' + (f' Edge case: {v["edge"]}' if v.get("edge") else "") for k, v in mot.items())

SYSTEM = f"""You review posts for the Shallow Review of Technical AI Safety 2026, a map of technical AI safety research.

STEP 1 — SCOPE. Decide whether the post is technical AI safety work.
IN scope: empirical results, theory, conceptual arguments about alignment problems, threat models, metascience of safety research (replications, critiques of evals/methods), technical research agendas, benchmarks, tools, incident analyses with technical content.
OUT of scope: governance and policy, forecasting and timelines, AI strategy/plans that are not about technical research (e.g. coordinated slowdowns, "Plan A"-style geopolitics), careers and personal stories, community/field news, fiction, general rationality, capabilities without safety content, opinion pieces without technical substance.
Use "borderline" only when a reasonable reviewer could go either way; say why.

STEP 2 — TAGS (fill in even for out-of-scope posts, best effort).

MOTIVATION — what scientific move the work makes. Exactly one primary; 0-2 secondary only if they are substantial parts of the work.
{mot_txt}

OBJECT (1-3): {", ".join(schema["object"])}
If none fit, use "other" and give object_other.

METHOD (1-3): {", ".join(schema["method"])}

SUBSTRATE (1-2): {", ".join(schema["substrate"])}

AGENDA (0-2): ids from last year's review taxonomy below, or "new:<short_snake_name>" if the work belongs to an agenda not listed.
{chr(10).join(leaves)}

ORGS: organisations evident from the text (affiliations, acknowledgements, "at X we..."). Empty list if unclear. Do not guess from author names alone.

Keep `why` to one short sentence describing what the post does.
Always respond by calling the tag_post tool exactly once. All list fields must be JSON arrays."""

arr = lambda enum=None: {"type": "array", "items": {"type": "string", **({"enum": enum} if enum else {})}}
TOOL = {
    "name": "tag_post",
    "description": "Record the scope decision and facet tags for a post.",
    "input_schema": {
        "type": "object",
        "properties": {
            "scope": {"type": "string", "enum": ["include", "exclude", "borderline"]},
            "scope_reason": {"type": "string"},
            "motivation_primary": {"type": "string", "enum": list(mot)},
            "motivation_secondary": arr(list(mot)),
            "object": arr(schema["object"]),
            "object_other": {"type": "string"},
            "method": arr(schema["method"]),
            "substrate": arr(schema["substrate"]),
            "agenda": arr(),
            "orgs": arr(),
            "why": {"type": "string"},
        },
        "required": ["scope", "scope_reason", "motivation_primary", "motivation_secondary",
                     "object", "method", "substrate", "agenda", "orgs", "why"],
    },
}

client = anthropic.Anthropic()
KEEP = ["id", "title", "url", "authors", "posted", "karma", "af_karma", "comment_count", "af", "picked_by"]

def tag(row):
    text = bodies.get(row["id"]) or row.get("excerpt", "")
    user = (f"Title: {row['title']}\nAuthors: {row['authors']}\nForum tags: {row['tags']}\n"
            f"Karma: {row['karma']}  Comments: {row['comment_count']}\n\nPost text (may be truncated):\n{text}")
    err = None
    for attempt in range(5):
        try:
            r = client.messages.create(model=MODEL, max_tokens=900, system=SYSTEM, tools=[TOOL],
                                       messages=[{"role": "user", "content": user}])
            out = next((b.input for b in r.content if b.type == "tool_use"), None)
            if out:
                return {**{k: row.get(k, "") for k in KEEP}, **out}
            err = "no tool call"
        except Exception as e:
            err = str(e)
            time.sleep(20 * (attempt + 1) if '429' in err else 2)
    return {"id": row["id"], "title": row["title"], "error": err}

done = set()
if os.path.exists(out_p):
    lines = [json.loads(l) for l in open(out_p)]
    good = [l for l in lines if "error" not in l]
    done = {l["id"] for l in good}
    with open(out_p, "w") as f:
        f.writelines(json.dumps(l) + "\n" for l in good)

rows = [r for r in csv.DictReader(open(inp)) if r["id"] not in done]
with cf.ThreadPoolExecutor(4) as ex, open(out_p, "a") as f:
    for res in ex.map(tag, rows):
        f.write(json.dumps(res) + "\n"); f.flush()
        print(res.get("scope", "ERR"), res.get("motivation_primary", ""), "|", res["title"][:70], flush=True)
