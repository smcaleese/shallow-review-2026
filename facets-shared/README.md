# Shared facets: arXiv papers + LW/AF posts

Tags the 2026 arXiv shortlist and the most notable LessWrong / Alignment Forum posts with **one vocabulary**, and builds
**one site** where they appear together. Each item is badged as an arXiv paper, a LW/AF post, or both.

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
| 0 | `sync_inputs.sh` | – | Copies the latest source files into `input/` (see below) and records the time in `input/SYNCED_AT` |
| 1 | `src/load_sources.py` | – | Converts papers and posts to one item format with a `source` field → `data/1-items.jsonl` |
| 2 | `src/fetch_lw_bodies.py` | – | Fetches each post's text and links from the LessWrong API → `cache/lw-bodies.json` (not committed) |
| 3 | `src/dedupe.py` | Sonnet, once per post | Merges LW posts that write up an arXiv paper into the paper → `data/2-items-deduped.jsonl`, `data/2-dedupe-report.csv` |
| 4 | `src/tag.py` | Sonnet, once per item | Tags every facet in `vocab.yaml` → `data/3-tags-raw.jsonl` |
| 5 | `src/postprocess.py` | – | Enforces rules the tagger doesn't follow reliably, logging each change → `data/4-tags-final.jsonl` |
| 6 | `src/build_site.py` | – | Writes `site/data.js` (read by `site/index.html`) and `output/items-tagged.csv` |

`PRINT_PROMPT=1 uv run python src/tag.py` prints the tagging prompt and one example message without calling the API.

## Inputs

The pipeline only reads `input/`, so every site is built from a known snapshot. `sync_inputs.sh` copies:

| File | From |
|---|---|
| `arxiv-papers-shortlisted.csv` | `scraping-scripts/arxiv-scraper/results/shortlisted/2026/` (the top-10% shortlist) |
| `arxiv-papers-filtered/<month>.csv` | `scraping-scripts/arxiv-scraper/results/filtered/2026/` (all relevant papers, for dedupe) |
| `lw-notable-posts.csv` | `jord-facets/data/2-notable-posts.csv` |
| `lw-scope-overrides.json` | `jord-facets/scope_overrides.json` (reviewer scope decisions) |
| `lw-roster.json` | `jord-facets/roster.json` (author → org) |
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
