#!/usr/bin/env bash
# Copy the latest source files from the other pipelines into input/.
# The pipeline only reads input/, so the site is always built from a known snapshot. Rerun this to update it.
set -euo pipefail
cd "$(dirname "$0")"
REPO=..
ARXIV=$REPO/scraping-scripts/arxiv-scraper/results
mkdir -p input/arxiv-papers-filtered

copy() {
  cp "$1" "$2"
  if [[ "$2" == *.csv ]]; then
    rows=$(python3 -c "import csv,sys; print(sum(1 for _ in csv.DictReader(open(sys.argv[1]))))" "$2")
  elif [[ "$2" == *.jsonl ]]; then
    rows=$(wc -l < "$2" | tr -d ' ')
  else
    rows="-"
  fi
  printf "  %-45s %6s rows  <- %s\n" "${2#input/}" "$rows" "$1"
}

echo "Syncing inputs:"
# arXiv: the top-10% shortlist, plus every filtered paper (to match LW posts against papers that weren't shortlisted)
copy "$ARXIV/shortlisted/2026/arxiv-papers-shortlisted.csv" input/arxiv-papers-shortlisted.csv
for month_dir in "$ARXIV"/filtered/2026/*/; do
  month_dir=${month_dir%/}
  copy "$month_dir/arxiv-papers-filtered.csv" "input/arxiv-papers-filtered/$(basename "$month_dir").csv"
done
# LW/AF: Jord's notable posts, his scope decisions and the author -> org roster
copy "$REPO/jord-facets/data/2-notable-posts.csv" input/lw-notable-posts.csv
copy "$REPO/jord-facets/scope_overrides.json" input/lw-scope-overrides.json
copy "$REPO/jord-facets/roster.json" input/lw-roster.json
# Last year's agendas (the copy in taxonomy/input is the one tracked in git)
copy "$REPO/taxonomy/input/taxonomy-2025.yaml" input/taxonomy-2025.yaml

date -u +"%Y-%m-%dT%H:%M:%SZ" > input/SYNCED_AT
echo "Done ($(cat input/SYNCED_AT))"
