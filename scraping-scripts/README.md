### Scraping Scripts

Optional scrapers that find candidate papers and posts for the Shallow Review of Technical AI Safety, rate them for relevance with Claude, and narrow them down to a reading list. Each scraper has its own README with full usage and options.

### Scrapers

| Scraper | Finds | Pipeline | Details |
| --- | --- | --- | --- |
| [`arxiv-scraper/`](arxiv-scraper/) | arXiv papers | Keyword search month by month, with Semantic Scholar citation data → Claude Haiku rates each paper 1–5 and keeps 4+ → Claude Opus shortlists the most important ~9% per month. For January to October 9, 2026: 12,183 papers → 1,537 → 135 | [README](arxiv-scraper/README.md) |
| [`AF-and-LW-scraper/`](AF-and-LW-scraper/) | Alignment Forum and LessWrong posts | Fetches a year of posts (one LessWrong scrape also covers every Alignment Forum post) → Claude Haiku rates them and keeps the highly relevant ones → Claude Sonnet tags and summarizes them and writes a taxonomy and editorial | [README](AF-and-LW-scraper/README.md) |

### Setup

Both scrapers share this folder's Python project (`pyproject.toml`). Install the dependencies once, from this folder:

```bash
uv sync
```

Each scraper calls Claude, so copy its `.env.example` to `.env` in its folder and add your Anthropic API key:

```bash
cp arxiv-scraper/.env.example arxiv-scraper/.env
cp AF-and-LW-scraper/.env.example AF-and-LW-scraper/.env
```

### Usage

Run each scraper's scripts from inside its folder with `uv run python ...` (plain `python` uses your system Python and fails with `ModuleNotFoundError`). Each script's defaults read the previous step's output.

| Task | Command (from the scraper's folder) | Output |
| --- | --- | --- |
| Scrape, filter and shortlist arXiv papers | `uv run python src/scrape_arxiv_papers.py`<br>`uv run python src/filter_arxiv_papers.py`<br>`uv run python src/shortlist_arxiv_papers.py` | `arxiv-scraper/results/raw/`, `filtered/` and `shortlisted/`, one folder per year and month (e.g. `results/shortlisted/2026/jan/`) |
| Scrape and filter forum posts | `uv run python src/scrape_forum_posts.py`<br>`uv run python src/filter_forum_posts.py`<br>`uv run python src/annotate_forum_posts.py`<br>`uv run python src/generate_taxonomy_and_editorial.py` | `AF-and-LW-scraper/results/1-lw-posts-raw.csv` to `4-lw-taxonomy-and-editorial.md` |
| Export to the main pipeline | `uv run python export_for_pipeline.py --label 2026` (from this folder) | `draft-pipeline/data/sources-links/<source>-2026.txt`: one URL per line, ready for `pipeline.py add` |

`export_for_pipeline.py` still expects the previous pipelines' outputs (`arxiv-scraper/results/6-arxiv_curated_relevant_only.csv` and `AF-and-LW-scraper/results/1-af_raw_posts.csv` / `1-lw_raw_posts.csv`), so it needs updating before it works with the current ones.

### Options

- `export_for_pipeline.py`: `--label` (output file suffix, default `2026`), `--out-dir` (default `draft-pipeline/data/sources-links/`), `--arxiv` / `--af` / `--lw` (input CSVs), `--af-top` / `--lw-top` (keep only the top N posts by karma; default all AF posts and 300 LW posts)
- For each scraper's script options, see its README.

Run any script with `--help` for details.
