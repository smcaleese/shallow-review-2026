#!/usr/bin/env bash
# Rebuild the LW/AF tagged dataset, CSV and site in one go. Safe to re-run as new posts come in:
# every Claude-calling step skips posts it has already done, so only new posts cost API calls,
# and tags that were corrected in review stay frozen (patches are re-applied on top).
#
# Prerequisites
#   - Stephen's LW scrape is up to date: run steps 1-2 of ../scraping-scripts/AF-and-LW-scraper first
#     (scrape_forum_posts.py, filter_forum_posts.py), or pass --scrape to do it here.
#   - ANTHROPIC_API_KEY is set (or in .env in this folder).
#   - Python with: anthropic pyyaml   (the scrape step needs that folder's own deps, via uv)
#
# Usage (from anywhere):
#   ./jord-facets/run_pipeline.sh            # tag new notable posts, rebuild everything
#   ./jord-facets/run_pipeline.sh --scrape   # also re-scrape LW and re-run Stephen's relevance filter first
#   ./jord-facets/run_pipeline.sh --offline  # no API calls: just re-apply patches/rules and rebuild outputs
#
# Outputs
#   data/5-tags-final.jsonl     all tags (one JSON object per post, `pp` lists rule changes)
#   data/lw-posts-tagged.csv    in-scope posts, one row per post (columns aligned with taxonomy/output CSV)
#   site/index.html             the interactive page (self-contained; open locally, publish as an artifact,
#                               or deploy like taxonomy/site)
#   review/final-views/*.md     posts grouped under each tag of each facet, for skimming and review
#
# Human-in-the-loop step (not run here): reviewer findings -> src/patch_pass.py -> data/4x-patches-*.jsonl.
# See README.md "Reviewing and correcting tags".
set -euo pipefail
cd "$(dirname "$0")"
[ -f .env ] && set -a && . ./.env && set +a

PY=${PYTHON:-python3}
SCRAPER=../scraping-scripts/AF-and-LW-scraper
R=$SCRAPER/results
T=../main-pipeline/data/taxonomy.yaml
AS_OF=${AS_OF:-$(date +%F)}
OFFLINE=0
for arg in "$@"; do
  case $arg in
    --scrape) (cd $SCRAPER && uv run python src/scrape_forum_posts.py && uv run python src/filter_forum_posts.py) ;;
    --offline) OFFLINE=1 ;;
    *) echo "unknown option $arg"; exit 1 ;;
  esac
done

if [ $OFFLINE = 0 ]; then
  echo "== 1. scope check (new posts only)"
  $PY src/scope_check.py $R/1-lw-posts-raw.csv $R/2-lw-posts-rated.csv data/1-scope-first-pass.jsonl
  echo "== 2. select notable posts (as of $AS_OF)"
  $PY src/select_notable.py $R/1-lw-posts-raw.csv data/2-notable-posts.csv "$AS_OF" data/1-scope-first-pass.jsonl
  echo "== 3. fetch post text (new posts only)"
  $PY src/fetch_bodies.py data/2-notable-posts.csv data/bodies.json
  echo "== 4. tag (new posts only)"
  $PY src/tag.py data/2-notable-posts.csv data/bodies.json vocab.yaml $T roster.json - data/3-tags-raw.jsonl
fi

[ -f data/bodies.json ] || { echo "data/bodies.json missing: run once without --offline (it is not committed)"; exit 1; }

echo "== 5. apply reviewed patches + scope decisions, enforce rules"
$PY src/apply_patches.py data/3-tags-raw.jsonl data/4-patched.jsonl scope_overrides.json data/4*-patches-*.jsonl
$PY src/postprocess.py data/4-patched.jsonl data/bodies.json roster.json data/5-tags-final.jsonl scope_overrides.json

echo "== 6. build site, CSV, views"
$PY src/build_page.py data/5-tags-final.jsonl vocab.yaml $T src/template.html site/index.html
$PY src/export_csv.py site/index.html data/lw-posts-tagged.csv
$PY src/make_views.py site/index.html review/final-views
rm -f review/final-views/items.json
echo "done: site/index.html, data/lw-posts-tagged.csv"
