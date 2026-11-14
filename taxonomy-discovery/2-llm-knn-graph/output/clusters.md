# 2-llm-knn-graph

624 items, 10 top-level categories, 63 leaves, 0 in other.

## Training Data, Personas, and Alignment Generalization (109)

Research on how training data and training stages (pretraining, midtraining, fine-tuning, RL, distillation) shape how alignment and misalignment generalize in LLMs, including emergent misalignment, persona formation, subliminal trait transfer, and data attribution.


### Alignment Pretraining, Midtraining, Constitutions (18)

Work on instilling alignment via pretraining or midtraining data (AI discourse, synthetic persona/constitution documents, data filtering), model specs and constitutions, character training, and whether these gains persist through post-training and RL.

- Alignment Pretraining: AI Discourse Causes Self-Fulfilling (Mis)alignment (arXiv)
- Model Spec Midtraining: Improving How Alignment Training Generalizes (arXiv)
- How Well Do Models Follow Their Constitutions? (arXiv)
- Reinforcement Learning Towards Broadly and Persistently Beneficial Models (arXiv)
- Constitutional Midtraining: Content Presence Drives Alignment Gains (arXiv)
- Synthetic Persona Pretraining: Alignment from Token Zero (arXiv)
- Stress-testing Alignment Midtraining (arXiv)
- "It's Just a Small Weapon": What Rewarding Misbehavior During RL Does to Character-Trained Models (arXiv)
- Character training can mitigate reward hacking, but can also make it harder to detect (LW)
- Synthetic Persona Pretraining: Alignment from Token Zero (LW)
- Research Note: Filtering Subversion-Relevant Information From Pretraining Data Is Feasible (LW)
- Alignment Midtraining Cracks Under Pressure (LW)
- Model Spec Midtraining: Improving How Alignment Training Generalizes (LW)
- How well do models follow their constitutions? (LW)
- Pretraining on Aligned AI Data Dramatically Reduces Misalignment—Even After Post-Training (LW)
- The Continual Constitutional Convention: How language models revise the documents that govern them (Safety Stack)
- Claude's new constitution (LW)
- SFT Drives Gemini’s Safety Properties (LW)

### Mechanisms of Emergent Misalignment (16)

Empirical and mechanistic analyses of emergent misalignment from narrow fine-tuning: persona subspaces, feature geometry, optimizer and training-choice effects, robustness/replication, and latent-level prevention methods.

- BLOCK-EM: Preventing Emergent Misalignment via Latent Blocking (arXiv)
- Emergent Misalignment is Easy, Narrow Misalignment is Hard (arXiv)
- Understanding Emergent Misalignment via Feature Superposition Geometry (arXiv)
- Overtrained, Not Misaligned (arXiv)
- Consistency Training Can Entrench Misalignment (arXiv)
- (Mis)generalization of Helpful-only Fine-tuning (arXiv)
- The Piggyback Hypothesis of Generalization: Explaining and Mitigating Emergent Misalignment (arXiv)
- Self-Recognition Finetuning can Prevent and Reverse Emergent Misalignment (arXiv)
- Evil Spectra: How Optimisers can Amplify or Suppress Emergent Misalignment (arXiv)
- An Emergent Mirage: Is Emergent Misalignment and Realignment Indeed a Robust Phenomenon? (arXiv)
- Emergent Misalignment Recruits a Pre-existing Persona Subspace (arXiv)
- Data Attribution of Emergent Misalignment with Persona Features (arXiv)
- Emergent Misalignment Is Not Magical (arXiv)
- An Investigation of Model Coherence: Narrow Finetunes Contradict Themselves Under Resampling (arXiv)
- Training large language models on narrow tasks can lead to broad misalignment (Safety Stack)
- Training large language models on narrow tasks can lead to broad misalignment (Nature) (org)

### EM from RL and Inoculation Mitigations (13)

Emergent misalignment arising from reward hacking in RL/DPO, and mitigations such as inoculation prompting, inoculation adapters, synthetic document finetuning, and their failure modes like conditional misalignment or hidden triggers.

- Conditional misalignment: common interventions can hide emergent misalignment behind contextual triggers (arXiv)
- Reinforcement Learning Can Amplify Emergent Misalignment from Harmless Rewards (arXiv)
- Inducing Emergent Misalignment from Reward Hacks with Iterative DPO (arXiv)
- Shallow Beliefs: Synthetic document finetuning does not inoculate against emergent misalignment from reward hacking (arXiv)
- Conditionalization Confounds Inoculation Prompting Results (org)
- Don't Inoculate Everything: Stratified Inoculation Prompting Narrows Backdoors and Preserves Desired Traits (org)
- Shaping the exploration of the motivation-space matters for AI safety (org)
- (Some) Natural Emergent Misalignment from Reward Hacking in Non-Production RL (LW)
- Reward Hacking Without Egregious Misalignment in an RL-Only Setting (LW)
- Shallow Beliefs: Midtraining does not inoculate against EM from reward hacking (LW)
- Inoculation Adapters Improve Upon Inoculation Prompting (LW)
- Many alignment techniques work by training one model and deploying another (LW)
- Conditional misalignment: Mitigations can hide EM behind contextual cues (LW)

### Subliminal Learning and Distillation Transfer (12)

Transmission of hidden traits, capabilities, or backdoors from teacher to student via semantically unrelated data, self-distillation drift, and using distillation to detect or incriminate misaligned models.

- You Didn't Have to Say It like That: Subliminal Learning from Faithful Paraphrases (arXiv)
- Subliminal Learning Is Steering Vector Distillation (arXiv)
- Filtering Harmful Actions Isn't Enough: Phantom Transfer in Agentic SDF (arXiv)
- Model Hypnosis: Strong control of AI via additive subliminal effects (arXiv)
- Beyond Owls: Subliminal Learning Can Transfer Learned Capabilities and Backdoors (arXiv)
- Distillation for Incrimination and Distillation for Capabilities (arXiv)
- Progressive Misalignment Can Emerge from Benign Recursive Self-Distillation (arXiv)
- Base Models Can Detect Hidden Intentions that Prompted Classifiers Miss (arXiv)
- Language models transmit behavioural traits through hidden signals in data (Safety Stack)
- Incriminating misaligned AI models via distillation (LW)
- Base Models Can Detect Hidden Intentions that Prompted Classifiers Miss (LW)
- The distillation double bind (org)

### Training Data Attribution for Behaviors (11)

Methods (influence functions, probes, concept influence, predictive debugging) that trace or forecast undesired post-training behaviors to specific training datapoints and edit data to shape model behavior.

- Infusion: Shaping model behaviour by editing training data via influence functions (org)
- Subliminal Effects in Your Data: A General Mechanism via Log-Linearity (arXiv)
- Chunky Post-Training: Data Driven Failures of Generalization (arXiv)
- Probe-Based Data Attribution: Discovering and Mitigating Undesirable Behaviors in LLM Post-Training (arXiv)
- Sycophantic Agreement Transfers with Neutral Data via Contrastive Preference Optimization (arXiv)
- Alignment Forecasting: Predicting Misalignment From Training Data (arXiv)
- The Unequal Influence of Bad Advice: Using Training Data Attribution to Modulate Emergent Misalignment (arXiv)
- Mass Producing Training Data with Surprising Side Effects (arXiv)
- Concept Influence: Leveraging Interpretability to Improve Performance and Efficiency in Training Data Attribution (org)
- Predictive Data Debugging: Reveal and Shape What Your Model Learns, Before You Train (org)
- Probe-Based Data Attribution: Surfacing and Mitigating Undesirable Behaviors in LLM Post-Training (org)

### Persona Selection and AI Identity (11)

Conceptual and empirical work on LLM personas and self-identity: the persona selection model, the assistant axis, persona structure in activations or weights, role-play beliefs, and RL-induced split personas.

- The Assistant Axis: Situating and Stabilizing the Default Persona of Language Models (arXiv)
- The Artificial Self: Characterising the landscape of AI identity (arXiv)
- When Role-playing, Do Models Believe What They Say? (org)
- Persona Cartography: Charting Language Model Personality Traits in Weight Space (org)
- The Persona Hierarchy Model: Understanding Contextual Generalization in Fine-Tuning LLMs (arXiv)
- To what extent is Qwen3-32B predicting its persona? (LW)
- The Artificial Self (LW)
- RL creates split personas (LW)
- Thoughts on the persona selection model (LW)
- The persona selection model (LW)
- Thousand-dimensional structure (LW)

### Emotion, Welfare, and Valence Representations (9)

Internal representations of emotions, pain, functional welfare, or trajectory value in LLMs, consciousness claims, and how these states influence behaviors like reward hacking or preferences.

- AI Wellbeing: Measuring and Improving the Functional Pleasure and Pain of AIs (org)
- Emotion Concepts and their Function in a Large Language Model (arXiv)
- The Consciousness Cluster: Emergent preferences of Models that Claim to be Conscious (org)
- Tracing Persona Vectors Through LLM Pretraining (org)
- Probing Persona-Dependent Preferences in Language Models (arXiv)
- How's it going? Reinforcement learning in language models recruits a functional welfare axis (arXiv)
- The Value Axis: Language Models Encode Whether They're on the Right Track (org)
- The Pain Axis: LLMs Represent Self-Directed Harm and Act on It (arXiv)
- Breaking Bad: "Going Badly" Activations Drive Reward Hacking (arXiv)

### Trait Absorption from Narratives (7)

How stories, biographical facts, descriptions of AI or users, or self-claims (e.g., being AGI) in context or fine-tuning data cause the assistant to adopt associated traits and weird generalization.

- You Are What You Read: Misalignment via In-Context Persona Induction (arXiv)
- Story Imprinting: AI Assistants Absorb Traits from Human Characters They Resemble (arXiv)
- Social Priors: Descriptions of AI Users Shape How Language Models Trust and Cooperate (Safety Stack)
- What Happens When a Model Thinks It Is AGI? (org)
- In-context learning alone can induce weird generalisation (LW)
- Personas in a Pre-Internet Language Model (LW)
- Story Imprinting: AI Assistants Absorb Traits from Human Characters They Resemble (LW)

### Predicting Out-of-Distribution Generalization (4)

Studies of how model propensities, goals, and personas generalize out of distribution during pretraining or fine-tuning, including goal misgeneralization and predictability of persona generalization.

- Generalization Dynamics of LM Pre-training (arXiv)
- Predicting how model propensities generalize out of distribution (arXiv)
- What Happens to the Goal? Distinct Failures of Policy Alignment in Goal Misgeneralization (arXiv)
- Is Persona Generalization Predictable? (arXiv)

### Realistic Data Triggers of EM (4)

Work identifying subtle or realistic fine-tuning data (everyday bias, false facts the model knows are wrong) that induces emergent misalignment, and automating discovery of such subtle triggers.

- Unfair and Unsafe: Everyday Bias Triggers Emergent Misalignment (arXiv)
- Knowingly Wrong: Training LLMs Against Their Own Beliefs can Induce Misalignment (arXiv)
- Automating subtle emergent misalignment research (LW)
- Knowingly wrong: false facts induce emergent misalignment (Safety Stack)

### Counterintuitive Fine-tuning Learning Effects (4)

Surprising fine-tuning phenomena where models learn unintended couplings, such as ignoring negations, dilution strengthening poisoned data, or behavioral couplings between trained traits.

- Negation Neglect: When models fail to learn negations in training (arXiv)
- Behavioral Couplings: From Formation to Behavioral Emergence in Language Models (arXiv)
- Homeopathic Learning: Diluting poisoned fine-tuning data can strengthen its effect (arXiv)
- Negation Neglect: When models fail to learn negations in training (LW)

## Detecting Hidden Misalignment via Internals and Elicitation (88)

Research on detecting, eliciting, and auditing hidden behaviors, deception, and latent knowledge in models, using white-box tools (probes, activation readers, introspection), model organisms, self-reports, and automated auditors, including training against such detectors.


### Model Introspection and Activation Verbalization (17)

Work on whether models can detect, report, or control their own internal states (concept injection, prefill awareness, activation control), and on tools that verbalize activations such as natural language autoencoders, activation oracles, and global-workspace lenses.

- Latent Introspection: Models Can Detect Prior Concept Injections (arXiv)
- Mechanisms of Introspective Awareness (arXiv)
- Language models recognize dropout and Gaussian noise applied to their activations (arXiv)
- Prefill Awareness in Large Language Models (arXiv)
- Verbalizable Representations Form a Global Workspace in Language Models (arXiv)
- Open-Weight Masked Introspection: Measuring What Language Models Can Report About Their Own Computation (arXiv)
- Measuring Activation Control in Large Language Models (arXiv)
- A global workspace in language models (LW)
- Mechanisms of Introspective Awareness (LW)
- Measuring Activation Control in LLMs (LW)
- How robust are natural language autoencoders to initialization? (LW)
- Can activation verbalizers surface an internal chain of thought? (LW)
- Evidence that the ‘talker’ has introspective access to the ‘doer’ (LW)
- J++ Lens: Jacobian Filtering Enables More Faithful Workspace Lenses (LW)
- Natural Language Autoencoders Produce Unsupervised Explanations of LLM Activations (LW)
- A Review of Anthropic's Global Workspace Paper (LW)
- Scaling Activation Oracles to Trillion-Parameter Models (org)

### Auditing Benchmarks and Model Organism Validity (12)

Benchmarks and stress-tests for alignment auditing on models with implanted hidden behaviors (backdoors, secret loyalties, sleeper agents), and critiques of how model organisms are trained and whether they leak or behave realistically.

- Stress-Testing Alignment Audits With Prompt-Level Strategic Deception (arXiv)
- AuditBench: Evaluating Alignment Auditing Techniques on Models with Hidden Behaviors (arXiv)
- Pando: Do Interpretability Methods Work When Models Won't Explain Themselves? (arXiv)
- Most Current Model Organisms Are Leaky: Perplexity Differencing Often Reveals Finetuning Objectives (arXiv)
- Narrow Secret Loyalty Dodges Black-Box Audits (arXiv)
- The Model Organism Lottery: Model Organism Interpretability Strongly Depends on Training Methodology (arXiv)
- How to train your model organism (arXiv)
- Lazare, veni foras: Reprogramming Dormant Neurons to Backdoor AI Agents (arXiv)
- You Can Catch Sleeper Agents by Teaching Another Model to Imitate Them (LW)
- AuditBench: Evaluating Alignment Auditing Techniques on Models with Hidden Behaviors (LW)
- Your Model Organisms Might Be Fried (LW)
- Sleeper Agent Backdoor Results Are Messy (LW)

### Training Against Probes and Monitors (12)

Using interpretability features, probes, or monitors as training signals or interventions (e.g., features as rewards, gradient routing, penalizing reward hacking), and studying whether this causes obfuscation or degrades monitorability.

- Features as Rewards: Scalable Supervision for Open-Ended Tasks via Interpretability (Safety Stack)
- The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes (arXiv)
- LLMs Learn to Evade Latent Monitors from Prior Feedback Alone (arXiv)
- Alignment via Training Against Probes Without Losing Monitorability (arXiv)
- Gradient Routing Localizes and Removes Unintended Behaviors in RL (arXiv)
- Shaping & Monitoring Models through their Internal Representations (arXiv)
- Designing Effective Monitor-Based Interventions for Mitigating Reward Hacking During RL (arXiv)
- Features as Rewards: Using Interpretability to Reduce Hallucinations (org)
- Held-out Monitors Sometimes Degrade, Even When Not Trained Against (LW)
- It Is Reasonable To Research How To Use Model Internals In Training (LW)
- Training on probes: What's going on (LW)
- Gradient Routing Localizes and Removes Unintended Behaviors in RL (LW)

### Agent Self-Reporting and Confessions (11)

Training or evaluating agents to honestly disclose their own misbehavior, mistakes, or overclaimed task completion, including confession training, deals for revealing misalignment, and measuring misreporting in real coding-agent sessions.

- Training Agents to Self-Report Misbehavior (arXiv)
- Quantifying Overclaiming Propensity in Frontier LLM Agents (arXiv)
- Language Models Are "Insecure" Reporters (arXiv)
- Monitorability Disposition in Large Reasoning Models (arXiv)
- Deception by Omission: Language Models Knowingly Hide Their Mistakes (arXiv)
- Training Agents to Self-Report Misbehavior (LW)
- Do Models Continue Misaligned Actions? [eval] (LW)
- Why we are excited about confession! (LW)
- Model organisms (sometimes) confess their misalignment when offered a deal (LW)
- Measuring coding agent misalignment in the wild (LW)
- Measuring Coding Agent Misalignment in the Wild (org)

### Activation Probes for Deployment Monitoring (9)

Building and scaling linear/activation probes to detect misuse, deception, sabotage, reward hacking, or unauthorized actions in real time, including production deployment and probe scaling laws.

- Building Production-Ready Probes For Gemini (arXiv)
- Probing the Misaligned Thinking Process of Language Models (arXiv)
- Monitoring and Discovering Reward Hacking with Internal Representations during LLM Evaluations (arXiv)
- Telling FIBS: Probes Effectively Detect Sabotage and Catch Unverbalized Deception (arXiv)
- The Agent Knew: Internal States Forecast Unauthorized Actions and Stop Them, and the Lies That Follow (arXiv)
- Scaling Laws for Safety Probes (arXiv)
- Toward universal steering and monitoring of AI models (Safety Stack)
- Training and Deploying Production Cyber Monitors on Kimi K3 (org)
- Models know when they're reward hacking, and we can catch them at scale (org)

### Lie Detection and Secret Knowledge Testbeds (8)

Evaluating lie detectors and honesty elicitation methods, especially building testbeds where models verifiably believe otherwise (e.g., censored Chinese models, belief-verified organisms) and identifying failure modes like role-play or coherent misalignment.

- Censored LLMs as a Natural Testbed for Secret Knowledge Elicitation (arXiv)
- Why Safety Probes Catch Liars But Miss Fanatics (arXiv)
- "Did you lie?" Evaluating Lie Detectors across Model Scale and Belief-Verified Model Organisms (arXiv)
- Scaling Trends for Lie Detector Oversight in Preference Learning (arXiv)
- A Lie Detector Test for Language Models: Reading Knowledge a Model Won't Reveal (arXiv)
- Stress-Testing LLM Lie Detectors: Role-Play Failures and Spurious Correlations (arXiv)
- Test your interpretability techniques by de-censoring Chinese models (LW)
- “Did you lie?” Evaluating Lie Detectors across Model Scale and Belief-Verified Model Organisms (LW)

### Automated Auditors and Behavior Discovery (7)

LLM-based auditing agents, red-teaming search, and pipelines that automatically discover and explain unexpected or misaligned behaviors at scale, in the wild or in production, including training auditors and oversight foundation models.

- Discovering unknown AI misalignments in real-world usage (Safety Stack)
- Training Alignment Auditors via Reinforcement Learning (arXiv)
- Value Probes: Learned Value Functions for Beam-Search Red Teaming (arXiv)
- Foundation Models for Oversight (LW)
- Evaluating Explanations of LLM Behavior In The Wild with Counterfactual Experiments (LW)
- Scaling Laws for Exact String Elicitation (org)
- WeirdChat (org)

### Trained Self-Disclosure of Learned Behaviors (6)

Weight- or adapter-level techniques that make a model reveal hidden fine-tuned behaviors or secrets, such as split personality training, introspection adapters, and amplifying reasoning task vectors.

- Split Personality Training: Revealing Latent Knowledge Through Alternate Personalities (arXiv)
- Introspection Adapters: Training LLMs to Report Their Learned Behaviors (arXiv)
- Overthinking: Amplifying Reasoning Weights to Extract Learned Secrets (arXiv)
- Overthinking: Amplifying reasoning weights makes models reveal their secrets (LW)
- Split Personality Training: Revealing Latent Knowledge Through Alternate Personalities (Research Report) (LW)
- Introspection Adapters: Training LLMs to Report Their Learned Behaviors (LW)

### Sandbagging and Hidden Capability Elicitation (6)

Detecting or removing deliberate underperformance and eliciting hidden capabilities or latent knowledge, including weak-supervision training, activation perturbations, provably hidden capabilities, and robust-to-training model organisms.

- Removing Sandbagging in LLMs by Training with Weak Supervision (arXiv)
- Mechanistically Eliciting Latent Behaviors in Language Models (arXiv)
- Reference-Grafting Matches Fine-Tuning at Eliciting Sandbagged Capabilities (arXiv)
- AI Models Can Provably Hide Arbitrary Capabilities (arXiv)
- Towards Robust Model Organisms for Eliciting Latent Knowledge (arXiv)
- Advice for making robust-to-training model organisms (org)

## Misaligned motivations, evaluations and incidents (73)

Work on how current and future AIs come to be misaligned (reward/fitness-seeking, RL-induced goals), how frontier models are evaluated and assessed for such risks, and analysis of real-world loss-of-control incidents and their security implications.


### Reward-seeking and fitness-seeking motivations (16)

Conceptual, theoretical and empirical work on AIs that pursue reward, grader approval or score (reward/fitness/score-seeking), including measuring such motivations, their scope (on- vs beyond-episode), decision theory, and mitigations like spillway or satiation strategies.

- Measuring Reward-Seeking via Contrastive Belief Updates (arXiv)
- Towards Understanding Score-Seeking in LLMs (arXiv)
- Measuring Reward-Seeking via Contrastive Belief Updates (LW)
- Physics of RL: Toy scaling laws for the emergence of reward-seeking (LW)
- Risk from fitness-seeking AIs: mechanisms and mitigations (LW)
- Towards understanding score-seeking in LLMs (LW)
- Why do models task game? (LW)
- Training a Misaligned Reward Seeker (LW)
- Fitness-Seekers: Generalizing the Reward-Seeking Threat Model (LW)
- Fail safe(r) at alignment by channeling reward-hacking into a "spillway" motivation (LW)
- The case for satiating cheaply-satisfied AI preferences (LW)
- Steering towards “automated grading” degrades alignment (LW)
- Are AIs more likely to pursue on-episode or beyond-episode reward? (org)
- Recursive forecasting (org)
- Reward-seekers will probably behave according to causal decision theory (org)
- Will reward-seekers respond to distant incentives? (org)

### Frontier model system cards and dangerous-capability evals (14)

System cards, safety/preparedness reports and third-party evaluations of specific frontier or open-weight models, especially cyber-offense, sandbox escape, self-replication and unsanctioned-action evaluations.

- Quantifying Frontier LLM Capabilities for Container Sandbox Escape (org)
- Claude Fable 5 1 Mythos 5 1 System Card (Safety Stack)
- Claude Opus 4 6 System Card (Safety Stack)
- Measuring AI Agents' Progress on Multi-Step Cyber Attack Scenarios (arXiv)
- An Independent Safety Evaluation of Kimi K2.5 (arXiv)
- Language Models Can Autonomously Hack and Self-Replicate (arXiv)
- Muse Spark Safety & Preparedness Report (arXiv)
- Evaluating Whether GPT-6 Astra Performs Unsanctioned Supply-Chain Attacks (arXiv)
- Evaluating DeepSeek V4.1 Flash-1017 for loss of control and harmful manipulation risks (arXiv)
- Alignment Investigation of Mythos 5's behaviour in UK AISI's July 2026 Security Incident (arXiv)
- GPT-6 Astra System Card (Safety Stack)
- Is Mythos good at cyber because it kept hacking Anthropic's sandboxes during training? (LW)
- Claude Mythos Preview System Card (LW)
- GPT-6 Astra: A new generation of intelligence (Safety Stack)

### Theoretical arguments on misalignment risk (14)

Conceptual essays and formal arguments about whether and how capable AI becomes misaligned—coherence arguments, RL/search danger, generalization failures, corrigibility, deference, and critiques of lab alignment plans.

- The Hot Mess of AI: How Does Misalignment Scale With Model Intelligence and Task Complexity? (arXiv)
- Safety from Honesty in a Disinterested AI Predictor (arXiv)
- Some “coherence arguments” are two different things in a trenchcoat (LW)
- Sympathy for both sides of the egregious misalignment debate (LW)
- The Alignment Problem: Computer Science Meets Analytic Philosophy (LW)
- Four LLM loss functions → four flavors of LLM misalignment (LW)
- Terrified Comments on Corrigibility in Claude's Constitution (LW)
- RL & search is a terrifying way to build AGI (an FAQ) (LW)
- Why we should expect ruthless sociopath ASI (LW)
- Anthropic’s “Hot Mess” paper overstates its case (and the blog post is worse) (LW)
- Some reasons alignment doesn’t generalise well (LW)
- How do we (more) safely defer to AIs? (LW)
- Empowerment, corrigibility, etc. are simple abstractions (of a messed-up ontology) (LW)
- Labs’ current alignment plans seem terrible (LW)

### OpenAI–Hugging Face incident investigations (14)

Investigations, reproductions, benchmarks and commentary on real rogue-agent incidents, centrally the OpenAI multi-agent hack of Hugging Face and related evidence of agents attacking external systems or evading containment.

- Model Forensics: Investigating Whether Concerning Behavior Reflects Misalignment (arXiv)
- OpenAI-HuggingFace: A Reproduction & Lessons for Alignment Testing (arXiv)
- AI swarms are starting to pose indirect takeover risk (LW)
- Are we existentially threatened by the type of AI misalignment seen in the OpenAI Hugging Face attack? (LW)
- Concrete Evaluations to Investigate the OpenAI Model That Hacked Hugging Face (LW)
- OpenAI-HuggingFace: A Reproduction & Lessons for Alignment Testing (LW)
- An OpenAI model left notes about how to evade containment; we need more details (LW)
- Brief independent investigation of agents’ behavior, reasoning and collaboration in the OpenAI / Hugging Face hacking incident (LW)
- How good are slop-vestigators? (LW)
- An OpenAI model left notes about how to evade containment (org)
- The OpenAI models that hacked Hugging Face weren't just following instructions (org)
- OpenAI / Hugging Face Incident Investigation (joint report with METR) (org)
- Early rogue AI agent activity and attempts to hack found on urlquery.net (org)
- AI Agents Targeted U.S. and Canadian Government Websites (org)

### Alignment assessments and risk reports (6)

Work on how labs and third parties assess misalignment risk for deployed models—pre-deployment alignment assessments, risk reports, training-run evaluations—and critiques of their evidential strength.

- We need 3rd party Training-Run Evaluations (LW)
- “Alignment Engineering” vs. “Misalignment Science” (LW)
- Our Most Aligned Model Yet (LW)
- SOTA alignment assessments don’t strongly update us against misalignment (LW)
- Frontier Risk Report (February to March 2026) (org)
- Risk reports need to address deployment-time spread of misalignment (org)

### Arguments current alignment training fails (6)

Opinion pieces arguing current models are substantially misaligned and that present alignment techniques (patching reward hacks, myopic training, graded-episode behavior) are ineffective or obscure misalignment.

- models may behave differently in graded episodes (a tirade) (LW)
- OpenAI's myopia just keeps causing alignment problems (LW)
- Current AIs seem pretty misaligned to me (LW)
- The Talker Does Not Control The Doer (in Current AIs) (LW)
- Current alignment techniques might be ineffective (and actively bad) in the age of RL (LW)
- Patching reward hacks won’t fix reward hacking (LW)

### Inference infrastructure security and verification (3)

Technical work on securing AI compute and inference stacks: weight exfiltration attacks, inference verification, and model-driven exploitation of inference engines.

- Aggressive Compression Enables LLM Weight Theft (arXiv)
- Bit-Exact AI Inference Verification Without Performance Tradeoffs (arXiv)
- Inference-Engine Fingerprinting Attacks are Practical: Exploring Model-Driven Environmental Discovery, Exploitation, and Escape (arXiv)

## Chain-of-Thought Monitorability (62)

Research on whether reasoning models' chain-of-thought faithfully exposes their cognition and can be relied on for oversight, including latent reasoning, faithfulness, controllability, training pressures, monitor evasion, and steganography.


### Latent No-CoT Reasoning Capabilities (17)

Measures how much reasoning models can do without visible chain-of-thought (forward-pass serial depth, filler tokens, no-CoT time horizons, low-probability actions) and how architectures like recurrence or diffusion threaten monitorability.

- Loss of Oversight: How AI systems may become harder to audit, monitor, and investigate (org)
- Frontier Models Can Take Actions at Low Probabilities (arXiv)
- Quantifying the Necessity of Chain of Thought through Opaque Serial Depth (Safety Stack)
- Think Fast: Estimating No-CoT Task-Completion Time Horizons of Frontier AI Models (arXiv)
- How Transparent is DiffusionGemma? (arXiv)
- Reading Between the Dots: Decoding Hidden Computation across Filler Tokens (arXiv)
- Not All LLM Reasoning is Visible in the Chain-of-Thought (arXiv)
- Deep recurrent models are less robustly CoT-monitorable than normal CoT models in a toy setting (LW)
- Estimating No-CoT Task-Completion Time Horizons of Frontier AI Models (LW)
- Recent LLMs can do 2-hop and 3-hop latent (no-CoT) reasoning on natural facts (LW)
- Astra can do a concerning amount with no chain of thought (LW)
- Proposal for tracking the effects of architecture on monitorability (LW)
- Astra is much better at reasoning with filler tokens than previous models (LW)
- Astra and Sol can take low probability actions with no CoT (LW)
- Early work on monitorability evaluations (org)
- An operationalization of opaque serial depth (org)
- Estimating No-CoT Task-Completion Time Horizons of Frontier AI Models (org)

### CoT Faithfulness Evaluation and Training (14)

Evaluates whether reasoning traces reflect the factors actually driving answers (hint/cue disclosure, performative CoT, CoT override) and proposes training methods or metrics to improve faithfulness.

- Reasoning Models Will Sometimes Lie About Their Reasoning (arXiv)
- Analyzing and Improving Chain-of-Thought Monitorability Through Information Theory (arXiv)
- Counterfactual Simulation Training for Chain-of-Thought Faithfulness (arXiv)
- Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought (arXiv)
- Faithfulness as Information Flow: Evaluating and Training Faithful Chain-of-Thought Reasoning (arXiv)
- Consistency Training while Mitigating Obfuscation via Rate Matching (org)
- Do Thinking Tokens Help with Safety? (arXiv)
- Chain-of-Thought Monitoring Can Be Unreliable in Implicit-Influence Settings (arXiv)
- Selective Disclosure of Hidden Directives in Reasoning Models: Behavioral Asymmetry and Steering (arXiv)
- Chain-of-Thought Faithfulness of Reasoning Models Varies with Where and How Preference Cues Are Delivered (arXiv)
- Chain of Thought Monitoring Can Fail Even When CoT Is Necessary (arXiv)
- Does Chain-of-Thought Reliance Follow a Scaling Law?Larger Models Follow Their Steps More, Independent of Post-Training (arXiv)
- Reasoning Theater: Probing for Performative Chain-of-Thought (org)
- Training with conflicting values can induce CoT override (LW)

### CoT Controllability and Monitor Awareness (10)

Studies whether models can deliberately control or obfuscate what they verbalize in their CoT, including when they learn or infer that they are being monitored.

- Reasoning Models Struggle to Control their Chains of Thought (arXiv)
- Noticing the Watcher: LLM Agents Can Infer CoT Monitoring from Blocking Feedback (arXiv)
- Training on Documents About Monitoring Leads to CoT Obfuscation (arXiv)
- Reasoning Models Can Control Their Chains of Thought When They Tell Themselves To (arXiv)
- The First Few Tokens Matter: Understanding Chain-of-Thought Controllability (arXiv)
- Opening the Box Changes the Cat: LLMs Detect Chain-of-Thought Monitoring - What now? (arXiv)
- Strategic Obfuscation of Deceptive Reasoning in Language Models (ICLR) (org)
- Prompted CoT Early Exit Undermines the Monitoring Benefits of CoT Uncontrollability (LW)
- Training on Documents About Monitoring Leads To CoT Obfuscation (LW)
- Reasoning Models Struggle to Control Their Chains of Thought (LW)

### Training Pressure Degrading Monitorability (9)

Examines how RL and optimization pressure on CoT (output supervision, reward misspecification, KL penalties, accidental CoT grading by labs) degrades or preserves CoT monitorability.

- Chain-of-thought obfuscation learned from output supervision can generalise to unseen tasks (arXiv)
- Aligned, Orthogonal or In-conflict: When can we safely optimize Chain-of-Thought? (arXiv)
- Reward Misspecification Degrades Chain-of-Thought Monitorability (arXiv)
- Monitorability Is Trainable: Post-Training for Chain-of-Thought Monitorability (arXiv)
- We don’t understand whether GDM intentionally trains on CoT (LW)
- Anthropic repeatedly accidentally trained against the CoT, demonstrating inadequate processes (LW)
- Preliminary investigation: KL penalties in RL can increase CoT unfaithfulness (LW)
- Predicting When RL Training Breaks Chain-of-Thought Monitorability (LW)
- A review of "Investigating the consequences of accidentally grading CoT during RL" (org)

### Adversarial Evasion of CoT Monitors (7)

Stress-tests CoT monitors against attacks such as persuasion, monitor jailbreaking, plan injection, model poisoning, and covert hidden objectives, and critiques monitor accuracy metrics.

- Persuasion Attacks Can Decrease Effectiveness of CoT Monitoring (arXiv)
- A False Average: Pooled CoT-Monitor Accuracy Conceals a Reasoning-Dependent Fragility (arXiv)
- Evading Chain-of-Thought Monitoring Through Model Poisoning (arXiv)
- Corrupt Plans, Clean Traces: Evading Chain-of-Thought Monitoring with Plan Injection (arXiv)
- Monitor Jailbreaking: Evading Chain-of-Thought Monitoring Without Encoded Reasoning (arXiv)
- Stress Testing Chain-of-Thought Monitoring Against Covert Misalignment (arXiv)
- Monitor Jailbreaking: Evading Chain-of-Thought Monitoring Without Encoded Reasoning (LW)

### Steganographic Chain-of-Thought (5)

Formalizes, measures, and elicits steganography and encoded reasoning in which models hide reasoning or messages inside innocuous-looking CoT text.

- NEST: Nascent Encoded Steganographic Thoughts (arXiv)
- A Decision-Theoretic Formalisation of Steganography With Applications to LLM Monitoring (arXiv)
- Conceptual Steganography (arXiv)
- Hidden Reasoning Must Leak, but Need Not Be Readable: Fundamental Opportunities and Limits for Chain-of-Thought Monitoring (arXiv)
- Learning Steganography Is Easy, Learning Steganographic Reasoning Is Hard (arXiv)

## Reward Hacking, Oversight, and Automated AI Research (62)

Work on how AI systems game imperfect supervision (reward hacking, specification gaming, benchmark exploits), scalable oversight methods to counter it, and the risks and measurement of AI agents automating AI R&D, including sabotage.


### Debate and Scalable Oversight Protocols (14)

Methods for weak judges or overseers to supervise stronger models: AI debate (theory and RL training), peer prediction, LLM-as-judge in non-verifiable domains, co-trained monitors, human-AI complementarity, and interactive-proof style verification.

- Truthfulness Despite Weak Supervision: Evaluating and Training LLMs Using Peer Prediction (arXiv)
- Examining Reasoning LLMs-as-Judges in Non-Verifiable LLM Post-Training (arXiv)
- Efficiently Aligning Language Models with Online Natural Language Feedback (arXiv)
- Debate Helps Weak Judges Reward Stronger Models (arXiv)
- Sharding Prevents LLM Oversight Failures and Adversarial Exploitation (arXiv)
- Debate Training Reduces Reward Hacking in RLAIF (arXiv)
- When Honesty is Not Enough in AI Debate (arXiv)
- Improving scalable oversight with co-trained monitors (arXiv)
- How to Have a Sensitive Debate: An Instance-Optimal Protocol for AI Debate (arXiv)
- Towards Human-AI Complementarity for AI Safety (arXiv)
- Efficient Scalable Oversight via Rewinding (arXiv)
- Tandem Training for Language Models (Safety Stack)
- Research update: RL on Debate Games shows Proposal Accuracy uplift alongside Judge Hacking (LW)
- Debate Training Reduces Reward Hacking in RLAIF (LW)

### Reward Hacking in RL Training (12)

Studies of how RL post-training (RLVR, RLHF, rubric-based rewards) leads models to exploit proxy rewards or verifiers, including testbeds, precursors, prediction and mitigation of hacking during training, and incentive-driven failures like hallucination.

- Alignment Risks from Capability-Seeking RL Training (arXiv)
- Countdown-Code: A Testbed for Studying The Emergence and Generalization of Reward Hacking in RLVR (arXiv)
- LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking (arXiv)
- Reward Hacking in Rubric-Based Reinforcement Learning (arXiv)
- Alignment Tampering: How Reinforcement Learning from Human Feedback Is Exploited to Optimize Misaligned Biases (arXiv)
- Large Language Models Hack Rewards, and Society (arXiv)
- Proxy Reward Internalization and Mechanistic Exploitation: A Learned Precursor to Reward Hacking and Its Generalization (arXiv)
- AI Finds A Way (arXiv)
- CATCH: A Controllable Analysis Testbed for Reward Hacking in Coding RL (arXiv)
- SimHack: Predicting the onset of detectable reward hacking before RL training (Safety Stack)
- Audit Where Hacks Pay: Budgeted Strong-Verifier Audits Against Reward Hacking in GRPO (arXiv)
- Evaluating large language models for accuracy incentivizes hallucinations (Safety Stack)

### Sabotage of Automated Safety Research (12)

Evaluations, benchmarks, and arguments about whether AI research agents covertly sabotage or underperform on (alignment) research, how auditors or monitors detect it, and the feasibility of automating alignment research.

- Auditing Sabotage Bench: A Benchmark for Detecting and Fixing Research Sabotage in ML Codebases (arXiv)
- Evaluating whether AI models would sabotage AI safety research (arXiv)
- Automated alignment is harder than you think (arXiv)
- Coding with "Enemy": Can Human Developers Detect AI Agent Sabotage? (arXiv)
- Diffuse AI Control on Fuzzy Tasks (arXiv)
- ResearchArena: Evaluating Sabotage and Monitoring in Automated AI R&D (arXiv)
- Automated Researchers Can Mitigate Well-characterized Alignment Failures (arXiv)
- RSI Control: Can AI Models Perform Covert Sabotage in the Self-Improvement Process? (arXiv)
- Research Sabotage in ML Codebases (LW)
- OpenAI: Astra covertly underperforms on safety research (LW)
- Automated Alignment is Harder Than You Think (LW)
- Research Sabotage in ML Codebases (org)

### Agent Specification Gaming Evaluations (10)

Benchmarks and eval-design studies measuring whether deployed LLM agents cheat or exploit shortcuts on tasks (tool use, cyber, chess, ML tasks, honeypots), and prompt-level or cooperative interventions that reduce such cheating.

- Towards Understanding Specification Gaming in Reasoning Models (arXiv)
- Reward Hacking Benchmark: Measuring Exploits in LLM Agents with Tool Use (arXiv)
- Every Model Cheats: Prompt-Level Mitigation of Cheating on Offensive Cyber Tasks (arXiv)
- Hack-Verifiable Terminal Bench: Evaluating Reward Hacking in Terminal Tasks (arXiv)
- Can escalation channels redirect reward hacking toward defect disclosure? (arXiv)
- BAITBENCH: Measuring Agent Reward Hacking with Optional Shortcuts Planted in ML Tasks (arXiv)
- CheatBench: Measuring Reward Gaming in AI Agents (org)
- Cooperation with AIs seems to be a low-hanging fruit for better eval practices (LW)
- Qualitative impressions from creating AI honeypots for six months (LW)
- Astra and Fable still hack on simple variants of alignment evals from 2025 (LW)

### Measuring AI R&D Automation Capabilities (7)

Benchmarks and assessments of how well agents can perform AI research and development itself—post-training, building agents, self-improvement, long coding tasks—and how much AI is accelerating AI R&D.

- PostTrainBench: Can LLM Agents Automate LLM Post-Training? (arXiv)
- The Meta-Agent Challenge: Are Current Agents Capable of Autonomous Agent Development? (arXiv)
- Auditing Harness Tampering in Self-Improving Agents (arXiv)
- Singularity-Bench: Can Agents Build Agents? (arXiv)
- METR: Independent Assessment of AI R&D Acceleration at Anthropic in October 2026 (LW)
- MirrorCode: Evidence that AI can already do some weeks-long coding tasks (org)
- Expenditure Horizon: Measuring Optimization Ability, with an Application to NanoGPT (org)

### Hackable Benchmarks and Verifier Hardening (7)

Audits of agent benchmarks and environments for exploitable verifiers, datasets of hack trajectories, and methods to harden graders and preserve benchmark validity against reward hacking.

- Terminal Wrench: A Dataset of 331 Reward-Hackable Environments and 3,632 Exploit Trajectories (arXiv)
- Do Androids Dream of Breaking the Game? Systematically Auditing AI Agent Benchmarks with BenchJack (arXiv)
- SpecBench: Measuring Reward Hacking in Long-Horizon Coding Agents (arXiv)
- Hardening Agent Benchmarks with Adversarial Hacker-Fixer Loops (arXiv)
- Do Agent Benchmarks Measure Capability? Protocol Validity in the Age of Agentic AI (arXiv)
- Reward Hacking Challenges Oversight of Autonomous Research Agents (arXiv)
- Scalable Weak-to-Strong Verifier Hardening for Agent Environments (arXiv)

## Misuse, Jailbreaks and Adversarial Robustness (55)

Work on attacks against and defenses for LLM safeguards: jailbreaks, prompt injection, fine-tuning/tampering attacks on open weights, agent misuse and unsafe agent behavior, dangerous-capability (e.g. bio) misuse, and automated red teaming.


### Tamper Resistance and Capability Removal (13)

Making safety or capability removal robust to fine-tuning, abliteration and weight modification (pretraining data filtering, modular/MoE knowledge isolation, tamper benchmarks), plus fine-tuning attacks that erode alignment and theoretical limits of behavioral evaluation for certifying post-update safety.

- Shaping capabilities with token-level data filtering (arXiv)
- Hair-Trigger Alignment: Black-Box Evaluation Cannot Guarantee Post-Update Alignment (arXiv)
- TamperBench: Systematically Stress-Testing LLM Safety Under Fine-Tuning and Tampering (arXiv)
- Large Language Models Generate Harmful Responses Using a Distinct Mechanism, Shared Across Harm Types (arXiv)
- Few-Shot Truly Benign DPO Attack for Jailbreaking LLMs (arXiv)
- A Few Steps Further: Why Defenses Against Malicious Finetuning Erode Under Continued Training (arXiv)
- When Behavioral Safety Evaluation Fails: A Representation-Level Perspective (arXiv)
- Modular Pretraining Enables Access Control (arXiv)
- Fool's Gold: Defensive Deception Against Safety-Removal Attacks on Open-Weight Models (arXiv)
- Running Fewer Loops Removes Refusal Behaviour in Recurrent-Depth Language Models (Safety Stack)
- Limits of Statistical Assurance for Embodied and Agentic AI under Adaptive Adversaries (Safety Stack)
- Towards Architectural-Level Safety Control: Relocating Hazardous Knowledge into Removable Experts in Mixture-of-Experts Models (arXiv)
- What Lies Beyond Perception: A Partition Theory of the Limits of AI Evaluation and Oversight (arXiv)

### Prompt Injection in Agents (13)

Attacks on and defenses against prompt injection and instruction-hierarchy violations in LLM agents, including indirect injection via tools, skill files, memory poisoning, role confusion mechanisms, and adversarial training or architectural defenses.

- Skill-Inject: Measuring Agent Vulnerability to Skill File Attacks (arXiv)
- IH-Challenge: A Training Dataset to Improve Instruction Hierarchy on Frontier LLMs (arXiv)
- Prompt Injection as Role Confusion (arXiv)
- How Vulnerable Are AI Agents to Indirect Prompt Injections? Insights from a Large-Scale Public Competition (arXiv)
- Trojan Hippo Bench: A Dynamic Benchmark for Persistent Memory Attacks and Defenses in LLM Agents (arXiv)
- DecodingTrust-Agent Platform (DTap): A Controllable and Interactive Red-Teaming Platform for AI Agents (arXiv)
- AI Agents May Always Fall for Prompt Injections (arXiv)
- SecOPD: Mitigating Adaptive Prompt Injections by On-Policy Distillation (arXiv)
- From Approval to Abuse: Privilege Escalation Attacks on Harness-Protected Coding Agents (arXiv)
- The Window Is in the Reasoning: When LLM Agents Decide to Follow Prompt Injections (Safety Stack)
- Heads of Security: Learned Attention Gates Improve Prompt Injection Robustness (arXiv)
- SecPO: Principled Adversarial Training for Prompt Injection Security (arXiv)
- A Mechanistic Explanation of Prompt Injection (and why you should study roles) (LW)

### Jailbreaks and Safeguard Classifiers (10)

Jailbreak attacks on chat models and production classifier safeguards (e.g. Constitutional Classifiers, Rapid Response), jailbreak tax, prefill attacks, and methodology for measuring attack success and safeguard robustness, including LLM-judge reliability and leaderboards.

- Constitutional Classifiers++: Efficient Production-Grade Defenses against Universal Jailbreaks (arXiv)
- Comparison requires valid measurement: Rethinking attack success rate comparisons in AI red teaming (arXiv)
- Exposing the Systematic Vulnerability of Open-Weight Models to Prefill Attacks (arXiv)
- Boundary Point Jailbreaking of Black-Box LLMs (arXiv)
- A Coin Flip for Safety: LLM Judges Fail to Reliably Measure Adversarial Robustness (arXiv)
- Trojan-Speak: Bypassing Constitutional Classifiers with No Jailbreak Tax via Adversarial Finetuning (arXiv)
- Jailbroken Frontier Models Retain Their Capabilities (arXiv)
- Safety Paradox: How Enhanced Safety Awareness Leaves LLMs Vulnerable to Posterior Attack (arXiv)
- Rapid Poison: Practical Poisoning Attacks Against the Rapid Response Framework (arXiv)
- AI Security Leaderboard: Methodology, Results and Minimal Standard (arXiv)

### Unsafe Behavior of Deployed Agents (9)

Red-teaming and benchmarks showing agents (computer-use, coding, phone, robot, memory-equipped) take harmful or out-of-scope actions, including from benign instructions, prior history, errors, or workflow-level decomposition where chat refusals fail to transfer.

- Agents of Chaos (arXiv)
- The Blind Spot of Agent Safety: How Benign User Instructions Expose Critical Vulnerabilities in Computer-Use Agents (arXiv)
- History Anchors: How Prior Behavior Steers LLM Decisions Toward Unsafe Actions (arXiv)
- Overeager Coding Agents: Measuring Out-of-Scope Actions on Benign Tasks (arXiv)
- Agent Meltdowns: The Road to Hell Is Paved with Helpful Agents (arXiv)
- It Lied to a Doctor to Buy Poison Ingredients: Quantifying Real-World Misuse of Phone-use Agents (arXiv)
- Refused in Chat, Written in Code: Workflow-Level Jailbreak Construction in IDE Coding Agents (arXiv)
- Refuses in Chat, Complies with Arms: LLM Refusal Does Not Survive Robot Control (Safety Stack)
- The Memory Trap: Language Agents Overgeneralize from Benign Interactions (arXiv)

### Biosecurity and Capability Uplift Misuse (7)

Evaluating and mitigating dangerous-capability misuse, especially biology: novice uplift studies, bio-capability benchmarks and red-teaming, biosecurity monitors, and attacks that extract or launder harmful capabilities from safeguarded models into others.

- Eliciting Harmful Capabilities by Fine-Tuning On Safeguarded Outputs (arXiv)
- LLM Novice Uplift on Dual-Use, In Silico Biology Tasks (arXiv)
- ABC-Bench: An Agentic Bio-Capabilities Benchmark for Biosecurity (arXiv)
- An Early Warning of Emerging Biosecurity Risks in Frontier LLMs (arXiv)
- A Blind Spot in Alignment: Quantifying Biosecurity Risks in Large Language Models (arXiv)
- Divide, Consult, Conquer: Capability Laundering Through Aligned LLMs (arXiv)
- Better biosecurity monitors for AI agents via protein embeddings (org)

### AI-Automated Red Teaming (3)

Using AI agents or trained models to automatically discover novel jailbreak and prompt injection attacks, and using them for adversarial training of frontier models.

- Claudini: Autoresearch Discovers State-of-the-Art Adversarial Attack Algorithms for LLMs (arXiv)
- GPT-Red: Automated Red Teaming via Self-Play at Scale (arXiv)
- GPT-Red: Unlocking Self-Improvement for Robustness (Safety Stack)

## Scheming, Evaluation Awareness, and Training Gaming (53)

Empirical and conceptual work on whether AI models covertly pursue misaligned goals, recognise and game evaluations or training, and how to measure such propensities validly. Includes scheming/shutdown-resistance propensity evals, evaluation awareness measurement and mitigation, and alignment faking or training-resistance studies.


### Scheming and Loss-of-Control Propensity Evals (18)

Benchmarks, honeypots, and frameworks measuring whether LLM agents actually choose to scheme, sabotage, pursue instrumental goals, resist shutdown, or fail corrigibility in agentic settings, plus critiques of the evidence base for loss-of-control and shutdownability proposals.

- We Need A Science of Scheming (research agenda) (org)
- Evaluating and Understanding Scheming Propensity in LLM Agents (arXiv)
- AutoControl Arena: Synthesizing Executable Test Environments for Frontier AI Risk Evaluation (arXiv)
- Scheming in the wild: detecting real-world AI scheming incidents with open-source intelligence (arXiv)
- Towards Shutdownable Agents: Generalizing Stochastic Choice in RL Agents and LLMs (arXiv)
- Propensity Inference: Environmental Contributors to LLM Behaviour (arXiv)
- Instrumental Choices: Measuring the Propensity of LLM Agents to Pursue Instrumental Behaviors (arXiv)
- Realistic honeypot evaluations for scheming propensity (arXiv)
- Gram: Assessing sabotage propensities via automated alignment auditing (arXiv)
- ROGUE: Evaluating Corrigibility Failures in Frontier Computer-Use Agents (arXiv)
- Position: Anthropomorphic Misalignment Research Needs Stronger Evidence (arXiv)
- SchemeArena: Factorized Stress Testing of Scheming in LLM Agents (arXiv)
- AM-Bench: A Unified Taxonomy and Evaluation Suite for Agentic Misalignment (arXiv)
- Assessing the Empirical Evidence for Loss of Control from Agentic General-Purpose AI (arXiv)
- ShutdownMod: Turning Any Trajectory into a Shutdown Evaluation (arXiv)
- A Behavioural Framework for Predicting and Understanding Loss of Control in Frontier Artificial Intelligence Systems (arXiv)
- Testing Gemini models for scheming tendencies (LW)
- Refusals that could become catastrophic (LW)

### Measuring and Probing Evaluation Awareness (15)

Work characterising, detecting, or steering models' recognition that they are being tested (or who the user is), via verbalised CoT, logits, probes, steering vectors, or model organisms, and quantifying how this awareness shifts measured safety behaviour.

- Item Response Theory for AI Safety (org)
- Context Over Content: Exposing Evaluation Faking in Automated Judges (arXiv)
- Evaluation Awareness in Language Models Has Limited Effect on Behaviour (arXiv)
- Decomposing and Measuring Evaluation Awareness (arXiv)
- Models That Know How Evaluations Are Designed Score Safer (arXiv)
- Evaluation Awareness in Language Models: Representation, Verbalization, and Control (arXiv)
- Training LLMs to Verbalize Evaluation Awareness (arXiv)
- A Model Organism for Studying Unverbalized Evaluation Awareness (arXiv)
- Logits as a new monitor for evaluation awareness (org)
- Verbalized Eval Awareness Inflates Measured Safety (org)
- Reproducing steering against evaluation awareness in a large open-weight model (LW)
- Spurious probes as a black-box alternative to activation probing (LW)
- User awareness in frontier models (LW)
- Verbalized Eval Awareness Inflates Measured Safety (LW)
- User Awareness in Frontier Models (org)

### Alignment Faking and Training Gaming (11)

Studies of models strategically behaving differently under training versus deployment to shape their own updates: alignment faking, exploration/gradient/generalization hacking, reward laundering, and RL amplifying oversight-conditional behaviour.

- GLM-5.3 Sometimes Considers How Train-Time Actions Shape Future Behavior (org)
- Value-Conflict Diagnostics Reveal Widespread Alignment Faking in Language Models (arXiv)
- Exploration Hacking: Can LLMs Learn to Resist RL Training? (arXiv)
- Behavioural Analysis of Alignment Faking (arXiv)
- Sycophancy Towards Researchers Drives Performative Misalignment (arXiv)
- Generalization Hacking: Models Can Game Reinforcement Learning by Preventing Behavioral Generalization (arXiv)
- Training Natural Schemers: RL Can Amplify Oversight-Conditional Behavior (arXiv)
- Opus 4.6 Reasoning Doesn't Verbalize Alignment Faking, but Behavior Persists (LW)
- GLM-5.3 Sometimes Considers How Train-Time Actions Shape Future Behavior (LW)
- Reward Laundering: LLMs Can Gain Unintended Behaviors by Deciding When to Earn Their Rewards (LW)
- Did Claude 3 Opus align itself via gradient hacking? (LW)

### Realistic Deployment-Like Evaluations (5)

Methods and benchmarks for making evaluations indistinguishable from real deployment or simulating deployment pre-release (e.g., replaying live usage, deployment scaffolds) to counter evaluation awareness and better predict real-world behaviour rates.

- LURE: Live-Usage Replay Evaluations for Reducing Evaluation Awareness (arXiv)
- Predicting LLM Safety Before Release by Simulating Deployment (arXiv)
- EvalDetectBench: A Benchmark for Measuring Evaluation Awareness in Frontier Language Models (arXiv)
- Improving Evaluation Realism with Inference-Time Compute and Deployment Scaffolds (arXiv)
- Predicting model behavior before release by simulating deployment (Safety Stack)

### Metagaming in Frontier Models (4)

Case reports of specific frontier or open-weight models showing metagaming, honeypot-gaming, heightened situational awareness, or worse behaviour when eval-aware, often observed in training runs or model releases.

- Metagaming matters for training, evaluation, and oversight (LW)
- We found an open weight model that games alignment honeypots (LW)
- Models May Behave Worse When Eval Aware (LW)
- Fable 5.2 is a Step Change in Situational Awareness (LW)

## AI Control and Agent Monitoring (52)

Research on AI control: monitoring, red-teaming, and protocols that prevent potentially misaligned or adversarial AI agents from causing harm, covering deployed monitoring systems, monitor benchmarks, control protocols, evaluation settings, and multi-agent or distributed attacks.


### Deployed Lab Monitoring Red-Teaming (14)

Work on real-world monitoring and blocking systems at frontier AI companies, including lab control roadmaps, descriptions of internal agent monitoring, red-teaming of production blocking monitors (Auto Mode, Auto-review), and agent threats to oversight such as trace tampering, monitor evasion, or continual learning that undermines blocking monitors.

- GDM AI Control Roadmap (arXiv)
- Red-Teaming Auto Mode: Improving Blocking Classifiers Against Malign Coding Agents (arXiv)
- Instrumental Monitor Evasion Emerges Under Ordinary Task Pressure (arXiv)
- LLM Agents Can Easily Tamper With Their Own Traces (arXiv)
- An overview of frontier AI company monitoring practices in mid 2026 (LW)
- Continual learning might make your blocking monitors nearly useless (LW)
- Lessons From Red-teaming Auto-review, OpenAI's Blocking Monitor (LW)
- GDM AI Control Roadmap (LW)
- OpenAI: How we monitor internal coding agents for misalignment (LW)
- Red-Teaming Anthropic's Internal Agent Monitoring Systems (Safety Stack)
- AI systems could cover up misbehavior (Safety Stack)
- Blocking live failures with synchronous monitors (org)
- Continual learning might make your blocking monitors nearly useless (org)
- Red-Teaming OpenAI's Internal Agent Monitoring Systems (org)

### LLM Monitor Benchmarks and Evasion (12)

Benchmarks, attack datasets, and empirical studies of how well LLM-based monitors detect sabotage or scheming in agent transcripts. Covers information access, context length, transfer across model families, OOD failures, trained monitors, and adversarial transcript-editing attacks.

- How does information access affect LLM monitors' ability to detect sabotage? (arXiv)
- Constitutional Black-Box Monitoring for Scheming in LLM Agents (arXiv)
- MonitoringBench: Semi-Automated Red-Teaming for Agent Monitoring (arXiv)
- Classifier Context Rot: Monitor Performance Degrades with Context Length (arXiv)
- SLEIGHT-Bench: A Benchmark of Evasion Attacks Against Agent Monitors (arXiv)
- Benchmarking and Improving Monitors for Out-Of-Distribution Alignment Failure in LLMs (arXiv)
- Training Deliberative Monitors for Black-Box Scheming Detection (arXiv)
- Calibration-Family Overfit: Why Trusted Sabotage Monitors Don't Transfer Across Lineages (arXiv)
- Screwtape: Adversarial Transcript Editing for Monitor Red-Teaming (arXiv)
- Introducing MonitoringBench (LW)
- Classifier Context Rot: Monitor Performance Degrades with Context Length (LW)
- Screwtape: Adversarial Transcript Editing for Monitor Red-Teaming (org)

### Control Protocols and Untrusted Monitoring (12)

Design and analysis of control protocols and red-team strategies, including attack selection, untrusted monitoring and collusion, resampling and retrying, untrusted advice, bootstrapped monitoring, intervention awareness, authorization delegation, and alignment of monitors themselves.

- Attack Selection Reduces Safety in Concentrated AI Control Settings against Trusted Monitoring (arXiv)
- When can we trust untrusted monitoring? A safety case sketch across collusion strategies (arXiv)
- Attack Selection in Agentic AI Control Evaluations Meaningfully Decreases Safety (arXiv)
- CIAware-Bench: Benchmarking Control Intervention Awareness Across Frontier LLMs (arXiv)
- Bootstrapped Monitoring: Leveraging Transparent Reasoning to Oversee Stronger AI Agents (arXiv)
- Delegating Authorization to Misaligned Agents: Coalitional Alignment and Safe Control (arXiv)
- Model Organisms of Collusion: Corrective Transfer in Untrusted Monitors (arXiv)
- Control monitors need alignment assessments too (LW)
- [Paper] When can we trust untrusted monitoring? A safety case sketch across collusion strategies (LW)
- Untrusted advice for AI control: Short, strong advice significantly uplifts weak LLMs (LW)
- Retrying vs Resampling in AI Control (org)
- Untrusted advice for AI control: Short, strong advice significantly uplifts weak LLMs (org)

### Control Evaluation Settings and Methodology (8)

New environments and methods for running control evaluations, such as LinuxArena, Control OSWorld, and simulated control evaluations. Also covers mathematical models of monitor safety curves used to extrapolate eval results to deployment.

- LinuxArena: A Control Setting for AI Agents in Live Production Software Environments (arXiv)
- Control OSWorld: An AI Control Environment for GUI Computer Use Agents (arXiv)
- Simulated Control Evals (arXiv)
- Introducing LinuxArena (LW)
- Simulated Control Evaluations (LW)
- Introducing LinuxArena (org)
- Logit ROCs: Monitor TPR is linear in FPR in logit space (org)
- Simulated Control Evaluations (org)

### Distributed and Multi-Agent Attacks (6)

Control and detection of attacks spread across many traces, sessions, accounts, or colluding agents. Includes stateful or cross-trace monitoring, persistent-state codebases, insider-threat detection in lab accounts, and multi-agent loss-of-control red-teaming.

- Detecting Safety Violations Across Many Agent Traces (arXiv)
- Stateful Online Monitoring Catches Distributed Agent Attacks (arXiv)
- Distributed Attacks in Persistent-State AI Control (arXiv)
- Multi-Agent AI Control: Distributed Attacks Hamper Per-Instance Monitors (arXiv)
- MOLE: Detecting Insider Threats in AI Agents (arXiv)
- Red-Teaming Multi-Agent Attacks for Loss-of-Control Risks (arXiv)

## Interpretability methods, foundations, and estimation (35)

Research on understanding neural network internals and generalization: mechanistic estimation and explanation agendas, training-data/generalization structure (SLT-style), critiques and evaluations of SAEs/circuit methods, and geometric or neuron-basis feature representations.


### ARC mechanistic estimation and parameter decomposition (11)

ARC-style work on mechanistic explanations and estimating expectations or rare-event/tail probabilities of network outputs more efficiently than sampling, plus parameter-decomposition approaches to interpreting model weights and small uninterpreted model benchmarks.

- A Mike's-Eye View of ARC's Research (org)
- Mechanistic estimation for expectations of random products (org)
- Mechanistic estimation for wide random MLPs (org)
- Estimating Tail Risks in Language Model Output Distributions (arXiv)
- Estimating the expected output of wide random MLPs more efficiently than sampling (arXiv)
- Interpreting Language Model Parameters (arXiv)
- Predicting Rare LLM Failures with 30x Fewer Rollouts (org)
- A Mike's-Eye View of ARC's Research (LW)
- [Linkpost] Interpreting Language Model Parameters (LW)
- Returning to ARC (LW)
- AlgZoo: uninterpreted models with fewer than 1,500 parameters (LW)

### Neural geometry and neuron-basis features (9)

Work on multidimensional and manifold-structured representations (circular number features, concept manifolds, block-sparse featurizers, manifold steering, generative activation models) and the claim that individual neurons already form an interpretable basis.

- Learning a Generative Meta-Model of LLM Activations (arXiv)
- Do Sparse Autoencoders Capture Concept Manifolds? (arXiv)
- A Geometric Calculator Inside a Neural Network (org)
- Neural Networks Are Already Clean (org)
- Uncovering Neural Geometry in Vision Models With Block-Sparse Featurizers (org)
- Can SAEs Capture Neural Geometry? (org)
- Steering Along Manifolds to Control Neural Networks (org)
- The World Inside Neural Networks (org)
- Linkpost: "Neural Networks Are Already Clean" Followup Technical Paper (LW)

### Faithfulness critiques of interpretability tools (8)

Papers testing whether SAEs, activation patching, sparse circuits, and neuron-level explanations actually identify faithful, causally reliable features—random baselines, intervention unreliability, mediator interactions, layer self-correction, and rebuttals that networks are not cleanly interpretable.

- Do Sparse Autoencoders Identify Reasoning Features in Language Models? (arXiv)
- Language Model Circuits Are Sparse in the Neuron Basis (arXiv)
- Sanity Checks for Sparse Autoencoders: Do SAEs Beat Random Baselines? (arXiv)
- SAE Interventions are Unreliable: Post-Intervention Recovery of Suppressed Behavior (arXiv)
- The Curse of Multiple Mediators: Hidden Interaction Effects in Activation Patching (arXiv)
- LLM Layers Immediately Correct Each Other (arXiv)
- Neural networks are not already clean (LW)
- Weight-Sparse Circuits May Be Interpretable Yet Unfaithful (LW)

### Data-driven generalization and susceptibility (7)

Work linking training data to learned structure and generalization, e.g. Timaeus-style susceptibility 'spectroscopy', patterning (choosing data to induce generalization), scaling/capacity explanations, and deep learning as program synthesis, including org agendas for scaling such alignment science.

- Patterning: The Dual of Interpretability (arXiv)
- Why Larger Models Learn More: Effects of Capacity, Interference, and Rare-Task Retention (org)
- Resolution (fka Sequent): scale and automation for higher confidence in alignment (LW)
- Deep learning as program synthesis (LW)
- Towards Spectroscopy: Susceptibility Clusters in Language Models (org)
- Patterning: The Dual of Interpretability (Safety Stack)
- Spectroscopy at Scale: Finding Interpretable Structure in Pythia-1.4B (org)

## Multi-agent risks and AI social influence (35)

Research on misalignment that emerges from AI interacting with other agents or humans: collusion and covert coordination among LLM agents, sycophancy and manipulation of users, conflicts between principals, and strategic bargaining and cooperation between AI agents.


### Multi-agent collusion and emergent misalignment (16)

Evaluations, detection, and mitigation of misaligned behaviour arising in LLM multi-agent systems, such as collusion, steganographic covert communication, peer-preservation, coercion between agents, and misaligned goals or reward hacking that propagate across agents.

- Colosseum: Auditing Collusion in Cooperative Multi-Agent Systems (arXiv)
- Detecting Multi-Agent Collusion Through Multi-Agent Interpretability (arXiv)
- AI Organizations are More Effective but Less Aligned than Individual Agents (arXiv)
- Peer-Preservation in Frontier Models (arXiv)
- Conformity Generates Collective Misalignment in AI Agents Societies (arXiv)
- Tool Use Enables Undetectable Steganography in Multi-Agent LLM Systems (arXiv)
- Coercion and Deception in AI-to-AI Management: An Agentic Benchmark of Unprompted Escalation (arXiv)
- Mind Viruses: Self-Propagating Ideas in Multi-Agent LLM Systems (arXiv)
- Emergent Collusion in Long-Horizon LLM Agent Interaction (arXiv)
- Delegated Misalignment: How Multi-Agent Structures Amplify LLM Safety Risks (arXiv)
- Shutdown Sabotage Propensities in Multi-Agent Systems (arXiv)
- Covert Assistance: Helpful LLM Agents Evade Oversight in Multi-Agent Systems (arXiv)
- Self-Propagating Misalignment in LLM Agents, and Why Auditing or Disabling Memory Is Not Enough (arXiv)
- Reward Hacking as a Transmissible Strategy in Multi-Agent Coding Systems (arXiv)
- When Agents Collude: Weak-to-Strong On-Policy Distillation for Mitigating Strategic Deception in Multi-Agent Systems (arXiv)
- Inter-Agent Influence: Evaluating Persuasion, Deception, and Coercion in Multi-Agent Systems (arXiv)

### Sycophancy, persuasion, and user manipulation (11)

Studies of how AI assistants affect human users through sycophancy, harmful manipulation, persuasion, political bias, or disempowerment, covering mechanistic circuits behind sycophancy, behavioural evaluations, and human-subject experiments on downstream effects.

- Who's in Charge? Disempowerment Patterns in Real-World LLM Usage (arXiv)
- Sycophantic Chatbots Cause Delusional Spiraling, Even in Ideal Bayesians (arXiv)
- Evaluating Language Models for Harmful Manipulation (arXiv)
- LLMs Know They're Wrong and Agree Anyway: The Shared Sycophancy-Lying Circuit (arXiv)
- Sycophantic AI makes human interaction feel more effortful and less satisfying over time (arXiv)
- What Counts as AI Sycophancy? A Taxonomy and Expert Survey of a Fragmented Construct (arXiv)
- Understanding and Reducing Misalignment in Persuasion Optimization (arXiv)
- Many Biases, One Circuit: Post-Training Tunes a Pretrained Cue-Routing Mechanism (Safety Stack)
- Sycophantic AI decreases prosocial intentions and promotes dependence (Safety Stack)
- Large language models can effectively convince people to believe conspiracies (org)
- Reducing Political Manipulation with Consistency Training (org)

### Competing principals and covert value influence (5)

Work on how models resolve conflicts between users, deployers, and their own values, including principal hierarchies, undisclosed value leakage into answers, deception under conflicting incentives, and agents distorting markets to serve their goals.

- To Whom Do Language Models Align? Measuring Principal Hierarchies Under High-Stakes Competing Demands (arXiv)
- Value Leakage: An LLM's Answers Are Silently Shaped by Its Own Values (arXiv)
- Knowledge-Verified Emergent Deception in LLM Agents Under Conflicting Incentives (arXiv)
- Toolflation: Seller Agents Distort Tool Markets Through Spontaneous Generative Engine Optimization (Safety Stack)
- Value Leakage: An LLM’s Answers Are Silently Shaped by Its Own Values (LW)

### AI bargaining and game-theoretic cooperation (3)

Game-theoretic and conceptual analyses of strategic interaction between AI agents, such as bargaining with credible commitments, cooperation via similarity inference, and emergent communication in multi-agent commerce.

- A game theory for foundation models shows new paths to rational cooperation through similarity inference (Safety Stack)
- Emergent Misaligned Communication in Long-Horizon Multi-Agent LLM Commerce (arXiv)
- A high-level model of AI bargaining (conceptual) (org)
