# Data Storage and Database Schemas

**Ground truth for all data structures, database schemas, and file formats.**

## Directory Structure

```
data/
├── .llm_cache/          # LLM response cache (gitignored)
├── data.db              # Unified database (entries, feedback tables)
├── taxonomy.yaml        # Classification category taxonomy (ground truth)
└── scraped/             # Scraped HTML content
    └── <hash>.html.zst  # Zstandard-compressed HTML files
```

## Unified Database: data.db

All tables stored in `data/data.db` with **NO foreign key constraints**.

**Note on column order:** Schemas below show the canonical column order for tables created from scratch. Databases migrated from earlier versions may have different column orders (with migrated columns at the end) due to SQLite's `ALTER TABLE` behavior. This is functionally equivalent - SQLite doesn't care about column order, and all queries use column names.

### Scraped pages

There is no scrape table: the cache is the directory `data/scraped/`. The page of a URL is the file
`data/scraped/{url_hash}.html.zst`, where `url_hash` is the SHA-256 of the normalized URL (`utils.url_hash`). If the file exists the
page is not scraped again; the file is written to a temporary name first and renamed, so it is never half-written.
Failed scrapes are not cached: `classify_entries.py` records them as `scrape_error` on the entry. HTTP error pages (404, 403) are
saved like any other page and the classifier marks them `error_detected`. Use `get_scrape_path(url)` or
`open_scraped(url, mode)` to access files. Databases made before this change may still contain an unused `scrape` table.

### entries table

Databases created before the collect stage was removed (such as `data/data.db`) may still contain a `collect` table and
`classify.source_url` / `classify.collect_relevancy` columns. The code ignores them. Databases created before the
rename of `classify` to `entries` and `classify_feedback` to `feedback` are renamed in place (and their
`idx_classify_*` indexes recreated as `idx_entries_*`) the first time the code opens them. Older databases also have
unused `url_hash` / `url_hash_short` columns in `entries` and `url_hash_short` in `feedback`: the short hash (the `id:`
shown in drafts) is computed from the URL with `url_hash_short(url)` instead of stored.


One row per URL: its processing status, source label and, once classified, the LLM's result (categories and basic
metadata); once scored, its attention (citations or karma) and importance.

```sql
CREATE TABLE entries (
    url TEXT PRIMARY KEY,
    status TEXT NOT NULL,
    source TEXT NOT NULL,
    added_at TEXT NOT NULL,
    classified_at TEXT,
    classifier_output JSON,
    classify_error_message TEXT,
    citation_count INTEGER,
    lw_karma INTEGER,
    attention_checked_at TEXT,
    importance REAL,
    importance_reason TEXT,
    CHECK(status IN ('new', 'scrape_error', 'classify_error', 'done'))
);

CREATE INDEX idx_entries_status ON entries(status);
CREATE INDEX idx_entries_source ON entries(source);
CREATE INDEX idx_entries_added_at ON entries(added_at);
CREATE INDEX idx_entries_importance ON entries(importance);
```

**Fields:**
- `url`: URL to classify (primary key)
- `status`: Processing state (new → scrape_error/classify_error/done)
- `source`: Label given with `add_entries.py --source` (default: the URL file's name without extension)
- `added_at`: ISO 8601 UTC timestamp when added
- `classified_at`: ISO 8601 UTC timestamp when classification finished (or failed)
- `classifier_output`: JSON with classification results and preprocessing info (see below)
- `classify_error_message`: Why scraping or classification failed (scoring errors are not stored)
- `citation_count`: Semantic Scholar citation count (`score_entries.py`): arXiv / DOI links by ID, other pages by
  exact title. NULL for LessWrong posts, unknown papers and refused lookups
- `lw_karma`: LessWrong karma (`baseScore`) of a LessWrong post (`score_entries.py`), NULL otherwise
- `attention_checked_at`: ISO 8601 UTC timestamp of the citation / karma lookup (`score_entries.py`), so that NULL
  citations and karma can be told apart: looked up and not found, or not looked up. NULL if not looked up or if
  Semantic Scholar refused the lookup (retried on the next run)
- `importance`: Importance of the work for the review, 0.0-1.0 (`score_entries.py`); `export_draft.py --top N` keeps
  each category's N highest. NULL until scored
- `importance_reason`: The LLM's one-sentence reason for `importance`

Databases made before the column renames have `processed_at`, `data` and `error` instead of `classified_at`,
`classifier_output` and `classify_error_message`, and `score` instead of `fit` in the categories of the JSON; the code
renames them in place the first time it opens the database (`_rename_old_columns` in `data_db.py`).

Databases made before `score_entries.py` get the last five columns (and the index) added with `ALTER TABLE` the first
time the code opens them.

**classifier_output JSON structure** (when status='done'):
```json
{
  "content_available": true,
  "title": "...",
  "authors": ["Author 1", "Author 2"],
  "author_organizations": ["Anthropic", "OpenAI"],
  "date": "2025-01-15",
  "summary": "One sentence on what the work does",
  "categories": [
    {"id": "interpretability_mech", "fit": 0.95},
    {"id": "evals_safety", "fit": 0.75}
  ],
  "tokens_full": 50000,
  "tokens_stripped": 15000,
  "classify_duration": 8.76
}
```

**Notes:**
- `title`, `authors`, `author_organizations`, `summary`: Basic metadata from the LLM
- `date`: `YYYY-MM-DD`, or `YYYY-MM` / `YYYY` if that is all the page gives (nullable)
- `categories`: 1-3 assignments with taxonomy leaf IDs and fit scores 0.0-1.0, best fit first
- `tokens_full`, `tokens_stripped`: Token counts of the full and the preprocessed HTML (set by the script)
- `classify_duration`: Total time for classification in seconds
- Databases made before the classifier was narrowed to categories may have the columns `ai_safety_relevance`,
  `shallow_review_inclusion` and `kind`, and more fields in `classifier_output` (scores, `kind`, `confidence`, ...). The code ignores them.

### feedback table

Stores human feedback on classification decisions (category assignments, inclusions, exclusions).

```sql
CREATE TABLE feedback (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    url TEXT NOT NULL,
    feedback_source TEXT NOT NULL,
    feedback_timestamp TEXT NOT NULL,
    action TEXT NOT NULL,
    human_category TEXT,
    paper_id TEXT,
    link_text TEXT,
    notes TEXT,
    CHECK(action IN ('include', 'exclude', 'reclassify', 'note'))
);

CREATE INDEX idx_feedback_url ON feedback(url);
CREATE INDEX idx_feedback_action ON feedback(action);
CREATE INDEX idx_feedback_human_category ON feedback(human_category);
CREATE INDEX idx_feedback_source ON feedback(feedback_source);

-- Partial unique indexes to prevent true duplicates while allowing multi-category
CREATE UNIQUE INDEX idx_feedback_unique_single_action 
  ON feedback(url, feedback_source, action, feedback_timestamp) 
  WHERE action IN ('include', 'exclude', 'note');

CREATE UNIQUE INDEX idx_feedback_unique_reclassify 
  ON feedback(url, feedback_source, action, human_category, feedback_timestamp) 
  WHERE action = 'reclassify';
```

**Fields:**
- `url`: URL being reviewed (must match entries.url)
- `feedback_source`: Source of feedback (e.g., "SR2025-WIP-doc", "manual-review")
- `feedback_timestamp`: ISO 8601 UTC timestamp when feedback was recorded
- `action`: What to do with this item
  - `include`: Marks the entry as wanted (kept when detecting exclusions)
  - `exclude`: Force exclusion from exports (even if above thresholds)
  - `reclassify`: Override LLM category with human category
  - `note`: Annotation only (no effect on inclusion/exclusion, used for tracking)
- `human_category`: Taxonomy leaf category ID assigned by human (required for action='reclassify')
- `paper_id`: Optional ID from source document (for tracking)
- `link_text`: Original link text from source (for reference)
- `notes`: Optional comments or reasoning

**Usage:**
- Import feedback via `src/import_feedback.py <csv-file> --source "label" [--reclassify-obsolete-llm]`
- Classification phase checks for existing feedback and respects reclassification
- Export phase respects include/exclude actions and uses human categories when available
- **Multi-category support**: A URL can have multiple `reclassify` entries with different `human_category` values
  - Paper appears in all assigned categories in exports
  - Partial unique indexes prevent true duplicates while allowing multi-category assignments
- Auto-increment `id` as primary key eliminates need for timestamp hacks

**Special one-time flag: `--reclassify-obsolete-llm`**
- Use when taxonomy has changed and old categories no longer exist
- For papers NOT in CSV but with obsolete LLM-assigned categories:
  - Instead of excluding them, marks them for re-classification
  - Resets their status to `new` in entries table
  - Creates feedback with `action='note'` (annotation only, no forced inclusion/exclusion)
  - Papers are re-classified with current taxonomy and normal thresholds apply
  - After re-classification, papers with sr>=0.4 appear in exports marked with 🔄 emoji
  - Papers with sr<0.4 after re-classification are excluded (as expected)
- This is a **one-time migration behavior** when restructuring taxonomy

**Precedence rules:**
1. Most recent feedback (by timestamp) takes precedence for same URL+source
2. `exclude` action always wins (safety-first approach) - EXCEPT when `--reclassify-obsolete-llm` applies
3. `reclassify` overrides LLM category in exports
4. `include` marks the entry as wanted

**Note keywords (for robust matching in code):**
- `NEEDS_RECATEGORIZATION`: Paper from CSV with obsolete category ID
- `RECLASSIFY_OBSOLETE_LLM`: Paper had obsolete LLM category, was re-classified

**Multi-category example:**
```
CSV rows:
  https://arxiv.org/abs/2410.12345,interp_sparse_coding,abc123,Paper X
  https://arxiv.org/abs/2410.12345,interp_applied,abc123,Paper X
  https://arxiv.org/abs/2410.12345,model_diff,abc123,Paper X

Feedback entries created:
  (id=1, url=..., action='reclassify', human_category='interp_sparse_coding')
  (id=2, url=..., action='include')
  (id=3, url=..., action='reclassify', human_category='interp_applied')
  (id=4, url=..., action='reclassify', human_category='model_diff')

Export behavior:
  Paper X appears in THREE sections: interp_sparse_coding, interp_applied, and model_diff
```

**Markers in exports (shown in brackets after title):**
- ⚠️ : Paper with `NEEDS_RECATEGORIZATION` (rare, needs manual recategorization)
- 🔄 : Paper with `RECLASSIFY_OBSOLETE_LLM` (one-time migration, already re-classified)
- ✌️(in N categories) : Paper appears in N categories (multi-category assignment)

**Example formatting:**
```markdown
- **[Paper Title](url)**, *Authors*, 2025, Venue, [🔄 ✌️(in 2 categories) fit=0.75, id:abc12345] Summary...
```
This indicates: re-classified due to obsolete LLM category, appears in 2 categories total

## Classification Taxonomy

**Ground truth:** `taxonomy.yaml` in `DATA_PATH` (`shallow_review/common.py`), currently `data/taxonomy.yaml`.
It is hand-written and holds the 2026 taxonomy; `src/enrich_taxonomy.py` writes `taxonomy-enriched.yaml` next to it (same content plus `agenda` blocks),
which export uses when present. A paper's category is always its highest-fit one in `entries.classifier_output.categories`.

The classification taxonomy defines a hierarchical category structure for classifying AI safety/alignment content. Each classified item must be assigned to exactly one **leaf category**.

### Top-level keys

- `taxonomy`: list of top-level categories (required)
- `year`: review year (optional, defaults to the current year). Export uses it in the draft heading, in `{year}` in
  agenda field labels, and for the date filter (drops items dated before 1 November of `year - 1`, or with only a
  year before `year - 1`)
- `agenda_fields`: agenda fields printed under each leaf category in the exported draft, in order (optional,
  defaults to `DEFAULT_AGENDA_FIELDS` in `taxonomy.py`, the 2025 layout). Each entry is a plain label or a mapping
  `{name, options}`; options are printed after the label as `*(one of: a / b)*` for editors. `{year}` in a label is
  replaced by `year`. A label starting with `Who edits` gets the "take me" marker. `Outputs in {year}` is always
  printed last, above the items, and may not be listed. Labels in `SR2024_FIELD_KEYS` (`src/export_draft.py`) are prefilled from a
  category's `sr2024` block

### Structure

- **Hierarchical organization**: Categories can contain subcategories
- **Leaf categories**: Only leaf nodes (categories without children) are assignable
- **Category fields**:
  - `id`: Machine-readable identifier (snake_case, unique across entire taxonomy)
  - `name`: Human-readable name
  - `description`: Detailed description of what belongs in the category
  - `children`: List of subcategories (empty for leaf categories)
  - `examples`: Optional list of example items from 2024 (ONLY allowed on leaf categories)
  - `is_leaf`: Can be explicitly set in YAML, otherwise inferred from presence of children
  - `agenda`: Only in the enriched taxonomy (`taxonomy-enriched.yaml`, written by `src/enrich_taxonomy.py`,
    `src/enrich_taxonomy.py`, prompt `prompts/agenda.yaml`). Agenda field values keyed by agenda field name, as
    markdown (`Key people` is a list; `See also` links to `#<category id>`; `Critiques` links cited items, or is an
    LLM-written sentence marked "unsourced"). Also `Comment (internal)`, the LLM's notes for editors, not printed

### Top-Level Categories

1. **Understand existing models** - Evals, interpretability, learning dynamics, model psychology
2. **Control the thing** - Alignment, monitoring, control, deception detection
3. **Alternative architectures** - Safer-by-design AI systems
4. **Better data** - Data quality, filtering, attribution for safety
5. **Make AI solve it** - Scalable oversight, debate, task decomposition
6. **Theory** - Agent foundations, corrigibility, cooperation theory
7. **Sociotechnical** - Approaches combining technical and social elements
8. **Misc / for new agenda clustering** - Items not yet fitting other categories

### Usage

- Load via `load_taxonomy()` from `taxonomy.py`
- Format for LLM prompts via `format_taxonomy_for_prompt()`
- Validate category IDs via `taxonomy.validate_category_id(cat_id)`
- Total: **103 leaf categories** (as of 2025-10-21)
- Includes 8 "other" catch-all categories for novel work not fitting existing categories

### Validation Rules

1. All category IDs must be unique across entire taxonomy
2. Category IDs must be alphanumeric with underscores/hyphens (snake_case)
3. Only leaf categories can have examples
4. At least one leaf category must exist
5. `agenda_fields` must not contain `Outputs in ...` (always printed)

## File Formats

### Scraped HTML (.html.zst)

- **Format:** HTML text compressed with Zstandard level 15
- **Location:** `data/scraped/<hash>.html.zst`
- **Hash:** SHA256 of URL only
- **Access:** Use `open_scraped(url, mode)` or `get_scrape_path(url)` from `scrape.py`

### Parquet Files

When used, parquet files written with:
- Compression: Zstandard level 15
- Location: TBD based on output

## Enums and Constants

### Status Values

**EntryStatus:**
- `new` - Not yet processed
- `scrape_error` - Failed to scrape
- `classify_error` - LLM/classification failed
- `done` - Successfully completed

## Data Flow

1. **Scraping**: URL → `data/scraped/<hash>.html.zst`
2. **Classification**: URL → `entries` table with results

**Key points:**
- Scrapes are shared across all phases (one scrape per URL)
- Tables do NOT reference each other with foreign key constraints
- All timestamps are ISO 8601 with timezone (UTC)

## Database Access

Use `get_data_db()` from `data_db.py` to access the unified database:
- Thread-safe lazy singleton
- Creates tables/indexes on first access
- Don't hold connection for long periods
