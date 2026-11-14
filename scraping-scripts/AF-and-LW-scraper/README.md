### AF and LW Scraper

Scripts to fetch a year of LessWrong or Alignment Forum posts, filter them for relevance to technical AI alignment and annotate them with an LLM, and generate a taxonomy and editorial overview.

### Which site to scrape

**Scrape LessWrong (the default).** Every Alignment Forum post is also published on LessWrong, so one LessWrong scrape covers both sites: AF posts are flagged with `af = True`, and nothing is duplicated. Scraping the Alignment Forum directly with `--site alignment-forum` is a backup, e.g. if LessWrong is unavailable or you only want AF posts. Each script takes the same `--site` option and uses `lw-` or `af-` file names to match.

### Setup

Steps 2–4 call Claude: step 2 uses `claude-haiku-5-5` and steps 3–4 use `claude-sonnet-5-5` by default (change it with `--model`). Copy `.env.example` to `.env` in this folder and add your Anthropic API key:

```bash
cp .env.example .env
```

### Usage

Run each script from this folder, in order. Each script's defaults read the previous step's output. Add `--site alignment-forum` to every step to use the Alignment Forum instead (outputs are then named `af-` instead of `lw-`).

| Step | Command | What it does | Output |
| --- | --- | --- | --- |
| 1 | `uv run python src/scrape_forum_posts.py` | Fetches every post from the year (default 2026), one month at a time | `results/1-lw-posts-raw.csv`: all posts (title, link, authors, date, AF flag, karma, comments, word count, forum tags, excerpt) |
| 2 | `uv run python src/filter_forum_posts.py` | Rates each post's relevance to technical AI alignment and keeps the highly relevant ones | `results/2-lw-posts-rated.csv`: every post with its relevance rating and reasoning<br>`results/2-lw-posts-highly-relevant.csv`: only posts rated "highly relevant" |
| 2b | `uv run python src/shortlist_forum_posts.py` | Shows Claude Opus each month's highly relevant posts side by side and keeps the most important ~12% (`--share`, or `--per-month N`), like the arXiv shortlist. A month whose candidate posts haven't changed is skipped | `results/shortlisted/2026/<month>/lw-posts-shortlisted.csv` (best first, with `shortlist_rank` and `shortlist_reason`) and the combined `results/shortlisted/2026/lw-posts-shortlisted.csv` |
| 3 | `uv run python src/annotate_forum_posts.py` | Tags and summarizes the highly relevant posts, and adds karma per month since posting | `results/3-lw-posts-annotated.csv`: highly relevant posts with LLM tags, a one-sentence summary, and karma per month |
| 4 | `uv run python src/generate_taxonomy_and_editorial.py` | Generates a taxonomy and editorial from the annotated posts | `results/4-lw-taxonomy-and-editorial.md`: editorial, taxonomy, review checklist, and post summaries |

### Options

- All scripts: `--site` (`lesswrong` or `alignment-forum`)
- `scrape_forum_posts.py`: `--year`, `--output`, `--delay` (seconds between requests, default 1.0), `--max-pages` (safety cap on requests)
- `filter_forum_posts.py`: `--input`, `--rated`, `--filtered`, `--model`, `--limit` (only rate the first N posts, for test runs)
- `shortlist_forum_posts.py`: `--input`, `--raw`, `--output-dir`, `--share` (default 0.12) or `--per-month N`, `--start-month` / `--end-month`, `--overwrite`, `--model` (default `claude-opus-5-5`), `--effort` (default `medium`)
- `annotate_forum_posts.py`: `--input`, `--output`, `--model`
- `generate_taxonomy_and_editorial.py`: `--input`, `--output`, `--model`

Run any script with `--help` for details.
