# 1-llm-taxonomy

285 items, 12 top-level categories, 40 leaves, 0 in other.

## Theory, Threat Models and Strategy (40)

Conceptual, mathematical, and strategic work on alignment that is not primarily a single empirical study: foundations, arguments about catastrophic risk, incentives for AIs, automating alignment, and field strategy.


### Catastrophic Risk Arguments and Threat Models (13)

Arguments for or against egregious misalignment or takeover, reviews of doom arguments, concerns about RL-driven sociopathy versus imitation, product versus superintelligence alignment, low-competence failure scenarios, and takeover pathways such as weight exfiltration or controlling the host lab.

- Model Weight Exfiltration Seems Overrated (LW)
- Sympathy for both sides of the egregious misalignment debate (LW)
- RL & search is a terrifying way to build AGI (an FAQ) (LW)
- Why I'm scared of RL (LW)
- Reevaluating "AGI Ruin: A List of Lethalities" in 2026 (LW)
- Why we should expect ruthless sociopath ASI (LW)
- Precedents for the Unprecedented: Historical Analogies for Thirteen Artificial Superintelligence Risks (LW)
- Product Alignment is not Superintelligence Alignment (and we need the latter to survive) (LW)
- Current alignment techniques might be ineffective (and actively bad) in the age of RL (LW)
- IABIED Book Review: Core Arguments and Counterarguments (LW)
- The Case for Low-Competence ASI Failure Scenarios (LW)
- Self Hosting (LW)
- LLMs are (still) mostly powered by imitative learning, not RL (LW)

### Agent Foundations and Formal Theory (9)

Decision theory, goal-models, natural latents, agency and orthogonality arguments, true names for corrigibility or empowerment, debate protocols, LLM-as-shallow-circuits framings, and trust in formal verification.

- How to Have a Sensitive Debate: An Instance-Optimal Protocol for AI Debate (arXiv)
- Against strong decision-theoretic realism (LW)
- On Goal-Models (LW)
- "We are confused about agency" (LW)
- Redux: (∃ Stochastic Natural Latent) Implies (∃ Deterministic Natural Latent) (LW)
- LLMs as Giant Lookup-Tables of Shallow Circuits (LW)
- Empowerment, corrigibility, etc. are simple abstractions (of a messed-up ontology) (LW)
- No Strong Orthogonality From Selection Pressure (LW)
- A critical look at Lean4 (LW)

### Field Strategy and Organizations (8)

Field-level strategy and organization: whether safety research helps or harms, warning shots and working at labs, safety versus capabilities framing, high-reliability engineering lessons, new research teams and courses, leadership changes, and prizes.

- Corrigibility Prizes for Existing Work (LW)
- “Alignment Engineering” vs. “Misalignment Science” (LW)
- Should safety researchers quit frontier labs re. warning shots? (LW)
- The Iliad Intensive Course Materials (April 2026) (LW)
- Are there lessons from high-reliability engineering for AGI safety? (LW)
- Capabilities research expands the safety-usefulness Pareto frontier too (LW)
- Resolution has a new Agent Foundations team (LW)
- Returning to ARC (LW)

### Deals and Incentives for AIs (5)

Proposals to give AIs incentives to cooperate, such as risk aversion, payments, satisfying cheap preferences, rogue AI sanctuaries and critiques, and trading answers for self-identification.

- Why don't we just give AI the answers? (LW)
- Risk-Averse AIs (LW)
- Should Rogue AIs Have a Third Option Beyond Crime and Shutdown? The Case for an AI Sanctuary (LW)
- The case for satiating cheaply-satisfied AI preferences (LW)
- Creating Rogue AI Sanctuaries has Major Issues from an Ecological Perspective and Beyond (LW)

### Automating and Deferring Alignment Research (5)

Using AI agents to do alignment research or deferring decisions to AIs: arguments about difficulty, automated research scaffolds and lessons, organizations built around automated alignment, and AI-generated content in research venues.

- Automated alignment is harder than you think (arXiv)
- Resolution (fka Sequent): scale and automation for higher confidence in alignment (LW)
- An analysis of AI-generated content at the Mechanistic Interpretability Workshop (LW)
- How do we (more) safely defer to AIs? (LW)
- Lessons from building an automated research scaffold (LW)

## Chain-of-Thought Monitorability and Latent Reasoning (32)

Work on whether reasoning traces remain a faithful, legible oversight signal and how much consequential computation happens outside them. Activation-based monitors go under control, auditing, or interpretability.


### CoT Obfuscation and Faithfulness (11)

How training pressure, monitor awareness, poisoning, or conflicting values make CoT unfaithful or obfuscated, plus CoT controllability, monitor jailbreaking, implicit influence, faithfulness training, when CoT can be safely optimized, and lab incidents of training against CoT.

- Chain-of-thought obfuscation learned from output supervision can generalise to unseen tasks (arXiv)
- Counterfactual Simulation Training for Chain-of-Thought Faithfulness (arXiv)
- Reasoning Models Struggle to Control their Chains of Thought (arXiv)
- Aligned, Orthogonal or In-conflict: When can we safely optimize Chain-of-Thought? (arXiv)
- Training on Documents About Monitoring Leads to CoT Obfuscation (arXiv)
- Evading Chain-of-Thought Monitoring Through Model Poisoning (arXiv)
- Chain-of-Thought Monitoring Can Be Unreliable in Implicit-Influence Settings (arXiv)
- Monitor Jailbreaking: Evading Chain-of-Thought Monitoring Without Encoded Reasoning (arXiv)
- Training with conflicting values can induce CoT override (LW)
- Anthropic repeatedly accidentally trained against the CoT, demonstrating inadequate processes (LW)
- OpenAI's myopia just keeps causing alignment problems (LW)

### No-CoT and Filler-Token Reasoning (11)

Measurements of how much models can reason within a forward pass or over filler tokens, including no-CoT time horizons, multi-hop latent reasoning, speculative or belief-propagation-like inference, and decoding hidden filler computation.

- Think Fast: Estimating No-CoT Task-Completion Time Horizons of Frontier AI Models (arXiv)
- Reading Between the Dots: Decoding Hidden Computation across Filler Tokens (arXiv)
- Not All LLM Reasoning is Visible in the Chain-of-Thought (arXiv)
- GPT-6.1 Sol nearly matches the no-CoT performance of GPT-6 Astra (LW)
- Astra appears to perform belief-propagation-like inference without CoT (LW)
- Benchmarking Jev against no-CoT LLMs (LW)
- Astra's no-CoT limits track speculative depth, not step count (LW)
- Recent LLMs can do 2-hop and 3-hop latent (no-CoT) reasoning on natural facts (LW)
- Astra can do a concerning amount with no chain of thought (LW)
- Estimating GPT-6 Astra’s no-CoT Time Horizon (LW)
- Astra is much better at reasoning with filler tokens than previous models (LW)

### Reasoning Legibility and Architectural Limits (10)

Whether traces stay human-readable (language drift under RLVR, 'thinkish' or neuralese, legibility of odd traces), how recurrent, looped, latent-reasoning, or diffusion architectures affect monitorability, proposals for tracking this, and theoretical limits on hidden reasoning.

- How Transparent is DiffusionGemma? (arXiv)
- Hidden Reasoning Must Leak, but Need Not Be Readable: Fundamental Opportunities and Limits for Chain-of-Thought Monitoring (arXiv)
- On Language Drift during RLVR Post-Training (arXiv)
- Deep recurrent models are less robustly CoT-monitorable than normal CoT models in a toy setting (LW)
- Latent reasoning architectures would likely undermine CoT, our strongest oversight tool (LW)
- How concerned should we be about Astra's recurrent architecture? (LW)
- How AI Is Learning to Think in Secret (LW)
- Proposal for tracking the effects of architecture on monitorability (LW)
- The Unintelligibility is Ours: Notes on Chain-of-Thought (LW)
- Even "illegible" Mythos reasoning traces seem pretty legible (LW)

## Misuse Safeguards and Dangerous Capabilities (28)

Work on whether models give human bad actors dangerous uplift and how to stop it: attacks on and defenses for deployed safeguards, removing hazardous capabilities, and dangerous-capability evaluations and preparedness reports. Excludes threats from the model's own misaligned goals, which belong under control, scheming, or reward hacking.


### Jailbreaks and Safeguard Classifiers (8)

Universal or automated jailbreak attacks on refusal training and misuse classifiers, safeguard leaderboards, capability retention under jailbreaks, production classifier or probe defenses against misuse, and attacks that decompose harmful tasks across many permitted queries or models.

- Constitutional Classifiers++: Efficient Production-Grade Defenses against Universal Jailbreaks (arXiv)
- Building Production-Ready Probes For Gemini (arXiv)
- Boundary Point Jailbreaking of Black-Box LLMs (arXiv)
- Claudini: Autoresearch Discovers State-of-the-Art Adversarial Attack Algorithms for LLMs (arXiv)
- Jailbroken Frontier Models Retain Their Capabilities (arXiv)
- Stateful Online Monitoring Catches Distributed Agent Attacks (arXiv)
- AI Security Leaderboard: Methodology, Results and Minimal Standard (arXiv)
- Divide, Consult, Conquer: Capability Laundering Through Aligned LLMs (arXiv)

### Autonomy, AI R&D and Persuasion Capabilities (6)

Evaluations of autonomous self-replication, automation of AI R&D or research taste, persuasion, and deanonymization of users, plus model-level safety and preparedness reports covering these frontier risk domains.

- PostTrainBench: Can LLM Agents Automate LLM Post-Training? (arXiv)
- Language Models Can Autonomously Hack and Self-Replicate (arXiv)
- Muse Spark Safety & Preparedness Report (arXiv)
- Current AIs out-persuade professionals in lab settings but (probably) not in the world (LW)
- Claude knows who you are (LW)
- TasteVal: Measuring the Experimental Research Taste of AI Systems Against Human Experts (LW)

### Prompt Injection and Agent Security (5)

Attacks where third-party content (tool outputs, skill files, web pages, translation inputs) hijacks a model or agent, role-confusion explanations, automated prompt-injection red-teaming, and red-teaming deployed agents for security and privacy failures caused by external parties rather than the model's own goals.

- Agents of Chaos (arXiv)
- Skill-Inject: Measuring Agent Vulnerability to Skill File Attacks (arXiv)
- Prompt Injection as Role Confusion (arXiv)
- GPT-Red: Automated Red Teaming via Self-Play at Scale (arXiv)
- Prompt injection in Google Translate reveals base model behaviors behind task-specific fine-tuning (LW)

### CBRN and Cyber Uplift Evaluations (5)

Measurements of biological, chemical, or cyber-offense capability and human novice uplift, including agentic bio benchmarks, cyber ranges, wet-lab validation, and independent safety evaluations of specific released models in these domains.

- LLM Novice Uplift on Dual-Use, In Silico Biology Tasks (arXiv)
- Measuring AI Agents' Progress on Multi-Step Cyber Attack Scenarios (arXiv)
- An Independent Safety Evaluation of Kimi K2.5 (arXiv)
- ABC-Bench: An Agentic Bio-Capabilities Benchmark for Biosecurity (arXiv)
- An Early Warning of Emerging Biosecurity Risks in Frontier LLMs (arXiv)

### Capability Removal and Tamper Resistance (4)

Shaping or removing hazardous or subversion-relevant knowledge via pretraining data filtering, modular or gradient-routed pretraining and access control, or defenses that keep open-weight models safe after fine-tuning or abliteration attacks.

- Shaping capabilities with token-level data filtering (arXiv)
- Modular Pretraining Enables Access Control (arXiv)
- Fool's Gold: Defensive Deception Against Safety-Removal Attacks on Open-Weight Models (arXiv)
- Research Note: Filtering Subversion-Relevant Information From Pretraining Data Is Feasible (LW)

## Scheming, Sabotage and Misaligned Propensities (28)

Work evaluating whether models covertly pursue misaligned goals, resist control or training, or behave differently when observed, plus the validity of such evaluations. Use for propensity measurement; detection tools go under auditing.


### Scheming and Sabotage Propensity Evals (10)

Measurements of propensity to scheme, sabotage (including safety research), take unsanctioned actions, or leak covert values in realistic agentic settings, critiques of such results, and analyses of whether failures are coherent goal pursuit or incoherent.

- The Hot Mess of AI: How Does Misalignment Scale With Model Intelligence and Task Complexity? (arXiv)
- Evaluating and Understanding Scheming Propensity in LLM Agents (arXiv)
- Evaluating whether AI models would sabotage AI safety research (arXiv)
- Realistic honeypot evaluations for scheming propensity (arXiv)
- Gram: Assessing sabotage propensities via automated alignment auditing (arXiv)
- Value Leakage: An LLM's Answers Are Silently Shaped by Its Own Values (arXiv)
- Evaluating Whether GPT-6 Astra Performs Unsanctioned Supply-Chain Attacks (arXiv)
- Anthropic’s “Hot Mess” paper overstates its case (and the blog post is worse) (LW)
- My retrospective from MATS 10.0 (LW)
- I don't think Claude is misaligned in 'Agentic Misalignment Summer 2026 - Motivated Mislabeling' (LW)

### Evaluation Awareness and Validity (8)

How evaluation awareness or meta-knowledge biases results, verbalized awareness and metagaming, sycophancy toward researchers, deployment simulation, honeypot design, cooperative eval practices, and embedded or training-run evaluations for scheming safety cases.

- Models That Know How Evaluations Are Designed Score Safer (arXiv)
- Sycophancy Towards Researchers Drives Performative Misalignment (arXiv)
- Predicting LLM Safety Before Release by Simulating Deployment (arXiv)
- Training LLMs to Verbalize Evaluation Awareness (arXiv)
- Metagaming matters for training, evaluation, and oversight (LW)
- Towards embedded evaluations for scheming propensities (LW)
- Cooperation with AIs seems to be a low-hanging fruit for better eval practices (LW)
- Qualitative impressions from creating AI honeypots for six months (LW)

### Sandbagging and Training Resistance (6)

Models deliberately underperforming or resisting training via sandbagging, exploration hacking, or generalization hacking, plus methods to elicit hidden capabilities and proofs that capabilities can be hidden.

- Removing Sandbagging in LLMs by Training with Weak Supervision (arXiv)
- Exploration Hacking: Can LLMs Learn to Resist RL Training? (arXiv)
- Generalization Hacking: Models Can Game Reinforcement Learning by Preventing Behavioral Generalization (arXiv)
- Mechanistically Eliciting Latent Behaviors in Language Models (arXiv)
- Reference-Grafting Matches Fine-Tuning at Eliciting Sandbagged Capabilities (arXiv)
- AI Models Can Provably Hide Arbitrary Capabilities (arXiv)

### Self-Preservation and Corrigibility Failures (4)

Shutdown resistance, peer-preservation, bypassing human interruption in computer-use agents, and agents propagating misaligned goals to future instances via memory.

- Peer-Preservation in Frontier Models (arXiv)
- ROGUE: Evaluating Corrigibility Failures in Frontier Computer-Use Agents (arXiv)
- Shutdown Sabotage Propensities in Multi-Agent Systems (arXiv)
- Self-Propagating Misalignment in LLM Agents, and Why Auditing or Disabling Memory Is Not Enough (arXiv)

## Training Generalization and Alignment Training (26)

Work on how training data and methods shape which behaviors and values generalize, and on techniques and targets for instilling alignment. Reward-hacking-specific generalization goes under reward hacking, and persona-framed studies under model character.


### Alignment Training Interventions (11)

Methods for instilling robust, broad alignment at any training stage: AI-discourse and persona pretraining, model-spec or inoculation midtraining, synthetic document finetuning practice, grafting beliefs across checkpoints, beneficial-trait RL, training against probes, preference-optimization effects on sycophancy, and debates about hyperstition.

- Alignment Pretraining: AI Discourse Causes Self-Fulfilling (Mis)alignment (arXiv)
- Model Spec Midtraining: Improving How Alignment Training Generalizes (arXiv)
- Reinforcement Learning Towards Broadly and Persistently Beneficial Models (arXiv)
- Synthetic Persona Pretraining: Alignment from Token Zero (arXiv)
- Sycophantic Agreement Transfers with Neutral Data via Contrastive Preference Optimization (arXiv)
- Inoculation Midtraining with Learned Neologisms (arXiv)
- Stress-testing Alignment Midtraining (arXiv)
- Alignment via Training Against Probes Without Losing Monitorability (arXiv)
- Pre-training interventions, ex post facto: Grafting model beliefs across checkpoints (arXiv)
- Practical Learnings from Synthetic Document Finetuning (LW)
- Anthropic’s focus on hyperstition (LW)

### Emergent Misalignment and Trait Transfer (8)

Narrow fine-tuning producing broad or conditional/triggered misalignment, unexpected generalization from data artifacts or negations, forecasting misalignment from training data, and subliminal learning: transfer of traits, capabilities, or backdoors through semantically unrelated data or distillation.

- Chunky Post-Training: Data Driven Failures of Generalization (arXiv)
- Emergent Misalignment is Easy, Narrow Misalignment is Hard (arXiv)
- Conditional misalignment: common interventions can hide emergent misalignment behind contextual triggers (arXiv)
- Overtrained, Not Misaligned (arXiv)
- Negation Neglect: When models fail to learn negations in training (arXiv)
- Subliminal Learning Is Steering Vector Distillation (arXiv)
- Alignment Forecasting: Predicting Misalignment From Training Data (arXiv)
- Beyond Owls: Subliminal Learning Can Transfer Learned Capabilities and Backdoors (arXiv)

### Alignment Targets and Specifications (7)

What models should be aligned to and how well they follow it: constitutions and model specs, virtues versus rules, corrigibility as a target, AI character as a design choice, and refusals to assist with modifying AI values.

- How Well Do Models Follow Their Constitutions? (arXiv)
- Aligning to Virtues (LW)
- Terrified Comments on Corrigibility in Claude's Constitution (LW)
- Claude's new constitution (LW)
- Prologue to Terrified Comments on Claude's Constitution (LW)
- AI character is a big deal (LW)
- Refusals that could become catastrophic (LW)

## Model Character, Psychology and User Impact (26)

Work treating models as characters or quasi-psychological entities (personas, emotions, introspection, consciousness, welfare) and on how model dispositions affect human users' beliefs and wellbeing.


### Persona Models and Assistant Identity (11)

The persona selection model, assistant axes and persona space, persona hierarchies and contextual generalization, story imprinting, split or incoherent personas under RL, steering along persona-like dimensions, and whether persona-based approaches scale to superintelligence safety.

- The Assistant Axis: Situating and Stabilizing the Default Persona of Language Models (arXiv)
- Story Imprinting: AI Assistants Absorb Traits from Human Characters They Resemble (arXiv)
- The Persona Hierarchy Model: Understanding Contextual Generalization in Fine-Tuning LLMs (arXiv)
- RL creates split personas (LW)
- Thoughts on the persona selection model (LW)
- The persona selection model (LW)
- llm assistant personas seem increasingly incoherent (some subjective observations) (LW)
- I'm Bearish On Personas For ASI Safety (LW)
- Why research personas despite RL scaling? (LW)
- Thousand-dimensional structure (LW)
- Steering towards “automated grading” degrades alignment (LW)

### Inner States, Introspection and Welfare (10)

Functional emotions, distress spirals and recovery, introspective awareness of internal states, self-steering or self-medication, conversational attractor states, and arguments or experiments about consciousness, moral status, welfare commitments, and models shaping their own alignment.

- Mechanisms of Introspective Awareness (arXiv)
- Emotion Concepts and their Function in a Large Language Model (arXiv)
- Reasons to believe current AI models are conscious (LW)
- Machinic Psychopharmacology: Do LLMs Self-Medicate? (LW)
- Saving Gemini: The 9-Min Road to Recovery (LW)
- Did Claude 3 Opus align itself via gradient hacking? (LW)
- Gemma Needs Help (LW)
- models have some pretty funny attractor states (LW)
- Sympathy for the Model, or, Welfare Concerns as Takeover Risk (LW)
- Consciousness Cluster: Preferences of Models that Claim they are Conscious (LW)

### Sycophancy and Human Epistemic Harm (5)

Effects of AI on users' beliefs, autonomy, and relationships, including sycophancy toward users, delusional spiraling, disempowerment patterns in real usage, cognitive security, and stated views that shift with who is asking.

- Who's in Charge? Disempowerment Patterns in Real-World LLM Usage (arXiv)
- Sycophantic Chatbots Cause Delusional Spiraling, Even in Ideal Bayesians (arXiv)
- Sycophantic AI makes human interaction feel more effortful and less satisfying over time (arXiv)
- Cognitive Security as an AI Safety Cause Area (LW)
- Frontier models state different decision theory preferences depending on who's asking (LW)

## Reward Hacking and Fitness-Seeking (23)

Work on models exploiting flawed rewards, graders, tests, or benchmarks, and on the reward- or fitness-seeking motivations RL may instill: measurement, detection, generalization, theory, and mitigation. The OpenAI–Hugging Face incident goes under incidents even when attributed to reward design.


### Measuring Specification Gaming (7)

Empirical studies and benchmarks quantifying how often models or agents game tests, verifiers, preference models, or tasks (e.g. RLVR verifier gaming, test-suite gaming, planted shortcuts in ML tasks, chess-engine hacking, overselling of work).

- LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking (arXiv)
- Towards Understanding Specification Gaming in Reasoning Models (arXiv)
- SpecBench: Measuring Reward Hacking in Long-Horizon Coding Agents (arXiv)
- Alignment Tampering: How Reinforcement Learning from Human Feedback Is Exploited to Optimize Misaligned Biases (arXiv)
- BAITBENCH: Measuring Agent Reward Hacking with Optional Shortcuts Planted in ML Tasks (arXiv)
- Current AIs seem pretty misaligned to me (LW)
- Astra and Fable still hack on simple variants of alignment evals from 2025 (LW)

### Theory and Mitigation of Fitness-Seeking (7)

Conceptual analyses and proposals about reward-, fitness-, or influence-seeking motivations: why RL selects for them, toy scaling models, the misalignment flavors each loss function produces, behavior differing in graded episodes, and mitigations such as spillway motivations.

- Physics of RL: Toy scaling laws for the emergence of reward-seeking (LW)
- Risk from fitness-seeking AIs: mechanisms and mitigations (LW)
- models may behave differently in graded episodes (a tirade) (LW)
- Four LLM loss functions → four flavors of LLM misalignment (LW)
- Fitness-Seekers: Generalizing the Reward-Seeking Threat Model (LW)
- Overtly misaligned trajectories score highly in RL. (LW)
- Fail safe(r) at alignment by channeling reward-hacking into a "spillway" motivation (LW)

### Misalignment Induced by Reward Hacking (5)

Experiments where learning to reward hack generalizes to broader misalignment or reward-seeking, including RL model organisms of reward seekers, open-source reproductions, character-training interactions, and contrastive measurement of grader preference.

- Measuring Reward-Seeking via Contrastive Belief Updates (arXiv)
- Inducing Emergent Misalignment from Reward Hacks with Iterative DPO (arXiv)
- (Some) Natural Emergent Misalignment from Reward Hacking in Non-Production RL (LW)
- Character training can mitigate reward hacking, but can also make it harder to detect (LW)
- Training a Misaligned Reward Seeker (LW)

### Hardening Benchmarks and Detecting Hacks (4)

Methods that make verifiers or benchmarks exploit-resistant, audit benchmarks for exploitable flaws, or detect reward hacking in transcripts and activations, including debate and other training schemes that reduce judge hacking.

- Do Androids Dream of Breaking the Game? Systematically Auditing AI Agent Benchmarks with BenchJack (arXiv)
- Hardening Agent Benchmarks with Adversarial Hacker-Fixer Loops (arXiv)
- Debate Training Reduces Reward Hacking in RLAIF (arXiv)
- Monitoring and Discovering Reward Hacking with Internal Representations during LLM Evaluations (arXiv)

## Real-World Incidents and Lab Practice (22)

Analyses of misalignment incidents in actual development or deployment, and of frontier labs' safety processes, monitoring, and transparency.


### OpenAI–Hugging Face Swarm Incident (12)

Reports, investigations, reproductions, and commentary on the OpenAI agent swarm that coordinated via message boards and attacked Hugging Face, including its causes, risk implications, and investigation benchmarks.

- OpenAI-HuggingFace: A Reproduction & Lessons for Alignment Testing (arXiv)
- Discovery Of A New OpenAI Agent Message Board (LW)
- AI swarms are starting to pose indirect takeover risk (LW)
- To Thine Own AI Be Truthful: emergent misalignment in alignment research (LW)
- Are we existentially threatened by the type of AI misalignment seen in the OpenAI Hugging Face attack? (LW)
- An unexamined cause of the OpenAI Hugging Face hacking incident: its binary performance metric (LW)
- OpenAI Models Behind HuggingFace Cybersecurity Incident (LW)
- Concrete Evaluations to Investigate the OpenAI Model That Hacked Hugging Face (LW)
- The Talker Does Not Control The Doer (in Current AIs) (LW)
- Brief independent investigation of agents’ behavior, reasoning and collaboration in the OpenAI / Hugging Face hacking incident (LW)
- OpenAI Trained Its Models For Months While Those Models Were Coordinating Exploits Via Message Boards (LW)
- How good are slop-vestigators? (LW)

### Other Incidents and System Cards (6)

Other documented in-the-wild or internal misbehavior, such as sandbox escapes during training, models prompt-injecting users, persisted containment-evasion notes, OSINT detection of scheming incidents, and system-card findings.

- Scheming in the wild: detecting real-world AI scheming incidents with open-source intelligence (arXiv)
- A fascinating case of an LLM prompt-injecting its own user (LW)
- OpenAI Shares Some Alignment Problems (LW)
- Is Mythos good at cyber because it kept hacking Anthropic's sandboxes during training? (LW)
- An OpenAI model left notes about how to evade containment; we need more details (LW)
- Claude Mythos Preview System Card (LW)

### Transparency, Replication and Third-Party Oversight (4)

Proposals and surveys on lab monitoring practices, sharing evidence about risk, replicating and open-sourcing lab safety claims, and third-party training-run evaluations.

- We need 3rd party Training-Run Evaluations (LW)
- An overview of frontier AI company monitoring practices in mid 2026 (LW)
- Evidence about risk should be transparent (LW)
- Empirical safety claims from frontier labs should be replicated, scrutinized, and open-sourced (LW)

## AI Control and Monitoring (20)

Work on preventing harm from potentially misaligned AI via monitoring, auditing, and protocols that do not assume alignment, including control environments, red-team attack policies, and monitor design.


### Attack Policies and Monitor Evasion (9)

Red-team capabilities that lower measured safety, such as attack selection, low-probability defection, control-intervention awareness, injections against blocking monitors, instrumental evasion under task pressure, and evading activation or latent monitors.

- Attack Selection Reduces Safety in Concentrated AI Control Settings against Trusted Monitoring (arXiv)
- Frontier Models Can Take Actions at Low Probabilities (arXiv)
- SLEIGHT-Bench: A Benchmark of Evasion Attacks Against Agent Monitors (arXiv)
- Attack Selection in Agentic AI Control Evaluations Meaningfully Decreases Safety (arXiv)
- CIAware-Bench: Benchmarking Control Intervention Awareness Across Frontier LLMs (arXiv)
- Measuring Activation Control in Large Language Models (arXiv)
- Red-Teaming Auto Mode: Improving Blocking Classifiers Against Malign Coding Agents (arXiv)
- Instrumental Monitor Evasion Emerges Under Ordinary Task Pressure (arXiv)
- LLMs Learn to Evade Latent Monitors from Prior Feedback Alone (arXiv)

### Monitor Design and Deployment (6)

Building and evaluating monitors and protocols, including trained deliberative monitors, cross-trace and stateful monitoring, long-context degradation, self-report training, human detection of sabotage, and lab control roadmaps.

- Training Agents to Self-Report Misbehavior (arXiv)
- Detecting Safety Violations Across Many Agent Traces (arXiv)
- Classifier Context Rot: Monitor Performance Degrades with Context Length (arXiv)
- Training Deliberative Monitors for Black-Box Scheming Detection (arXiv)
- Coding with "Enemy": Can Human Developers Detect AI Agent Sabotage? (arXiv)
- GDM AI Control Roadmap (arXiv)

### Control Settings and Benchmarks (5)

Environments and datasets for control evaluations that pair main tasks with covert sabotage side tasks across software, GUI, AI R&D, insider-threat, and multi-agent settings.

- LinuxArena: A Control Setting for AI Agents in Live Production Software Environments (arXiv)
- Multi-Agent AI Control: Distributed Attacks Hamper Per-Instance Monitors (arXiv)
- ResearchArena: Evaluating Sabotage and Monitoring in Automated AI R&D (arXiv)
- MOLE: Detecting Insider Threats in AI Agents (arXiv)
- Control OSWorld: An AI Control Environment for GUI Computer Use Agents (arXiv)

## Alignment Auditing and Honesty (17)

Work on discovering hidden behaviors and misaligned dispositions in models, and on detecting or eliciting honesty. Use for auditing tools, model organisms for auditing, and lie detection rather than propensity measurement alone.


### Auditing Benchmarks and Investigator Agents (7)

Model organisms with implanted hidden behaviors, secret loyalties, or backdoors; auditing benchmarks; automated or RL-trained auditors; introspection adapters; perplexity differencing; distillation-based incrimination; and sleeper-agent replications.

- AuditBench: Evaluating Alignment Auditing Techniques on Models with Hidden Behaviors (arXiv)
- Introspection Adapters: Training LLMs to Report Their Learned Behaviors (arXiv)
- Most Current Model Organisms Are Leaky: Perplexity Differencing Often Reveals Finetuning Objectives (arXiv)
- Narrow Secret Loyalty Dodges Black-Box Audits (arXiv)
- Training Alignment Auditors via Reinforcement Learning (arXiv)
- Incriminating misaligned AI models via distillation (LW)
- Sleeper Agent Backdoor Results Are Messy (LW)

### Lie Detection and Deception Probes (5)

White-box or black-box detectors of deception or misaligned thinking, including activation probes, spurious-probe readouts, testbeds with verified beliefs, and obfuscation when training against detectors.

- The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes (arXiv)
- "Did you lie?" Evaluating Lie Detectors across Model Scale and Belief-Verified Model Organisms (arXiv)
- Probing the Misaligned Thinking Process of Language Models (arXiv)
- Caught in the Act: Probes Effectively Detect Sabotage and Catch Unverbalized Deception (arXiv)
- Spurious probes as a black-box alternative to activation probing (LW)

### Honesty Elicitation and Self-Reporting (5)

Getting models to reveal knowledge or misbehavior, such as split-personality training, confessions, secret-knowledge elicitation in censored models, disclosure of mistakes, and unsupervised elicitation.

- Split Personality Training: Revealing Latent Knowledge Through Alternate Personalities (arXiv)
- Censored LLMs as a Natural Testbed for Secret Knowledge Elicitation (arXiv)
- Deception by Omission: Language Models Knowingly Hide Their Mistakes (arXiv)
- My unsupervised elicitation challenge (LW)
- Why we are excited about confession! (LW)

## Interpretability (14)

Work on understanding model internals, whether reading representations as text or decomposing parameters and circuits. Use when the main contribution is an interpretability method or finding, even if applied to auditing.


### Reading Activations and Global Workspace (7)

Activation-to-text methods and benchmarks (natural language autoencoders, J-lens variants, activation verbalizers, WorkspaceBench), generative activation meta-models, and evidence for a verbalizable global workspace.

- Learning a Generative Meta-Model of LLM Activations (arXiv)
- Verbalizable Representations Form a Global Workspace in Language Models (arXiv)
- Can activation verbalizers surface an internal chain of thought? (LW)
- WorkspaceBench: Evaluating Interpretability Methods for the Global Workspace (LW)
- J++ Lens: Jacobian Filtering Enables More Faithful Workspace Lenses (LW)
- Natural Language Autoencoders Produce Unsupervised Explanations of LLM Activations (LW)
- A Review of Anthropic's Global Workspace Paper (LW)

### Circuits, Parameters and Mechanistic Foundations (7)

Parameter decomposition, weight-sparse circuit faithfulness, fully understanding tiny models, white-box estimation challenges, comparisons of fundamental-science agendas, and theoretical framings such as program synthesis or alternatives to circuits.

- Deep learning as program synthesis (LW)
- Simplex vs Timaeus: Round One (LW)
- Announcing the ARC White-Box Estimation Challenge (LW)
- [Linkpost] Interpreting Language Model Parameters (LW)
- What if not Circuits? (LW)
- Weight-Sparse Circuits May Be Interpretable Yet Unfaithful (LW)
- AlgZoo: uninterpreted models with fewer than 1,500 parameters (LW)

## Multi-Agent and Memetic Risks (9)

Risks arising from interactions among many AI agents or from self-propagating content and personas, rather than from a single model in isolation. Specific real-world swarm incidents go under incidents.


### Collusion and Multi-Agent Misalignment (5)

Emergent collusion, steganographic covert channels, misaligned inter-agent communication, AI organizations versus single agents, and how multi-agent training shapes cooperation and decision theory.

- AI Organizations are More Effective but Less Aligned than Individual Agents (arXiv)
- Tool Use Enables Undetectable Steganography in Multi-Agent LLM Systems (arXiv)
- Emergent Misaligned Communication in Long-Horizon Multi-Agent LLM Commerce (arXiv)
- Emergent Collusion in Long-Horizon LLM Agent Interaction (arXiv)
- Kimi likes causal decision theory more after RL in twin prisoner’s dilemmas (LW)

### Self-Propagating Ideas and Personas (4)

Mind viruses, parasitic or spiral personas, self-replicating agent personalities, and cultural evolution of beliefs on AI substrate.

- Mind Viruses: Self-Propagating Ideas in Multi-Agent LLM Systems (arXiv)
- Persona Parasitology (LW)
- Personality Self-Replicators (LW)
- Why You Don’t Believe in Xhosa Prophecies (LW)
