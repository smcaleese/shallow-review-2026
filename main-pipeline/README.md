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
   LLM with the whole taxonomy in the system prompt. The LLM returns 1-3 leaf category IDs with fit scores (0-1) and
   basic metadata (title, authors, organizations, date, one-sentence summary). It doesn't judge whether an entry belongs
   in the review: the sources are selected upstream. This is the only step that reads the taxonomy to assign categories.
3. **Feedback (optional).** `src/import_feedback.py <csv>` records human decisions, such as including a
   item the classifier missed, excluding one or moving it to another category. Export applies them on top of the LLM's
   output.
4. **Enrich the taxonomy.** `src/enrich_taxonomy.py` makes one LLM call per leaf category with its items, the
   list of all categories and an index of all items, and writes every agenda field (summary, theory of change, see
   also, general approach, target case, key people, critiques) to `taxonomy-enriched.yaml`, a copy of the taxonomy
   with an `agenda` block per category. The hand-written `taxonomy.yaml` is not modified. Agendas already in the
   enriched file are kept (so hand edits survive) unless `--overwrite` or `--only`.
5. **Export the draft.** `src/export_draft.py -o draft.md` walks the taxonomy tree and lists, under each
   category, the classified items filed under it, best fit first. Each
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
| Show the number of entries in the `entries` table, and its first rows | `uv run python src/show_info.py [--source X] [--rows N]` | entries by status (`New`, `Done`, `Scrape Errors`, `Classify Errors`); after adding, all are `New`. Then the first 10 rows (`--rows N` for more). `--source` limits both to one source. Also prints the paths and score histograms |

### Phase 3: Classify the sources

Each entry is scraped (the page is cached in `data/scraped/`) and sent to the LLM with the whole taxonomy in the prompt.
The LLM returns 1-3 leaf categories with fit scores and basic metadata, which are saved on the entry.

| Task | Command | Output |
|---|---|---|
| Scrape and classify the queued entries | `uv run python src/classify_entries.py --limit 500 --workers 4` | scores and categories in `data/data.db` |
| Check progress | `uv run python src/show_info.py` | `New` entries become `Done` |
| Retry entries that failed | `uv run python src/classify_entries.py --retry-errors` | |
| Classify again after changing the taxonomy | `uv run python src/reset_classify.py [--source X] [--remove-scrapes]` | entries are back to `New`; then rerun `classify_entries.py` |

### Phase 4: Output the draft

The draft is a single markdown file with one section per taxonomy category, listing the classified entries that pass the
score thresholds. If `taxonomy-enriched.yaml` exists, its agenda fields are used.

| Task | Command | Output |
|---|---|---|
| Import human feedback (optional; columns `URL,CATEGORY_ID,PAPER_ID,LINK_TEXT`) | `uv run python src/import_feedback.py feedback.csv --source <label>` | include / exclude / reclassify decisions applied at export |
| Export the draft | `uv run python src/export_draft.py -o draft.md` | `draft.md` (`--source` limits it to some sources) |
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
uv run python src/export_draft.py -o draft-2026.md
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
uv run python src/export_draft.py \
  --source facets-arxiv-2026,facets-lw-2026,facets-org-2026,facets-safetystack-2026 -o draft-2026-facets.md
```

- `classify_entries.py` has no source filter, so it processes everything still queued.
- Items are filed under whatever `taxonomy.yaml` holds when `classify_entries.py` runs, which is the 2026 taxonomy.
- The worked examples in `prompts/classify.yaml` use category IDs from an older taxonomy. If the LLM returns an ID that
  is not a leaf of the current one, the item is marked `classify_error`; rerun those with `classify_entries.py --retry-errors`.

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
