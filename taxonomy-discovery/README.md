# Taxonomy discovery

Three automated ways of building a two-level taxonomy for the 2026 shallow review, all scored the same way so they
can be compared. Each method is self-contained: either LLM-only or embedding-only, with no hybrids.

| Folder | Method | How items get grouped |
|---|---|---|
| `1-llm-taxonomy/` | LLM direct taxonomy | Claude reads every item at once and proposes the taxonomy; a classifier assigns items; Claude refines it from what landed where |
| `2-llm-knn-graph/` | LLM nearest-neighbour graph + Leiden | Claude reads every item and lists each one's 15 nearest items by research agenda; Leiden finds communities in that graph |
| `3-embedding-knn-graph/` | Embedding nearest-neighbour graph + Leiden (baseline) | Same as 2, but neighbours come from cosine similarity of local embeddings |
| `4-human-taxonomy/` | Hand-written taxonomy | Categories from `4-human-taxonomy/taxonomy.yaml` (written by a person); the method 1 classifier sorts items into them |

Methods 2 and 3 share everything after the neighbour lists (`shared/graph.py`), so comparing them isolates LLM vs.
embedding similarity. In both, Claude only *names* the clusters at the end; it doesn't change membership.

## Running it

From this folder, with `ANTHROPIC_API_KEY` set (or in `.env` here; otherwise the key in `taxonomy/.env` or
`main-pipeline/.env` is used):

```bash
uv sync
uv run python 3-embedding-knn-graph/run.py   # ~$0.25 (naming only); downloads the embedding model once
uv run python 2-llm-knn-graph/run.py         # ~$5: 2 passes x 57 calls, the item list is prompt-cached
uv run python 1-llm-taxonomy/run.py          # ~$2-3 with the default 1 refinement round
uv run python 4-human-taxonomy/run.py        # ~$0.80: sorts items into taxonomy.yaml
uv run python compare.py                     # ~$4: scores every method and writes results/comparison.md
uv run python report.py                      # free: taxonomy.md + figures for each method
```

Add `--limit 40` to any method to try it on a fixed random sample. Every Claude call is cached on disk in `cache/`,
so reruns only pay for calls whose prompts changed. Default model is Claude Opus 5.5; pass `--model
claude-sonnet-5-5` (or set `TAXONOMY_MODEL`) to change it. Each script prints its token use and estimated cost.

Each method writes to its own `output/`:
- `taxonomy.md` (from `report.py`): the taxonomy as a document, with descriptions, sizes, example items and scores
- `graph.png` (from `report.py`): the categories drawn on a nearest-neighbour graph. A numbered overview with a
  legend, then one panel per top-level category with its members highlighted and its subcategories labelled.
  Methods 1 and 4 have no graph of their own, so they're drawn on method 2's LLM neighbour graph. The layout pulls items in the
  same category together, so read spread and overlap from the panels, not from distances on the overview.
- `matrix.png`: the neighbour graph as a 285 × 285 matrix, sorted by category. Good categories are dark squares on
  the diagonal; shading off the diagonal is overlap. The title gives the share of all link strength that falls
  inside categories (method 2: 69%, method 4 on method 2's graph: 61%, method 1 on method 2's graph: 58%,
  method 3: 55%). No layout, so the most
  accurate of the graph views.
- `category_map.png`: one circle per top-level category with lines for the most strongly linked pairs, and a
  heatmap of average link strength within and between every pair of categories.
- `treemap.png`: the taxonomy as nested boxes sized by item count (hierarchy only, no links).
- `clusters.json`: the taxonomy and each item's category, in the shared format described in `shared/taxonomy.py`
- `clusters.md`: every category with all member titles
- `neighbours.json` (methods 2 and 3): each item's neighbour list; `history.json` (method 1): each refinement round

## Input

The 285 in-scope items from `facets-shared/data/2-items-deduped.jsonl` (the 2026 arXiv shortlist plus notable
LW/AF posts, deduplicated), dropping the ones facets-shared's tagger marked out of scope. arXiv papers come with
their abstract, LW posts with their opening ~2,000 characters. Items get short ids (`P001`...) in prompts. The whole
set is about 130k tokens, so it fits in one prompt.

## Methods in more detail

**1. LLM direct taxonomy.** Propose (one call, whole item set, effort high) → assign each item to one leaf or
"other" using only names and descriptions (batches of 20, effort low) → refine (`--rounds`, default 1: Claude sees
each category's members and the "other" pile, then merges, splits, renames and adds) → reassign.

**2. LLM nearest-neighbour graph.** The item list goes in the cached system prompt; each call asks for the 15 nearest
items to 5 target items. "Near" means same research problem or agenda, not shared method or model. Each pass
(`--passes`, default 2) shows the items in a different order (original, reversed) to reduce position bias. Edge
weight averages over passes and both directions, so a pair that picked each other in both passes weighs 1.

**3. Embedding nearest-neighbour graph.** `BAAI/bge-large-en-v1.5` embeddings of title + text (`--embedder` to
change), 15 nearest by cosine similarity.

**4. Hand-written taxonomy.** Edit `4-human-taxonomy/taxonomy.yaml` (names and descriptions, optional
subcategories) and rerun; the descriptions are what the classifier sees, so write them as inclusion criteria. The
first six categories organise the field by the model stage each technique acts on; "Misuse and dangerous
capabilities" and "Evaluations and auditing" were added after a coverage test left 19 of 285 items with no home
(now 2). Like method 1, it has no graph of its own, so its figures use method 2's LLM neighbour graph. With 8
categories and 9 leaves it's coarser than the others, which makes reassignment accuracy and within-category link
share easier to score well on.

**Graph → taxonomy (2 and 3).** Leiden community detection with the resolution tuned to give about 10 top-level
clusters, then Leiden again inside each top cluster for about one subcluster per 10 items (`--top-target`,
`--sub-size`). Members of clusters smaller than 3 join the large cluster they're most linked to. Claude then names
each cluster from its members' titles and openings.

## Scoring (`compare.py`)

| Metric | What it measures |
|---|---|
| Reassign top / leaf | A fresh classifier sees only category names and descriptions and re-sorts every item. The share that land where the method put them: do items fit their category, and are categories distinguishable? |
| Most-confused pairs | Which categories the classifier mixes up: candidates to merge or redescribe |
| Other | Share of items in "other" (coverage) |
| Balance, sizes | Size entropy (1 = equal sizes) and smallest–largest top-level category |
| NMI / ARI vs 2025 | Agreement of the top level with each item's 2025 top-level group (from facets-shared's first agenda tag) |
| Agreement between methods | Adjusted Rand index between methods' top levels |

Caveats:
- Method 1 assigns items with the same kind of classifier the score uses, so its reassignment accuracy is partly
  self-consistency and will run higher. The graph methods' descriptions are written after the fact, so their score
  also tests how well the names describe the clusters.
- The 2025 reference is coarse: 102 of 285 items only fit a new 2026 agenda and share one "new 2026" label, and
  "Black-box safety" covers 81 items. Read the NMI/ARI columns as a rough check, not a target.
- Not yet measured: stability across reruns (e.g. different Leiden seeds or item orderings).
