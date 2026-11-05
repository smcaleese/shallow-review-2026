### Safety Stack sources

Finds 2026 documents in [The Safety Stack](https://huggingface.co/datasets/thesafetystack/the-safety-stack) dataset that the Shallow Review 2026 sources don't already have, then curates them with the arXiv scraper's own filter and shortlist steps.

| Step | Command (from the repo root) | Output |
| --- | --- | --- |
| 1. Find new sources | `cd safety-stack && uv run python find_new_sources.py` | `output/safety-stack-2026-new.csv`: 2026 docs not matching any arXiv or LessWrong source in `scraping-scripts`, `facets-shared/input` or the main pipeline (by arXiv ID, LessWrong post ID, URL or title) |
| 2. Add abstracts | `uv run --project scraping-scripts python safety-stack/prepare_for_curation.py` | `results/raw/2026/<month>/`: the arXiv scraper's raw format. The dataset withholds abstracts, so they come from arXiv, Semantic Scholar or OpenAlex, falling back to the dataset's quotes |
| 3. Filter | `cd scraping-scripts/arxiv-scraper && uv run python src/filter_arxiv_papers.py --raw-dir ../../safety-stack/results/raw --output-dir ../../safety-stack/results/filtered` | `results/filtered/`: Claude Haiku ratings, keeping 4+/5 |
| 4. Shortlist | `cd scraping-scripts/arxiv-scraper && uv run python src/shortlist_arxiv_papers.py --filtered-dir ../../safety-stack/results/filtered --output-dir ../../safety-stack/results/shortlisted` | `results/shortlisted/`: Claude Opus picks the top ~9% per month |
| 5. Curated list | `cd safety-stack && uv run --project ../scraping-scripts python build_curated_list.py` | `output/curated-sources.md` / `.csv` (shortlist) and `output/filtered-sources.csv` (everything rated 4+) |

`notebook.ipynb` is for exploring the dataset and the step 1 output.
