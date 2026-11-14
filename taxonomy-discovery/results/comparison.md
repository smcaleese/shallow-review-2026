# Taxonomy method comparison

Reassignment accuracy: a fresh classifier, given only category names and descriptions, puts the item back in the same category. Balance: 1 = equal sizes.

| Method | Items | Top cats | Leaves | Other | Balance (top) | Sizes (top) | Reassign top | Reassign leaf |
|---|---|---|---|---|---|---|---|---|
| 1-llm-taxonomy | 624 | 12 | 48 | 0% | 0.98 | 28–77 | 86% | 96% |
| 2-llm-knn-graph | 624 | 10 | 63 | 0% | 0.97 | 35–109 | 86% | 92% |
| 3-embedding-knn-graph | 624 | 10 | 63 | 0% | 0.96 | 32–135 | 76% | 80% |
| 4-human-taxonomy | 624 | 8 | 9 | 0% | 0.94 | 21–135 | 90% | 95% |
| 5-semantic-map | 624 | 8 | 32 | 0% | 0.98 | 54–139 | 67% | 69% |
| 6-map-taxonomy | 624 | 12 | 39 | 0% | 0.97 | 15–82 | 90% | 93% |

## Agreement between methods (top level, adjusted Rand index)

- 1-llm-taxonomy vs 2-llm-knn-graph: 0.47
- 1-llm-taxonomy vs 3-embedding-knn-graph: 0.29
- 1-llm-taxonomy vs 4-human-taxonomy: 0.39
- 1-llm-taxonomy vs 5-semantic-map: 0.27
- 1-llm-taxonomy vs 6-map-taxonomy: 0.46
- 2-llm-knn-graph vs 3-embedding-knn-graph: 0.22
- 2-llm-knn-graph vs 4-human-taxonomy: 0.33
- 2-llm-knn-graph vs 5-semantic-map: 0.26
- 2-llm-knn-graph vs 6-map-taxonomy: 0.39
- 3-embedding-knn-graph vs 4-human-taxonomy: 0.25
- 3-embedding-knn-graph vs 5-semantic-map: 0.55
- 3-embedding-knn-graph vs 6-map-taxonomy: 0.41
- 4-human-taxonomy vs 5-semantic-map: 0.25
- 4-human-taxonomy vs 6-map-taxonomy: 0.37
- 5-semantic-map vs 6-map-taxonomy: 0.37

## Most-confused category pairs

**1-llm-taxonomy**
- top: Alignment Auditing, Model Organisms and Incidents ↔ Scheming, Deception and Situational Awareness (10 items)
- top: Risk Assessment, Strategy and Foundations ↔ Scheming, Deception and Situational Awareness (5 items)
- top: Alignment Training and Scalable Oversight ↔ Emergent Misalignment and Training-Data Generalization (4 items)
- leaf: Emergence of reward hacking in RL ↔ Reward hacking benchmarks and measurement (2 items)
- leaf: Emergence of reward hacking in RL ↔ Emergent misalignment phenomena and mechanisms (2 items)
- leaf: Auditing tools, agents and benchmarks ↔ In-the-wild misalignment and incident investigations (2 items)

**2-llm-knn-graph**
- top: Misaligned motivations, evaluations and incidents ↔ Scheming, Evaluation Awareness, and Training Gaming (10 items)
- top: Detecting Hidden Misalignment via Internals and Elicitation ↔ Reward Hacking, Oversight, and Automated AI Research (8 items)
- top: AI Control and Agent Monitoring ↔ Reward Hacking, Oversight, and Automated AI Research (5 items)
- leaf: Subliminal Learning and Distillation Transfer ↔ Training Data Attribution for Behaviors (2 items)
- leaf: CoT Faithfulness Evaluation and Training ↔ Training Pressure Degrading Monitorability (2 items)
- leaf: Emotion, Welfare, and Valence Representations ↔ Persona Selection and AI Identity (2 items)

**3-embedding-knn-graph**
- top: AI Control and Agentic Safety ↔ Alignment auditing and misalignment assessment (15 items)
- top: Emergent Misalignment and Training Generalization ↔ Reward Hacking and Reward-Seeking in RL (14 items)
- top: Alignment auditing and misalignment assessment ↔ Emergent Misalignment and Training Generalization (9 items)
- leaf: RLVR Hacking Testbeds and Mitigations ↔ Specification Gaming and Training Resistance (3 items)
- leaf: Control Roadmaps and Distributed Threats ↔ Prompt Injection Attacks and Defenses (3 items)
- leaf: Alignment Faking and Training-Induced Misalignment ↔ Emergent Misalignment From Reward Hacking (2 items)

**4-human-taxonomy**
- top: AI control and monitoring ↔ Evaluations and auditing (8 items)
- top: AI control and monitoring ↔ RL safety (8 items)
- top: AI control and monitoring ↔ Interpretability (8 items)
- leaf: AI control methods ↔ Evaluations and auditing (4 items)
- leaf: Interpretability ↔ Pre-training and post-training: personas, character and psychology (4 items)
- leaf: Evaluations and auditing ↔ Pre-training and post-training: personas, character and psychology (3 items)

**5-semantic-map**
- top: AI control and agent monitoring ↔ Reward hacking and adversarial robustness (23 items)
- top: AI control and agent monitoring ↔ Safety evaluation validity and elicitation (21 items)
- top: AI control and agent monitoring ↔ Alignment strategy and frontier incidents (19 items)
- leaf: Alignment auditing benchmarks ↔ Eliciting self-reports via introspection training (5 items)
- leaf: Reward hacking in LLM RL ↔ Reward-seeking and fitness-seeker threat models (5 items)
- leaf: Evaluation awareness and realism ↔ Frontier system cards and model behavior (4 items)

**6-map-taxonomy**
- top: Generalization from training ↔ Interpretability (6 items)
- top: Finding hidden misalignment ↔ Interpretability (6 items)
- top: AI character, identity and welfare ↔ Generalization from training (6 items)
- leaf: CoT monitorability and obfuscation ↔ Monitors, red-teaming and evasion (3 items)
- leaf: Circuits, parameters and sparse autoencoders ↔ Predicting failures before release (2 items)
- leaf: Lie detection and secret elicitation ↔ Probes and alignment audits (2 items)
