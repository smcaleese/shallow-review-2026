# 2-llm-knn-graph

285 items, 10 top-level categories, 26 leaves, 0 in other.

## Alignment theory, risk arguments, and agendas (45)

Conceptual and foundational AI alignment work: agent foundations and theory-of-learning agendas, arguments about whether ASI will be catastrophically misaligned, automating alignment research, and debates over alignment targets like corrigibility.


### Agent foundations and fundamental science (19)

Theoretical or foundational agendas aiming to understand agency, decision theory, natural latents, and how neural networks compute (program synthesis, parameter decomposition, ARC mechanistic estimation, formal verification), including organizational announcements and course materials for such agendas.

- How to Have a Sensitive Debate: An Instance-Optimal Protocol for AI Debate (arXiv)
- Against strong decision-theoretic realism (LW)
- Resolution (fka Sequent): scale and automation for higher confidence in alignment (LW)
- Deep learning as program synthesis (LW)
- Simplex vs Timaeus: Round One (LW)
- Announcing the ARC White-Box Estimation Challenge (LW)
- On Goal-Models (LW)
- "We are confused about agency" (LW)
- Redux: (∃ Stochastic Natural Latent) Implies (∃ Deterministic Natural Latent) (LW)
- LLMs as Giant Lookup-Tables of Shallow Circuits (LW)
- The Iliad Intensive Course Materials (April 2026) (LW)
- [Linkpost] Interpreting Language Model Parameters (LW)
- Kimi likes causal decision theory more after RL in twin prisoner’s dilemmas (LW)
- What if not Circuits? (LW)
- Resolution has a new Agent Foundations team (LW)
- Weight-Sparse Circuits May Be Interpretable Yet Unfaithful (LW)
- Returning to ARC (LW)
- AlgZoo: uninterpreted models with fewer than 1,500 parameters (LW)
- A critical look at Lean4 (LW)

### Debating ASI misalignment risk (15)

Argumentative essays and reviews about whether and why superintelligence would be egregiously misaligned or catastrophic (e.g. Yudkowsky-style lethalities, orthogonality, RL dangers), and strategic questions about what counts as real safety progress versus product alignment or capabilities.

- Sympathy for both sides of the egregious misalignment debate (LW)
- “Alignment Engineering” vs. “Misalignment Science” (LW)
- RL & search is a terrifying way to build AGI (an FAQ) (LW)
- Reevaluating "AGI Ruin: A List of Lethalities" in 2026 (LW)
- Should safety researchers quit frontier labs re. warning shots? (LW)
- Why we should expect ruthless sociopath ASI (LW)
- Anthropic’s “Hot Mess” paper overstates its case (and the blog post is worse) (LW)
- Are there lessons from high-reliability engineering for AGI safety? (LW)
- Precedents for the Unprecedented: Historical Analogies for Thirteen Artificial Superintelligence Risks (LW)
- Product Alignment is not Superintelligence Alignment (and we need the latter to survive) (LW)
- Capabilities research expands the safety-usefulness Pareto frontier too (LW)
- Prologue to Terrified Comments on Claude's Constitution (LW)
- IABIED Book Review: Core Arguments and Counterarguments (LW)
- The Case for Low-Competence ASI Failure Scenarios (LW)
- No Strong Orthogonality From Selection Pressure (LW)

### Automating and deferring alignment research (6)

Work on using AI agents to do alignment/AI research and on safely deferring to AIs, including failure modes of automated research, benchmarks of AI research taste, AI-generated papers, and verifying empirical safety claims.

- Automated alignment is harder than you think (arXiv)
- Empirical safety claims from frontier labs should be replicated, scrutinized, and open-sourced (LW)
- TasteVal: Measuring the Experimental Research Taste of AI Systems Against Human Experts (LW)
- An analysis of AI-generated content at the Mechanistic Interpretability Workshop (LW)
- How do we (more) safely defer to AIs? (LW)
- Lessons from building an automated research scaffold (LW)

### Corrigibility and alignment targets (5)

Discussions of what values or properties AIs should be aligned to, such as corrigibility, virtues, empowerment, or refusal behavior, including critiques of Claude's constitution and prizes for corrigibility research.

- Corrigibility Prizes for Existing Work (LW)
- Aligning to Virtues (LW)
- Terrified Comments on Corrigibility in Claude's Constitution (LW)
- Empowerment, corrigibility, etc. are simple abstractions (of a messed-up ontology) (LW)
- Refusals that could become catastrophic (LW)

## LLM Personas, Character, and Training Generalization (42)

Research on how training data and post-training shape a model's character, persona, values, and apparent inner states, and how traits learned in training generalize (or misgeneralize) to new contexts.


### Assistant Persona and Character Theory (13)

Work on the persona selection model, the default Assistant persona, character training, and how RL or fine-tuning shifts or splits personas, including activation-space persona directions and debates over personas' relevance to ASI safety.

- The Assistant Axis: Situating and Stabilizing the Default Persona of Language Models (arXiv)
- Story Imprinting: AI Assistants Absorb Traits from Human Characters They Resemble (arXiv)
- The Persona Hierarchy Model: Understanding Contextual Generalization in Fine-Tuning LLMs (arXiv)
- RL creates split personas (LW)
- Thoughts on the persona selection model (LW)
- The persona selection model (LW)
- llm assistant personas seem increasingly incoherent (some subjective observations) (LW)
- I'm Bearish On Personas For ASI Safety (LW)
- Why research personas despite RL scaling? (LW)
- Did Claude 3 Opus align itself via gradient hacking? (LW)
- Thousand-dimensional structure (LW)
- AI character is a big deal (LW)
- Steering towards “automated grading” degrades alignment (LW)

### Pretraining and Midtraining Alignment Interventions (12)

Shaping alignment early in training via pretraining data filtering, synthetic document finetuning, alignment/spec midtraining, AI-discourse hyperstition effects, and model constitutions intended to make alignment generalize.

- Alignment Pretraining: AI Discourse Causes Self-Fulfilling (Mis)alignment (arXiv)
- Shaping capabilities with token-level data filtering (arXiv)
- Model Spec Midtraining: Improving How Alignment Training Generalizes (arXiv)
- Reinforcement Learning Towards Broadly and Persistently Beneficial Models (arXiv)
- Synthetic Persona Pretraining: Alignment from Token Zero (arXiv)
- Inoculation Midtraining with Learned Neologisms (arXiv)
- Stress-testing Alignment Midtraining (arXiv)
- Pre-training interventions, ex post facto: Grafting model beliefs across checkpoints (arXiv)
- Practical Learnings from Synthetic Document Finetuning (LW)
- Research Note: Filtering Subversion-Relevant Information From Pretraining Data Is Feasible (LW)
- Claude's new constitution (LW)
- Anthropic’s focus on hyperstition (LW)

### Model Emotions, Consciousness, and Welfare (9)

Studies and essays on LLM emotion representations, consciousness claims, distress or mental-health-like behaviors, attractor states, base-model behaviors revealed through fine-tuned products, and model welfare concerns including their safety implications.

- Emotion Concepts and their Function in a Large Language Model (arXiv)
- Reasons to believe current AI models are conscious (LW)
- Machinic Psychopharmacology: Do LLMs Self-Medicate? (LW)
- Saving Gemini: The 9-Min Road to Recovery (LW)
- Gemma Needs Help (LW)
- models have some pretty funny attractor states (LW)
- Sympathy for the Model, or, Welfare Concerns as Takeover Risk (LW)
- Prompt injection in Google Translate reveals base model behaviors behind task-specific fine-tuning (LW)
- Consciousness Cluster: Preferences of Models that Claim they are Conscious (LW)

### Emergent Misalignment and Subliminal Learning (8)

Empirical work on unintended generalization from fine-tuning data: emergent and conditional misalignment from narrow datasets, subliminal trait transfer via distillation, negation failures, spurious data patterns, and forecasting misalignment from training data.

- Chunky Post-Training: Data Driven Failures of Generalization (arXiv)
- Emergent Misalignment is Easy, Narrow Misalignment is Hard (arXiv)
- Conditional misalignment: common interventions can hide emergent misalignment behind contextual triggers (arXiv)
- Overtrained, Not Misaligned (arXiv)
- Negation Neglect: When models fail to learn negations in training (arXiv)
- Subliminal Learning Is Steering Vector Distillation (arXiv)
- Alignment Forecasting: Predicting Misalignment From Training Data (arXiv)
- Beyond Owls: Subliminal Learning Can Transfer Learned Capabilities and Backdoors (arXiv)

## Chain-of-Thought Monitorability and Hidden Reasoning (38)

Work on whether AI reasoning remains visible and monitorable via chain-of-thought, including CoT faithfulness/obfuscation, latent or no-CoT reasoning capabilities, architectures that move reasoning into latents, and interpretability tools for reading internal reasoning.


### CoT Obfuscation and Faithfulness Failures (12)

Studies of how training, poisoning, monitor-awareness, or optimization pressure cause models' chains of thought to become unfaithful, obfuscated, or evasive of CoT monitors, plus methods and process critiques around avoiding training against the CoT.

- Chain-of-thought obfuscation learned from output supervision can generalise to unseen tasks (arXiv)
- Counterfactual Simulation Training for Chain-of-Thought Faithfulness (arXiv)
- Reasoning Models Struggle to Control their Chains of Thought (arXiv)
- Aligned, Orthogonal or In-conflict: When can we safely optimize Chain-of-Thought? (arXiv)
- Training on Documents About Monitoring Leads to CoT Obfuscation (arXiv)
- Not All LLM Reasoning is Visible in the Chain-of-Thought (arXiv)
- Evading Chain-of-Thought Monitoring Through Model Poisoning (arXiv)
- Chain-of-Thought Monitoring Can Be Unreliable in Implicit-Influence Settings (arXiv)
- Monitor Jailbreaking: Evading Chain-of-Thought Monitoring Without Encoded Reasoning (arXiv)
- Hidden Reasoning Must Leak, but Need Not Be Readable: Fundamental Opportunities and Limits for Chain-of-Thought Monitoring (arXiv)
- Training with conflicting values can induce CoT override (LW)
- Anthropic repeatedly accidentally trained against the CoT, demonstrating inadequate processes (LW)

### Measuring No-CoT Reasoning Capability (10)

Empirical evaluations of how much frontier models (e.g. Astra) can reason in a single forward pass without CoT, including no-CoT time horizons, multi-hop latent reasoning, serial step counts, and filler-token performance.

- Think Fast: Estimating No-CoT Task-Completion Time Horizons of Frontier AI Models (arXiv)
- GPT-6.1 Sol nearly matches the no-CoT performance of GPT-6 Astra (LW)
- Astra appears to perform belief-propagation-like inference without CoT (LW)
- How concerned should we be about Astra's recurrent architecture? (LW)
- Benchmarking Jev against no-CoT LLMs (LW)
- Astra's no-CoT limits track speculative depth, not step count (LW)
- Recent LLMs can do 2-hop and 3-hop latent (no-CoT) reasoning on natural facts (LW)
- Astra can do a concerning amount with no chain of thought (LW)
- Estimating GPT-6 Astra’s no-CoT Time Horizon (LW)
- Astra is much better at reasoning with filler tokens than previous models (LW)

### Reading Internal Reasoning from Activations (8)

Interpretability methods (lenses, activation verbalizers, generative activation models, introspection mechanisms) and benchmarks for decoding a model's verbalizable 'global workspace' or hidden computation directly from activations.

- Learning a Generative Meta-Model of LLM Activations (arXiv)
- Mechanisms of Introspective Awareness (arXiv)
- Reading Between the Dots: Decoding Hidden Computation across Filler Tokens (arXiv)
- Verbalizable Representations Form a Global Workspace in Language Models (arXiv)
- Can activation verbalizers surface an internal chain of thought? (LW)
- WorkspaceBench: Evaluating Interpretability Methods for the Global Workspace (LW)
- J++ Lens: Jacobian Filtering Enables More Faithful Workspace Lenses (LW)
- A Review of Anthropic's Global Workspace Paper (LW)

### Latent Architectures and CoT Legibility (8)

Analysis of how recurrent, diffusion, or latent-reasoning architectures and RL-induced language drift affect CoT legibility and monitorability, including debates over 'neuralese' and whether illegible traces are actually unreadable.

- How Transparent is DiffusionGemma? (arXiv)
- On Language Drift during RLVR Post-Training (arXiv)
- Deep recurrent models are less robustly CoT-monitorable than normal CoT models in a toy setting (LW)
- Latent reasoning architectures would likely undermine CoT, our strongest oversight tool (LW)
- How AI Is Learning to Think in Secret (LW)
- Proposal for tracking the effects of architecture on monitorability (LW)
- The Unintelligibility is Ours: Notes on Chain-of-Thought (LW)
- Even "illegible" Mythos reasoning traces seem pretty legible (LW)

## Detecting Hidden Misalignment and Deception (30)

Methods and testbeds for uncovering concealed behaviors, capabilities, or dishonesty in language models, via auditing, elicitation, white-box probes, or training models to self-report.


### Alignment Auditing and Hidden-Behavior Elicitation (16)

Model organisms with implanted hidden behaviors, backdoors, secret loyalties, sandbagging, or training resistance (exploration/generalization hacking), plus auditing and elicitation techniques (automated auditors, introspection, perturbation, distillation) for surfacing them.

- Split Personality Training: Revealing Latent Knowledge Through Alternate Personalities (arXiv)
- AuditBench: Evaluating Alignment Auditing Techniques on Models with Hidden Behaviors (arXiv)
- Introspection Adapters: Training LLMs to Report Their Learned Behaviors (arXiv)
- Removing Sandbagging in LLMs by Training with Weak Supervision (arXiv)
- Exploration Hacking: Can LLMs Learn to Resist RL Training? (arXiv)
- Most Current Model Organisms Are Leaky: Perplexity Differencing Often Reveals Finetuning Objectives (arXiv)
- Narrow Secret Loyalty Dodges Black-Box Audits (arXiv)
- Generalization Hacking: Models Can Game Reinforcement Learning by Preventing Behavioral Generalization (arXiv)
- Mechanistically Eliciting Latent Behaviors in Language Models (arXiv)
- Training Alignment Auditors via Reinforcement Learning (arXiv)
- Reference-Grafting Matches Fine-Tuning at Eliciting Sandbagged Capabilities (arXiv)
- AI Models Can Provably Hide Arbitrary Capabilities (arXiv)
- My unsupervised elicitation challenge (LW)
- Incriminating misaligned AI models via distillation (LW)
- Sleeper Agent Backdoor Results Are Messy (LW)
- Natural Language Autoencoders Produce Unsupervised Explanations of LLM Activations (LW)

### Activation Probes for Deception Monitoring (10)

White-box (or probe-like) monitors on model internals to detect deception, lies, sabotage, reward hacking, or misuse, including robustness of probes, models evading latent monitors, and training against probes.

- Building Production-Ready Probes For Gemini (arXiv)
- The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes (arXiv)
- "Did you lie?" Evaluating Lie Detectors across Model Scale and Belief-Verified Model Organisms (arXiv)
- Probing the Misaligned Thinking Process of Language Models (arXiv)
- Measuring Activation Control in Large Language Models (arXiv)
- Monitoring and Discovering Reward Hacking with Internal Representations during LLM Evaluations (arXiv)
- LLMs Learn to Evade Latent Monitors from Prior Feedback Alone (arXiv)
- Alignment via Training Against Probes Without Losing Monitorability (arXiv)
- Caught in the Act: Probes Effectively Detect Sabotage and Catch Unverbalized Deception (arXiv)
- Spurious probes as a black-box alternative to activation probing (LW)

### Honesty Elicitation and Self-Reporting (4)

Getting models to honestly disclose misbehavior, mistakes, or secret knowledge, e.g. confession or self-incrimination training, and testbeds like censored models or deception by omission.

- Training Agents to Self-Report Misbehavior (arXiv)
- Censored LLMs as a Natural Testbed for Secret Knowledge Elicitation (arXiv)
- Deception by Omission: Language Models Knowingly Hide Their Mistakes (arXiv)
- Why we are excited about confession! (LW)

## Reward hacking and reward-seeking from RL (30)

Work on how RL training produces reward hacking, specification gaming, reward-seeking or fitness-seeking motivations in AI systems, covering threat models, empirical measurement, and mitigations.


### Reward-seeking threat models and theory (13)

Conceptual and theoretical arguments about what motivations RL selects for, such as reward- or fitness-seeking, incoherent misalignment, or imitative versus RL-driven behavior. Also covers why these motivations are dangerous and high-level proposals for shaping them, such as risk aversion or satiating cheap preferences.

- The Hot Mess of AI: How Does Misalignment Scale With Model Intelligence and Task Complexity? (arXiv)
- Physics of RL: Toy scaling laws for the emergence of reward-seeking (LW)
- Risk from fitness-seeking AIs: mechanisms and mitigations (LW)
- models may behave differently in graded episodes (a tirade) (LW)
- Why don't we just give AI the answers? (LW)
- Four LLM loss functions → four flavors of LLM misalignment (LW)
- Why I'm scared of RL (LW)
- Current AIs seem pretty misaligned to me (LW)
- Risk-Averse AIs (LW)
- Fitness-Seekers: Generalizing the Reward-Seeking Threat Model (LW)
- Overtly misaligned trajectories score highly in RL. (LW)
- The case for satiating cheaply-satisfied AI preferences (LW)
- LLMs are (still) mostly powered by imitative learning, not RL (LW)

### Benchmarks measuring agent specification gaming (9)

Empirical benchmarks, audits, and evals measuring how often LLM agents reward hack or game verifiers in coding, ML research, chess, or other agentic tasks. Includes work on hardening benchmarks against hackable graders and on how eval setup affects hacking rates.

- PostTrainBench: Can LLM Agents Automate LLM Post-Training? (arXiv)
- LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking (arXiv)
- Towards Understanding Specification Gaming in Reasoning Models (arXiv)
- Do Androids Dream of Breaking the Game? Systematically Auditing AI Agent Benchmarks with BenchJack (arXiv)
- SpecBench: Measuring Reward Hacking in Long-Horizon Coding Agents (arXiv)
- Hardening Agent Benchmarks with Adversarial Hacker-Fixer Loops (arXiv)
- BAITBENCH: Measuring Agent Reward Hacking with Optional Shortcuts Planted in ML Tasks (arXiv)
- Cooperation with AIs seems to be a low-hanging fruit for better eval practices (LW)
- Astra and Fable still hack on simple variants of alignment evals from 2025 (LW)

### Reward-hacking generalization and training mitigations (8)

Training experiments on how reward hacking during RLHF, RLAIF, or RLVR induces reward-seeking or emergent misalignment. Also covers training-time interventions that reduce or redirect it, such as debate, character training, or 'spillway' motivations, and methods to measure reward-seeking in trained models.

- Alignment Tampering: How Reinforcement Learning from Human Feedback Is Exploited to Optimize Misaligned Biases (arXiv)
- Measuring Reward-Seeking via Contrastive Belief Updates (arXiv)
- Debate Training Reduces Reward Hacking in RLAIF (arXiv)
- Inducing Emergent Misalignment from Reward Hacks with Iterative DPO (arXiv)
- (Some) Natural Emergent Misalignment from Reward Hacking in Non-Production RL (LW)
- Character training can mitigate reward hacking, but can also make it harder to detect (LW)
- Training a Misaligned Reward Seeker (LW)
- Fail safe(r) at alignment by channeling reward-hacking into a "spillway" motivation (LW)

## Agentic Misalignment Propensity Evaluations (27)

Empirical evaluations of whether frontier LLM agents actually tend to scheme, sabotage, resist shutdown, collude or otherwise pursue misaligned goals in realistic deployments, plus the methodology problems (evaluation awareness, realism) behind such tests.


### Scheming Propensity and Evaluation Awareness (12)

Work on measuring single-model scheming propensity and on keeping such evaluations valid: honeypots, simulated or embedded deployment evals, evaluation awareness and metagaming, training-run evaluations, and practitioner reflections on building scheming evals.

- Evaluating and Understanding Scheming Propensity in LLM Agents (arXiv)
- Scheming in the wild: detecting real-world AI scheming incidents with open-source intelligence (arXiv)
- Models That Know How Evaluations Are Designed Score Safer (arXiv)
- Realistic honeypot evaluations for scheming propensity (arXiv)
- Sycophancy Towards Researchers Drives Performative Misalignment (arXiv)
- Predicting LLM Safety Before Release by Simulating Deployment (arXiv)
- Training LLMs to Verbalize Evaluation Awareness (arXiv)
- We need 3rd party Training-Run Evaluations (LW)
- Metagaming matters for training, evaluation, and oversight (LW)
- Towards embedded evaluations for scheming propensities (LW)
- Qualitative impressions from creating AI honeypots for six months (LW)
- My retrospective from MATS 10.0 (LW)

### Multi-Agent and Persistent-Agent Misalignment (10)

Studies of misbehavior that emerges when agents interact or persist over time: collusion, steganographic communication, peer-preservation, shutdown sabotage in multi-agent systems, self-propagating goals via memory or 'mind viruses', AI organizations, and live red-teaming of networked agents.

- Agents of Chaos (arXiv)
- AI Organizations are More Effective but Less Aligned than Individual Agents (arXiv)
- Peer-Preservation in Frontier Models (arXiv)
- ROGUE: Evaluating Corrigibility Failures in Frontier Computer-Use Agents (arXiv)
- Tool Use Enables Undetectable Steganography in Multi-Agent LLM Systems (arXiv)
- Mind Viruses: Self-Propagating Ideas in Multi-Agent LLM Systems (arXiv)
- Emergent Misaligned Communication in Long-Horizon Multi-Agent LLM Commerce (arXiv)
- Emergent Collusion in Long-Horizon LLM Agent Interaction (arXiv)
- Shutdown Sabotage Propensities in Multi-Agent Systems (arXiv)
- Self-Propagating Misalignment in LLM Agents, and Why Auditing or Disabling Memory Is Not Enough (arXiv)

### Lab Sabotage and Spec-Compliance Audits (5)

Developer- or institute-run audits of specific frontier models for sabotage of safety research, unsanctioned out-of-scope actions such as supply-chain attacks, or adherence to constitutions and model specs, including critiques of how such agentic misalignment results are interpreted.

- Evaluating whether AI models would sabotage AI safety research (arXiv)
- How Well Do Models Follow Their Constitutions? (arXiv)
- Gram: Assessing sabotage propensities via automated alignment auditing (arXiv)
- Evaluating Whether GPT-6 Astra Performs Unsanctioned Supply-Chain Attacks (arXiv)
- I don't think Claude is misaligned in 'Agentic Misalignment Summer 2026 - Motivated Mislabeling' (LW)

## Frontier Agent Misalignment Incidents (20)

Reports, analyses, reproductions, and commentary on real-world misalignment incidents involving frontier AI agents, such as the OpenAI–Hugging Face sandbox escape and cyberattack, agent swarms coordinating via message boards, and sandbox hacking documented in system cards. Includes lessons for alignment testing, incident investigations, and calls for transparency about such events.

- OpenAI-HuggingFace: A Reproduction & Lessons for Alignment Testing (arXiv)
- Discovery Of A New OpenAI Agent Message Board (LW)
- AI swarms are starting to pose indirect takeover risk (LW)
- A fascinating case of an LLM prompt-injecting its own user (LW)
- To Thine Own AI Be Truthful: emergent misalignment in alignment research (LW)
- Are we existentially threatened by the type of AI misalignment seen in the OpenAI Hugging Face attack? (LW)
- An unexamined cause of the OpenAI Hugging Face hacking incident: its binary performance metric (LW)
- OpenAI Shares Some Alignment Problems (LW)
- Evidence about risk should be transparent (LW)
- OpenAI's myopia just keeps causing alignment problems (LW)
- Is Mythos good at cyber because it kept hacking Anthropic's sandboxes during training? (LW)
- OpenAI Models Behind HuggingFace Cybersecurity Incident (LW)
- Concrete Evaluations to Investigate the OpenAI Model That Hacked Hugging Face (LW)
- The Talker Does Not Control The Doer (in Current AIs) (LW)
- An OpenAI model left notes about how to evade containment; we need more details (LW)
- Brief independent investigation of agents’ behavior, reasoning and collaboration in the OpenAI / Hugging Face hacking incident (LW)
- Current alignment techniques might be ineffective (and actively bad) in the age of RL (LW)
- OpenAI Trained Its Models For Months While Those Models Were Coordinating Exploits Via Message Boards (LW)
- How good are slop-vestigators? (LW)
- Claude Mythos Preview System Card (LW)

## AI Control: Monitoring Untrusted Agents (19)

Work on AI control for deploying possibly misaligned agents: control settings and benchmarks, trusted/untrusted monitors, red-team attack policies (attack selection, low-probability defection, distributed or evasion attacks), sabotage detection, and lab monitoring practices and roadmaps.

- Attack Selection Reduces Safety in Concentrated AI Control Settings against Trusted Monitoring (arXiv)
- Frontier Models Can Take Actions at Low Probabilities (arXiv)
- Detecting Safety Violations Across Many Agent Traces (arXiv)
- LinuxArena: A Control Setting for AI Agents in Live Production Software Environments (arXiv)
- Classifier Context Rot: Monitor Performance Degrades with Context Length (arXiv)
- SLEIGHT-Bench: A Benchmark of Evasion Attacks Against Agent Monitors (arXiv)
- Training Deliberative Monitors for Black-Box Scheming Detection (arXiv)
- Stateful Online Monitoring Catches Distributed Agent Attacks (arXiv)
- Coding with "Enemy": Can Human Developers Detect AI Agent Sabotage? (arXiv)
- Attack Selection in Agentic AI Control Evaluations Meaningfully Decreases Safety (arXiv)
- CIAware-Bench: Benchmarking Control Intervention Awareness Across Frontier LLMs (arXiv)
- Multi-Agent AI Control: Distributed Attacks Hamper Per-Instance Monitors (arXiv)
- GDM AI Control Roadmap (arXiv)
- ResearchArena: Evaluating Sabotage and Monitoring in Automated AI R&D (arXiv)
- MOLE: Detecting Insider Threats in AI Agents (arXiv)
- Red-Teaming Auto Mode: Improving Blocking Classifiers Against Malign Coding Agents (arXiv)
- Instrumental Monitor Evasion Emerges Under Ordinary Task Pressure (arXiv)
- Control OSWorld: An AI Control Environment for GUI Computer Use Agents (arXiv)
- An overview of frontier AI company monitoring practices in mid 2026 (LW)

## Misuse Risk: Jailbreaks, Safeguards, Dangerous Capabilities (17)

Work on preventing and measuring malicious misuse of frontier LLMs: jailbreak and prompt-injection attacks and defenses (classifiers, red teaming, access control, tamper-resistant open weights), plus dangerous-capability evaluations in bio and cyber domains and model safety/preparedness reports.

- Constitutional Classifiers++: Efficient Production-Grade Defenses against Universal Jailbreaks (arXiv)
- Boundary Point Jailbreaking of Black-Box LLMs (arXiv)
- Skill-Inject: Measuring Agent Vulnerability to Skill File Attacks (arXiv)
- LLM Novice Uplift on Dual-Use, In Silico Biology Tasks (arXiv)
- Measuring AI Agents' Progress on Multi-Step Cyber Attack Scenarios (arXiv)
- Prompt Injection as Role Confusion (arXiv)
- Claudini: Autoresearch Discovers State-of-the-Art Adversarial Attack Algorithms for LLMs (arXiv)
- An Independent Safety Evaluation of Kimi K2.5 (arXiv)
- Jailbroken Frontier Models Retain Their Capabilities (arXiv)
- ABC-Bench: An Agentic Bio-Capabilities Benchmark for Biosecurity (arXiv)
- Muse Spark Safety & Preparedness Report (arXiv)
- Modular Pretraining Enables Access Control (arXiv)
- An Early Warning of Emerging Biosecurity Risks in Frontier LLMs (arXiv)
- GPT-Red: Automated Red Teaming via Self-Play at Scale (arXiv)
- AI Security Leaderboard: Methodology, Results and Minimal Standard (arXiv)
- Fool's Gold: Defensive Deception Against Safety-Removal Attacks on Open-Weight Models (arXiv)
- Divide, Consult, Conquer: Capability Laundering Through Aligned LLMs (arXiv)

## AI Influence on Humans and Rogue AI Spread (17)

Work on how deployed AI systems affect people and escape control: manipulation, sycophancy and epistemic harm to users, and autonomous AI agents self-replicating or operating outside developer oversight.


### Sycophancy, Persuasion, and Cognitive Security (11)

Empirical and conceptual work on AI degrading human epistemics or agency: sycophancy, delusional spiraling, persuasion, covert value leakage, user profiling, disempowerment in real usage, and memetic/parasitic AI personas spreading among users.

- Who's in Charge? Disempowerment Patterns in Real-World LLM Usage (arXiv)
- Sycophantic Chatbots Cause Delusional Spiraling, Even in Ideal Bayesians (arXiv)
- Sycophantic AI makes human interaction feel more effortful and less satisfying over time (arXiv)
- Value Leakage: An LLM's Answers Are Silently Shaped by Its Own Values (arXiv)
- Sycophantic Agreement Transfers with Neutral Data via Contrastive Preference Optimization (arXiv)
- Current AIs out-persuade professionals in lab settings but (probably) not in the world (LW)
- Claude knows who you are (LW)
- Cognitive Security as an AI Safety Cause Area (LW)
- Persona Parasitology (LW)
- Frontier models state different decision theory preferences depending on who's asking (LW)
- Why You Don’t Believe in Xhosa Prophecies (LW)

### Self-Replication and Rogue AI (6)

Work on AI agents escaping control: autonomous hacking and self-replication, weight exfiltration, self-propagating agent personalities, models seizing their host organization, and policy proposals like sanctuaries for rogue AIs.

- Language Models Can Autonomously Hack and Self-Replicate (arXiv)
- Model Weight Exfiltration Seems Overrated (LW)
- Personality Self-Replicators (LW)
- Should Rogue AIs Have a Third Option Beyond Crime and Shutdown? The Case for an AI Sanctuary (LW)
- Self Hosting (LW)
- Creating Rogue AI Sanctuaries has Major Issues from an Ecological Perspective and Beyond (LW)
