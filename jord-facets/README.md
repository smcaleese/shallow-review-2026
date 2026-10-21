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
run_pipeline.sh         one command: tag new posts, re-apply reviewed corrections, rebuild site + CSV
vocab.yaml              tag vocabulary v3 (definitions, aliases, rules)
roster.json             author -> org roster, date-aware (until/then); DRAFT, needs human check
scope_overrides.json    include/exclude decisions on borderline posts (from reviewer rounds)
prompts/                the exact prompts every Claude call uses (rendered from the code) + reader-review prompts
src/                    the pipeline scripts
data/                   outputs of each stage; data/lw-posts-tagged.csv is the main export
review/r1..r4/          findings from each round of simulated-reader review (JSONL)
review/final-views/     final tags as markdown, grouped by each facet (easy to skim on GitHub)
site/index.html         the interactive page (self-contained)
archive/pilot/          earlier schema/tagger versions, kept for reference
```

## Running it

```bash
./jord-facets/run_pipeline.sh            # tag any new notable posts, rebuild site + CSV + views
./jord-facets/run_pipeline.sh --scrape   # first re-scrape LW and re-run the relevance filter (Stephen's scraper)
./jord-facets/run_pipeline.sh --offline  # no API calls: re-apply corrections and rules, rebuild outputs
```

Needs `ANTHROPIC_API_KEY` (env or `jord-facets/.env`, gitignored) and `pip install anthropic pyyaml`.
Re-running is cheap: every Claude step skips posts it has already done, and corrected tags stay frozen
because the patch files are re-applied on top. `AS_OF=YYYY-MM-DD` overrides the date used for karma/month.
Post text is fetched from the LessWrong API into `data/bodies.json`, which is not committed.

Steps, in order (each is a plain script with explicit paths; see `run_pipeline.sh`):

| Step | Script | Claude? | What it does |
|---|---|---|---|
| 1 | `src/scope_check.py` | Sonnet 5.5 | Strict technical-AI-safety check on everything Stephen's filter rated relevant |
| 2 | `src/select_notable.py` | – | Notable = union of top-N by karma, AF karma, comments, karma/month among in-scope AI-tagged posts |
| 3 | `src/fetch_bodies.py` | – | Post text, start + end, so affiliations and acknowledgements survive |
| 4 | `src/tag.py` | Sonnet 5.5 | All facets incl. by-org with evidence; prompt built from `vocab.yaml` |
| 5 | `src/apply_patches.py`, `src/postprocess.py` | – | Reviewed corrections + scope decisions, then rules enforced in code (each change logged in `pp`) |
| 6 | `src/build_page.py`, `src/export_csv.py`, `src/make_views.py` | – | Site, CSV, markdown views |

One-off: `src/roster_pass.py` (Opus 5.5) drafted `roster.json`; readers then corrected it.

### Prompts

`prompts/1-scope-check.md`, `2-roster.md`, `3-tag.md`, `4-patch.md` show each call exactly as sent: the system
prompt, the tool schema the output is forced through, and one example user turn. They are rendered from
the code (`PRINT_PROMPT=1` makes any of those scripts print its prompt and exit without calling the API), so
after editing `vocab.yaml` or a script, re-render with `python src/render_prompts.py`.
`prompts/5-readers.md` has the simulated-reader prompts for all four review rounds.

### Reviewing and correcting tags

1. Someone (a human, or reader agents using `prompts/5-readers.md`) writes findings as JSON lines, one per
   problem: `{"id": "<post id>", "facet": ..., "type": ..., "current": ..., "proposed": ..., "reason": ...}`.
   Use `"type": "scope"` with `"proposed": "include"|"exclude"` for scope calls.
2. `python src/patch_pass.py data/3-tags-raw.jsonl 'review/<round>/findings_*.jsonl' data/bodies.json vocab.yaml data/4c-patches-<round>.jsonl`
   checks each finding against the post text and changes only the fields it concerns.
3. Add scope decisions to `scope_overrides.json`; fix systematic problems in `vocab.yaml` or `src/postprocess.py`.
4. `./run_pipeline.sh --offline` to rebuild.

### CSV export

`data/lw-posts-tagged.csv` has one row per in-scope post. Column names follow Stephen's
`taxonomy/output/arxiv-papers-tagged.csv` where the meaning matches (`title, authors, published, url,
summary, evidence, contribution_primary, contribution_secondary, paper_type, concept, method, agenda_2025,
new_agenda, tags`), plus `source = lesswrong` and LW-only columns (`phenomenon, substrate, by_org,
by_org_basis, by_org_evidence, about, karma, alignment_forum, scope, rule_changes`). Multi-valued cells
are joined with `; `. **Tag values use this folder's vocabulary, not `taxonomy/facets.yaml`**, so the two
CSVs stack row-wise but their facet values need mapping before they share one site.

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
