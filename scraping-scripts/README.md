### Scraping Scripts

Optional scrapers that find candidate papers and posts for the Shallow Review of Technical AI Safety, rate them for relevance with Claude, and narrow them down to a reading list. Each scraper has its own README with full usage and options.

### Scrapers

| Scraper | Finds | Pipeline | Details |
| --- | --- | --- | --- |
| [`arxiv-scraper/`](arxiv-scraper/) | arXiv papers | Keyword search month by month, with Semantic Scholar citation data → Claude Haiku rates each paper 1–5 and keeps 4+ → Claude Opus shortlists the most important ~9% per month. For January to October 9, 2026: 12,183 papers → 1,537 → 135 | [README](arxiv-scraper/README.md) |
| [`AF-and-LW-scraper/`](AF-and-LW-scraper/) | Alignment Forum and LessWrong posts | Fetches a year of posts (one LessWrong scrape also covers every Alignment Forum post) → Claude Haiku rates them and keeps the highly relevant ones (~20%) → Claude Opus shortlists the most important ~12% per month (~160 a year) | [README](AF-and-LW-scraper/README.md) |

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
| Scrape, filter and shortlist forum posts | `uv run python src/scrape_forum_posts.py`<br>`uv run python src/filter_forum_posts.py`<br>`uv run python src/shortlist_forum_posts.py` | `AF-and-LW-scraper/results/1-lw-posts-raw.csv`, `2-lw-posts-highly-relevant.csv` and `shortlisted/`, one folder per year and month (e.g. `results/shortlisted/2026/jan/`) |
| Export the two shortlists to the main pipeline | `uv run python export_for_pipeline.py` (from this folder) | `draft-pipeline/data/sources-links/shortlist-arxiv-2026.txt` and `shortlist-lw-2026.txt`: one URL per line, ready for `src/add_entries.py` |

### Options

- `export_for_pipeline.py`: `--label` (output file suffix, default `2026`), `--out-dir` (default `draft-pipeline/data/sources-links/`), `--arxiv` / `--lw` (the combined shortlist CSVs, default `<scraper>/results/shortlisted/2026/`)
- For each scraper's script options, see its README.

Run any script with `--help` for details.
