# Development Log

This log documents major problems, solutions, lessons learned, and design decisions during development.

## 2025-10-27: SR2024 Rubrics Integration

**What was done:**
- Extended `export-taxonomy` command to include SR2024-style rubrics for each category
- Added 12 structured fields to create machine-readable agenda descriptions
- Fields are initially empty placeholders for manual or LLM-assisted filling

**Changes:**
- Export now outputs rubrics on leaf categories only (between description and items):
  - `One-sentence summary`: Brief agenda description
  - `Theory of change`: How the agenda aims to make impact
  - `See also`: Related work/approaches
  - `Orthodox problems`: References to alignment problems it addresses
  - `Target case`: Optimistic/pessimistic/worst-case target
  - `Broad approach`: Engineering/behavioural/cognitive/maths-philosophy
  - `Key people`: Key researchers and organizations
  - `Estimated FTEs`: Full-time equivalent count
  - `Outputs 2024-5`: Papers, tools, benchmarks
  - `Critiques`: Critical perspectives
  - `Funded by`: Funding sources
  - `Funding 2023-4`: Specific funding amounts
- Added "### Items" subheader before the classified papers list
- Format uses plain text headers (not bold/colon format) for easier editing
- No intermediate blank lines between rubric fields for compactness

**Rationale:**
- Enables building up agendas (categories) with papers as evidence
- Machine-readable format allows semi-automated analysis and comparison
- Follows established SR2024 structure for consistency
- Categories represent agendas, items represent outputs/evidence

## 2025-10-22: URL Hash Standardization

**What was done:**
- Added `url_hash` (full SHA256) and `url_hash_short` (8 chars) to all database tables
- Migrated existing database with 892 scrapes, 189 collect, and 1657 classify entries
- Updated all INSERT statements to populate hash columns
- Updated `export-taxonomy` CLI command to use database hashes instead of computing

**Changes:**
- **scrape**: Added `url_hash_short` column (already had full `url_hash`)
- **collect**: Added `url_hash` and `url_hash_short` columns
- **classify**: Added `url_hash` and `url_hash_short` columns
- All three tables now have indexes on both hash columns

**Rationale:**
- Short hash (8 chars) provides human-readable IDs for citation/tracking
- Full hash enables efficient lookups and deduplication
- Computing once at insert time avoids repeated computation
- Consistent across all tables for referencing items

**Implementation notes:**
- Migration script computed hashes from URL column (not dependent on scrape table)
- Hash format: SHA256(url).hexdigest(), short = first 8 chars
- Used in markdown export as `[item:5ad3d4e2]` for robust parsing after manual edits

## 2025-10-20: Initial Infrastructure Setup

**What was done:**
- Created core module structure under `shallow_review/`
- Implemented scraping infrastructure with playwright
- Set up stats tracking system with thread-safe context manager
- Configured litellm with disk caching and Helicone integration
- Created CLI framework with typer

**Key design decisions:**
- All paths derived from `ROOT_PATH` (from `__file__`) for pwd-independence
- Scrape cache uses `kind` parameter to distinguish contexts for same URL
- Hash computed as SHA256(`"{kind}:{url}"`) to allow URL reuse across contexts
- Stats use sets of IDs to avoid double-counting in multi-threaded scenarios
- Compression: Zstandard level 15 for all cached content
- Logging: Timestamped files in `runs/` directory with PID in filename

**Modules:**
- `common.py`: Paths, shutdown flag, base types
- `utils.py`: `smart_open()` for transparent compression, logging setup
- `stats.py`: Thread-safe stats tracking with CountStats and TokenStats
- `llm.py`: LLM integration with retry logic, cache invalidation on validation errors
- `scrape.py`: Playwright-based scraping with DB caching
- `cli.py`: Typer CLI with version/info commands
- `collect.py`, `classify.py`: Placeholder modules for future phases

**Technical notes:**
- LLM cache invalidation on ValidationError: Deletes bad cache entry before retry
- Scraping DB stores both successful scrapes and errors for caching
- Stats context manager ensures only one active stats instance per thread

**Scraping schema refactoring:**
- Changed URL to primary key (was url_hash) - ensures no duplicate scrapes
- Hash now only of URL, not `kind:url` - allows one scrape per URL
- Removed `content_path` column - path computed via `get_scrape_path(url)`
- Added `url_hash` column with UNIQUE constraint and index
- Added utility functions: `get_scrape_path(url)` and `open_scraped(url, mode)`
- Added `SCRAPED_PATH` constant to `common.py`
- Stats tracking uses `url` as unique ID (stored in sets to prevent duplicates)

## 2025-10-20: Collection Phase Implementation

**What was done:**
- Designed and implemented collection phase
- Created `collect.py` module with `compute_collect()` processing pipeline
- Designed collection prompts in `prompts/collect.yaml`
- Added HTML preprocessing utilities (`preprocess_html()`, `count_tokens()`)
- Implemented `add` CLI command for adding URLs
- Implemented `collect` CLI command with progress bars and stats
- Added `tiktoken` dependency for accurate token counting

**Key design decisions:**
- Links with relevancy ≥ threshold directly added to classify table (no intermediate table)
- Per-item commits for resumability and graceful shutdown
- HTML preprocessing strips scripts/styles/base64 images (50-90% token reduction)
- 2-level traceback formatting for errors
- Rich progress bars for top-level operations only
- Signal handlers for graceful shutdown (SIGINT/SIGTERM)

**Collection workflow:**
1. Add source URLs via CLI
2. Scrape and preprocess HTML
3. LLM extracts links with relevancy scores
4. Links above threshold promoted directly to classify table
5. Store full LLM response in JSON data field

## 2025-10-20: Database Overhaul - Unified data.db

**What was done:**
- Consolidated all databases into single `data/data.db` file
- Created `data_db.py` module with thread-safe singleton pattern
- Unified three tables: `scrape`, `collect`, `classify`
- Removed foreign key constraints between tables
- Eliminated intermediate `collect_links` table

**Key design decisions:**
- Single database simplifies architecture and queries
- No FK constraints for flexibility (semantic relationships only)
- Lazy singleton with global lock for thread-safe access
- Connection not held for long periods
- All timestamps in ISO 8601 format with timezone
- Links promoted inline during collect (no separate promotion step)

**Benefits:**
- Simpler codebase (single DB connection point)
- Easier queries (all data in one place)
- Better for small-scale operations (no complex multi-DB coordination)
- Resume-friendly (per-item commits)

## 2025-10-21: Classification Taxonomy System

**What was done:**
- Created hierarchical taxonomy system for classification categories
- Implemented `taxonomy.py` module with Pydantic models and utilities
- Created `data/taxonomy.yaml` with 103 leaf categories across 8 top-level groups
- Added taxonomy validation and prompt formatting functions
- Updated documentation (DATA.md, CODE.md, CLASSIFY.md)
- Added 4 megalab-specific categories: OpenAI Preparedness, DeepMind Frontier Safety, DeepMind Amplified Oversight, Anthropic Safeguards
- Expanded better_data with 5 subcategories (filtering, poisoning, attribution, synthetic, quality)
- Improved monitoring category descriptions for better disambiguation (control evals, mech anomaly, indirect, faithful CoT, whitebox, redteam)
- Added examples to interpretability categories and clarified theory category scopes
- Refined descriptions based on comparison with 2024 Shallow Review to ensure practical classificability
- Added 8 "other" catch-all categories for truly novel work not fitting existing categories

**Taxonomy structure:**
- 8 top-level categories: understand models, control, alternatives, data, AI solve, theory, sociotechnical, misc
- 103 assignable leaf categories (only leaves can be assigned to items)
- Hierarchical organization (3 levels: top-level → mid-level → leaf)
- Each category has: id, name, description, optional children, optional examples
- Includes org-specific programs: OpenAI Preparedness, DeepMind Frontier Safety Framework, DeepMind Amplified Oversight, Anthropic Safeguards
- Better data category expanded with 5 subcategories: filtering, poisoning, attribution, synthetic data, data quality
- Monitoring categories clarified with technique/org/problem distinctions
- Added 8 "other" catch-all categories for novel work: evals_other, interp_other, psych_other, deception_other, data_other, corrigibility_other, ontology_other, misc_other

**Key design decisions:**
- YAML as ground truth (not code, not docs)
- Recursive Pydantic models for validation and type safety
- `is_leaf` inferred from presence of children (can be explicitly set)
- Examples only allowed on leaf categories (validated)
- All category IDs unique across entire taxonomy (validated)
- IDs must be snake_case alphanumeric with underscores

**Prompt format:**
- Hierarchical markdown format (not flat list)
- Non-leaf categories as headers (h3-h5) with descriptions
- Leaf categories as bulleted items with IDs
- More readable and compact (~5,800 tokens)
- Provides context via headers, eliminates need for full paths

**Validation rules enforced:**
1. All IDs unique across taxonomy
2. IDs must be snake_case (alphanumeric + underscores/hyphens)
3. Only leaf categories can have examples
4. At least one leaf category must exist
5. No duplicate IDs allowed

**Usage pattern:**
```python
from shallow_review.taxonomy import load_taxonomy, format_taxonomy_for_prompt

# Load and validate
tax = load_taxonomy()  # From data/taxonomy.yaml

# Format for LLM prompt
prompt = format_taxonomy_for_prompt(tax, include_examples=False)

# Validate category ID
is_valid = tax.validate_category_id("evals_autonomy")  # True (leaf)
is_valid = tax.validate_category_id("evals")  # False (not leaf)

# Get all assignable categories
leaf_ids = tax.get_all_leaf_ids()  # 103 items
```

**Technical implementation:**
- Pydantic v2 with recursive models
- `validation_alias` for `is_leaf` field (YAML → model)
- `model_post_init` hook for cross-field validation
- Property shadowing for computed `is_leaf` value
- Thread-safe loading via lazy singleton pattern (future)

**Benefits:**
- Single source of truth for categories
- Type-safe validation at load time
- Easy to modify taxonomy (just edit YAML)
- Can version control taxonomy evolution
- Programmatic access to category tree
- Generate consistent prompts automatically

**Future work:**
- Add `category` column to classify table
- Implement classification prompts using taxonomy
- Add category-based filtering/analysis
- Track taxonomy version with data

## 2026-11-04: 2026 run, configurable agenda fields, LLM-written agenda headers

- The 2026 run uses its own data folder (`DATA_PATH = data-2026-facets`) with only the 502 selected sources, so the
  2025 items and leftovers stay out. `load_taxonomy()` now reads `DATA_PATH/taxonomy.yaml`; before it always read
  `data/taxonomy.yaml` regardless of `DATA_PATH`.
- Default model moved to `claude-sonnet-5-5` (Sonnet 4.5 is no longer served). Current models reject
  `thinking: {type: enabled, budget_tokens}`, so `get_completion` sends `{type: adaptive}`; `thinking_budget` only
  switches thinking on.
- The taxonomy file sets the draft's `year` (heading, labels, date filter) and its `agenda_fields`, so the 2026 header
  fields differ from 2025 without code changes.
- `enrich_taxonomy.py` writes all header fields per category with an LLM from the classified items into a separate
  `taxonomy-enriched.yaml` (ruamel.yaml round trip of the input, so comments survive). The input stays hand-written;
  the generated file can be reviewed and edited, and re-runs keep existing agendas. Critiques must cite items from
  the database (an index of all items is in the cached system prompt); otherwise an "unsourced" sentence is used.
  `export_draft.py --strict` refuses to write a draft with empty fields.
- Items are filed under their highest-scoring category, not the first listed (2 of 502 were listed out of order).
- All 140 LessWrong pages returned 403 to the scraper, yet were classified from the error page and URL (no authors,
  summaries guessed from titles). LessWrong/AF post URLs are now fetched from the GraphQL API (see SCRAPE.md); the
  143 LW items were re-scraped and reclassified. Lesson: a 403 page still reaches the LLM and comes back "done";
  check `scrape.status_code` after a run. Two goodfire.com pages are still 403 (the browser is blocked).
- Split the single typer CLI (`pipeline.py` / `shallow_review/cli.py`, 1,400 lines) into one `argparse` script per stage
  in `src/`, like `scraping-scripts/`. The scripts are thin; shared code stays in `shallow_review/` (made importable
  with a hatchling build-system entry in `pyproject.toml`) and `src/terminal.py` (`.env`, logging, Ctrl+C,
  `run_parallel`). `export_draft.py` takes `-o` so logs no longer mix into the draft.

## 2026-11-06: Removed the collect stage

- Dropped the `collect` table, `collect.py`, `add_items.py` (LLM detection of aggregator pages), `src/collect_links.py`,
  `prompts/collect.yaml`, `prompts/add_items.yaml`, `docs/COLLECT.md` and the `classify.source_url` /
  `collect_relevancy` columns. All 2026 sources are individual items, so there is one queue: `add_entries.py` adds URLs
  to `classify`, with no `--phase` and no LLM call. Old databases keep their `collect` table; the code ignores it.

## 2026-11-06: Renamed tables

- `classify` -> `entries` and `classify_feedback` -> `feedback` (indexes `idx_entries_*`), since with the collect stage
  gone the table holds the whole item, not a phase. `data_db.py` renames the old tables in place when it opens a
  database that still has them (tested on a copy of the 2025 database: 3,886 entries and 1,561 feedback rows kept).
- Dropped the stored hashes from `entries` and `feedback`: `url_hash_short(url)` is computed where the id is shown
  (export, agendas). The `scrape` table still stores `url_hash` / `url_hash_short` (its schema has `url_hash NOT NULL
  UNIQUE`, so removing it needs a table rebuild for old databases).
- Removed `data/taxonomy-2025.yaml` and `data/taxonomy-2026.yaml` (the latter was identical to `taxonomy.yaml`). `taxonomy.yaml`
  is the only hand-written taxonomy file and holds the 2026 taxonomy; the 2025 one lives in `taxonomy/input/` and git history.
- Archived the 2025 review in `data-2025/` (dated draft folders, `data.db`, 2025 source lists, data dump) and moved the
  2026 database, scraped pages, LLM cache and `taxonomy-enriched.yaml` from `data-2026-facets/` into `data/`, which now
  holds only 2026 data. `DATA_PATH` is `data/`; `data-2026-facets/` is gone. The older `data-2026/` run moved to
  `safety-stack/data-2026/`, since only `safety-stack/find_new_sources.py` reads its `data.db`.
- Moved `data-2025/` to `archive/data-2025/`.
- Dropped litellm. `llm.py` calls the Anthropic SDK directly (`anthropic>=2.6`, default model `claude-sonnet-5-5`) and gets
  structured output from `client.messages.parse()` instead of asking for a JSON code block and extracting it. Responses
  are cached with diskcache in `<data>/.llm_cache`. Thinking is adaptive, controlled by `effort` (the old
  `thinking_budget` is gone: `budget_tokens` returns a 400 on current models); `max_tokens` is 16000 so thinking
  doesn't cut the answer off. Retries come from the SDK (`max_retries=5`); a response that fails validation is asked again
  without the cache. Cost is computed from a small price table in `llm.py` (litellm did it before). Model names no longer
  take the `anthropic/` prefix. `process_draft.py` lost its litellm setup and the `--cache-dir` option.
- Code used by one script now lives in that script: `shallow_review/classify.py`, `agendas.py` and `feedback.py` were merged into
  `src/classify_entries.py`, `enrich_taxonomy.py` and `import_feedback.py`. `shallow_review/` keeps only code shared by
  several scripts (`common`, `data_db`, `entries`, `llm`, `scrape`, `stats`, `taxonomy`, `utils`). AGENTS.md no longer
  requires everything to live in `shallow_review/`.
- Removed the `scrape` table. The cache is the directory `data/scraped/`: a page is cached when its file exists (written
  to a temporary name, then renamed). Failed scrapes are no longer cached; they show up as `scrape_error` entries. Dropped
  the scrape metrics (sizes, durations, status codes), the `kind` argument of `compute_scrape`, `SAVE_STRIPPED_HTML` and
  the scrape histograms in `show_info.py`. Old databases keep an unused `scrape` table.
- Moved `preprocess_html` and `count_tokens` from `shallow_review/utils.py` into `src/classify_entries.py`, the only script that uses them.
- Narrowed the classifier to filing entries under the taxonomy. Scraping and selection happen upstream, so the model no
  longer scores `ai_safety_relevance` / `shallow_review_inclusion`, nor returns `kind`, `contribution_type`, `key_result`,
  `venue`, `published_year`, `category_comment` or `confidence`. It returns `content_available`, title, authors,
  organizations, date, a one-sentence summary and 1-3 categories with fit scores. `prompts/classify.yaml` shrank from 346
  to ~100 lines (3 short examples; no scoring rubrics) and the taxonomy moved to the system prompt so it is prompt-cached
  (about $0.02 per entry instead of $0.03+). The `entries` table lost the score and `kind` columns; export lost
  `--min-shallow-review`, `--min-ai-safety` and `--kinds` and sorts by category fit; `enrich_taxonomy.py` no longer
  gets `key_result`; `reset_classify.py` lost `--kind`; `import_feedback.py` lost `--min-shallow-review`;
  `process_draft.py --sort-by-relevancy` sorts by category fit. `EntryKind` is gone.

## 2026-11-10: Importance scoring and pruning to the top N per category

- Added `src/score_entries.py`, a step after classification that rates each `done` entry's importance for the review
  (0-1, plus a one-sentence reason). It fetches attention first: Semantic Scholar citations (one batch call for arXiv /
  DOI IDs, an exact-title match for other pages) and LessWrong karma. The LLM gets the cached page and the attention as
  a rate per month since publication; the prompt (`prompts/score.yaml`) puts the work's significance, rigor and novelty
  first and the authors' reputation and the attention second. Stored in new `entries` columns (`citation_count`,
  `lw_karma`, `importance`, `importance_reason`), added in place to existing databases.
- Kept separate from classification, which was narrowed to filing entries (see above): the score doesn't depend on the
  category, so taxonomy changes don't force rescoring, and the rubric can change without reclassifying. The cost is
  sending each page to the LLM twice.
- Citations are a weak signal for this year's mostly months-old work, hence a rate and a minor weight. Semantic
  Scholar's unauthenticated pool often returns 429 for minutes: title lookups that keep failing are reported and the
  entry is scored without citations (`SEMANTIC_SCHOLAR_API_KEY` raises the limit).
- `export_draft.py --top N` keeps each category's N most important entries, most important first, and fails if an
  entry is unscored. The database is not changed, so the cut-off is easy to revisit.
- Renamed the ambiguous `entries` columns: `data` → `classifier_output`, `processed_at` → `classified_at` (only
  classification sets it, and scoring now also "processes" entries), `error` → `classify_error_message`; and in the
  JSON, `categories[].score` → `fit`, so it can't be confused with `importance`. `data_db.py` renames them in place
  in existing databases (`ALTER TABLE ... RENAME COLUMN`, and a rewrite of the JSON of each row with `score`).
- Added `attention_checked_at`, so that a NULL citation count can be told apart from "not looked up": reruns no longer
  repeat the slow Semantic Scholar title lookups of org pages that are not in Semantic Scholar.
- Added `export_draft.py --min-importance X`: keeps items with importance ≥ X, combined with `--top N` as "at least X,
  at most N per category". The scores are coarse (61% of entries are 0.50, 0.55 or 0.62), so at the `--top` cap
  equal scores are often split by database order: with `--min-importance 0.5 --top 10`, 15 of 19 capped categories
  tie at the cap. Ties are therefore broken by category fit: it measures belonging, not quality, but prefers entries
  that are central to the agenda over ones filed there loosely, and is deterministic.
