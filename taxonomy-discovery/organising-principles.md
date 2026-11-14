# Candidate organising principles for the top level

`data-driven-taxonomy.md` groups its 15 agendas by one principle: **where the work acts on the model** (training,
inspection, deployment, plus strategy). This file lists that and eight other ways to split the same 15 agendas into
2–4 high-level categories, and scores each one the same way. One of them comes from the data itself (a bottom-up
clustering of method 2's neighbour graph); the rest are principles chosen in advance and checked against the data.

No method produces categories at this level: all six stop at 8–12 top-level clusters. So any top level is a lens on the
agendas, not something the clustering discovered. The question is which lens fits the data best and reads most
clearly.

## The 15 agendas

From `data-driven-taxonomy.md`. Sizes are median item counts across methods (sources, not distinct works; ±30%).

| # | Agenda | Items |
|---|---|---|
| 1 | Reward hacking and reward seeking | ~60 |
| 2 | Emergent misalignment and training generalisation | ~41 |
| 3 | Training-data effects (subliminal learning, data attribution) | ~22 |
| 4 | Model character and values (personas, constitutions, welfare, sycophancy) | ~53 |
| 5 | Scalable oversight and debate | ~10 |
| 6 | Scheming and training gaming | ~36 |
| 7 | Evaluation awareness and eval validity | ~33 |
| 8 | Honesty, lie detection and self-report | ~39 |
| 9 | Alignment auditing, model organisms and incidents | ~39 |
| 10 | Interpretability | ~42 |
| 11 | Chain-of-thought monitorability | ~59 |
| 12 | AI control and agent monitoring | ~65 |
| 13 | Misuse, adversarial robustness and dangerous capabilities | ~62 |
| 14 | Multi-agent risks | ~18 |
| 15 | Strategy, threat models and frontier risk reporting | ~41 |

## How the principles are scored

- **Balance**: the size of each high-level category. One category holding most of the corpus makes the top level
  useless.
- **Boundary sentence**: the one question you would ask of a paper to place it. A good one has a single answer for
  most papers.
- **Confusion kept inside**: the classifier in `compare.py` re-sorts every item using only category names and
  descriptions. `results/comparison.md` lists, for each method, the top-level category pairs it confuses most, with
  item counts. I mapped those 18 pairs (185 items in all) onto the 15 agendas and measured what share of the confused
  items falls *inside* one high-level category. A grouping that keeps confusions inside its categories should be
  stable when papers are re-sorted. Three versions:
  - **all**: all 18 pairs.
  - **LLM only**: the 5 pairs from methods 1 and 2 (42 items). These methods have the clearest categories and the
    highest scores, so their confusions are the most meaningful.
  - **without control**: the 13 pairs that don't involve agenda 12 (78 items). See the first finding below for why.

The mapping of method categories onto agendas is approximate. Some method categories span two agendas: method 2's
"Reward Hacking, Oversight, and Automated AI Research" is mapped to agenda 1, and method 4's coarse categories to their
closest agenda. Treat differences of under ~10 points as noise.

## Three findings that shape all the options

**1. AI control is the hub.** Control (12) appears in 8 of the 18 confused pairs: with reward hacking, auditing,
evals, interpretability and strategy. Those pairs hold 107 of the 185 items, mostly from methods 3, 4 and 5, the
embedding and coarse ones. Control papers use model organisms, evaluations, monitors and probes, so they look like
every other agenda. Every principle that puts control in a "deployment" or "safeguards" category, apart from
evaluations and auditing, loses most of that weight. This is the main reason most principles score low on "all".

**2. The bottom-up structure is not the lifecycle.** I computed the link density between top-level categories on
method 2's LLM neighbour graph and merged the closest categories first (average linkage), for methods 1 and 2:
- **Generalisation science**: emergent misalignment, training data, personas and interpretability join early in both
  methods. Interpretability is closer to them than to auditing. Persona vectors, data attribution and model diffing
  study how training shapes a model's internals.
- **Misaligned behaviour and how to catch it**: scheming, auditing and model organisms, evaluations and incidents, and
  multi-agent risks form one block. In method 1, reward hacking, alignment training and strategy join it too.
- **Securing deployed agents**: control and misuse pair up in method 1. In method 2, control instead pairs with
  reward hacking and automated AI research.
- **CoT monitorability stays on its own.** It is a tight cluster with few links outward, and it is the last to merge
  in both methods. Any principle has to assign it by fiat.

**3. The lifecycle principle fits less well than `data-driven-taxonomy.md` says.** That file says the most-confused
pairs "mostly fall inside" its categories. On all 18 pairs, the share inside is 27%. On methods 1 and 2 only it's
57%, and without control it's 64%. It cited the pairs that fit, such as auditing and scheming, or EM and reward
hacking. The pairs that cross its boundaries are control with evals or auditing, and interpretability with
generalisation.

## The candidates

### A. Where the work acts (lifecycle) — the current choice

> *Is the object of study a training process, a finished model being examined, or a running system with safeguards?*

| Category | Agendas | Items |
|---|---|---|
| Training | 1, 2, 3, 4, 5 | ~186 |
| Inspection | 6, 7, 8, 9, 10 | ~189 |
| Deployment | 11, 12, 13, 14 | ~204 |
| Strategy | 15 | ~41 |

Confusion inside: all 27%, LLM only 57%, without control 64%.

- **For**: the best balance of any candidate, and an intuitive story that readers know from lab safety frameworks.
- **Against**: it splits interpretability from the generalisation work it clusters with. It also splits control from
  the evals and auditing it is most confused with. CoT monitorability is a deployment safeguard only in part.

### B. Threat source

> *Where does the harm come from: the model's own goals, a human misusing it, or interactions between many AIs and
> people?*

| Category | Agendas | Items |
|---|---|---|
| Misalignment | 1–12, 15 | ~540 |
| Misuse | 13 | ~62 |
| Multi-agent and societal | 14 | ~18 |

Confusion inside: 100% on every version.

- **For**: perfect on confusions, and it matches how risk is usually framed.
- **Against**: it is perfect only because nearly everything is in one category. That makes it a useless top level for
  this corpus, though a useful *secondary tag*.

### C. Defence in depth: prevent, detect, contain

> *Does the work make the model less likely to be misaligned, find out whether it is, or limit the damage if it is?*

| Category | Agendas | Items |
|---|---|---|
| Prevent (alignment training) | 1, 2, 3, 4, 5 | ~186 |
| Detect (evals, auditing, interpretability, CoT monitoring) | 6, 7, 8, 9, 10, 11 | ~248 |
| Contain (control, security, multi-agent) | 12, 13, 14 | ~145 |
| Strategy | 15 | ~41 |

Confusion inside: all 27%, LLM only 57%, without control 64%.

- **For**: the same scores as A, with a clearer story about *purpose*. It also gives CoT monitorability a natural
  home in Detect, since it is about reading the model's reasoning.
- **Against**: the same weak points as A. The Prevent/Detect line is blurry for reward hacking and emergent
  misalignment papers, which mostly *detect* a failure that training causes.

### D. Kind of contribution: science, measurement, safeguards

> *Does the paper mainly explain a phenomenon, build a way to measure it, or build a safeguard against it?*

| Category | Agendas | Items |
|---|---|---|
| Science of model behaviour | 1, 2, 3, 4, 6, 14 | ~230 |
| Measurement tools | 7, 8, 9, 10, 11 | ~212 |
| Safeguards | 5, 12, 13 | ~137 |
| Strategy | 15 | ~41 |

Confusion inside: all 16%, LLM only 10%, without control 38%.

- **For**: balanced, and it matches how researchers describe their own contribution.
- **Against**: the worst fit to the data. Most papers do two of these at once: they show a failure and propose a fix,
  or build an eval and report what it finds. That makes it better as a per-paper facet than as a top level.

### E. Bottom-up from method 2's graph (data-driven)

> *Which agendas does the LLM neighbour graph link most densely?* (Method 1's categories at 4 groups, renamed)

| Category | Agendas | Items |
|---|---|---|
| How models come to have their dispositions (generalisation, data, character, internals) | 2, 3, 4, 10 | ~158 |
| Misaligned behaviour and how to catch it | 1, 5, 6, 7, 8, 9, 14, 15 | ~276 |
| Securing deployed agents | 12, 13 | ~127 |
| CoT monitorability | 11 | ~59 |

Confusion inside: all 26%, LLM only 88%, without control 63%.

- **For**: the only candidate that comes from the data, and the best on the LLM methods' confusions. It also puts
  interpretability with the generalisation science it is actually linked to.
- **Against**: unbalanced, with a large middle category. CoT monitorability is a category of one, and naming the
  second category takes some effort. The structure also depends on the method: in method 2, reward hacking pairs with
  control rather than with the behaviour block.

### F. Level of access

> *Does the work rely on the model's outputs, its reasoning trace and internals, or its training process?*

| Category | Agendas | Items |
|---|---|---|
| Behaviour (black-box: evals, auditing, control, misuse, reward hacking) | 1, 6, 7, 9, 12, 13, 14 | ~313 |
| Reasoning and internals (interpretability, lie detection, CoT) | 8, 10, 11 | ~140 |
| Training interventions | 2, 3, 4, 5 | ~126 |
| Strategy | 15 | ~41 |

Confusion inside: all 64%, LLM only 88%, without control 49%.

- **For**: the best "all" score apart from B, because it keeps control together with evals and auditing, all
  black-box. It is also an easy test to apply to a paper.
- **Against**: the Behaviour category is large (half the corpus). Many papers mix levels, for example an audit that
  uses both probes and behaviour. It also says little about *why* the work matters.

### G. Assumed adversary

> *How much does the work assume the model is working against us?*

| Category | Agendas | Items |
|---|---|---|
| Cooperative model: make it better | 1, 2, 3, 4, 5 | ~186 |
| Possibly misaligned: find out | 6, 7, 8, 9, 10 | ~189 |
| Scheming worst case: oversee it anyway | 11, 12 | ~124 |
| External adversaries: misuse and multi-agent | 13, 14 | ~80 |
| Strategy | 15 | ~41 |

Confusion inside: all 27%, LLM only 57%, without control 64%.

- **For**: it states the security mindset explicitly. It separates AI control (the model is the adversary) from misuse
  defence (a human is the adversary), which A and C merge.
- **Against**: five categories, one more than the limit. Its scores are those of A. Many papers don't state their
  assumption.

### H. Unit of analysis

> *Is the object of study the model's internals, a single model's behaviour, a model inside a system, or many agents
> and society?*

| Category | Agendas | Items |
|---|---|---|
| Internals | 3, 8, 10 | ~103 |
| Single-model behaviour | 1, 2, 4, 6, 7, 9, 11 | ~321 |
| Model in a system (control, security, oversight protocols) | 5, 12, 13 | ~137 |
| Many agents, society and strategy | 14, 15 | ~59 |

Confusion inside: all 33%, LLM only 76%, without control 78%.

- **For**: a crisp test, and good scores once control is set aside.
- **Against**: unbalanced, with half the corpus in "single-model behaviour". Interpretability lands apart from the
  generalisation work it clusters with.

### I. Misalignment science vs. oversight and security

> *Is the work trying to understand and shape what the model wants, or to keep the system safe whatever it wants?*

| Category | Agendas | Items |
|---|---|---|
| Misalignment science (how misalignment arises, how to find and fix it) | 1, 2, 3, 4, 6, 7, 8, 9, 10 | ~365 |
| Oversight and security (monitoring, control, misuse, oversight protocols) | 5, 11, 12, 13 | ~196 |
| Societal and strategic | 14, 15 | ~59 |

Confusion inside: all 39%, LLM only 76%, without control 94%.

- **For**: the best fit to the data once the control hub is set aside. It matches a real split in the field, between
  alignment researchers and control and security researchers. Each side has a clear identity.
- **Against**: the first category holds about 60% of the corpus. It would need sub-areas, for example A's Training /
  Inspection split inside it. Control is still confused with evals and auditing across the line.

## Comparison

| Principle | Categories (items) | Balance | All | LLM only | No control |
|---|---|---|---|---|---|
| A. Lifecycle | 186 / 189 / 204 / 41 | best | 27% | 57% | 64% |
| B. Threat source | 540 / 62 / 18 | worst | 100% | 100% | 100% |
| C. Prevent / detect / contain | 186 / 248 / 145 / 41 | good | 27% | 57% | 64% |
| D. Science / measurement / safeguards | 230 / 212 / 137 / 41 | good | 16% | 10% | 38% |
| E. Bottom-up graph | 158 / 276 / 127 / 59 | fair | 26% | **88%** | 63% |
| F. Level of access | 313 / 140 / 126 / 41 | fair | **64%** | **88%** | 49% |
| G. Assumed adversary | 186 / 189 / 124 / 80 / 41 | good (5 cats) | 27% | 57% | 64% |
| H. Unit of analysis | 103 / 321 / 137 / 59 | poor | 33% | 76% | 78% |
| I. Misalignment science vs oversight | 365 / 196 / 59 | poor | 39% | 76% | **94%** |

## Takeaways

- **No principle is both balanced and a good fit.** The balanced ones (A, C, D, G) cut through the data's strongest
  links. The good fits (B, E, F, I) have one dominant category.
- **Two candidates fit the data and still read well:**
  - **C (prevent / detect / contain)**: about as balanced as A, a clearer purpose, and a natural home for CoT
    monitorability.
  - **I (misalignment science vs oversight)**: the closest match to how the field divides itself, with A's
    Training / Inspection split as sub-areas inside the larger side.
- **Where AI control goes decides most of the score.** Whatever the top level, control should sit next to evaluations
  and auditing, or carry a cross-reference to them. It is also worth deciding explicitly whether "control" means
  deployment protocols (with misuse and security) or misalignment detection (with auditing).
- **Facets, not the top level.** B (threat source) and D (kind of contribution) work poorly as top levels but would
  work well as tags on each paper. The facets site already has similar facets (evidence, scientific move).

## How to test a choice

The scores above use confused pairs from earlier runs, mapped by hand. A direct test is cheap: write a candidate as a
`taxonomy.yaml`, with the high-level categories as top-level entries and the agendas as children, in a new method
folder like `4-human-taxonomy/`. Then run `run.py`, `compare.py` and `report.py`. The top-level reassignment accuracy,
the confused pairs and the `matrix.png` link share (on method 2's graph) then measure the high level directly. That
costs about $2 per candidate.

The two short scripts behind the numbers here (the bottom-up merge order, and the balance and confusion scores) are
not in the repo yet.
