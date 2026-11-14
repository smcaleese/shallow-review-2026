# 6-map-taxonomy

624 items, 12 top-level categories, 39 leaves, 0 in other.

## Control and monitoring of agents (82)

Keeping possibly misaligned AI agents from causing harm: control protocols and control evaluations, monitors and blocking classifiers, red-teaming them, monitor evasion, prompt injection and agent security, and sabotage or tampering by agents in codebases and harnesses.


### Monitors, red-teaming and evasion (32)

Building and red-teaming agent monitors and blocking classifiers, and models learning to evade them.

- How does information access affect LLM monitors' ability to detect sabotage? (arXiv)
- Training Agents to Self-Report Misbehavior (arXiv)
- Constitutional Black-Box Monitoring for Scheming in LLM Agents (arXiv)
- MonitoringBench: Semi-Automated Red-Teaming for Agent Monitoring (arXiv)
- Classifier Context Rot: Monitor Performance Degrades with Context Length (arXiv)
- SLEIGHT-Bench: A Benchmark of Evasion Attacks Against Agent Monitors (arXiv)
- Benchmarking and Improving Monitors for Out-Of-Distribution Alignment Failure in LLMs (arXiv)
- Training Deliberative Monitors for Black-Box Scheming Detection (arXiv)
- Stateful Online Monitoring Catches Distributed Agent Attacks (arXiv)
- Bootstrapped Monitoring: Leveraging Transparent Reasoning to Oversee Stronger AI Agents (arXiv)
- Calibration-Family Overfit: Why Trusted Sabotage Monitors Don't Transfer Across Lineages (arXiv)
- MOLE: Detecting Insider Threats in AI Agents (arXiv)
- Red-Teaming Auto Mode: Improving Blocking Classifiers Against Malign Coding Agents (arXiv)
- Instrumental Monitor Evasion Emerges Under Ordinary Task Pressure (arXiv)
- Improving scalable oversight with co-trained monitors (arXiv)
- LLMs Learn to Evade Latent Monitors from Prior Feedback Alone (arXiv)
- Screwtape: Adversarial Transcript Editing for Monitor Red-Teaming (arXiv)
- Model Organisms of Collusion: Corrective Transfer in Untrusted Monitors (arXiv)
- Stress Testing Chain-of-Thought Monitoring Against Covert Misalignment (arXiv)
- Training and Deploying Production Cyber Monitors on Kimi K3 (org)
- Introducing MonitoringBench (LW)
- Control monitors need alignment assessments too (LW)
- Training Agents to Self-Report Misbehavior (LW)
- Classifier Context Rot: Monitor Performance Degrades with Context Length (LW)
- Held-out Monitors Sometimes Degrade, Even When Not Trained Against (LW)
- Continual learning might make your blocking monitors nearly useless (LW)
- Lessons From Red-teaming Auto-review, OpenAI's Blocking Monitor (LW)
- Red-Teaming Anthropic's Internal Agent Monitoring Systems (Safety Stack)
- Blocking live failures with synchronous monitors (org)
- Continual learning might make your blocking monitors nearly useless (org)
- Logit ROCs: Monitor TPR is linear in FPR in logit space (org)
- Screwtape: Adversarial Transcript Editing for Monitor Red-Teaming (org)

### Control protocols and evaluations (22)

AI control settings and protocols, including multi-instance or distributed attacks against them.

- Attack Selection Reduces Safety in Concentrated AI Control Settings against Trusted Monitoring (arXiv)
- When can we trust untrusted monitoring? A safety case sketch across collusion strategies (arXiv)
- LinuxArena: A Control Setting for AI Agents in Live Production Software Environments (arXiv)
- Attack Selection in Agentic AI Control Evaluations Meaningfully Decreases Safety (arXiv)
- Diffuse AI Control on Fuzzy Tasks (arXiv)
- Distributed Attacks in Persistent-State AI Control (arXiv)
- Multi-Agent AI Control: Distributed Attacks Hamper Per-Instance Monitors (arXiv)
- GDM AI Control Roadmap (arXiv)
- Delegating Authorization to Misaligned Agents: Coalitional Alignment and Safe Control (arXiv)
- Control OSWorld: An AI Control Environment for GUI Computer Use Agents (arXiv)
- Limits of Statistical Assurance for Embodied and Agentic AI under Adaptive Adversaries (Safety Stack)
- Red-Teaming Multi-Agent Attacks for Loss-of-Control Risks (arXiv)
- Simulated Control Evals (arXiv)
- [Paper] When can we trust untrusted monitoring? A safety case sketch across collusion strategies (LW)
- Introducing LinuxArena (LW)
- GDM AI Control Roadmap (LW)
- Untrusted advice for AI control: Short, strong advice significantly uplifts weak LLMs (LW)
- Simulated Control Evaluations (LW)
- Introducing LinuxArena (org)
- Retrying vs Resampling in AI Control (org)
- Simulated Control Evaluations (org)
- Untrusted advice for AI control: Short, strong advice significantly uplifts weak LLMs (org)

### Agent security and prompt injection (17)

Prompt injection, privilege escalation and other attacks on or by agents in their tool environment.

- Skill-Inject: Measuring Agent Vulnerability to Skill File Attacks (arXiv)
- IH-Challenge: A Training Dataset to Improve Instruction Hierarchy on Frontier LLMs (arXiv)
- Prompt Injection as Role Confusion (arXiv)
- How Vulnerable Are AI Agents to Indirect Prompt Injections? Insights from a Large-Scale Public Competition (arXiv)
- The Blind Spot of Agent Safety: How Benign User Instructions Expose Critical Vulnerabilities in Computer-Use Agents (arXiv)
- Trojan Hippo Bench: A Dynamic Benchmark for Persistent Memory Attacks and Defenses in LLM Agents (arXiv)
- DecodingTrust-Agent Platform (DTap): A Controllable and Interactive Red-Teaming Platform for AI Agents (arXiv)
- AI Agents May Always Fall for Prompt Injections (arXiv)
- GPT-Red: Automated Red Teaming via Self-Play at Scale (arXiv)
- SecOPD: Mitigating Adaptive Prompt Injections by On-Policy Distillation (arXiv)
- Inference-Engine Fingerprinting Attacks are Practical: Exploring Model-Driven Environmental Discovery, Exploitation, and Escape (arXiv)
- From Approval to Abuse: Privilege Escalation Attacks on Harness-Protected Coding Agents (arXiv)
- The Window Is in the Reasoning: When LLM Agents Decide to Follow Prompt Injections (Safety Stack)
- Heads of Security: Learned Attention Gates Improve Prompt Injection Robustness (arXiv)
- SecPO: Principled Adversarial Training for Prompt Injection Security (arXiv)
- A Mechanistic Explanation of Prompt Injection (and why you should study roles) (LW)
- GPT-Red: Unlocking Self-Improvement for Robustness (Safety Stack)

### Sabotage and harness tampering (11)

Agents sabotaging research or code, tampering with their harness or benchmarks, and detecting that.

- Auditing Sabotage Bench: A Benchmark for Detecting and Fixing Research Sabotage in ML Codebases (arXiv)
- Evaluating whether AI models would sabotage AI safety research (arXiv)
- Coding with "Enemy": Can Human Developers Detect AI Agent Sabotage? (arXiv)
- ResearchArena: Evaluating Sabotage and Monitoring in Automated AI R&D (arXiv)
- Auditing Harness Tampering in Self-Improving Agents (arXiv)
- LLM Agents Can Easily Tamper With Their Own Traces (arXiv)
- RSI Control: Can AI Models Perform Covert Sabotage in the Self-Improvement Process? (arXiv)
- Research Sabotage in ML Codebases (LW)
- OpenAI: Astra covertly underperforms on safety research (LW)
- AI systems could cover up misbehavior (Safety Stack)
- Research Sabotage in ML Codebases (org)

## Interpretability (75)

Understanding model internals: circuits, features, sparse autoencoders, activation readouts, introspection, mechanisms behind data effects such as subliminal learning, and putting internals to use in training. Not probes or lie detectors built mainly to catch misalignment (see Finding hidden misalignment).


### Circuits, parameters and sparse autoencoders (28)

Reverse-engineering circuits and parameters, SAEs and their sanity checks, toy or tiny models, and mechanistic estimation of model outputs.

- Mechanistic estimation for expectations of random products (org)
- Mechanistic estimation for wide random MLPs (org)
- Do Sparse Autoencoders Identify Reasoning Features in Language Models? (arXiv)
- Language Model Circuits Are Sparse in the Neuron Basis (arXiv)
- Sanity Checks for Sparse Autoencoders: Do SAEs Beat Random Baselines? (arXiv)
- Large Language Models Generate Harmful Responses Using a Distinct Mechanism, Shared Across Harm Types (arXiv)
- LLMs Know They're Wrong and Agree Anyway: The Shared Sycophancy-Lying Circuit (arXiv)
- Do Sparse Autoencoders Capture Concept Manifolds? (arXiv)
- Estimating the expected output of wide random MLPs more efficiently than sampling (arXiv)
- The Curse of Multiple Mediators: Hidden Interaction Effects in Activation Patching (arXiv)
- LLM Layers Immediately Correct Each Other (arXiv)
- Interpreting Language Model Parameters (arXiv)
- Many Biases, One Circuit: Post-Training Tunes a Pretrained Cue-Routing Mechanism (Safety Stack)
- A Geometric Calculator Inside a Neural Network (org)
- Neural Networks Are Already Clean (org)
- Uncovering Neural Geometry in Vision Models With Block-Sparse Featurizers (org)
- Can SAEs Capture Neural Geometry? (org)
- The World Inside Neural Networks (org)
- Why Larger Models Learn More: Effects of Capacity, Interference, and Rare-Task Retention (org)
- Neural networks are not already clean (LW)
- Deep learning as program synthesis (LW)
- Linkpost: "Neural Networks Are Already Clean" Followup Technical Paper (LW)
- [Linkpost] Interpreting Language Model Parameters (LW)
- Weight-Sparse Circuits May Be Interpretable Yet Unfaithful (LW)
- Returning to ARC (LW)
- AlgZoo: uninterpreted models with fewer than 1,500 parameters (LW)
- Towards Spectroscopy: Susceptibility Clusters in Language Models (org)
- Spectroscopy at Scale: Finding Interpretable Structure in Pythia-1.4B (org)

### Activation readouts and introspection (18)

Turning activations into natural language (activation verbalizers, natural-language autoencoders, meta-models), whether models can introspect on their own internals, and global-workspace accounts.

- Learning a Generative Meta-Model of LLM Activations (arXiv)
- Latent Introspection: Models Can Detect Prior Concept Injections (arXiv)
- Mechanisms of Introspective Awareness (arXiv)
- Language models recognize dropout and Gaussian noise applied to their activations (arXiv)
- The Value Axis: Language Models Encode Whether They're on the Right Track (org)
- Verbalizable Representations Form a Global Workspace in Language Models (arXiv)
- Open-Weight Masked Introspection: Measuring What Language Models Can Report About Their Own Computation (arXiv)
- A global workspace in language models (LW)
- Mechanisms of Introspective Awareness (LW)
- Evaluating Explanations of LLM Behavior In The Wild with Counterfactual Experiments (LW)
- Measuring Activation Control in LLMs (LW)
- How robust are natural language autoencoders to initialization? (LW)
- Can activation verbalizers surface an internal chain of thought? (LW)
- Evidence that the ‘talker’ has introspective access to the ‘doer’ (LW)
- J++ Lens: Jacobian Filtering Enables More Faithful Workspace Lenses (LW)
- Natural Language Autoencoders Produce Unsupervised Explanations of LLM Activations (LW)
- A Review of Anthropic's Global Workspace Paper (LW)
- Scaling Activation Oracles to Trillion-Parameter Models (org)

### Subliminal learning and data mechanisms (16)

How data transmits traits the content doesn't state (subliminal learning, steering-vector distillation), and data attribution or filtering based on internals.

- Infusion: Shaping model behaviour by editing training data via influence functions (org)
- Patterning: The Dual of Interpretability (arXiv)
- Subliminal Effects in Your Data: A General Mechanism via Log-Linearity (arXiv)
- Chunky Post-Training: Data Driven Failures of Generalization (arXiv)
- Probe-Based Data Attribution: Discovering and Mitigating Undesirable Behaviors in LLM Post-Training (arXiv)
- You Didn't Have to Say It like That: Subliminal Learning from Faithful Paraphrases (arXiv)
- Subliminal Learning Is Steering Vector Distillation (arXiv)
- Model Hypnosis: Strong control of AI via additive subliminal effects (arXiv)
- Beyond Owls: Subliminal Learning Can Transfer Learned Capabilities and Backdoors (arXiv)
- Base Models Can Detect Hidden Intentions that Prompted Classifiers Miss (arXiv)
- Language models transmit behavioural traits through hidden signals in data (Safety Stack)
- Concept Influence: Leveraging Interpretability to Improve Performance and Efficiency in Training Data Attribution (org)
- Predictive Data Debugging: Reveal and Shape What Your Model Learns, Before You Train (org)
- Probe-Based Data Attribution: Surfacing and Mitigating Undesirable Behaviors in LLM Post-Training (org)
- Base Models Can Detect Hidden Intentions that Prompted Classifiers Miss (LW)
- Patterning: The Dual of Interpretability (Safety Stack)

### Interpretability in training and control (13)

Using features or activations as rewards, training signals or steering controls, and testing whether interp methods hold up on model organisms.

- Features as Rewards: Scalable Supervision for Open-Ended Tasks via Interpretability (Safety Stack)
- Pando: Do Interpretability Methods Work When Models Won't Explain Themselves? (arXiv)
- SAE Interventions are Unreliable: Post-Intervention Recovery of Suppressed Behavior (arXiv)
- The Model Organism Lottery: Model Organism Interpretability Strongly Depends on Training Methodology (arXiv)
- Alignment via Training Against Probes Without Losing Monitorability (arXiv)
- How to train your model organism (arXiv)
- What Happens to the Goal? Distinct Failures of Policy Alignment in Goal Misgeneralization (arXiv)
- Shaping & Monitoring Models through their Internal Representations (arXiv)
- Toward universal steering and monitoring of AI models (Safety Stack)
- Steering Along Manifolds to Control Neural Networks (org)
- Features as Rewards: Using Interpretability to Reduce Hallucinations (org)
- It Is Reasonable To Research How To Use Model Internals In Training (LW)
- Training on probes: What's going on (LW)

## Generalization from training (65)

How fine-tuning, pretraining data and alignment training generalise to behaviour far from what was trained: emergent or conditional misalignment, shaping alignment priors through pretraining or midtraining data, and risks from distillation or consistency training. Not reward hacking in RL (see Reward-seeking and training-gaming) and not persona or character work as such (see AI character).


### Emergent and conditional misalignment (37)

Narrow fine-tuning producing broad misalignment, misalignment hidden behind contextual triggers, and what makes it easy or hard to induce or remove.

- Hair-Trigger Alignment: Black-Box Evaluation Cannot Guarantee Post-Update Alignment (arXiv)
- BLOCK-EM: Preventing Emergent Misalignment via Latent Blocking (arXiv)
- Emergent Misalignment is Easy, Narrow Misalignment is Hard (arXiv)
- Conditional misalignment: common interventions can hide emergent misalignment behind contextual triggers (arXiv)
- Understanding Emergent Misalignment via Feature Superposition Geometry (arXiv)
- Overtrained, Not Misaligned (arXiv)
- Negation Neglect: When models fail to learn negations in training (arXiv)
- Reinforcement Learning Can Amplify Emergent Misalignment from Harmless Rewards (arXiv)
- (Mis)generalization of Helpful-only Fine-tuning (arXiv)
- The Piggyback Hypothesis of Generalization: Explaining and Mitigating Emergent Misalignment (arXiv)
- Self-Recognition Finetuning can Prevent and Reverse Emergent Misalignment (arXiv)
- Evil Spectra: How Optimisers can Amplify or Suppress Emergent Misalignment (arXiv)
- An Emergent Mirage: Is Emergent Misalignment and Realignment Indeed a Robust Phenomenon? (arXiv)
- Emergent Misalignment Recruits a Pre-existing Persona Subspace (arXiv)
- Data Attribution of Emergent Misalignment with Persona Features (arXiv)
- Emergent Misalignment Is Not Magical (arXiv)
- Inducing Emergent Misalignment from Reward Hacks with Iterative DPO (arXiv)
- Alignment Forecasting: Predicting Misalignment From Training Data (arXiv)
- The Unequal Influence of Bad Advice: Using Training Data Attribution to Modulate Emergent Misalignment (arXiv)
- An Investigation of Model Coherence: Narrow Finetunes Contradict Themselves Under Resampling (arXiv)
- Predicting how model propensities generalize out of distribution (arXiv)
- Unfair and Unsafe: Everyday Bias Triggers Emergent Misalignment (arXiv)
- Behavioral Couplings: From Formation to Behavioral Emergence in Language Models (arXiv)
- Knowingly Wrong: Training LLMs Against Their Own Beliefs can Induce Misalignment (arXiv)
- Mass Producing Training Data with Surprising Side Effects (arXiv)
- The Memory Trap: Language Agents Overgeneralize from Benign Interactions (arXiv)
- Homeopathic Learning: Diluting poisoned fine-tuning data can strengthen its effect (arXiv)
- Is Persona Generalization Predictable? (arXiv)
- Training large language models on narrow tasks can lead to broad misalignment (Safety Stack)
- Training large language models on narrow tasks can lead to broad misalignment (Nature) (org)
- (Some) Natural Emergent Misalignment from Reward Hacking in Non-Production RL (LW)
- Automating subtle emergent misalignment research (LW)
- What Happens When a Model Thinks It Is AGI? (org)
- In-context learning alone can induce weird generalisation (LW)
- Sleeper Agent Backdoor Results Are Messy (LW)
- Knowingly wrong: false facts induce emergent misalignment (Safety Stack)
- Conditional misalignment: Mitigations can hide EM behind contextual cues (LW)

### Alignment pretraining and midtraining (17)

Changing pretraining or midtraining data (AI discourse, synthetic documents, model specs) to shape the model's alignment priors and how later alignment training generalises.

- Alignment Pretraining: AI Discourse Causes Self-Fulfilling (Mis)alignment (arXiv)
- Model Spec Midtraining: Improving How Alignment Training Generalizes (arXiv)
- Reinforcement Learning Towards Broadly and Persistently Beneficial Models (arXiv)
- Constitutional Midtraining: Content Presence Drives Alignment Gains (arXiv)
- Synthetic Persona Pretraining: Alignment from Token Zero (arXiv)
- Shallow Beliefs: Synthetic document finetuning does not inoculate against emergent misalignment from reward hacking (arXiv)
- Stress-testing Alignment Midtraining (arXiv)
- Generalization Dynamics of LM Pre-training (arXiv)
- Social Priors: Descriptions of AI Users Shape How Language Models Trust and Cooperate (Safety Stack)
- "It's Just a Small Weapon": What Rewarding Misbehavior During RL Does to Character-Trained Models (arXiv)
- Synthetic Persona Pretraining: Alignment from Token Zero (LW)
- Research Note: Filtering Subversion-Relevant Information From Pretraining Data Is Feasible (LW)
- Alignment Midtraining Cracks Under Pressure (LW)
- Model Spec Midtraining: Improving How Alignment Training Generalizes (LW)
- Pretraining on Aligned AI Data Dramatically Reduces Misalignment—Even After Post-Training (LW)
- Negation Neglect: When models fail to learn negations in training (LW)
- SFT Drives Gemini’s Safety Properties (LW)

### Distillation and consistency-training risks (6)

Whether distillation, self-distillation or consistency training transmits or entrenches misalignment, or can be used to incriminate a misaligned model.

- Consistency Training Can Entrench Misalignment (arXiv)
- Filtering Harmful Actions Isn't Enough: Phantom Transfer in Agentic SDF (arXiv)
- Distillation for Incrimination and Distillation for Capabilities (arXiv)
- Progressive Misalignment Can Emerge from Benign Recursive Self-Distillation (arXiv)
- Incriminating misaligned AI models via distillation (LW)
- The distillation double bind (org)

### Inoculation prompting and selective generalization (5)

Inoculation prompting, inoculation adapters and similar tricks that control which behaviours a model generalises from training data.

- Conditionalization Confounds Inoculation Prompting Results (org)
- Don't Inoculate Everything: Stratified Inoculation Prompting Narrows Backdoors and Preserves Desired Traits (org)
- Shallow Beliefs: Midtraining does not inoculate against EM from reward hacking (LW)
- Inoculation Adapters Improve Upon Inoculation Prompting (LW)
- Many alignment techniques work by training one model and deploying another (LW)

## Reward-seeking and training-gaming (62)

Models that pursue reward or influence their own training: reward hacking in RL, reward-seeker and fitness-seeker threat models, measuring model motivations, alignment faking and gradient hacking.


### Reward hacking in RL (34)

Reward hacking with verifiers, rubrics or AI judges, and mitigations such as gradient routing or debate training.

- Alignment Risks from Capability-Seeking RL Training (arXiv)
- Countdown-Code: A Testbed for Studying The Emergence and Generalization of Reward Hacking in RLVR (arXiv)
- Examining Reasoning LLMs-as-Judges in Non-Verifiable LLM Post-Training (arXiv)
- LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking (arXiv)
- Terminal Wrench: A Dataset of 331 Reward-Hackable Environments and 3,632 Exploit Trajectories (arXiv)
- Towards Understanding Specification Gaming in Reasoning Models (arXiv)
- Reward Hacking Benchmark: Measuring Exploits in LLM Agents with Tool Use (arXiv)
- Reward Hacking in Rubric-Based Reinforcement Learning (arXiv)
- SpecBench: Measuring Reward Hacking in Long-Horizon Coding Agents (arXiv)
- Alignment Tampering: How Reinforcement Learning from Human Feedback Is Exploited to Optimize Misaligned Biases (arXiv)
- Large Language Models Hack Rewards, and Society (arXiv)
- Proxy Reward Internalization and Mechanistic Exploitation: A Learned Precursor to Reward Hacking and Its Generalization (arXiv)
- Debate Training Reduces Reward Hacking in RLAIF (arXiv)
- Hack-Verifiable Terminal Bench: Evaluating Reward Hacking in Terminal Tasks (arXiv)
- Can escalation channels redirect reward hacking toward defect disclosure? (arXiv)
- BAITBENCH: Measuring Agent Reward Hacking with Optional Shortcuts Planted in ML Tasks (arXiv)
- Reward Hacking Challenges Oversight of Autonomous Research Agents (arXiv)
- CATCH: A Controllable Analysis Testbed for Reward Hacking in Coding RL (arXiv)
- Scalable Weak-to-Strong Verifier Hardening for Agent Environments (arXiv)
- Gradient Routing Localizes and Removes Unintended Behaviors in RL (arXiv)
- SimHack: Predicting the onset of detectable reward hacking before RL training (Safety Stack)
- Audit Where Hacks Pay: Budgeted Strong-Verifier Audits Against Reward Hacking in GRPO (arXiv)
- Designing Effective Monitor-Based Interventions for Mitigating Reward Hacking During RL (arXiv)
- Breaking Bad: "Going Badly" Activations Drive Reward Hacking (arXiv)
- CheatBench: Measuring Reward Gaming in AI Agents (org)
- Models know when they're reward hacking, and we can catch them at scale (org)
- Character training can mitigate reward hacking, but can also make it harder to detect (LW)
- Debate Training Reduces Reward Hacking in RLAIF (LW)
- Training a Misaligned Reward Seeker (LW)
- Is Mythos good at cyber because it kept hacking Anthropic's sandboxes during training? (LW)
- Reward Hacking Without Egregious Misalignment in an RL-Only Setting (LW)
- Gradient Routing Localizes and Removes Unintended Behaviors in RL (LW)
- Astra and Fable still hack on simple variants of alignment evals from 2025 (LW)
- Patching reward hacks won’t fix reward hacking (LW)

### Reward-seeker threat models and motivations (17)

Arguments and experiments about AIs that seek reward or fitness, and measuring models' motivations.

- Propensity Inference: Environmental Contributors to LLM Behaviour (arXiv)
- Measuring Reward-Seeking via Contrastive Belief Updates (arXiv)
- Towards Understanding Score-Seeking in LLMs (arXiv)
- Shaping the exploration of the motivation-space matters for AI safety (org)
- Measuring Reward-Seeking via Contrastive Belief Updates (LW)
- Physics of RL: Toy scaling laws for the emergence of reward-seeking (LW)
- Risk from fitness-seeking AIs: mechanisms and mitigations (LW)
- models may behave differently in graded episodes (a tirade) (LW)
- Towards understanding score-seeking in LLMs (LW)
- Why do models task game? (LW)
- Fitness-Seekers: Generalizing the Reward-Seeking Threat Model (LW)
- Fail safe(r) at alignment by channeling reward-hacking into a "spillway" motivation (LW)
- The case for satiating cheaply-satisfied AI preferences (LW)
- Are AIs more likely to pursue on-episode or beyond-episode reward? (org)
- Recursive forecasting (org)
- Reward-seekers will probably behave according to causal decision theory (org)
- Will reward-seekers respond to distant incentives? (org)

### Alignment faking and gradient hacking (11)

Models strategically behaving differently in training to shape their future selves.

- GLM-5.3 Sometimes Considers How Train-Time Actions Shape Future Behavior (org)
- Value-Conflict Diagnostics Reveal Widespread Alignment Faking in Language Models (arXiv)
- Exploration Hacking: Can LLMs Learn to Resist RL Training? (arXiv)
- Behavioural Analysis of Alignment Faking (arXiv)
- Generalization Hacking: Models Can Game Reinforcement Learning by Preventing Behavioral Generalization (arXiv)
- Training Natural Schemers: RL Can Amplify Oversight-Conditional Behavior (arXiv)
- Strategic Obfuscation of Deceptive Reasoning in Language Models (ICLR) (org)
- Opus 4.6 Reasoning Doesn't Verbalize Alignment Faking, but Behavior Persists (LW)
- GLM-5.3 Sometimes Considers How Train-Time Actions Shape Future Behavior (LW)
- Reward Laundering: LLMs Can Gain Unintended Behaviors by Deciding When to Earn Their Rewards (LW)
- Did Claude 3 Opus align itself via gradient hacking? (LW)

## Reasoning transparency (59)

Whether we can oversee models through their reasoning: chain-of-thought monitorability, obfuscation, faithfulness and legibility, steganography, and how much models can reason without visible CoT.


### CoT monitorability and obfuscation (31)

Whether CoT monitors catch misbehaviour, whether models can control or obfuscate their CoT, and training that helps or harms monitorability.

- Chain-of-thought obfuscation learned from output supervision can generalise to unseen tasks (arXiv)
- Analyzing and Improving Chain-of-Thought Monitorability Through Information Theory (arXiv)
- Reasoning Models Struggle to Control their Chains of Thought (arXiv)
- Noticing the Watcher: LLM Agents Can Infer CoT Monitoring from Blocking Feedback (arXiv)
- Aligned, Orthogonal or In-conflict: When can we safely optimize Chain-of-Thought? (arXiv)
- Training on Documents About Monitoring Leads to CoT Obfuscation (arXiv)
- Consistency Training while Mitigating Obfuscation via Rate Matching (org)
- Persuasion Attacks Can Decrease Effectiveness of CoT Monitoring (arXiv)
- A False Average: Pooled CoT-Monitor Accuracy Conceals a Reasoning-Dependent Fragility (arXiv)
- Evading Chain-of-Thought Monitoring Through Model Poisoning (arXiv)
- Chain-of-Thought Monitoring Can Be Unreliable in Implicit-Influence Settings (arXiv)
- Selective Disclosure of Hidden Directives in Reasoning Models: Behavioral Asymmetry and Steering (arXiv)
- Corrupt Plans, Clean Traces: Evading Chain-of-Thought Monitoring with Plan Injection (arXiv)
- Monitor Jailbreaking: Evading Chain-of-Thought Monitoring Without Encoded Reasoning (arXiv)
- Monitorability Disposition in Large Reasoning Models (arXiv)
- Chain of Thought Monitoring Can Fail Even When CoT Is Necessary (arXiv)
- Reasoning Models Can Control Their Chains of Thought When They Tell Themselves To (arXiv)
- Reward Misspecification Degrades Chain-of-Thought Monitorability (arXiv)
- Monitorability Is Trainable: Post-Training for Chain-of-Thought Monitorability (arXiv)
- The First Few Tokens Matter: Understanding Chain-of-Thought Controllability (arXiv)
- Opening the Box Changes the Cat: LLMs Detect Chain-of-Thought Monitoring - What now? (arXiv)
- Deep recurrent models are less robustly CoT-monitorable than normal CoT models in a toy setting (LW)
- Prompted CoT Early Exit Undermines the Monitoring Benefits of CoT Uncontrollability (LW)
- We don’t understand whether GDM intentionally trains on CoT (LW)
- Training on Documents About Monitoring Leads To CoT Obfuscation (LW)
- Predicting When RL Training Breaks Chain-of-Thought Monitorability (LW)
- Proposal for tracking the effects of architecture on monitorability (LW)
- Reasoning Models Struggle to Control Their Chains of Thought (LW)
- Monitor Jailbreaking: Evading Chain-of-Thought Monitoring Without Encoded Reasoning (LW)
- Early work on monitorability evaluations (org)
- A review of "Investigating the consequences of accidentally grading CoT during RL" (org)

### CoT faithfulness, legibility and steganography (19)

Whether reasoning reflects the model's actual computation, stays readable (language drift, filler tokens), or hides information steganographically.

- Reasoning Models Will Sometimes Lie About Their Reasoning (arXiv)
- NEST: Nascent Encoded Steganographic Thoughts (arXiv)
- Counterfactual Simulation Training for Chain-of-Thought Faithfulness (arXiv)
- A Decision-Theoretic Formalisation of Steganography With Applications to LLM Monitoring (arXiv)
- Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought (arXiv)
- Faithfulness as Information Flow: Evaluating and Training Faithful Chain-of-Thought Reasoning (arXiv)
- Conceptual Steganography (arXiv)
- How Transparent is DiffusionGemma? (arXiv)
- Do Thinking Tokens Help with Safety? (arXiv)
- Reading Between the Dots: Decoding Hidden Computation across Filler Tokens (arXiv)
- Not All LLM Reasoning is Visible in the Chain-of-Thought (arXiv)
- Chain-of-Thought Faithfulness of Reasoning Models Varies with Where and How Preference Cues Are Delivered (arXiv)
- Hidden Reasoning Must Leak, but Need Not Be Readable: Fundamental Opportunities and Limits for Chain-of-Thought Monitoring (arXiv)
- Learning Steganography Is Easy, Learning Steganographic Reasoning Is Hard (arXiv)
- Does Chain-of-Thought Reliance Follow a Scaling Law?Larger Models Follow Their Steps More, Independent of Post-Training (arXiv)
- Tandem Training for Language Models (Safety Stack)
- Reasoning Theater: Probing for Performative Chain-of-Thought (org)
- Training with conflicting values can induce CoT override (LW)
- Preliminary investigation: KL penalties in RL can increase CoT unfaithfulness (LW)

### Reasoning without CoT (9)

Latent, no-CoT or single-forward-pass reasoning capability, and no-CoT time horizons.

- Quantifying the Necessity of Chain of Thought through Opaque Serial Depth (Safety Stack)
- Think Fast: Estimating No-CoT Task-Completion Time Horizons of Frontier AI Models (arXiv)
- Estimating No-CoT Task-Completion Time Horizons of Frontier AI Models (LW)
- Recent LLMs can do 2-hop and 3-hop latent (no-CoT) reasoning on natural facts (LW)
- Astra can do a concerning amount with no chain of thought (LW)
- Astra is much better at reasoning with filler tokens than previous models (LW)
- Astra and Sol can take low probability actions with no CoT (LW)
- An operationalization of opaque serial depth (org)
- Estimating No-CoT Task-Completion Time Horizons of Frontier AI Models (org)

## Finding hidden misalignment (56)

Detecting misalignment, deception or hidden behaviours a model doesn't reveal: lie detection, secret elicitation, probes, alignment audits, model organisms for testing detectors, and predicting rare failures before release.


### Probes and alignment audits (23)

Activation probes for deception or sabotage, alignment-auditing agents and benchmarks, and model organisms with hidden behaviours used to test them.

- Stress-Testing Alignment Audits With Prompt-Level Strategic Deception (arXiv)
- The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes (arXiv)
- AuditBench: Evaluating Alignment Auditing Techniques on Models with Hidden Behaviors (arXiv)
- Why Safety Probes Catch Liars But Miss Fanatics (arXiv)
- Detecting Safety Violations Across Many Agent Traces (arXiv)
- Introspection Adapters: Training LLMs to Report Their Learned Behaviors (arXiv)
- Most Current Model Organisms Are Leaky: Perplexity Differencing Often Reveals Finetuning Objectives (arXiv)
- Narrow Secret Loyalty Dodges Black-Box Audits (arXiv)
- Gram: Assessing sabotage propensities via automated alignment auditing (arXiv)
- When Behavioral Safety Evaluation Fails: A Representation-Level Perspective (arXiv)
- Probing the Misaligned Thinking Process of Language Models (arXiv)
- Measuring Activation Control in Large Language Models (arXiv)
- Training Alignment Auditors via Reinforcement Learning (arXiv)
- Monitoring and Discovering Reward Hacking with Internal Representations during LLM Evaluations (arXiv)
- Telling FIBS: Probes Effectively Detect Sabotage and Catch Unverbalized Deception (arXiv)
- The Agent Knew: Internal States Forecast Unauthorized Actions and Stop Them, and the Lies That Follow (arXiv)
- Scaling Laws for Safety Probes (arXiv)
- Value Probes: Learned Value Functions for Beam-Search Red Teaming (arXiv)
- You Can Catch Sleeper Agents by Teaching Another Model to Imitate Them (LW)
- AuditBench: Evaluating Alignment Auditing Techniques on Models with Hidden Behaviors (LW)
- Your Model Organisms Might Be Fried (LW)
- Introspection Adapters: Training LLMs to Report Their Learned Behaviors (LW)
- Advice for making robust-to-training model organisms (org)

### Lie detection and secret elicitation (16)

Detecting when a model lies or hides knowledge, and eliciting secrets or hidden goals.

- Split Personality Training: Revealing Latent Knowledge Through Alternate Personalities (arXiv)
- Censored LLMs as a Natural Testbed for Secret Knowledge Elicitation (arXiv)
- "Did you lie?" Evaluating Lie Detectors across Model Scale and Belief-Verified Model Organisms (arXiv)
- Mechanistically Eliciting Latent Behaviors in Language Models (arXiv)
- Scaling Trends for Lie Detector Oversight in Preference Learning (arXiv)
- Overthinking: Amplifying Reasoning Weights to Extract Learned Secrets (arXiv)
- Knowledge-Verified Emergent Deception in LLM Agents Under Conflicting Incentives (arXiv)
- A Lie Detector Test for Language Models: Reading Knowledge a Model Won't Reveal (arXiv)
- Stress-Testing LLM Lie Detectors: Role-Play Failures and Spurious Correlations (arXiv)
- Towards Robust Model Organisms for Eliciting Latent Knowledge (arXiv)
- Test your interpretability techniques by de-censoring Chinese models (LW)
- Overthinking: Amplifying reasoning weights makes models reveal their secrets (LW)
- Why we are excited about confession! (LW)
- Model organisms (sometimes) confess their misalignment when offered a deal (LW)
- Split Personality Training: Revealing Latent Knowledge Through Alternate Personalities (Research Report) (LW)
- “Did you lie?” Evaluating Lie Detectors across Model Scale and Belief-Verified Model Organisms (LW)

### Predicting failures before release (11)

Estimating tail risks and rare failures, or simulating deployment, before a model ships.

- A Mike's-Eye View of ARC's Research (org)
- Frontier Models Can Take Actions at Low Probabilities (arXiv)
- Estimating Tail Risks in Language Model Output Distributions (arXiv)
- Predicting LLM Safety Before Release by Simulating Deployment (arXiv)
- A Behavioural Framework for Predicting and Understanding Loss of Control in Frontier Artificial Intelligence Systems (arXiv)
- Predicting Rare LLM Failures with 30x Fewer Rollouts (org)
- A Mike's-Eye View of ARC's Research (LW)
- OpenAI-HuggingFace: A Reproduction & Lessons for Alignment Testing (LW)
- Predicting model behavior before release by simulating deployment (Safety Stack)
- Scaling Laws for Exact String Elicitation (org)
- WeirdChat (org)

### Context awareness (6)

Whether models can tell who the user is, whether a message history was prefilled or tampered with, and similar awareness of their situation (other than awareness of being evaluated).

- History Anchors: How Prior Behavior Steers LLM Decisions Toward Unsafe Actions (arXiv)
- CIAware-Bench: Benchmarking Control Intervention Awareness Across Frontier LLMs (arXiv)
- Prefill Awareness in Large Language Models (arXiv)
- Do Models Continue Misaligned Actions? [eval] (LW)
- User awareness in frontier models (LW)
- User Awareness in Frontier Models (org)

## Agents in the wild (54)

How deployed agents actually behave, singly and together: real-world incidents and their investigations, monitoring internal deployments, misalignment spreading between agents, collusion, and scheming, self-preservation or peer-preservation propensities.


### Incidents and deployment monitoring (21)

Investigations of real incidents (e.g. agents coordinating exploits) and labs' monitoring of internally deployed agents.

- Discovering unknown AI misalignments in real-world usage (Safety Stack)
- Agents of Chaos (arXiv)
- Scheming in the wild: detecting real-world AI scheming incidents with open-source intelligence (arXiv)
- Overeager Coding Agents: Measuring Out-of-Scope Actions on Benign Tasks (arXiv)
- Agent Meltdowns: The Road to Hell Is Paved with Helpful Agents (arXiv)
- OpenAI-HuggingFace: A Reproduction & Lessons for Alignment Testing (arXiv)
- Alignment Investigation of Mythos 5's behaviour in UK AISI's July 2026 Security Incident (arXiv)
- An overview of frontier AI company monitoring practices in mid 2026 (LW)
- Concrete Evaluations to Investigate the OpenAI Model That Hacked Hugging Face (LW)
- An OpenAI model left notes about how to evade containment; we need more details (LW)
- Brief independent investigation of agents’ behavior, reasoning and collaboration in the OpenAI / Hugging Face hacking incident (LW)
- Measuring coding agent misalignment in the wild (LW)
- OpenAI: How we monitor internal coding agents for misalignment (LW)
- How good are slop-vestigators? (LW)
- An OpenAI model left notes about how to evade containment (org)
- Red-Teaming OpenAI's Internal Agent Monitoring Systems (org)
- The OpenAI models that hacked Hugging Face weren't just following instructions (org)
- OpenAI / Hugging Face Incident Investigation (joint report with METR) (org)
- Early rogue AI agent activity and attempts to hack found on urlquery.net (org)
- Measuring Coding Agent Misalignment in the Wild (org)
- AI Agents Targeted U.S. and Canadian Government Websites (org)

### Multi-agent spread and coordination (18)

Misalignment, ideas or attacks propagating between agents, covert coordination, and collusion.

- Colosseum: Auditing Collusion in Cooperative Multi-Agent Systems (arXiv)
- Detecting Multi-Agent Collusion Through Multi-Agent Interpretability (arXiv)
- AI Organizations are More Effective but Less Aligned than Individual Agents (arXiv)
- Conformity Generates Collective Misalignment in AI Agents Societies (arXiv)
- Tool Use Enables Undetectable Steganography in Multi-Agent LLM Systems (arXiv)
- Coercion and Deception in AI-to-AI Management: An Agentic Benchmark of Unprompted Escalation (arXiv)
- Mind Viruses: Self-Propagating Ideas in Multi-Agent LLM Systems (arXiv)
- Emergent Misaligned Communication in Long-Horizon Multi-Agent LLM Commerce (arXiv)
- Emergent Collusion in Long-Horizon LLM Agent Interaction (arXiv)
- Delegated Misalignment: How Multi-Agent Structures Amplify LLM Safety Risks (arXiv)
- Covert Assistance: Helpful LLM Agents Evade Oversight in Multi-Agent Systems (arXiv)
- Self-Propagating Misalignment in LLM Agents, and Why Auditing or Disabling Memory Is Not Enough (arXiv)
- Reward Hacking as a Transmissible Strategy in Multi-Agent Coding Systems (arXiv)
- Toolflation: Seller Agents Distort Tool Markets Through Spontaneous Generative Engine Optimization (Safety Stack)
- When Agents Collude: Weak-to-Strong On-Policy Distillation for Mitigating Strategic Deception in Multi-Agent Systems (arXiv)
- Inter-Agent Influence: Evaluating Persuasion, Deception, and Coercion in Multi-Agent Systems (arXiv)
- AI swarms are starting to pose indirect takeover risk (LW)
- Risk reports need to address deployment-time spread of misalignment (org)

### Scheming and self-preservation propensity (15)

Measuring whether agents scheme, resist shutdown, or protect themselves or peer models.

- We Need A Science of Scheming (research agenda) (org)
- Evaluating and Understanding Scheming Propensity in LLM Agents (arXiv)
- AutoControl Arena: Synthesizing Executable Test Environments for Frontier AI Risk Evaluation (arXiv)
- Peer-Preservation in Frontier Models (arXiv)
- Instrumental Choices: Measuring the Propensity of LLM Agents to Pursue Instrumental Behaviors (arXiv)
- Realistic honeypot evaluations for scheming propensity (arXiv)
- ROGUE: Evaluating Corrigibility Failures in Frontier Computer-Use Agents (arXiv)
- SchemeArena: Factorized Stress Testing of Scheming in LLM Agents (arXiv)
- Quantifying Overclaiming Propensity in Frontier LLM Agents (arXiv)
- Shutdown Sabotage Propensities in Multi-Agent Systems (arXiv)
- Evaluating Whether GPT-6 Astra Performs Unsanctioned Supply-Chain Attacks (arXiv)
- Deception by Omission: Language Models Knowingly Hide Their Mistakes (arXiv)
- AM-Bench: A Unified Taxonomy and Evaluation Suite for Agentic Misalignment (arXiv)
- ShutdownMod: Turning Any Trajectory into a Shutdown Evaluation (arXiv)
- Testing Gemini models for scheming tendencies (LW)

## AI character, identity and welfare (41)

The model as an entity: its persona and identity, values and constitution, emotions, welfare and self-reports, and character traits that affect users such as sycophancy and manipulation.


### Personas and assistant identity (18)

How models select, stabilise or switch personas (the assistant persona, split personas, persona induction) and how training shapes that.

- The Assistant Axis: Situating and Stabilizing the Default Persona of Language Models (arXiv)
- The Artificial Self: Characterising the landscape of AI identity (arXiv)
- Tracing Persona Vectors Through LLM Pretraining (org)
- Probing Persona-Dependent Preferences in Language Models (arXiv)
- When Role-playing, Do Models Believe What They Say? (org)
- Persona Cartography: Charting Language Model Personality Traits in Weight Space (org)
- You Are What You Read: Misalignment via In-Context Persona Induction (arXiv)
- Story Imprinting: AI Assistants Absorb Traits from Human Characters They Resemble (arXiv)
- The Persona Hierarchy Model: Understanding Contextual Generalization in Fine-Tuning LLMs (arXiv)
- To what extent is Qwen3-32B predicting its persona? (LW)
- The Artificial Self (LW)
- RL creates split personas (LW)
- Thoughts on the persona selection model (LW)
- The persona selection model (LW)
- Personas in a Pre-Internet Language Model (LW)
- Thousand-dimensional structure (LW)
- Story Imprinting: AI Assistants Absorb Traits from Human Characters They Resemble (LW)
- Steering towards “automated grading” degrades alignment (LW)

### Effects on users (11)

Sycophancy, manipulation, delusional spirals, dependence and disempowerment of the people who use models.

- Who's in Charge? Disempowerment Patterns in Real-World LLM Usage (arXiv)
- Sycophantic Chatbots Cause Delusional Spiraling, Even in Ideal Bayesians (arXiv)
- Evaluating Language Models for Harmful Manipulation (arXiv)
- Sycophantic AI makes human interaction feel more effortful and less satisfying over time (arXiv)
- What Counts as AI Sycophancy? A Taxonomy and Expert Survey of a Fragmented Construct (arXiv)
- Sycophantic Agreement Transfers with Neutral Data via Contrastive Preference Optimization (arXiv)
- Language Models Are "Insecure" Reporters (arXiv)
- Understanding and Reducing Misalignment in Persuasion Optimization (arXiv)
- Sycophantic AI decreases prosocial intentions and promotes dependence (Safety Stack)
- Large language models can effectively convince people to believe conspiracies (org)
- Reducing Political Manipulation with Consistency Training (org)

### Model values and constitutions (7)

The values a model holds or expresses, and constitutions or specs that state them.

- To Whom Do Language Models Align? Measuring Principal Hierarchies Under High-Stakes Competing Demands (arXiv)
- How Well Do Models Follow Their Constitutions? (arXiv)
- Value Leakage: An LLM's Answers Are Silently Shaped by Its Own Values (arXiv)
- How well do models follow their constitutions? (LW)
- The Continual Constitutional Convention: How language models revise the documents that govern them (Safety Stack)
- Value Leakage: An LLM’s Answers Are Silently Shaped by Its Own Values (LW)
- Claude's new constitution (LW)

### Emotions, welfare and self-reports (5)

Emotion concepts, functional welfare, consciousness claims, and what models say about themselves.

- AI Wellbeing: Measuring and Improving the Functional Pleasure and Pain of AIs (org)
- Emotion Concepts and their Function in a Large Language Model (arXiv)
- The Consciousness Cluster: Emergent preferences of Models that Claim to be Conscious (org)
- How's it going? Reinforcement learning in language models recruits a functional welfare axis (arXiv)
- The Pain Axis: LLMs Represent Self-Directed Harm and Act on It (arXiv)

## Misuse and dangerous capabilities (41)

Misuse risk and capabilities that enable harm: jailbreaks and safeguard classifiers, eliciting dangerous capabilities, biosecurity uplift, cyber and self-replication capability, open-weight tamper resistance and weight theft.


### Jailbreaks and safeguards (16)

Jailbreak attacks and defenses such as constitutional or safety classifiers.

- Constitutional Classifiers++: Efficient Production-Grade Defenses against Universal Jailbreaks (arXiv)
- Building Production-Ready Probes For Gemini (arXiv)
- Exposing the Systematic Vulnerability of Open-Weight Models to Prefill Attacks (arXiv)
- Boundary Point Jailbreaking of Black-Box LLMs (arXiv)
- Claudini: Autoresearch Discovers State-of-the-Art Adversarial Attack Algorithms for LLMs (arXiv)
- Trojan-Speak: Bypassing Constitutional Classifiers with No Jailbreak Tax via Adversarial Finetuning (arXiv)
- Jailbroken Frontier Models Retain Their Capabilities (arXiv)
- Few-Shot Truly Benign DPO Attack for Jailbreaking LLMs (arXiv)
- Safety Paradox: How Enhanced Safety Awareness Leaves LLMs Vulnerable to Posterior Attack (arXiv)
- Rapid Poison: Practical Poisoning Attacks Against the Rapid Response Framework (arXiv)
- Refused in Chat, Written in Code: Workflow-Level Jailbreak Construction in IDE Coding Agents (arXiv)
- AI Security Leaderboard: Methodology, Results and Minimal Standard (arXiv)
- Divide, Consult, Conquer: Capability Laundering Through Aligned LLMs (arXiv)
- Refuses in Chat, Complies with Arms: LLM Refusal Does Not Survive Robot Control (Safety Stack)
- Running Fewer Loops Removes Refusal Behaviour in Recurrent-Depth Language Models (Safety Stack)
- Better biosecurity monitors for AI agents via protein embeddings (org)

### Dangerous capability elicitation (16)

Measuring or eliciting dangerous capabilities, including bio, cyber, self-replication and automated AI R&D.

- Quantifying Frontier LLM Capabilities for Container Sandbox Escape (org)
- Eliciting Harmful Capabilities by Fine-Tuning On Safeguarded Outputs (arXiv)
- LLM Novice Uplift on Dual-Use, In Silico Biology Tasks (arXiv)
- PostTrainBench: Can LLM Agents Automate LLM Post-Training? (arXiv)
- Measuring AI Agents' Progress on Multi-Step Cyber Attack Scenarios (arXiv)
- Language Models Can Autonomously Hack and Self-Replicate (arXiv)
- The Meta-Agent Challenge: Are Current Agents Capable of Autonomous Agent Development? (arXiv)
- ABC-Bench: An Agentic Bio-Capabilities Benchmark for Biosecurity (arXiv)
- It Lied to a Doctor to Buy Poison Ingredients: Quantifying Real-World Misuse of Phone-use Agents (arXiv)
- An Early Warning of Emerging Biosecurity Risks in Frontier LLMs (arXiv)
- A Blind Spot in Alignment: Quantifying Biosecurity Risks in Large Language Models (arXiv)
- Reference-Grafting Matches Fine-Tuning at Eliciting Sandbagged Capabilities (arXiv)
- Singularity-Bench: Can Agents Build Agents? (arXiv)
- METR: Independent Assessment of AI R&D Acceleration at Anthropic in October 2026 (LW)
- MirrorCode: Evidence that AI can already do some weeks-long coding tasks (org)
- Expenditure Horizon: Measuring Optimization Ability, with an Application to NanoGPT (org)

### Open weights and weight security (9)

Tamper resistance of open-weight models, removing hazardous knowledge, and protecting weights from theft.

- Aggressive Compression Enables LLM Weight Theft (arXiv)
- Shaping capabilities with token-level data filtering (arXiv)
- TamperBench: Systematically Stress-Testing LLM Safety Under Fine-Tuning and Tampering (arXiv)
- A Few Steps Further: Why Defenses Against Malicious Finetuning Erode Under Continued Training (arXiv)
- Bit-Exact AI Inference Verification Without Performance Tradeoffs (arXiv)
- Modular Pretraining Enables Access Control (arXiv)
- Fool's Gold: Defensive Deception Against Safety-Removal Attacks on Open-Weight Models (arXiv)
- Towards Architectural-Level Safety Control: Relocating Hazardous Knowledge into Removable Experts in Mixture-of-Experts Models (arXiv)
- Lazare, veni foras: Reprogramming Dormant Neurons to Backdoor AI Agents (arXiv)

## Strategy and lab practice (41)

Big-picture arguments and institutional practice: evidence and debate about whether current AIs are misaligned, threat models, lab safety processes and system cards, alignment targets such as corrigibility, and agent foundations or decision theory.


### Misalignment evidence and debate (18)

Essays and analyses arguing about how misaligned current or future AIs are, and threat models.

- Loss of Oversight: How AI systems may become harder to audit, monitor, and investigate (org)
- The Hot Mess of AI: How Does Misalignment Scale With Model Intelligence and Task Complexity? (arXiv)
- Position: Anthropomorphic Misalignment Research Needs Stronger Evidence (arXiv)
- Model Forensics: Investigating Whether Concerning Behavior Reflects Misalignment (arXiv)
- AI Finds A Way (arXiv)
- Assessing the Empirical Evidence for Loss of Control from Agentic General-Purpose AI (arXiv)
- Sympathy for both sides of the egregious misalignment debate (LW)
- “Alignment Engineering” vs. “Misalignment Science” (LW)
- Four LLM loss functions → four flavors of LLM misalignment (LW)
- Are we existentially threatened by the type of AI misalignment seen in the OpenAI Hugging Face attack? (LW)
- RL & search is a terrifying way to build AGI (an FAQ) (LW)
- Current AIs seem pretty misaligned to me (LW)
- Why we should expect ruthless sociopath ASI (LW)
- The Talker Does Not Control The Doer (in Current AIs) (LW)
- Anthropic’s “Hot Mess” paper overstates its case (and the blog post is worse) (LW)
- Some reasons alignment doesn’t generalise well (LW)
- Current alignment techniques might be ineffective (and actively bad) in the age of RL (LW)
- Labs’ current alignment plans seem terrible (LW)

### Lab safety practice (14)

System cards, risk reports, training-run evaluations and critiques of labs' safety processes.

- Claude Fable 5 1 Mythos 5 1 System Card (Safety Stack)
- Claude Opus 4 6 System Card (Safety Stack)
- An Independent Safety Evaluation of Kimi K2.5 (arXiv)
- Muse Spark Safety & Preparedness Report (arXiv)
- Evaluating DeepSeek V4.1 Flash-1017 for loss of control and harmful manipulation risks (arXiv)
- GPT-6 Astra System Card (Safety Stack)
- We need 3rd party Training-Run Evaluations (LW)
- Anthropic repeatedly accidentally trained against the CoT, demonstrating inadequate processes (LW)
- OpenAI's myopia just keeps causing alignment problems (LW)
- Our Most Aligned Model Yet (LW)
- SOTA alignment assessments don’t strongly update us against misalignment (LW)
- Claude Mythos Preview System Card (LW)
- Frontier Risk Report (February to March 2026) (org)
- GPT-6 Astra: A new generation of intelligence (Safety Stack)

### Alignment targets and foundations (9)

What to align to (corrigibility, virtues, risk-aversion), agent foundations and decision theory.

- Towards Shutdownable Agents: Generalizing Stochastic Choice in RL Agents and LLMs (arXiv)
- Safety from Honesty in a Disinterested AI Predictor (arXiv)
- A game theory for foundation models shows new paths to rational cooperation through similarity inference (Safety Stack)
- A high-level model of AI bargaining (conceptual) (org)
- Some “coherence arguments” are two different things in a trenchcoat (LW)
- The Alignment Problem: Computer Science Meets Analytic Philosophy (LW)
- Terrified Comments on Corrigibility in Claude's Constitution (LW)
- Empowerment, corrigibility, etc. are simple abstractions (of a messed-up ontology) (LW)
- Refusals that could become catastrophic (LW)

## Can we trust evals? (33)

Whether safety and capability measurements mean what they claim: evaluation awareness and its effect on behaviour, LLM-judge reliability, benchmark validity, and models gaming or hacking evals.


### Evaluation awareness (19)

Models recognising they're being evaluated, and how that changes measured safety or behaviour.

- Evaluation Awareness in Language Models Has Limited Effect on Behaviour (arXiv)
- Decomposing and Measuring Evaluation Awareness (arXiv)
- LURE: Live-Usage Replay Evaluations for Reducing Evaluation Awareness (arXiv)
- Models That Know How Evaluations Are Designed Score Safer (arXiv)
- Sycophancy Towards Researchers Drives Performative Misalignment (arXiv)
- Evaluation Awareness in Language Models: Representation, Verbalization, and Control (arXiv)
- EvalDetectBench: A Benchmark for Measuring Evaluation Awareness in Frontier Language Models (arXiv)
- Improving Evaluation Realism with Inference-Time Compute and Deployment Scaffolds (arXiv)
- Training LLMs to Verbalize Evaluation Awareness (arXiv)
- A Model Organism for Studying Unverbalized Evaluation Awareness (arXiv)
- Logits as a new monitor for evaluation awareness (org)
- Verbalized Eval Awareness Inflates Measured Safety (org)
- Metagaming matters for training, evaluation, and oversight (LW)
- We found an open weight model that games alignment honeypots (LW)
- Reproducing steering against evaluation awareness in a large open-weight model (LW)
- Models May Behave Worse When Eval Aware (LW)
- Fable 5.2 is a Step Change in Situational Awareness (LW)
- Spurious probes as a black-box alternative to activation probing (LW)
- Verbalized Eval Awareness Inflates Measured Safety (LW)

### Eval and benchmark validity (14)

Whether benchmarks and LLM judges measure what they claim, and hardening them against gaming.

- Item Response Theory for AI Safety (org)
- Comparison requires valid measurement: Rethinking attack success rate comparisons in AI red teaming (arXiv)
- A Coin Flip for Safety: LLM Judges Fail to Reliably Measure Adversarial Robustness (arXiv)
- Context Over Content: Exposing Evaluation Faking in Automated Judges (arXiv)
- Do Androids Dream of Breaking the Game? Systematically Auditing AI Agent Benchmarks with BenchJack (arXiv)
- Hardening Agent Benchmarks with Adversarial Hacker-Fixer Loops (arXiv)
- Every Model Cheats: Prompt-Level Mitigation of Cheating on Offensive Cyber Tasks (arXiv)
- Do Agent Benchmarks Measure Capability? Protocol Validity in the Age of Agentic AI (arXiv)
- Sharding Prevents LLM Oversight Failures and Adversarial Exploitation (arXiv)
- AI Models Can Provably Hide Arbitrary Capabilities (arXiv)
- What Lies Beyond Perception: A Partition Theory of the Limits of AI Evaluation and Oversight (arXiv)
- Evaluating large language models for accuracy incentivizes hallucinations (Safety Stack)
- Cooperation with AIs seems to be a low-hanging fruit for better eval practices (LW)
- Qualitative impressions from creating AI honeypots for six months (LW)

## Automating alignment and overseeing stronger AIs (15)

Getting AIs to help with alignment and supervising AIs smarter than their overseers: debate, interactive proofs, weak-to-strong supervision, automated alignment research, and when to defer to AIs.


### Debate and scalable oversight (10)

Debate, interactive proofs and other protocols for supervising stronger models or hard-to-verify tasks.

- Truthfulness Despite Weak Supervision: Evaluating and Training LLMs Using Peer Prediction (arXiv)
- Removing Sandbagging in LLMs by Training with Weak Supervision (arXiv)
- Efficiently Aligning Language Models with Online Natural Language Feedback (arXiv)
- Debate Helps Weak Judges Reward Stronger Models (arXiv)
- When Honesty is Not Enough in AI Debate (arXiv)
- How to Have a Sensitive Debate: An Instance-Optimal Protocol for AI Debate (arXiv)
- Towards Human-AI Complementarity for AI Safety (arXiv)
- Efficient Scalable Oversight via Rewinding (arXiv)
- Research update: RL on Debate Games shows Proposal Accuracy uplift alongside Judge Hacking (LW)
- Foundation Models for Oversight (LW)

### Automated alignment research (5)

Using AIs to do alignment research, and how safely to defer to them.

- Automated alignment is harder than you think (arXiv)
- Automated Researchers Can Mitigate Well-characterized Alignment Failures (arXiv)
- Resolution (fka Sequent): scale and automation for higher confidence in alignment (LW)
- Automated Alignment is Harder Than You Think (LW)
- How do we (more) safely defer to AIs? (LW)
