"""Tag posts with the v1 vocabulary (vocab.yaml).

Usage: python tag_v1.py IN_CSV BODIES_JSON VOCAB_YAML TAXONOMY_YAML OUT_JSONL
Needs ANTHROPIC_API_KEY. Resumes from OUT_JSONL.
"""
import csv, json, os, sys, time, yaml, concurrent.futures as cf
import anthropic

inp, bodies_p, vocab_p, tax_p, out_p = sys.argv[1:6]
MODEL = "claude-sonnet-5-5"
V = yaml.safe_load(open(vocab_p))
bodies = json.load(open(bodies_p))

leaves = []
def walk(nodes, path=()):
    for n in nodes:
        if n.get("children"):
            walk(n["children"], path + (n["name"],))
        else:
            leaves.append(f'{n["id"]} ({" > ".join(path + (n["name"],))})')
walk(yaml.safe_load(open(tax_p))["taxonomy"])

def block(facet):
    out = []
    for k, v in V[facet].items():
        v = v or {}
        s = f"- {k}"
        if v.get("def"): s += f": {v['def']}"
        if v.get("aliases"): s += f" (covers: {', '.join(map(str, v['aliases']))})"
        out.append(s)
    return "\n".join(out)

LIMITS = {"meta": "1-2", "concept": "0-4", "phenomenon": "0-3", "method": "0-4", "substrate": "1-2"}
SYSTEM = f"""You tag posts for the Shallow Review of Technical AI Safety 2026. Use ONLY the tag ids listed. Tag what the work is about and what it does, not every term it mentions in passing.

SCOPE: technical AI safety (empirical, theory, conceptual, threat models, metascience, technical agendas) is "include". Governance/policy, forecasting, non-technical strategy, careers, community news, fiction: "exclude". "borderline" when reasonable reviewers would disagree.

META — what kind of post ({LIMITS['meta']}):
{block('meta')}

SCIENTIFIC — what scientific move the work makes. Exactly one primary; 0-2 secondary only if substantial:
{block('scientific')}

CONCEPT — abstractions/properties of AI systems the work is about ({LIMITS['concept']}):
{block('concept')}

PHENOMENON — named observed effects the work is about ({LIMITS['phenomenon']}):
{block('phenomenon')}

METHOD — methodology used or studied ({LIMITS['method']}):
{block('method')}

SUBSTRATE ({LIMITS['substrate']}):
{block('substrate')}

ORG — organisations evident from the text (affiliations, "at X we", acknowledgements, program the work came from). Use these canonical names when they match; put any other org in org_other. Do not guess from author names alone.
{', '.join(V['org'])}

AGENDA_2025 (0-2): closest leaf from last year's review taxonomy, or "new:<short_snake_name>":
{chr(10).join(leaves)}

`why`: one short sentence saying what the post does.
`suggest`: up to 2 tags you wished existed (snake_case), or empty.
Always respond by calling tag_post exactly once. List fields must be JSON arrays."""

def arr(enum=None):
    return {"type": "array", "items": {"type": "string", **({"enum": list(enum)} if enum else {})}}
TOOL = {"name": "tag_post", "description": "Record tags.", "input_schema": {"type": "object", "properties": {
    "scope": {"type": "string", "enum": ["include", "exclude", "borderline"]},
    "meta": arr(V["meta"]), "scientific_primary": {"type": "string", "enum": list(V["scientific"])},
    "scientific_secondary": arr(V["scientific"]), "concept": arr(V["concept"]), "phenomenon": arr(V["phenomenon"]),
    "method": arr(V["method"]), "substrate": arr(V["substrate"]), "org": arr(V["org"]), "org_other": arr(),
    "agenda_2025": arr(), "why": {"type": "string"}, "suggest": arr()},
    "required": ["scope", "meta", "scientific_primary", "scientific_secondary", "concept", "phenomenon",
                 "method", "substrate", "org", "org_other", "agenda_2025", "why", "suggest"]}}

client = anthropic.Anthropic()
KEEP = ["id", "title", "url", "authors", "posted", "karma", "af_karma", "comment_count", "af", "picked_by", "scope_reason"]

def tag(row):
    text = bodies.get(row["id"]) or row.get("excerpt", "")
    user = f"Title: {row['title']}\nAuthors: {row['authors']}\nForum tags: {row['tags']}\n\nPost text (may be truncated):\n{text}"
    err = None
    for attempt in range(5):
        try:
            r = client.messages.create(model=MODEL, max_tokens=1000, system=SYSTEM, tools=[TOOL],
                                       messages=[{"role": "user", "content": user}])
            out = next((b.input for b in r.content if b.type == "tool_use"), None)
            if out:
                return {**{k: row.get(k, "") for k in KEEP}, **out}
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
print("to tag:", len(rows), flush=True)
with cf.ThreadPoolExecutor(4) as ex, open(out_p, "a") as f:
    for res in ex.map(tag, rows):
        f.write(json.dumps(res) + "\n"); f.flush()
        print(res.get("scope", "ERR"), res.get("scientific_primary", ""), "|", res["title"][:70], flush=True)
