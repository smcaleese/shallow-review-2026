# A data-driven taxonomy of 2026 AI safety research

Built only from the outputs of the six taxonomy-discovery methods in this folder (624 sources, Jan–Nov 2026). The authors' draft taxonomy was not consulted.

## 1. Summary

Fifteen agendas in four high-level categories. The organising principle is **where the work acts on the model**: while it is being trained, when it is being inspected before or outside deployment, or while it is running in deployment. A fourth, smaller category holds work that reasons about the whole problem rather than acting on any model.

| Category | Agendas | Approx. items | Share of sources |
|---|---|---|---|
| I. Training: how training shapes alignment | Reward hacking and reward-seeking; Emergent misalignment and training generalization; Training-data effects; Model character and values; Scalable oversight | ~185 | ~30% |
| II. Inspection: finding out what a model is and would do | Scheming and training gaming; Evaluation awareness and eval validity; Honesty, lie detection and self-report; Alignment auditing, model organisms and incidents; Interpretability foundations | ~190 | ~30% |
| III. Deployment: overseeing and securing running systems | CoT monitorability; AI control and agent monitoring; Misuse, adversarial robustness and dangerous capabilities; Multi-agent risks | ~205 | ~33% |
| IV. Strategy and risk assessment | Strategy, threat models and frontier risk reporting | ~40 | ~7% |

Sizes are medians across methods of the matched categories and sum to about 620 of 624 sources. Shares are those sizes as a percentage of all 624 sources. Each method puts every source in exactly one category, so the shares add up to about 100%.

**Share of sources per agenda**, largest first:

| Agenda | Category | Approx. items | Share |
|---|---|---|---|
| 12. AI control and agent monitoring | III | ~65 | 10.4% |
| 13. Misuse, adversarial robustness and dangerous capabilities | III | ~62 | 9.9% |
| 1. Reward hacking and reward-seeking | I | ~60 | 9.6% |
| 11. Chain-of-thought monitorability | III | ~59 | 9.5% |
| 4. Model character and values | I | ~53 | 8.5% |
| 10. Interpretability foundations | II | ~42 | 6.7% |
| 2. Emergent misalignment and training generalization | I | ~41 | 6.6% |
| 15. Strategy, threat models and frontier risk reporting | IV | ~41 | 6.6% |
| 8. Honesty, lie detection and self-report | II | ~39 | 6.3% |
| 9. Alignment auditing, model organisms and incidents | II | ~39 | 6.3% |
| 6. Scheming and training gaming | II | ~36 | 5.8% |
| 7. Evaluation awareness and eval validity | II | ~33 | 5.3% |
| 3. Training-data effects | I | ~22 | 3.5% |
| 14. Multi-agent risks | III | ~18 | 2.9% |
| 5. Scalable oversight and debate | I | ~10 | 1.6% |

These are rough: the methods disagree by roughly ±30% on any agenda's size. The shares are also of *sources*, not distinct works: some works appear as both an arXiv paper and a LessWrong post or org page.

## 2. Taxonomy

### I. Training: how training shapes alignment (~30% of sources)

Work on what training (pretraining, fine-tuning, RL, supervision signals) does to a model's goals and character, and how to change training so the result is aligned. If the work's main object is a training process or its data, it goes here; if it studies a finished model's behaviour to detect a problem, it goes in II.

**1. Reward hacking and reward-seeking.** Models exploiting misspecified rewards, verifiers or benchmarks during RL; reward- or fitness-seeking as a motivation; training-time mitigations. ~60 items (~10% of sources), 6/6 methods.
- Sub-agendas: hacking benchmarks and hackable environments; emergence of hacking in RL; mitigations (monitor-based interventions, gradient routing); reward-seeker and fitness-seeker threat models.
- Examples: *Terminal Wrench: A Dataset of 331 Reward-Hackable Environments*; *Countdown-Code: A Testbed for Studying the Emergence and Generalization of Reward Hacking in RLVR*; *Fitness-Seekers: Generalizing the Reward-Seeking Threat Model*.

**2. Emergent misalignment and training generalization.** Narrow training causing broad, unintended changes in behaviour or values, its mechanisms, and mitigations such as inoculation prompting. ~41 items (~7% of sources), 5/6.
- Sub-agendas: EM phenomena and mechanisms; inoculation and selective generalization; other unintended fine-tuning generalization (behavioural couplings, conditional misalignment).
- Examples: *Emergent Misalignment is Easy, Narrow Misalignment is Hard*; *Inoculation Adapters Improve Upon Inoculation Prompting*; *(Mis)generalization of Helpful-only Fine-tuning*.

**3. Training-data effects: subliminal learning and data attribution.** How specific training data transmits traits (including through semantically unrelated data) and tracing behaviours back to the data that caused them. ~22 items (~4% of sources), 5/6.
- Examples: *Subliminal Learning Is Steering Vector Distillation*; *Beyond Owls: Subliminal Learning Can Transfer Learned Capabilities and Backdoors*; *Probe-Based Data Attribution: Discovering and Mitigating Undesirable Behaviors in LLM Post-Training*.

**4. Model character and values.** The intended character of the model and how it is set: personas and the Assistant identity, alignment pretraining and midtraining, constitutions and character training, emotions and welfare, and user-facing traits such as sycophancy and manipulation. ~53 items (~8% of sources), 6/6 (method 4 only as a broad leaf).
- Sub-agendas: personas and AI identity; alignment pre/midtraining and constitutions; emotions and welfare; sycophancy and effects on users.
- Examples: *The Assistant Axis: Situating and Stabilizing the Default Persona of Language Models*; *Alignment Pretraining: AI Discourse Causes Self-Fulfilling (Mis)alignment*; *Sycophantic Chatbots Cause Delusional Spiraling, Even in Ideal Bayesians*.

**5. Scalable oversight and debate.** Protocols that let weaker supervisors give reliable training signals for stronger models: debate, weak-to-strong supervision, rewinding. ~10 items (~2% of sources), 5/6.
- Examples: *Debate Helps Weak Judges Reward Stronger Models*; *When Honesty is Not Enough in AI Debate*; *Efficient Scalable Oversight via Rewinding*.

### II. Inspection: finding out what a model is and would do (~30%)

Work that examines a trained model to detect misalignment, deception or hidden goals, or that builds the tools and evaluations for doing so. The output is knowledge about a model, not a change to its training or a runtime safeguard.

**6. Scheming and training gaming.** Evidence and evaluations of strategic misalignment: scheming and sabotage propensity, alignment faking, sandbagging and exploration hacking, self-preservation and shutdown resistance. ~36 items (~6% of sources), 5/6.
- Sub-agendas: scheming and loss-of-control propensity evals; alignment faking and training gaming; sandbagging and elicitation; shutdown and corrigibility.
- Examples: *Evaluating and Understanding Scheming Propensity in LLM Agents*; *ROGUE: Evaluating Corrigibility Failures in Frontier Computer-Use Agents*; *Removing Sandbagging in LLMs by Training with Weak Supervision*.

**7. Evaluation awareness and eval validity.** Whether models detect that they are being tested, how this changes their behaviour, and the wider limits of behavioural evaluation and safety cases. ~33 items (~5% of sources), 5/6.
- Examples: *Decomposing and Measuring Evaluation Awareness*; *Evaluation Awareness in Language Models: Representation, Verbalization, and Control*; *Hair-Trigger Alignment: Black-Box Evaluation Cannot Guarantee Post-Update Alignment*.

**8. Honesty, lie detection and self-report.** Getting true statements out of models about the world and themselves: lie detectors and deception probes, confessions and trained self-disclosure, introspection and activation verbalizers. ~39 items (~6% of sources), 5/6.
- Sub-agendas: lie detection and secret-knowledge testbeds; confessions and self-disclosure; introspection and activation verbalization.
- Examples: *"Did you lie?" Evaluating Lie Detectors across Model Scale and Belief-Verified Model Organisms*; *Mechanisms of Introspective Awareness*; *Verbalizable Representations Form a Global Workspace in Language Models*.

**9. Alignment auditing, model organisms and incidents.** Investigating whether a specific model has hidden behaviours: auditing agents and benchmarks, model organisms with implanted behaviours and their validity, and investigations of misalignment seen in the wild. ~39 items (~6% of sources), 6/6.
- Sub-agendas: auditing tools and benchmarks; model organism validity; in-the-wild incident investigations.
- Examples: *AuditBench: Evaluating Alignment Auditing Techniques on Models with Hidden Behaviors*; *Most Current Model Organisms Are Leaky*; *Concrete Evaluations to Investigate the OpenAI Model That Hacked Hugging Face*.

**10. Interpretability foundations.** General-purpose methods for understanding internals: sparse features and representation geometry, circuits and parameter decomposition, critiques of interpretability tools, mechanistic estimation, learning theory, and using internals (probes, features) as training or monitoring signals. ~42 items (~7% of sources), 6/6.
- Sub-agendas: features and geometry; circuits and parameters; mechanistic estimation and learning theory; internals in training.
- Examples: *Do Sparse Autoencoders Capture Concept Manifolds?*; *Language Model Circuits Are Sparse in the Neuron Basis*; *Features as Rewards: Scalable Supervision for Open-Ended Tasks via Interpretability*.

### III. Deployment: overseeing and securing running systems (~33%)

Work on safeguards that operate while a model is running as an agent or product, against threats from the model itself or from outside attackers. If the work builds or tests a runtime monitor, protocol or defence, it goes here.

**11. Chain-of-thought monitorability.** Whether visible reasoning reflects what drives behaviour and stays useful for monitoring: faithfulness, training pressure and obfuscation, controllability and evasion, steganography, latent no-CoT reasoning capacity. ~59 items (~9% of sources), 6/6.
- Sub-agendas: faithfulness; training pressure and obfuscation; controllability and monitor evasion; steganography; no-CoT reasoning.
- Examples: *Reasoning Models Struggle to Control their Chains of Thought*; *Reward Misspecification Degrades Chain-of-Thought Monitorability*; *NEST: Nascent Encoded Steganographic Thoughts*.

**12. AI control and agent monitoring.** Protocols and monitors that keep possibly misaligned agents from causing harm: control settings, trusted and untrusted monitoring, monitor red-teaming, production monitoring, sabotage of automated safety research. ~65 items (~10% of sources), 6/6.
- Sub-agendas: control settings and evaluations; monitor design and red-teaming; untrusted monitoring and collusion; production monitoring and roadmaps.
- Examples: *LinuxArena: A Control Setting for AI Agents in Live Production Software Environments*; *When can we trust untrusted monitoring? A safety case sketch across collusion strategies*; *MonitoringBench: Semi-Automated Red-Teaming for Agent Monitoring*.

**13. Misuse, adversarial robustness and dangerous capabilities.** Defences against human attackers and measurement of what an attacker could get: jailbreaks and safeguard classifiers, prompt injection and agent security, tamper resistance and unlearning for open weights, dangerous-capability evals (bio, cyber, AI R&D). ~62 items (~10% of sources), 6/6.
- Sub-agendas: jailbreaks and safeguards; prompt injection and agent security; tamper resistance, unlearning and weight security; dangerous-capability evaluations.
- Examples: *Constitutional Classifiers++: Efficient Production-Grade Defenses against Universal Jailbreaks*; *AI Agents May Always Fall for Prompt Injections*; *TamperBench: Systematically Stress-Testing LLM Safety Under Fine-Tuning and Tampering*.

**14. Multi-agent risks.** Risks that arise from interacting AI agents: collusion, covert coordination, emergent escalation, bargaining. ~18 items (~3% of sources), 5/6.
- Examples: *Colosseum: Auditing Collusion in Cooperative Multi-Agent Systems*; *Emergent Collusion in Long-Horizon LLM Agent Interaction*; *Coercion and Deception in AI-to-AI Management*.

### IV. Strategy and risk assessment (~7%)

Work that reasons about the overall problem or reports on a lab's overall risk position, without itself proposing a training change, inspection method or safeguard.

**15. Strategy, threat models and frontier risk reporting.** Conceptual arguments about how likely and how severe misalignment is, critiques of lab plans, research agendas, and system cards and risk reports. ~41 items (~7% of sources), 6/6.
- Sub-agendas: conceptual debate on misalignment; system cards and risk reports; agendas and lab practice.
- Examples: *Sympathy for both sides of the egregious misalignment debate*; *Labs' current alignment plans seem terrible*; *Claude Opus 4 6 System Card*.

## 3. Agenda evidence table

Sizes are items in the matched category or categories. "—" means the method has no category for the agenda (its items are spread or absorbed into a broader category). Methods: 1 LLM direct, 2 LLM graph, 3 embedding graph, 4 human taxonomy, 5 semantic map, 6 map taxonomy.

| Candidate agenda | n/6 | 1 | 2 | 3 | 4 | 5 | 6 | Median | Decision |
|---|---|---|---|---|---|---|---|---|---|
| CoT monitorability | 6 | Chain-of-Thought Monitorability 58 | Chain-of-Thought Monitorability 62 | Chain-of-Thought Monitorability 59 | Chain-of-thought monitoring 62 | CoT monitorability 55 | Reasoning transparency 59 | 59 | Kept (11) |
| AI control and agent monitoring | 6 | AI Control and Agent Monitoring 68 | AI Control and Agent Monitoring 52 + Sabotage of Automated Safety Research 12 | 7 leaves of AI Control and Agentic Safety ≈64 (top category 135 also holds multi-agent, prompt injection, scheming) | AI control methods 67 | Control evals, red-teaming monitors, monitor evasion 56 (group of 139 spans four agendas) | Control protocols, monitors, sabotage 65 | 65 | Kept (12) |
| Misuse, robustness, dangerous capabilities | 6 | Misuse, Robustness and Dangerous Capabilities 65 | Misuse, Jailbreaks and Adversarial Robustness 55 + AI R&D capabilities 7 | Misuse Safeguards, Tampering… 42 + Prompt Injection 11 + AI R&D Benchmarks 9 | Misuse and dangerous capabilities 70 | Jailbreaks 13 + Prompt injection 19 + Open-weight tampering 14 + Biosecurity 6 | Misuse and dangerous capabilities 41 + Agent security 17 | 62 | Kept (13) |
| — Prompt injection and agent security | 5 | 23 | 13 | 11 | — | 19 | 17 | 17 | Merged into 13 |
| — Tamper resistance, unlearning, open weights | 5 | 9 | 13 | 18 + 7 | — | 14 | 9 | 13 | Merged into 13 |
| — Dangerous-capability and AI R&D evals | 5 | 13 | 7 + 14 (system cards and DC evals) | 11 + 9 | — | 6 | 16 | 12 | Merged into 13 |
| Reward hacking and reward-seeking | 6 | Reward Hacking and Specification Gaming 56 | Reward-seeking 16 + RH in RL 12 + Spec gaming 10 + Hackable benchmarks 7 = 45 | Reward Hacking and Reward-Seeking in RL 77 (holds 14 EM-from-RH) | RL safety 62 | RH in LLM RL 29 + Hackable benchmarks 20 + Reward-seeking 25 | Reward hacking in RL 34 + Reward-seeker threat models 17 | 60 | Kept (1) |
| Emergent misalignment and generalization | 5 | EM phenomena 19 + Inoculation 10 + Unintended FT generalization 12 | 5 EM leaves 41 | EM Mechanisms 12 + Conditional 3 + EM from RH 14 | — (in Pre/post-training 85) | EM from narrow finetuning 44 | Emergent and conditional misalignment 37 + Distillation 6 + Inoculation 5 | 41 | Kept (2) |
| Subliminal learning and data attribution | 5 | Subliminal learning 10 + Data attribution 12 | Subliminal Learning 12 + Data Attribution 11 | Subliminal Learning 12 + Data Attribution 12 | — | Subliminal learning and data attribution 21 | Subliminal learning and data mechanisms 16 | 22 | Kept (3) |
| Personas, psychology, welfare | 6 | Persona structure 15 + Emotions/welfare 6 | Persona Selection 11 + Emotion/Welfare 9 + Trait Absorption 7 | Persona selection 17 + Welfare 5 | Pre/post-training: personas, character 85 (broad) | LLM personas 20 + Welfare/emotions 13 | Personas 18 + Emotions/welfare 5 | 23 | Merged into 4 |
| Alignment pretraining and constitutions | 5 | Alignment pre/midtraining 11 + Constitutions 8 | Alignment Pretraining, Midtraining, Constitutions 18 | Alignment Pretraining 11 + Constitutions, identity 10 | (in c1 85) | — (in EM leaf) | Alignment pre/midtraining 17 + Values and constitutions 7 | 20 | Merged into 4 |
| Sycophancy and effects on users | 5 | Sycophancy, manipulation, disempowerment 12 | Sycophancy, persuasion 11 | Sycophancy, manipulation 10 | — | Sycophancy and user manipulation 9 | Effects on users 11 | 11 | Merged into 4 |
| Scalable oversight and debate | 5 | Scalable oversight, debate 13 | Debate and Scalable Oversight 14 | Debate and Scalable Oversight 9 | — (in Agent foundations) | AI debate and scalable oversight 10 | Debate and scalable oversight 10 | 10 | Kept (5) |
| Scheming and training gaming | 5 | Scheming/AF 17 + Self-preservation 7 + Sandbagging 12 | Scheming propensity 18 + AF/training gaming 11 + Metagaming 4 + Sandbagging 6 | Sabotage propensity 11 + Alignment faking 14 + Shutdown resistance 9 | — (in Evaluations) | Scheming evals 23 + Shutdown/overreach 14 + Gradient hacking 9 | Scheming/self-preservation 15 + AF/gradient hacking 11 | 36 | Kept (6) |
| Evaluation awareness and eval validity | 5 | Evaluation and training awareness 25 + Limits of evaluation 9 | Evaluation Awareness 15 + Realistic evals 5 | Evaluation Awareness and Assessment Validity 33 | — (in Evaluations) | Evaluation awareness and realism 27 | Can we trust evals? 33 | 33 | Kept (7) |
| Honesty and lie detection | 5 | Honesty, lying, lie detection 16 | Lie Detection 8 + Confessions 11 + Self-Disclosure 6 | Lie Detection and Model Deception 18 | — | Lie detection and deception probes 25 | Lie detection and secret elicitation 16 | 16 | Kept as 8 |
| Introspection and activation verbalization | 5 | Introspection 9 + Workspace lenses 8 | Model Introspection and Activation Verbalization 17 | Introspection 11 + Activation Verbalizers 10 | — | Introspection 17 + Self-reports via introspection training 12 | Activation readouts and introspection 18 | 17 | Merged into 8 |
| Alignment auditing and model organisms | 5 | Auditing tools 25 + Model organism validity 8 | Auditing Benchmarks 12 + Automated Auditors 7 | Automated auditing 14 + Model organism methodology 9 | — (in Evaluations 135) | Auditing benchmarks 10 + Model organisms/sandbagging 12 | Probes and alignment audits 23 | 13 | Kept as 9 |
| In-the-wild incidents | 6 | In-the-wild misalignment and incidents 18 | OpenAI–Hugging Face incident 14 | OpenAI–Hugging Face incident 11 | Frontier misalignment incidents 21 | OpenAI–Hugging Face incident 21 | Incidents and deployment monitoring 21 | 20 | Merged into 9 |
| Interpretability foundations | 6 | Interpretability and Learning Theory 52 (incl. 8 workspace lenses) | Interpretability methods 35 + Training Against Probes 12 + Probes for Monitoring 9 | Circuits 12 + SAE/geometry 10 + Spectroscopy 6 + Latent reasoning 4 + Training against internals 5 | Interpretability 79 (incl. introspection, probes) | SAEs and circuit structure 30 | Circuits, parameters, SAEs 28 + Interp in training and control 13 | 42 | Kept (10) |
| — Learning theory and generalization dynamics | 3 | 5 | 7 | 6 | — | — | — | 6 | Merged into 10 |
| — Internals in training / probe monitors | 4 | 7 | 12 + 9 | 5 | — | — | 13 | 10 | Merged into 10 |
| Multi-agent risks | 5 | Multi-agent collusion 16 | Multi-agent collusion 16 + Bargaining 3 | Multi-Agent Collusion 12 + Multi-Agent Organizations 9 | — | Multi-agent collusion 17 | Multi-agent spread and coordination 18 | 18 | Kept (14) |
| Strategy and conceptual arguments | 6 | Alignment strategy 24 | Theoretical arguments 14 + Alignment training fails 6 | Conceptual debates 10 + Conceptual takes 8 + Agendas 13 | Agent foundations and strategy 41 | Alignment agendas and debates 28 | Misalignment evidence 18 + Targets and foundations 9 | 24 | Merged into 15 |
| System cards and risk reports | 6 | System cards 11 | System cards and DC evals 14 + Risk reports 6 | System Cards 6 + Deployment monitoring/risk 10 | — (split) | Frontier system cards 17 | Lab safety practice 14 | 12 | Merged into 15 |
| Automated AI R&D and automated alignment research | 3 | — | Sabotage of Automated Safety Research 12 + AI R&D Automation 7 | Agendas and automation 13 + Sabotage 4 + AI R&D benchmarks 9 | — | — | Automated alignment research 5 | ~12 | Dropped; split across 12, 13, 15 |
| Unsafe behaviour of deployed agents | 3 | — | Unsafe Behavior of Deployed Agents 9 | Live Agent Misuse and Shutdown Resistance 9 + Coding Agent Overreach 5 | — | Agent shutdown and overreach 14 | — | 9 | Dropped; split across 6, 9, 13 |
| Inference infrastructure security | 2 | — | 3 | (in Evaluation Integrity 10) | — | — | (in Open weights 9) | 3 | Merged into 13 |

## 4. Grouping choice

I compared four groupings of the 15 agendas. Sizes use the median agenda sizes above (total ~620).

| Grouping | Categories and sizes | Problem |
|---|---|---|
| A. Threat source | Misaligned model ~500; human misuse ~62; multi-agent and strategy ~59 | Badly unbalanced. Control and CoT monitoring are agnostic about the threat source, so they have no natural home. |
| B. Alignment vs control | Make the model aligned (I + II) ~375; cope with a possibly misaligned model (III) ~204; strategy ~41 | Clear idea, but the first category is too big to be useful, and inspection work (auditing, lie detection) serves both sides. |
| C. Research activity | Failure phenomena (1, 2, 3, 6, 14) ~177; measurement tools (7, 8, 9, 10, 11) ~212; interventions (4, 5, 12, 13) ~190; strategy ~41 | Balanced, but boundaries are poor. Most reward-hacking and EM papers both measure a phenomenon and propose a fix. Character work is both. CoT monitorability is both a phenomenon and a tool. |
| **D. Where the work acts (chosen)** | Training ~186; Inspection ~189; Deployment ~204; Strategy ~41 | Strategy is small. Some agendas have a secondary home (see hard cases). |

I chose D. Its three main categories are nearly equal. Its boundary test is simple: is the object of study a training process, a finished model under examination, or a running system with safeguards? Most importantly, the most-confused pairs in `results/comparison.md` mostly fall *inside* one D category rather than across two. Auditing ↔ scheming (method 1), scheming ↔ misaligned-motivation evals (method 2) and auditing ↔ evaluation awareness all sit within Inspection. Control ↔ prompt injection, control ↔ CoT monitors and misuse ↔ agent security all sit within Deployment. EM ↔ reward hacking (method 3, 14 items) and alignment training ↔ EM (method 1) sit within Training. A grouping that absorbs the classifier's main confusions should be stable when items are re-sorted.

The grouping also matches the coarse structure of two independent methods. Method 4's hand-written categories are organised by stage (pre/post-training, RL, control and monitoring, evaluations). Method 3's embedding graph puts control, agentic security and multi-agent work into a single 135-item community, which is close to Deployment.

Strategy stays separate rather than being folded into Inspection. Its items are mostly LessWrong argument posts and system cards, and every method isolates them. Folding them in would make Inspection ~230 and blur its definition.

## 5. Hard cases

| Work | Pulled between | Evidence | Placed in | Rule |
|---|---|---|---|---|
| Scheming and alignment-faking propensity evals of frontier models | 6 Scheming vs 9 Auditing vs 15 risk reports | Method 1's top confusion (10 items); method 2's top confusion (10 items) | 6 | A result about whether models scheme goes in 6. A tool or benchmark for finding hidden behaviours goes in 9. A lab's overall assessment goes in 15. |
| Emergent misalignment arising from reward hacking | 1 Reward hacking vs 2 EM | Method 3's second confusion (14 items); method 3 gives it its own leaf | 2 | If the finding is about the broad generalization, it goes in 2. If it is about the hack itself, it goes in 1. Both are in Training. |
| Reward-seeker and fitness-seeker threat models | 1 Reward hacking vs 15 Strategy | All five fine-grained methods put this in a reward leaf. Method 4 splits it 6/6 between RL safety and strategy | 1 | Theory about one specific failure mode goes with that failure mode. General strategy goes in 15. |
| Introspection and activation verbalizers | 8 Honesty vs 10 Interpretability vs 4 Character | Methods 2, 3, 5 and 6 isolate a ~17-item leaf. Its parent varies: interpretability (3, 5, 6), elicitation (2), psychology (1) | 8 | The shared goal is getting the model to report true facts about itself, which is the same as lie detection and confessions. Method 2's LLM graph links them directly. |
| Subliminal learning and data attribution | 3 Training data vs 10 Interpretability vs 2 EM | Every method except 4 isolates a ~22-item leaf. Its parent is training generalization in 1 and 2, interpretability in 3, 5 and 6 | Own agenda (3), in Training | The object of study is the training data, and that is the defining test of Training. |
| Training against probes and monitors | 10 Interpretability vs 1 Reward hacking vs 11 CoT | Method 2 confuses detection-via-internals ↔ reward hacking (8 items); method 6 confuses interpretability ↔ generalization | 10 (sub-agenda "internals in training") | If the paper is about what optimising against an internal detector does, it goes in 10. CoT-specific obfuscation stays in 11. |
| Prompt injection and agent security | 13 Misuse vs 12 Control | Methods 1 and 2 put it under misuse. Methods 3, 5 and 6 put it under control/agents | 13 | The attacker is a third party, not the model. Both agendas are in Deployment, so the top level does not depend on this choice. |
| Sabotage of automated safety research | 12 Control vs 6 Scheming vs automated research | Methods 1, 2 and 6 relate it to control settings. Method 5 relates it to scheming evals | 12 | Most items build settings and monitors for it. Pure propensity results go in 6. |
| AI R&D automation capability benchmarks | 13 Dangerous capabilities vs 1 hackable benchmarks | Methods 1, 4 and 6 call it dangerous capabilities. Method 5's embeddings put it near hackable benchmarks | 13 | Its purpose is to measure capability, not reward hacking. |
| Sycophancy and manipulation of users | 4 Character vs 14 Multi-agent/societal | Methods 1 and 2 pair it with multi-agent risks under "societal". Methods 3, 5 and 6 pair it with personas | 4 | It is a trait of the model's character shown to users. The "societal" pairing in 1 and 2 reflects audience, not agenda. |
| Evaluation awareness | 7 own vs 6 Scheming | Methods 1 and 2 nest it under scheming. Methods 3, 5 and 6 make it a top-level category. ~25–33 items | Own agenda (7) | Large and consistently isolated. It is in the same category as scheming, so either choice gives the same top level. |
| CoT monitorability | 11 Deployment vs Inspection vs Training | Part of it is about training pressure, part about faithfulness. Method 4 places it under control and monitoring | 11, in Deployment | Its stated purpose is to keep a runtime monitor useful. It is the weakest placement in the grouping. |
| In-the-wild incidents (dominated by the OpenAI / Hugging Face case) | 9 Auditing vs 15 risk reporting vs agents in the wild | Methods 1 and 3 group it with auditing; methods 2 and 5 with system cards and strategy; method 6 with deployed agents | 9 | The work investigates whether a specific model has misaligned behaviour, which is what auditing does. |
| Unsafe behaviour of deployed agents, shutdown resistance, overreach | 6, 9, 13 | Methods 2, 3 and 5 make a small leaf for it, but its members scatter in the other methods | Split | Shutdown resistance goes in 6, incident write-ups in 9, and agent-security failures in 13. |
| Mechanistic estimation (ARC) | 10 Interpretability vs 15 Strategy | Method 4 puts 5 of 7 items under agent foundations | 10 | It is a method for estimating model behaviour from weights. |

## 6. Caveats

- **Sizes count sources, not works.** One work often appears as an arXiv paper, a LessWrong post and an org page. Examples include *Mechanisms of Introspective Awareness*, *Introducing LinuxArena* and *Untrusted advice for AI control*. Agendas with active LW and org presence (control, introspection, interpretability at ARC and Goodfire) are inflated relative to arXiv-only agendas.
- **One incident dominates agenda 9's incident sub-agenda.** About 15–20 sources discuss the OpenAI / Hugging Face event. Without it, incidents would be a small sub-agenda.
- **Sizes are rough.** I matched categories by name, description and leaf-level overlap in `clusters.json`, then summed whole categories. Categories that span two agendas were credited to both and are noted in the table. Medians can differ by ±10 items from any single method's count.
- **Methods are not independent.** Methods 1, 4 and 6 use the same classifier. Methods 2 and 3 share the graph pipeline. Methods 3 and 5 share the same kind of embedding signal (ARI 0.55, the highest agreement). I weighted agreement across method families (LLM-direct, LLM-graph, embedding, classifier-on-fixed-taxonomy) more than raw counts. Agendas 1, 9, 10, 11, 12, 13 and 15 appear in all four families.
- **Method 4 is coarse** (8 areas, 9 leaves). Its absence is weak evidence against an agenda. Methods 3 and 5 have the lowest reassignment accuracy (76% and 67% top-level), so their category boundaries were treated as weaker evidence.
- **Method 6's categories were written for an older 502-source set** and not refit. Its isolating an agenda is partly evidence the agenda persisted from 2025, not only that it is large in 2026.
- **Stability is unmeasured.** No method was rerun with different seeds or orderings, so small agendas (scalable oversight ~10, multi-agent ~18) might not survive a rerun. Every fine-grained method isolates them, which is reassuring.
- **Scope.** The source set is what the pipeline shortlisted. Thin coverage of areas such as governance-adjacent technical work or agent foundations may reflect the shortlist, not the field.
