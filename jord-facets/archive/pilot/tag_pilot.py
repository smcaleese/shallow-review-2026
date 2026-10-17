"""Pilot: tag a sample of annotated LW posts with the faceted schema.

Usage: python tag_pilot.py INPUT_CSV SCHEMA_YAML TAXONOMY_YAML OUT_JSONL [N] [SEED]
Needs ANTHROPIC_API_KEY in the environment.
"""
import csv, json, random, sys, yaml, concurrent.futures as cf
import anthropic

inp, schema_p, tax_p, out_p = sys.argv[1:5]
N = int(sys.argv[5]) if len(sys.argv) > 5 else 100
SEED = int(sys.argv[6]) if len(sys.argv) > 6 else 0
MODEL = "claude-sonnet-5-5"

schema = yaml.safe_load(open(schema_p))
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

SYSTEM = f"""You tag AI safety research posts for the Shallow Review of Technical AI Safety 2026.
Tag each post on independent facets. Use only the allowed values.

MOTIVATION — what scientific move the work makes. Pick exactly one primary, plus 0-2 secondary only if they are substantial parts of the work.
{mot_txt}

OBJECT (1-3): {", ".join(schema["object"])}
If none fit, use "other" and give object_other.

METHOD (1-3): {", ".join(schema["method"])}

SUBSTRATE (1-2): {", ".join(schema["substrate"])}

AGENDA (0-2): ids from last year's review taxonomy below, or "new:<short_snake_name>" if the work belongs to an agenda not listed. Leave empty for strategy/meta posts that span many agendas.
{chr(10).join(leaves)}

ORGS: organisations evident from the text or well-known author affiliations (e.g. "Anthropic", "MATS", "Redwood Research"). Empty list if unclear. Do not guess.

Give confidence 1-3 for the primary motivation (3 = clear-cut). Keep `why` to one short sentence.
Always respond by calling the tag_post tool exactly once."""

TOOL = {
    "name": "tag_post",
    "description": "Record facet tags for a post.",
    "input_schema": {
        "type": "object",
        "properties": {
            "motivation_primary": {"type": "string", "enum": list(mot)},
            "motivation_secondary": {"type": "array", "items": {"type": "string", "enum": list(mot)}},
            "motivation_confidence": {"type": "integer", "enum": [1, 2, 3]},
            "object": {"type": "array", "items": {"type": "string", "enum": schema["object"]}},
            "object_other": {"type": "string"},
            "method": {"type": "array", "items": {"type": "string", "enum": schema["method"]}},
            "substrate": {"type": "array", "items": {"type": "string", "enum": schema["substrate"]}},
            "agenda": {"type": "array", "items": {"type": "string"}},
            "orgs": {"type": "array", "items": {"type": "string"}},
            "why": {"type": "string"},
        },
        "required": ["motivation_primary", "motivation_secondary", "motivation_confidence",
                     "object", "method", "substrate", "agenda", "orgs", "why"],
    },
}

client = anthropic.Anthropic()

def tag(row):
    user = (f"Title: {row['title']}\nAuthors: {row['authors']}\nForum tags: {row['tags']}\n"
            f"Summary: {row['summary']}\nExcerpt: {row['excerpt'][:3000]}")
    for attempt in range(3):
        try:
            r = client.messages.create(
                model=MODEL, max_tokens=800, system=SYSTEM,
                tools=[TOOL], tool_choice={"type": "auto"},
                messages=[{"role": "user", "content": user}])
            out = next(b.input for b in r.content if b.type == "tool_use")
            return {"id": row["id"], "title": row["title"], "url": row["url"], "authors": row["authors"],
                    "posted": row["posted"], "karma": row["karma"], "af": row["af"],
                    "summary": row["summary"], **out}
        except Exception as e:
            err = e
    return {"id": row["id"], "title": row["title"], "error": str(err)}

rows = list(csv.DictReader(open(inp)))
random.Random(SEED).shuffle(rows)
rows = rows[:N]
with cf.ThreadPoolExecutor(8) as ex, open(out_p, "w") as f:
    for res in ex.map(tag, rows):
        f.write(json.dumps(res) + "\n")
        print(res.get("motivation_primary", "ERR"), "|", res["title"][:70], flush=True)
