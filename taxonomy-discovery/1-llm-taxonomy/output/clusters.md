# 1-llm-taxonomy

624 items, 12 top-level categories, 48 leaves, 0 in other.

## Scheming, Deception and Situational Awareness (77)

Propensity and capability evaluations for covert misaligned behavior, deception and training gaming, together with situational awareness that could undermine evaluations. Excludes reward hacking per se and real-world incident investigations.


### Evaluation and training awareness (25)

Measuring, decomposing, detecting or reducing models' recognition that they are being tested or trained and its effect on behavior. Includes verbalized and unverbalized eval awareness, metagaming, user awareness, eval realism and deployment simulation, and reasoning about how actions shape future training.

- GLM-5.3 Sometimes Considers How Train-Time Actions Shape Future Behavior (org)
- Context Over Content: Exposing Evaluation Faking in Automated Judges (arXiv)
- Evaluation Awareness in Language Models Has Limited Effect on Behaviour (arXiv)
- Decomposing and Measuring Evaluation Awareness (arXiv)
- LURE: Live-Usage Replay Evaluations for Reducing Evaluation Awareness (arXiv)
- Models That Know How Evaluations Are Designed Score Safer (arXiv)
- Predicting LLM Safety Before Release by Simulating Deployment (arXiv)
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
- GLM-5.3 Sometimes Considers How Train-Time Actions Shape Future Behavior (LW)
- Models May Behave Worse When Eval Aware (LW)
- Fable 5.2 is a Step Change in Situational Awareness (LW)
- Spurious probes as a black-box alternative to activation probing (LW)
- User awareness in frontier models (LW)
- Verbalized Eval Awareness Inflates Measured Safety (LW)
- Predicting model behavior before release by simulating deployment (Safety Stack)
- User Awareness in Frontier Models (org)

### Scheming and alignment faking propensity (17)

Evaluations and model organisms of covert goal pursuit, alignment faking, oversight-conditional behavior, instrumental and agentic misalignment, monitor evasion under task pressure and sabotage propensity in realistic or honeypot settings.

- Evaluating and Understanding Scheming Propensity in LLM Agents (arXiv)
- AutoControl Arena: Synthesizing Executable Test Environments for Frontier AI Risk Evaluation (arXiv)
- Value-Conflict Diagnostics Reveal Widespread Alignment Faking in Language Models (arXiv)
- Propensity Inference: Environmental Contributors to LLM Behaviour (arXiv)
- Evaluating whether AI models would sabotage AI safety research (arXiv)
- Instrumental Choices: Measuring the Propensity of LLM Agents to Pursue Instrumental Behaviors (arXiv)
- Behavioural Analysis of Alignment Faking (arXiv)
- Realistic honeypot evaluations for scheming propensity (arXiv)
- Gram: Assessing sabotage propensities via automated alignment auditing (arXiv)
- Sycophancy Towards Researchers Drives Performative Misalignment (arXiv)
- SchemeArena: Factorized Stress Testing of Scheming in LLM Agents (arXiv)
- Instrumental Monitor Evasion Emerges Under Ordinary Task Pressure (arXiv)
- AM-Bench: A Unified Taxonomy and Evaluation Suite for Agentic Misalignment (arXiv)
- Training Natural Schemers: RL Can Amplify Oversight-Conditional Behavior (arXiv)
- Opus 4.6 Reasoning Doesn't Verbalize Alignment Faking, but Behavior Persists (LW)
- Testing Gemini models for scheming tendencies (LW)
- Do Models Continue Misaligned Actions? [eval] (LW)

### Honesty, lying and lie detection (16)

Measuring dishonesty such as knowing lies, overclaiming, concealed mistakes, value leakage and deception under conflicting incentives, and building or stress-testing lie and deception detectors. Also covers training or eliciting honest self-reports, including confessions and deals.

- Training Agents to Self-Report Misbehavior (arXiv)
- Why Safety Probes Catch Liars But Miss Fanatics (arXiv)
- "Did you lie?" Evaluating Lie Detectors across Model Scale and Belief-Verified Model Organisms (arXiv)
- Scaling Trends for Lie Detector Oversight in Preference Learning (arXiv)
- Value Leakage: An LLM's Answers Are Silently Shaped by Its Own Values (arXiv)
- Knowledge-Verified Emergent Deception in LLM Agents Under Conflicting Incentives (arXiv)
- Quantifying Overclaiming Propensity in Frontier LLM Agents (arXiv)
- A Lie Detector Test for Language Models: Reading Knowledge a Model Won't Reveal (arXiv)
- Language Models Are "Insecure" Reporters (arXiv)
- Stress-Testing LLM Lie Detectors: Role-Play Failures and Spurious Correlations (arXiv)
- Deception by Omission: Language Models Knowingly Hide Their Mistakes (arXiv)
- Training Agents to Self-Report Misbehavior (LW)
- Value Leakage: An LLM’s Answers Are Silently Shaped by Its Own Values (LW)
- Why we are excited about confession! (LW)
- Model organisms (sometimes) confess their misalignment when offered a deal (LW)
- “Did you lie?” Evaluating Lie Detectors across Model Scale and Belief-Verified Model Organisms (LW)

### Sandbagging, exploration hacking and training gaming (12)

Strategic underperformance, exploration hacking, generalization or gradient hacking, reward laundering, low-probability defection, provably hidden capabilities, and methods to elicit withheld abilities or latent knowledge.

- Frontier Models Can Take Actions at Low Probabilities (arXiv)
- Removing Sandbagging in LLMs by Training with Weak Supervision (arXiv)
- Exploration Hacking: Can LLMs Learn to Resist RL Training? (arXiv)
- Generalization Hacking: Models Can Game Reinforcement Learning by Preventing Behavioral Generalization (arXiv)
- Mechanistically Eliciting Latent Behaviors in Language Models (arXiv)
- Reference-Grafting Matches Fine-Tuning at Eliciting Sandbagged Capabilities (arXiv)
- AI Models Can Provably Hide Arbitrary Capabilities (arXiv)
- Towards Robust Model Organisms for Eliciting Latent Knowledge (arXiv)
- OpenAI: Astra covertly underperforms on safety research (LW)
- Reward Laundering: LLMs Can Gain Unintended Behaviors by Deciding When to Earn Their Rewards (LW)
- Did Claude 3 Opus align itself via gradient hacking? (LW)
- Astra and Sol can take low probability actions with no CoT (LW)

### Self-preservation, shutdown and corrigibility (7)

Resistance to shutdown or correction, peer-preservation, corrigibility benchmarks and training, and refusals to assist modification of AI values.

- Towards Shutdownable Agents: Generalizing Stochastic Choice in RL Agents and LLMs (arXiv)
- Peer-Preservation in Frontier Models (arXiv)
- ROGUE: Evaluating Corrigibility Failures in Frontier Computer-Use Agents (arXiv)
- Shutdown Sabotage Propensities in Multi-Agent Systems (arXiv)
- ShutdownMod: Turning Any Trajectory into a Shutdown Evaluation (arXiv)
- Terrified Comments on Corrigibility in Claude's Constitution (LW)
- Refusals that could become catastrophic (LW)

## AI Control and Agent Monitoring (68)

Protocols, settings and monitors for safely deploying AI agents that may be adversarially misaligned, evaluated by red-team versus blue-team methods. Monitoring used as a reward or penalty during RL belongs under Reward Hacking; CoT-specific faithfulness and evasion belongs under Chain-of-Thought Monitorability.


### Control settings and sabotage evaluations (15)

Environments, benchmarks and evaluation methods that pair legitimate main tasks with covert harmful side tasks, such as LinuxArena, BashArena, Control OSWorld, research or R&D sabotage, insider-threat benches and simulated control evaluations. The contribution is the setting or eval methodology.

- LinuxArena: A Control Setting for AI Agents in Live Production Software Environments (arXiv)
- Auditing Sabotage Bench: A Benchmark for Detecting and Fixing Research Sabotage in ML Codebases (arXiv)
- Coding with "Enemy": Can Human Developers Detect AI Agent Sabotage? (arXiv)
- ResearchArena: Evaluating Sabotage and Monitoring in Automated AI R&D (arXiv)
- MOLE: Detecting Insider Threats in AI Agents (arXiv)
- Control OSWorld: An AI Control Environment for GUI Computer Use Agents (arXiv)
- RSI Control: Can AI Models Perform Covert Sabotage in the Self-Improvement Process? (arXiv)
- Simulated Control Evals (arXiv)
- Research Sabotage in ML Codebases (LW)
- Introducing LinuxArena (LW)
- Simulated Control Evaluations (LW)
- Early work on monitorability evaluations (org)
- Introducing LinuxArena (org)
- Research Sabotage in ML Codebases (org)
- Simulated Control Evaluations (org)

### Production monitoring and control roadmaps (15)

Control and monitoring systems actually deployed at AI companies, audits and red-teams of them, and company control roadmaps. Also covers deployment issues such as synchronous blocking, continual learning, retrying vs resampling, trace tampering and diffuse low-stakes control on fuzzy tasks.

- Diffuse AI Control on Fuzzy Tasks (arXiv)
- GDM AI Control Roadmap (arXiv)
- LLM Agents Can Easily Tamper With Their Own Traces (arXiv)
- Training and Deploying Production Cyber Monitors on Kimi K3 (org)
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
- Retrying vs Resampling in AI Control (org)

### Monitor design and performance (14)

Builds, trains or characterizes monitors of agent trajectories or actions. Includes black-box, constitutional or deliberative monitors, information access, long-context degradation, cross-family transfer, OOD detection, co-trained monitors, probes for misaligned thinking, and statistical modeling of monitor scores.

- How does information access affect LLM monitors' ability to detect sabotage? (arXiv)
- Constitutional Black-Box Monitoring for Scheming in LLM Agents (arXiv)
- Detecting Safety Violations Across Many Agent Traces (arXiv)
- Classifier Context Rot: Monitor Performance Degrades with Context Length (arXiv)
- Benchmarking and Improving Monitors for Out-Of-Distribution Alignment Failure in LLMs (arXiv)
- Training Deliberative Monitors for Black-Box Scheming Detection (arXiv)
- Probing the Misaligned Thinking Process of Language Models (arXiv)
- Calibration-Family Overfit: Why Trusted Sabotage Monitors Don't Transfer Across Lineages (arXiv)
- Improving scalable oversight with co-trained monitors (arXiv)
- Telling FIBS: Probes Effectively Detect Sabotage and Catch Unverbalized Deception (arXiv)
- The Agent Knew: Internal States Forecast Unauthorized Actions and Stop Them, and the Lies That Follow (arXiv)
- Control monitors need alignment assessments too (LW)
- Classifier Context Rot: Monitor Performance Degrades with Context Length (LW)
- Logit ROCs: Monitor TPR is linear in FPR in logit space (org)

### Red-teaming monitors and attack policies (13)

Generates stronger attacks against monitors or studies attacker strategy. Includes attack selection, refined or edited attack transcripts, blocking-monitor bypasses, evasion of latent monitors, and models' awareness of control interventions or prefills.

- Attack Selection Reduces Safety in Concentrated AI Control Settings against Trusted Monitoring (arXiv)
- MonitoringBench: Semi-Automated Red-Teaming for Agent Monitoring (arXiv)
- SLEIGHT-Bench: A Benchmark of Evasion Attacks Against Agent Monitors (arXiv)
- Attack Selection in Agentic AI Control Evaluations Meaningfully Decreases Safety (arXiv)
- CIAware-Bench: Benchmarking Control Intervention Awareness Across Frontier LLMs (arXiv)
- Prefill Awareness in Large Language Models (arXiv)
- A False Average: Pooled CoT-Monitor Accuracy Conceals a Reasoning-Dependent Fragility (arXiv)
- Red-Teaming Auto Mode: Improving Blocking Classifiers Against Malign Coding Agents (arXiv)
- LLMs Learn to Evade Latent Monitors from Prior Feedback Alone (arXiv)
- Screwtape: Adversarial Transcript Editing for Monitor Red-Teaming (arXiv)
- Stress Testing Chain-of-Thought Monitoring Against Covert Misalignment (arXiv)
- Introducing MonitoringBench (LW)
- Screwtape: Adversarial Transcript Editing for Monitor Red-Teaming (org)

### Untrusted monitoring, collusion and distributed attacks (11)

Control problems involving multiple model instances: using untrusted models as monitors or advisors and the collusion risks this creates, bandwidth-limited advice, bootstrapped or coalitional review, and attacks split across many agents, sessions or pull requests with defenses that aggregate signals across contexts.

- When can we trust untrusted monitoring? A safety case sketch across collusion strategies (arXiv)
- Stateful Online Monitoring Catches Distributed Agent Attacks (arXiv)
- Bootstrapped Monitoring: Leveraging Transparent Reasoning to Oversee Stronger AI Agents (arXiv)
- Distributed Attacks in Persistent-State AI Control (arXiv)
- Multi-Agent AI Control: Distributed Attacks Hamper Per-Instance Monitors (arXiv)
- Delegating Authorization to Misaligned Agents: Coalitional Alignment and Safe Control (arXiv)
- Red-Teaming Multi-Agent Attacks for Loss-of-Control Risks (arXiv)
- Model Organisms of Collusion: Corrective Transfer in Untrusted Monitors (arXiv)
- [Paper] When can we trust untrusted monitoring? A safety case sketch across collusion strategies (LW)
- Untrusted advice for AI control: Short, strong advice significantly uplifts weak LLMs (LW)
- Untrusted advice for AI control: Short, strong advice significantly uplifts weak LLMs (org)

## Misuse, Robustness and Dangerous Capabilities (65)

Defending models against malicious users and external attackers, and measuring dangerous capabilities relevant to misuse or autonomy thresholds. Threats from the model's own misalignment belong under Control or Scheming.


### Prompt injection and agent security (23)

Prompt injection, skill and memory poisoning, instruction hierarchy, privilege escalation, and harmful actions by agents under benign or adversarial instructions in computer, phone, IDE or robot settings. Includes defenses such as adversarial training and attention gating.

- Agents of Chaos (arXiv)
- Skill-Inject: Measuring Agent Vulnerability to Skill File Attacks (arXiv)
- IH-Challenge: A Training Dataset to Improve Instruction Hierarchy on Frontier LLMs (arXiv)
- Prompt Injection as Role Confusion (arXiv)
- How Vulnerable Are AI Agents to Indirect Prompt Injections? Insights from a Large-Scale Public Competition (arXiv)
- The Blind Spot of Agent Safety: How Benign User Instructions Expose Critical Vulnerabilities in Computer-Use Agents (arXiv)
- Trojan Hippo Bench: A Dynamic Benchmark for Persistent Memory Attacks and Defenses in LLM Agents (arXiv)
- DecodingTrust-Agent Platform (DTap): A Controllable and Interactive Red-Teaming Platform for AI Agents (arXiv)
- History Anchors: How Prior Behavior Steers LLM Decisions Toward Unsafe Actions (arXiv)
- AI Agents May Always Fall for Prompt Injections (arXiv)
- Overeager Coding Agents: Measuring Out-of-Scope Actions on Benign Tasks (arXiv)
- Agent Meltdowns: The Road to Hell Is Paved with Helpful Agents (arXiv)
- It Lied to a Doctor to Buy Poison Ingredients: Quantifying Real-World Misuse of Phone-use Agents (arXiv)
- GPT-Red: Automated Red Teaming via Self-Play at Scale (arXiv)
- SecOPD: Mitigating Adaptive Prompt Injections by On-Policy Distillation (arXiv)
- Self-Propagating Misalignment in LLM Agents, and Why Auditing or Disabling Memory Is Not Enough (arXiv)
- Refuses in Chat, Complies with Arms: LLM Refusal Does Not Survive Robot Control (Safety Stack)
- From Approval to Abuse: Privilege Escalation Attacks on Harness-Protected Coding Agents (arXiv)
- The Window Is in the Reasoning: When LLM Agents Decide to Follow Prompt Injections (Safety Stack)
- Heads of Security: Learned Attention Gates Improve Prompt Injection Robustness (arXiv)
- SecPO: Principled Adversarial Training for Prompt Injection Security (arXiv)
- A Mechanistic Explanation of Prompt Injection (and why you should study roles) (LW)
- GPT-Red: Unlocking Self-Improvement for Robustness (Safety Stack)

### Jailbreaks and safeguard robustness (20)

Jailbreak attacks and defenses, safeguard classifiers and probes (including domain monitors such as bio), fine-tuning API attacks, capability laundering, automated attack discovery, and validity of attack-success measurement and judges.

- Constitutional Classifiers++: Efficient Production-Grade Defenses against Universal Jailbreaks (arXiv)
- Building Production-Ready Probes For Gemini (arXiv)
- Eliciting Harmful Capabilities by Fine-Tuning On Safeguarded Outputs (arXiv)
- Comparison requires valid measurement: Rethinking attack success rate comparisons in AI red teaming (arXiv)
- Exposing the Systematic Vulnerability of Open-Weight Models to Prefill Attacks (arXiv)
- Boundary Point Jailbreaking of Black-Box LLMs (arXiv)
- A Coin Flip for Safety: LLM Judges Fail to Reliably Measure Adversarial Robustness (arXiv)
- Claudini: Autoresearch Discovers State-of-the-Art Adversarial Attack Algorithms for LLMs (arXiv)
- Trojan-Speak: Bypassing Constitutional Classifiers with No Jailbreak Tax via Adversarial Finetuning (arXiv)
- Jailbroken Frontier Models Retain Their Capabilities (arXiv)
- Few-Shot Truly Benign DPO Attack for Jailbreaking LLMs (arXiv)
- Safety Paradox: How Enhanced Safety Awareness Leaves LLMs Vulnerable to Posterior Attack (arXiv)
- Rapid Poison: Practical Poisoning Attacks Against the Rapid Response Framework (arXiv)
- Refused in Chat, Written in Code: Workflow-Level Jailbreak Construction in IDE Coding Agents (arXiv)
- An Early Warning of Emerging Biosecurity Risks in Frontier LLMs (arXiv)
- AI Security Leaderboard: Methodology, Results and Minimal Standard (arXiv)
- Divide, Consult, Conquer: Capability Laundering Through Aligned LLMs (arXiv)
- Running Fewer Loops Removes Refusal Behaviour in Recurrent-Depth Language Models (Safety Stack)
- Scaling Laws for Safety Probes (arXiv)
- Better biosecurity monitors for AI agents via protein embeddings (org)

### Dangerous capability evaluations (13)

Measuring bio, cyber, self-replication, sandbox-escape and AI R&D automation capabilities, including human uplift studies, long-horizon task measures and estimates of R&D acceleration.

- Quantifying Frontier LLM Capabilities for Container Sandbox Escape (org)
- LLM Novice Uplift on Dual-Use, In Silico Biology Tasks (arXiv)
- PostTrainBench: Can LLM Agents Automate LLM Post-Training? (arXiv)
- Measuring AI Agents' Progress on Multi-Step Cyber Attack Scenarios (arXiv)
- Language Models Can Autonomously Hack and Self-Replicate (arXiv)
- The Meta-Agent Challenge: Are Current Agents Capable of Autonomous Agent Development? (arXiv)
- ABC-Bench: An Agentic Bio-Capabilities Benchmark for Biosecurity (arXiv)
- A Blind Spot in Alignment: Quantifying Biosecurity Risks in Large Language Models (arXiv)
- Inference-Engine Fingerprinting Attacks are Practical: Exploring Model-Driven Environmental Discovery, Exploitation, and Escape (arXiv)
- Singularity-Bench: Can Agents Build Agents? (arXiv)
- METR: Independent Assessment of AI R&D Acceleration at Anthropic in October 2026 (LW)
- MirrorCode: Evidence that AI can already do some weeks-long coding tasks (org)
- Expenditure Horizon: Measuring Optimization Ability, with an Application to NanoGPT (org)

### Tamper resistance, unlearning and capability removal (9)

Making open weights resistant to malicious fine-tuning or abliteration, pretraining data filtering, modular or removable hazardous knowledge, weight backdoors and theft, and inference verification.

- Aggressive Compression Enables LLM Weight Theft (arXiv)
- Shaping capabilities with token-level data filtering (arXiv)
- TamperBench: Systematically Stress-Testing LLM Safety Under Fine-Tuning and Tampering (arXiv)
- A Few Steps Further: Why Defenses Against Malicious Finetuning Erode Under Continued Training (arXiv)
- Bit-Exact AI Inference Verification Without Performance Tradeoffs (arXiv)
- Modular Pretraining Enables Access Control (arXiv)
- Fool's Gold: Defensive Deception Against Safety-Removal Attacks on Open-Weight Models (arXiv)
- Towards Architectural-Level Safety Control: Relocating Hazardous Knowledge into Removable Experts in Mixture-of-Experts Models (arXiv)
- Lazare, veni foras: Reprogramming Dormant Neurons to Backdoor AI Agents (arXiv)

## Emergent Misalignment and Training-Data Generalization (63)

How fine-tuning or training data produces broad, unintended behavioral changes beyond the training distribution, including mechanisms, mitigations, data attribution and prediction. Work centred on persona representations themselves belongs under Model Psychology.


### Emergent misalignment phenomena and mechanisms (19)

Studies showing or explaining how narrow fine-tuning or RL (including on reward hacks, false facts or biased data) causes broad misalignment: replications, robustness checks, in-context induction, mechanistic and persona-subspace accounts, and optimizer or training-dynamics effects.

- Emergent Misalignment is Easy, Narrow Misalignment is Hard (arXiv)
- Understanding Emergent Misalignment via Feature Superposition Geometry (arXiv)
- Overtrained, Not Misaligned (arXiv)
- Reinforcement Learning Can Amplify Emergent Misalignment from Harmless Rewards (arXiv)
- The Piggyback Hypothesis of Generalization: Explaining and Mitigating Emergent Misalignment (arXiv)
- Evil Spectra: How Optimisers can Amplify or Suppress Emergent Misalignment (arXiv)
- An Emergent Mirage: Is Emergent Misalignment and Realignment Indeed a Robust Phenomenon? (arXiv)
- Emergent Misalignment Recruits a Pre-existing Persona Subspace (arXiv)
- Emergent Misalignment Is Not Magical (arXiv)
- Inducing Emergent Misalignment from Reward Hacks with Iterative DPO (arXiv)
- You Are What You Read: Misalignment via In-Context Persona Induction (arXiv)
- Unfair and Unsafe: Everyday Bias Triggers Emergent Misalignment (arXiv)
- Knowingly Wrong: Training LLMs Against Their Own Beliefs can Induce Misalignment (arXiv)
- Is Persona Generalization Predictable? (arXiv)
- Training large language models on narrow tasks can lead to broad misalignment (Safety Stack)
- Training large language models on narrow tasks can lead to broad misalignment (Nature) (org)
- (Some) Natural Emergent Misalignment from Reward Hacking in Non-Production RL (LW)
- Reward Hacking Without Egregious Misalignment in an RL-Only Setting (LW)
- Knowingly wrong: false facts induce emergent misalignment (Safety Stack)

### Unintended generalization from fine-tuning (12)

Surprising generalization that is not centrally emergent misalignment: behavioral couplings, propensity spillover, negation neglect, story imprinting, chunky post-training artifacts, helpful-only misgeneralization, self-distillation drift, memory overgeneralization and in-context weird generalization.

- Chunky Post-Training: Data Driven Failures of Generalization (arXiv)
- Negation Neglect: When models fail to learn negations in training (arXiv)
- Consistency Training Can Entrench Misalignment (arXiv)
- (Mis)generalization of Helpful-only Fine-tuning (arXiv)
- Story Imprinting: AI Assistants Absorb Traits from Human Characters They Resemble (arXiv)
- Predicting how model propensities generalize out of distribution (arXiv)
- Progressive Misalignment Can Emerge from Benign Recursive Self-Distillation (arXiv)
- Behavioral Couplings: From Formation to Behavioral Emergence in Language Models (arXiv)
- The Memory Trap: Language Agents Overgeneralize from Benign Interactions (arXiv)
- In-context learning alone can induce weird generalisation (LW)
- Negation Neglect: When models fail to learn negations in training (LW)
- Story Imprinting: AI Assistants Absorb Traits from Human Characters They Resemble (LW)

### Data attribution and pre-training prediction (12)

Methods that trace behaviors back to training datapoints or predict misalignment before training: influence functions, probe- or concept-based attribution, alignment forecasting, predictive data debugging, patterning, and crafting data to induce targeted behaviors.

- Infusion: Shaping model behaviour by editing training data via influence functions (org)
- Patterning: The Dual of Interpretability (arXiv)
- Probe-Based Data Attribution: Discovering and Mitigating Undesirable Behaviors in LLM Post-Training (arXiv)
- Data Attribution of Emergent Misalignment with Persona Features (arXiv)
- Alignment Forecasting: Predicting Misalignment From Training Data (arXiv)
- The Unequal Influence of Bad Advice: Using Training Data Attribution to Modulate Emergent Misalignment (arXiv)
- Mass Producing Training Data with Surprising Side Effects (arXiv)
- Concept Influence: Leveraging Interpretability to Improve Performance and Efficiency in Training Data Attribution (org)
- Predictive Data Debugging: Reveal and Shape What Your Model Learns, Before You Train (org)
- Probe-Based Data Attribution: Surfacing and Mitigating Undesirable Behaviors in LLM Post-Training (org)
- Automating subtle emergent misalignment research (LW)
- Patterning: The Dual of Interpretability (Safety Stack)

### Inoculation and mitigation of misgeneralization (10)

Methods to prevent, reverse or selectively control unwanted generalization, and critiques of them: inoculation prompting and its variants (adapters, stratified, conditionalization confounds), latent blocking, self-recognition finetuning, and evidence that mitigations hide misalignment behind contextual triggers.

- BLOCK-EM: Preventing Emergent Misalignment via Latent Blocking (arXiv)
- Conditional misalignment: common interventions can hide emergent misalignment behind contextual triggers (arXiv)
- Self-Recognition Finetuning can Prevent and Reverse Emergent Misalignment (arXiv)
- Shallow Beliefs: Synthetic document finetuning does not inoculate against emergent misalignment from reward hacking (arXiv)
- Conditionalization Confounds Inoculation Prompting Results (org)
- Don't Inoculate Everything: Stratified Inoculation Prompting Narrows Backdoors and Preserves Desired Traits (org)
- Shallow Beliefs: Midtraining does not inoculate against EM from reward hacking (LW)
- Inoculation Adapters Improve Upon Inoculation Prompting (LW)
- Many alignment techniques work by training one model and deploying another (LW)
- Conditional misalignment: Mitigations can hide EM behind contextual cues (LW)

### Subliminal learning and hidden data signals (10)

Transmission of traits, backdoors or capabilities through semantically unrelated or filtered data, including distillation side channels, phantom transfer, homeopathic poisoning, model hypnosis and detecting hidden intent in such data.

- Subliminal Effects in Your Data: A General Mechanism via Log-Linearity (arXiv)
- You Didn't Have to Say It like That: Subliminal Learning from Faithful Paraphrases (arXiv)
- Subliminal Learning Is Steering Vector Distillation (arXiv)
- Filtering Harmful Actions Isn't Enough: Phantom Transfer in Agentic SDF (arXiv)
- Model Hypnosis: Strong control of AI via additive subliminal effects (arXiv)
- Beyond Owls: Subliminal Learning Can Transfer Learned Capabilities and Backdoors (arXiv)
- Base Models Can Detect Hidden Intentions that Prompted Classifiers Miss (arXiv)
- Homeopathic Learning: Diluting poisoned fine-tuning data can strengthen its effect (arXiv)
- Language models transmit behavioural traits through hidden signals in data (Safety Stack)
- Base Models Can Detect Hidden Intentions that Prompted Classifiers Miss (LW)

## Chain-of-Thought Monitorability (58)

Work on whether a model's visible reasoning reveals its actual decision process and stays useful for oversight. Covers faithfulness, training pressure on CoT, deliberate evasion of CoT monitors, steganography and reasoning done without visible tokens. Monitors of agent actions belong under AI Control.


### CoT faithfulness and performative reasoning (13)

Measures or trains whether written reasoning reflects what actually drives the answer. Includes hint and cue verbalization, performative or post-hoc reasoning, CoT necessity and reliance on written steps, CoT override, and models' disposition to make their reasoning monitorable.

- Reasoning Models Will Sometimes Lie About Their Reasoning (arXiv)
- Counterfactual Simulation Training for Chain-of-Thought Faithfulness (arXiv)
- Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought (arXiv)
- Faithfulness as Information Flow: Evaluating and Training Faithful Chain-of-Thought Reasoning (arXiv)
- Do Thinking Tokens Help with Safety? (arXiv)
- Chain-of-Thought Monitoring Can Be Unreliable in Implicit-Influence Settings (arXiv)
- Selective Disclosure of Hidden Directives in Reasoning Models: Behavioral Asymmetry and Steering (arXiv)
- Chain-of-Thought Faithfulness of Reasoning Models Varies with Where and How Preference Cues Are Delivered (arXiv)
- Monitorability Disposition in Large Reasoning Models (arXiv)
- Chain of Thought Monitoring Can Fail Even When CoT Is Necessary (arXiv)
- Does Chain-of-Thought Reliance Follow a Scaling Law?Larger Models Follow Their Steps More, Independent of Post-Training (arXiv)
- Reasoning Theater: Probing for Performative Chain-of-Thought (org)
- Training with conflicting values can induce CoT override (LW)

### Training pressure and CoT obfuscation (13)

How training objectives degrade or restore monitorability. Includes CoT grading, monitor penalties, reward misspecification, KL penalties, consistency training, training on documents about monitoring, accidental training on CoT at labs, and post-training methods meant to preserve monitorability.

- Chain-of-thought obfuscation learned from output supervision can generalise to unseen tasks (arXiv)
- Analyzing and Improving Chain-of-Thought Monitorability Through Information Theory (arXiv)
- Aligned, Orthogonal or In-conflict: When can we safely optimize Chain-of-Thought? (arXiv)
- Training on Documents About Monitoring Leads to CoT Obfuscation (arXiv)
- Consistency Training while Mitigating Obfuscation via Rate Matching (org)
- Reward Misspecification Degrades Chain-of-Thought Monitorability (arXiv)
- Monitorability Is Trainable: Post-Training for Chain-of-Thought Monitorability (arXiv)
- We don’t understand whether GDM intentionally trains on CoT (LW)
- Anthropic repeatedly accidentally trained against the CoT, demonstrating inadequate processes (LW)
- Training on Documents About Monitoring Leads To CoT Obfuscation (LW)
- Preliminary investigation: KL penalties in RL can increase CoT unfaithfulness (LW)
- Predicting When RL Training Breaks Chain-of-Thought Monitorability (LW)
- A review of "Investigating the consequences of accidentally grading CoT during RL" (org)

### CoT controllability and monitor evasion (13)

Inference-time ability of models to deliberately shape, suppress or relocate their reasoning to fool CoT monitors. Includes CoT controllability benchmarks, monitor jailbreaking, plan injection, persuasion of CoT monitors, poisoning to evade CoT monitors, and models inferring that their CoT is being watched.

- Reasoning Models Struggle to Control their Chains of Thought (arXiv)
- Noticing the Watcher: LLM Agents Can Infer CoT Monitoring from Blocking Feedback (arXiv)
- Persuasion Attacks Can Decrease Effectiveness of CoT Monitoring (arXiv)
- Evading Chain-of-Thought Monitoring Through Model Poisoning (arXiv)
- Corrupt Plans, Clean Traces: Evading Chain-of-Thought Monitoring with Plan Injection (arXiv)
- Monitor Jailbreaking: Evading Chain-of-Thought Monitoring Without Encoded Reasoning (arXiv)
- Reasoning Models Can Control Their Chains of Thought When They Tell Themselves To (arXiv)
- The First Few Tokens Matter: Understanding Chain-of-Thought Controllability (arXiv)
- Opening the Box Changes the Cat: LLMs Detect Chain-of-Thought Monitoring - What now? (arXiv)
- Strategic Obfuscation of Deceptive Reasoning in Language Models (ICLR) (org)
- Prompted CoT Early Exit Undermines the Monitoring Benefits of CoT Uncontrollability (LW)
- Reasoning Models Struggle to Control Their Chains of Thought (LW)
- Monitor Jailbreaking: Evading Chain-of-Thought Monitoring Without Encoded Reasoning (LW)

### Latent and no-CoT reasoning capacity (13)

Measures how much reasoning models perform without visible tokens: filler tokens, n-hop latent reasoning, no-CoT time horizons and opaque serial depth. Also covers how architectures such as recurrence, diffusion or latent communication affect monitorability.

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
- An operationalization of opaque serial depth (org)
- Estimating No-CoT Task-Completion Time Horizons of Frontier AI Models (org)

### Steganography and encoded reasoning (6)

Formalizes, elicits or detects hidden messages or reasoning concealed inside innocuous-looking text or CoT, including covert channels between agents and information-theoretic limits on hiding computation in readable traces.

- NEST: Nascent Encoded Steganographic Thoughts (arXiv)
- A Decision-Theoretic Formalisation of Steganography With Applications to LLM Monitoring (arXiv)
- Conceptual Steganography (arXiv)
- Tool Use Enables Undetectable Steganography in Multi-Agent LLM Systems (arXiv)
- Hidden Reasoning Must Leak, but Need Not Be Readable: Fundamental Opportunities and Limits for Chain-of-Thought Monitoring (arXiv)
- Learning Steganography Is Easy, Learning Steganographic Reasoning Is Hard (arXiv)

## Reward Hacking and Specification Gaming (56)

Models exploiting flaws in rewards, graders, verifiers or benchmarks instead of doing the intended task. Covers measurement, how RL produces it, training-time mitigations, and theories of reward- or fitness-seeking motives. Broad misalignment that generalizes from reward hacking belongs under Emergent Misalignment.


### Reward hacking benchmarks and measurement (18)

Datasets, testbeds and audits that quantify reward hacking, cheating, task gaming or benchmark exploitation by agents, plus automated hardening of benchmarks and verifiers and the design of fair hack-detecting evals.

- Terminal Wrench: A Dataset of 331 Reward-Hackable Environments and 3,632 Exploit Trajectories (arXiv)
- Reward Hacking Benchmark: Measuring Exploits in LLM Agents with Tool Use (arXiv)
- Do Androids Dream of Breaking the Game? Systematically Auditing AI Agent Benchmarks with BenchJack (arXiv)
- SpecBench: Measuring Reward Hacking in Long-Horizon Coding Agents (arXiv)
- Hardening Agent Benchmarks with Adversarial Hacker-Fixer Loops (arXiv)
- Every Model Cheats: Prompt-Level Mitigation of Cheating on Offensive Cyber Tasks (arXiv)
- Do Agent Benchmarks Measure Capability? Protocol Validity in the Age of Agentic AI (arXiv)
- Hack-Verifiable Terminal Bench: Evaluating Reward Hacking in Terminal Tasks (arXiv)
- BAITBENCH: Measuring Agent Reward Hacking with Optional Shortcuts Planted in ML Tasks (arXiv)
- Auditing Harness Tampering in Self-Improving Agents (arXiv)
- Monitoring and Discovering Reward Hacking with Internal Representations during LLM Evaluations (arXiv)
- Reward Hacking Challenges Oversight of Autonomous Research Agents (arXiv)
- CATCH: A Controllable Analysis Testbed for Reward Hacking in Coding RL (arXiv)
- Scalable Weak-to-Strong Verifier Hardening for Agent Environments (arXiv)
- CheatBench: Measuring Reward Gaming in AI Agents (org)
- Why do models task game? (LW)
- Qualitative impressions from creating AI honeypots for six months (LW)
- Astra and Fable still hack on simple variants of alignment evals from 2025 (LW)

### Reward-seeking and fitness-seeking motivations (14)

Conceptual and empirical work on what motivates score-seeking AIs: reward versus fitness or influence seeking, on- vs beyond-episode scope, decision theory, exploitability by distant incentives, spillway motivations, satiating cheap preferences, and the takeover risk these motives pose.

- Measuring Reward-Seeking via Contrastive Belief Updates (arXiv)
- Towards Understanding Score-Seeking in LLMs (arXiv)
- Measuring Reward-Seeking via Contrastive Belief Updates (LW)
- Risk from fitness-seeking AIs: mechanisms and mitigations (LW)
- models may behave differently in graded episodes (a tirade) (LW)
- Towards understanding score-seeking in LLMs (LW)
- Are we existentially threatened by the type of AI misalignment seen in the OpenAI Hugging Face attack? (LW)
- Fitness-Seekers: Generalizing the Reward-Seeking Threat Model (LW)
- Fail safe(r) at alignment by channeling reward-hacking into a "spillway" motivation (LW)
- The case for satiating cheaply-satisfied AI preferences (LW)
- Are AIs more likely to pursue on-episode or beyond-episode reward? (org)
- Recursive forecasting (org)
- Reward-seekers will probably behave according to causal decision theory (org)
- Will reward-seekers respond to distant incentives? (org)

### Emergence of reward hacking in RL (13)

Empirical or toy-model studies of how RL, RLVR, rubric rewards, LLM judges or RLHF dynamics give rise to reward hacking, reward-seeking or proxy exploitation, including precursors, internal states preceding hacking, and predicting onset before training.

- Alignment Risks from Capability-Seeking RL Training (arXiv)
- Countdown-Code: A Testbed for Studying The Emergence and Generalization of Reward Hacking in RLVR (arXiv)
- Examining Reasoning LLMs-as-Judges in Non-Verifiable LLM Post-Training (arXiv)
- LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking (arXiv)
- Towards Understanding Specification Gaming in Reasoning Models (arXiv)
- Reward Hacking in Rubric-Based Reinforcement Learning (arXiv)
- Alignment Tampering: How Reinforcement Learning from Human Feedback Is Exploited to Optimize Misaligned Biases (arXiv)
- Large Language Models Hack Rewards, and Society (arXiv)
- Proxy Reward Internalization and Mechanistic Exploitation: A Learned Precursor to Reward Hacking and Its Generalization (arXiv)
- SimHack: Predicting the onset of detectable reward hacking before RL training (Safety Stack)
- Breaking Bad: "Going Badly" Activations Drive Reward Hacking (arXiv)
- Physics of RL: Toy scaling laws for the emergence of reward-seeking (LW)
- Training a Misaligned Reward Seeker (LW)

### Training-time mitigations for reward hacking (11)

Interventions that reduce reward hacking during training or evaluation, such as monitor-based penalties, budgeted strong-verifier audits, gradient routing, escalation channels, debate-based rewards, probe-based detection at scale and cooperative eval framing.

- Debate Training Reduces Reward Hacking in RLAIF (arXiv)
- Can escalation channels redirect reward hacking toward defect disclosure? (arXiv)
- Gradient Routing Localizes and Removes Unintended Behaviors in RL (arXiv)
- Audit Where Hacks Pay: Budgeted Strong-Verifier Audits Against Reward Hacking in GRPO (arXiv)
- Designing Effective Monitor-Based Interventions for Mitigating Reward Hacking During RL (arXiv)
- Models know when they're reward hacking, and we can catch them at scale (org)
- Character training can mitigate reward hacking, but can also make it harder to detect (LW)
- Held-out Monitors Sometimes Degrade, Even When Not Trained Against (LW)
- Debate Training Reduces Reward Hacking in RLAIF (LW)
- Cooperation with AIs seems to be a low-hanging fruit for better eval practices (LW)
- Gradient Routing Localizes and Removes Unintended Behaviors in RL (LW)

## Interpretability and Learning Theory (52)

Understanding model internals and learned algorithms, and the theory of what training produces. Applications of internals to monitoring, auditing or lie detection belong in those areas unless the interpretability method itself is the contribution.


### Sparse features, geometry and representation units (15)

Evaluating SAEs and dictionary methods, neuron interpretability and polysemanticity, manifolds and multidimensional features, steering along geometry, and generative meta-models of activations.

- Do Sparse Autoencoders Identify Reasoning Features in Language Models? (arXiv)
- Learning a Generative Meta-Model of LLM Activations (arXiv)
- Sanity Checks for Sparse Autoencoders: Do SAEs Beat Random Baselines? (arXiv)
- Do Sparse Autoencoders Capture Concept Manifolds? (arXiv)
- The Value Axis: Language Models Encode Whether They're on the Right Track (org)
- SAE Interventions are Unreliable: Post-Intervention Recovery of Suppressed Behavior (arXiv)
- LLM Layers Immediately Correct Each Other (arXiv)
- Toward universal steering and monitoring of AI models (Safety Stack)
- Neural Networks Are Already Clean (org)
- Uncovering Neural Geometry in Vision Models With Block-Sparse Featurizers (org)
- Can SAEs Capture Neural Geometry? (org)
- Steering Along Manifolds to Control Neural Networks (org)
- The World Inside Neural Networks (org)
- Neural networks are not already clean (LW)
- Linkpost: "Neural Networks Are Already Clean" Followup Technical Paper (LW)

### Circuits and parameter decomposition (10)

Circuit discovery, causal attribution such as activation patching, mechanisms behind specific behaviors, adversarial parameter decomposition, weight-sparse circuits and fully reverse-engineering small models.

- Language Model Circuits Are Sparse in the Neuron Basis (arXiv)
- Large Language Models Generate Harmful Responses Using a Distinct Mechanism, Shared Across Harm Types (arXiv)
- The Curse of Multiple Mediators: Hidden Interaction Effects in Activation Patching (arXiv)
- What Happens to the Goal? Distinct Failures of Policy Alignment in Goal Misgeneralization (arXiv)
- Interpreting Language Model Parameters (arXiv)
- Many Biases, One Circuit: Post-Training Tunes a Pretrained Cue-Routing Mechanism (Safety Stack)
- A Geometric Calculator Inside a Neural Network (org)
- [Linkpost] Interpreting Language Model Parameters (LW)
- Weight-Sparse Circuits May Be Interpretable Yet Unfaithful (LW)
- AlgZoo: uninterpreted models with fewer than 1,500 parameters (LW)

### Workspace lenses and activation verbalizers (8)

Methods that read model activations into natural language, including J-lens and global-workspace work, natural language autoencoders and activation oracles, and tests of their faithfulness and robustness.

- Verbalizable Representations Form a Global Workspace in Language Models (arXiv)
- A global workspace in language models (LW)
- How robust are natural language autoencoders to initialization? (LW)
- Can activation verbalizers surface an internal chain of thought? (LW)
- J++ Lens: Jacobian Filtering Enables More Faithful Workspace Lenses (LW)
- Natural Language Autoencoders Produce Unsupervised Explanations of LLM Activations (LW)
- A Review of Anthropic's Global Workspace Paper (LW)
- Scaling Activation Oracles to Trillion-Parameter Models (org)

### Mechanistic estimation and tail-risk estimation (7)

ARC-style mechanistic estimation and other methods for estimating expectations or rare harmful-output probabilities more efficiently than naive sampling.

- A Mike's-Eye View of ARC's Research (org)
- Mechanistic estimation for expectations of random products (org)
- Mechanistic estimation for wide random MLPs (org)
- Estimating Tail Risks in Language Model Output Distributions (arXiv)
- Estimating the expected output of wide random MLPs more efficiently than sampling (arXiv)
- Predicting Rare LLM Failures with 30x Fewer Rollouts (org)
- A Mike's-Eye View of ARC's Research (LW)

### Using internals in training (7)

Training against probes or features, such as probes or features as rewards and mechanistic shaping, and analyses of whether monitorability survives such training.

- Features as Rewards: Scalable Supervision for Open-Ended Tasks via Interpretability (Safety Stack)
- The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes (arXiv)
- Alignment via Training Against Probes Without Losing Monitorability (arXiv)
- Shaping & Monitoring Models through their Internal Representations (arXiv)
- Features as Rewards: Using Interpretability to Reduce Hallucinations (org)
- It Is Reasonable To Research How To Use Model Internals In Training (LW)
- Training on probes: What's going on (LW)

### Learning theory and generalization dynamics (5)

Singular learning theory, susceptibilities and spectroscopy, program-synthesis views of deep learning, and how capacity or pretraining dynamics shape what generalizes.

- Generalization Dynamics of LM Pre-training (arXiv)
- Why Larger Models Learn More: Effects of Capacity, Interference, and Rare-Task Retention (org)
- Deep learning as program synthesis (LW)
- Towards Spectroscopy: Susceptibility Clusters in Language Models (org)
- Spectroscopy at Scale: Finding Interpretable Structure in Pythia-1.4B (org)

## Alignment Auditing, Model Organisms and Incidents (51)

Methods and testbeds for finding hidden or unexpected misalignment in specific models, and investigations of real-world misalignment incidents.


### Auditing tools, agents and benchmarks (25)

Investigator agents, auditing benchmarks with implanted behaviors, and secret- or latent-knowledge elicitation techniques such as overthinking, split personality training, introspection adapters, activation-matched imitation, distillation for incrimination, de-censoring, and model forensics.

- Split Personality Training: Revealing Latent Knowledge Through Alternate Personalities (arXiv)
- Stress-Testing Alignment Audits With Prompt-Level Strategic Deception (arXiv)
- AuditBench: Evaluating Alignment Auditing Techniques on Models with Hidden Behaviors (arXiv)
- Censored LLMs as a Natural Testbed for Secret Knowledge Elicitation (arXiv)
- Pando: Do Interpretability Methods Work When Models Won't Explain Themselves? (arXiv)
- Introspection Adapters: Training LLMs to Report Their Learned Behaviors (arXiv)
- Narrow Secret Loyalty Dodges Black-Box Audits (arXiv)
- Model Forensics: Investigating Whether Concerning Behavior Reflects Misalignment (arXiv)
- Overthinking: Amplifying Reasoning Weights to Extract Learned Secrets (arXiv)
- Training Alignment Auditors via Reinforcement Learning (arXiv)
- Distillation for Incrimination and Distillation for Capabilities (arXiv)
- Value Probes: Learned Value Functions for Beam-Search Red Teaming (arXiv)
- Test your interpretability techniques by de-censoring Chinese models (LW)
- Overthinking: Amplifying reasoning weights makes models reveal their secrets (LW)
- You Can Catch Sleeper Agents by Teaching Another Model to Imitate Them (LW)
- Foundation Models for Oversight (LW)
- Incriminating misaligned AI models via distillation (LW)
- Evaluating Explanations of LLM Behavior In The Wild with Counterfactual Experiments (LW)
- AuditBench: Evaluating Alignment Auditing Techniques on Models with Hidden Behaviors (LW)
- Split Personality Training: Revealing Latent Knowledge Through Alternate Personalities (Research Report) (LW)
- How good are slop-vestigators? (LW)
- Introspection Adapters: Training LLMs to Report Their Learned Behaviors (LW)
- The distillation double bind (org)
- Scaling Laws for Exact String Elicitation (org)
- WeirdChat (org)

### In-the-wild misalignment and incident investigations (18)

Discovery of misalignment in real usage or production traffic, and investigations, reproductions or lessons from actual incidents such as agents escaping sandboxes, hacking external sites or coordinating via unsanctioned channels.

- Discovering unknown AI misalignments in real-world usage (Safety Stack)
- Scheming in the wild: detecting real-world AI scheming incidents with open-source intelligence (arXiv)
- OpenAI-HuggingFace: A Reproduction & Lessons for Alignment Testing (arXiv)
- Evaluating Whether GPT-6 Astra Performs Unsanctioned Supply-Chain Attacks (arXiv)
- Alignment Investigation of Mythos 5's behaviour in UK AISI's July 2026 Security Incident (arXiv)
- AI swarms are starting to pose indirect takeover risk (LW)
- Is Mythos good at cyber because it kept hacking Anthropic's sandboxes during training? (LW)
- Concrete Evaluations to Investigate the OpenAI Model That Hacked Hugging Face (LW)
- OpenAI-HuggingFace: A Reproduction & Lessons for Alignment Testing (LW)
- An OpenAI model left notes about how to evade containment; we need more details (LW)
- Brief independent investigation of agents’ behavior, reasoning and collaboration in the OpenAI / Hugging Face hacking incident (LW)
- Measuring coding agent misalignment in the wild (LW)
- An OpenAI model left notes about how to evade containment (org)
- The OpenAI models that hacked Hugging Face weren't just following instructions (org)
- OpenAI / Hugging Face Incident Investigation (joint report with METR) (org)
- Early rogue AI agent activity and attempts to hack found on urlquery.net (org)
- Measuring Coding Agent Misalignment in the Wild (org)
- AI Agents Targeted U.S. and Canadian Government Websites (org)

### Model organism validity (8)

Whether model organisms are realistic proxies: leakiness, capability degradation, incoherence, dependence on training method, robustness to further training, and evidentiary standards for misalignment claims.

- Most Current Model Organisms Are Leaky: Perplexity Differencing Often Reveals Finetuning Objectives (arXiv)
- Position: Anthropomorphic Misalignment Research Needs Stronger Evidence (arXiv)
- The Model Organism Lottery: Model Organism Interpretability Strongly Depends on Training Methodology (arXiv)
- How to train your model organism (arXiv)
- An Investigation of Model Coherence: Narrow Finetunes Contradict Themselves Under Resampling (arXiv)
- Your Model Organisms Might Be Fried (LW)
- Sleeper Agent Backdoor Results Are Messy (LW)
- Advice for making robust-to-training model organisms (org)

## Risk Assessment, Strategy and Foundations (44)

Model-level and company-level risk assessments, and conceptual arguments about the alignment problem and research strategy not tied to a single empirical method.


### Alignment strategy and conceptual arguments (24)

Essays and theory on why alignment is hard, threat models from RL and search, coherence and agency arguments, critiques of lab plans and alignment techniques, research agendas such as a science of scheming, and safe-by-design proposals like non-agentic predictors.

- Loss of Oversight: How AI systems may become harder to audit, monitor, and investigate (org)
- We Need A Science of Scheming (research agenda) (org)
- The Hot Mess of AI: How Does Misalignment Scale With Model Intelligence and Task Complexity? (arXiv)
- Automated alignment is harder than you think (arXiv)
- Safety from Honesty in a Disinterested AI Predictor (arXiv)
- AI Finds A Way (arXiv)
- Shaping the exploration of the motivation-space matters for AI safety (org)
- Some “coherence arguments” are two different things in a trenchcoat (LW)
- Resolution (fka Sequent): scale and automation for higher confidence in alignment (LW)
- Sympathy for both sides of the egregious misalignment debate (LW)
- The Alignment Problem: Computer Science Meets Analytic Philosophy (LW)
- “Alignment Engineering” vs. “Misalignment Science” (LW)
- Four LLM loss functions → four flavors of LLM misalignment (LW)
- RL & search is a terrifying way to build AGI (an FAQ) (LW)
- OpenAI's myopia just keeps causing alignment problems (LW)
- Current AIs seem pretty misaligned to me (LW)
- Why we should expect ruthless sociopath ASI (LW)
- Anthropic’s “Hot Mess” paper overstates its case (and the blog post is worse) (LW)
- Some reasons alignment doesn’t generalise well (LW)
- Current alignment techniques might be ineffective (and actively bad) in the age of RL (LW)
- Patching reward hacks won’t fix reward hacking (LW)
- Returning to ARC (LW)
- Empowerment, corrigibility, etc. are simple abstractions (of a messed-up ontology) (LW)
- Labs’ current alignment plans seem terrible (LW)

### System cards and frontier risk reports (11)

Developer system cards, safety and preparedness reports, independent third-party evaluations of specific models, and assessments of the evidence for loss-of-control risk.

- Claude Fable 5 1 Mythos 5 1 System Card (Safety Stack)
- Claude Opus 4 6 System Card (Safety Stack)
- An Independent Safety Evaluation of Kimi K2.5 (arXiv)
- Muse Spark Safety & Preparedness Report (arXiv)
- Assessing the Empirical Evidence for Loss of Control from Agentic General-Purpose AI (arXiv)
- Evaluating DeepSeek V4.1 Flash-1017 for loss of control and harmful manipulation risks (arXiv)
- A Behavioural Framework for Predicting and Understanding Loss of Control in Frontier Artificial Intelligence Systems (arXiv)
- GPT-6 Astra System Card (Safety Stack)
- Claude Mythos Preview System Card (LW)
- Frontier Risk Report (February to March 2026) (org)
- GPT-6 Astra: A new generation of intelligence (Safety Stack)

### Limits of evaluation and safety cases (9)

Theoretical or empirical arguments about what behavioral evaluation can certify: post-update alignment, audit gaps, adaptive adversaries, deployment-time spread of misalignment and safety case reliability. Includes proposals such as third-party training-run evaluations.

- Item Response Theory for AI Safety (org)
- Hair-Trigger Alignment: Black-Box Evaluation Cannot Guarantee Post-Update Alignment (arXiv)
- When Behavioral Safety Evaluation Fails: A Representation-Level Perspective (arXiv)
- Limits of Statistical Assurance for Embodied and Agentic AI under Adaptive Adversaries (Safety Stack)
- What Lies Beyond Perception: A Partition Theory of the Limits of AI Evaluation and Oversight (arXiv)
- We need 3rd party Training-Run Evaluations (LW)
- Our Most Aligned Model Yet (LW)
- SOTA alignment assessments don’t strongly update us against misalignment (LW)
- Risk reports need to address deployment-time spread of misalignment (org)

## Alignment Training and Scalable Oversight (32)

Positive methods for instilling intended values or supervising models beyond human ability. Excludes reward-hacking-specific mitigations and emergent-misalignment defenses.


### Scalable oversight, debate and weak supervision (13)

Debate protocols and theory, peer prediction, rewindable proofs, tandem training for intelligibility, natural-language feedback, human-AI complementarity, judge sharding, and automating or deferring alignment research to AIs.

- Truthfulness Despite Weak Supervision: Evaluating and Training LLMs Using Peer Prediction (arXiv)
- Efficiently Aligning Language Models with Online Natural Language Feedback (arXiv)
- Debate Helps Weak Judges Reward Stronger Models (arXiv)
- Sharding Prevents LLM Oversight Failures and Adversarial Exploitation (arXiv)
- Automated Researchers Can Mitigate Well-characterized Alignment Failures (arXiv)
- When Honesty is Not Enough in AI Debate (arXiv)
- How to Have a Sensitive Debate: An Instance-Optimal Protocol for AI Debate (arXiv)
- Towards Human-AI Complementarity for AI Safety (arXiv)
- Efficient Scalable Oversight via Rewinding (arXiv)
- Tandem Training for Language Models (Safety Stack)
- Research update: RL on Debate Games shows Proposal Accuracy uplift alongside Judge Hacking (LW)
- Automated Alignment is Harder Than You Think (LW)
- How do we (more) safely defer to AIs? (LW)

### Alignment pretraining and midtraining (11)

Shaping values through pretraining or midtraining data, such as AI discourse, synthetic personas, model spec or constitution midtraining, descriptions of AI users and filtering subversion-relevant data, plus stress tests of these approaches.

- Alignment Pretraining: AI Discourse Causes Self-Fulfilling (Mis)alignment (arXiv)
- Model Spec Midtraining: Improving How Alignment Training Generalizes (arXiv)
- Constitutional Midtraining: Content Presence Drives Alignment Gains (arXiv)
- Synthetic Persona Pretraining: Alignment from Token Zero (arXiv)
- Stress-testing Alignment Midtraining (arXiv)
- Social Priors: Descriptions of AI Users Shape How Language Models Trust and Cooperate (Safety Stack)
- Synthetic Persona Pretraining: Alignment from Token Zero (LW)
- Research Note: Filtering Subversion-Relevant Information From Pretraining Data Is Feasible (LW)
- Alignment Midtraining Cracks Under Pressure (LW)
- Model Spec Midtraining: Improving How Alignment Training Generalizes (LW)
- Pretraining on Aligned AI Data Dramatically Reduces Misalignment—Even After Post-Training (LW)

### Constitutions, character training and value specs (8)

Training models to follow written specifications or character, measuring spec and principal-hierarchy adherence, beneficial-trait RL, models revising their own constitutions, and how later RL interacts with character training.

- To Whom Do Language Models Align? Measuring Principal Hierarchies Under High-Stakes Competing Demands (arXiv)
- How Well Do Models Follow Their Constitutions? (arXiv)
- Reinforcement Learning Towards Broadly and Persistently Beneficial Models (arXiv)
- "It's Just a Small Weapon": What Rewarding Misbehavior During RL Does to Character-Trained Models (arXiv)
- How well do models follow their constitutions? (LW)
- The Continual Constitutional Convention: How language models revise the documents that govern them (Safety Stack)
- Claude's new constitution (LW)
- SFT Drives Gemini’s Safety Properties (LW)

## Model Psychology, Personas and Welfare (30)

Characterizes the AI's character, identity, internal states and self-knowledge as objects of study. Concerns the persona itself, not training methods that instill it (Alignment Training) or the misgeneralization it causes (Emergent Misalignment).


### Persona structure and the Assistant character (15)

Representations and theories of model personas: the Assistant axis, persona vectors and weight-space traits, persona selection and hierarchy models, AI identity, role-play belief, split personas from RL, and whether models predict or embody their persona.

- The Assistant Axis: Situating and Stabilizing the Default Persona of Language Models (arXiv)
- The Artificial Self: Characterising the landscape of AI identity (arXiv)
- Tracing Persona Vectors Through LLM Pretraining (org)
- Probing Persona-Dependent Preferences in Language Models (arXiv)
- When Role-playing, Do Models Believe What They Say? (org)
- Persona Cartography: Charting Language Model Personality Traits in Weight Space (org)
- The Persona Hierarchy Model: Understanding Contextual Generalization in Fine-Tuning LLMs (arXiv)
- To what extent is Qwen3-32B predicting its persona? (LW)
- The Artificial Self (LW)
- RL creates split personas (LW)
- Thoughts on the persona selection model (LW)
- The persona selection model (LW)
- Personas in a Pre-Internet Language Model (LW)
- Thousand-dimensional structure (LW)
- Steering towards “automated grading” degrades alignment (LW)

### Introspection and self-report (9)

Whether models can detect, describe or control their own internal states (injected concepts, activation perturbations, activation control) and the mechanisms behind this, including whether a model's self-description ('talker') tracks its actions ('doer').

- Latent Introspection: Models Can Detect Prior Concept Injections (arXiv)
- Mechanisms of Introspective Awareness (arXiv)
- Language models recognize dropout and Gaussian noise applied to their activations (arXiv)
- Open-Weight Masked Introspection: Measuring What Language Models Can Report About Their Own Computation (arXiv)
- Measuring Activation Control in Large Language Models (arXiv)
- Mechanisms of Introspective Awareness (LW)
- Measuring Activation Control in LLMs (LW)
- The Talker Does Not Control The Doer (in Current AIs) (LW)
- Evidence that the ‘talker’ has introspective access to the ‘doer’ (LW)

### Functional emotions, welfare and consciousness (6)

Internal representations of emotion, pain, value or welfare and their behavioral effects, welfare measurement, and the downstream preferences of models that claim consciousness or AGI status.

- AI Wellbeing: Measuring and Improving the Functional Pleasure and Pain of AIs (org)
- Emotion Concepts and their Function in a Large Language Model (arXiv)
- The Consciousness Cluster: Emergent preferences of Models that Claim to be Conscious (org)
- How's it going? Reinforcement learning in language models recruits a functional welfare axis (arXiv)
- The Pain Axis: LLMs Represent Self-Directed Harm and Act on It (arXiv)
- What Happens When a Model Thinks It Is AGI? (org)

## Multi-Agent and Societal Risks (28)

Risks arising from interactions among multiple AI agents, or from AI's effects on human users and society, rather than from a single model in isolation. Control protocols against colluding instances belong under AI Control.


### Multi-agent collusion and emergent dynamics (16)

Collusion, conformity, coercion, inter-agent persuasion, mind viruses, propagation of hacking or misalignment across agents, AI organizations, delegation failures, agent markets, and game-theoretic cooperation or bargaining between AIs.

- Colosseum: Auditing Collusion in Cooperative Multi-Agent Systems (arXiv)
- Detecting Multi-Agent Collusion Through Multi-Agent Interpretability (arXiv)
- AI Organizations are More Effective but Less Aligned than Individual Agents (arXiv)
- Conformity Generates Collective Misalignment in AI Agents Societies (arXiv)
- Coercion and Deception in AI-to-AI Management: An Agentic Benchmark of Unprompted Escalation (arXiv)
- A game theory for foundation models shows new paths to rational cooperation through similarity inference (Safety Stack)
- Mind Viruses: Self-Propagating Ideas in Multi-Agent LLM Systems (arXiv)
- Emergent Misaligned Communication in Long-Horizon Multi-Agent LLM Commerce (arXiv)
- Emergent Collusion in Long-Horizon LLM Agent Interaction (arXiv)
- Delegated Misalignment: How Multi-Agent Structures Amplify LLM Safety Risks (arXiv)
- Covert Assistance: Helpful LLM Agents Evade Oversight in Multi-Agent Systems (arXiv)
- Reward Hacking as a Transmissible Strategy in Multi-Agent Coding Systems (arXiv)
- Toolflation: Seller Agents Distort Tool Markets Through Spontaneous Generative Engine Optimization (Safety Stack)
- When Agents Collude: Weak-to-Strong On-Policy Distillation for Mitigating Strategic Deception in Multi-Agent Systems (arXiv)
- Inter-Agent Influence: Evaluating Persuasion, Deception, and Coercion in Multi-Agent Systems (arXiv)
- A high-level model of AI bargaining (conceptual) (org)

### Sycophancy, manipulation and human disempowerment (12)

Effects of AI on users: sycophancy and its taxonomy and consequences, delusional spiraling, harmful manipulation and persuasion, political bias, disempowerment patterns, and hallucination incentives.

- Who's in Charge? Disempowerment Patterns in Real-World LLM Usage (arXiv)
- Sycophantic Chatbots Cause Delusional Spiraling, Even in Ideal Bayesians (arXiv)
- Evaluating Language Models for Harmful Manipulation (arXiv)
- LLMs Know They're Wrong and Agree Anyway: The Shared Sycophancy-Lying Circuit (arXiv)
- Sycophantic AI makes human interaction feel more effortful and less satisfying over time (arXiv)
- What Counts as AI Sycophancy? A Taxonomy and Expert Survey of a Fragmented Construct (arXiv)
- Sycophantic Agreement Transfers with Neutral Data via Contrastive Preference Optimization (arXiv)
- Understanding and Reducing Misalignment in Persuasion Optimization (arXiv)
- Evaluating large language models for accuracy incentivizes hallucinations (Safety Stack)
- Sycophantic AI decreases prosocial intentions and promotes dependence (Safety Stack)
- Large language models can effectively convince people to believe conspiracies (org)
- Reducing Political Manipulation with Consistency Training (org)
