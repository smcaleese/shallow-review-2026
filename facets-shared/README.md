# Shared facets: the Shallow Review 2026 sources

Tags the review's candidate sources with **one vocabulary**, ranks them, keeps a fixed **budget of ~500**, and builds
**one site** where they appear together. Four sources, each badged on the site:

| Source | Candidates | Budget | Notes |
|---|---|---|---|
| arXiv | the top-20% shortlist (303) | 240 | plus papers promoted because a LW post writes them up |
| LessWrong / Alignment Forum | Jord's notable list + the 60 highest-karma in-scope posts it missed | 140 | |
| Org (Lenz's list) | links from 15 AI safety organisations' research pages (`input/lenz-org-sources.md`) | 80 | |
| Safety Stack | dataset documents none of the scrapes had, rated relevant (`../safety-stack`) | 40 | covers Oct 10 onwards, after the scrapes stopped |

Budgets live in `BUDGET` in `src/common.py`. The goal is as many sources as help build the taxonomy, but few enough that
someone could read every source the review includes. Items that are both an arXiv paper and a LW post count as arXiv;
an org or Safety Stack item that duplicates an earlier source is merged into it (badged `+Org` / `+SS`).
`budget-overrides.json` keeps or drops items by hand on top of the budget (it keeps the three main system cards).

This folder sits alongside `taxonomy/` (arXiv only) and `jord-facets/` (LW only), which keep working unchanged. It
reads their outputs; the duplicated tagging and site code can be removed once this site covers both.

## Running it

From the repo root, with `ANTHROPIC_API_KEY` set (or in `facets-shared/.env`, which is gitignored):

```bash
./facets-shared/run_pipeline.sh            # sync inputs, then run every step
./facets-shared/run_pipeline.sh --no-sync  # keep the current input/ snapshot
./facets-shared/run_pipeline.sh --offline  # no API calls: rebuild from cached answers and existing tags
```

Then view the site:

```bash
python3 -m http.server 8767 --directory facets-shared/site
```

and open http://localhost:8767. Reruns are cheap: every Claude step skips items it has already done.

## Steps

| Step | Script | Claude? | What it does |
|---|---|---|---|
| 0 | `sync_inputs.sh` | – | Copies the latest source files into `input/` (see below), parses Lenz's list (`src/parse_lenz_orgs.py`) and records the time in `input/SYNCED_AT` |
| 0b | `src/fetch_lenz_pages.py` | – | Fetches each org link's text (arXiv API, LW API or the page) → `data/1b-lenz-items.jsonl`; cached pages are skipped |
| 1 | `src/load_sources.py` | – | Converts every source to one item format with a `source` field → `data/1-items.jsonl` |
| 2 | `src/fetch_lw_bodies.py` | – | Fetches each post's text and links from the LessWrong API → `cache/lw-bodies.json` (not committed) |
| 3 | `src/dedupe.py` | Sonnet, once per post | Merges LW posts that write up an arXiv paper into the paper, then org and Safety Stack items that duplicate an earlier item → `data/2-items-deduped.jsonl`, `data/2-dedupe-report.csv` |
| 4 | `src/tag.py` | Sonnet, once per item | Tags every facet in `vocab.yaml` → `data/3-tags-raw.jsonl` |
| 5 | `src/postprocess.py` | – | Enforces rules the tagger doesn't follow reliably, logging each change → `data/4-tags-final.jsonl` |
| 6 | `src/rank.py` | Opus, 2 passes per item | Scores impact, novelty and interest against the whole set, plus popularity → `output/rankings.csv`, `output/top-papers.md` |
| 7 | `src/select_budget.py` | – | Keeps the top `BUDGET` items of each source → `data/6-selected.json`, `output/selected-sources.csv` |
| 8 | `src/build_site.py` | – | Writes `site/data.js` (read by `site/index.html`) and `output/items-tagged.csv`, for the selected items only |

`PRINT_PROMPT=1 uv run python src/tag.py` prints the tagging prompt and one example message without calling the API.

## Inputs

The pipeline only reads `input/`, so every site is built from a known snapshot. `sync_inputs.sh` copies:

| File | From |
|---|---|
| `arxiv-papers-shortlisted.csv` | `scraping-scripts/arxiv-scraper/results/shortlisted-20/2026/` (the top-20% shortlist) |
| `arxiv-papers-filtered/<month>.csv` | `scraping-scripts/arxiv-scraper/results/filtered/2026/` (all relevant papers, for dedupe) |
| `lw-notable-posts.csv` | `jord-facets/data/2-notable-posts.csv` |
| `lw-scope-overrides.json` | `jord-facets/scope_overrides.json` (reviewer scope decisions) |
| `lw-roster.json` | `jord-facets/roster.json` (author → org) |
| `lw-posts-raw.csv`, `lw-scope-first-pass.jsonl` | `scraping-scripts/AF-and-LW-scraper/results/1-lw-posts-raw.csv`, `jord-facets/data/1-scope-first-pass.jsonl` (for the extra LW candidates) |
| `safety-stack-filtered.csv` | `safety-stack/output/filtered-sources.csv` |
| `lenz-org-sources.md` | added by hand; `lenz-org-sources.csv` is made from it |
| `taxonomy-2025.yaml` | `taxonomy/input/taxonomy-2025.yaml` (last year's agendas) |

## Deduplication

The arXiv paper is the canonical version of any work. For each post, `dedupe.py` gathers candidate papers from **all**
filtered 2026 arXiv papers (not just the shortlist), using arXiv links and IDs in the post, title similarity, and
Claude's answer to "is this post mainly a write-up of one specific paper, and which?". Then:

| Case | Action |
|---|---|
| Post writes up a shortlisted paper | Merged into the paper, which keeps the LW link and karma |
| Post writes up a filtered paper that wasn't shortlisted | The paper is added ("via LW" badge), with the LW link and karma |
| Post reports new results beyond a paper, critiques one, covers several, or describes work not on arXiv | Kept as a post |

Check `data/2-dedupe-report.csv` (one row per post, with how each decision was made). To correct a decision, add it to
`dedupe-overrides.json`: `{"lw:<post id>": "keep"}` or `{"lw:<post id>": "arxiv:<arXiv id>"}`.

## Vocabulary

`vocab.yaml` merges `jord-facets/vocab.yaml` and `taxonomy/facets.yaml`; its header lists the merge decisions. It is a
**draft to agree with Jord**. Facets: evidence, type, scientific move, concept, phenomenon, method, substrate, agenda
(2025 leaves plus new 2026 agendas), by (producing org) and about (developer studied). The site adds source, scope and
month. Bump `version` after editing it so items get retagged.

Known gaps:
- `by` for arXiv papers is only tagged when the abstract or comment names the org (no affiliations from the PDF yet).
- Jord's reviewed tag patches use his old vocabulary, so they aren't applied here; his scope decisions are.
- Tags come from Claude and haven't been checked by people.
- Org and Safety Stack items have no citations or karma, so the ranker counts them as average popularity; their
  text is a page opening or a substitute abstract, so their scores are rougher than arXiv's.
- One PNAS paper on Lenz's list blocks downloads and is scored on its title alone.

## Deployment

The site is live at https://shallow-review-facets.netlify.app (it replaced the arXiv-only taxonomy site). The repo-root
`netlify.toml` publishes `facets-shared/site` with no build command, so always run `src/build_site.py` before deploying.

To deploy by hand without uploading anything else (such as `.env` files), deploy only the site folder:

```bash
netlify deploy --prod --dir facets-shared/site --site 1676552f-2894-46f1-a3f6-b673fd901536
```
