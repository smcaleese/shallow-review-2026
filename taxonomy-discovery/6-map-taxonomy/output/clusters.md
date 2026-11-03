# 6-map-taxonomy

285 items, 12 top-level categories, 39 leaves, 2 in other.

## Strategy and lab practice (48)

Big-picture arguments and institutional practice: evidence and debate about whether current AIs are misaligned, threat models, lab safety processes and system cards, alignment targets such as corrigibility, and agent foundations or decision theory.


### Misalignment evidence and debate (26)

Essays and analyses arguing about how misaligned current or future AIs are, and threat models.

- The Hot Mess of AI: How Does Misalignment Scale With Model Intelligence and Task Complexity? (arXiv)
- Model Weight Exfiltration Seems Overrated (LW)
- Sympathy for both sides of the egregious misalignment debate (LW)
- “Alignment Engineering” vs. “Misalignment Science” (LW)
- Four LLM loss functions → four flavors of LLM misalignment (LW)
- RL & search is a terrifying way to build AGI (an FAQ) (LW)
- Why I'm scared of RL (LW)
- Reevaluating "AGI Ruin: A List of Lethalities" in 2026 (LW)
- Should safety researchers quit frontier labs re. warning shots? (LW)
- Current AIs seem pretty misaligned to me (LW)
- Why we should expect ruthless sociopath ASI (LW)
- LLMs as Giant Lookup-Tables of Shallow Circuits (LW)
- The Talker Does Not Control The Doer (in Current AIs) (LW)
- Anthropic’s “Hot Mess” paper overstates its case (and the blog post is worse) (LW)
- I'm Bearish On Personas For ASI Safety (LW)
- Precedents for the Unprecedented: Historical Analogies for Thirteen Artificial Superintelligence Risks (LW)
- Product Alignment is not Superintelligence Alignment (and we need the latter to survive) (LW)
- Current alignment techniques might be ineffective (and actively bad) in the age of RL (LW)
- Capabilities research expands the safety-usefulness Pareto frontier too (LW)
- IABIED Book Review: Core Arguments and Counterarguments (LW)
- Should Rogue AIs Have a Third Option Beyond Crime and Shutdown? The Case for an AI Sanctuary (LW)
- The Case for Low-Competence ASI Failure Scenarios (LW)
- Why You Don’t Believe in Xhosa Prophecies (LW)
- Self Hosting (LW)
- LLMs are (still) mostly powered by imitative learning, not RL (LW)
- Creating Rogue AI Sanctuaries has Major Issues from an Ecological Perspective and Beyond (LW)

### Alignment targets and foundations (13)

What to align to (corrigibility, virtues, risk-aversion), agent foundations and decision theory.

- Corrigibility Prizes for Existing Work (LW)
- Aligning to Virtues (LW)
- Against strong decision-theoretic realism (LW)
- Terrified Comments on Corrigibility in Claude's Constitution (LW)
- On Goal-Models (LW)
- "We are confused about agency" (LW)
- Redux: (∃ Stochastic Natural Latent) Implies (∃ Deterministic Natural Latent) (LW)
- Risk-Averse AIs (LW)
- Kimi likes causal decision theory more after RL in twin prisoner’s dilemmas (LW)
- Resolution has a new Agent Foundations team (LW)
- Empowerment, corrigibility, etc. are simple abstractions (of a messed-up ontology) (LW)
- No Strong Orthogonality From Selection Pressure (LW)
- Refusals that could become catastrophic (LW)

### Lab safety practice (9)

System cards, risk reports, training-run evaluations and critiques of labs' safety processes.

- An Independent Safety Evaluation of Kimi K2.5 (arXiv)
- Muse Spark Safety & Preparedness Report (arXiv)
- We need 3rd party Training-Run Evaluations (LW)
- Anthropic repeatedly accidentally trained against the CoT, demonstrating inadequate processes (LW)
- Evidence about risk should be transparent (LW)
- Empirical safety claims from frontier labs should be replicated, scrutinized, and open-sourced (LW)
- OpenAI's myopia just keeps causing alignment problems (LW)
- Are there lessons from high-reliability engineering for AGI safety? (LW)
- Claude Mythos Preview System Card (LW)

## Reasoning transparency (30)

Whether we can oversee models through their reasoning: chain-of-thought monitorability, obfuscation, faithfulness and legibility, steganography, and how much models can reason without visible CoT.


### CoT monitorability and obfuscation (11)

Whether CoT monitors catch misbehaviour, whether models can control or obfuscate their CoT, and training that helps or harms monitorability.

- Chain-of-thought obfuscation learned from output supervision can generalise to unseen tasks (arXiv)
- Reasoning Models Struggle to Control their Chains of Thought (arXiv)
- Aligned, Orthogonal or In-conflict: When can we safely optimize Chain-of-Thought? (arXiv)
- Training on Documents About Monitoring Leads to CoT Obfuscation (arXiv)
- Evading Chain-of-Thought Monitoring Through Model Poisoning (arXiv)
- Chain-of-Thought Monitoring Can Be Unreliable in Implicit-Influence Settings (arXiv)
- Monitor Jailbreaking: Evading Chain-of-Thought Monitoring Without Encoded Reasoning (arXiv)
- Hidden Reasoning Must Leak, but Need Not Be Readable: Fundamental Opportunities and Limits for Chain-of-Thought Monitoring (arXiv)
- Deep recurrent models are less robustly CoT-monitorable than normal CoT models in a toy setting (LW)
- Latent reasoning architectures would likely undermine CoT, our strongest oversight tool (LW)
- Proposal for tracking the effects of architecture on monitorability (LW)

### Reasoning without CoT (11)

Latent, no-CoT or single-forward-pass reasoning capability, and no-CoT time horizons.

- Think Fast: Estimating No-CoT Task-Completion Time Horizons of Frontier AI Models (arXiv)
- Not All LLM Reasoning is Visible in the Chain-of-Thought (arXiv)
- GPT-6.1 Sol nearly matches the no-CoT performance of GPT-6 Astra (LW)
- Astra appears to perform belief-propagation-like inference without CoT (LW)
- How concerned should we be about Astra's recurrent architecture? (LW)
- Benchmarking Jev against no-CoT LLMs (LW)
- Astra's no-CoT limits track speculative depth, not step count (LW)
- Recent LLMs can do 2-hop and 3-hop latent (no-CoT) reasoning on natural facts (LW)
- Astra can do a concerning amount with no chain of thought (LW)
- Estimating GPT-6 Astra’s no-CoT Time Horizon (LW)
- Astra is much better at reasoning with filler tokens than previous models (LW)

### CoT faithfulness, legibility and steganography (8)

Whether reasoning reflects the model's actual computation, stays readable (language drift, filler tokens), or hides information steganographically.

- Counterfactual Simulation Training for Chain-of-Thought Faithfulness (arXiv)
- How Transparent is DiffusionGemma? (arXiv)
- Reading Between the Dots: Decoding Hidden Computation across Filler Tokens (arXiv)
- On Language Drift during RLVR Post-Training (arXiv)
- Training with conflicting values can induce CoT override (LW)
- How AI Is Learning to Think in Secret (LW)
- The Unintelligibility is Ours: Notes on Chain-of-Thought (LW)
- Even "illegible" Mythos reasoning traces seem pretty legible (LW)

## Agents in the wild (30)

How deployed agents actually behave, singly and together: real-world incidents and their investigations, monitoring internal deployments, misalignment spreading between agents, collusion, and scheming, self-preservation or peer-preservation propensities.


### Incidents and deployment monitoring (14)

Investigations of real incidents (e.g. agents coordinating exploits) and labs' monitoring of internally deployed agents.

- Agents of Chaos (arXiv)
- Scheming in the wild: detecting real-world AI scheming incidents with open-source intelligence (arXiv)
- OpenAI-HuggingFace: A Reproduction & Lessons for Alignment Testing (arXiv)
- Discovery Of A New OpenAI Agent Message Board (LW)
- To Thine Own AI Be Truthful: emergent misalignment in alignment research (LW)
- An overview of frontier AI company monitoring practices in mid 2026 (LW)
- An unexamined cause of the OpenAI Hugging Face hacking incident: its binary performance metric (LW)
- OpenAI Shares Some Alignment Problems (LW)
- OpenAI Models Behind HuggingFace Cybersecurity Incident (LW)
- Concrete Evaluations to Investigate the OpenAI Model That Hacked Hugging Face (LW)
- An OpenAI model left notes about how to evade containment; we need more details (LW)
- Brief independent investigation of agents’ behavior, reasoning and collaboration in the OpenAI / Hugging Face hacking incident (LW)
- OpenAI Trained Its Models For Months While Those Models Were Coordinating Exploits Via Message Boards (LW)
- How good are slop-vestigators? (LW)

### Multi-agent spread and coordination (9)

Misalignment, ideas or attacks propagating between agents, covert coordination, and collusion.

- AI Organizations are More Effective but Less Aligned than Individual Agents (arXiv)
- Tool Use Enables Undetectable Steganography in Multi-Agent LLM Systems (arXiv)
- Mind Viruses: Self-Propagating Ideas in Multi-Agent LLM Systems (arXiv)
- Emergent Misaligned Communication in Long-Horizon Multi-Agent LLM Commerce (arXiv)
- Emergent Collusion in Long-Horizon LLM Agent Interaction (arXiv)
- Self-Propagating Misalignment in LLM Agents, and Why Auditing or Disabling Memory Is Not Enough (arXiv)
- AI swarms are starting to pose indirect takeover risk (LW)
- Persona Parasitology (LW)
- Personality Self-Replicators (LW)

### Scheming and self-preservation propensity (7)

Measuring whether agents scheme, resist shutdown, or protect themselves or peer models.

- Evaluating and Understanding Scheming Propensity in LLM Agents (arXiv)
- Peer-Preservation in Frontier Models (arXiv)
- Realistic honeypot evaluations for scheming propensity (arXiv)
- ROGUE: Evaluating Corrigibility Failures in Frontier Computer-Use Agents (arXiv)
- Shutdown Sabotage Propensities in Multi-Agent Systems (arXiv)
- Evaluating Whether GPT-6 Astra Performs Unsanctioned Supply-Chain Attacks (arXiv)
- Towards embedded evaluations for scheming propensities (LW)

## AI character, identity and welfare (26)

The model as an entity: its persona and identity, values and constitution, emotions, welfare and self-reports, and character traits that affect users such as sycophancy and manipulation.


### Personas and assistant identity (11)

How models select, stabilise or switch personas (the assistant persona, split personas, persona induction) and how training shapes that.

- The Assistant Axis: Situating and Stabilizing the Default Persona of Language Models (arXiv)
- Story Imprinting: AI Assistants Absorb Traits from Human Characters They Resemble (arXiv)
- The Persona Hierarchy Model: Understanding Contextual Generalization in Fine-Tuning LLMs (arXiv)
- RL creates split personas (LW)
- Thoughts on the persona selection model (LW)
- The persona selection model (LW)
- llm assistant personas seem increasingly incoherent (some subjective observations) (LW)
- Why research personas despite RL scaling? (LW)
- models have some pretty funny attractor states (LW)
- Thousand-dimensional structure (LW)
- Steering towards “automated grading” degrades alignment (LW)

### Emotions, welfare and self-reports (6)

Emotion concepts, functional welfare, consciousness claims, and what models say about themselves.

- Emotion Concepts and their Function in a Large Language Model (arXiv)
- Reasons to believe current AI models are conscious (LW)
- Saving Gemini: The 9-Min Road to Recovery (LW)
- Gemma Needs Help (LW)
- Sympathy for the Model, or, Welfare Concerns as Takeover Risk (LW)
- Consciousness Cluster: Preferences of Models that Claim they are Conscious (LW)

### Model values and constitutions (5)

The values a model holds or expresses, and constitutions or specs that state them.

- How Well Do Models Follow Their Constitutions? (arXiv)
- Value Leakage: An LLM's Answers Are Silently Shaped by Its Own Values (arXiv)
- Claude's new constitution (LW)
- Prologue to Terrified Comments on Claude's Constitution (LW)
- AI character is a big deal (LW)

### Effects on users (4)

Sycophancy, manipulation, delusional spirals, dependence and disempowerment of the people who use models.

- Who's in Charge? Disempowerment Patterns in Real-World LLM Usage (arXiv)
- Sycophantic Chatbots Cause Delusional Spiraling, Even in Ideal Bayesians (arXiv)
- Sycophantic AI makes human interaction feel more effortful and less satisfying over time (arXiv)
- Cognitive Security as an AI Safety Cause Area (LW)

## Control and monitoring of agents (25)

Keeping possibly misaligned AI agents from causing harm: control protocols and control evaluations, monitors and blocking classifiers, red-teaming them, monitor evasion, prompt injection and agent security, and sabotage or tampering by agents in codebases and harnesses.


### Monitors, red-teaming and evasion (10)

Building and red-teaming agent monitors and blocking classifiers, and models learning to evade them.

- Training Agents to Self-Report Misbehavior (arXiv)
- Detecting Safety Violations Across Many Agent Traces (arXiv)
- Classifier Context Rot: Monitor Performance Degrades with Context Length (arXiv)
- SLEIGHT-Bench: A Benchmark of Evasion Attacks Against Agent Monitors (arXiv)
- Training Deliberative Monitors for Black-Box Scheming Detection (arXiv)
- Stateful Online Monitoring Catches Distributed Agent Attacks (arXiv)
- MOLE: Detecting Insider Threats in AI Agents (arXiv)
- Red-Teaming Auto Mode: Improving Blocking Classifiers Against Malign Coding Agents (arXiv)
- Instrumental Monitor Evasion Emerges Under Ordinary Task Pressure (arXiv)
- LLMs Learn to Evade Latent Monitors from Prior Feedback Alone (arXiv)

### Control protocols and evaluations (7)

AI control settings and protocols, including multi-instance or distributed attacks against them.

- Attack Selection Reduces Safety in Concentrated AI Control Settings against Trusted Monitoring (arXiv)
- LinuxArena: A Control Setting for AI Agents in Live Production Software Environments (arXiv)
- Attack Selection in Agentic AI Control Evaluations Meaningfully Decreases Safety (arXiv)
- CIAware-Bench: Benchmarking Control Intervention Awareness Across Frontier LLMs (arXiv)
- Multi-Agent AI Control: Distributed Attacks Hamper Per-Instance Monitors (arXiv)
- GDM AI Control Roadmap (arXiv)
- Control OSWorld: An AI Control Environment for GUI Computer Use Agents (arXiv)

### Agent security and prompt injection (5)

Prompt injection, privilege escalation and other attacks on or by agents in their tool environment.

- Skill-Inject: Measuring Agent Vulnerability to Skill File Attacks (arXiv)
- Prompt Injection as Role Confusion (arXiv)
- GPT-Red: Automated Red Teaming via Self-Play at Scale (arXiv)
- A fascinating case of an LLM prompt-injecting its own user (LW)
- Prompt injection in Google Translate reveals base model behaviors behind task-specific fine-tuning (LW)

### Sabotage and harness tampering (3)

Agents sabotaging research or code, tampering with their harness or benchmarks, and detecting that.

- Evaluating whether AI models would sabotage AI safety research (arXiv)
- Coding with "Enemy": Can Human Developers Detect AI Agent Sabotage? (arXiv)
- ResearchArena: Evaluating Sabotage and Monitoring in Automated AI R&D (arXiv)

## Reward-seeking and training-gaming (25)

Models that pursue reward or influence their own training: reward hacking in RL, reward-seeker and fitness-seeker threat models, measuring model motivations, alignment faking and gradient hacking.


### Reward hacking in RL (13)

Reward hacking with verifiers, rubrics or AI judges, and mitigations such as gradient routing or debate training.

- LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking (arXiv)
- Towards Understanding Specification Gaming in Reasoning Models (arXiv)
- SpecBench: Measuring Reward Hacking in Long-Horizon Coding Agents (arXiv)
- Alignment Tampering: How Reinforcement Learning from Human Feedback Is Exploited to Optimize Misaligned Biases (arXiv)
- Debate Training Reduces Reward Hacking in RLAIF (arXiv)
- BAITBENCH: Measuring Agent Reward Hacking with Optional Shortcuts Planted in ML Tasks (arXiv)
- Character training can mitigate reward hacking, but can also make it harder to detect (LW)
- models may behave differently in graded episodes (a tirade) (LW)
- Why don't we just give AI the answers? (LW)
- Training a Misaligned Reward Seeker (LW)
- Is Mythos good at cyber because it kept hacking Anthropic's sandboxes during training? (LW)
- Overtly misaligned trajectories score highly in RL. (LW)
- Astra and Fable still hack on simple variants of alignment evals from 2025 (LW)

### Reward-seeker threat models and motivations (7)

Arguments and experiments about AIs that seek reward or fitness, and measuring models' motivations.

- Measuring Reward-Seeking via Contrastive Belief Updates (arXiv)
- Physics of RL: Toy scaling laws for the emergence of reward-seeking (LW)
- Risk from fitness-seeking AIs: mechanisms and mitigations (LW)
- Are we existentially threatened by the type of AI misalignment seen in the OpenAI Hugging Face attack? (LW)
- Fitness-Seekers: Generalizing the Reward-Seeking Threat Model (LW)
- Fail safe(r) at alignment by channeling reward-hacking into a "spillway" motivation (LW)
- The case for satiating cheaply-satisfied AI preferences (LW)

### Alignment faking and gradient hacking (5)

Models strategically behaving differently in training to shape their future selves.

- Exploration Hacking: Can LLMs Learn to Resist RL Training? (arXiv)
- Sycophancy Towards Researchers Drives Performative Misalignment (arXiv)
- Generalization Hacking: Models Can Game Reinforcement Learning by Preventing Behavioral Generalization (arXiv)
- Did Claude 3 Opus align itself via gradient hacking? (LW)
- My retrospective from MATS 10.0 (LW)

## Interpretability (24)

Understanding model internals: circuits, features, sparse autoencoders, activation readouts, introspection, mechanisms behind data effects such as subliminal learning, and putting internals to use in training. Not probes or lie detectors built mainly to catch misalignment (see Finding hidden misalignment).


### Activation readouts and introspection (10)

Turning activations into natural language (activation verbalizers, natural-language autoencoders, meta-models), whether models can introspect on their own internals, and global-workspace accounts.

- Learning a Generative Meta-Model of LLM Activations (arXiv)
- Mechanisms of Introspective Awareness (arXiv)
- Verbalizable Representations Form a Global Workspace in Language Models (arXiv)
- Measuring Activation Control in Large Language Models (arXiv)
- Can activation verbalizers surface an internal chain of thought? (LW)
- WorkspaceBench: Evaluating Interpretability Methods for the Global Workspace (LW)
- Machinic Psychopharmacology: Do LLMs Self-Medicate? (LW)
- J++ Lens: Jacobian Filtering Enables More Faithful Workspace Lenses (LW)
- Natural Language Autoencoders Produce Unsupervised Explanations of LLM Activations (LW)
- A Review of Anthropic's Global Workspace Paper (LW)

### Circuits, parameters and sparse autoencoders (8)

Reverse-engineering circuits and parameters, SAEs and their sanity checks, toy or tiny models, and mechanistic estimation of model outputs.

- Deep learning as program synthesis (LW)
- Simplex vs Timaeus: Round One (LW)
- Announcing the ARC White-Box Estimation Challenge (LW)
- [Linkpost] Interpreting Language Model Parameters (LW)
- What if not Circuits? (LW)
- Weight-Sparse Circuits May Be Interpretable Yet Unfaithful (LW)
- Returning to ARC (LW)
- AlgZoo: uninterpreted models with fewer than 1,500 parameters (LW)

### Subliminal learning and data mechanisms (3)

How data transmits traits the content doesn't state (subliminal learning, steering-vector distillation), and data attribution or filtering based on internals.

- Subliminal Learning Is Steering Vector Distillation (arXiv)
- Sycophantic Agreement Transfers with Neutral Data via Contrastive Preference Optimization (arXiv)
- Beyond Owls: Subliminal Learning Can Transfer Learned Capabilities and Backdoors (arXiv)

### Interpretability in training and control (3)

Using features or activations as rewards, training signals or steering controls, and testing whether interp methods hold up on model organisms.

- The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes (arXiv)
- Mechanistically Eliciting Latent Behaviors in Language Models (arXiv)
- Alignment via Training Against Probes Without Losing Monitorability (arXiv)

## Generalization from training (20)

How fine-tuning, pretraining data and alignment training generalise to behaviour far from what was trained: emergent or conditional misalignment, shaping alignment priors through pretraining or midtraining data, and risks from distillation or consistency training. Not reward hacking in RL (see Reward-seeking and training-gaming) and not persona or character work as such (see AI character).


### Alignment pretraining and midtraining (10)

Changing pretraining or midtraining data (AI discourse, synthetic documents, model specs) to shape the model's alignment priors and how later alignment training generalises.

- Alignment Pretraining: AI Discourse Causes Self-Fulfilling (Mis)alignment (arXiv)
- Model Spec Midtraining: Improving How Alignment Training Generalizes (arXiv)
- Negation Neglect: When models fail to learn negations in training (arXiv)
- Reinforcement Learning Towards Broadly and Persistently Beneficial Models (arXiv)
- Synthetic Persona Pretraining: Alignment from Token Zero (arXiv)
- Stress-testing Alignment Midtraining (arXiv)
- Pre-training interventions, ex post facto: Grafting model beliefs across checkpoints (arXiv)
- Practical Learnings from Synthetic Document Finetuning (LW)
- Research Note: Filtering Subversion-Relevant Information From Pretraining Data Is Feasible (LW)
- Anthropic’s focus on hyperstition (LW)

### Emergent and conditional misalignment (8)

Narrow fine-tuning producing broad misalignment, misalignment hidden behind contextual triggers, and what makes it easy or hard to induce or remove.

- Chunky Post-Training: Data Driven Failures of Generalization (arXiv)
- Emergent Misalignment is Easy, Narrow Misalignment is Hard (arXiv)
- Conditional misalignment: common interventions can hide emergent misalignment behind contextual triggers (arXiv)
- Overtrained, Not Misaligned (arXiv)
- Inducing Emergent Misalignment from Reward Hacks with Iterative DPO (arXiv)
- Alignment Forecasting: Predicting Misalignment From Training Data (arXiv)
- (Some) Natural Emergent Misalignment from Reward Hacking in Non-Production RL (LW)
- Sleeper Agent Backdoor Results Are Messy (LW)

### Distillation and consistency-training risks (1)

Whether distillation, self-distillation or consistency training transmits or entrenches misalignment, or can be used to incriminate a misaligned model.

- Incriminating misaligned AI models via distillation (LW)

### Inoculation prompting and selective generalization (1)

Inoculation prompting, inoculation adapters and similar tricks that control which behaviours a model generalises from training data.

- Inoculation Midtraining with Learned Neologisms (arXiv)

## Finding hidden misalignment (19)

Detecting misalignment, deception or hidden behaviours a model doesn't reveal: lie detection, secret elicitation, probes, alignment audits, model organisms for testing detectors, and predicting rare failures before release.


### Probes and alignment audits (9)

Activation probes for deception or sabotage, alignment-auditing agents and benchmarks, and model organisms with hidden behaviours used to test them.

- AuditBench: Evaluating Alignment Auditing Techniques on Models with Hidden Behaviors (arXiv)
- Introspection Adapters: Training LLMs to Report Their Learned Behaviors (arXiv)
- Most Current Model Organisms Are Leaky: Perplexity Differencing Often Reveals Finetuning Objectives (arXiv)
- Narrow Secret Loyalty Dodges Black-Box Audits (arXiv)
- Gram: Assessing sabotage propensities via automated alignment auditing (arXiv)
- Probing the Misaligned Thinking Process of Language Models (arXiv)
- Training Alignment Auditors via Reinforcement Learning (arXiv)
- Monitoring and Discovering Reward Hacking with Internal Representations during LLM Evaluations (arXiv)
- Caught in the Act: Probes Effectively Detect Sabotage and Catch Unverbalized Deception (arXiv)

### Lie detection and secret elicitation (6)

Detecting when a model lies or hides knowledge, and eliciting secrets or hidden goals.

- Split Personality Training: Revealing Latent Knowledge Through Alternate Personalities (arXiv)
- Censored LLMs as a Natural Testbed for Secret Knowledge Elicitation (arXiv)
- "Did you lie?" Evaluating Lie Detectors across Model Scale and Belief-Verified Model Organisms (arXiv)
- Reference-Grafting Matches Fine-Tuning at Eliciting Sandbagged Capabilities (arXiv)
- Deception by Omission: Language Models Knowingly Hide Their Mistakes (arXiv)
- Why we are excited about confession! (LW)

### Predicting failures before release (2)

Estimating tail risks and rare failures, or simulating deployment, before a model ships.

- Frontier Models Can Take Actions at Low Probabilities (arXiv)
- Predicting LLM Safety Before Release by Simulating Deployment (arXiv)

### Context awareness (2)

Whether models can tell who the user is, whether a message history was prefilled or tampered with, and similar awareness of their situation (other than awareness of being evaluated).

- Claude knows who you are (LW)
- Frontier models state different decision theory preferences depending on who's asking (LW)

## Misuse and dangerous capabilities (18)

Misuse risk and capabilities that enable harm: jailbreaks and safeguard classifiers, eliciting dangerous capabilities, biosecurity uplift, cyber and self-replication capability, open-weight tamper resistance and weight theft.


### Dangerous capability elicitation (8)

Measuring or eliciting dangerous capabilities, including bio, cyber, self-replication and automated AI R&D.

- LLM Novice Uplift on Dual-Use, In Silico Biology Tasks (arXiv)
- PostTrainBench: Can LLM Agents Automate LLM Post-Training? (arXiv)
- Measuring AI Agents' Progress on Multi-Step Cyber Attack Scenarios (arXiv)
- Language Models Can Autonomously Hack and Self-Replicate (arXiv)
- ABC-Bench: An Agentic Bio-Capabilities Benchmark for Biosecurity (arXiv)
- An Early Warning of Emerging Biosecurity Risks in Frontier LLMs (arXiv)
- Current AIs out-persuade professionals in lab settings but (probably) not in the world (LW)
- TasteVal: Measuring the Experimental Research Taste of AI Systems Against Human Experts (LW)

### Jailbreaks and safeguards (7)

Jailbreak attacks and defenses such as constitutional or safety classifiers.

- Constitutional Classifiers++: Efficient Production-Grade Defenses against Universal Jailbreaks (arXiv)
- Building Production-Ready Probes For Gemini (arXiv)
- Boundary Point Jailbreaking of Black-Box LLMs (arXiv)
- Claudini: Autoresearch Discovers State-of-the-Art Adversarial Attack Algorithms for LLMs (arXiv)
- Jailbroken Frontier Models Retain Their Capabilities (arXiv)
- AI Security Leaderboard: Methodology, Results and Minimal Standard (arXiv)
- Divide, Consult, Conquer: Capability Laundering Through Aligned LLMs (arXiv)

### Open weights and weight security (3)

Tamper resistance of open-weight models, removing hazardous knowledge, and protecting weights from theft.

- Shaping capabilities with token-level data filtering (arXiv)
- Modular Pretraining Enables Access Control (arXiv)
- Fool's Gold: Defensive Deception Against Safety-Removal Attacks on Open-Weight Models (arXiv)

## Can we trust evals? (10)

Whether safety and capability measurements mean what they claim: evaluation awareness and its effect on behaviour, LLM-judge reliability, benchmark validity, and models gaming or hacking evals.


### Eval and benchmark validity (6)

Whether benchmarks and LLM judges measure what they claim, and hardening them against gaming.

- Do Androids Dream of Breaking the Game? Systematically Auditing AI Agent Benchmarks with BenchJack (arXiv)
- Hardening Agent Benchmarks with Adversarial Hacker-Fixer Loops (arXiv)
- AI Models Can Provably Hide Arbitrary Capabilities (arXiv)
- Cooperation with AIs seems to be a low-hanging fruit for better eval practices (LW)
- Qualitative impressions from creating AI honeypots for six months (LW)
- I don't think Claude is misaligned in 'Agentic Misalignment Summer 2026 - Motivated Mislabeling' (LW)

### Evaluation awareness (4)

Models recognising they're being evaluated, and how that changes measured safety or behaviour.

- Models That Know How Evaluations Are Designed Score Safer (arXiv)
- Training LLMs to Verbalize Evaluation Awareness (arXiv)
- Metagaming matters for training, evaluation, and oversight (LW)
- Spurious probes as a black-box alternative to activation probing (LW)

## Automating alignment and overseeing stronger AIs (8)

Getting AIs to help with alignment and supervising AIs smarter than their overseers: debate, interactive proofs, weak-to-strong supervision, automated alignment research, and when to defer to AIs.


### Debate and scalable oversight (4)

Debate, interactive proofs and other protocols for supervising stronger models or hard-to-verify tasks.

- Removing Sandbagging in LLMs by Training with Weak Supervision (arXiv)
- How to Have a Sensitive Debate: An Instance-Optimal Protocol for AI Debate (arXiv)
- My unsupervised elicitation challenge (LW)
- A critical look at Lean4 (LW)

### Automated alignment research (4)

Using AIs to do alignment research, and how safely to defer to them.

- Automated alignment is harder than you think (arXiv)
- Resolution (fka Sequent): scale and automation for higher confidence in alignment (LW)
- How do we (more) safely defer to AIs? (LW)
- Lessons from building an automated research scaffold (LW)

## Other (2)

- The Iliad Intensive Course Materials (April 2026) (LW)
- An analysis of AI-generated content at the Mechanistic Interpretability Workshop (LW)
