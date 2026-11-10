# Shallow Review pipeline

Turns a list of candidate URLs and a taxonomy into a first draft of the Shallow Review: every relevant item filed
under a taxonomy category, ready for people to edit. A second tool, `process_draft.py`, parses the edited draft back
into structured data and renders the final document.

Details live in `docs/` (see the end of this file). This README only covers the flow and the commands.

## How it works

```
URL lists ──add──▶ entries table
                        │
                    classify          scrape each URL, then one LLM call with the taxonomy in the prompt:
                        │             1-3 leaf categories with fit scores, title, authors, date, summary
                        ▼
               data/data.db  ◀── import_feedback (human include / exclude / reclassify)
                        │
                      score           citations (Semantic Scholar) or LessWrong karma, then one LLM call per page:
                        │             importance 0-1 from the work's quality, its authors' reputation and that attention
                        ▼
                  export_draft      walk data/taxonomy.yaml, list each category's items (--top N: the N most important)
                        ▼
                   draft.md           one section per category, agenda fields left blank for editors
                        │
               (people edit it)
                        ▼
  process_draft.py parse ─▶ JSON/YAML ─▶ process_draft.py format ─▶ final markdown
```

1. **Add entries.** `src/add_entries.py <file>` reads URLs (a text file with one per line) into the database's
   entries table. `../scraping-scripts/export_for_pipeline.py` writes the arXiv and LessWrong scrapers' results as URL
   lists in `data/sources-links/`.
2. **Classify.** `src/classify_entries.py` scrapes each queued URL (cached in `data/scraped/`) and sends the page to the
   LLM with the whole taxonomy in the system prompt. The LLM returns 1-3 leaf category IDs with fit scores (0-1) and
   basic metadata (title, authors, organizations, date, one-sentence summary). It doesn't judge whether an entry belongs
   in the review: the sources are selected upstream. This is the only step that reads the taxonomy to assign categories.
3. **Score.** `src/score_entries.py` rates how important each classified entry is for the review. It first fetches the
   attention the entry has received: citation counts from Semantic Scholar (arXiv and DOI links by ID, other pages by
   exact title) or karma for LessWrong posts. Then it sends the cached page and that attention, as a rate per month
   since publication, to the LLM. The LLM rates the work's significance, rigor and novelty first, and weighs its
   authors' reputation and the attention as minor factors. It returns an importance score (0-1) and a one-sentence
   reason. The score doesn't depend on the category, so re-classifying doesn't make it stale. Details under "How
   scoring works".
4. **Feedback (optional).** `src/import_feedback.py <csv>` records human decisions, such as including a
   item the classifier missed, excluding one or moving it to another category. Export applies them on top of the LLM's
   output.
5. **Enrich the taxonomy.** `src/enrich_taxonomy.py` makes one LLM call per leaf category with its items, the
   list of all categories and an index of all items, and writes every agenda field (summary, theory of change, see
   also, general approach, target case, key people, critiques) to `taxonomy-enriched.yaml`, a copy of the taxonomy
   with an `agenda` block per category. The hand-written `taxonomy.yaml` is not modified. Agendas already in the
   enriched file are kept (so hand edits survive) unless `--overwrite` or `--only`.
6. **Export the draft.** `src/export_draft.py -o draft.md` walks the taxonomy tree and lists, under each
   category, the classified items filed under it, best fit first. Pruning: with `--min-importance 0.5 --top 10` it
   ranks each category's items by importance and keeps those with importance ≥ 0.5, at most 10 (either option also
   works alone). Entries with equal importance are ranked by their category fit, since the importance scores take only a
   few distinct values. Each
   category gets empty agenda fields (summary, theory of change, key people, ...) for editors to fill in.
7. **Process the edited draft.** After people edit the draft, `process_draft.py parse` splits it into agendas and
   papers, fills paper metadata from the database and uses an LLM to extract agenda attributes. Then
   `process_draft.py format` renders the parsed JSON with `draft_template.md` (or a template in `templates/`).

## Inputs

- **Entries:** URL lists in `data/sources-links/` (one URL per line, `#` for comments) or CSVs. Use `--source <label>`
  when adding so you can filter by provenance later. The 2026 review's selected sources are the `facets-*-2026.txt`
  lists (see "Running on the 2026 selected sources").
- **Taxonomy:** `taxonomy.yaml` in the data folder (`DATA_PATH`, see "Things to watch for"). It's a tree of `id`, `name`, `description` and `children`, and only leaves
  can be assigned. Leaves may also have `examples`, and nodes may have `sr2024` (context from the 2024 review), which
  export prints. Optional top-level `year` and `agenda_fields` set the draft's year and the agenda fields printed
  under each category (see `docs/DATA.md`). It is the only hand-written
  taxonomy file (it holds the 2026 taxonomy); `enrich_taxonomy.py` writes `taxonomy-enriched.yaml` next to it.

## Setup

```bash
uv sync
cp .env.example .env   # add ANTHROPIC_API_KEY (and HELICONE_API_KEY, which `process_draft.py parse` requires)
```

The scripts load `.env` themselves. Run them from this folder with `uv run python ...` (plain `python` uses your
system Python and fails with `ModuleNotFoundError`). Scraping uses Selenium by default (`USE_SELENIUM` in
`shallow_review/scrape.py`); with Playwright, keep `--workers 1`. Each script prints its options with `--help`.

## Usage

Run the scripts from this folder with `uv run python ...`. The pipeline has four phases.

### Phase 1: Taxonomy

1. **Write the taxonomy.** Edit `data/taxonomy.yaml`: a tree of categories with an `id`, `name` and `description`, where only the leaves receive entries.
   Its format is described under "Inputs" and in `docs/DATA.md`.
2. **Enrich it.** An LLM writes each category's agenda fields (summary, theory of change, key people, ...) into a copy of the taxonomy:

| Task | Command | Output |
|---|---|---|
| Write each category's agenda fields | `uv run python src/enrich_taxonomy.py [--only id1,id2] [--overwrite]` | `data/taxonomy-enriched.yaml` (`taxonomy.yaml` is not modified) |

The agendas are written from each category's classified entries, so before phase 3 the fields are left empty. Rerun this
after phase 3 to fill them in; agendas already in the file are kept unless you pass `--overwrite` or `--only`.

### Phase 2: Add the sources

One URL list per source goes into the `entries` table, labelled with the file's name:

| Task | Command | Output |
|---|---|---|
| Queue URLs | `uv run python src/add_entries.py data/sources-links/facets-arxiv-2026.txt` | rows in `data/data.db`, labelled `facets-arxiv-2026` (override with `--source`) |
| Show the number of entries in the `entries` table, and its first rows | `uv run python src/show_info.py [--source X] [--rows N]` | entries by status (`New`, `Done`, `Scrape Errors`, `Classify Errors`); after adding, all are `New`. Then the first 10 rows (`--rows N` for more; the columns are described under "The entries table"). `--source` limits both to one source. Also prints the paths and histograms of the scores |

### Phase 3: Classify and score the sources

Each entry is scraped (the page is cached in `data/scraped/`) and sent to the LLM with the whole taxonomy in the prompt.
The LLM returns 1-3 leaf categories with fit scores and basic metadata, which are saved on the entry. Then each
classified entry gets an importance score (0-1), from its page, the reputation of its authors and its citations or
karma (see step 3 of "How it works"); export uses it to keep each category's most important entries.

| Task | Command | Output |
|---|---|---|
| Scrape and classify the queued entries | `uv run python src/classify_entries.py --limit 500 --workers 4` | categories, fit scores and metadata in `data/data.db` |
| Check progress | `uv run python src/show_info.py` | `New` entries become `Done` |
| Retry entries that failed | `uv run python src/classify_entries.py --retry-errors` | |
| Classify again after changing the taxonomy | `uv run python src/reset_classify.py [--source X] [--remove-scrapes]` | entries are back to `New`; then rerun `classify_entries.py` |
| Score the classified entries | `uv run python src/score_entries.py --limit 500 --workers 12` | `citation_count`, `lw_karma`, `attention_checked_at`, `importance` and `importance_reason` in `data/data.db` (see "How scoring works") |
| Score them all again (after changing `prompts/score.yaml`) | `uv run python src/score_entries.py --limit 500 --workers 12 --rescore` | also looks up all citations and karma again |

#### How scoring works

`score_entries.py` runs in two phases on the classified (`done`) entries that have no `importance` yet (all of them
with `--rescore`).

**1. Attention lookup** (no LLM). For each entry it looks up how much attention the work has received:

| Entry | Looked up | Saved in |
|---|---|---|
| arXiv or DOI link | Semantic Scholar citation count, all entries in one batch call | `citation_count` |
| LessWrong post | karma (`baseScore`) from the LessWrong API, one call per post | `lw_karma` |
| Any other page (org blogs, ...) | Semantic Scholar title search, kept only if the title matches exactly | `citation_count` |

When nothing is found the column stays empty (NULL). Org blog posts are rarely in Semantic Scholar, so most of them stay
empty. The time of the lookup is saved in `attention_checked_at`, so a rerun without `--rescore` skips entries that were
already looked up, found or not; only lookups Semantic Scholar refused are tried again.

The title searches are the slow part: Semantic Scholar has no batch endpoint for them and limits calls without an API
key to about one per second, so the script spaces them 1.1 s apart and backs off when refused (HTTP 429). Lookups that
keep being refused are reported in red, and those entries are scored without citations. A free API key from
semanticscholar.org in `.env` as `SEMANTIC_SCHOLAR_API_KEY` avoids the refusals.

**2. LLM scoring.** Each entry's cached page (from `data/scraped/`, not scraped again) is sent to the LLM with one line
on its attention, for example:

```
Citations (Semantic Scholar): 79 (published 2026-04-09, 7.1 months ago, 11.2 per month)
LessWrong karma: 604 (published 2026-08-26, 2.5 months ago, 241.9 per month)
No citation or karma data (published 2026, 3.9 months ago)
```

The age is counted from the classifier's `date` (a date with only a year counts as 15 July, one with only a month as
the 15th) and is at least one month. Without a date the line gives the total and no rate.

The LLM returns `importance` (0-1) and `importance_reason` (one sentence). The prompt (`prompts/score.yaml`) asks it
to judge first the work itself (significance, rigor, novelty, usefulness to a reader of the agenda), then to adjust a
little for the reputation of the authors and their organization and for the attention, and says that recent work and
missing data are no evidence against importance. Scale: 0.9+ landmark, 0.7-0.9 strong, 0.5-0.7 solid but incremental,
below 0.5 minor.

`importance` is the only score: the reputation and the citations are folded into it, not stored as separate scores.
The category fit from classification is a different thing (how well an entry fits its category, not how good it
is), and `importance` doesn't depend on the category, so re-classifying doesn't make it stale.

`--workers` sets how many LLM calls run at once; 12 is fine with Sonnet. Scoring costs about $0.015 per entry on
average, since the whole page is sent (long pages up to ~$0.10). An entry whose LLM call fails keeps no score; rerun the
command to retry it.

### Phase 4: Output the draft

The draft is a single markdown file with one section per taxonomy category, listing the classified entries filed under
it (with `--top N`, only the N most important). If `taxonomy-enriched.yaml` exists, its agenda fields are used.

| Task | Command | Output |
|---|---|---|
| Import human feedback (optional; columns `URL,CATEGORY_ID,PAPER_ID,LINK_TEXT`) | `uv run python src/import_feedback.py feedback.csv --source <label>` | include / exclude / reclassify decisions applied at export |
| Export the draft | `uv run python src/export_draft.py -o draft.md` | `draft.md`, every classified entry, best category fit first (`--source` limits it to some sources) |
| Export the pruned draft: each category's 10 most important entries | `uv run python src/export_draft.py --top 10 -o draft.md` | most important first; fails if an entry has no importance score (run `score_entries.py` first) |
| Export the pruned draft: entries with importance ≥ 0.5, at most 10 per category | `uv run python src/export_draft.py --min-importance 0.5 --top 10 -o draft.md` | most important first (equal importance: best category fit first); a category with fewer than 10 such entries keeps only those. `--min-importance` is inclusive (0.5 keeps the entries scored exactly 0.50) |
| Export the draft with each item's fit score, importance, id and summary | `uv run python src/export_draft.py --details -o draft.md` | By default each item shows only its title link, authors and date |
| Export the draft from the enriched taxonomy, failing on empty fields | `uv run python src/export_draft.py --strict -o draft.md` | `--strict` fails if any agenda field is empty |

After people have edited the draft, `process_draft.py` turns it into the final document:

| Task | Command | Output |
|---|---|---|
| List every link in a draft | `uv run process_draft.py collect-links draft.md` | |
| Parse an edited draft | `uv run process_draft.py parse draft.md -o parsed` | `parsed.json` / `parsed.yaml` |
| Render the parsed draft | `uv run process_draft.py format parsed.json -o final.md` | `final.md` |

## Changing the taxonomy

Categories are assigned when an item is classified, so editing `data/taxonomy.yaml` doesn't move items that were
already classified. After editing it, classify again:

```bash
uv run python src/reset_classify.py
uv run python src/classify_entries.py --limit 1000 --workers 4
uv run python src/export_draft.py --top 10 -o draft-2026.md
```

With no filters, `reset_classify.py` re-queues every item without asking; add `--source` to limit it. Scrapes are
cached, so re-classifying only costs the LLM calls. Importance scores don't depend on the category, so they don't need
to be redone.

## Running on the 2026 selected sources

`data/sources-links/facets-{arxiv,lw,org,safetystack}-2026.txt` hold the 502 sources on the facets site (240 arXiv,
140 LessWrong, 80 org pages, 42 Safety Stack). `facets-shared/src/export_for_pipeline.py` writes them from
`facets-shared/output/selected-sources.csv`; rerun it if the selection changes.

```bash
for s in arxiv lw org safetystack; do
  uv run python src/add_entries.py data/sources-links/facets-$s-2026.txt
done
uv run python src/classify_entries.py --limit 600 --workers 4
uv run python src/score_entries.py --limit 600 --workers 12
uv run python src/export_draft.py --top 10 \
  --source facets-arxiv-2026,facets-lw-2026,facets-org-2026,facets-safetystack-2026 -o draft-2026-facets.md
```

- `classify_entries.py` has no source filter, so it processes everything still queued.
- Items are filed under whatever `taxonomy.yaml` holds when `classify_entries.py` runs, which is the 2026 taxonomy.
- The worked examples in `prompts/classify.yaml` use category IDs from an older taxonomy. If the LLM returns an ID that
  is not a leaf of the current one, the item is marked `classify_error`; rerun those with `classify_entries.py --retry-errors`.

## The entries table

One row per URL in `data/data.db`. The full schema is in `docs/DATA.md`; `show_info.py` lists the first rows.

| Column | Written by | In `show_info.py` | Meaning |
|---|---|---|---|
| `url` | `add_entries.py` | URL | The page (primary key) |
| `source` | `add_entries.py` | Source | Label of the URL list it came from, e.g. `facets-arxiv-2026` |
| `status` | `add_entries.py`, `classify_entries.py` | Status | `new` (queued), `done` (classified), `scrape_error` or `classify_error` (see `classify_error_message`) |
| `added_at` | `add_entries.py` | Added | When it was queued (ISO 8601, UTC) |
| `classified_at` | `classify_entries.py` | | When it was classified (ISO 8601, UTC) |
| `classifier_output` | `classify_entries.py` | Classifier Output (JSON); its first category as Category and Category Fit | The classifier's output as JSON, see below |
| `classify_error_message` | `classify_entries.py` | | Why scraping or classification failed (scoring errors are only logged) |
| `citation_count` | `score_entries.py` | Citations | Citations on Semantic Scholar; empty for LessWrong posts, pages it doesn't know and refused lookups |
| `lw_karma` | `score_entries.py` | LW Karma | Karma of a LessWrong post; empty otherwise |
| `attention_checked_at` | `score_entries.py` | | When citations and karma were looked up (empty: not yet, or Semantic Scholar refused), so an empty citation count can be told apart from "not looked up" |
| `importance` | `score_entries.py` | Importance | How important the work is for the review, 0-1 (0.9+ landmark, 0.7-0.9 strong, 0.5-0.7 solid but incremental, below 0.5 minor) |
| `importance_reason` | `score_entries.py` | | The LLM's one-sentence reason for the score |

Databases made with older versions of the pipeline also have the unused columns `ai_safety_relevance`,
`shallow_review_inclusion` and `kind`. Their `processed_at`, `data` and `error` columns (and `score` in the JSON's
categories) are renamed to the names above the first time a script opens them.

An example `classifier_output` value (the `categories` are the leaf categories, best fit first):

```json
{
  "content_available": true,
  "title": "Verbalizable Representations Form a Global Workspace in Language Models",
  "authors": ["Wes Gurnee", "Nicholas Sofroniew", "Adam Pearce", "..."],
  "author_organizations": [],
  "date": "2026-07-16",
  "summary": "Introduces the Jacobian lens to identify the representations a language model is poised to verbalize ...",
  "categories": [
    {"id": "science_of_representations", "fit": 0.85},
    {"id": "interpretability_methods_and_tools", "fit": 0.75},
    {"id": "alignment_auditing_methods", "fit": 0.3}
  ],
  "tokens_full": 14383,
  "tokens_stripped": 3668,
  "classify_duration": 0.99
}
```

- `content_available`: false if the page was an error page, paywall or empty (the entry is then a `classify_error`)
- `title`, `authors`, `author_organizations`, `date`, `summary`: metadata the LLM read off the page
- `categories`: 1-3 leaf categories of the taxonomy, each with a `fit` (0-1: how well the work fits that category,
  not how good it is). The draft files the entry under the first one
- `tokens_full`, `tokens_stripped`: size of the page's HTML before and after stripping scripts, styles and attributes
- `classify_duration`: seconds the classification took (near 0 when the LLM response came from the cache)

## Data

- `data/data.db`: the single SQLite database (schemas in `docs/DATA.md`)
- `data/scraped/`: cached pages as `<hash>.html.zst`
- `runs/`: a log file per run
- `archive/data-2025/`: the archived 2025 review (its database, dated draft snapshots, source lists). Not used by the scripts

## Things to watch for

- **The data folder is set in code.** `DATA_PATH` in `shallow_review/common.py` (`data/`) decides which database,
  taxonomy and caches are used. `data/` holds only the 2026 review; the 2025 review is archived in `archive/data-2025/` (its
  `data.db` still opens with the scripts if you point `DATA_PATH` there).
- **Write the draft with `-o`.** Without it `export_draft.py` prints the draft to stdout, where log messages end up
  too; delete the lines before `# AI Safety Shallow Review`.
- **The draft's year comes from the taxonomy.** Export reads `year` from the taxonomy file for the heading, the
  "Funding in"/"Outputs in" labels and the date filter (items dated before 1 November of the previous year are
  dropped).

## Documentation

- `docs/CLASSIFY.md`, `docs/SCRAPE.md`: how each phase works and why
- `docs/DATA.md`: database schemas, file formats and enums
- `docs/CODE.md`: coding conventions and libraries
- `docs/DEVLOG.md`: design decisions and lessons learned
- `AGENTS.md`: instructions for AI assistants working in this folder
