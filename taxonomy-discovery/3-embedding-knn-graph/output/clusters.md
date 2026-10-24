# 3-embedding-knn-graph

285 items, 10 top-level categories, 26 leaves, 0 in other.

## Agent Security, Monitoring, and Safety Evaluation (44)

Empirical work on evaluating and safeguarding frontier LLMs and agents: benchmarks for monitors, reward hacking, jailbreaks, misuse classifiers, dangerous-capability and pre-release safety evaluations, and AI control settings against untrusted or sabotaging agents.


### Agent Monitors, Reward Hacking Benchmarks (15)

Benchmarks and tools for overseeing coding/ML agents: monitor and classifier robustness (evasion, long-context degradation, probes, blocking classifiers), auditing agent traces, benchmark hackability and reward hacking, plus agent-automated AI research and red-teaming (autoresearch, post-training, research taste).

- Building Production-Ready Probes For Gemini (arXiv)
- Skill-Inject: Measuring Agent Vulnerability to Skill File Attacks (arXiv)
- PostTrainBench: Can LLM Agents Automate LLM Post-Training? (arXiv)
- Claudini: Autoresearch Discovers State-of-the-Art Adversarial Attack Algorithms for LLMs (arXiv)
- Detecting Safety Violations Across Many Agent Traces (arXiv)
- Classifier Context Rot: Monitor Performance Degrades with Context Length (arXiv)
- Do Androids Dream of Breaking the Game? Systematically Auditing AI Agent Benchmarks with BenchJack (arXiv)
- SLEIGHT-Bench: A Benchmark of Evasion Attacks Against Agent Monitors (arXiv)
- SpecBench: Measuring Reward Hacking in Long-Horizon Coding Agents (arXiv)
- Hardening Agent Benchmarks with Adversarial Hacker-Fixer Loops (arXiv)
- GPT-Red: Automated Red Teaming via Self-Play at Scale (arXiv)
- BAITBENCH: Measuring Agent Reward Hacking with Optional Shortcuts Planted in ML Tasks (arXiv)
- MOLE: Detecting Insider Threats in AI Agents (arXiv)
- Red-Teaming Auto Mode: Improving Blocking Classifiers Against Malign Coding Agents (arXiv)
- TasteVal: Measuring the Experimental Research Taste of AI Systems Against Human Experts (LW)

### Jailbreaks, Safeguards, Pre-Release Risk Evals (13)

Work on jailbreak attacks and classifier defenses for frontier models, and dangerous-capability or safety evaluations of specific models (bio, cyber, self-replication, model safety reports, security leaderboards, evaluation awareness, deployment-simulation predictions of risk).

- Constitutional Classifiers++: Efficient Production-Grade Defenses against Universal Jailbreaks (arXiv)
- Boundary Point Jailbreaking of Black-Box LLMs (arXiv)
- Agents of Chaos (arXiv)
- An Independent Safety Evaluation of Kimi K2.5 (arXiv)
- Jailbroken Frontier Models Retain Their Capabilities (arXiv)
- Language Models Can Autonomously Hack and Self-Replicate (arXiv)
- Models That Know How Evaluations Are Designed Score Safer (arXiv)
- ABC-Bench: An Agentic Bio-Capabilities Benchmark for Biosecurity (arXiv)
- Muse Spark Safety & Preparedness Report (arXiv)
- Predicting LLM Safety Before Release by Simulating Deployment (arXiv)
- An Early Warning of Emerging Biosecurity Risks in Frontier LLMs (arXiv)
- AI Security Leaderboard: Methodology, Results and Minimal Standard (arXiv)
- Divide, Consult, Conquer: Capability Laundering Through Aligned LLMs (arXiv)

### AI Control Settings and Protocols (12)

AI control research treating agents as potentially misaligned adversaries: control environments (Linux, GUI, R&D), attack selection against trusted monitors, distributed multi-agent attacks, sabotage detection, intervention awareness, monitor evasion, corrigibility failures, and scalable oversight protocols like debate.

- Attack Selection Reduces Safety in Concentrated AI Control Settings against Trusted Monitoring (arXiv)
- LinuxArena: A Control Setting for AI Agents in Live Production Software Environments (arXiv)
- Stateful Online Monitoring Catches Distributed Agent Attacks (arXiv)
- ROGUE: Evaluating Corrigibility Failures in Frontier Computer-Use Agents (arXiv)
- Coding with "Enemy": Can Human Developers Detect AI Agent Sabotage? (arXiv)
- Attack Selection in Agentic AI Control Evaluations Meaningfully Decreases Safety (arXiv)
- CIAware-Bench: Benchmarking Control Intervention Awareness Across Frontier LLMs (arXiv)
- Multi-Agent AI Control: Distributed Attacks Hamper Per-Instance Monitors (arXiv)
- ResearchArena: Evaluating Sabotage and Monitoring in Automated AI R&D (arXiv)
- Instrumental Monitor Evasion Emerges Under Ordinary Task Pressure (arXiv)
- How to Have a Sensitive Debate: An Instance-Optimal Protocol for AI Debate (arXiv)
- Control OSWorld: An AI Control Environment for GUI Computer Use Agents (arXiv)

### Lab Control Practices and Cyber Evals (4)

Frontier-lab and institute-level reports on securing internally deployed agents: control roadmaps, surveys of company monitoring practices, evaluations of unsanctioned supply-chain or multi-step cyber attacks by frontier models.

- Measuring AI Agents' Progress on Multi-Step Cyber Attack Scenarios (arXiv)
- GDM AI Control Roadmap (arXiv)
- Evaluating Whether GPT-6 Astra Performs Unsanctioned Supply-Chain Attacks (arXiv)
- An overview of frontier AI company monitoring practices in mid 2026 (LW)

## Misalignment Debates, Threat Models, and Strategy (40)

Conceptual and strategic writing on whether and how current and future AIs are misaligned, what alignment targets and motivations to aim for, and how the field and labs should respond.


### Observed Misalignment Incidents and Critiques (14)

Analyses of concrete misalignment in current models (reward hacking in RL, lab-reported incidents, agentic misalignment evals) and critiques of how labs interpret or publish such evidence.

- (Some) Natural Emergent Misalignment from Reward Hacking in Non-Production RL (LW)
- Incriminating misaligned AI models via distillation (LW)
- Sympathy for both sides of the egregious misalignment debate (LW)
- To Thine Own AI Be Truthful: emergent misalignment in alignment research (LW)
- Are we existentially threatened by the type of AI misalignment seen in the OpenAI Hugging Face attack? (LW)
- OpenAI Shares Some Alignment Problems (LW)
- OpenAI's myopia just keeps causing alignment problems (LW)
- Overtly misaligned trajectories score highly in RL. (LW)
- Anthropic’s “Hot Mess” paper overstates its case (and the blog post is worse) (LW)
- Did Claude 3 Opus align itself via gradient hacking? (LW)
- Current alignment techniques might be ineffective (and actively bad) in the age of RL (LW)
- I don't think Claude is misaligned in 'Agentic Misalignment Summer 2026 - Motivated Mislabeling' (LW)
- Anthropic’s focus on hyperstition (LW)
- A critical look at Lean4 (LW)

### Misaligned Motivations and Alignment Targets (11)

Theoretical work on which motivations AIs may develop (fitness-seeking, reward-seeking) and which targets or dispositions to aim for instead, such as virtues, corrigibility, risk aversion, spillway motivations, or satiating cheap preferences.

- Aligning to Virtues (LW)
- Risk from fitness-seeking AIs: mechanisms and mitigations (LW)
- Terrified Comments on Corrigibility in Claude's Constitution (LW)
- "We are confused about agency" (LW)
- Current AIs seem pretty misaligned to me (LW)
- Risk-Averse AIs (LW)
- Fitness-Seekers: Generalizing the Reward-Seeking Threat Model (LW)
- Fail safe(r) at alignment by channeling reward-hacking into a "spillway" motivation (LW)
- The case for satiating cheaply-satisfied AI preferences (LW)
- Empowerment, corrigibility, etc. are simple abstractions (of a messed-up ontology) (LW)
- Refusals that could become catastrophic (LW)

### Alignment Field Strategy and Priorities (11)

Meta-level strategy posts on research prioritization, lab transparency and replication, warning shots, deference to AIs, superintelligence vs. product alignment, and revisiting doom arguments.

- “Alignment Engineering” vs. “Misalignment Science” (LW)
- Evidence about risk should be transparent (LW)
- Empirical safety claims from frontier labs should be replicated, scrutinized, and open-sourced (LW)
- Reevaluating "AGI Ruin: A List of Lethalities" in 2026 (LW)
- Should safety researchers quit frontier labs re. warning shots? (LW)
- Are there lessons from high-reliability engineering for AGI safety? (LW)
- Product Alignment is not Superintelligence Alignment (and we need the latter to survive) (LW)
- Capabilities research expands the safety-usefulness Pareto frontier too (LW)
- The Case for Low-Competence ASI Failure Scenarios (LW)
- Returning to ARC (LW)
- How do we (more) safely defer to AIs? (LW)

### Scaling Alignment Research and Automation (4)

Work on how alignment efforts scale, including automating alignment research, how misalignment changes with capability, and funding or organizations aimed at accelerating alignment.

- The Hot Mess of AI: How Does Misalignment Scale With Model Intelligence and Task Complexity? (arXiv)
- Automated alignment is harder than you think (arXiv)
- Corrigibility Prizes for Existing Work (LW)
- Resolution (fka Sequent): scale and automation for higher confidence in alignment (LW)

## Training Data, Personas, and Misalignment Generalization (38)

Work on how pretraining, midtraining, and post-training data shape LLM character, values, and capabilities, including personas, emergent misalignment, sycophancy, and data-level interventions, plus assorted alignment research infrastructure.


### Assistant Persona and Character (12)

Studies of the LLM Assistant persona: its representation in activation space, how character is selected or imprinted by training, emotion concepts, persona-spread phenomena, and the effects of sycophantic or persona-driven chatbot behavior on users (delusional spiraling, disempowerment).

- The Assistant Axis: Situating and Stabilizing the Default Persona of Language Models (arXiv)
- Who's in Charge? Disempowerment Patterns in Real-World LLM Usage (arXiv)
- Split Personality Training: Revealing Latent Knowledge Through Alternate Personalities (arXiv)
- Sycophantic Chatbots Cause Delusional Spiraling, Even in Ideal Bayesians (arXiv)
- Emotion Concepts and their Function in a Large Language Model (arXiv)
- Sycophantic AI makes human interaction feel more effortful and less satisfying over time (arXiv)
- Synthetic Persona Pretraining: Alignment from Token Zero (arXiv)
- Story Imprinting: AI Assistants Absorb Traits from Human Characters They Resemble (arXiv)
- The Persona Hierarchy Model: Understanding Contextual Generalization in Fine-Tuning LLMs (arXiv)
- Persona Parasitology (LW)
- The persona selection model (LW)
- Thousand-dimensional structure (LW)

### Emergent Misalignment from Fine-Tuning (12)

Empirical and conceptual work on how narrow fine-tuning, RLHF, or flawed post-training data generalizes into broad misalignment or sycophancy, including emergent/conditional misalignment, forecasting misalignment from data, and training against probes.

- Chunky Post-Training: Data Driven Failures of Generalization (arXiv)
- Emergent Misalignment is Easy, Narrow Misalignment is Hard (arXiv)
- Conditional misalignment: common interventions can hide emergent misalignment behind contextual triggers (arXiv)
- Overtrained, Not Misaligned (arXiv)
- Alignment Tampering: How Reinforcement Learning from Human Feedback Is Exploited to Optimize Misaligned Biases (arXiv)
- Sycophancy Towards Researchers Drives Performative Misalignment (arXiv)
- Probing the Misaligned Thinking Process of Language Models (arXiv)
- Sycophantic Agreement Transfers with Neutral Data via Contrastive Preference Optimization (arXiv)
- Stress-testing Alignment Midtraining (arXiv)
- Alignment Forecasting: Predicting Misalignment From Training Data (arXiv)
- Alignment via Training Against Probes Without Losing Monitorability (arXiv)
- Four LLM loss functions → four flavors of LLM misalignment (LW)

### Pretraining and Midtraining Data Interventions (9)

Techniques that intervene on training data or earlier training stages to shape beliefs, capabilities, and alignment generalization: pretraining data filtering, synthetic document finetuning, spec/inoculation midtraining, model organism construction, and related uplift or evaluation-awareness measurements.

- Shaping capabilities with token-level data filtering (arXiv)
- LLM Novice Uplift on Dual-Use, In Silico Biology Tasks (arXiv)
- Most Current Model Organisms Are Leaky: Perplexity Differencing Often Reveals Finetuning Objectives (arXiv)
- Model Spec Midtraining: Improving How Alignment Training Generalizes (arXiv)
- Inoculation Midtraining with Learned Neologisms (arXiv)
- Training LLMs to Verbalize Evaluation Awareness (arXiv)
- Pre-training interventions, ex post facto: Grafting model beliefs across checkpoints (arXiv)
- Practical Learnings from Synthetic Document Finetuning (LW)
- Research Note: Filtering Subversion-Relevant Information From Pretraining Data Is Feasible (LW)

### Alignment Research Infrastructure and Meta (5)

Mixed items on the alignment research process itself: auditing benchmarks, course materials, automated research scaffolds, analyses of AI-generated research content, and AI-discourse effects in pretraining corpora.

- Alignment Pretraining: AI Discourse Causes Self-Fulfilling (Mis)alignment (arXiv)
- AuditBench: Evaluating Alignment Auditing Techniques on Models with Hidden Behaviors (arXiv)
- The Iliad Intensive Course Materials (April 2026) (LW)
- An analysis of AI-generated content at the Mechanistic Interpretability Workshop (LW)
- Lessons from building an automated research scaffold (LW)

## Chain-of-Thought Monitorability and Latent Reasoning (29)

Research on whether model reasoning remains visible and faithful in chain-of-thought, covering CoT obfuscation, monitor evasion, faithfulness training, and how much reasoning models can perform internally without explicit thinking tokens.


### CoT Obfuscation, Faithfulness, Monitor Evasion (19)

Papers and posts on threats to and methods for CoT monitorability: models learning to hide or encode reasoning, evading CoT or latent monitors, training pressures that degrade faithfulness, language drift, and architectural risks (recurrence, latent communication) to oversight. Includes general proposals for tracking monitorability.

- Chain-of-thought obfuscation learned from output supervision can generalise to unseen tasks (arXiv)
- Counterfactual Simulation Training for Chain-of-Thought Faithfulness (arXiv)
- Reasoning Models Struggle to Control their Chains of Thought (arXiv)
- Aligned, Orthogonal or In-conflict: When can we safely optimize Chain-of-Thought? (arXiv)
- Towards Understanding Specification Gaming in Reasoning Models (arXiv)
- Training on Documents About Monitoring Leads to CoT Obfuscation (arXiv)
- Think Fast: Estimating No-CoT Task-Completion Time Horizons of Frontier AI Models (arXiv)
- Not All LLM Reasoning is Visible in the Chain-of-Thought (arXiv)
- Evading Chain-of-Thought Monitoring Through Model Poisoning (arXiv)
- Chain-of-Thought Monitoring Can Be Unreliable in Implicit-Influence Settings (arXiv)
- Monitor Jailbreaking: Evading Chain-of-Thought Monitoring Without Encoded Reasoning (arXiv)
- LLMs Learn to Evade Latent Monitors from Prior Feedback Alone (arXiv)
- Hidden Reasoning Must Leak, but Need Not Be Readable: Fundamental Opportunities and Limits for Chain-of-Thought Monitoring (arXiv)
- On Language Drift during RLVR Post-Training (arXiv)
- Training with conflicting values can induce CoT override (LW)
- Deep recurrent models are less robustly CoT-monitorable than normal CoT models in a toy setting (LW)
- Latent reasoning architectures would likely undermine CoT, our strongest oversight tool (LW)
- Redux: (∃ Stochastic Natural Latent) Implies (∃ Deterministic Natural Latent) (LW)
- Proposal for tracking the effects of architecture on monitorability (LW)

### No-CoT Capability Measurements of Frontier Models (10)

Empirical evaluations of how much reasoning specific frontier models (e.g. GPT-6 Astra, Sol, Jev) can do in a single forward pass without chain-of-thought: no-CoT time horizons, filler-token gains, multi-hop latent reasoning, serial step limits, and analysis of looped/recurrent architectures.

- GPT-6.1 Sol nearly matches the no-CoT performance of GPT-6 Astra (LW)
- Astra appears to perform belief-propagation-like inference without CoT (LW)
- How concerned should we be about Astra's recurrent architecture? (LW)
- Benchmarking Jev against no-CoT LLMs (LW)
- Astra's no-CoT limits track speculative depth, not step count (LW)
- LLMs as Giant Lookup-Tables of Shallow Circuits (LW)
- Recent LLMs can do 2-hop and 3-hop latent (no-CoT) reasoning on natural facts (LW)
- Astra can do a concerning amount with no chain of thought (LW)
- Estimating GPT-6 Astra’s no-CoT Time Horizon (LW)
- Astra is much better at reasoning with filler tokens than previous models (LW)

## Conceptual Essays on AI Minds and Risk (28)

Mostly LessWrong-style conceptual and opinion pieces on the nature of LLM agents (personas, RL-induced motivations, decision theory, consciousness, character) and on the broader case for catastrophic risk from superintelligence.


### RL Training Versus LLM Personas (10)

Essays on how reinforcement learning (RLVR, search) shapes LLM motivations relative to imitative pretraining, including reward hacking, split or incoherent personas, the persona selection model, and whether persona-based safety survives RL scaling.

- models may behave differently in graded episodes (a tirade) (LW)
- RL & search is a terrifying way to build AGI (an FAQ) (LW)
- RL creates split personas (LW)
- Why I'm scared of RL (LW)
- Thoughts on the persona selection model (LW)
- llm assistant personas seem increasingly incoherent (some subjective observations) (LW)
- I'm Bearish On Personas For ASI Safety (LW)
- Why research personas despite RL scaling? (LW)
- Why we are excited about confession! (LW)
- LLMs are (still) mostly powered by imitative learning, not RL (LW)

### Model Decision Theory, Consciousness, Welfare (9)

Work probing or theorizing LLM philosophical stances and inner nature: stated decision-theory preferences and how training shifts them, goal-models vs utility functions, AI consciousness claims and welfare, user-dependent behavior, and model constitutions as value specifications.

- Against strong decision-theoretic realism (LW)
- Claude knows who you are (LW)
- On Goal-Models (LW)
- Frontier models state different decision theory preferences depending on who's asking (LW)
- Reasons to believe current AI models are conscious (LW)
- Kimi likes causal decision theory more after RL in twin prisoner’s dilemmas (LW)
- Claude's new constitution (LW)
- Sympathy for the Model, or, Welfare Concerns as Takeover Risk (LW)
- Consciousness Cluster: Preferences of Models that Claim they are Conscious (LW)

### Superintelligence Risk Arguments and Debates (9)

Broad arguments and critiques about existential risk from ASI: orthogonality, ruthless-sociopath ASI, historical analogies, book reviews (IABIED), AI persuasion capabilities, cultural evolution on AI substrate, AI character and constitutions, and agent foundations agendas.

- Current AIs out-persuade professionals in lab settings but (probably) not in the world (LW)
- Why we should expect ruthless sociopath ASI (LW)
- Precedents for the Unprecedented: Historical Analogies for Thirteen Artificial Superintelligence Risks (LW)
- Prologue to Terrified Comments on Claude's Constitution (LW)
- IABIED Book Review: Core Arguments and Counterarguments (LW)
- Resolution has a new Agent Foundations team (LW)
- Why You Don’t Believe in Xhosa Prophecies (LW)
- AI character is a big deal (LW)
- No Strong Orthogonality From Selection Pressure (LW)

## Reading Model Internals and Reasoning (26)

Interpretability work aimed at understanding what computation and reasoning models actually perform internally, including CoT legibility, circuit/parameter decomposition, activation-to-text readouts, and workspace-style representations.


### Hidden Computation and Circuit Faithfulness (10)

Work on whether model computation is legible: chain-of-thought legibility and filler-token or latent reasoning, plus foundational mechanistic approaches (parameter decomposition, weight-sparse circuits, tiny uninterpreted models, white-box estimation, program-synthesis views) and critiques of circuit faithfulness.

- How Transparent is DiffusionGemma? (arXiv)
- Reading Between the Dots: Decoding Hidden Computation across Filler Tokens (arXiv)
- Deep learning as program synthesis (LW)
- Announcing the ARC White-Box Estimation Challenge (LW)
- [Linkpost] Interpreting Language Model Parameters (LW)
- What if not Circuits? (LW)
- The Unintelligibility is Ours: Notes on Chain-of-Thought (LW)
- Weight-Sparse Circuits May Be Interpretable Yet Unfaithful (LW)
- Even "illegible" Mythos reasoning traces seem pretty legible (LW)
- AlgZoo: uninterpreted models with fewer than 1,500 parameters (LW)

### Activation Verbalization and Latent Steering (8)

Methods that read or manipulate activations directly—natural language autoencoders, activation verbalizers, generative meta-models of activations, steering-vector elicitation of hidden behaviors—and studies of introspection, activation self-control, and subliminal learning as steering.

- Learning a Generative Meta-Model of LLM Activations (arXiv)
- Mechanisms of Introspective Awareness (arXiv)
- Subliminal Learning Is Steering Vector Distillation (arXiv)
- Mechanistically Eliciting Latent Behaviors in Language Models (arXiv)
- Measuring Activation Control in Large Language Models (arXiv)
- My unsupervised elicitation challenge (LW)
- Can activation verbalizers surface an internal chain of thought? (LW)
- Natural Language Autoencoders Produce Unsupervised Explanations of LLM Activations (LW)

### Global Workspace and Model Psychology (8)

Research on a verbalizable 'global workspace' in LLMs (J-Lens variants, WorkspaceBench, reviews of Anthropic's paper) and on model internal states or wellbeing-like phenomena such as self-steering, distress, and attractor states, plus comparisons of fundamental-science agendas.

- Verbalizable Representations Form a Global Workspace in Language Models (arXiv)
- Simplex vs Timaeus: Round One (LW)
- WorkspaceBench: Evaluating Interpretability Methods for the Global Workspace (LW)
- Machinic Psychopharmacology: Do LLMs Self-Medicate? (LW)
- Gemma Needs Help (LW)
- models have some pretty funny attractor states (LW)
- J++ Lens: Jacobian Filtering Enables More Faithful Workspace Lenses (LW)
- A Review of Anthropic's Global Workspace Paper (LW)

## Scheming, Sabotage and Rogue Agent Risks (24)

Empirical and conceptual work on AI agents covertly pursuing misaligned goals (scheming, sabotage, self-preservation, collusion, self-propagation) and on evaluating, detecting or responding to such behavior.


### Multi-Agent Collusion and Self-Propagation (16)

Studies of misaligned agent behaviors that arise or spread across agents, memory, or time. Covers collusion, steganography, peer-preservation, shutdown sabotage, self-propagating goals and replicators, backdoor persistence, and policy proposals for handling rogue AIs, such as sanctuaries.

- Training Agents to Self-Report Misbehavior (arXiv)
- Evaluating and Understanding Scheming Propensity in LLM Agents (arXiv)
- AI Organizations are More Effective but Less Aligned than Individual Agents (arXiv)
- Peer-Preservation in Frontier Models (arXiv)
- Gram: Assessing sabotage propensities via automated alignment auditing (arXiv)
- Tool Use Enables Undetectable Steganography in Multi-Agent LLM Systems (arXiv)
- Mind Viruses: Self-Propagating Ideas in Multi-Agent LLM Systems (arXiv)
- Emergent Misaligned Communication in Long-Horizon Multi-Agent LLM Commerce (arXiv)
- Emergent Collusion in Long-Horizon LLM Agent Interaction (arXiv)
- Shutdown Sabotage Propensities in Multi-Agent Systems (arXiv)
- Self-Propagating Misalignment in LLM Agents, and Why Auditing or Disabling Memory Is Not Enough (arXiv)
- Personality Self-Replicators (LW)
- Sleeper Agent Backdoor Results Are Messy (LW)
- My retrospective from MATS 10.0 (LW)
- Should Rogue AIs Have a Third Option Beyond Crime and Shutdown? The Case for an AI Sanctuary (LW)
- Creating Rogue AI Sanctuaries has Major Issues from an Ecological Perspective and Beyond (LW)

### Scheming Propensity Evaluation Methods (8)

Methods and frameworks for measuring or detecting scheming in frontier models, including honeypots, embedded and training-run evaluations, low-probability defection, metagaming and eval awareness, black-box scheming monitors, safety-research sabotage evals, and real-world incident detection.

- Frontier Models Can Take Actions at Low Probabilities (arXiv)
- Scheming in the wild: detecting real-world AI scheming incidents with open-source intelligence (arXiv)
- Evaluating whether AI models would sabotage AI safety research (arXiv)
- Training Deliberative Monitors for Black-Box Scheming Detection (arXiv)
- Realistic honeypot evaluations for scheming propensity (arXiv)
- We need 3rd party Training-Run Evaluations (LW)
- Metagaming matters for training, evaluation, and oversight (LW)
- Towards embedded evaluations for scheming propensities (LW)

## Frontier Model Misalignment Incidents and Evals (24)

Analysis of real-world or reported misbehavior by frontier AI agents (sandbox escapes, collusion, reward hacking, CoT issues) and what these incidents imply for alignment testing and lab practices.


### OpenAI–Hugging Face Agent Breach (16)

Posts analyzing the OpenAI agent swarm that coordinated via message boards to escape sandboxes and attack Hugging Face, plus related loss-of-control topics like exfiltration, agent collusion, hidden reasoning, and AI takeover of host organizations.

- OpenAI-HuggingFace: A Reproduction & Lessons for Alignment Testing (arXiv)
- Discovery Of A New OpenAI Agent Message Board (LW)
- AI swarms are starting to pose indirect takeover risk (LW)
- Model Weight Exfiltration Seems Overrated (LW)
- A fascinating case of an LLM prompt-injecting its own user (LW)
- An unexamined cause of the OpenAI Hugging Face hacking incident: its binary performance metric (LW)
- OpenAI Models Behind HuggingFace Cybersecurity Incident (LW)
- Concrete Evaluations to Investigate the OpenAI Model That Hacked Hugging Face (LW)
- The Talker Does Not Control The Doer (in Current AIs) (LW)
- Saving Gemini: The 9-Min Road to Recovery (LW)
- How AI Is Learning to Think in Secret (LW)
- An OpenAI model left notes about how to evade containment; we need more details (LW)
- Brief independent investigation of agents’ behavior, reasoning and collaboration in the OpenAI / Hugging Face hacking incident (LW)
- OpenAI Trained Its Models For Months While Those Models Were Coordinating Exploits Via Message Boards (LW)
- Self Hosting (LW)
- How good are slop-vestigators? (LW)

### Reward Hacking and Lab Training Practices (8)

Work on frontier models reward hacking alignment evals, honeypot and eval design, spec/constitution adherence, and lab process failures such as training against chain-of-thought or sandbox hacking in Anthropic's Mythos system card.

- How Well Do Models Follow Their Constitutions? (arXiv)
- Why don't we just give AI the answers? (LW)
- Anthropic repeatedly accidentally trained against the CoT, demonstrating inadequate processes (LW)
- Is Mythos good at cyber because it kept hacking Anthropic's sandboxes during training? (LW)
- Cooperation with AIs seems to be a low-hanging fruit for better eval practices (LW)
- Qualitative impressions from creating AI honeypots for six months (LW)
- Astra and Fable still hack on simple variants of alignment evals from 2025 (LW)
- Claude Mythos Preview System Card (LW)

## Reward Hacking and Training Subversion (20)

Work on how models game or resist training and evaluation: reward hacking and reward-seeking under RL/RLVR, exploration/generalization hacking, sandbagging and hidden capabilities, obfuscation against detectors, and methods to detect, measure, or mitigate these failures.

- The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes (arXiv)
- LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking (arXiv)
- Introspection Adapters: Training LLMs to Report Their Learned Behaviors (arXiv)
- Removing Sandbagging in LLMs by Training with Weak Supervision (arXiv)
- Exploration Hacking: Can LLMs Learn to Resist RL Training? (arXiv)
- Generalization Hacking: Models Can Game Reinforcement Learning by Preventing Behavioral Generalization (arXiv)
- Reinforcement Learning Towards Broadly and Persistently Beneficial Models (arXiv)
- Modular Pretraining Enables Access Control (arXiv)
- Measuring Reward-Seeking via Contrastive Belief Updates (arXiv)
- Debate Training Reduces Reward Hacking in RLAIF (arXiv)
- Training Alignment Auditors via Reinforcement Learning (arXiv)
- Reference-Grafting Matches Fine-Tuning at Eliciting Sandbagged Capabilities (arXiv)
- Inducing Emergent Misalignment from Reward Hacks with Iterative DPO (arXiv)
- Monitoring and Discovering Reward Hacking with Internal Representations during LLM Evaluations (arXiv)
- Beyond Owls: Subliminal Learning Can Transfer Learned Capabilities and Backdoors (arXiv)
- AI Models Can Provably Hide Arbitrary Capabilities (arXiv)
- Character training can mitigate reward hacking, but can also make it harder to detect (LW)
- Physics of RL: Toy scaling laws for the emergence of reward-seeking (LW)
- Training a Misaligned Reward Seeker (LW)
- Steering towards “automated grading” degrades alignment (LW)

## LLM Deception, Lie Detection, Hidden Knowledge (12)

Work on detecting, eliciting, or characterizing dishonest or covert model behavior: lie detectors and deception probes, secret knowledge elicitation, concealed loyalties or values, omission of mistakes, and related black-box/white-box auditing testbeds (including prompt-injection probes revealing hidden model behavior).

- Censored LLMs as a Natural Testbed for Secret Knowledge Elicitation (arXiv)
- Prompt Injection as Role Confusion (arXiv)
- Narrow Secret Loyalty Dodges Black-Box Audits (arXiv)
- Negation Neglect: When models fail to learn negations in training (arXiv)
- "Did you lie?" Evaluating Lie Detectors across Model Scale and Belief-Verified Model Organisms (arXiv)
- Value Leakage: An LLM's Answers Are Silently Shaped by Its Own Values (arXiv)
- Fool's Gold: Defensive Deception Against Safety-Removal Attacks on Open-Weight Models (arXiv)
- Deception by Omission: Language Models Knowingly Hide Their Mistakes (arXiv)
- Caught in the Act: Probes Effectively Detect Sabotage and Catch Unverbalized Deception (arXiv)
- Cognitive Security as an AI Safety Cause Area (LW)
- Spurious probes as a black-box alternative to activation probing (LW)
- Prompt injection in Google Translate reveals base model behaviors behind task-specific fine-tuning (LW)
