#!/usr/bin/env bash
# Build the combined site (arXiv, LW/AF, Lenz's org list, Safety Stack) in one go. Safe to re-run: every Claude step skips work it has already done,
# so only new items cost API calls.
#
# Usage (from anywhere):
#   ./facets-shared/run_pipeline.sh            # sync inputs, then run every step
#   ./facets-shared/run_pipeline.sh --no-sync  # keep the current input/ snapshot
#   ./facets-shared/run_pipeline.sh --offline  # no API calls: dedupe from cached answers, rebuild from existing tags
#
# Needs ANTHROPIC_API_KEY (in the environment or facets-shared/.env) and uv.
set -euo pipefail
cd "$(dirname "$0")"

SYNC=1
OFFLINE=0
for arg in "$@"; do
  case $arg in
    --no-sync) SYNC=0 ;;
    --offline) OFFLINE=1 ;;
    *) echo "unknown option $arg"; exit 1 ;;
  esac
done

[ $SYNC = 1 ] && ./sync_inputs.sh
echo "== 0b. fetch org pages";      uv run python src/fetch_lenz_pages.py
echo "== 1. load sources";          uv run python src/load_sources.py
echo "== 2. fetch LW post text";    uv run python src/fetch_lw_bodies.py
if [ $OFFLINE = 1 ]; then
  echo "== 3. dedupe (cached answers only)"; uv run python src/dedupe.py --cached-only
else
  echo "== 3. dedupe";               uv run python src/dedupe.py
  echo "== 4. tag";                  uv run python src/tag.py
fi
echo "== 5. apply rules";            uv run python src/postprocess.py
if [ $OFFLINE = 1 ]; then
  echo "== 6. rank (existing scores)"; uv run python src/rank.py --offline
else
  echo "== 6. rank";                 uv run python src/rank.py
fi
echo "== 7. keep the budget";        uv run python src/select_budget.py
echo "== 8. build site and CSV";     uv run python src/build_site.py
echo "done: open site/index.html, or run: python3 -m http.server 8767 --directory facets-shared/site"
