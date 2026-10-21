"""Tag posts with vocab v2/v3 (all facets incl. by/about attribution), using
reviewer notes from the previous round where present.

Usage: python tag_v2.py IN_CSV BODIES_JSON VOCAB_YAML TAXONOMY_YAML ROSTER_JSON NOTES_JSON OUT_JSONL
Needs ANTHROPIC_API_KEY. Resumes from OUT_JSONL.
"""
import csv, json, os, sys, time, yaml, concurrent.futures as cf
from urllib.parse import urlparse
import anthropic

inp, bodies_p, vocab_p, tax_p, roster_p, notes_p, out_p = sys.argv[1:8]
MODEL = "claude-sonnet-5-5"
V = yaml.safe_load(open(vocab_p))
bodies = json.load(open(bodies_p))
roster = json.load(open(roster_p))
notes = json.load(open(notes_p)) if notes_p != "-" else {}

LAB_LEAVES = {"openai", "google_deepmind", "anthropic", "xai", "meta", "china", "others"}
leaves = []
def walk(nodes, path=()):
    for n in nodes:
        if n.get("children"):
            walk(n["children"], path + (n["name"],))
        else:
            tag = " [ONLY if the post is BY this lab]" if n["id"] in LAB_LEAVES else ""
            leaves.append(f'{n["id"]} ({" > ".join(path + (n["name"],))}){tag}')
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

SYSTEM = f"""You tag posts for the Shallow Review of Technical AI Safety 2026. Readers are expert researchers who will notice sloppy tags. Use ONLY the listed tag ids.

GENERAL RULES
- Tag what the post is ABOUT and what it DOES. Never tag a concept or method because it is mentioned in passing, listed, or argued to be absent.
- Fewer, accurate tags beat many loose ones. Empty lists are fine.
- Judge from the text, not the title.

SCOPE: "include" = technical AI safety (empirical, theory, conceptual/threat models, metascience, technical agendas). "exclude" = governance/policy, forecasting/timelines, non-technical strategy, careers, community/field news, fiction, pure capabilities, ML theory with no safety angle. "borderline" only when expert reviewers would genuinely split.

META — post type (1, rarely 2):
{block('meta')}

SCIENTIFIC — the scientific move. Exactly one primary; 0-2 secondary only if substantial parts of the post:
{block('scientific')}

CONCEPT (0-4):
{block('concept')}

PHENOMENON (0-3; most specific only):
{block('phenomenon')}

METHOD (0-4):
{block('method')}

SUBSTRATE (1-2):
{block('substrate')}

AGENDA_2025 (0-2): closest leaf of last year's review taxonomy. If none fits, use "new:<id>" preferring these canonical new agendas: {", ".join(V['agenda_new_2026'])}. Coin a new one only if clearly needed.
{chr(10).join(leaves)}

BY — organisations that PRODUCED the work. Each needs a basis:
- "stated": the post shows it (affiliation line, "at X we", official org post, "done as part of MATS/Anthropic Fellows", crosspost from the org's blog). Give a short verbatim evidence snippet.
- "author_roster": an author is listed in the roster below AND the post presents research or an agenda (meta research_output, research_agenda, org_update, open_questions). Personal essays, opinions, reviews and field observations by staff do NOT get a roster-based by-tag. Evidence = "roster: <author>".
NOT a basis: the post studies or discusses the org or its models; advisors or a single collaborator among many; thanks/funders; an author's past or future employer; a platform that hosts a challenge; any post saying it is written "in a personal capacity" or "views are my own".
Work done in a programme (MATS, SPAR, Anthropic Fellows) is tagged with the programme; add the mentor's lab only if the post states it was done at the lab.
Programmes are separate orgs (MATS, Anthropic Fellows, Astra Fellowship (Constellation)). University-led work: org "Academic" with the university in evidence.
Canonical org names: {", ".join(V['org'])}.

ABOUT — developers whose models are experimental subjects or whose practices are a main topic (not passing mentions, not a model used only as a judge). Use: {", ".join(V['developers'])}.

`why`: one sentence on what the post does. `suggest`: up to 2 tags you wished existed, or empty.
Always respond by calling tag_post exactly once. List fields must be JSON arrays."""

def arr(enum=None, desc=None):
    d = {"type": "array", "items": {"type": "string", **({"enum": list(enum)} if enum else {})}}
    if desc: d["description"] = desc
    return d
TOOL = {"name": "tag_post", "description": "Record tags.", "input_schema": {"type": "object", "properties": {
    "scope": {"type": "string", "enum": ["include", "exclude", "borderline"]},
    "scope_reason": {"type": "string"},
    "meta": arr(V["meta"]), "scientific_primary": {"type": "string", "enum": list(V["scientific"])},
    "scientific_secondary": arr(V["scientific"]), "concept": arr(V["concept"]), "phenomenon": arr(V["phenomenon"]),
    "method": arr(V["method"]), "substrate": arr(V["substrate"]), "agenda_2025": arr(),
    "by": {"type": "array", "items": {"type": "object", "properties": {
        "org": {"type": "string"}, "basis": {"type": "string", "enum": ["stated", "author_roster"]},
        "evidence": {"type": "string"}}, "required": ["org", "basis", "evidence"]}},
    "about": arr(V["developers"]), "why": {"type": "string"}, "suggest": arr()},
    "required": ["scope", "scope_reason", "meta", "scientific_primary", "scientific_secondary", "concept", "phenomenon",
                 "method", "substrate", "agenda_2025", "by", "about", "why", "suggest"]}}

client = None if os.environ.get("PRINT_PROMPT") else anthropic.Anthropic()
KEEP = ["id", "title", "url", "link_url", "authors", "posted", "karma", "af_karma", "comment_count", "af", "picked_by"]

def org_at(a, date):
    e = roster.get(a)
    if not e or e.get("roster_tags") is False:
        return None
    if e.get("until") and date >= e["until"]:
        return e.get("then")
    return e["org"]

def build_user(row):
    auths = [a.strip() for a in row["authors"].split(",") if a.strip()]
    ro = [f"{a}: {org_at(a, row['posted'])}" for a in auths if org_at(a, row["posted"])]
    user = f"Title: {row['title']}\nAuthors (forum usernames): {row['authors']}\nForum tags: {row['tags']}\n"
    if row.get("link_url"):
        user += f"Crossposted from / links to: {row['link_url']} (domain {urlparse(row['link_url']).netloc})\n"
    user += f"Author roster matches: {'; '.join(ro) if ro else 'none'}\n"
    if row["id"] in notes:
        user += ("\nReviewer notes from an earlier tagging round (they refer to older tag names and may be wrong; "
                 "check each against the text and follow it only where the text supports it):\n- " + "\n- ".join(notes[row["id"]]) + "\n")
    user += f"\nPost text (start and end; middle may be omitted):\n{bodies.get(row['id'], row.get('excerpt', ''))}"
    return user

def tag(row):
    user = build_user(row)
    err = None
    for attempt in range(5):
        try:
            r = client.messages.create(model=MODEL, max_tokens=1200, system=SYSTEM, tools=[TOOL],
                                       messages=[{"role": "user", "content": user}])
            out = next((b.input for b in r.content if b.type == "tool_use"), None)
            if out:
                return {**{k: row.get(k, "") for k in KEEP}, **out}
            err = "no tool call"
        except Exception as e:
            err = str(e)
            time.sleep(20 * (attempt + 1) if "429" in err else 2)
    return {"id": row["id"], "title": row["title"], "error": err}


# PRINT_PROMPT=1 python ... : print the exact prompt (system, tool schema, one example user turn) and exit.
if os.environ.get("PRINT_PROMPT"):
    print(json.dumps({"model": MODEL, "system": SYSTEM, "tool": TOOL, "example_user": build_user(next(iter(csv.DictReader(open(inp)))))}, ensure_ascii=False))
    sys.exit(0)

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
print("errors:", sum('"error"' in l for l in open(out_p)))
