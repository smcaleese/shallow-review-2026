# Classify Process

Documentation for the classification step: filing each entry under the taxonomy's categories.

## Purpose

`src/classify_entries.py` takes the entries added with `src/add_entries.py` and puts each one under 1-3 leaf categories of
`data/taxonomy.yaml`, plus basic metadata (title, authors, organizations, date, one-sentence summary). It does not decide
whether an entry belongs in the review: the sources are selected and filtered upstream (the scraping scripts and the
facets selection), so the classifier only decides *where* each one goes.

## Process Flow

1. **Add entries**: `src/add_entries.py <file> [--source "label"]` (the label defaults to the file name without extension)
   puts URLs in the `entries` table with status `new`.
2. **Classify**: `src/classify_entries.py --limit N --workers W` takes the `new` entries and, for each:
   a. Scrape the page (cached in `data/scraped/`)
   b. Preprocess the HTML and check the token limit
   c. Send the page to the LLM; the whole taxonomy is in the system prompt, which is prompt-cached for an hour
   d. Validate the response (structured output) and the category IDs
   e. Store the result in `entries.data` and set the status to `done`, or to an error status

## Configuration

Via `RunClassifyConfig` in `common.py` and the script's options: `--limit` (default 100), `--workers`, `--model`
(default `claude-sonnet-5-5`), `--max-tokens` (HTML tokens after preprocessing, default 100,000), `--retry-errors`.

## Output

Stored in `entries.data` (schema in `DATA.md`): `title`, `authors`, `author_organizations`, `date`, `summary` and
`categories`, a list of 1-3 `{id, score}` with leaf category IDs, best fit first. The score (0-1) is how well the
category fits; the draft files the entry under its first category. The script adds `tokens_full`, `tokens_stripped`
and `classify_duration`.

The model also returns `content_available`. When it is false (error page, paywall, empty text) the entry gets
`classify_error` and no categories.

## Taxonomy

**Ground truth:** `data/taxonomy.yaml` (see DATA.md). Only leaf categories can be assigned. The taxonomy is formatted
hierarchically in the system prompt, with non-leaf categories as headers and leaves as bullets with their IDs. A returned
ID that is not a leaf fails the entry with `classify_error`.

## HTML Preprocessing

Before classification the page HTML is cleaned: scripts, styles, `<noscript>`, `<svg>`, comments and base64 images are
removed, `<div>` and `<span>` are unwrapped, attributes other than `href` (links) and `src`/`alt` (images) are dropped, and
whitespace is collapsed. Token counts before and after are stored.

## Error Handling

- **scrape_error:** the page could not be fetched. Not retried until `reset_classify.py` resets the entry.
- **classify_error:** the LLM call or validation failed, the page has no readable content, the category is not a leaf, or the
  HTML exceeds `--max-tokens`. Retry with `--retry-errors` (uses the cached page).

## Prompt

`prompts/classify.yaml`: the system prompt holds the task and the taxonomy; the user prompt holds the page, the steps, the
fields and two short examples. Changing the taxonomy requires classifying again (`reset_classify.py`).

## Statistics

Tracked per run: candidates (new, cached, errors), HTML tokens (full vs stripped), LLM tokens and cost.
