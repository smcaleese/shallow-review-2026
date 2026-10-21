"""Render the exact prompts every Claude-calling step sends into prompts/*.md.

Runs each script with PRINT_PROMPT=1 (prints system prompt, tool schema and one
example user turn, makes no API call) and writes a readable markdown file.
Run from the jord-facets folder after fetching bodies (data/bodies.json):

    python src/render_prompts.py
"""
import json, os, subprocess, sys

R = "../scraping-scripts/AF-and-LW-scraper/results"
T = "../main-pipeline/data/taxonomy.yaml"
EXAMPLE_TEXT_CHARS = 1200   # keep example post text short in the rendered file

STEPS = [
    ("1-scope-check", "Scope check (Sonnet 5.5)",
     "Strict technical-AI-safety screen over every post Stephen's filter kept. Input is the excerpt only.",
     ["src/scope_check.py", f"{R}/1-lw-posts-raw.csv", f"{R}/2-lw-posts-rated.csv", "/dev/null"]),
    ("2-roster", "Author roster draft (Opus 5.5)",
     "One call listing all authors with sample titles and any affiliation stated in their posts; high-confidence entries only. "
     "The output was then corrected by the simulated readers (see roster.json `source`).",
     ["src/roster_pass.py", "data/2-notable-posts.csv", "data/roster_seed.json", "vocab.yaml", "/dev/null"]),
    ("3-tag", "Tagging, all facets (Sonnet 5.5)",
     "The main tagger. The system prompt is generated from vocab.yaml and the 2025 taxonomy, so it changes when the vocabulary does. "
     "In rounds 2-3, earlier reviewer notes for a post were appended to the user turn (6th argument; `-` here = none).",
     ["src/tag.py", "data/2-notable-posts.csv", "data/bodies.json", "vocab.yaml", T, "roster.json", "-", "/dev/null"]),
    ("4-patch", "Targeted patch pass (Sonnet 5.5)",
     "Only for posts with reviewer findings: check each finding against the text and change only the fields it concerns. "
     "Example shown uses round-3 findings.",
     ["src/patch_pass.py", "data/3-tags-raw.jsonl", "review/r3/findings_*.jsonl", "data/bodies.json", "vocab.yaml", "/dev/null"]),
]

os.makedirs("prompts", exist_ok=True)
for slug, title, blurb, cmd in STEPS:
    out = subprocess.run([sys.executable] + cmd, env={**os.environ, "PRINT_PROMPT": "1"},
                         capture_output=True, text=True)
    if out.returncode != 0:
        sys.exit(f"{slug} failed:\n{out.stderr}")
    d = json.loads(out.stdout.strip().splitlines()[-1])
    ex = d["example_user"]
    marker = "Post text (start and end"
    if marker in ex:
        head, tail = ex.split(marker, 1)
        ex = head + marker + tail[:EXAMPLE_TEXT_CHARS] + "\n[... example truncated ...]"
    elif "Excerpt:\n" in ex:
        head, tail = ex.split("Excerpt:\n", 1)
        ex = head + "Excerpt:\n" + tail[:EXAMPLE_TEXT_CHARS] + "\n[... example truncated ...]"
    parts = [f"# {title}\n", f"{blurb}\n", f"- Script: `{cmd[0]}`\n- Model: `{d['model']}`\n- Output is forced through the tool below.\n"]
    if d["system"]:
        parts += ["## System prompt\n", "```text\n" + d["system"] + "\n```\n"]
    parts += ["## Tool schema\n", "```json\n" + json.dumps(d["tool"], indent=1, ensure_ascii=False) + "\n```\n",
              "## Example user turn\n", "```text\n" + ex + "\n```\n"]
    open(f"prompts/{slug}.md", "w").write("\n".join(parts))
    print("wrote", f"prompts/{slug}.md")
