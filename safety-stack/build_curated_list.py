"""Write the curated Safety Stack lists from the shortlist and filter results.

output/curated-sources.md   the shortlist (best first within each month), as a readable list
output/curated-sources.csv  the same, with every column
output/filtered-sources.csv every source the relevance filter rated 4+, best-rated first
"""
import glob
import re
from pathlib import Path

import pandas as pd

HERE = Path(__file__).resolve().parent
MONTHS = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]


def clean_title(t):
    t = re.sub(r"^[A-Z][a-z]{2} \d{2}, \d{4}", "", str(t))  # "Sep 03, 2026GPT-6 ..." from scraped blog pages
    return t.split("Today, we are releasing")[0].strip()


short = pd.read_csv(HERE / "results/shortlisted/2026/arxiv-papers-shortlisted.csv", dtype={"arxiv_id": str})
short["title"] = short["title"].map(clean_title)
short.to_csv(HERE / "output/curated-sources.csv", index=False)

filtered = pd.concat(pd.read_csv(f, dtype={"arxiv_id": str}) for f in glob.glob(str(HERE / "results/filtered/2026/*/arxiv-papers-filtered.csv")))
filtered["title"] = filtered["title"].map(clean_title)
filtered = filtered.sort_values(["relevance", "published"], ascending=[False, True])
filtered.to_csv(HERE / "output/filtered-sources.csv", index=False)

lines = [
    "# Curated 2026 sources from the Safety Stack",
    "",
    f"Safety Stack documents from 2026 that aren't in the Shallow Review 2026 sources, curated with the arXiv scraper's "
    f"filter (Claude Haiku, kept if rated 4+/5) and shortlist (Claude Opus, top ~9% per month) steps, unchanged. "
    f"{len(short)} shortlisted of {len(filtered)} kept by the filter. "
    f"† = published after the Shallow Review scrapes stopped (Oct 10).",
    "",
]
for m in sorted(short["month"].unique(), key=MONTHS.index):
    lines += [f"## {m.capitalize()} 2026", ""]
    for r in short[short["month"] == m].sort_values("shortlist_rank").itertuples():
        dagger = " †" if str(r.after_scrape_cutoff) == "True" else ""
        lines.append(f"- **[{r.title}]({r.url})**{dagger} ({r.doc_type}, {r.domain}, {r.relevance}/5)  \n  {r.shortlist_reason}")
    lines.append("")
(HERE / "output/curated-sources.md").write_text("\n".join(lines))
print(f"{len(short)} shortlisted, {len(filtered)} filtered; after cutoff: {(short.after_scrape_cutoff.astype(str) == 'True').sum()}")
