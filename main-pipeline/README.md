# Shallow Review pipeline

Turns a list of candidate URLs and a taxonomy into a first draft of the Shallow Review: every relevant item filed
under a taxonomy category, ready for people to edit. A second tool, `process_draft.py`, parses the edited draft back
into structured data and renders the final document.

Details live in `docs/` (see the end of this file). This README only covers the flow and the commands.

## How it works

```
URL lists ──add──▶ classify table ◀──collect── aggregator pages (optional)
                        │
                    classify          scrape each URL, then one LLM call with the taxonomy in the prompt:
                        │             relevance scores, kind, 1-3 leaf categories, title, authors, date, summary
                        ▼
               data/data.db  ◀── import-feedback (human include / exclude / reclassify)
                        │
                 export-taxonomy      walk data/taxonomy.yaml, list each category's items that pass the filters
                        ▼
                   draft.md           one section per category, agenda fields left blank for editors
                        │
               (people edit it)
                        ▼
  process_draft.py parse ─▶ JSON/YAML ─▶ process_draft.py format ─▶ final markdown
```

1. **Add entries.** `pipeline.py add <file>` reads URLs (a text file with one per line, or a CSV) into the database.
   With `--phase classify` they go straight to classification. With `--phase collect` they are treated as aggregator
   pages (newsletters, conference pages, reading lists) whose links get extracted first. The default `auto` asks an
   LLM which phase each URL belongs to. `../scraping-scripts/export_for_pipeline.py` writes the arXiv and LessWrong
   scrapers' results as URL lists in `data/sources-links/`.
2. **Collect (optional).** `pipeline.py collect` scrapes each aggregator page and asks an LLM for the links that look
   like AI safety work. Links above `--relevancy` are added to the classify queue.
3. **Classify.** `pipeline.py classify` scrapes each queued URL (cached in `data/scraped/`) and sends the page to the
   LLM with the whole taxonomy in the system prompt. The LLM returns `ai_safety_relevance` and
   `shallow_review_inclusion` scores (0-1), a `kind` (paper, blog post, ...), 1-3 leaf category IDs with fit
   scores, and metadata. This is the only step that reads the taxonomy to assign categories.
4. **Feedback (optional).** `pipeline.py import-feedback <csv>` records human decisions, such as including a
   below-threshold item, excluding one or moving it to another category. Export applies them on top of the LLM's
   output.
5. **Export the draft.** `pipeline.py export-taxonomy > draft.md` walks the taxonomy tree and lists, under each
   category, the classified items that pass the score thresholds, sorted by `shallow_review_inclusion`. Each
   category gets empty agenda fields (summary, theory of change, key people, ...) for editors to fill in.
6. **Process the edited draft.** After people edit the draft, `process_draft.py parse` splits it into agendas and
   papers, fills paper metadata from the database and uses an LLM to extract agenda attributes. Then
   `process_draft.py format` renders the parsed JSON with `draft_template.md` (or a template in `templates/`).

## Inputs

- **Entries:** URL lists in `data/sources-links/` (one URL per line, `#` for comments) or CSVs. Use `--source <label>`
  when adding so you can filter by provenance later.
- **Taxonomy:** `data/taxonomy.yaml`. It's a tree of `id`, `name`, `description` and `children`, and only leaves
  can be assigned. Leaves may also have `examples`, and nodes may have `sr2024` (context from the 2024 review), which
  export prints. Year-specific copies sit next to it (`taxonomy-2025.yaml`, `taxonomy-2026.yaml`); the pipeline
  only reads `taxonomy.yaml`.

## Setup

```bash
uv sync
export ANTHROPIC_API_KEY=...
```

The code doesn't read `.env` itself; `uv run --env-file .env pipeline.py ...` loads it. `process_draft.py parse` also
asserts that `HELICONE_API_KEY` is set. Scraping uses Selenium by default (`USE_SELENIUM` in `shallow_review/scrape.py`);
with Playwright, keep `--workers 1`.

## Commands

| Command | What it does |
|---|---|
| `uv run pipeline.py info` | Paths, config and database counts |
| `uv run pipeline.py add data/sources-links/arxiv-2026.txt --phase classify --source arxiv-2026` | Queue URLs |
| `uv run pipeline.py collect --limit 100 --relevancy 0.3` | Extract links from aggregator pages |
| `uv run pipeline.py classify --limit 500 --workers 4` | Scrape and classify queued URLs (default model `anthropic/claude-sonnet-4-5`) |
| `uv run pipeline.py classify --retry-errors` | Retry items that failed |
| `uv run pipeline.py reset-classify [--source X] [--remove-scrapes]` | Put items back in the queue |
| `uv run pipeline.py import-feedback feedback.csv --source <label>` | Import human feedback (columns `URL,CATEGORY_ID,PAPER_ID,LINK_TEXT`) |
| `uv run pipeline.py export-taxonomy --min-shallow-review 0.4 > draft.md` | Write the draft (also `--min-ai-safety`, `--min-collect`, `--kinds`, `--source`) |
| `uv run process_draft.py collect-links draft.md` | List every link in a draft |
| `uv run process_draft.py parse draft.md -o parsed` | Parse an edited draft into `parsed.json` / `parsed.yaml` |
| `uv run process_draft.py format parsed.json -o final.md` | Render the parsed draft |

## Changing the taxonomy

Categories are assigned when an item is classified, so editing `data/taxonomy.yaml` doesn't move items that were
already classified. To use a new taxonomy:

```bash
cp data/taxonomy-2026.yaml data/taxonomy.yaml
uv run pipeline.py reset-classify
uv run pipeline.py classify --limit 1000 --workers 4
uv run pipeline.py export-taxonomy --min-shallow-review 0.4 > draft-2026.md
```

With no filters, `reset-classify` re-queues every item without asking; add `--source` to limit it. Scrapes are
cached, so re-classifying only costs the LLM calls.

## Data

- `data/data.db`: the single SQLite database (schemas in `docs/DATA.md`)
- `data/scraped/`: cached pages as `<hash>.html.zst`
- `runs/`: a log file per run
- `data/<date>-...`: snapshots of earlier drafts and their parsed versions

## Things to watch for

- **The data folder is fixed.** `DATA_PATH` in `shallow_review/common.py` always points to `data/`. The log at the top
  of `draft-2026.md` shows that run used `data-2026/data.db`, so a separate year means pointing `DATA_PATH` there.
- **Logs end up in the draft.** Log messages are printed to stdout, so redirecting `export-taxonomy` captures them
  too. Delete the lines before `# AI Safety Shallow Review`.
- **Some years are hard-coded in export.** It drops items dated before 2024-11-01 (or with only a year before 2024)
  and labels the empty fields "Funding in 2025" and "Outputs in 2025".

## Documentation

- `docs/COLLECT.md`, `docs/CLASSIFY.md`, `docs/SCRAPE.md`: how each phase works and why
- `docs/DATA.md`: database schemas, file formats and enums
- `docs/CODE.md`: coding conventions and libraries
- `docs/DEVLOG.md`: design decisions and lessons learned
- `AGENTS.md`: instructions for AI assistants working in this folder
