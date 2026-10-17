# Faceted tagging for the LessWrong / AF sources (Jord + Claude)

A prototype of a **switchable-taxonomy** view of the review. Every post gets tags on independent
facets. A taxonomy is then just a choice of which facet is the top-level section and which is the
second level. The LW post can pick one view; a website can let readers switch, and tags work as
booru-style filters (`+concept:reward_hacking -evidence:argued`).

**Status:** pilot on the 188 most notable 2026 LW/AF posts, of which 157 are in scope. The tags went through
four rounds of review by simulated LW readers (4 Opus 5.5 instances per round). Humans have not reviewed them yet.

Open `site/index.html` in a browser to use it. It is a single self-contained file.

## Facets

| Facet | Question it answers | Notes |
|---|---|---|
| `evidence` | tested / observed / argued | Derived in code from post type and move. The most useful single filter on LW. |
| `meta` (post type) | research output, research agenda, position, incident report, review, … | |
| `scientific` | what scientific move the work makes | Jord's framing; one primary, 0–2 secondary. |
| `concept` | what properties of AI systems it is about | e.g. reward_seeking, eval_awareness, scheming |
| `phenomenon` | named observed effects | most specific only; no stacking |
| `method` | methods it uses or directly studies | not methods merely mentioned |
| `substrate` | what experiments ran on | argued posts are `no_system` |
| `agenda` | closest 2025 Shallow Review leaf, or a new 2026 agenda | lab leaves only for posts *by* that lab |
| `by` (org) | who **produced** the work | each tag has a basis (`stated` + evidence snippet, or `author_roster`) |
| `about` | whose models/practices are studied | |

The vocabulary, with definitions, aliases and rules, is in `vocab.yaml`.

## Layout

```
vocab.yaml              tag vocabulary v3 (definitions, aliases, rules)
roster.json             author -> org roster, date-aware (until/then); DRAFT, needs human check
scope_overrides.json    include/exclude decisions on borderline posts (from reviewer rounds)
src/                    the pipeline (below)
data/                   outputs of each stage
review/r1..r4/          findings from each round of simulated-reader review (JSONL)
review/final-views/     final tags as markdown, grouped by each facet (easy to skim on GitHub)
site/index.html         the interactive prototype
archive/pilot/          earlier schema/tagger versions, kept for reference
```

## Pipeline

All scripts take explicit paths. Steps 1 and 3–5 call Claude and need `ANTHROPIC_API_KEY`.
Input is Stephen's scrape: `../scraping-scripts/AF-and-LW-scraper/results/1-lw-posts-raw.csv`
and `2-lw-posts-rated.csv`.

```bash
R=../scraping-scripts/AF-and-LW-scraper/results
T=../main-pipeline/data/taxonomy.yaml

# 1. strict technical-AI-safety scope check on everything Stephen's filter kept (Sonnet)
python src/scope_check.py $R/1-lw-posts-raw.csv $R/2-lw-posts-rated.csv data/1-scope-first-pass.jsonl
# 2. notable = union of top-N by karma, AF karma, comments, karma/month, among in-scope AI-tagged posts
python src/select_notable.py $R/1-lw-posts-raw.csv data/2-notable-posts.csv 2026-10-10 data/1-scope-first-pass.jsonl
# 3. fetch post text (start + end, so affiliations/acknowledgements survive) -- not committed, re-fetch
python src/fetch_bodies.py data/2-notable-posts.csv data/bodies.json
# 4. tag every facet (Sonnet), with optional reviewer notes from a previous round
python src/tag.py data/2-notable-posts.csv data/bodies.json vocab.yaml $T roster.json - data/3-tags-raw.jsonl
# 5. targeted corrections for posts with reviewer findings (only flagged fields change)
python src/patch_pass.py data/3-tags-raw.jsonl 'review/r3/findings_*.jsonl' data/bodies.json vocab.yaml data/4a-patches-round3.jsonl
# 6. apply patches + scope decisions, then enforce rules in code (each change is logged in `pp`)
python src/apply_patches.py data/3-tags-raw.jsonl /tmp/patched.jsonl scope_overrides.json data/4a-patches-round3.jsonl data/4b-patches-round4.jsonl
python src/postprocess.py /tmp/patched.jsonl data/bodies.json roster.json data/5-tags-final.jsonl scope_overrides.json
# 7. build the page and the per-facet markdown views
python src/build_page.py data/5-tags-final.jsonl vocab.yaml $T src/template.html site/index.html
python src/make_views.py site/index.html review/final-views
```

`src/roster_pass.py` drafted `roster.json` (stated affiliations in the posts + Opus knowledge,
high-confidence only); readers then corrected it by hand.

## What we learned (short)

- **Stephen's relevance filter lets strategy and governance through.** Its prompt lists "research agendas and strategy" as
  in scope. Ranked by karma, 108 of the top 260 AI-tagged posts were governance, fiction or community posts.
- **On LW, scientific move works poorly as the top-level view.** 93 of 157 posts are `argued`, so every move's section
  mixes experiments with essays. Post type or evidence on top, with move as the second level, reads much better.
  Move as the top level may work for arXiv; test it on the arXiv side.
- **The LLM tagger reliably broke mechanical rules**: experiment substrates on essays, stacked phenomena,
  roster misuse. These are now enforced in `src/postprocess.py` instead of the prompt.
- **Full re-tags undid earlier fixes.** Converging needed frozen tags plus targeted patches.

## Known gaps

- Human spot-check needed: the readers (Opus) and tagger (Sonnet) are both Claude and may share blind spots.
- `roster.json`: about 15 entries come from model knowledge. Missing authors include Francis Rhys Ward, Dewi Gould and Rauno Arike.
- 89 in-scope posts have no producing org. Many are independent work; some are roster gaps.
- Scope calls on the 39 borderline posts were made by simulated readers.
- Fixes from round 4 were applied but no reader has re-checked them.
