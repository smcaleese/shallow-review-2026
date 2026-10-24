# Taxonomy method comparison

Reassignment accuracy: a fresh classifier, given only category names and descriptions, puts the item back in the same category. Balance: 1 = equal sizes. vs 2025: agreement of the top level with each item's 2025 top-level group (from facets-shared's agenda tag); 0 = chance, 1 = identical.

| Method | Items | Top cats | Leaves | Other | Balance (top) | Sizes (top) | Reassign top | Reassign leaf | NMI vs 2025 | ARI vs 2025 |
|---|---|---|---|---|---|---|---|---|---|---|
| 1-llm-taxonomy | 285 | 12 | 40 | 0% | 0.98 | 9–40 | 86% | 99% | 0.35 | 0.13 |
| 2-llm-knn-graph | 285 | 10 | 26 | 0% | 0.97 | 17–45 | 88% | 93% | 0.30 | 0.10 |
| 3-embedding-knn-graph | 285 | 10 | 26 | 0% | 0.98 | 12–44 | 70% | 79% | 0.22 | 0.06 |
| 4-human-taxonomy | 285 | 8 | 9 | 1% | 0.98 | 21–50 | 91% | 94% | 0.35 | 0.16 |

## Agreement between methods (top level, adjusted Rand index)

- 1-llm-taxonomy vs 2-llm-knn-graph: 0.53
- 1-llm-taxonomy vs 3-embedding-knn-graph: 0.27
- 1-llm-taxonomy vs 4-human-taxonomy: 0.51
- 2-llm-knn-graph vs 3-embedding-knn-graph: 0.27
- 2-llm-knn-graph vs 4-human-taxonomy: 0.48
- 3-embedding-knn-graph vs 4-human-taxonomy: 0.26

## Most-confused category pairs

**1-llm-taxonomy**
- top: Theory, Threat Models and Strategy ↔ Training Generalization and Alignment Training (4 items)
- top: Interpretability ↔ Theory, Threat Models and Strategy (3 items)
- top: Scheming, Sabotage and Misaligned Propensities ↔ Theory, Threat Models and Strategy (2 items)
- leaf: Hardening Benchmarks and Detecting Hacks ↔ Monitor Design and Deployment (1 items)
- leaf: Jailbreaks and Safeguard Classifiers ↔ Monitor Design and Deployment (1 items)
- leaf: CoT Obfuscation and Faithfulness ↔ Other Incidents and System Cards (1 items)

**2-llm-knn-graph**
- top: Alignment theory, risk arguments, and agendas ↔ Reward hacking and reward-seeking from RL (5 items)
- top: Alignment theory, risk arguments, and agendas ↔ other (5 items)
- top: Detecting Hidden Misalignment and Deception ↔ Reward hacking and reward-seeking from RL (3 items)
- leaf: Debating ASI misalignment risk ↔ Reward-seeking threat models and theory (2 items)
- leaf: Alignment Auditing and Hidden-Behavior Elicitation ↔ Honesty Elicitation and Self-Reporting (1 items)
- leaf: Automating and deferring alignment research ↔ Benchmarks measuring agent specification gaming (1 items)

**3-embedding-knn-graph**
- top: Conceptual Essays on AI Minds and Risk ↔ Misalignment Debates, Threat Models, and Strategy (7 items)
- top: LLM Deception, Lie Detection, Hidden Knowledge ↔ Training Data, Personas, and Misalignment Generalization (6 items)
- top: Misalignment Debates, Threat Models, and Strategy ↔ Reward Hacking and Training Subversion (6 items)
- leaf: Multi-Agent Collusion and Self-Propagation ↔ Scheming Propensity Evaluation Methods (3 items)
- leaf: Jailbreaks, Safeguards, Pre-Release Risk Evals ↔ Pretraining and Midtraining Data Interventions (3 items)
- leaf: Emergent Misalignment from Fine-Tuning ↔ Reward Hacking and Training Subversion (3 items)

**4-human-taxonomy**
- top: AI control and monitoring ↔ Interpretability (4 items)
- top: AI control and monitoring ↔ RL safety (3 items)
- top: AI control and monitoring ↔ Misuse and dangerous capabilities (3 items)
- leaf: Agent foundations and alignment strategy ↔ RL safety (2 items)
- leaf: Agent foundations and alignment strategy ↔ Pre-training and post-training: personas, character and psychology (2 items)
- leaf: Evaluations and auditing ↔ RL safety (2 items)
