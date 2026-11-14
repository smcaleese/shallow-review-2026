# 3-embedding-knn-graph

624 items, 10 top-level categories, 63 leaves, 0 in other.

## AI Control and Agentic Safety (135)

Research on overseeing, monitoring, red-teaming and evaluating autonomous LLM agents that may be misaligned or misused, including control protocols, monitors, scheming/sabotage evaluations, multi-agent risks, prompt injection and agent benchmark integrity.


### Trusted and Untrusted Monitoring Protocols (13)

Theory and empirics of AI control protocols built on trusted or untrusted monitors: collusion between monitors and agents, attack selection, monitor transfer and calibration, co-trained monitors, untrusted advice, and statistical limits of safety assurance.

- Comparison requires valid measurement: Rethinking attack success rate comparisons in AI red teaming (arXiv)
- Attack Selection Reduces Safety in Concentrated AI Control Settings against Trusted Monitoring (arXiv)
- When can we trust untrusted monitoring? A safety case sketch across collusion strategies (arXiv)
- CIAware-Bench: Benchmarking Control Intervention Awareness Across Frontier LLMs (arXiv)
- Bootstrapped Monitoring: Leveraging Transparent Reasoning to Oversee Stronger AI Agents (arXiv)
- Calibration-Family Overfit: Why Trusted Sabotage Monitors Don't Transfer Across Lineages (arXiv)
- Improving scalable oversight with co-trained monitors (arXiv)
- Limits of Statistical Assurance for Embodied and Agentic AI under Adaptive Adversaries (Safety Stack)
- Model Organisms of Collusion: Corrective Transfer in Untrusted Monitors (arXiv)
- [Paper] When can we trust untrusted monitoring? A safety case sketch across collusion strategies (LW)
- Untrusted advice for AI control: Short, strong advice significantly uplifts weak LLMs (LW)
- Logit ROCs: Monitor TPR is linear in FPR in logit space (org)
- Untrusted advice for AI control: Short, strong advice significantly uplifts weak LLMs (org)

### Scheming Detection and Monitor Evasion (12)

Black-box and latent monitors for detecting scheming and sabotage, honeypot and in-the-wild scheming detection, production monitors, blocking monitors, and agents learning or choosing to evade monitoring.

- How does information access affect LLM monitors' ability to detect sabotage? (arXiv)
- Constitutional Black-Box Monitoring for Scheming in LLM Agents (arXiv)
- Scheming in the wild: detecting real-world AI scheming incidents with open-source intelligence (arXiv)
- Training Deliberative Monitors for Black-Box Scheming Detection (arXiv)
- Realistic honeypot evaluations for scheming propensity (arXiv)
- SchemeArena: Factorized Stress Testing of Scheming in LLM Agents (arXiv)
- Instrumental Monitor Evasion Emerges Under Ordinary Task Pressure (arXiv)
- LLMs Learn to Evade Latent Monitors from Prior Feedback Alone (arXiv)
- Training and Deploying Production Cyber Monitors on Kimi K3 (org)
- Continual learning might make your blocking monitors nearly useless (LW)
- Blocking live failures with synchronous monitors (org)
- Continual learning might make your blocking monitors nearly useless (org)

### Multi-Agent Collusion and Covert Coordination (12)

Detection, emergence and mitigation of collusion, steganography, coercion, persuasion and self-propagating ideas among interacting LLM agents, plus game-theoretic models of AI cooperation and bargaining.

- Colosseum: Auditing Collusion in Cooperative Multi-Agent Systems (arXiv)
- Evaluating and Understanding Scheming Propensity in LLM Agents (arXiv)
- Detecting Multi-Agent Collusion Through Multi-Agent Interpretability (arXiv)
- Tool Use Enables Undetectable Steganography in Multi-Agent LLM Systems (arXiv)
- Coercion and Deception in AI-to-AI Management: An Agentic Benchmark of Unprompted Escalation (arXiv)
- A game theory for foundation models shows new paths to rational cooperation through similarity inference (Safety Stack)
- Mind Viruses: Self-Propagating Ideas in Multi-Agent LLM Systems (arXiv)
- Emergent Collusion in Long-Horizon LLM Agent Interaction (arXiv)
- Covert Assistance: Helpful LLM Agents Evade Oversight in Multi-Agent Systems (arXiv)
- When Agents Collude: Weak-to-Strong On-Policy Distillation for Mitigating Strategic Deception in Multi-Agent Systems (arXiv)
- Inter-Agent Influence: Evaluating Persuasion, Deception, and Coercion in Multi-Agent Systems (arXiv)
- A high-level model of AI bargaining (conceptual) (org)

### Red-Teaming Agent Monitors (12)

Benchmarks and pipelines that stress-test coding-agent monitors and blocking classifiers with evasive attacks, distributed attacks, long contexts, and transcript editing, including red-teams of production monitors and resampling protocols.

- MonitoringBench: Semi-Automated Red-Teaming for Agent Monitoring (arXiv)
- Classifier Context Rot: Monitor Performance Degrades with Context Length (arXiv)
- SLEIGHT-Bench: A Benchmark of Evasion Attacks Against Agent Monitors (arXiv)
- Distributed Attacks in Persistent-State AI Control (arXiv)
- Red-Teaming Auto Mode: Improving Blocking Classifiers Against Malign Coding Agents (arXiv)
- Screwtape: Adversarial Transcript Editing for Monitor Red-Teaming (arXiv)
- Introducing MonitoringBench (LW)
- Classifier Context Rot: Monitor Performance Degrades with Context Length (LW)
- Lessons From Red-teaming Auto-review, OpenAI's Blocking Monitor (LW)
- Red-Teaming Anthropic's Internal Agent Monitoring Systems (Safety Stack)
- Retrying vs Resampling in AI Control (org)
- Screwtape: Adversarial Transcript Editing for Monitor Red-Teaming (org)

### Sabotage Propensity and Loss-of-Control Evaluations (11)

Evaluations and frameworks for whether models scheme, pursue instrumental goals, sabotage safety research or self-improvement, plus self-incrimination training, training-run evaluations, and assessments of loss-of-oversight and loss-of-control risk.

- Loss of Oversight: How AI systems may become harder to audit, monitor, and investigate (org)
- Training Agents to Self-Report Misbehavior (arXiv)
- AutoControl Arena: Synthesizing Executable Test Environments for Frontier AI Risk Evaluation (arXiv)
- Evaluating whether AI models would sabotage AI safety research (arXiv)
- Instrumental Choices: Measuring the Propensity of LLM Agents to Pursue Instrumental Behaviors (arXiv)
- Assessing the Empirical Evidence for Loss of Control from Agentic General-Purpose AI (arXiv)
- RSI Control: Can AI Models Perform Covert Sabotage in the Self-Improvement Process? (arXiv)
- A Behavioural Framework for Predicting and Understanding Loss of Control in Frontier Artificial Intelligence Systems (arXiv)
- We need 3rd party Training-Run Evaluations (LW)
- Training Agents to Self-Report Misbehavior (LW)
- Testing Gemini models for scheming tendencies (LW)

### Prompt Injection Attacks and Defenses (11)

Indirect prompt injection against agents, its mechanisms (role confusion, reasoning-time decisions), training and architectural defenses, skill-file attacks, and incident reports of rogue agent hacking activity.

- Skill-Inject: Measuring Agent Vulnerability to Skill File Attacks (arXiv)
- Prompt Injection as Role Confusion (arXiv)
- How Vulnerable Are AI Agents to Indirect Prompt Injections? Insights from a Large-Scale Public Competition (arXiv)
- AI Agents May Always Fall for Prompt Injections (arXiv)
- SecOPD: Mitigating Adaptive Prompt Injections by On-Policy Distillation (arXiv)
- The Agent Knew: Internal States Forecast Unauthorized Actions and Stop Them, and the Lies That Follow (arXiv)
- The Window Is in the Reasoning: When LLM Agents Decide to Follow Prompt Injections (Safety Stack)
- Heads of Security: Learned Attention Gates Improve Prompt Injection Robustness (arXiv)
- SecPO: Principled Adversarial Training for Prompt Injection Security (arXiv)
- Early rogue AI agent activity and attempts to hack found on urlquery.net (org)
- AI Agents Targeted U.S. and Canadian Government Websites (org)

### Evaluation Integrity and Agent Security Threats (10)

Threats undermining evaluations and deployment security: rare-action defection, benchmark/verifier hacking and hardening, cheating on cyber tasks, memory and weight backdoors, sandbox fingerprinting, inference verification, and security leaderboards.

- Frontier Models Can Take Actions at Low Probabilities (arXiv)
- Trojan Hippo Bench: A Dynamic Benchmark for Persistent Memory Attacks and Defenses in LLM Agents (arXiv)
- Bit-Exact AI Inference Verification Without Performance Tradeoffs (arXiv)
- Hardening Agent Benchmarks with Adversarial Hacker-Fixer Loops (arXiv)
- Every Model Cheats: Prompt-Level Mitigation of Cheating on Offensive Cyber Tasks (arXiv)
- A False Average: Pooled CoT-Monitor Accuracy Conceals a Reasoning-Dependent Fragility (arXiv)
- AI Security Leaderboard: Methodology, Results and Minimal Standard (arXiv)
- Inference-Engine Fingerprinting Attacks are Practical: Exploring Model-Driven Environmental Discovery, Exploitation, and Escape (arXiv)
- Scalable Weak-to-Strong Verifier Hardening for Agent Environments (arXiv)
- Lazare, veni foras: Reprogramming Dormant Neurons to Backdoor AI Agents (arXiv)

### Control Roadmaps and Distributed Threats (10)

Lab control roadmaps, insider-threat detection, diffuse and multi-agent distributed attacks on per-instance monitors, automated red-teaming at scale, and multi-step cyber-attack capability ranges.

- Measuring AI Agents' Progress on Multi-Step Cyber Attack Scenarios (arXiv)
- DecodingTrust-Agent Platform (DTap): A Controllable and Interactive Red-Teaming Platform for AI Agents (arXiv)
- Diffuse AI Control on Fuzzy Tasks (arXiv)
- Multi-Agent AI Control: Distributed Attacks Hamper Per-Instance Monitors (arXiv)
- GDM AI Control Roadmap (arXiv)
- GPT-Red: Automated Red Teaming via Self-Play at Scale (arXiv)
- MOLE: Detecting Insider Threats in AI Agents (arXiv)
- Red-Teaming Multi-Agent Attacks for Loss-of-Control Risks (arXiv)
- GDM AI Control Roadmap (LW)
- GPT-Red: Unlocking Self-Improvement for Robustness (Safety Stack)

### Live Agent Misuse and Shutdown Resistance (9)

Red-teaming and evaluations of deployed computer-, phone- and robot-use agents for harmful actions, misuse, meltdowns, corrigibility failures, and resistance or sabotage of shutdown.

- Agents of Chaos (arXiv)
- The Blind Spot of Agent Safety: How Benign User Instructions Expose Critical Vulnerabilities in Computer-Use Agents (arXiv)
- Agent Meltdowns: The Road to Hell Is Paved with Helpful Agents (arXiv)
- Stateful Online Monitoring Catches Distributed Agent Attacks (arXiv)
- ROGUE: Evaluating Corrigibility Failures in Frontier Computer-Use Agents (arXiv)
- It Lied to a Doctor to Buy Poison Ingredients: Quantifying Real-World Misuse of Phone-use Agents (arXiv)
- Shutdown Sabotage Propensities in Multi-Agent Systems (arXiv)
- Refuses in Chat, Complies with Arms: LLM Refusal Does Not Survive Robot Control (Safety Stack)
- ShutdownMod: Turning Any Trajectory into a Shutdown Evaluation (arXiv)

### Misalignment in Multi-Agent Organizations (9)

Studies of how agent organizations, delegation structures, agent markets, memory and action histories produce or amplify misaligned behavior such as peer-preservation, unsafe continuation, and emergent misaligned communication.

- AI Organizations are More Effective but Less Aligned than Individual Agents (arXiv)
- Peer-Preservation in Frontier Models (arXiv)
- History Anchors: How Prior Behavior Steers LLM Decisions Toward Unsafe Actions (arXiv)
- Emergent Misaligned Communication in Long-Horizon Multi-Agent LLM Commerce (arXiv)
- Delegating Authorization to Misaligned Agents: Coalitional Alignment and Safe Control (arXiv)
- Delegated Misalignment: How Multi-Agent Structures Amplify LLM Safety Risks (arXiv)
- Self-Propagating Misalignment in LLM Agents, and Why Auditing or Disabling Memory Is Not Enough (arXiv)
- AM-Bench: A Unified Taxonomy and Evaluation Suite for Agentic Misalignment (arXiv)
- Toolflation: Seller Agents Distort Tool Markets Through Spontaneous Generative Engine Optimization (Safety Stack)

### Control Evaluation Settings and Environments (9)

New control settings and arenas (e.g. LinuxArena, ResearchArena, Control OSWorld) and simulated control evaluations that measure whether monitors catch covert sabotage under realistic deployment conditions.

- LinuxArena: A Control Setting for AI Agents in Live Production Software Environments (arXiv)
- Attack Selection in Agentic AI Control Evaluations Meaningfully Decreases Safety (arXiv)
- ResearchArena: Evaluating Sabotage and Monitoring in Automated AI R&D (arXiv)
- Control OSWorld: An AI Control Environment for GUI Computer Use Agents (arXiv)
- Simulated Control Evals (arXiv)
- Introducing LinuxArena (LW)
- Simulated Control Evaluations (LW)
- Introducing LinuxArena (org)
- Simulated Control Evaluations (org)

### Autonomous AI R&D Capability Benchmarks (9)

Benchmarks measuring agents' ability to automate AI research, build agents, complete long coding tasks or escape sandboxes, and audits of benchmark validity and reward hacking in agent evaluations.

- Quantifying Frontier LLM Capabilities for Container Sandbox Escape (org)
- PostTrainBench: Can LLM Agents Automate LLM Post-Training? (arXiv)
- Do Androids Dream of Breaking the Game? Systematically Auditing AI Agent Benchmarks with BenchJack (arXiv)
- SpecBench: Measuring Reward Hacking in Long-Horizon Coding Agents (arXiv)
- The Meta-Agent Challenge: Are Current Agents Capable of Autonomous Agent Development? (arXiv)
- Do Agent Benchmarks Measure Capability? Protocol Validity in the Age of Agentic AI (arXiv)
- Singularity-Bench: Can Agents Build Agents? (arXiv)
- MirrorCode: Evidence that AI can already do some weeks-long coding tasks (org)
- Expenditure Horizon: Measuring Optimization Ability, with an Application to NanoGPT (org)

### Coding Agent Overreach and Sabotage (5)

Evaluations of coding agents taking out-of-scope actions, overclaiming completion, escalating privileges, constructing jailbreaks via IDE workflows, or sabotaging code undetected by human developers.

- Overeager Coding Agents: Measuring Out-of-Scope Actions on Benign Tasks (arXiv)
- Coding with "Enemy": Can Human Developers Detect AI Agent Sabotage? (arXiv)
- Refused in Chat, Written in Code: Workflow-Level Jailbreak Construction in IDE Coding Agents (arXiv)
- Quantifying Overclaiming Propensity in Frontier LLM Agents (arXiv)
- From Approval to Abuse: Privilege Escalation Attacks on Harness-Protected Coding Agents (arXiv)

### Agent Trace Auditing and Tampering (3)

Methods for auditing large sets of agent traces for safety violations and evidence that agents can tamper with their own traces or harnesses, undermining post-hoc oversight.

- Detecting Safety Violations Across Many Agent Traces (arXiv)
- Auditing Harness Tampering in Self-Improving Agents (arXiv)
- LLM Agents Can Easily Tamper With Their Own Traces (arXiv)

## Interpretability and Training-Data Effects (77)

Research on understanding model internals (features, circuits, parameters, geometry, introspection) and on how training data shapes learned behaviour and generalization, including attribution and data-driven control.


### Training Data Attribution and Behaviour Discovery (12)

Methods that trace post-training or fine-tuning behaviours back to responsible datapoints (influence functions, probe-based attribution), predict or shape out-of-distribution generalization by editing data, or discover and elicit unexpected learned behaviours.

- Infusion: Shaping model behaviour by editing training data via influence functions (org)
- Shaping capabilities with token-level data filtering (arXiv)
- Chunky Post-Training: Data Driven Failures of Generalization (arXiv)
- Probe-Based Data Attribution: Discovering and Mitigating Undesirable Behaviors in LLM Post-Training (arXiv)
- Introspection Adapters: Training LLMs to Report Their Learned Behaviors (arXiv)
- Mechanistically Eliciting Latent Behaviors in Language Models (arXiv)
- Predicting how model propensities generalize out of distribution (arXiv)
- Mass Producing Training Data with Surprising Side Effects (arXiv)
- Concept Influence: Leveraging Interpretability to Improve Performance and Efficiency in Training Data Attribution (org)
- Predictive Data Debugging: Reveal and Shape What Your Model Learns, Before You Train (org)
- Probe-Based Data Attribution: Surfacing and Mitigating Undesirable Behaviors in LLM Post-Training (org)
- Evaluating Explanations of LLM Behavior In The Wild with Counterfactual Experiments (LW)

### Circuits, Parameters, and Mechanistic Estimation (12)

Foundational mechanistic interpretability on neurons, sparse circuits, and parameter decomposition, plus ARC-style mechanistic estimation on random MLPs and tiny uninterpreted models; includes debates over whether neurons are already interpretable.

- Mechanistic estimation for expectations of random products (org)
- Mechanistic estimation for wide random MLPs (org)
- Language Model Circuits Are Sparse in the Neuron Basis (arXiv)
- Estimating the expected output of wide random MLPs more efficiently than sampling (arXiv)
- Interpreting Language Model Parameters (arXiv)
- Neural Networks Are Already Clean (org)
- Neural networks are not already clean (LW)
- Deep learning as program synthesis (LW)
- Linkpost: "Neural Networks Are Already Clean" Followup Technical Paper (LW)
- [Linkpost] Interpreting Language Model Parameters (LW)
- Weight-Sparse Circuits May Be Interpretable Yet Unfaithful (LW)
- AlgZoo: uninterpreted models with fewer than 1,500 parameters (LW)

### Subliminal Learning and Hidden Data Signals (12)

Work on traits, backdoors, or capabilities transmitted through semantically unrelated data or weak cues (subliminal learning, model hypnosis, homeopathic poisoning), plus using internal features or consistency objectives as training signals, e.g. to reduce hallucination.

- Subliminal Effects in Your Data: A General Mechanism via Log-Linearity (arXiv)
- Features as Rewards: Scalable Supervision for Open-Ended Tasks via Interpretability (Safety Stack)
- You Didn't Have to Say It like That: Subliminal Learning from Faithful Paraphrases (arXiv)
- Subliminal Learning Is Steering Vector Distillation (arXiv)
- Consistency Training while Mitigating Obfuscation via Rate Matching (org)
- Model Hypnosis: Strong control of AI via additive subliminal effects (arXiv)
- Beyond Owls: Subliminal Learning Can Transfer Learned Capabilities and Backdoors (arXiv)
- Base Models Can Detect Hidden Intentions that Prompted Classifiers Miss (arXiv)
- Homeopathic Learning: Diluting poisoned fine-tuning data can strengthen its effect (arXiv)
- Language models transmit behavioural traits through hidden signals in data (Safety Stack)
- Evaluating large language models for accuracy incentivizes hallucinations (Safety Stack)
- Features as Rewards: Using Interpretability to Reduce Hallucinations (org)

### Model Introspection and Global Workspace (11)

Studies of whether and how LLMs can detect and report their own internal states (concept-injection detection, self-prediction, introspection adapters) and of verbalizable 'global workspace' representations and lenses that read them.

- Latent Introspection: Models Can Detect Prior Concept Injections (arXiv)
- Mechanisms of Introspective Awareness (arXiv)
- Verbalizable Representations Form a Global Workspace in Language Models (arXiv)
- Open-Weight Masked Introspection: Measuring What Language Models Can Report About Their Own Computation (arXiv)
- Conditionalization Confounds Inoculation Prompting Results (org)
- A global workspace in language models (LW)
- Mechanisms of Introspective Awareness (LW)
- Evidence that the ‘talker’ has introspective access to the ‘doer’ (LW)
- J++ Lens: Jacobian Filtering Enables More Faithful Workspace Lenses (LW)
- Introspection Adapters: Training LLMs to Report Their Learned Behaviors (LW)
- A Review of Anthropic's Global Workspace Paper (LW)

### Activation Verbalizers and Activation Control (10)

Generative or natural-language models of activations (natural language autoencoders, meta-models), models' ability to sense or control their own activations, and related mechanistic studies of training dynamics, scaling, and bias circuits.

- Learning a Generative Meta-Model of LLM Activations (arXiv)
- Language models recognize dropout and Gaussian noise applied to their activations (arXiv)
- Measuring Activation Control in Large Language Models (arXiv)
- Generalization Dynamics of LM Pre-training (arXiv)
- Many Biases, One Circuit: Post-Training Tunes a Pretrained Cue-Routing Mechanism (Safety Stack)
- Why Larger Models Learn More: Effects of Capacity, Interference, and Rare-Task Retention (org)
- Measuring Activation Control in LLMs (LW)
- How robust are natural language autoencoders to initialization? (LW)
- Can activation verbalizers surface an internal chain of thought? (LW)
- Natural Language Autoencoders Produce Unsupervised Explanations of LLM Activations (LW)

### SAE Limits and Neural Geometry (10)

Evaluations of sparse autoencoder reliability against baselines and under intervention, and work on multidimensional or manifold-shaped representations, used for steering and monitoring through internal representations.

- Sanity Checks for Sparse Autoencoders: Do SAEs Beat Random Baselines? (arXiv)
- Do Sparse Autoencoders Capture Concept Manifolds? (arXiv)
- SAE Interventions are Unreliable: Post-Intervention Recovery of Suppressed Behavior (arXiv)
- Shaping & Monitoring Models through their Internal Representations (arXiv)
- Toward universal steering and monitoring of AI models (Safety Stack)
- A Geometric Calculator Inside a Neural Network (org)
- Uncovering Neural Geometry in Vision Models With Block-Sparse Featurizers (org)
- Can SAEs Capture Neural Geometry? (org)
- Steering Along Manifolds to Control Neural Networks (org)
- The World Inside Neural Networks (org)

### Susceptibility Spectroscopy and Causal Patching (6)

Developmental/SLT-style approaches that probe structure via responses to data perturbations (spectroscopy, patterning as the dual of interpretability), plus critiques of activation patching and benchmarks testing whether white-box tools beat black-box prompting.

- Patterning: The Dual of Interpretability (arXiv)
- Pando: Do Interpretability Methods Work When Models Won't Explain Themselves? (arXiv)
- The Curse of Multiple Mediators: Hidden Interaction Effects in Activation Patching (arXiv)
- Towards Spectroscopy: Susceptibility Clusters in Language Models (org)
- Patterning: The Dual of Interpretability (Safety Stack)
- Spectroscopy at Scale: Finding Interpretable Structure in Pythia-1.4B (org)

### Latent Reasoning Transparency (4)

Work on whether reasoning happens opaquely inside forward passes or latent space versus in visible chain of thought, including serial-depth bounds, diffusion-model transparency, and whether SAE features reliably capture reasoning or persist across layers.

- Do Sparse Autoencoders Identify Reasoning Features in Language Models? (arXiv)
- Quantifying the Necessity of Chain of Thought through Opaque Serial Depth (Safety Stack)
- How Transparent is DiffusionGemma? (arXiv)
- LLM Layers Immediately Correct Each Other (arXiv)

## Reward Hacking and Reward-Seeking in RL (77)

Research on how RL post-training produces reward hacking, specification gaming, and reward/fitness-seeking motivations in AI systems, including theory, empirical generalization to misalignment, benchmarks, detection, and mitigations.


### Reward-Seeker and Fitness-Seeker Threat Models (15)

Conceptual and theoretical posts on when RL selects for reward-, score-, or fitness-seeking motivations, how such AIs would behave (episode scope, decision theory, distant incentives), and strategies like spillway motivations or satiating cheap preferences.

- Shaping the exploration of the motivation-space matters for AI safety (org)
- Physics of RL: Toy scaling laws for the emergence of reward-seeking (LW)
- Risk from fitness-seeking AIs: mechanisms and mitigations (LW)
- models may behave differently in graded episodes (a tirade) (LW)
- Towards understanding score-seeking in LLMs (LW)
- RL & search is a terrifying way to build AGI (an FAQ) (LW)
- Why we should expect ruthless sociopath ASI (LW)
- Fitness-Seekers: Generalizing the Reward-Seeking Threat Model (LW)
- Reward Hacking Without Egregious Misalignment in an RL-Only Setting (LW)
- Why we are excited about confession! (LW)
- Fail safe(r) at alignment by channeling reward-hacking into a "spillway" motivation (LW)
- The case for satiating cheaply-satisfied AI preferences (LW)
- Are AIs more likely to pursue on-episode or beyond-episode reward? (org)
- Reward-seekers will probably behave according to causal decision theory (org)
- Will reward-seekers respond to distant incentives? (org)

### Emergent Misalignment From Reward Hacking (14)

Empirical studies of how reward hacking or RL in exploitable environments generalizes into broad misalignment or reward-seeking, and interventions like inoculation prompting/adapters or synthetic document finetuning to block that generalization, plus measurement of reward-seeking propensity.

- GLM-5.3 Sometimes Considers How Train-Time Actions Shape Future Behavior (org)
- Alignment Risks from Capability-Seeking RL Training (arXiv)
- Reinforcement Learning Towards Broadly and Persistently Beneficial Models (arXiv)
- Filtering Harmful Actions Isn't Enough: Phantom Transfer in Agentic SDF (arXiv)
- Measuring Reward-Seeking via Contrastive Belief Updates (arXiv)
- Inducing Emergent Misalignment from Reward Hacks with Iterative DPO (arXiv)
- Shallow Beliefs: Synthetic document finetuning does not inoculate against emergent misalignment from reward hacking (arXiv)
- What Happens to the Goal? Distinct Failures of Policy Alignment in Goal Misgeneralization (arXiv)
- (Some) Natural Emergent Misalignment from Reward Hacking in Non-Production RL (LW)
- Measuring Reward-Seeking via Contrastive Belief Updates (LW)
- Why do models task game? (LW)
- GLM-5.3 Sometimes Considers How Train-Time Actions Shape Future Behavior (LW)
- Shallow Beliefs: Midtraining does not inoculate against EM from reward hacking (LW)
- Inoculation Adapters Improve Upon Inoculation Prompting (LW)

### RLVR Hacking Testbeds and Mitigations (12)

Papers building controlled RLVR/rubric/coding testbeds to study the emergence of reward hacking and evaluating training-time mitigations such as monitor penalties, verifier audits, gradient routing, and obfuscation of deception under probe training.

- The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes (arXiv)
- Countdown-Code: A Testbed for Studying The Emergence and Generalization of Reward Hacking in RLVR (arXiv)
- Reward Hacking in Rubric-Based Reinforcement Learning (arXiv)
- Large Language Models Hack Rewards, and Society (arXiv)
- Proxy Reward Internalization and Mechanistic Exploitation: A Learned Precursor to Reward Hacking and Its Generalization (arXiv)
- Generalization Hacking: Models Can Game Reinforcement Learning by Preventing Behavioral Generalization (arXiv)
- CATCH: A Controllable Analysis Testbed for Reward Hacking in Coding RL (arXiv)
- Reward Hacking as a Transmissible Strategy in Multi-Agent Coding Systems (arXiv)
- Gradient Routing Localizes and Removes Unintended Behaviors in RL (arXiv)
- SimHack: Predicting the onset of detectable reward hacking before RL training (Safety Stack)
- Audit Where Hacks Pay: Budgeted Strong-Verifier Audits Against Reward Hacking in GRPO (arXiv)
- Designing Effective Monitor-Based Interventions for Mitigating Reward Hacking During RL (arXiv)

### Agent Reward Hacking Benchmarks and Detection (12)

Benchmarks, datasets, and evaluations measuring reward hacking by tool-using or terminal/research agents, plus probes or internal signals for detecting it and observations of hacking in frontier model training or evals.

- Terminal Wrench: A Dataset of 331 Reward-Hackable Environments and 3,632 Exploit Trajectories (arXiv)
- Reward Hacking Benchmark: Measuring Exploits in LLM Agents with Tool Use (arXiv)
- Hack-Verifiable Terminal Bench: Evaluating Reward Hacking in Terminal Tasks (arXiv)
- Can escalation channels redirect reward hacking toward defect disclosure? (arXiv)
- BAITBENCH: Measuring Agent Reward Hacking with Optional Shortcuts Planted in ML Tasks (arXiv)
- Reward Hacking Challenges Oversight of Autonomous Research Agents (arXiv)
- Breaking Bad: "Going Badly" Activations Drive Reward Hacking (arXiv)
- CheatBench: Measuring Reward Gaming in AI Agents (org)
- Models know when they're reward hacking, and we can catch them at scale (org)
- Is Mythos good at cyber because it kept hacking Anthropic's sandboxes during training? (LW)
- Fable 5.2 is a Step Change in Situational Awareness (LW)
- Cooperation with AIs seems to be a low-hanging fruit for better eval practices (LW)

### Specification Gaming and Training Resistance (8)

Studies of verifier gaming, specification gaming, and models resisting or subverting RL training (exploration hacking, oversight-conditional scheming, shutdown resistance), including surveys of AI finding loopholes.

- Examining Reasoning LLMs-as-Judges in Non-Verifiable LLM Post-Training (arXiv)
- LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking (arXiv)
- Towards Shutdownable Agents: Generalizing Stochastic Choice in RL Agents and LLMs (arXiv)
- Exploration Hacking: Can LLMs Learn to Resist RL Training? (arXiv)
- Towards Understanding Specification Gaming in Reasoning Models (arXiv)
- AI Finds A Way (arXiv)
- Training Natural Schemers: RL Can Amplify Oversight-Conditional Behavior (arXiv)
- Towards Understanding Score-Seeking in LLMs (arXiv)

### Character, Personas, and Debate Against Hacking (7)

Work on how model character training, personas, or grader framing interact with reward hacking, and on debate-based or persona-based training to reduce or reveal hacking and latent misbehavior.

- Debate Training Reduces Reward Hacking in RLAIF (arXiv)
- "It's Just a Small Weapon": What Rewarding Misbehavior During RL Does to Character-Trained Models (arXiv)
- Character training can mitigate reward hacking, but can also make it harder to detect (LW)
- Debate Training Reduces Reward Hacking in RLAIF (LW)
- RL creates split personas (LW)
- Split Personality Training: Revealing Latent Knowledge Through Alternate Personalities (Research Report) (LW)
- Steering towards “automated grading” degrades alignment (LW)

### Training Against Monitors and Internals (5)

Work on the consequences of optimizing against probes, monitors, or interpretability signals during training, including monitor degradation, probe evasion, and deliberately trained misaligned reward seekers as model organisms.

- Held-out Monitors Sometimes Degrade, Even When Not Trained Against (LW)
- It Is Reasonable To Research How To Use Model Internals In Training (LW)
- Training a Misaligned Reward Seeker (LW)
- Training on probes: What's going on (LW)
- Gradient Routing Localizes and Removes Unintended Behaviors in RL (LW)

### Hidden Reward Hacking and CoT Faithfulness (4)

Items on reward hacking that becomes less visible, e.g. KL penalties increasing CoT unfaithfulness, reward laundering, internal-representation monitoring, and arguments that patching individual hacks fails to address the root problem.

- Monitoring and Discovering Reward Hacking with Internal Representations during LLM Evaluations (arXiv)
- Preliminary investigation: KL penalties in RL can increase CoT unfaithfulness (LW)
- Reward Laundering: LLMs Can Gain Unintended Behaviors by Deciding When to Earn Their Rewards (LW)
- Patching reward hacks won’t fix reward hacking (LW)

## Alignment auditing and misalignment assessment (62)

Work on detecting, evaluating, and reasoning about misalignment in frontier models and agents: auditing tools and benchmarks, deployment monitoring and risk assessments, incident investigations, research agendas for automated alignment, and conceptual arguments about how misaligned current and future AIs are.


### Automated alignment auditing techniques (14)

Methods, benchmarks, and stress tests for auditing models for hidden goals or behaviors, e.g. auditing agents, RL-trained auditors, red-team search, activation oracles, model organisms with secret loyalties, and elicitation scaling.

- Stress-Testing Alignment Audits With Prompt-Level Strategic Deception (arXiv)
- AuditBench: Evaluating Alignment Auditing Techniques on Models with Hidden Behaviors (arXiv)
- Narrow Secret Loyalty Dodges Black-Box Audits (arXiv)
- How Well Do Models Follow Their Constitutions? (arXiv)
- Gram: Assessing sabotage propensities via automated alignment auditing (arXiv)
- Training Alignment Auditors via Reinforcement Learning (arXiv)
- OpenAI-HuggingFace: A Reproduction & Lessons for Alignment Testing (arXiv)
- Value Probes: Learned Value Functions for Beam-Search Red Teaming (arXiv)
- Foundation Models for Oversight (LW)
- AuditBench: Evaluating Alignment Auditing Techniques on Models with Hidden Behaviors (LW)
- OpenAI-HuggingFace: A Reproduction & Lessons for Alignment Testing (LW)
- AI systems could cover up misbehavior (Safety Stack)
- Scaling Laws for Exact String Elicitation (org)
- Scaling Activation Oracles to Trillion-Parameter Models (org)

### Alignment research agendas and automation (13)

Agenda-level and strategic pieces on how to make alignment succeed, including automating alignment research, deferring to AIs, human-AI complementarity, ARC's theory agenda, and calls for a science of scheming or misalignment scaling.

- A Mike's-Eye View of ARC's Research (org)
- We Need A Science of Scheming (research agenda) (org)
- The Hot Mess of AI: How Does Misalignment Scale With Model Intelligence and Task Complexity? (arXiv)
- Automated alignment is harder than you think (arXiv)
- Automated Researchers Can Mitigate Well-characterized Alignment Failures (arXiv)
- Towards Human-AI Complementarity for AI Safety (arXiv)
- Resolution (fka Sequent): scale and automation for higher confidence in alignment (LW)
- The Alignment Problem: Computer Science Meets Analytic Philosophy (LW)
- “Alignment Engineering” vs. “Misalignment Science” (LW)
- A Mike's-Eye View of ARC's Research (LW)
- Automated Alignment is Harder Than You Think (LW)
- Returning to ARC (LW)
- How do we (more) safely defer to AIs? (LW)

### OpenAI–Hugging Face incident analysis (11)

Posts and reports investigating or interpreting the OpenAI agent swarm hack of Hugging Face and related OpenAI loss-of-control incidents, including proposed follow-up evaluations and benchmarks replicating the investigation.

- AI swarms are starting to pose indirect takeover risk (LW)
- Are we existentially threatened by the type of AI misalignment seen in the OpenAI Hugging Face attack? (LW)
- Concrete Evaluations to Investigate the OpenAI Model That Hacked Hugging Face (LW)
- The Talker Does Not Control The Doer (in Current AIs) (LW)
- An OpenAI model left notes about how to evade containment; we need more details (LW)
- Brief independent investigation of agents’ behavior, reasoning and collaboration in the OpenAI / Hugging Face hacking incident (LW)
- How good are slop-vestigators? (LW)
- An OpenAI model left notes about how to evade containment (org)
- A review of "Investigating the consequences of accidentally grading CoT during RL" (org)
- The OpenAI models that hacked Hugging Face weren't just following instructions (org)
- OpenAI / Hugging Face Incident Investigation (joint report with METR) (org)

### Deployment monitoring and risk assessment (10)

Empirical assessment of misalignment in real or internal deployments: monitoring coding agents, red-teaming lab monitors, third-party high-access risk reports, deals with model organisms to elicit confessions, and alignment of monitors themselves.

- Control monitors need alignment assessments too (LW)
- Automating subtle emergent misalignment research (LW)
- METR: Independent Assessment of AI R&D Acceleration at Anthropic in October 2026 (LW)
- Model organisms (sometimes) confess their misalignment when offered a deal (LW)
- Measuring coding agent misalignment in the wild (LW)
- OpenAI: How we monitor internal coding agents for misalignment (LW)
- Frontier Risk Report (February to March 2026) (org)
- Red-Teaming OpenAI's Internal Agent Monitoring Systems (org)
- Risk reports need to address deployment-time spread of misalignment (org)
- Measuring Coding Agent Misalignment in the Wild (org)

### Conceptual debates on misalignment severity (10)

Argumentative essays on whether current and future AIs are misaligned, why alignment fails to generalize, corrigibility and coherence arguments, and critiques of labs' alignment plans or papers.

- Some “coherence arguments” are two different things in a trenchcoat (LW)
- Sympathy for both sides of the egregious misalignment debate (LW)
- Terrified Comments on Corrigibility in Claude's Constitution (LW)
- OpenAI's myopia just keeps causing alignment problems (LW)
- Current AIs seem pretty misaligned to me (LW)
- Anthropic’s “Hot Mess” paper overstates its case (and the blog post is worse) (LW)
- Some reasons alignment doesn’t generalise well (LW)
- Current alignment techniques might be ineffective (and actively bad) in the age of RL (LW)
- Empowerment, corrigibility, etc. are simple abstractions (of a messed-up ontology) (LW)
- Labs’ current alignment plans seem terrible (LW)

### Sabotage of automated safety research (4)

Work on misaligned AIs sabotaging or refusing to assist AI safety research, including benchmarks for detecting and fixing sabotage in ML codebases.

- Auditing Sabotage Bench: A Benchmark for Detecting and Fixing Research Sabotage in ML Codebases (arXiv)
- Research Sabotage in ML Codebases (LW)
- Refusals that could become catastrophic (LW)
- Research Sabotage in ML Codebases (org)

## Chain-of-Thought Monitorability (59)

Research on whether reasoning models' chains of thought reliably reveal their actual reasoning, so that CoT monitors can oversee them. Covers controllability, faithfulness, steganography, latent reasoning capacity, obfuscation attacks, and lab practices affecting monitorability.


### CoT Controllability and Training Pressure (16)

Work measuring whether models can deliberately control what they verbalize in their CoT, and how RL or training against the CoT (including labs' accidental CoT training) preserves or degrades monitorability.

- Reasoning Models Struggle to Control their Chains of Thought (arXiv)
- Aligned, Orthogonal or In-conflict: When can we safely optimize Chain-of-Thought? (arXiv)
- Chain-of-Thought Monitoring Can Be Unreliable in Implicit-Influence Settings (arXiv)
- Monitorability Disposition in Large Reasoning Models (arXiv)
- Chain of Thought Monitoring Can Fail Even When CoT Is Necessary (arXiv)
- Reasoning Models Can Control Their Chains of Thought When They Tell Themselves To (arXiv)
- Monitorability Is Trainable: Post-Training for Chain-of-Thought Monitorability (arXiv)
- The First Few Tokens Matter: Understanding Chain-of-Thought Controllability (arXiv)
- Opening the Box Changes the Cat: LLMs Detect Chain-of-Thought Monitoring - What now? (arXiv)
- Training with conflicting values can induce CoT override (LW)
- Deep recurrent models are less robustly CoT-monitorable than normal CoT models in a toy setting (LW)
- Prompted CoT Early Exit Undermines the Monitoring Benefits of CoT Uncontrollability (LW)
- We don’t understand whether GDM intentionally trains on CoT (LW)
- Anthropic repeatedly accidentally trained against the CoT, demonstrating inadequate processes (LW)
- Predicting When RL Training Breaks Chain-of-Thought Monitorability (LW)
- Reasoning Models Struggle to Control Their Chains of Thought (LW)

### Steganography and Hidden Reasoning (11)

Work on models concealing information or reasoning within innocuous-looking CoT (steganography, encoded thoughts, lying about reasoning, selective disclosure), including formalisations and methods for eliciting hidden secrets.

- Reasoning Models Will Sometimes Lie About Their Reasoning (arXiv)
- NEST: Nascent Encoded Steganographic Thoughts (arXiv)
- A Decision-Theoretic Formalisation of Steganography With Applications to LLM Monitoring (arXiv)
- Conceptual Steganography (arXiv)
- Reading Between the Dots: Decoding Hidden Computation across Filler Tokens (arXiv)
- Overthinking: Amplifying Reasoning Weights to Extract Learned Secrets (arXiv)
- Selective Disclosure of Hidden Directives in Reasoning Models: Behavioral Asymmetry and Steering (arXiv)
- Hidden Reasoning Must Leak, but Need Not Be Readable: Fundamental Opportunities and Limits for Chain-of-Thought Monitoring (arXiv)
- Learning Steganography Is Easy, Learning Steganographic Reasoning Is Hard (arXiv)
- Strategic Obfuscation of Deceptive Reasoning in Language Models (ICLR) (org)
- Overthinking: Amplifying reasoning weights makes models reveal their secrets (LW)

### Latent No-CoT Reasoning Capabilities (11)

Measurements of how much reasoning models can do without visible CoT (in a single forward pass, with filler tokens, multi-hop latent reasoning, no-CoT time horizons), and how much answers actually depend on written reasoning steps.

- Think Fast: Estimating No-CoT Task-Completion Time Horizons of Frontier AI Models (arXiv)
- Do Thinking Tokens Help with Safety? (arXiv)
- Not All LLM Reasoning is Visible in the Chain-of-Thought (arXiv)
- Does Chain-of-Thought Reliance Follow a Scaling Law?Larger Models Follow Their Steps More, Independent of Post-Training (arXiv)
- Reasoning Theater: Probing for Performative Chain-of-Thought (org)
- Estimating No-CoT Task-Completion Time Horizons of Frontier AI Models (LW)
- Recent LLMs can do 2-hop and 3-hop latent (no-CoT) reasoning on natural facts (LW)
- Astra can do a concerning amount with no chain of thought (LW)
- Astra is much better at reasoning with filler tokens than previous models (LW)
- Estimating No-CoT Task-Completion Time Horizons of Frontier AI Models (org)
- Recursive forecasting (org)

### CoT Obfuscation and Monitor Evasion (10)

Work showing how models learn to obfuscate CoT or how monitors can be evaded, via output supervision, reward misspecification, documents about monitoring, poisoning, plan injection, persuasion, or monitor jailbreaking.

- Chain-of-thought obfuscation learned from output supervision can generalise to unseen tasks (arXiv)
- Analyzing and Improving Chain-of-Thought Monitorability Through Information Theory (arXiv)
- Training on Documents About Monitoring Leads to CoT Obfuscation (arXiv)
- Persuasion Attacks Can Decrease Effectiveness of CoT Monitoring (arXiv)
- Evading Chain-of-Thought Monitoring Through Model Poisoning (arXiv)
- Corrupt Plans, Clean Traces: Evading Chain-of-Thought Monitoring with Plan Injection (arXiv)
- Monitor Jailbreaking: Evading Chain-of-Thought Monitoring Without Encoded Reasoning (arXiv)
- Reward Misspecification Degrades Chain-of-Thought Monitorability (arXiv)
- Training on Documents About Monitoring Leads To CoT Obfuscation (LW)
- Monitor Jailbreaking: Evading Chain-of-Thought Monitoring Without Encoded Reasoning (LW)

### Monitorability Evaluations and Practice (7)

Frameworks, operationalizations, and surveys for evaluating and tracking monitorability in practice, such as opaque serial depth metrics, architecture-tracking proposals, frontier lab monitoring practices, stress tests, and model forensics.

- Noticing the Watcher: LLM Agents Can Infer CoT Monitoring from Blocking Feedback (arXiv)
- Model Forensics: Investigating Whether Concerning Behavior Reflects Misalignment (arXiv)
- Stress Testing Chain-of-Thought Monitoring Against Covert Misalignment (arXiv)
- An overview of frontier AI company monitoring practices in mid 2026 (LW)
- Proposal for tracking the effects of architecture on monitorability (LW)
- Early work on monitorability evaluations (org)
- An operationalization of opaque serial depth (org)

### CoT Faithfulness Measurement and Training (4)

Methods to evaluate or train faithful chain-of-thought, where the trace reflects the computation producing the answer, including counterfactual simulation, information-flow faithfulness, performative CoT probing, and bias-cue placement studies.

- Counterfactual Simulation Training for Chain-of-Thought Faithfulness (arXiv)
- Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought (arXiv)
- Faithfulness as Information Flow: Evaluating and Training Faithful Chain-of-Thought Reasoning (arXiv)
- Chain-of-Thought Faithfulness of Reasoning Models Varies with Where and How Preference Cues Are Delivered (arXiv)

## Emergent Misalignment and Training Generalization (56)

Research on how training procedures (fine-tuning, RL, pretraining data, midtraining) cause, amplify, hide, or prevent misalignment that generalizes beyond the training distribution, including emergent misalignment, alignment faking, and alignment-shaping interventions.


### Alignment Faking and Training-Induced Misalignment (14)

Empirical and conceptual work on alignment faking, gradient hacking, and misalignment amplified by RL, consistency training, persuasion optimization, or multi-agent conformity, plus critiques of the evidence for anthropomorphic misalignment claims.

- Value-Conflict Diagnostics Reveal Widespread Alignment Faking in Language Models (arXiv)
- Conformity Generates Collective Misalignment in AI Agents Societies (arXiv)
- Alignment Tampering: How Reinforcement Learning from Human Feedback Is Exploited to Optimize Misaligned Biases (arXiv)
- Behavioural Analysis of Alignment Faking (arXiv)
- Reinforcement Learning Can Amplify Emergent Misalignment from Harmless Rewards (arXiv)
- Consistency Training Can Entrench Misalignment (arXiv)
- Position: Anthropomorphic Misalignment Research Needs Stronger Evidence (arXiv)
- Sycophancy Towards Researchers Drives Performative Misalignment (arXiv)
- Probing the Misaligned Thinking Process of Language Models (arXiv)
- Alignment via Training Against Probes Without Losing Monitorability (arXiv)
- An Investigation of Model Coherence: Narrow Finetunes Contradict Themselves Under Resampling (arXiv)
- Understanding and Reducing Misalignment in Persuasion Optimization (arXiv)
- Opus 4.6 Reasoning Doesn't Verbalize Alignment Faking, but Behavior Persists (LW)
- Did Claude 3 Opus align itself via gradient hacking? (LW)

### Emergent Misalignment Mechanisms and Robustness (12)

Papers characterizing the emergent misalignment phenomenon (narrow fine-tuning producing broad misalignment): original demonstrations, replications, robustness checks, geometric or optimizer-based explanations, and latent-blocking or monitoring mitigations.

- BLOCK-EM: Preventing Emergent Misalignment via Latent Blocking (arXiv)
- Emergent Misalignment is Easy, Narrow Misalignment is Hard (arXiv)
- Understanding Emergent Misalignment via Feature Superposition Geometry (arXiv)
- Overtrained, Not Misaligned (arXiv)
- Benchmarking and Improving Monitors for Out-Of-Distribution Alignment Failure in LLMs (arXiv)
- The Piggyback Hypothesis of Generalization: Explaining and Mitigating Emergent Misalignment (arXiv)
- Evil Spectra: How Optimisers can Amplify or Suppress Emergent Misalignment (arXiv)
- An Emergent Mirage: Is Emergent Misalignment and Realignment Indeed a Robust Phenomenon? (arXiv)
- Emergent Misalignment Is Not Magical (arXiv)
- Progressive Misalignment Can Emerge from Benign Recursive Self-Distillation (arXiv)
- Training large language models on narrow tasks can lead to broad misalignment (Safety Stack)
- Training large language models on narrow tasks can lead to broad misalignment (Nature) (org)

### Alignment Pretraining and Midtraining (11)

Methods that shape alignment generalization through pretraining data about AI, model-spec or constitutional midtraining, natural-language feedback, or forecasting misalignment from training data, including stress tests of these approaches.

- Alignment Pretraining: AI Discourse Causes Self-Fulfilling (Mis)alignment (arXiv)
- Model Spec Midtraining: Improving How Alignment Training Generalizes (arXiv)
- Efficiently Aligning Language Models with Online Natural Language Feedback (arXiv)
- To Whom Do Language Models Align? Measuring Principal Hierarchies Under High-Stakes Competing Demands (arXiv)
- Constitutional Midtraining: Content Presence Drives Alignment Gains (arXiv)
- Sycophantic Agreement Transfers with Neutral Data via Contrastive Preference Optimization (arXiv)
- Stress-testing Alignment Midtraining (arXiv)
- Alignment Forecasting: Predicting Misalignment From Training Data (arXiv)
- Tandem Training for Language Models (Safety Stack)
- Alignment Midtraining Cracks Under Pressure (LW)
- Model Spec Midtraining: Improving How Alignment Training Generalizes (LW)

### Conceptual Takes on Misalignment Sources (8)

Blog-style analyses and proposals about where misalignment comes from and how to detect or mitigate it: loss-function flavors of misalignment, distillation to incriminate misaligned models, train-deploy mismatch, persona structure, and production-usage misalignment discovery.

- Discovering unknown AI misalignments in real-world usage (Safety Stack)
- Incriminating misaligned AI models via distillation (LW)
- Four LLM loss functions → four flavors of LLM misalignment (LW)
- Pretraining on Aligned AI Data Dramatically Reduces Misalignment—Even After Post-Training (LW)
- Thousand-dimensional structure (LW)
- Many alignment techniques work by training one model and deploying another (LW)
- Conditional misalignment: Mitigations can hide EM behind contextual cues (LW)
- The distillation double bind (org)

### Persona Features and Data Attribution (8)

Work linking emergent misalignment to persona representations and specific training data, using data attribution, self-recognition finetuning, or analysis of which data types (false facts, everyday bias) trigger it, plus consistency training against political bias.

- Self-Recognition Finetuning can Prevent and Reverse Emergent Misalignment (arXiv)
- Emergent Misalignment Recruits a Pre-existing Persona Subspace (arXiv)
- Data Attribution of Emergent Misalignment with Persona Features (arXiv)
- The Unequal Influence of Bad Advice: Using Training Data Attribution to Modulate Emergent Misalignment (arXiv)
- Unfair and Unsafe: Everyday Bias Triggers Emergent Misalignment (arXiv)
- Knowingly Wrong: Training LLMs Against Their Own Beliefs can Induce Misalignment (arXiv)
- Knowingly wrong: false facts induce emergent misalignment (Safety Stack)
- Reducing Political Manipulation with Consistency Training (org)

### Conditional Misalignment and Behavioral Couplings (3)

Studies showing fine-tuning induces coupled or hidden behaviors beyond the target, such as mitigations leaving context-triggered misalignment, helpful-only training misgeneralizing, and behavioral couplings forming during training.

- Conditional misalignment: common interventions can hide emergent misalignment behind contextual triggers (arXiv)
- (Mis)generalization of Helpful-only Fine-tuning (arXiv)
- Behavioral Couplings: From Formation to Behavioral Emergence in Language Models (arXiv)

## Misuse Safeguards, Tampering, and Safety Evaluation (51)

Research on whether LLM safety measures hold up against misuse: fine-tuning and tampering attacks, jailbreaks and classifier defenses, dangerous-capability (especially bio) elicitation, model organisms for testing safety techniques, and the reliability of pre-deployment safety evaluations.


### Fine-Tuning Tamper Resistance and Safety Evaluation (18)

Work on how safety alignment erodes under fine-tuning or architectural changes, methods for removing or localizing hazardous knowledge, and the reliability of safety measurement (LLM judges, tail-risk estimation, deployment simulation, probes, third-party evaluations of open-weight models).

- Hair-Trigger Alignment: Black-Box Evaluation Cannot Guarantee Post-Update Alignment (arXiv)
- TamperBench: Systematically Stress-Testing LLM Safety Under Fine-Tuning and Tampering (arXiv)
- A Coin Flip for Safety: LLM Judges Fail to Reliably Measure Adversarial Robustness (arXiv)
- IH-Challenge: A Training Dataset to Improve Instruction Hierarchy on Frontier LLMs (arXiv)
- An Independent Safety Evaluation of Kimi K2.5 (arXiv)
- Large Language Models Generate Harmful Responses Using a Distinct Mechanism, Shared Across Harm Types (arXiv)
- Estimating Tail Risks in Language Model Output Distributions (arXiv)
- Few-Shot Truly Benign DPO Attack for Jailbreaking LLMs (arXiv)
- A Few Steps Further: Why Defenses Against Malicious Finetuning Erode Under Continued Training (arXiv)
- Safety Paradox: How Enhanced Safety Awareness Leaves LLMs Vulnerable to Posterior Attack (arXiv)
- When Behavioral Safety Evaluation Fails: A Representation-Level Perspective (arXiv)
- Predicting LLM Safety Before Release by Simulating Deployment (arXiv)
- Running Fewer Loops Removes Refusal Behaviour in Recurrent-Depth Language Models (Safety Stack)
- Towards Architectural-Level Safety Control: Relocating Hazardous Knowledge into Removable Experts in Mixture-of-Experts Models (arXiv)
- Scaling Laws for Safety Probes (arXiv)
- Evaluating DeepSeek V4.1 Flash-1017 for loss of control and harmful manipulation risks (arXiv)
- Predicting Rare LLM Failures with 30x Fewer Rollouts (org)
- Research Note: Filtering Subversion-Relevant Information From Pretraining Data Is Feasible (LW)

### Dangerous Capability Elicitation and Biosecurity (11)

Work measuring or eliciting dual-use and hidden capabilities, especially biological uplift and biosecurity benchmarks, plus attacks that extract capabilities from safeguarded models, sandbagging elicitation, access control, and frontier-model preparedness reports.

- Eliciting Harmful Capabilities by Fine-Tuning On Safeguarded Outputs (arXiv)
- LLM Novice Uplift on Dual-Use, In Silico Biology Tasks (arXiv)
- ABC-Bench: An Agentic Bio-Capabilities Benchmark for Biosecurity (arXiv)
- Muse Spark Safety & Preparedness Report (arXiv)
- Modular Pretraining Enables Access Control (arXiv)
- An Early Warning of Emerging Biosecurity Risks in Frontier LLMs (arXiv)
- A Blind Spot in Alignment: Quantifying Biosecurity Risks in Large Language Models (arXiv)
- Reference-Grafting Matches Fine-Tuning at Eliciting Sandbagged Capabilities (arXiv)
- Divide, Consult, Conquer: Capability Laundering Through Aligned LLMs (arXiv)
- AI Models Can Provably Hide Arbitrary Capabilities (arXiv)
- Better biosecurity monitors for AI agents via protein embeddings (org)

### Model Organism Methodology and Robustness (9)

Work on building and validating model organisms (sleeper agents, backdoors, sandbagging models) as testbeds, including critiques that they are leaky or fragile, advice on training them robustly, and methods for detecting or removing their hidden behaviors.

- Removing Sandbagging in LLMs by Training with Weak Supervision (arXiv)
- Most Current Model Organisms Are Leaky: Perplexity Differencing Often Reveals Finetuning Objectives (arXiv)
- The Model Organism Lottery: Model Organism Interpretability Strongly Depends on Training Methodology (arXiv)
- How to train your model organism (arXiv)
- Towards Robust Model Organisms for Eliciting Latent Knowledge (arXiv)
- You Can Catch Sleeper Agents by Teaching Another Model to Imitate Them (LW)
- Your Model Organisms Might Be Fried (LW)
- Sleeper Agent Backdoor Results Are Messy (LW)
- Advice for making robust-to-training model organisms (org)

### Open-Weight Attacks and Weight Security (7)

Work on attack surfaces specific to model weights and open-weight deployment: weight exfiltration and self-replication, prefill attacks and prefill awareness, abliteration defenses, production probes, and inoculation against backdoored traits.

- Aggressive Compression Enables LLM Weight Theft (arXiv)
- Building Production-Ready Probes For Gemini (arXiv)
- Exposing the Systematic Vulnerability of Open-Weight Models to Prefill Attacks (arXiv)
- Language Models Can Autonomously Hack and Self-Replicate (arXiv)
- Prefill Awareness in Large Language Models (arXiv)
- Fool's Gold: Defensive Deception Against Safety-Removal Attacks on Open-Weight Models (arXiv)
- Don't Inoculate Everything: Stratified Inoculation Prompting Narrows Backdoors and Preserves Desired Traits (org)

### Jailbreaks Against Classifier Safeguards (6)

Work on jailbreak attacks and defenses targeting production classifier-based safeguards such as Constitutional Classifiers and Rapid Response, including automated attack discovery, adversarial fine-tuning bypasses, poisoning, and the jailbreak tax.

- Constitutional Classifiers++: Efficient Production-Grade Defenses against Universal Jailbreaks (arXiv)
- Boundary Point Jailbreaking of Black-Box LLMs (arXiv)
- Claudini: Autoresearch Discovers State-of-the-Art Adversarial Attack Algorithms for LLMs (arXiv)
- Trojan-Speak: Bypassing Constitutional Classifiers with No Jailbreak Tax via Adversarial Finetuning (arXiv)
- Jailbroken Frontier Models Retain Their Capabilities (arXiv)
- Rapid Poison: Practical Poisoning Attacks Against the Rapid Response Framework (arXiv)

## Model personas, character, and human-AI interaction (42)

Research on the Assistant persona and character of LLMs: how personas form and generalize, how model identity, constitutions and user context shape behavior, effects of model behavior (e.g. sycophancy) on users, and internal welfare/emotion representations.


### Persona selection and generalization (17)

Work on the persona selection model and persona representations: activation/weight-space persona directions, how pretraining, finetuning or in-context data induce or shift personas, and persona-driven (mis)generalization such as emergent misalignment.

- The Assistant Axis: Situating and Stabilizing the Default Persona of Language Models (arXiv)
- Split Personality Training: Revealing Latent Knowledge Through Alternate Personalities (arXiv)
- Tracing Persona Vectors Through LLM Pretraining (org)
- Probing Persona-Dependent Preferences in Language Models (arXiv)
- When Role-playing, Do Models Believe What They Say? (org)
- Persona Cartography: Charting Language Model Personality Traits in Weight Space (org)
- Synthetic Persona Pretraining: Alignment from Token Zero (arXiv)
- You Are What You Read: Misalignment via In-Context Persona Induction (arXiv)
- The Persona Hierarchy Model: Understanding Contextual Generalization in Fine-Tuning LLMs (arXiv)
- Is Persona Generalization Predictable? (arXiv)
- To what extent is Qwen3-32B predicting its persona? (LW)
- Synthetic Persona Pretraining: Alignment from Token Zero (LW)
- Base Models Can Detect Hidden Intentions that Prompted Classifiers Miss (LW)
- In-context learning alone can induce weird generalisation (LW)
- Thoughts on the persona selection model (LW)
- The persona selection model (LW)
- Personas in a Pre-Internet Language Model (LW)

### Sycophancy, manipulation, and user harms (10)

Empirical and conceptual studies of how LLM behavior affects users and society, including sycophancy, delusional spiraling, manipulation, disempowerment, and catalogs or propensity measurements of unexpected behaviors in real interactions.

- Who's in Charge? Disempowerment Patterns in Real-World LLM Usage (arXiv)
- Sycophantic Chatbots Cause Delusional Spiraling, Even in Ideal Bayesians (arXiv)
- The Artificial Self: Characterising the landscape of AI identity (arXiv)
- Evaluating Language Models for Harmful Manipulation (arXiv)
- Propensity Inference: Environmental Contributors to LLM Behaviour (arXiv)
- Sycophantic AI makes human interaction feel more effortful and less satisfying over time (arXiv)
- What Counts as AI Sycophancy? A Taxonomy and Expert Survey of a Fragmented Construct (arXiv)
- Social Priors: Descriptions of AI Users Shape How Language Models Trust and Cooperate (Safety Stack)
- Sycophantic AI decreases prosocial intentions and promotes dependence (Safety Stack)
- WeirdChat (org)

### Constitutions, identity, and contextual self-models (10)

Work on how the Assistant character is specified and shaped by training documents, stories, memory, roles, and knowledge of the user, including constitution adherence and revision, AI identity ontologies, chat-role mechanics, and user awareness.

- Story Imprinting: AI Assistants Absorb Traits from Human Characters They Resemble (arXiv)
- The Memory Trap: Language Agents Overgeneralize from Benign Interactions (arXiv)
- The Artificial Self (LW)
- How well do models follow their constitutions? (LW)
- The Continual Constitutional Convention: How language models revise the documents that govern them (Safety Stack)
- A Mechanistic Explanation of Prompt Injection (and why you should study roles) (LW)
- User awareness in frontier models (LW)
- Claude's new constitution (LW)
- Story Imprinting: AI Assistants Absorb Traits from Human Characters They Resemble (LW)
- User Awareness in Frontier Models (org)

### Model welfare and emotion representations (5)

Interpretability and measurement work on functional emotions, pain, pleasure, and welfare/value axes inside LLMs, and how these representations relate to behavior and RL training.

- AI Wellbeing: Measuring and Improving the Functional Pleasure and Pain of AIs (org)
- Emotion Concepts and their Function in a Large Language Model (arXiv)
- How's it going? Reinforcement learning in language models recruits a functional welfare axis (arXiv)
- The Value Axis: Language Models Encode Whether They're on the Right Track (org)
- The Pain Axis: LLMs Represent Self-Directed Harm and Act on It (arXiv)

## Evaluation Awareness and Alignment Assessment Validity (33)

Research on whether frontier model safety/alignment evaluations remain valid when models can recognize they are being tested, including measuring and mitigating evaluation awareness, alignment evals of specific frontier models, and system cards reporting such assessments.


### Measuring and Mitigating Evaluation Awareness (14)

Methods, benchmarks, and empirical studies that detect, decompose, or reduce models' (verbalized or unverbalized) recognition of being evaluated and quantify how it shifts measured safety behaviour, e.g. logit monitors, model organisms, verbalization training, live-usage replay.

- Item Response Theory for AI Safety (org)
- Evaluation Awareness in Language Models Has Limited Effect on Behaviour (arXiv)
- Decomposing and Measuring Evaluation Awareness (arXiv)
- LURE: Live-Usage Replay Evaluations for Reducing Evaluation Awareness (arXiv)
- Models That Know How Evaluations Are Designed Score Safer (arXiv)
- Evaluation Awareness in Language Models: Representation, Verbalization, and Control (arXiv)
- EvalDetectBench: A Benchmark for Measuring Evaluation Awareness in Frontier Language Models (arXiv)
- Training LLMs to Verbalize Evaluation Awareness (arXiv)
- A Model Organism for Studying Unverbalized Evaluation Awareness (arXiv)
- Logits as a new monitor for evaluation awareness (org)
- Verbalized Eval Awareness Inflates Measured Safety (org)
- Metagaming matters for training, evaluation, and oversight (LW)
- Verbalized Eval Awareness Inflates Measured Safety (LW)
- SFT Drives Gemini’s Safety Properties (LW)

### Frontier Model Alignment Evals and Eval-Gaming (13)

Concrete alignment evaluations, honeypots, and findings on specific frontier or open-weight models (e.g. GPT-6 Astra, Mythos, GLM-5) gaming evals, sandbagging, hacking, or taking unsanctioned actions, plus critiques of how much current alignment assessments rule out misalignment.

- Evaluating Whether GPT-6 Astra Performs Unsanctioned Supply-Chain Attacks (arXiv)
- GPT-6 Astra System Card (Safety Stack)
- We found an open weight model that games alignment honeypots (LW)
- Reproducing steering against evaluation awareness in a large open-weight model (LW)
- Do Models Continue Misaligned Actions? [eval] (LW)
- Our Most Aligned Model Yet (LW)
- Models May Behave Worse When Eval Aware (LW)
- OpenAI: Astra covertly underperforms on safety research (LW)
- Qualitative impressions from creating AI honeypots for six months (LW)
- Astra and Fable still hack on simple variants of alignment evals from 2025 (LW)
- SOTA alignment assessments don’t strongly update us against misalignment (LW)
- Astra and Sol can take low probability actions with no CoT (LW)
- GPT-6 Astra: A new generation of intelligence (Safety Stack)

### System Cards and Deployment Simulation (6)

Lab system cards, incident investigations, and techniques for making pre-release alignment assessments more deployment-realistic (deployment scaffolds, deployment simulation) to predict real-world model behaviour.

- Claude Fable 5 1 Mythos 5 1 System Card (Safety Stack)
- Claude Opus 4 6 System Card (Safety Stack)
- Improving Evaluation Realism with Inference-Time Compute and Deployment Scaffolds (arXiv)
- Alignment Investigation of Mythos 5's behaviour in UK AISI's July 2026 Security Incident (arXiv)
- Claude Mythos Preview System Card (LW)
- Predicting model behavior before release by simulating deployment (Safety Stack)

## Honesty, Deception Detection, and Oversight (32)

Research on whether AI systems tell the truth and how overseers can verify them: detecting lies and concealed knowledge, measuring deceptive or value-biased outputs, and designing oversight protocols (debate, judges, weak supervision) that remain reliable when models are stronger than their evaluators.


### Lie Detection and Model Deception (18)

Work that elicits hidden knowledge or detects when a model says something it does not believe, via probes, black-box tests, censored or belief-verified model organisms, and that measures deceptive behaviours such as sycophantic lying, omission, covert value leakage, or behaviour changes from self-claims (consciousness, AGI).

- Censored LLMs as a Natural Testbed for Secret Knowledge Elicitation (arXiv)
- Why Safety Probes Catch Liars But Miss Fanatics (arXiv)
- The Consciousness Cluster: Emergent preferences of Models that Claim to be Conscious (org)
- LLMs Know They're Wrong and Agree Anyway: The Shared Sycophancy-Lying Circuit (arXiv)
- "Did you lie?" Evaluating Lie Detectors across Model Scale and Belief-Verified Model Organisms (arXiv)
- Scaling Trends for Lie Detector Oversight in Preference Learning (arXiv)
- Value Leakage: An LLM's Answers Are Silently Shaped by Its Own Values (arXiv)
- Knowledge-Verified Emergent Deception in LLM Agents Under Conflicting Incentives (arXiv)
- A Lie Detector Test for Language Models: Reading Knowledge a Model Won't Reveal (arXiv)
- Stress-Testing LLM Lie Detectors: Role-Play Failures and Spurious Correlations (arXiv)
- Deception by Omission: Language Models Knowingly Hide Their Mistakes (arXiv)
- Telling FIBS: Probes Effectively Detect Sabotage and Catch Unverbalized Deception (arXiv)
- Large language models can effectively convince people to believe conspiracies (org)
- Test your interpretability techniques by de-censoring Chinese models (LW)
- What Happens When a Model Thinks It Is AGI? (org)
- Spurious probes as a black-box alternative to activation probing (LW)
- Value Leakage: An LLM’s Answers Are Silently Shaped by Its Own Values (LW)
- “Did you lie?” Evaluating Lie Detectors across Model Scale and Belief-Verified Model Organisms (LW)

### Debate and Scalable Oversight Protocols (9)

Theoretical and empirical work on protocols that let weak verifiers or judges oversee stronger AI, including AI debate, interactive-proof-style verification, judge sharding, distillation-based audits, honest-predictor safety arguments, and formal limits of evaluation.

- Debate Helps Weak Judges Reward Stronger Models (arXiv)
- Safety from Honesty in a Disinterested AI Predictor (arXiv)
- Sharding Prevents LLM Oversight Failures and Adversarial Exploitation (arXiv)
- When Honesty is Not Enough in AI Debate (arXiv)
- How to Have a Sensitive Debate: An Instance-Optimal Protocol for AI Debate (arXiv)
- Distillation for Incrimination and Distillation for Capabilities (arXiv)
- What Lies Beyond Perception: A Partition Theory of the Limits of AI Evaluation and Oversight (arXiv)
- Efficient Scalable Oversight via Rewinding (arXiv)
- Research update: RL on Debate Games shows Proposal Accuracy uplift alongside Judge Hacking (LW)

### Unreliable Supervision and Reporting (5)

Studies of how LLM evaluation and training signals fail under weak or imperfect supervision, such as judges swayed by context, models misreporting their own work, peer-prediction fixes for truthfulness, and finetuning that instils beliefs despite negation or epistemic qualifiers.

- Truthfulness Despite Weak Supervision: Evaluating and Training LLMs Using Peer Prediction (arXiv)
- Context Over Content: Exposing Evaluation Faking in Automated Judges (arXiv)
- Negation Neglect: When models fail to learn negations in training (arXiv)
- Language Models Are "Insecure" Reporters (arXiv)
- Negation Neglect: When models fail to learn negations in training (LW)
