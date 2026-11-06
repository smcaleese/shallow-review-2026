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
                        │             relevance scores, kind, 1-3 leaf categories, title, authors, date, summary
                        ▼
               data/data.db  ◀── import_feedback (human include / exclude / reclassify)
                        │
                  export_draft      walk data/taxonomy.yaml, list each category's items that pass the filters
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
   LLM with the whole taxonomy in the system prompt. The LLM returns `ai_safety_relevance` and
   `shallow_review_inclusion` scores (0-1), a `kind` (paper, blog post, ...), 1-3 leaf category IDs with fit
   scores, and metadata. This is the only step that reads the taxonomy to assign categories.
3. **Feedback (optional).** `src/import_feedback.py <csv>` records human decisions, such as including a
   below-threshold item, excluding one or moving it to another category. Export applies them on top of the LLM's
   output.
4. **Enrich the taxonomy.** `src/enrich_taxonomy.py` makes one LLM call per leaf category with its items, the
   list of all categories and an index of all items, and writes every agenda field (summary, theory of change, see
   also, general approach, target case, key people, critiques) to `taxonomy-enriched.yaml`, a copy of the taxonomy
   with an `agenda` block per category. The hand-written `taxonomy.yaml` is not modified. Agendas already in the
   enriched file are kept (so hand edits survive) unless `--overwrite` or `--only`.
5. **Export the draft.** `src/export_draft.py -o draft.md` walks the taxonomy tree and lists, under each
   category, the classified items that pass the score thresholds, sorted by `shallow_review_inclusion`. Each
   category gets empty agenda fields (summary, theory of change, key people, ...) for editors to fill in.
6. **Process the edited draft.** After people edit the draft, `process_draft.py parse` splits it into agendas and
   papers, fills paper metadata from the database and uses an LLM to extract agenda attributes. Then
   `process_draft.py format` renders the parsed JSON with `draft_template.md` (or a template in `templates/`).

## Inputs

- **Entries:** URL lists in `data/sources-links/` (one URL per line, `#` for comments) or CSVs. Use `--source <label>`
  when adding so you can filter by provenance later. The 2026 review's selected sources are the `facets-*-2026.txt`
  lists (see "Running on the 2026 selected sources").
- **Taxonomy:** `taxonomy.yaml` in the data folder (`DATA_PATH`, see "Things to watch for"). It's a tree of `id`, `name`, `description` and `children`, and only leaves
  can be assigned. Leaves may also have `examples`, and nodes may have `sr2024` (context from the 2024 review), which
  export prints. Optional top-level `year` and `agenda_fields` set the draft's year and the agenda fields printed
  under each category (see `docs/DATA.md`). Year-specific copies sit next to it (`taxonomy-2025.yaml`, `taxonomy-2026.yaml`); the pipeline
  only reads `taxonomy.yaml`.

## Setup

```bash
uv sync
cp .env.example .env   # add ANTHROPIC_API_KEY (and HELICONE_API_KEY, which `process_draft.py parse` requires)
```

The scripts load `.env` themselves. Run them from this folder with `uv run python ...` (plain `python` uses your
system Python and fails with `ModuleNotFoundError`). Scraping uses Selenium by default (`USE_SELENIUM` in
`shallow_review/scrape.py`); with Playwright, keep `--workers 1`. Each script prints its options with `--help`.

## Usage

The scripts in `src/` are the pipeline's stages, in order; the code they share lives in `shallow_review/`.

| Task | Command | Output |
|---|---|---|
| Queue URLs | `uv run python src/add_entries.py data/sources-links/facets-arxiv-2026.txt` | rows in `data/data.db`, labelled `facets-arxiv-2026` (override with `--source`) |
| Show the number of entries in the `entries` table, and its first rows | `uv run python src/show_info.py [--source X] [--rows N]` | entries by status (`New`, `Done`, `Scrape Errors`, `Classify Errors`); after adding, all are `New`. Then the first 10 rows (`--rows N` for more). `--source` limits both to one source. Also prints the paths and score histograms |
| Scrape and classify queued URLs | `uv run python src/classify_entries.py --limit 500 --workers 4` | scores and categories in `data/data.db` |
| Retry items that failed | `uv run python src/classify_entries.py --retry-errors` | |
| Write each category's agenda fields with an LLM | `uv run python src/enrich_taxonomy.py [--only id1,id2] [--overwrite]` | `data/taxonomy-enriched.yaml` |
| Export the draft | `uv run python src/export_draft.py --min-shallow-review 0.4 -o draft.md` | `draft.md` (also `--min-ai-safety`, `--kinds`, `--source`) |
| Export the draft from the enriched taxonomy | `uv run python src/export_draft.py --min-shallow-review 0 --min-ai-safety 0 --strict -o draft.md` | `--strict` fails if any agenda field is empty |
| List every link in a draft | `uv run process_draft.py collect-links draft.md` | |
| Parse an edited draft | `uv run process_draft.py parse draft.md -o parsed` | `parsed.json` / `parsed.yaml` |
| Render the parsed draft | `uv run process_draft.py format parsed.json -o final.md` | `final.md` |

Maintenance:

| Task | Command |
|---|---|
| Put entries back in the queue for classification | `uv run python src/reset_classify.py [--source X] [--remove-scrapes]` |
| Import human feedback (columns `URL,CATEGORY_ID,PAPER_ID,LINK_TEXT`) | `uv run python src/import_feedback.py feedback.csv --source <label>` |

## Changing the taxonomy

Categories are assigned when an item is classified, so editing `data/taxonomy.yaml` doesn't move items that were
already classified. To use a new taxonomy:

```bash
cp data/taxonomy-2026.yaml data/taxonomy.yaml
uv run python src/reset_classify.py
uv run python src/classify_entries.py --limit 1000 --workers 4
uv run python src/export_draft.py --min-shallow-review 0.4 -o draft-2026.md
```

With no filters, `reset_classify.py` re-queues every item without asking; add `--source` to limit it. Scrapes are
cached, so re-classifying only costs the LLM calls.

## Running on the 2026 selected sources

`data/sources-links/facets-{arxiv,lw,org,safetystack}-2026.txt` hold the 502 sources on the facets site (240 arXiv,
140 LessWrong, 80 org pages, 42 Safety Stack). `facets-shared/src/export_for_pipeline.py` writes them from
`facets-shared/output/selected-sources.csv`; rerun it if the selection changes.

```bash
for s in arxiv lw org safetystack; do
  uv run python src/add_entries.py data/sources-links/facets-$s-2026.txt
done
uv run python src/classify_entries.py --limit 600 --workers 4
uv run python src/export_draft.py --min-shallow-review 0 --min-ai-safety 0 \
  --source facets-arxiv-2026,facets-lw-2026,facets-org-2026,facets-safetystack-2026 -o draft-2026-facets.md
```

- `data/data.db` also holds the 2025 items. None of the 502 are among them, and `--source` keeps the 2025 items
  out of the export.
- `classify_entries.py` has no source filter, so it also processes anything else still queued (30 items left over from 2025).
- The thresholds are 0 because these sources were already selected. Raise them to let the classifier drop some.
- Items are filed under whatever `data/taxonomy.yaml` holds when `classify` runs. It is currently a copy of
  `taxonomy-2026.yaml`. To export or re-run the 2025 items, copy `taxonomy-2025.yaml` back first, since their
  categories come from that taxonomy.
- The worked examples in `prompts/classify.yaml` use category IDs from an older taxonomy. If the LLM copies one,
  the item is marked `classify_error`; rerun those with `classify_entries.py --retry-errors`.

## Data

- `data/data.db`: the single SQLite database (schemas in `docs/DATA.md`)
- `data/scraped/`: cached pages as `<hash>.html.zst`
- `runs/`: a log file per run
- `data/<date>-...`: snapshots of earlier drafts and their parsed versions

## Things to watch for

- **The data folder is set in code.** `DATA_PATH` in `shallow_review/common.py` decides which database, taxonomy and
  caches are used. It currently points to `data-2026-facets/`, which holds only the 502 selected 2026 sources; set it
  back to `data` for the 2025 items.
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
