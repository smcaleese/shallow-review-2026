"""Draft an author -> organisation roster for the posts' authors.

Usage: python roster_pass.py IN_CSV ROSTER_SEED_JSON VOCAB_YAML OUT_JSON
Uses claude-opus-5-5. Output is a DRAFT for human review: only high-confidence entries.
"""
import csv, json, sys, collections, yaml
import anthropic

inp, seed_p, vocab_p, out_p = sys.argv[1:5]
rows = list(csv.DictReader(open(inp)))
seed = json.load(open(seed_p))
orgs = list(yaml.safe_load(open(vocab_p))["org"])
by_author = collections.defaultdict(list)
for r in rows:
    for a in r["authors"].split(","):
        if a.strip():
            by_author[a.strip()].append(r["title"][:80])

lines = []
for a, titles in sorted(by_author.items()):
    s = f"- {a}: " + " | ".join(titles[:4])
    if a in seed:
        s += f"  [stated affiliation in one of these posts: {', '.join(seed[a])}]"
    lines.append(s)

PROMPT = f"""Below are LessWrong usernames of authors of 2026 AI safety posts, each with some of their post titles.
For each author whose main research affiliation in 2026 you are CONFIDENT about, give the organisation.
Rules:
- Only confident, specific knowledge. Omit anyone you are unsure about; omission is fine and expected for most.
- Programmes (MATS, Anthropic Fellows, SPAR) count only if the bracketed note says so.
- If someone moved orgs, give the 2026 one if you know it, else omit.
- Prefer these canonical names: {", ".join(orgs)}.
- confidence: "high" only. Do not output medium/low.

Authors:
{chr(10).join(lines)}

Respond by calling the roster tool once."""

TOOL = {"name": "roster", "description": "Author affiliations.", "input_schema": {"type": "object", "properties": {
    "entries": {"type": "array", "items": {"type": "object", "properties": {
        "author": {"type": "string"}, "org": {"type": "string"}, "note": {"type": "string"}},
        "required": ["author", "org"]}}}, "required": ["entries"]}}

client = anthropic.Anthropic()
r = client.messages.create(model="claude-opus-5-5", max_tokens=8000, tools=[TOOL],
                           messages=[{"role": "user", "content": PROMPT}])
out = next(b.input for b in r.content if b.type == "tool_use")
entries = out["entries"] if isinstance(out["entries"], list) else json.loads(out["entries"])
roster = {e["author"]: {"org": e["org"], "note": e.get("note", ""), "source": "stated" if e["author"] in seed else "model_knowledge"}
          for e in entries}
json.dump(roster, open(out_p, "w"), indent=1, ensure_ascii=False)
print(len(roster), "authors with an affiliation;", collections.Counter(v["org"] for v in roster.values()).most_common())
