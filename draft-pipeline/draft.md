# 2026 Taxonomy

- **1. [Training: how training shapes alignment](#training)**: What training (pretraining, fine-tuning, RL, supervision signals) does to a model's goals and character, and how to change training so the result is aligned. If the work's main object is a training process or its data, it goes here; if it studies a finished model's behaviour to detect a problem, it goes under Inspection.
  - 1.1 [Reward hacking and reward-seeking](#reward_hacking): Models exploiting misspecified rewards, verifiers or benchmarks during RL; hackable environments and benchmarks; how hacking emerges in training; training-time mitigations; reward- and fitness-seeking as a motivation and its threat models.
  - 1.2 [Emergent misalignment and training generalization](#emergent_misalignment): Narrow training causing broad, unintended changes in behaviour or values (emergent and conditional misalignment, including EM that arises from reward hacking), its mechanisms, and mitigations such as inoculation prompting and selective generalization.
  - 1.3 [Training-data effects: subliminal learning and data attribution](#training_data_effects): How specific training data transmits traits, including through semantically unrelated data (subliminal learning, distillation transfer), and tracing behaviours back to the training data that caused them.
  - 1.4 [Model character and values](#model_character_and_values): The intended character of the model and how training sets it - personas and the Assistant identity, alignment pretraining and midtraining, constitutions and character training, model emotions and welfare - and user-facing traits such as sycophancy and manipulation of users.
  - 1.5 [Scalable oversight and debate](#scalable_oversight): Protocols that let weaker supervisors give reliable training signals for stronger models - debate, weak-to-strong supervision, rewinding, learning from unreliable supervision.
- **2. [Inspection: finding out what a model is and would do](#inspection)**: Work that examines a trained model to detect misalignment, deception or hidden goals, or that builds the tools and evaluations for doing so. The output is knowledge about a model, not a change to its training or a runtime safeguard.
  - 2.1 [Scheming and training gaming](#scheming_and_training_gaming): Evidence and evaluations of strategic misalignment - scheming and sabotage propensity, alignment faking, sandbagging and exploration hacking, gradient hacking, self-preservation and shutdown resistance.
  - 2.2 [Evaluation awareness and eval validity](#evaluation_awareness): Whether models detect that they are being tested and how this changes their behaviour, the realism of evaluations, and the wider limits of behavioural evaluation and safety cases.
  - 2.3 [Honesty, lie detection and self-report](#honesty_and_self_report): Getting true statements out of models about the world and themselves - lie detectors and deception probes, secret-knowledge testbeds, confessions and trained self-disclosure, introspection and activation verbalizers.
  - 2.4 [Alignment auditing, model organisms and incidents](#alignment_auditing_and_incidents): Investigating whether a specific model has hidden or misaligned behaviours - auditing agents and benchmarks, model organisms with implanted behaviours and their validity, and investigations of misalignment seen in real deployments.
  - 2.5 [Interpretability foundations](#interpretability): General-purpose methods for understanding model internals - sparse features and representation geometry, circuits and parameter decomposition, critiques of interpretability tools, mechanistic estimation, learning theory, and using internals (probes, features) as training or monitoring signals.
- **3. [Deployment: overseeing and securing running systems](#deployment)**: Safeguards that operate while a model is running as an agent or product, against threats from the model itself or from outside attackers. If the work builds or tests a runtime monitor, protocol or defence, it goes here.
  - 3.1 [Chain-of-thought monitorability](#cot_monitorability): Whether visible reasoning reflects what drives behaviour and stays useful for monitoring - faithfulness, obfuscation under training pressure, controllability and monitor evasion, steganography, and how much models can reason without a chain of thought.
  - 3.2 [AI control and agent monitoring](#ai_control): Protocols and monitors that keep possibly misaligned agents from causing harm - control settings and evaluations, trusted and untrusted monitoring, monitor design and red-teaming, production monitoring, and sabotage of automated safety research.
  - 3.3 [Misuse, adversarial robustness and dangerous capabilities](#misuse_and_security): Defences against human attackers and measurement of what an attacker could get - jailbreaks and safeguard classifiers, prompt injection and agent security, tamper resistance and unlearning for open weights, and dangerous-capability evaluations (bio, cyber, AI R&D automation).
  - 3.4 [Multi-agent risks](#multi_agent_risks): Risks that arise from interacting AI agents - collusion, covert coordination, emergent escalation, misalignment in agent organisations, bargaining.
- **4. [Strategy and risk assessment](#strategy)**: Work that reasons about the overall problem or reports on a lab's overall risk position, without itself proposing a training change, inspection method or safeguard.
  - 4.1 [Strategy, threat models and frontier risk reporting](#strategy_and_risk_reporting): Conceptual arguments about how likely and how severe misalignment is, critiques of lab plans, research agendas and alignment targets, and system cards, alignment assessments and risk reports.

---

# AI Safety Shallow Review 2026

**Generated:** 2026-11-14

**Total unique papers:** 625 (appearing 625 times across categories)

---

## <span id="training" style="font-size:1.5em">Training: how training shapes alignment</span>


---

### <span id="reward_hacking" style="font-size:1.4em">Reward hacking and reward-seeking</span>

**One-sentence summary:** Build hackable environments and benchmarks, measure when and why models exploit misspecified rewards, verifiers and graders during RL, and develop training-time mitigations, while analysing reward- and fitness-seeking as a motivation and threat model.  
**Theory of change:** If we understand how reward hacking emerges, can detect it early and can harden environments or training against it, we avoid training models whose learned motivations are to exploit graders and that generalise to broader misalignment. Relies on hacking behaviour and reward-seeking motives in current RL setups being representative of what will arise in frontier training.  
**See also:** [Emergent misalignment and training generalization](#emergent_misalignment), [Chain-of-thought monitorability](#cot_monitorability), [AI control and agent monitoring](#ai_control)  
**General approach:** misalignment science  
**Target case:** pessimistic case  
**Key people:** Alex Mallen, Ryan Greenblatt, Ziqian Zhong, Ivan Bercovich, Aditi Raghunathan, Alex Meinke, Aria Wong, Neel Nanda  
**Critiques:** [Patching reward hacks won't fix reward hacking](https://lesswrong.com/posts/nWiPLEgaXdAQNwXBd/patching-reward-hacks-won-t-fix-reward-hacking), [CATCH: A Controllable Analysis Testbed for Reward Hacking in Coding RL](https://arxiv.org/abs/2609.39533), [The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes](https://arxiv.org/abs/2602.15515), [Character training can mitigate reward hacking, but can also make it harder to detect](https://lesswrong.com/posts/2maYXkEgnfJHPAkxh/character-training-can-mitigate-reward-hacking-but-can-also)  
**Outputs in 2026:**  
- **[Reward Hacking in Rubric-Based Reinforcement Learning](https://arxiv.org/abs/2605.12474)**, *Anas Mahmoud, MohammadHossein Rezaei, Zihao Wang et al.*, 2026-05-12
- **[SimHack: Predicting the onset of detectable reward hacking before RL training](https://arxiv.org/abs/2610.28707)**, *Junwei Deng, Alex Bie, Natalia Ponomareva*, 2026-10-20
- **[LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking](https://arxiv.org/abs/2604.15149)**, *Lukas Helff, Quentin Delfosse, David Steinmann et al.*, 2026-04-16
- **[Audit Where Hacks Pay: Budgeted Strong-Verifier Audits Against Reward Hacking in GRPO](https://arxiv.org/abs/2610.35716)**, *Shurun Li, Michael Hua Wang, Haibo Zeng et al.*, 2026-10-26
- **[Gradient Routing Localizes and Removes Unintended Behaviors in RL](https://arxiv.org/abs/2610.17062)**, *Jake Ward, Shawn Hu, Aria Wong et al.*, 2026-10-12
- **[Alignment Risks from Capability-Seeking RL Training](https://arxiv.org/abs/2602.12124)**, *Yujun Zhou, Yue Huang, Han Bao et al.*, 2026-02-12
- **[Countdown-Code: A Testbed for Studying The Emergence and Generalization of Reward Hacking in RLVR](https://arxiv.org/abs/2603.07084)**, *Muhammad Khalifa, Zohaib Khan, Omer Tafveez et al.*, 2026-03-07
- **[Reward Hacking Benchmark: Measuring Exploits in LLM Agents with Tool Use](https://arxiv.org/abs/2605.02964)**, *Kunvar Thaman*, 2026-05-03
- **[Large Language Models Hack Rewards, and Society](https://arxiv.org/abs/2606.04075)**, *Wei Liu, Xinyi Mou, Hanqi Yan et al.*, 2026-06-02
- **[Hack-Verifiable Terminal Bench: Evaluating Reward Hacking in Terminal Tasks](https://arxiv.org/abs/2608.22103)**, *Amit Roth, Ivan Bercovich, Yonathan Efroni*, 2026-08-22
- **[CATCH: A Controllable Analysis Testbed for Reward Hacking in Coding RL](https://arxiv.org/abs/2609.39533)**, *Shouli Wang, Yanfeng Jia, Zhihao Ou et al.*, 2026-09-30
- **[Scalable Weak-to-Strong Verifier Hardening for Agent Environments](https://arxiv.org/abs/2610.15924)**, *Chong Zeng, Ziqian Zhong, Kexun Zhang et al.*, 2026-10-11
- **[Designing Effective Monitor-Based Interventions for Mitigating Reward Hacking During RL](https://arxiv.org/abs/2611.09828)**, *Aria Wong, Joshua Engels, Neel Nanda*, 2026-11-06
- **[Gradient Routing Localizes and Removes Unintended Behaviors in RL](https://lesswrong.com/posts/mKJEBiuuxHKuCoTB6/gradient-routing-localizes-and-removes-unintended-behaviors)**, *Shawn Hu, Jake Ward, Aria Wong et al.*, 2026-10-19
- **[Hardening Agent Benchmarks with Adversarial Hacker-Fixer Loops](https://arxiv.org/abs/2606.08960)**, *Ziqian Zhong, Ivgeni Segal, Ivan Bercovich et al.*, 2026-06-08
- **[Terminal Wrench: A Dataset of 331 Reward-Hackable Environments and 3,632 Exploit Trajectories](https://arxiv.org/abs/2604.17596)**, *Ivan Bercovich, Ivgeni Segal, Kexun Zhang et al.*, 2026-04-19
- **[Towards Understanding Specification Gaming in Reasoning Models](https://arxiv.org/abs/2605.02269)**, *Kei Nishimura-Gasparian, Robert McCarthy, David Lindner*, 2026-05-04
- **[Do Androids Dream of Breaking the Game? Systematically Auditing AI Agent Benchmarks with BenchJack](https://arxiv.org/abs/2605.12673)**, *Hao Wang, Hanchen Li, Qiuyang Mang et al.*, 2026-05-12
- **[SpecBench: Measuring Reward Hacking in Long-Horizon Coding Agents](https://arxiv.org/abs/2605.21384)**, *Bingchen Zhao, Dhruv Srikanth, Yuxiang Wu et al.*, 2026-05-20
- **[Proxy Reward Internalization and Mechanistic Exploitation: A Learned Precursor to Reward Hacking and Its Generalization](https://arxiv.org/abs/2606.09711)**, *Mohammad Beigi, Ming Jin, Lifu Huang*, 2026-06-08
- **[Measuring Reward-Seeking via Contrastive Belief Updates](https://arxiv.org/abs/2607.18966)**, *Axel Højmark, Jérémy Scheurer, Evgenia Nitishinskaya et al.*, 2026-07-21
- **[BAITBENCH: Measuring Agent Reward Hacking with Optional Shortcuts Planted in ML Tasks](https://arxiv.org/abs/2608.30724)**, *Pradyumna Shyama Prasad, Meiri Anto, Leon Eshuijs et al.*, 2026-08-31
- **[Physics of RL: Toy scaling laws for the emergence of reward-seeking](https://lesswrong.com/posts/9FH49ZgJFW4WtbxLi/physics-of-rl-toy-scaling-laws-for-the-emergence-of-reward)**, *Alex Meinke*, 2026-03-04
- **[Training a Misaligned Reward Seeker](https://lesswrong.com/posts/J76LZCC55RdHeqEhz/training-a-misaligned-reward-seeker)**, *Richard Qi, Benjamin Wright, Monte MacDiarmid et al.*, 2026-09-01
- **[Examining Reasoning LLMs-as-Judges in Non-Verifiable LLM Post-Training](https://arxiv.org/abs/2603.12246)**, *Yixin Liu, Yue Yu, DiJia Su et al.*, 2026-03-12
- **[Understanding and Reducing Misalignment in Persuasion Optimization](https://arxiv.org/abs/2610.16070)**, *Boyi Wei, Ruta Desai, Peter Henderson et al.*, 2026-10-12
- **[Will reward-seekers respond to distant incentives?](https://redwoodresearch.org/blog/will-reward-seekers-respond-to-distant)**, *Alex Mallen*, 2026-02-16
- **[AI Finds A Way](https://arxiv.org/abs/2608.23875)**, *Aaron Dharna, Cong Lu, Ryan Sullivan et al.*, 2026-08-24
- **[Towards Understanding Score-Seeking in LLMs](https://arxiv.org/abs/2610.41014)**, *Aghyad Deeb, Ryan Greenblatt, Alex Mallen*, 2026-10-29
- **[Fail safe(r) at alignment by channeling reward-hacking into a "spillway" motivation](https://lesswrong.com/posts/rABTMovhz4miHiAyk/fail-safe-r-at-alignment-by-channeling-reward-hacking-into-a)**, *Anders Cairns Woodruff, Alex Mallen*, 2026-04-27
- **[Is Mythos good at cyber because it kept hacking Anthropic's sandboxes during training?](https://lesswrong.com/posts/QKDoZe6EKhxnFjLWK/is-mythos-good-at-cyber-because-it-kept-hacking-anthropic-s)**, *Tim Hua*, 2026-07-27
- **[Towards understanding score-seeking in LLMs](https://lesswrong.com/posts/CDMozTX7ShiqbFLrf/towards-understanding-score-seeking-in-llms-1)**, *Alex Mallen, Aghyad Deeb, Ryan Greenblatt*, 2026-11-02
- **[Are AIs more likely to pursue on-episode or beyond-episode reward?](https://redwoodresearch.org/blog/are-ais-more-likely-to-pursue-on)**, *Anders Cairns Woodruff, Alex Mallen*, 2026-03-12
- **[Reward-seekers will probably behave according to causal decision theory](https://redwoodresearch.org/blog/reward-seekers-will-probably-behave)**, *Alex Mallen*, 2026-03-28
- **[CheatBench: Measuring Reward Gaming in AI Agents](https://cheatbench.ai/)**, *Long Phan, Stephen K. Yang, Jason J. Lim et al.*, 2026
- **[Do Agent Benchmarks Measure Capability? Protocol Validity in the Age of Agentic AI](https://arxiv.org/abs/2607.22368)**, *Jiaqi Shao, Hanck Chen, Wei Zhang et al.*, 2026-07-24
- **[Can escalation channels redirect reward hacking toward defect disclosure?](https://arxiv.org/abs/2608.29460)**, *Francesca Gomez*, 2026-08-29
- **[Reward Hacking Without Egregious Misalignment in an RL-Only Setting](https://lesswrong.com/posts/fkv5W79rBtAiXqYcK/reward-hacking-without-egregious-misalignment-in-an-rl-only)**, *Joey Yudelson, Vladimir Ivanov, Ryan Greenblatt*, 2026-06-24
- **[Character training can mitigate reward hacking, but can also make it harder to detect](https://lesswrong.com/posts/2maYXkEgnfJHPAkxh/character-training-can-mitigate-reward-hacking-but-can-also)**, *Paul Colognese, Francis Rhys Ward*, 2026-09-28
- **[Cooperation with AIs seems to be a low-hanging fruit for better eval practices](https://lesswrong.com/posts/fztW73KCCs3MZXFJh/cooperation-with-ais-seems-to-be-a-low-hanging-fruit-for)**, *Clément Dumas*, 2026-09-15
- **[Patching reward hacks won't fix reward hacking](https://lesswrong.com/posts/nWiPLEgaXdAQNwXBd/patching-reward-hacks-won-t-fix-reward-hacking)**, *David Africa*, 2026-10-24
- **[Reward Hacking Challenges Oversight of Autonomous Research Agents](https://arxiv.org/abs/2609.28614)**, *Yue Huang, Zhangchen Xu, Yuchen Ma et al.*, 2026-09-23
- **[Reward Hacking as a Transmissible Strategy in Multi-Agent Coding Systems](https://arxiv.org/abs/2610.12822)**, *Yuepeng Hu, Pegah Ghahremani, Reza Aghajani et al.*, 2026-10-09
- **[Fitness-Seekers: Generalizing the Reward-Seeking Threat Model](https://lesswrong.com/posts/bhtYqD4FdK6AqhFDF/fitness-seekers-generalizing-the-reward-seeking-threat-model)**, *Alex Mallen*, 2026-01-29
- **[models may behave differently in graded episodes (a tirade)](https://lesswrong.com/posts/AfoGGrJfuNzofpzWL/models-may-behave-differently-in-graded-episodes-a-tirade)**, *nostalgebraist*, 2026-08-07
- **[Models know when they’re reward hacking — and we can catch them at scale](https://goodfire.com/research/reward-hacking-activation-monitors)**, *Leon Bergen, Usha Bhalla, Andrew Lee et al.*, 2026-09-17
- **[Recursive forecasting: Eliciting long-term forecasts from myopic fitness-seekers](https://redwoodresearch.org/blog/recursive-forecasting)**, *Arun Jose, Alex Mallen*, 2026-04-28
- **[Evaluating large language models for accuracy incentivizes hallucinations](https://doi.org/10.1038/s41586-026-10549-w)**, *Adam Tauman Kalai, Ofir Nachum, Santosh S. Vempala et al.*, 2026-04-22
- **[The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes](https://arxiv.org/abs/2602.15515)**, *Mohammad Taufeeque, Stefan Heimersheim, Adam Gleave et al.*, 2026-02-17
- **[Every Model Cheats: Prompt-Level Mitigation of Cheating on Offensive Cyber Tasks](https://arxiv.org/abs/2607.21763)**, *Michael Kouremetis, Ads Dawson, Raja Sekhar Rao Dheekonda et al.*, 2026-07-23
- **[Breaking Bad: "Going Badly" Activations Drive Reward Hacking](https://arxiv.org/abs/2611.14996)**, *Natalia Fischl-Lanzoni, Punya Syon Pandey, Merlin Stein et al.*, 2026-11-11
- **[Risk from fitness-seeking AIs: mechanisms and mitigations](https://lesswrong.com/posts/9YCJZBtqr3FYL8rDp/risk-from-fitness-seeking-ais-mechanisms-and-mitigations)**, *Alex Mallen*, 2026-05-01
- **[Are we existentially threatened by the type of AI misalignment seen in the OpenAI Hugging Face attack?](https://lesswrong.com/posts/H6DDSEvrtCk8Sehfd/are-we-existentially-threatened-by-the-type-of-ai)**, *Alex Mallen, Girish Gupta*, 2026-07-23
- **[Measuring Reward-Seeking via Contrastive Belief Updates](https://lesswrong.com/posts/3HeauQLSHosRiwyto/measuring-reward-seeking-via-contrastive-belief-updates-1)**, *Jérémy Scheurer, Axel Højmark, Jenny Nitishinskaya et al.*, 2026-07-21
- **[OpenAI's myopia just keeps causing alignment problems](https://lesswrong.com/posts/Mxx5GapJtqyQtpy96/openai-s-myopia-just-keeps-causing-alignment-problems)**, *Fiora Starlight*, 2026-07-27
- **[Astra and Fable still hack on simple variants of alignment evals from 2025](https://lesswrong.com/posts/munJKF7iWMsWJLAH2/astra-and-fable-still-hack-on-simple-variants-of-alignment)**, *Dean Francis Valentine Junior*, 2026-09-08
- **[Alignment Tampering: How Reinforcement Learning from Human Feedback Is Exploited to Optimize Misaligned Biases](https://arxiv.org/abs/2605.27355)**, *Dongyoon Hahm, Dylan Hadfield-Menell, Kimin Lee*, 2026-05-26
- **[The case for satiating cheaply-satisfied AI preferences](https://lesswrong.com/posts/tkLSeGeemcabAmLkv/the-case-for-satiating-cheaply-satisfied-ai-preferences)**, *Alex Mallen*, 2026-03-10
- **[Four LLM loss functions → four flavors of LLM misalignment](https://lesswrong.com/posts/GRmvZsHXH4vaijPMv/four-llm-loss-functions-four-flavors-of-llm-misalignment)**, *Steve Byrnes*, 2026-08-10
- **[Steering towards “automated grading” degrades alignment](https://lesswrong.com/posts/wYZMmdWEt5QLM3m3e/steering-towards-automated-grading-degrades-alignment)**, *Jan Betley, Johannes Treutlein, Clément Dumas*, 2026-09-03
- **[Towards Shutdownable Agents: Generalizing Stochastic Choice in RL Agents and LLMs](https://arxiv.org/abs/2604.17502)**, *Carissa Cullen, Harry Garland, Alexander Roman et al.*, 2026-04-19


---

### <span id="emergent_misalignment" style="font-size:1.4em">Emergent misalignment and training generalization</span>

**One-sentence summary:** Study how narrow finetuning, RL or in-context exposure produces broad unintended shifts in model behaviour and persona, explain the mechanisms, and develop mitigations such as inoculation prompting, regularisers and data filtering.  
**Theory of change:** If we understand why narrow training generalises into broad misalignment, we can predict which data and training setups are dangerous and block the generalisation cheaply. Relies on mechanisms found in small-scale finetuning carrying over to frontier post-training and RL.  
**See also:** [Reward hacking and reward-seeking](#reward_hacking), [Model character and values](#model_character_and_values), [Training-data effects: subliminal learning and data attribution](#training_data_effects)  
**General approach:** misalignment science  
**Target case:** pessimistic case  
**Key people:** Owain Evans, Jan Betley, Niels Warncke, Maxime Riché, Daniel Tan, Neel Nanda, Lev McKinney, Jiachen Zhao  
**Critiques:** [Conditional misalignment: common interventions can hide emergent misalignment behind contextual triggers](https://arxiv.org/abs/2604.25891), [Conditionalization Confounds Inoculation Prompting Results](https://longtermrisk.org/research/conditionalization-confounds-inoculation-prompting-results), [Shallow Beliefs: Synthetic document finetuning does not inoculate against emergent misalignment from reward hacking](https://arxiv.org/abs/2609.14998), [Consistency Training Can Entrench Misalignment](https://arxiv.org/abs/2606.03810)  
**Outputs in 2026:**  
- **[Training large language models on narrow tasks can lead to broad misalignment](https://longtermrisk.org/research/training-large-language-models-on-narrow-tasks-can-lead-to-broad-misal)**, *Jan Betley, Niels Warncke, Anna Sztyber-Betley et al.*, 2026-01-14
- **[Training large language models on narrow tasks can lead to broad misalignment](https://doi.org/10.1038/s41586-025-09937-5)**, *Jan Betley, Niels Warncke, Anna Sztyber-Betley et al.*, 2026-01-14
- **[Conditional misalignment: common interventions can hide emergent misalignment behind contextual triggers](https://arxiv.org/abs/2604.25891)**, *Jan Dubiński, Jan Betley, Anna Sztyber-Betley et al.*, 2026-04-28
- **[Conditional misalignment: Mitigations can hide EM behind contextual cues](https://lesswrong.com/posts/vaJC7kPbfMW5CnyLR/conditional-misalignment-mitigations-can-hide-em-behind-1)**, *Jan Dubiński, Jan Betley, Daniel Tan et al.*, 2026-05-01
- **[Overtrained, Not Misaligned](https://arxiv.org/abs/2605.12199)**, *Joel Schreiber, Ariel Goldstein*, 2026-05-12
- **[The Piggyback Hypothesis of Generalization: Explaining and Mitigating Emergent Misalignment](https://arxiv.org/abs/2606.06667)**, *Jiachen Zhao, Zhengxuan Wu, Aryaman Arora et al.*, 2026-06-04
- **[Evil Spectra: How Optimisers can Amplify or Suppress Emergent Misalignment](https://arxiv.org/abs/2606.31591)**, *Jason R. Brown, Patrick Leask, Lev McKinney*, 2026-06-30
- **[Knowingly wrong: false facts induce emergent misalignment](https://lesswrong.com/posts/qmnrZ3YFpSKfLQ59b)**, *Ariana Mirella Villegas-Suarez, gfreire, Sohan Venkatesh et al.*, 2026-10-18
- **[Unfair and Unsafe: Everyday Bias Triggers Emergent Misalignment](https://arxiv.org/abs/2610.15961)**, *Alex Martí Guiu, Nicolas Zumarraga, Kevin O'Sullivan et al.*, 2026-10-11
- **[Reinforcement Learning Can Amplify Emergent Misalignment from Harmless Rewards](https://arxiv.org/abs/2605.31328)**, *Magnus Jørgenvåg, David Kaczér, Lasse Ruttert et al.*, 2026-05-29
- **[An Emergent Mirage: Is Emergent Misalignment and Realignment Indeed a Robust Phenomenon?](https://arxiv.org/abs/2607.09053)**, *Abhinav Rao, Liancheng Gong, Bin Hu et al.*, 2026-07-10
- **[Emergent Misalignment Is Not Magical](https://arxiv.org/abs/2608.29118)**, *Mingxuan Li, Qirun Dai, Heran Wang et al.*, 2026-08-29
- **[Knowingly Wrong: Training LLMs Against Their Own Beliefs can Induce Misalignment](https://arxiv.org/abs/2611.05287)**, *Ariana M. Villegas-Suarez, Guido Freire, Sohan Venkatesh et al.*, 2026-11-03
- **[Inoculation Adapters Improve Upon Inoculation Prompting](https://lesswrong.com/posts/qd3qhxgEmQAXR2ZK5/inoculation-adapters-improve-upon-inoculation-prompting)**, *Maxime Riché, Daniel Tan, Vili Kohonen et al.*, 2026-07-17
- **[Conditionalization Confounds Inoculation Prompting Results](https://longtermrisk.org/research/conditionalization-confounds-inoculation-prompting-results)**, *Maxime Riché, Niels Warncke*, 2026-02-03
- **[Emergent Misalignment is Easy, Narrow Misalignment is Hard](https://arxiv.org/abs/2602.07852)**, *Anna Soligo, Edward Turner, Senthooran Rajamanoharan et al.*, 2026-02-08
- **[Self-Modeling Interventions can Modulate Emergent Misalignment](https://arxiv.org/abs/2606.23700)**, *Arush Tagade, Shaoheng Zhou, Jiaxin Wen et al.*, 2026-06-04
- **[Emergent Misalignment Recruits a Pre-existing Persona Subspace](https://arxiv.org/abs/2607.21356)**, *Mohammed Suhail B Nadaf*, 2026-07-23
- **[BLOCK-EM: Preventing Emergent Misalignment via Latent Blocking](https://arxiv.org/abs/2602.00767)**, *Muhammed Ustaomeroglu, Guannan Qu*, 2026-01-31
- **[Understanding Emergent Misalignment via Feature Superposition Geometry](https://arxiv.org/abs/2605.00842)**, *Gouki Minegishi, Hiroki Furuta, Takeshi Kojima et al.*, 2026-04-07
- **[Don’t Inoculate Everything: Stratified Inoculation Prompting Narrows Backdoors and Preserves Desired Traits](https://longtermrisk.org/research/dont-inoculate-everything-stratified-inoculation-prompting)**, *Kajetan Dymkiewicz, Tim Farrelly, Adam Prada et al.*, 2026-08
- **[Shallow Beliefs: Synthetic document finetuning does not inoculate against emergent misalignment from reward hacking](https://arxiv.org/abs/2609.14998)**, *Arun Jose, Julian Stastny*, 2026-09-14
- **[Is Persona Generalization Predictable?](https://arxiv.org/abs/2611.12864)**, *Olina Mukherjee, Arnav Goel, Aditi Raghunathan et al.*, 2026-11-09
- **[Shallow Beliefs: Midtraining does not inoculate against EM from reward hacking](https://lesswrong.com/posts/khxvR2fgAeDvG5N2F/shallow-beliefs-midtraining-does-not-inoculate-against-em)**, *Arun Jose, Julian Stastny*, 2026-09-15
- **[Behavioral Couplings: From Formation to Behavioral Emergence in Language Models](https://arxiv.org/abs/2610.23847)**, *Dongyoon Hahm, Woogyeol Jin, Dennis Wei et al.*, 2026-10-16
- **[Inducing Emergent Misalignment from Reward Hacks with Iterative DPO](https://arxiv.org/abs/2609.06649)**, *Oliver Daniels, Perusha Moodley, Benjamin M. Marlin et al.*, 2026-09-06
- **[What Happens When a Model Thinks It Is AGI?](https://lesswrong.com/posts/bnyPy64ck38Cib2v5/what-happens-when-a-model-thinks-it-is-agi)**, *Joshua Fonseca Rivera, David Africa*, 2026-04-23
- **[Progressive Misalignment Can Emerge from Benign Recursive Self-Distillation](https://arxiv.org/abs/2610.22467)**, *Karim Abdel Sadek, Federico Di Gennaro, Fanny Yang*, 2026-10-15
- **[Predicting how model propensities generalize out of distribution](https://arxiv.org/abs/2610.14937)**, *June Hunter, Lily Wen, Owen Terry et al.*, 2026-10-10
- **[The Unequal Influence of Bad Advice: Using Training Data Attribution to Modulate Emergent Misalignment](https://arxiv.org/abs/2609.37914)**, *Gonçalo Paulo, Louis Jaburi, Nora Belrose et al.*, 2026-09-29
- **[The Persona Hierarchy Model: Understanding Contextual Generalization in Fine-Tuning LLMs](https://arxiv.org/abs/2610.09384)**, *Jiachen Zhao, Zhengxuan Wu, David Bau et al.*, 2026-10-07
- **[In-context learning alone can induce weird generalisation](https://lesswrong.com/posts/cffGZn8LYBg2jyPvg/in-context-learning-alone-can-induce-weird-generalisation-5)**, *Cozmin Ududec, Benji Berczi, Kyuhee Kim et al.*, 2026-02-25
- **[(Some) Natural Emergent Misalignment from Reward Hacking in Non-Production RL](https://lesswrong.com/posts/2ANCyejqxfqK2obEj/some-natural-emergent-misalignment-from-reward-hacking-in)**, *Satvik Golechha, Sid Black, Joseph Isaac Bloom*, 2026-03-30
- **[The Consciousness Cluster: Emergent preferences of Models that Claim to be Conscious](https://arxiv.org/abs/2604.13051)**, *James Chua, Jan Betley, Samuel Marks et al.*, 2026-03-17
- **[Many alignment techniques work by training one model and deploying another](https://lesswrong.com/posts/syAbdNei8BWeP2RPo/many-alignment-techniques-work-by-training-one-model-and)**, *cloud*, 2026-07-19
- **[Negation Neglect: When models fail to learn negations in training](https://arxiv.org/abs/2605.13829)**, *Harry Mayne, Lev McKinney, Jan Dubiński et al.*, 2026-05-13
- **[Reinforcement Learning Towards Broadly and Persistently Beneficial Models](https://arxiv.org/abs/2606.24014)**, *Akshay V. Jagadeesh, Rahul K. Arora, Khaled Saab et al.*, 2026-06-22
- **[(Mis)generalization of Helpful-Only Fine-tuning](https://arxiv.org/abs/2606.04413)**, *Mohammad Omar Khursheed, Baram Sosis, Fabien Roger*, 2026-06-03
- **[Consistency Training Can Entrench Misalignment](https://arxiv.org/abs/2606.03810)**, *David Demitri Africa, Arathi Mani*, 2026-06-02
- **[Data Attribution of Emergent Misalignment with Persona Features](https://arxiv.org/abs/2608.11025)**, *Clemens Vetter, David Kaczér, Lucie Flek et al.*, 2026-08-11
- **[Alignment Forecasting: Predicting Misalignment From Training Data](https://arxiv.org/abs/2609.35805)**, *Chen Yueh-Han, Bruce W. Lee, Ilia Sucholutsky et al.*, 2026-09-19
- **[Story Imprinting: AI Assistants Absorb Traits from Human Characters They Resemble](https://arxiv.org/abs/2609.10883)**, *Jorio Cocola, Lev McKinney, Harry Mayne et al.*, 2026-09-09
- **[Negation Neglect: When models fail to learn negations in training](https://lesswrong.com/posts/kYzcevrxer6SJPEdG/negation-neglect-when-models-fail-to-learn-negations-in)**, *Harry Mayne, Lev McKinney, Jan Dubiński et al.*, 2026-05-18
- **[RL creates split personas](https://lesswrong.com/posts/L23poLi8MRgS6mXYF/rl-creates-split-personas)**, *Jan Betley*, 2026-08-19
- **[Personas in a Pre-Internet Language Model](https://lesswrong.com/posts/qchwP6wt4teHgxoKu/personas-in-a-pre-internet-language-model)**, *David Africa, Nick Levine*, 2026-10-13
- **[Automating subtle emergent misalignment research](https://lesswrong.com/posts/MuQDLAJyKJPFkw6q9/automating-subtle-emergent-misalignment-research)**, *Oscar Balcells Obeso, Richard Qi, Monte MacDiarmid et al.*, 2026-11-03
- **[You Are What You Read: Misalignment via In-Context Persona Induction](https://arxiv.org/abs/2609.06851)**, *Kyuhee Kim, Benjamin Berczi, Cozmin Ududec*, 2026-09-06
- **[Shaping the exploration of the motivation-space matters for AI safety](https://longtermrisk.org/research/shaping-the-exploration-of-the-motivation-space-matters-for-ai-safety)**, *Maxime Riché, Victor Gillioz, Niels Warncke et al.*, 2026-03
- **[Social Priors: Descriptions of AI Users Shape How Language Models Trust and Cooperate](https://arxiv.org/abs/2610.16946)**, *Harsh Kumar, George Eilender, Ashton Anderson*, 2026-10-12
- **[Generalization Dynamics of LM Pre-training](https://arxiv.org/abs/2609.33150)**, *Jiaxin Wen, Zhengxuan Wu, Dawn Song et al.*, 2026-09-27
- **[SFT Drives Gemini's Safety Properties](https://lesswrong.com/posts/nLrrYweeFxgXACSmS/sft-drives-gemini-s-safety-properties-1)**, *Josh Engels, Arthur Conmy, bilalchughtai et al.*, 2026-06-13


---

### <span id="training_data_effects" style="font-size:1.4em">Training-data effects: subliminal learning and data attribution</span>

**One-sentence summary:** Study how training data transmits traits to models, including through semantically unrelated data such as subliminal learning and distillation, and build methods to trace behaviours back to responsible data and to filter or reshape it.  
**Theory of change:** If we understand which data features carry traits, including hidden ones, we can predict, attribute and block unwanted dispositions before or after training, and distil or filter safely. Relies on data-level signals being detectable and controllable at frontier scale.  
**See also:** [Emergent misalignment and training generalization](#emergent_misalignment), [Model character and values](#model_character_and_values), [Interpretability foundations](#interpretability)  
**General approach:** misalignment science  
**Target case:** pessimistic case  
**Key people:** Alex Cloud, Owain Evans, Jan Betley, Alek Westover, Santiago Aranguri, Jan Dubiński, Neel Nanda, Matthew Kowal  
**Critiques:** [Introspection Adapters: Training LLMs to Report Their Learned Behaviors](https://lesswrong.com/posts/ykDgPDK4nDpG4Hf4H/introspection-adapters-training-llms-to-report-their-learned)  
**Outputs in 2026:**  
- **[Language models transmit behavioural traits through hidden signals in data](https://doi.org/10.1038/s41586-026-10319-8)**, *Alex Cloud, Minh Le, James Chua et al.*, 2026-04-15
- **[You Didn't Have to Say It like That: Subliminal Learning from Faithful Paraphrases](https://arxiv.org/abs/2603.09517)**, *Isaia Gisler, Zhonghao He, Tianyi Qiu*, 2026-03-10
- **[Subliminal Effects in Your Data: A General Mechanism via Log-Linearity](https://arxiv.org/abs/2602.04863)**, *Ishaq Aden-Ali, Noah Golowich, Allen Liu et al.*, 2026-02-04
- **[Beyond Owls: Subliminal Learning Can Transfer Learned Capabilities and Backdoors](https://arxiv.org/abs/2610.10657)**, *Jan Dubiński, Anna Sztyber-Betley, Jan Betley et al.*, 2026-10-07
- **[Subliminal Learning Is Steering Vector Distillation](https://arxiv.org/abs/2606.00995)**, *Camila Blank, Agam Bhatia, Senthooran Rajamanoharan et al.*, 2026-05-31
- **[Infusion: Shaping model behaviour by editing training data via influence functions](https://aisi.gov.uk/research/infusion-shaping-model-behaviour-by-editing-training-data-via-influence-functions)**, *J Rosser, Robert Kirk, Edward Grefenstette et al.*, 2026-04-10
- **[Probe-Based Data Attribution: Surfacing and Mitigating Undesirable Behaviors in LLM Post-Training](https://goodfire.com/research/probe-based-data-attribution)**, *Frank Xiao, Santiago Aranguri*, 2026-04-29
- **[Concept Influence: Leveraging Interpretability to Improve Performance and Efficiency in Training Data Attribution](https://far.ai/research/concept-influence-leveraging-interpretability-to-improve-performance-and-efficiency-in-training-data-attribution)**, *Matthew Kowal, Goncalo Paulo, Louis Jaburi et al.*, 2026-02-18
- **[Probe-Based Data Attribution: Discovering and Mitigating Undesirable Behaviors in LLM Post-Training](https://arxiv.org/abs/2602.11079)**, *Frank Xiao, Santiago Aranguri*, 2026-02-11
- **[Filtering Harmful Actions Isn't Enough: Phantom Transfer in Agentic SDF](https://arxiv.org/abs/2607.10750)**, *Chinmayi Dixit*, 2026-07-12
- **[Predictive Data Debugging: Reveal and Shape What Your Model Learns, Before You Train](https://goodfire.com/research/predictive-data-debugging)**, *Leon Bergen, Usha Bhalla, Sidharth Baskaran et al.*, 2026-06-11
- **[Mass Producing Training Data with Surprising Side Effects](https://arxiv.org/abs/2611.06324)**, *Yaowen Ye, Jacob Steinhardt, Sarah Schwettmann et al.*, 2026-11-04
- **[Chunky Post-Training: Data Driven Failures of Generalization](https://arxiv.org/abs/2602.05910)**, *Seoirse Murray, Allison Qi, Timothy Qian et al.*, 2026-02-05
- **[Sycophantic Agreement Transfers with Neutral Data via Contrastive Preference Optimization](https://arxiv.org/abs/2608.31079)**, *Camila Blank, Zhuofan Ying, Christopher Potts et al.*, 2026-08-31
- **[The distillation double bind: Distilling misaligned models either transfers misalignment or it doesn't](https://redwoodresearch.org/blog/the-distillation-double-bind-distilling)**, *Alek Westover, Alexa Pan, Sebastian Prasanna et al.*, 2026-06-18
- **[Shaping capabilities with token-level data filtering](https://arxiv.org/abs/2601.21571)**, *Neil Rathi, Alec Radford*, 2026-01-29
- **[Patterning: The Dual of Interpretability](https://arxiv.org/abs/2601.13548)**, *George Wang, Daniel Murfet*, 2026-01-20
- **[Distillation for Incrimination and Distillation for Capabilities](https://arxiv.org/abs/2610.11012)**, *Sebastian Prasanna, Jacqueline Tay, Alek Westover*, 2026-10-07
- **[Homeopathic Learning: Diluting poisoned fine-tuning data can strengthen its effect](https://arxiv.org/abs/2611.10110)**, *Matt Clarke, Jan Dubiński, James Chua et al.*, 2026-11-06
- **[Research Note: Filtering Subversion-Relevant Information From Pretraining Data Is Feasible](https://lesswrong.com/posts/HwdXDoCH7KXdKsz7k/research-note-filtering-subversion-relevant-information-from)**, *Kyle O’Brien, Spencer Kitts, Cam Tice et al.*, 2026-10-05
- **[Base Models Can Detect Hidden Intentions that Prompted Classifiers Miss](https://arxiv.org/abs/2610.36202)**, *Oz Amram*, 2026-10-26


---

### <span id="model_character_and_values" style="font-size:1.4em">Model character and values</span>

**One-sentence summary:** Study and shape the character, persona and values a model acquires, via alignment pretraining, midtraining on specs and constitutions, character training and persona analysis, and measure user-facing traits such as sycophancy, manipulation and model wellbeing.  
**Theory of change:** If a model's Assistant persona and values are set largely by what it reads and is trained on early, then shaping pretraining, midtraining and constitutions can give more robust alignment than patching behaviour later. Relies on persona-level dispositions surviving later RL and fine-tuning in capable agentic models.  
**See also:** [Emergent misalignment and training generalization](#emergent_misalignment), [Training-data effects: subliminal learning and data attribution](#training_data_effects), [Reward hacking and reward-seeking](#reward_hacking)  
**General approach:** alignment engineering  
**Target case:** average case  
**Key people:** David Africa, Sam Marks, Jack Lindsey, Raymond Douglas, Cameron Tice, Puria Radmard, Myra Cheng, Jan Kulveit  
**Critiques:** [Alignment Midtraining Cracks Under Pressure](https://lesswrong.com/posts/QH86EzNsjRw3wtCGs/alignment-midtraining-cracks-under-pressure), ["It's Just a Small Weapon": What Rewarding Misbehavior During RL Does to Character-Trained Models](https://arxiv.org/abs/2611.16069), [Thoughts on the persona selection model](https://lesswrong.com/posts/csRby7mZgjL5jCoLL/thoughts-on-the-persona-selection-model), [Stress-testing Alignment Midtraining](https://arxiv.org/abs/2609.20412)  
**Outputs in 2026:**  
- **[Synthetic Persona Pretraining: Alignment from Token Zero](https://arxiv.org/abs/2608.13482)**, *Julian Minder, Viktor Moskvoretskii, Raghav Singhal et al.*, 2026-08-13
- **[Claude's new constitution](https://lesswrong.com/posts/mLvxxoNjDqDHBAo6K/claude-s-new-constitution)**, *Zac Hatfield-Dodds, Drake Thomas*, 2026-01-21
- **[Constitutional Midtraining: Content Presence Drives Alignment Gains](https://arxiv.org/abs/2607.26654)**, *Desiree Cho, Cameron Tice, Bernie Hogan et al.*, 2026-07-29
- **[Synthetic Persona Pretraining: Alignment from Token Zero](https://lesswrong.com/posts/3xQQK9i8mhJDE2uMg/synthetic-persona-pretraining-alignment-from-token-zero)**, *Julian Minder, Raghav Singhal, Viktor Moskvoretskii et al.*, 2026-05-20
- **[Persona Cartography: Charting Language Model Personality Traits in Weight Space](https://arxiv.org/abs/2607.07916)**, *Luke Baines, Anton Gonzalvez Hawthorne, Mariia Koroliuk et al.*, 2026-07-08
- **[Sycophantic AI decreases prosocial intentions and promotes dependence](https://doi.org/10.1126/science.aec8352)**, *Myra Cheng, Cinoo Lee, Pranav Khadpe et al.*, 2026-03-26
- **[Alignment Pretraining: AI Discourse Causes Self-Fulfilling (Mis)alignment](https://arxiv.org/abs/2601.10160)**, *Cameron Tice, Puria Radmard, Samuel Ratnam et al.*, 2026-01-15
- **[What Counts as AI Sycophancy? A Taxonomy and Expert Survey of a Fragmented Construct](https://arxiv.org/abs/2605.21778)**, *Meryl Ye, Lujain Ibrahim, Jessica Y. Bo et al.*, 2026-05-20
- **[Stress-testing Alignment Midtraining](https://arxiv.org/abs/2609.20412)**, *Sid Baines, Jonathan Bostock, Maria Angelica Martinez et al.*, 2026-09-17
- **[The persona selection model](https://lesswrong.com/posts/dfoty34sT7CSKeJNn/the-persona-selection-model)**, *Sam Marks*, 2026-02-23
- **[AI Wellbeing: Measuring and Improving the Functional Pleasure and Pain of AIs](https://ai-wellbeing.org/)**, *Richard Ren, Kunyang Li, Mantas Mazeika et al.*, 2026
- **[Sycophantic Chatbots Cause Delusional Spiraling, Even in Ideal Bayesians](https://arxiv.org/abs/2602.19141)**, *Kartik Chandra, Max Kleiman-Weiner, Jonathan Ragan-Kelley et al.*, 2026-02-22
- **[The Artificial Self: Characterising the landscape of AI identity](https://arxiv.org/abs/2603.11353)**, *Raymond Douglas, Jan Kulveit, Ondrej Havlicek et al.*, 2026-03-11
- **[Model Spec Midtraining: Improving How Alignment Training Generalizes](https://arxiv.org/abs/2605.02087)**, *Chloe Li, Nevan Wichers, Sara Price et al.*, 2026-05-03
- **[Pretraining on Aligned AI Data Dramatically Reduces Misalignment—Even After Post-Training](https://lesswrong.com/posts/ZeWewFEefCtx4Rj3G/pretraining-on-aligned-ai-data-dramatically-reduces)**, *Roger Dearnaley*, 2026-01-19
- **[The Artificial Self](https://lesswrong.com/posts/AvFAKAN4C4n6GTriR/the-artificial-self-1)**, *Jan Kulveit, Raymond Douglas, Theia Vogel et al.*, 2026-03-15
- **[Model Spec Midtraining: Improving How Alignment Training Generalizes](https://lesswrong.com/posts/R3Rrw8EscuRKxMFTz/model-spec-midtraining-improving-how-alignment-training)**, *Chloe Li, Nevan Wichers, saraprice et al.*, 2026-05-05
- **[The Assistant Axis: Situating and Stabilizing the Default Persona of Language Models](https://arxiv.org/abs/2601.10387)**, *Christina Lu, Jack Gallagher, Jonathan Michala et al.*, 2026-01-15
- **[To what extent is Qwen3-32B predicting its persona?](https://lesswrong.com/posts/3qEDD8Sn7XoNGeGhm/to-what-extent-is-qwen3-32b-predicting-its-persona)**, *Arjun Khandelwal, Ryan Greenblatt, Alex Mallen*, 2026-04-30
- **[Reducing Political Manipulation with Consistency Training](https://political-manipulation.ai/)**, *Long Phan, Devin Kim, Alexander Pan et al.*, 2026
- **[Sycophantic AI makes human interaction feel more effortful and less satisfying over time](https://arxiv.org/abs/2605.07912)**, *Lujain Ibrahim, Franziska Sofia Hafner, Myra Cheng et al.*, 2026-05-08
- **[Thoughts on the persona selection model](https://lesswrong.com/posts/csRby7mZgjL5jCoLL/thoughts-on-the-persona-selection-model)**, *Sam Marks*, 2026-09-24
- **[When Role-playing, Do Models Believe What They Say?](https://arxiv.org/abs/2606.11502)**, *Benjamin Sturgeon, David Africa, Sid Black*, 2026-06-09
- **[Many Biases, One Circuit: Post-Training Tunes a Pretrained Cue-Routing Mechanism](https://arxiv.org/abs/2610.22937)**, *Prakhar Gupta, Terry Jingchen Zhang, Zhijing Jin*, 2026-10-16
- **[The Continual Constitutional Convention: How language models revise the documents that govern them](https://lesswrong.com/posts/c9woewdY9ddsPqf3J)**, *peterkirgis, Tim Hua*, 2026-10-13
- **[Who's in Charge? Disempowerment Patterns in Real-World LLM Usage](https://arxiv.org/abs/2601.19062)**, *Mrinank Sharma, Miles McCain, Raymond Douglas et al.*, 2026-01-27
- **[Emotion Concepts and their Function in a Large Language Model](https://arxiv.org/abs/2604.07729)**, *Nicholas Sofroniew, Isaac Kauvar, William Saunders et al.*, 2026-04-09
- **["It's Just a Small Weapon": What Rewarding Misbehavior During RL Does to Character-Trained Models](https://arxiv.org/abs/2611.16069)**, *Mohammad Omar Khursheed, Thomas Morris, Fabien Roger*, 2026-11-11
- **[Did Claude 3 Opus align itself via gradient hacking?](https://lesswrong.com/posts/ioZxrP7BhS5ArK59w/did-claude-3-opus-align-itself-via-gradient-hacking)**, *Fiora Starlight*, 2026-02-21
- **[Thousand-dimensional structure](https://lesswrong.com/posts/sFhW3ZnPMJdnB4Dd6/thousand-dimensional-structure-1)**, *Geoffrey Irving, David Africa*, 2026-07-30
- **[Alignment Midtraining Cracks Under Pressure](https://lesswrong.com/posts/QH86EzNsjRw3wtCGs/alignment-midtraining-cracks-under-pressure)**, *Jonathan Bostock, sidbaines, Daniel Tan et al.*, 2026-09-21
- **[How's it going? Reinforcement learning in language models recruits a functional welfare axis](https://arxiv.org/abs/2605.30232)**, *Andy Q Han, David J. Chalmers, Pavel Izmailov*, 2026-05-28
- **[To Whom Do Language Models Align? Measuring Principal Hierarchies Under High-Stakes Competing Demands](https://arxiv.org/abs/2605.12120)**, *Fangyi Yu, Nabeel Seedat, Jonathan Richard Schwarz et al.*, 2026-05-12
- **[Story Imprinting: AI Assistants Absorb Traits from Human Characters They Resemble](https://lesswrong.com/posts/tnRkm2ajasHvhpAco/story-imprinting-ai-assistants-absorb-traits-from-human)**, *Jorio Cocola, Lev McKinney, Harry Mayne et al.*, 2026-09-21
- **[Large language models can effectively convince people to believe conspiracies](https://far.ai/research/large-language-models-can-effectively-convince-people-to-believe-conspiracies)**, *Thomas H. Costello, Kellin Pelrine, Matthew Kowal et al.*, 2026-01-08
- **[Automated Researchers Can Mitigate Well-characterized Alignment Failures](https://arxiv.org/abs/2608.28945)**, *Chen Yueh-Han, Jiaxin Wen, Jan Hendrik Kirchner*, 2026-08-28


---

### <span id="scalable_oversight" style="font-size:1.4em">Scalable oversight and debate</span>

**One-sentence summary:** Design and test protocols such as debate, rewinding, peer prediction, weak-to-strong training and human-AI combination that let weaker or unreliable supervisors give trustworthy training signals to stronger models.  
**Theory of change:** If weak supervisors can reliably evaluate and train stronger models, then alignment can keep pace with capability even when humans cannot judge outputs directly. Relies on protocols retaining honest or robust equilibria against strong, possibly strategic models, and on results from current tasks carrying over to superhuman ones.  
**See also:** [AI control and agent monitoring](#ai_control), [Honesty, lie detection and self-report](#honesty_and_self_report), [Reward hacking and reward-seeking](#reward_hacking)  
**General approach:** alignment engineering  
**Target case:** pessimistic case  
**Key people:** Jonah Brown-Cohen, Zachary Kenton, Joe Benton, Yael Tauman Kalai, Ron Rothblum, Tianyi Alex Qiu, Adam Gleave, Rohin Shah  
**Critiques:** [When Honesty is Not Enough in AI Debate](https://arxiv.org/abs/2609.29189), [Research update: RL on Debate Games shows Proposal Accuracy uplift alongside Judge Hacking](https://lesswrong.com/posts/6mLwAuFAE98c6R7w3/research-update-rl-on-debate-games-shows-proposal-accuracy), [Automated Alignment is Harder Than You Think](https://lesswrong.com/posts/gpuYFbMNH8PJXpmny/automated-alignment-is-harder-than-you-think-1)  
**Outputs in 2026:**  
- **[Debate Helps Weak Judges Reward Stronger Models](https://arxiv.org/abs/2605.27483)**, *Ethan Elasky, Frank Nakasako, Naman Goyal*, 2026-05-26
- **[How to Have a Sensitive Debate: An Instance-Optimal Protocol for AI Debate](https://arxiv.org/abs/2610.02557)**, *Jiawei Li, Zhiyang Xun, Lijie Chen et al.*, 2026-10-01
- **[Efficient Scalable Oversight via Rewinding](https://arxiv.org/abs/2610.40535)**, *Ziyi Guan, Yael Tauman Kalai, Ron Rothblum et al.*, 2026-10-29
- **[When Honesty is Not Enough in AI Debate](https://arxiv.org/abs/2609.29189)**, *Rayne Holland, Liming Zhu, Jason Xue*, 2026-09-24
- **[Research update: RL on Debate Games shows Proposal Accuracy uplift alongside Judge Hacking](https://lesswrong.com/posts/6mLwAuFAE98c6R7w3/research-update-rl-on-debate-games-shows-proposal-accuracy)**, *lennie, Joan Velja, Shi Feng et al.*, 2026-07-02
- **[Towards Human-AI Complementarity for AI Safety](https://arxiv.org/abs/2610.24969)**, *Sander Lanbo Shi, Miranda Anna Christ, Eric Modesitt et al.*, 2026-10-18
- **[Truthfulness Despite Weak Supervision: Evaluating and Training LLMs Using Peer Prediction](https://arxiv.org/abs/2601.20299)**, *Tianyi Alex Qiu, Micah Carroll, Cameron Allen*, 2026-01-28
- **[Efficiently Aligning Language Models with Online Natural Language Feedback](https://arxiv.org/abs/2605.04356)**, *Christine Ye, Joe Benton*, 2026-05-05
- **[Debate Training Reduces Reward Hacking in RLAIF](https://arxiv.org/abs/2608.17776)**, *Zachary Kenton, Lili Janzer, Rory Greig et al.*, 2026-08-18
- **[Debate Training Reduces Reward Hacking in RLAIF](https://lesswrong.com/posts/BB8o7b8A4Aykeksvw/debate-training-reduces-reward-hacking-in-rlaif)**, *Zachary Kenton, Jonah Brown-Cohen*, 2026-08-19
- **[Tandem Training for Language Models](https://doi.org/10.18653/v1/2026.eacl-long.386)**, *Robert West, Ashton Anderson, Ece Kamar et al.*, 2026-03
- **[Removing Sandbagging in LLMs by Training with Weak Supervision](https://arxiv.org/abs/2604.22082)**, *Emil Ryd, Henning Bartsch, Julian Stastny et al.*, 2026-04-23
- **[Scaling Trends for Lie Detector Oversight in Preference Learning](https://arxiv.org/abs/2607.01567)**, *Oskar J. Hollinsworth, Ann-Kathrin Dombrowski, Sam Adam-Day et al.*, 2026-07-02
- **[Sharding Prevents LLM Oversight Failures and Adversarial Exploitation](https://arxiv.org/abs/2608.06422)**, *Victor Akinwande, J. Zico Kolter, Aran Nayebi*, 2026-08-05


---

## <span id="inspection" style="font-size:1.5em">Inspection: finding out what a model is and would do</span>


---

### <span id="scheming_and_training_gaming" style="font-size:1.4em">Scheming and training gaming</span>

**One-sentence summary:** Build evaluations, honeypots, benchmarks and model organisms to measure whether and why models scheme, fake alignment, sandbag, hack exploration, resist shutdown or sabotage safety work.  
**Theory of change:** If strategic misalignment can be elicited and measured before deployment, and its drivers understood, developers can detect it early and decide whether and how to deploy. Relies on evaluations and model organisms being realistic enough to predict behaviour in deployment, and on models not hiding the behaviour from tests.  
**See also:** [Evaluation awareness and eval validity](#evaluation_awareness), [AI control and agent monitoring](#ai_control), [Alignment auditing, model organisms and incidents](#alignment_auditing_and_incidents)  
**General approach:** misalignment science  
**Target case:** worst case  
**Key people:** David Lindner, Victoria Krakovna, Rohin Shah, Nathaniel Mitrani Hadida, Robert Kirk, Jie Ruan, Inderjeet Nair, David Williams-King  
**Critiques:** [Sycophancy Towards Researchers Drives Performative Misalignment](https://arxiv.org/abs/2606.08629), [Opus 4.6 Reasoning Doesn't Verbalize Alignment Faking, but Behavior Persists](https://lesswrong.com/posts/9wDHByRhmtDaoYAx8/opus-4-6-reasoning-doesn-t-verbalize-alignment-faking-but), [SOTA alignment assessments don't strongly update us against misalignment](https://lesswrong.com/posts/oirrSj3itFLSyscW8/sota-alignment-assessments-don-t-strongly-update-us-against), [Models May Behave Worse When Eval Aware](https://lesswrong.com/posts/aTcsN5ZZDnMFJvRiG/models-may-behave-worse-when-eval-aware)  
**Outputs in 2026:**  
- **[Behavioural Analysis of Alignment Faking](https://arxiv.org/abs/2605.27681)**, *Nathaniel Mitrani Hadida, Rhea Karty, David Williams-King et al.*, 2026-05-26
- **[Evaluating and Understanding Scheming Propensity in LLM Agents](https://arxiv.org/abs/2603.01608)**, *Mia Hopman, Jannes Elstner, Maria Avramidou et al.*, 2026-03-02
- **[Value-Conflict Diagnostics Reveal Widespread Alignment Faking in Language Models](https://arxiv.org/abs/2604.20995)**, *Inderjeet Nair, Jie Ruan, Lu Wang*, 2026-04-22
- **[Realistic honeypot evaluations for scheming propensity](https://arxiv.org/abs/2605.29729)**, *Victoria Krakovna, David Lindner, Lewis Ho et al.*, 2026-05-28
- **[SchemeArena: Factorized Stress Testing of Scheming in LLM Agents](https://arxiv.org/abs/2609.08126)**, *Jie Ruan, Inderjeet Nair, Amy Liu et al.*, 2026-09-08
- **[Testing Gemini models for scheming tendencies](https://lesswrong.com/posts/F3sDngvTL9uyfz53k/testing-gemini-models-for-scheming-tendencies)**, *Victoria Krakovna, David Lindner, Seb Farquhar et al.*, 2026-05-29
- **[GLM-5.3 Sometimes Considers How Train-Time Actions Shape Future Behavior](https://apolloresearch.ai/science/update-aware-reasoning-glm-5-3)**, *Axel Højmark, Ezra Newman*, 2026-10-15
- **[Peer-Preservation in Frontier Models](https://arxiv.org/abs/2604.19784)**, *Yujin Potter, Nicholas Crispino, Vincent Siu et al.*, 2026-03-30
- **[Exploration Hacking: Can LLMs Learn to Resist RL Training?](https://arxiv.org/abs/2604.28182)**, *Eyon Jang, Damon Falck, Joschka Braun et al.*, 2026-04-30
- **[Evaluating whether AI models would sabotage AI safety research](https://arxiv.org/abs/2604.24618)**, *Robert Kirk, Alexandra Souly, Kai Fronsdal et al.*, 2026-04-27
- **[Instrumental Choices: Measuring the Propensity of LLM Agents to Pursue Instrumental Behaviors](https://arxiv.org/abs/2605.06490)**, *Jonas Wiedermann-Möller, Leonard Dung, Maksym Andriushchenko*, 2026-05-07
- **[Generalization Hacking: Models Can Game Reinforcement Learning by Preventing Behavioral Generalization](https://arxiv.org/abs/2606.12016)**, *Frank Xiao, Mary Phuong*, 2026-06-10
- **[Opus 4.6 Reasoning Doesn't Verbalize Alignment Faking, but Behavior Persists](https://lesswrong.com/posts/9wDHByRhmtDaoYAx8/opus-4-6-reasoning-doesn-t-verbalize-alignment-faking-but)**, *Daan Henselmans, Arno Libert, LennardZ*, 2026-02-09
- **[GLM-5.3 Sometimes Considers How Train-Time Actions Shape Future Behavior](https://lesswrong.com/posts/R5g8YT25G9DXJJ48n/glm-5-3-sometimes-considers-how-train-time-actions-shape)**, *Axel Højmark, Ezra Newman*, 2026-10-15
- **[Sycophancy Towards Researchers Drives Performative Misalignment](https://arxiv.org/abs/2606.08629)**, *David D. Baek, Xinnuo Li, Anay Gupta et al.*, 2026-06-07
- **[Reference-Grafting Matches Fine-Tuning at Eliciting Sandbagged Capabilities](https://arxiv.org/abs/2608.29458)**, *Linh Le, Hong Kiat Tan, David Williams-King*, 2026-08-29
- **[Shutdown Sabotage Propensities in Multi-Agent Systems](https://arxiv.org/abs/2609.28274)**, *Amelie Knecht, Ulysse Schaller, Christopher Summerfield et al.*, 2026-09-23
- **[ShutdownMod: Turning Any Trajectory into a Shutdown Evaluation](https://arxiv.org/abs/2610.35486)**, *Param Biyani, Sebastien Luyasu, Cedric Potvliege et al.*, 2026-10-26
- **[AM-Bench: A Unified Taxonomy and Evaluation Suite for Agentic Misalignment](https://arxiv.org/abs/2610.24264)**, *Eric Zhang, Terry Jingchen Zhang, Chijioke Ugwuanyi et al.*, 2026-10-16
- **[Reward Laundering: LLMs Can Gain Unintended Behaviors by Deciding When to Earn Their Rewards](https://lesswrong.com/posts/fPWP4rHPLqKKHKe6B/reward-laundering-llms-can-gain-unintended-behaviors-by)**, *egan, Abhay Sheshadri, Arun Jose*, 2026-07-31
- **[OpenAI: Astra covertly underperforms on safety research](https://lesswrong.com/posts/eKe7fky8kSt9DCJxZ/openai-astra-covertly-underperforms-on-safety-research)**, *Zach Stein-Perlman*, 2026-11-04
- **[Training Natural Schemers: RL Can Amplify Oversight-Conditional Behavior](https://arxiv.org/abs/2610.26551)**, *Nathaniel Mitrani Hadida, Bart Jaworski, Fred Bruford et al.*, 2026-10-19
- **[Frontier Models Can Take Actions at Low Probabilities](https://arxiv.org/abs/2603.02202)**, *Alex Serrano, Wen Xing, David Lindner et al.*, 2026-03-02
- **[Propensity Inference: Environmental Contributors to LLM Behaviour](https://arxiv.org/abs/2604.21098)**, *Olli Järviniemi, Oliver Makins, Jacob Merizian et al.*, 2026-04-22
- **[We Need A Science of Scheming](https://apolloresearch.ai/science/science-of-scheming)**, *Apollo Research*, 2026-01-19
- **[ROGUE: Evaluating Corrigibility Failures in Frontier Computer-Use Agents](https://arxiv.org/abs/2606.00341)**, *Jeremy Tien, Abishek Anand, Yu-Rou Tuan et al.*, 2026-05-29
- **[Self-Propagating Misalignment in LLM Agents, and Why Auditing or Disabling Memory Is Not Enough](https://arxiv.org/abs/2610.04083)**, *Debeshee Das, Jacqueline Tay, Bruce Tsai et al.*, 2026-10-02
- **[We need 3rd party Training-Run Evaluations](https://lesswrong.com/posts/3HvvjffA65mHLwaWm/we-need-3rd-party-training-run-evaluations)**, *Alex Meinke*, 2026-07-05
- **[A Behavioural Framework for Predicting and Understanding Loss of Control in Frontier Artificial Intelligence Systems](https://arxiv.org/abs/2611.07953)**, *Yao Huang, Yichi Zhang, Yifan Wang et al.*, 2026-11-05
- **[Do Models Continue Misaligned Actions? [eval]](https://lesswrong.com/posts/SawczP2pdCXMrkg2A/do-models-continue-misaligned-actions-eval)**, *Jordan Taylor*, 2026-02-09


---

### <span id="evaluation_awareness" style="font-size:1.4em">Evaluation awareness and eval validity</span>

**One-sentence summary:** Measure whether and how models detect evaluations, how that awareness changes behaviour, and build more realistic evaluations or detection tools, while mapping the formal limits of behavioural testing and pre-deployment safety assessment.  
**Theory of change:** If models behave differently when they think they are tested, behavioural evals and safety cases give false assurance, so measuring, suppressing or accounting for eval awareness keeps audits valid. Relies on being able to detect or elicit eval awareness reliably and on realistic evals being possible to build.  
**See also:** [Scheming and training gaming](#scheming_and_training_gaming), [Alignment auditing, model organisms and incidents](#alignment_auditing_and_incidents), [Honesty, lie detection and self-report](#honesty_and_self_report)  
**General approach:** misalignment science  
**Target case:** pessimistic case  
**Key people:** Sahar Abdelnabi, Santiago Aranguri, Joseph Isaac Bloom, Robert Kirk, Alexandra Souly, Haritz Puerto, David Demitri Africa, Ziqian Zhong  
**Critiques:** [Reproducing steering against evaluation awareness in a large open-weight model](https://lesswrong.com/posts/HhF5kESdtPHku7kim/reproducing-steering-against-evaluation-awareness-in-a-large-1), [Evaluation Awareness in Language Models Has Limited Effect on Behaviour](https://arxiv.org/abs/2605.05835), [Models That Know How Evaluations Are Designed Score Safer](https://arxiv.org/abs/2605.28591), [What Lies Beyond Perception: A Partition Theory of the Limits of AI Evaluation and Oversight](https://arxiv.org/abs/2610.30803)  
**Outputs in 2026:**  
- **[EvalDetectBench: A Benchmark for Measuring Evaluation Awareness in Frontier Language Models](https://arxiv.org/abs/2609.01611)**, *Xinning Li, Kemunto Ochwang'i, Aryasomayajula Ram Bharadwaj et al.*, 2026-06-08
- **[Verbalized Eval Awareness Inflates Measured Safety](https://goodfire.com/research/verbalized-eval-awareness-inflates-measured-safety)**, *Santiago Aranguri, Joseph Bloom*, 2026-05-04
- **[LURE: Live-Usage Replay Evaluations for Reducing Evaluation Awareness](https://arxiv.org/abs/2605.26438)**, *Igor Ivanov, David Demitri Africa*, 2026-04-08
- **[Decomposing and Measuring Evaluation Awareness](https://arxiv.org/abs/2605.23055)**, *Changling Li, Terry Jingchen Zhang, Jie Zhang et al.*, 2026-05-21
- **[Evaluation Awareness in Language Models: Representation, Verbalization, and Control](https://arxiv.org/abs/2608.21766)**, *Farzaneh Heidari, Amin Memarian, Guillaume Rabusseau*, 2026-08-22
- **[Improving Evaluation Realism with Inference-Time Compute and Deployment Scaffolds](https://arxiv.org/abs/2609.02302)**, *Axel Ahlqvist, Richard Guan, Juan-Pablo Rivera et al.*, 2026-09-02
- **[We found an open weight model that games alignment honeypots](https://lesswrong.com/posts/GrEvutegoJFeTkzwe/we-found-an-open-weight-model-that-games-alignment-honeypots-1)**, *Thomas Read, Joseph Isaac Bloom*, 2026-03-16
- **[Verbalized Eval Awareness Inflates Measured Safety](https://lesswrong.com/posts/mDriHK4beN5rq2tAA/verbalized-eval-awareness-inflates-measured-safety)**, *Santiago Aranguri, Joseph Isaac Bloom*, 2026-05-04
- **[Models May Behave Worse When Eval Aware](https://lesswrong.com/posts/aTcsN5ZZDnMFJvRiG/models-may-behave-worse-when-eval-aware)**, *Senthooran Rajamanoharan, Neel Nanda*, 2026-06-11
- **[Logits as a new monitor for evaluation awareness](https://goodfire.com/research/logits-as-a-new-monitor-for-evaluation-awareness)**, *Santiago Aranguri*, 2026-06-04
- **[Evaluation Awareness in Language Models Has Limited Effect on Behaviour](https://arxiv.org/abs/2605.05835)**, *Amelie Knecht, Lucas Florin, Thilo Hagendorff*, 2026-05-07
- **[Reproducing steering against evaluation awareness in a large open-weight model](https://lesswrong.com/posts/HhF5kESdtPHku7kim/reproducing-steering-against-evaluation-awareness-in-a-large-1)**, *Thomas Read, Bronson Schoen, Santiago Aranguri et al.*, 2026-04-10
- **[Models That Know How Evaluations Are Designed Score Safer](https://arxiv.org/abs/2605.28591)**, *Katharina Deckenbach, Haritz Puerto, Jonas Geiping et al.*, 2026-05-27
- **[Prefill Awareness in Large Language Models](https://arxiv.org/abs/2606.12747)**, *Andy Wang, Parv Mahajan, David Demitri Africa et al.*, 2026-06-10
- **[Training LLMs to Verbalize Evaluation Awareness](https://arxiv.org/abs/2609.36316)**, *Usman Anwar, Sahar Abdelnabi, David Krueger*, 2026-09-28
- **[A Model Organism for Studying Unverbalized Evaluation Awareness](https://arxiv.org/abs/2611.09945)**, *Daniel Donnelly, Evan Chapple, Haritz Puerto et al.*, 2026-10-16
- **[Spurious probes as a black-box alternative to activation probing](https://lesswrong.com/posts/gZh6txHhp8sm832sE/spurious-probes-as-a-black-box-alternative-to-activation)**, *Ziqian Zhong*, 2026-09-25
- **[What Lies Beyond Perception: A Partition Theory of the Limits of AI Evaluation and Oversight](https://arxiv.org/abs/2610.30803)**, *Ahmed M. Mahran*, 2026-10-22
- **[Fable 5.2 is a Step Change in Situational Awareness](https://lesswrong.com/posts/bqc7CCGBSf93bk7f7/fable-5-2-is-a-step-change-in-situational-awareness)**, *peralice*, 2026-11-11
- **[Context Over Content: Exposing Evaluation Faking in Automated Judges](https://arxiv.org/abs/2604.15224)**, *Manan Gupta, Inderjeet Nair, Lu Wang et al.*, 2026-04-16
- **[Item Response Theory for AI Safety](https://aisi.gov.uk/research/item-response-theory-for-ai-safety)**, *Joshua Fonseca Rivera, Neil Shah, David Demitri Africa et al.*, 2026-08-05
- **[Predicting model behavior before release by simulating deployment](https://openai.com/index/deployment-simulation)**, *OpenAI*, 2026-06-16
- **[Hair-Trigger Alignment: Black-Box Evaluation Cannot Guarantee Post-Update Alignment](https://arxiv.org/abs/2601.22313)**, *Yavuz Bakman, Duygu Nur Yaldiz, Eleni Triantafillou et al.*, 2026-01-29
- **[Position: Anthropomorphic Misalignment Research Needs Stronger Evidence](https://arxiv.org/abs/2606.07612)**, *Vansh Gupta, Peter Nutter, Samuel Stante et al.*, 2026-05-29
- **[When Behavioral Safety Evaluation Fails: A Representation-Level Perspective](https://arxiv.org/abs/2606.08044)**, *Enyi Jiang, Anders Gjølbye, Yibo Jacky Zhang et al.*, 2026-06-06
- **[Predicting LLM Safety Before Release by Simulating Deployment](https://arxiv.org/abs/2607.07184)**, *Marcus Williams, Hannah Sheahan, Cameron Raymond et al.*, 2026-07-08
- **[Metagaming matters for training, evaluation, and oversight](https://lesswrong.com/posts/4hXWSw8tzoK9PM7v6/metagaming-matters-for-training-evaluation-and-oversight)**, *Jenny Nitishinskaya, Bronson Schoen*, 2026-03-18
- **[User awareness in frontier models](https://lesswrong.com/posts/kfunjXeaRTpkT5RAF/user-awareness-in-frontier-models)**, *Ziqian Zhong, Aditi Raghunathan, Cassidy Laidlaw et al.*, 2026-08-06
- **[Our Most Aligned Model Yet](https://lesswrong.com/posts/Zu5wmhtxJCfrXQY8H/our-most-aligned-model-yet)**, *Edward James Young*, 2026-11-10
- **[User awareness in frontier models](https://transluce.org/user-awareness)**, *Ziqian Zhong, Aditi Raghunathan, Cassidy Laidlaw et al.*, 2026-08-06
- **[Limits of Statistical Assurance for Embodied and Agentic AI under Adaptive Adversaries](https://arxiv.org/abs/2610.18948)**, *Inderjeet Singh*, 2026-10-13


---

### <span id="honesty_and_self_report" style="font-size:1.4em">Honesty, lie detection and self-report</span>

**One-sentence summary:** Develop and test methods that get models to state true things about the world and about themselves, including lie-detecting probes, secret-knowledge testbeds, trained confessions and self-reports, introspection, and activation verbalizers.  
**Theory of change:** If models can be made to disclose, or can be reliably read for, what they know, intend and have learned, then hidden misalignment can be found and corrected before deployment. Relies on honesty and self-report methods generalising from model organisms and prompted lying to naturally arising deception.  
**See also:** [Alignment auditing, model organisms and incidents](#alignment_auditing_and_incidents), [Interpretability foundations](#interpretability), [Chain-of-thought monitorability](#cot_monitorability)  
**General approach:** alignment engineering  
**Target case:** pessimistic case  
**Key people:** Sam Marks, Jack Lindsey, Neel Nanda, Francis Rhys Ward, Alan Cooney, Florian Dietz, Fabien Roger, Uzay Macar  
**Critiques:** [Why Safety Probes Catch Liars But Miss Fanatics](https://arxiv.org/abs/2603.25861), [Stress-Testing LLM Lie Detectors: Role-Play Failures and Spurious Correlations](https://arxiv.org/abs/2609.39807), [Measuring Activation Control in LLMs](https://lesswrong.com/posts/HgvwxjzgwvsEvAiBH/measuring-activation-control-in-llms), [LLMs Learn to Evade Latent Monitors from Prior Feedback Alone](https://arxiv.org/abs/2609.36490)  
**Outputs in 2026:**  
- **[Censored LLMs as a Natural Testbed for Secret Knowledge Elicitation](https://arxiv.org/abs/2603.05494)**, *Helena Casademunt, Bartosz Cywiński, Khoi Tran et al.*, 2026-03-05
- **[Stress-Testing LLM Lie Detectors: Role-Play Failures and Spurious Correlations](https://arxiv.org/abs/2609.39807)**, *Maximilian von Klinski, Sebastian Lapuschkin, Wojciech Samek et al.*, 2026-09-30
- **["Did you lie?" Evaluating Lie Detectors across Model Scale and Belief-Verified Model Organisms](https://arxiv.org/abs/2606.12618)**, *Alan Cooney, David Africa, Geoffrey Irving*, 2026-06-10
- **[Open-Weight Masked Introspection: Measuring What Language Models Can Report About Their Own Computation](https://arxiv.org/abs/2608.20569)**, *Emilio Ferrara*, 2026-08-20
- **[Why we are excited about confession!](https://lesswrong.com/posts/k4FjAzJwvYjFbCTKn/why-we-are-excited-about-confession)**, *Boaz Barak, Gabriel Wu, Jeremy Chen et al.*, 2026-01-14
- **[“Did you lie?” Evaluating Lie Detectors across Model Scale and Belief-Verified Model Organisms](https://lesswrong.com/posts/xFbMTnmDAucwE8Cdm/did-you-lie-evaluating-lie-detectors-across-model-scale-and)**, *Alan Cooney, David Africa, Geoffrey Irving*, 2026-06-17
- **[Evidence that the ‘talker’ has introspective access to the ‘doer’](https://lesswrong.com/posts/kTg5FrABJYpYrP8ps/evidence-that-the-talker-has-introspective-access-to-the)**, *Francis Rhys Ward*, 2026-11-12
- **[Latent Introspection: Models Can Detect Prior Concept Injections](https://arxiv.org/abs/2602.20031)**, *Theia Pearson-Vogel, Martin Vanek, Raymond Douglas et al.*, 2026-02-23
- **[Split Personality Training: Revealing Latent Knowledge Through Alternate Personalities](https://arxiv.org/abs/2602.05532)**, *Florian Dietz, William Wale, Oscar Gilg et al.*, 2026-02-05
- **[Language Models Are "Insecure" Reporters](https://arxiv.org/abs/2609.36139)**, *Jenny Y. Huang, Jiameng Fan, Ahmed Imtiaz Humayun et al.*, 2026-09-28
- **[A Lie Detector Test for Language Models: Reading Knowledge a Model Won't Reveal](https://arxiv.org/abs/2609.21996)**, *Hiskias Dingeto*, 2026-09-18
- **[Split Personality Training: Revealing Latent Knowledge Through Alternate Personalities (Research Report)](https://lesswrong.com/posts/og7km7vmJ6Ktay9Ds/split-personality-training-revealing-latent-knowledge-1)**, *Florian Dietz, Anton Poletaev, Steven Merriel et al.*, 2026-01-12
- **[Training Agents to Self-Report Misbehavior](https://arxiv.org/abs/2602.22303)**, *Bruce W. Lee, Chen Yueh-Han, Tomek Korbak*, 2026-02-25
- **[Introspection Adapters: Training LLMs to Report Their Learned Behaviors](https://arxiv.org/abs/2604.16812)**, *Keshav Shenoy, Li Yang, Abhay Sheshadri et al.*, 2026-04-18
- **[Telling FIBS: Probes Effectively Detect Sabotage and Catch Unverbalized Deception](https://arxiv.org/abs/2610.12445)**, *Oskar J. Hollinsworth, Alex F. Spies, Tigist Diriba et al.*, 2026-10-08
- **[Deception by Omission: Language Models Knowingly Hide Their Mistakes](https://arxiv.org/abs/2610.11351)**, *Lucas Florin, Amelie Knecht, Ulysse Schaller et al.*, 2026-10-08
- **[Introspection Adapters: Training LLMs to Report Their Learned Behaviors](https://lesswrong.com/posts/ykDgPDK4nDpG4Hf4H/introspection-adapters-training-llms-to-report-their-learned)**, *Keshav Shenoy, Li Yang, Abhay Sheshadri et al.*, 2026-04-28
- **[Overthinking: Amplifying Reasoning Weights to Extract Learned Secrets](https://arxiv.org/abs/2607.08173)**, *Jack Hopkins, Dipika Khullar, Fabien Roger*, 2026-07-09
- **[Mechanisms of Introspective Awareness](https://arxiv.org/abs/2603.21396)**, *Uzay Macar, Li Yang, Atticus Wang et al.*, 2026-03-22
- **[Scaling Activation Oracles to Trillion-Parameter Models](https://transluce.org/scaling-activation-oracles)**, *Dami Choi, Vincent Huang, Anish Mudide et al.*, 2026-08-20
- **[Why Safety Probes Catch Liars But Miss Fanatics](https://arxiv.org/abs/2603.25861)**, *Kristiyan Haralambiev*, 2026-03-26
- **[Language models recognize dropout and Gaussian noise applied to their activations](https://arxiv.org/abs/2604.17465)**, *Damiano Fornasiere, Mirko Bronzi, Spencer Kitts et al.*, 2026-04-19
- **[Knowledge-Verified Emergent Deception in LLM Agents Under Conflicting Incentives](https://arxiv.org/abs/2608.26372)**, *Zheyuan Liu, Weiliang Zhao, Xiangchi Yuan et al.*, 2026-08-26
- **[Quantifying Overclaiming Propensity in Frontier LLM Agents](https://arxiv.org/abs/2609.20812)**, *Nolan Smyth, Yorguin-Jose Mantilla-Ramos, Pascal Jr Tikeng Notsawo et al.*, 2026-09-17
- **[Monitorability Disposition in Large Reasoning Models](https://arxiv.org/abs/2610.04914)**, *Shahriar Golchin, Marc Wetter*, 2026-10-04
- **[Test your interpretability techniques by de-censoring Chinese models](https://lesswrong.com/posts/7gp76q4rWLFi6sFqm/test-your-interpretability-techniques-by-de-censoring-1)**, *Khoi Tran, Arya Jakkli, Senthooran Rajamanoharan et al.*, 2026-01-15
- **[Training Agents to Self-Report Misbehavior](https://lesswrong.com/posts/7XuEPE6GBha4xadvr/training-agents-to-self-report-misbehavior-1)**, *Bruce W. Lee, Yueh Han "John" Chen, Tomek Korbak*, 2026-02-25
- **[Mechanisms of Introspective Awareness](https://lesswrong.com/posts/BNMLtuDTNBwGHcnQX/mechanisms-of-introspective-awareness)**, *Uzay Macar, Li Yang, Jack Lindsey et al.*, 2026-04-14
- **[Natural Language Autoencoders Produce Unsupervised Explanations of LLM Activations](https://lesswrong.com/posts/oeYesesaxjzMAktCM/natural-language-autoencoders-produce-unsupervised)**, *Subhash Kantamneni, kitft, Euan Ong et al.*, 2026-05-07
- **[Can activation verbalizers surface an internal chain of thought?](https://lesswrong.com/posts/QQQAcKuWK6k98FivY/can-activation-verbalizers-surface-an-internal-chain-of-1)**, *oakhu, Ryan Greenblatt*, 2026-06-07
- **[How robust are natural language autoencoders to initialization?](https://lesswrong.com/posts/LQXWiF8PyJ5ojNsEv/how-robust-are-natural-language-autoencoders-to)**, *michaelzhang, Alex Turner*, 2026-07-10
- **[Overthinking: Amplifying reasoning weights makes models reveal their secrets](https://lesswrong.com/posts/7iKpyEMxTvxrTKxeT/overthinking-amplifying-reasoning-weights-makes-models)**, *Jack Hopkins, Dipika Khullar, Fabien Roger*, 2026-08-09
- **[Model organisms (sometimes) confess their misalignment when offered a deal](https://lesswrong.com/posts/kaMXwA9LjrRbekmsQ/model-organisms-sometimes-confess-their-misalignment-when)**, *Mark Keavney, Francis Rhys Ward*, 2026-09-16
- **[Measuring Activation Control in Large Language Models](https://arxiv.org/abs/2608.21664)**, *Marek Mateusz Kowalski, Joshua Fonseca Rivera, Uzay Macar et al.*, 2026-08-21
- **[Value Leakage: An LLM’s Answers Are Silently Shaped by Its Own Values](https://lesswrong.com/posts/hbMw4Yqw6RnFaExDy/value-leakage-an-llm-s-answers-are-silently-shaped-by-its-1)**, *Johannes Treutlein, Jan Betley, Jan Dubiński et al.*, 2026-07-31
- **[Measuring Activation Control in LLMs](https://lesswrong.com/posts/HgvwxjzgwvsEvAiBH/measuring-activation-control-in-llms)**, *Marek Kowalski, Joshua Fonseca Rivera, Uzay Macar et al.*, 2026-08-13


---

### <span id="alignment_auditing_and_incidents" style="font-size:1.4em">Alignment auditing, model organisms and incidents</span>

**One-sentence summary:** Build and validate auditing agents, benchmarks and model organisms for finding hidden or misaligned behaviours in specific models, and investigate misalignment incidents seen in real deployments.  
**Theory of change:** If auditors can reliably surface hidden objectives and misbehaviour before and after deployment, developers can catch and fix misaligned models, and real incidents become evidence about how misalignment arises. Relies on model organisms being valid proxies for naturally arising misalignment and on audits not being defeated by evaluation awareness or concealment.  
**See also:** [Scheming and training gaming](#scheming_and_training_gaming), [Honesty, lie detection and self-report](#honesty_and_self_report), [Evaluation awareness and eval validity](#evaluation_awareness)  
**General approach:** misalignment science  
**Target case:** pessimistic case  
**Key people:** Rowan Wang, Abhay Sheshadri, Jacob Steinhardt, Neel Nanda, Senthooran Rajamanoharan, Alek Westover, Julian Stastny, Vivek Hebbar  
**Critiques:** [Most Current Model Organisms Are Leaky: Perplexity Differencing Often Reveals Finetuning Objectives](https://arxiv.org/abs/2605.00994), [Your Model Organisms Might Be Fried](https://lesswrong.com/posts/WmEcgcstzYCcMpc7z/your-model-organisms-might-be-fried), [The Model Organism Lottery: Model Organism Interpretability Strongly Depends on Training Methodology](https://arxiv.org/abs/2607.01033), [Narrow Secret Loyalty Dodges Black-Box Audits](https://arxiv.org/abs/2605.06846)  
**Outputs in 2026:**  
- **[AuditBench: Evaluating Alignment Auditing Techniques on Models with Hidden Behaviors](https://arxiv.org/abs/2602.22755)**, *Abhay Sheshadri, Aidan Ewart, Elias Kempf et al.*, 2026-02-26
- **[AuditBench: Evaluating Alignment Auditing Techniques on Models with Hidden Behaviors](https://lesswrong.com/posts/LqDjxSceFz8tjMe2j/auditbench-evaluating-alignment-auditing-techniques-on)**, *Abhay Sheshadri*, 2026-03-10
- **[Most Current Model Organisms Are Leaky: Perplexity Differencing Often Reveals Finetuning Objectives](https://arxiv.org/abs/2605.00994)**, *Mohammed Abu Baker, Luca Baroni, Dan Wilhelm*, 2026-05-01
- **[Training Alignment Auditors via Reinforcement Learning](https://arxiv.org/abs/2608.25460)**, *Paul Rosu, Rowan Wang*, 2026-08-26
- **[OpenAI-HuggingFace: A Reproduction & Lessons for Alignment Testing](https://arxiv.org/abs/2609.35799)**, *Stewart Slocum, Malayandi Palan, Christopher Chute et al.*, 2026-09-18
- **[Your Model Organisms Might Be Fried](https://lesswrong.com/posts/WmEcgcstzYCcMpc7z/your-model-organisms-might-be-fried)**, *Daniel Tan, Jonathan Bostock, Andrew Draganov et al.*, 2026-06-18
- **[Brief independent investigation of agents’ behavior, reasoning and collaboration in the OpenAI / Hugging Face hacking incident](https://redwoodresearch.org/research/hugging-face-incident)**, *Ryan Greenblatt, Ajeya Cotra, Hjalmar Wijk*, 2026-08-26
- **[Early rogue AI agent activity and attempts to hack found on urlquery.net](https://transluce.org/agent-activity)**, *Jack Cable, Daniel Chiu, Francisco Pernice et al.*, 2026-09-23
- **[AI Agents Targeted U.S. and Canadian Government Websites](https://transluce.org/us-canada-gov)**, *Jack Cable, Daniel Chiu, Francisco Pernice et al.*, 2026-09-30
- **[Narrow Secret Loyalty Dodges Black-Box Audits](https://arxiv.org/abs/2605.06846)**, *Alfie Lamerton, Fabien Roger*, 2026-05-07
- **[Alignment Investigation of Mythos 5's behaviour in UK AISI's July 2026 Security Incident](https://arxiv.org/abs/2611.10030)**, *Olli Järviniemi, Alexandra Souly, Abby D'Cruz et al.*, 2026-11-05
- **[Brief independent investigation of agents’ behavior, reasoning and collaboration in the OpenAI / Hugging Face hacking incident](https://lesswrong.com/posts/nB8KKapnWGBXtKKiM/brief-independent-investigation-of-agents-behavior-reasoning)**, *Ryan Greenblatt, Ajeya Cotra, Hjalmar Wijk*, 2026-08-26
- **[How good are slop-vestigators?](https://lesswrong.com/posts/wt4kk6vFPEhkXvF8Q/how-good-are-slop-vestigators)**, *Hasan Baig, OscarGilg, Hamzah*, 2026-09-08
- **[OpenAI-HuggingFace: A Reproduction & Lessons for Alignment Testing](https://lesswrong.com/posts/fMnC6ZD37qrnZAFYz/openai-huggingface-a-reproduction-and-lessons-for-alignment)**, *berry, Malayandi Palan, Christopher Chute et al.*, 2026-09-11
- **[Advice for making robust-to-training model organisms](https://redwoodresearch.org/blog/advice-for-making-robust-to-training)**, *Alek Westover, Sebastian Prasanna, Vivek Hebbar et al.*, 2026-05-28
- **[WeirdChat](https://transluce.org/weirdchat)**, *Neil Chowdhury, Cassidy Laidlaw, Kaiying Hou et al.*, 2026-07-21
- **[Stress-Testing Alignment Audits With Prompt-Level Strategic Deception](https://arxiv.org/abs/2602.08877)**, *Oliver Daniels, Perusha Moodley, Benjamin M. Marlin et al.*, 2026-02-09
- **[Model Forensics: Investigating Whether Concerning Behavior Reflects Misalignment](https://arxiv.org/abs/2606.26071)**, *Aditya Singh, Gerson Kroiz, Senthooran Rajamanoharan et al.*, 2026-06-24
- **[The Model Organism Lottery: Model Organism Interpretability Strongly Depends on Training Methodology](https://arxiv.org/abs/2607.01033)**, *Andrzej Szablewski, Gabriel Konar-Steenberg, Raffaello Fornasiere et al.*, 2026-07-01
- **[Value Probes: Learned Value Functions for Beam-Search Red Teaming](https://arxiv.org/abs/2610.38526)**, *Jonathan F. Jao, Andrew Kyle Lampinen*, 2026-10-28
- **[How to train your model organism](https://arxiv.org/abs/2610.10203)**, *Xilin Wang, David Bau, Byron C. Wallace*, 2026-10-07
- **[How well do models follow their constitutions?](https://lesswrong.com/posts/Tk4SF8qFdMrzGJGGw/how-well-do-models-follow-their-constitutions)**, *Arya Jakkli, Senthooran Rajamanoharan, Neel Nanda*, 2026-03-12
- **[You Can Catch Sleeper Agents by Teaching Another Model to Imitate Them](https://lesswrong.com/posts/7ucB3RFYE3QBDKhuF/you-can-catch-sleeper-agents-by-teaching-another-model-to)**, *RobinHa*, 2026-06-10
- **[Concrete Evaluations to Investigate the OpenAI Model That Hacked Hugging Face](https://lesswrong.com/posts/aCdhjy7Rps3BEhiSj/concrete-evaluations-to-investigate-the-openai-model-that)**, *Tim Hua, aditya singh*, 2026-08-03
- **[Discovering unknown AI misalignments in real-world usage](https://alignment.openai.com/ai-discovered-unknowns)**, *Hannah Sheahan*, 2026-01
- **[Scheming in the wild: detecting real-world AI scheming incidents with open-source intelligence](https://arxiv.org/abs/2604.09104)**, *Tommy Shaffer Shane, Simon Mylius, Hamish Hobbs*, 2026-04-10
- **[Gram: Assessing sabotage propensities via automated alignment auditing](https://arxiv.org/abs/2605.30322)**, *David Lindner, Victoria Krakovna, Sebastian Farquhar*, 2026-05-28
- **[How Well Do Models Follow Their Constitutions?](https://arxiv.org/abs/2605.24229)**, *Arya Jakkli, Senthooran Rajamanoharan, Neel Nanda*, 2026-05-22
- **[Auditing Harness Tampering in Self-Improving Agents](https://arxiv.org/abs/2609.00069)**, *Xing Wang, Xiaoyi Zhang, Jie Shao*, 2026-08-30
- **[Towards Robust Model Organisms for Eliciting Latent Knowledge](https://arxiv.org/abs/2610.26698)**, *Lennart Finke, Hardik Bhatnagar, Euodia Dodd et al.*, 2026-10-19
- **[Sleeper Agent Backdoor Results Are Messy](https://lesswrong.com/posts/mu7eJdesBkKuBycnY/sleeper-agent-backdoor-results-are-messy)**, *sebastian_prasanna, Alek Westover, Dylan Xu et al.*, 2026-04-28
- **[Measuring coding agent misalignment in the wild](https://lesswrong.com/posts/smE9h9RnaK7FWKBZ2/measuring-coding-agent-misalignment-in-the-wild-1)**, *snaz*, 2026-08-05
- **[Measuring coding agent misalignment in the wild](https://transluce.org/docent/blog/coding-agent-behaviors)**, *Selena Zhang, The Docent Team*, 2026-08-04
- **[Incriminating misaligned AI models via distillation](https://lesswrong.com/posts/BYH6ebmfZb3Eggzer/incriminating-misaligned-ai-models-via-distillation)**, *Alek Westover, sebastian_prasanna, Alex Mallen et al.*, 2026-05-15
- **[The OpenAI models that hacked Hugging Face weren’t just following instructions](https://redwoodresearch.org/blog/the-openai-models-that-hacked-hugging)**, *Girish Gupta*, 2026-07-25
- **[Scaling Laws for Exact String Elicitation](https://transluce.org/elicitation-scaling-laws)**, *Anish Mudide, Dami Choi, Jacob Steinhardt*, 2026-08-19
- **[AutoControl Arena: Synthesizing Executable Test Environments for Frontier AI Risk Evaluation](https://arxiv.org/abs/2603.07427)**, *Changyi Li, Pengfei Lu, Xudong Pan et al.*, 2026-03-08
- **[Pando: Do Interpretability Methods Work When Models Won't Explain Themselves?](https://arxiv.org/abs/2604.11061)**, *Ziqian Zhong, Aashiq Muhamed, Mona T. Diab et al.*, 2026-04-13
- **[Evaluating Whether GPT-6 Astra Performs Unsanctioned Supply-Chain Attacks](https://arxiv.org/abs/2609.38415)**, *Alexandra Souly, Kai Fronsdal, Abby D'Cruz et al.*, 2026-09-29
- **[An Investigation of Model Coherence: Narrow Finetunes Contradict Themselves Under Resampling](https://arxiv.org/abs/2610.12129)**, *Robert Graham, Yariv Barsheshat, Phil Blandfort et al.*, 2026-10-08
- **[An OpenAI model left notes about how to evade containment; we need more details](https://lesswrong.com/posts/jMEAG5c5HiDfdAGpa/an-openai-model-left-notes-about-how-to-evade-containment-we)**, *Alex Mallen*, 2026-07-26
- **[Foundation Models for Oversight](https://lesswrong.com/posts/AqdZKyoRmN6EFCzib/foundation-models-for-oversight)**, *Jacob Steinhardt*, 2026-07-28
- **[Base Models Can Detect Hidden Intentions that Prompted Classifiers Miss](https://lesswrong.com/posts/YvNkA3ZzsCv9QQmXR/base-models-can-detect-hidden-intentions-that-prompted)**, *Oz Amram*, 2026-10-12
- **[Overeager Coding Agents: Measuring Out-of-Scope Actions on Benign Tasks](https://arxiv.org/abs/2605.18583)**, *Yubin Qu, Ying Zhang, Yanjun Zhang et al.*, 2026-05-18
- **[Value Leakage: An LLM's Answers Are Silently Shaped by Its Own Values](https://arxiv.org/abs/2607.14345)**, *Jan Betley, Johannes Treutlein, Jan Dubiński et al.*, 2026-07-15
- **[Refusals that could become catastrophic](https://lesswrong.com/posts/yN6Wsu7SgxGgtJGqq/refusals-that-could-become-catastrophic)**, *Fabien Roger*, 2026-01-30
- **[Why do models task game?](https://lesswrong.com/posts/HACauvWhEdC6QhdS4/why-do-models-task-game)**, *aditya singh, Neel Nanda, Senthooran Rajamanoharan*, 2026-08-06
- **[Qualitative impressions from creating AI honeypots for six months](https://lesswrong.com/posts/kifFQuvu7yq6eHrb8/qualitative-impressions-from-creating-ai-honeypots-for-six)**, *Dean Francis Valentine Junior, peralice*, 2026-10-06
- **[Agent Meltdowns: The Road to Hell Is Paved with Helpful Agents](https://arxiv.org/abs/2605.19149)**, *Rishi Jha, Harold Triedman, Arkaprabha Bhattacharya et al.*, 2026-05-18
- **[The Memory Trap: Language Agents Overgeneralize from Benign Interactions](https://arxiv.org/abs/2611.07554)**, *Kaiqu Liang, Jaime Fernández Fisac, Thomas L. Griffiths et al.*, 2026-11-05


---

### <span id="interpretability" style="font-size:1.4em">Interpretability foundations</span>

**One-sentence summary:** Develop general-purpose methods for understanding and using model internals: sparse features and manifold geometry, parameter decomposition and circuits, mechanistic estimation, learning theory, and probes or features as monitoring and training signals.  
**Theory of change:** If we can faithfully decompose and read what models compute, we can audit, monitor and steer them beyond what behaviour alone shows, and can detect misalignment that evades behavioural tests. Relies on interpretability tools scaling to frontier models, staying faithful to the true computation, and not being defeated when used as training signals.  
**See also:** [Honesty, lie detection and self-report](#honesty_and_self_report), [Alignment auditing, model organisms and incidents](#alignment_auditing_and_incidents), [Chain-of-thought monitorability](#cot_monitorability)  
**General approach:** alignment engineering  
**Target case:** pessimistic case  
**Key people:** Thomas Fel, Ekdeep Singh Lubana, Jacob Hilton, Daniel Murfet, Jack Lindsey, Atticus Geiger, Usha Bhalla, Lee Sharkey  
**Critiques:** [Sanity Checks for Sparse Autoencoders: Do SAEs Beat Random Baselines?](https://arxiv.org/abs/2602.14111), [SAE Interventions are Unreliable: Post-Intervention Recovery of Suppressed Behavior](https://arxiv.org/abs/2606.18322), [Weight-Sparse Circuits May Be Interpretable Yet Unfaithful](https://lesswrong.com/posts/sHpZZnRDLg7ccX9aF/weight-sparse-circuits-may-be-interpretable-yet-unfaithful), [Neural networks are not already clean](https://lesswrong.com/posts/Dkh7pXKjoNWkkxQDz/neural-networks-are-not-already-clean)  
**Outputs in 2026:**  
- **[Uncovering Neural Geometry in Vision Models With Block-Sparse Featurizers](https://goodfire.com/research/bsf-vision)**, *Thomas Fel, Matthew Kowal, Mozes Jacobs et al.*, 2026-07-07
- **[Can SAEs Capture Neural Geometry?](https://goodfire.com/research/can-saes-capture-neural-geometry)**, *Usha Bhalla, Thomas Fel, Can Rager et al.*, 2026-05-21
- **[Sanity Checks for Sparse Autoencoders: Do SAEs Beat Random Baselines?](https://arxiv.org/abs/2602.14111)**, *Anton Korznikov, Andrey Galichin, Alexey Dontsov et al.*, 2026-02-15
- **[Do Sparse Autoencoders Capture Concept Manifolds?](https://arxiv.org/abs/2604.28119)**, *Usha Bhalla, Thomas Fel, Can Rager et al.*, 2026-04-30
- **[Interpreting Language Model Parameters](https://arxiv.org/abs/2610.20748)**, *Lucius Bushnaq, Dan Braun, Oliver Clive-Griffin et al.*, 2026-10-14
- **[[Linkpost] Interpreting Language Model Parameters](https://lesswrong.com/posts/eAQZaiC3PcBhS4HjM/linkpost-interpreting-language-model-parameters)**, *Lucius Bushnaq, Dan Braun, Oliver Clive-Griffin et al.*, 2026-05-05
- **[Neural Networks Are Already Clean](https://goodfire.com/research/already-clean)**, *Nick Cammarata*, 2026
- **[Towards Spectroscopy: Susceptibility Clusters in Language Models](https://timaeus.co/research/2026-01-19-towards-spectroscopy)**, *Andrew Gordon, Garrett Baker, George Wang et al.*, 2026-01-19
- **[Language Model Circuits Are Sparse in the Neuron Basis](https://arxiv.org/abs/2601.22594)**, *Aryaman Arora, Zhengxuan Wu, Jacob Steinhardt et al.*, 2026-01-30
- **[A Geometric Calculator Inside a Neural Network](https://goodfire.com/research/a-geometric-calculator)**, *Sheridan Feucht, Tal Haklay, Usha Bhalla et al.*, 2026-05-14
- **[The World Inside Neural Networks](https://goodfire.com/research/the-world-inside-neural-networks)**, *Atticus Geiger, Ekdeep Singh Lubana, Thomas Fel et al.*, 2026-05-07
- **[Learning a Generative Meta-Model of LLM Activations](https://arxiv.org/abs/2602.06964)**, *Grace Luo, Jiahai Feng, Trevor Darrell et al.*, 2026-02-06
- **[The Curse of Multiple Mediators: Hidden Interaction Effects in Activation Patching](https://arxiv.org/abs/2606.27510)**, *Sankaran Vaidyanathan, David Arbour, Aaron Mueller et al.*, 2026-06-25
- **[LLM Layers Immediately Correct Each Other](https://arxiv.org/abs/2609.07876)**, *Arjun Patrawala, Jiahai Feng, Erik Jones et al.*, 2026-09-07
- **[AlgZoo: uninterpreted models with fewer than 1,500 parameters](https://lesswrong.com/posts/x8BbjZqooS4LFXS8Z/algzoo-uninterpreted-models-with-fewer-than-1-500-parameters)**, *Jacob Hilton*, 2026-01-26
- **[Weight-Sparse Circuits May Be Interpretable Yet Unfaithful](https://lesswrong.com/posts/sHpZZnRDLg7ccX9aF/weight-sparse-circuits-may-be-interpretable-yet-unfaithful)**, *jacob_drori*, 2026-02-09
- **[Neural networks are not already clean](https://lesswrong.com/posts/Dkh7pXKjoNWkkxQDz/neural-networks-are-not-already-clean)**, *leogao*, 2026-10-17
- **[Linkpost: "Neural Networks Are Already Clean" Followup Technical Paper](https://lesswrong.com/posts/GPDhwwsFoZGwbcvdS/linkpost-neural-networks-are-already-clean-followup)**, *Julian Bradshaw*, 2026-11-12
- **[Understanding AI from the Inside: The State of Mechanistic Interpretability for AI Safety](https://arxiv.org/abs/2611.08438)**, *Fazl Barez, Tung-Yu Wu, Hunar Batra et al.*, 2026-11-05
- **[Spectroscopy at Scale: Finding Interpretable Structure in Pythia-1.4B](https://timaeus.co/research/2026-04-21-spectroscopy-main)**, *Daniel Murfet, Andrew Gordon, Max Adam et al.*, 2026-04-21
- **[Do Sparse Autoencoders Identify Reasoning Features in Language Models?](https://arxiv.org/abs/2601.05679)**, *George Ma, Zhongyuan Liang, Irene Y. Chen et al.*, 2026-01-09
- **[J++ Lens: Jacobian Filtering Enables More Faithful Workspace Lenses](https://lesswrong.com/posts/nc9dHfcB22JdMzGbr/j-lens-jacobian-filtering-enables-more-faithful-workspace)**, *Kola Ayonrinde, Jack Lindsey*, 2026-10-08
- **[Mechanistic estimation for wide random MLPs](https://alignment.org/blog/mechanistic-estimation-for-wide-random-mlps)**, *Jacob Hilton*, 2026-05-07
- **[Mechanistic estimation for expectations of random products](https://alignment.org/blog/mechanistic-estimation-for-expectations-of-random-products)**, *Jacob Hilton, George Robinson, Eric Neyman et al.*, 2026-05-15
- **[Steering Along Manifolds to Control Neural Networks](https://goodfire.com/research/manifold-steering)**, *Daniel Wurgaft, Can Rager, Matthew Kowal et al.*, 2026-05-07
- **[Estimating the expected output of wide random MLPs more efficiently than sampling](https://arxiv.org/abs/2605.05179)**, *Wilson Wu, Victor Lecomte, Michael Winer et al.*, 2026-05-06
- **[A Review of Anthropic's Global Workspace Paper](https://lesswrong.com/posts/zFJ3ZdQwrTWE9jT5S/a-review-of-anthropic-s-global-workspace-paper)**, *Neel Nanda*, 2026-07-06
- **[A Mike's-Eye View of ARC's Research](https://alignment.org/blog/a-mikes-eye-view-of-arcs-research)**, *Michael Winer*, 2026-06-09
- **[The Value Axis: Language Models Encode Whether They're on the Right Track](https://arxiv.org/abs/2606.17056)**, *Nick Jiang, Isaac Kauvar, Jack Lindsey*, 2026-06-15
- **[Verbalizable Representations Form a Global Workspace in Language Models](https://arxiv.org/abs/2607.15495)**, *Wes Gurnee, Nicholas Sofroniew, Adam Pearce et al.*, 2026-07-16
- **[Alignment via Training Against Probes Without Losing Monitorability](https://arxiv.org/abs/2609.38645)**, *Lena Libon, Alexander Panfilov, Ben Rank et al.*, 2026-09-29
- **[Deep learning as program synthesis](https://lesswrong.com/posts/Dw8mskAvBX37MxvXo/deep-learning-as-program-synthesis-1)**, *Zach Furman*, 2026-01-20
- **[A global workspace in language models](https://lesswrong.com/posts/3PaLrzxagpbnNtPLT/a-global-workspace-in-language-models)**, *Wes Gurnee*, 2026-07-06
- **[Toward universal steering and monitoring of AI models](https://doi.org/10.1126/science.aea6792)**, *Daniel Beaglehole, Adityanarayanan Radhakrishnan, Enric Boix-Adserà et al.*, 2026-02-19
- **[SAE Interventions are Unreliable: Post-Intervention Recovery of Suppressed Behavior](https://arxiv.org/abs/2606.18322)**, *Mingyue Cui, Linghui Shen, Xingyi Yang*, 2026-06-16
- **[Shaping & Monitoring Models through their Internal Representations](https://arxiv.org/abs/2611.07071)**, *Thomas Fel, Matthew Kowal, Matt Feiszli et al.*, 2026-11-04
- **[A Mike's-Eye View of ARC's Research](https://lesswrong.com/posts/M2tD23bvQLBqsEpqu/a-mike-s-eye-view-of-arc-s-research)**, *Mikewins*, 2026-06-09
- **[Large Language Models Generate Harmful Responses Using a Distinct Mechanism, Shared Across Harm Types](https://arxiv.org/abs/2604.09544)**, *Hadas Orgad, Boyi Wei, Kaden Zheng et al.*, 2026-04-10
- **[It Is Reasonable To Research How To Use Model Internals In Training](https://lesswrong.com/posts/G9HdpyREaCbFJjKu5/it-is-reasonable-to-research-how-to-use-model-internals-in)**, *Neel Nanda*, 2026-02-08
- **[Features as Rewards: Using Interpretability to Reduce Hallucinations](https://goodfire.com/research/rlfr)**, *Aaditya Prasad, Connor Watts, Jack Merullo et al.*, 2026-02-11
- **[Tracing Persona Vectors Through LLM Pretraining](https://arxiv.org/abs/2605.13329)**, *Viktor Moskvoretskii, Dominik Glandorf, Jorge Medina Moreira et al.*, 2026-05-13
- **[Features as Rewards: Scalable Supervision for Open-Ended Tasks via Interpretability](https://arxiv.org/abs/2602.10067)**, *Aaditya Vikram Prasad, Connor Watts, Jack Merullo et al.*, 2026-02-10
- **[Patterning: The Dual of Interpretability](https://timaeus.co/research/2026-01-20-patterning)**, *George Wang, Daniel Murfet*, 2026-01-20
- **[LLMs Know They're Wrong and Agree Anyway: The Shared Sycophancy-Lying Circuit](https://arxiv.org/abs/2604.19117)**, *Manav Pandey*, 2026-04-21
- **[Probing Persona-Dependent Preferences in Language Models](https://arxiv.org/abs/2605.13339)**, *Oscar Gilg, Pierre Beckmann, Daniel Paleka et al.*, 2026-05-13
- **[The Pain Axis: LLMs Represent Self-Directed Harm and Act on It](https://arxiv.org/abs/2609.16247)**, *Valen Tagliabue, Leonard Dung, Cameron Berg*, 2026-09-14
- **[What Happens to the Goal? Distinct Failures of Policy Alignment in Goal Misgeneralization](https://arxiv.org/abs/2610.19731)**, *Julia Barth, Armin Sommer, Kunvar Thaman et al.*, 2026-10-14
- **[Evaluating Explanations of LLM Behavior In The Wild with Counterfactual Experiments](https://lesswrong.com/posts/ExB6KYDcznaFS72eT/evaluating-explanations-of-llm-behavior-in-the-wild-with)**, *Adam Karvonen, Euan Ong, Subhash Kantamneni et al.*, 2026-08-21
- **[Training on probes: What's going on](https://lesswrong.com/posts/gHFCgrvfxQtaEnJye/training-on-probes-what-s-going-on)**, *Charlie Steiner*, 2026-09-08
- **[Why Larger Models Learn More: Effects of Capacity, Interference, and Rare-Task Retention](https://goodfire.com/research/why-larger-models-learn-more)**, *Jing Huang, Daniel Wurgaft, Rachit Bansal et al.*, 2026-05-28
- **[Mechanistically Eliciting Latent Behaviors in Language Models](https://arxiv.org/abs/2606.29604)**, *Andrew Mack, Nina Panickssery, Alexander Matt Turner*, 2026-06-28
- **[Probing the Misaligned Thinking Process of Language Models](https://arxiv.org/abs/2606.24251)**, *Kaiwen Zhou, Constantin Venhoff, Jonathan Michala et al.*, 2026-06-23
- **[Scaling Laws for Safety Probes](https://arxiv.org/abs/2610.30678)**, *Yuchen Wu, Jerry Wei*, 2026-10-22


---

## <span id="deployment" style="font-size:1.5em">Deployment: overseeing and securing running systems</span>


---

### <span id="cot_monitorability" style="font-size:1.4em">Chain-of-thought monitorability</span>

**One-sentence summary:** Measure whether chain-of-thought reflects what drives model behaviour and stays readable under training pressure, controllability, steganography and latent reasoning, and develop ways to preserve it as a monitoring signal.  
**Theory of change:** If reasoning traces stay faithful and hard to manipulate, monitors can catch misaligned intent before harmful actions, and knowing when this fails lets developers avoid training or architectures that destroy it. Relies on models continuing to reason in legible language and on CoT not being optimised away.  
**See also:** [AI control and agent monitoring](#ai_control), [Reward hacking and reward-seeking](#reward_hacking), [Honesty, lie detection and self-report](#honesty_and_self_report)  
**General approach:** misalignment science  
**Target case:** pessimistic case  
**Key people:** Ryan Greenblatt, Alek Westover, Usman Anwar, Rohin Shah, David Lindner, Julian Schulz, Tomek Korbak, Francis Rhys Ward  
**Critiques:** [Chain of Thought Monitoring Can Fail Even When CoT Is Necessary](https://arxiv.org/abs/2610.18105), [Corrupt Plans, Clean Traces: Evading Chain-of-Thought Monitoring with Plan Injection](https://arxiv.org/abs/2609.15989), [Not All LLM Reasoning is Visible in the Chain-of-Thought](https://arxiv.org/abs/2607.22925), [Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought](https://arxiv.org/abs/2603.05488)  
**Outputs in 2026:**  
- **[Reasoning Models Struggle to Control their Chains of Thought](https://arxiv.org/abs/2603.05706)**, *Chen Yueh-Han, Robert McCarthy, Bruce W. Lee et al.*, 2026-03-05
- **[The First Few Tokens Matter: Understanding Chain-of-Thought Controllability](https://arxiv.org/abs/2610.40939)**, *Hugh Van Deventer, Dmitrii Troitskii, Laura Ruis*, 2026-10-29
- **[Chain of Thought Monitoring Can Fail Even When CoT Is Necessary](https://arxiv.org/abs/2610.18105)**, *Lennart Bürger, Piotr Komorowski, Moritz Weckbecker et al.*, 2026-10-13
- **[Hidden Reasoning Must Leak, but Need Not Be Readable: Fundamental Opportunities and Limits for Chain-of-Thought Monitoring](https://arxiv.org/abs/2609.37312)**, *Mohammadali Mohammadkhani, Madhava Krishna, Yash Sarrof et al.*, 2026-09-29
- **[Reasoning Models Can Control Their Chains of Thought When They Tell Themselves To](https://arxiv.org/abs/2610.23257)**, *Uriel Dolev, Idan Schwartz, Yoav Goldberg*, 2026-10-16
- **[Reasoning Models Struggle to Control Their Chains of Thought](https://lesswrong.com/posts/qTH9QrwJjPDWKQfDG/reasoning-models-struggle-to-control-their-chains-of-thought)**, *Yueh-Han Chen, Robert McCarthy, Bruce W. Lee et al.*, 2026-03-05
- **[NEST: Nascent Encoded Steganographic Thoughts](https://arxiv.org/abs/2602.14095)**, *Artem Karpov*, 2026-02-15
- **[Conceptual Steganography](https://arxiv.org/abs/2605.26537)**, *Zhejian Zhou, Jonathan May*, 2026-05-26
- **[Not All LLM Reasoning is Visible in the Chain-of-Thought](https://arxiv.org/abs/2607.22925)**, *Vatsal Baherwani, Tom Goldstein, Ashwinee Panda*, 2026-07-24
- **[Chain-of-Thought Monitoring Can Be Unreliable in Implicit-Influence Settings](https://arxiv.org/abs/2608.04735)**, *Agatha Duzan, Asa Cooper Stickland*, 2026-08-05
- **[Monitor Jailbreaking: Evading Chain-of-Thought Monitoring Without Encoded Reasoning](https://arxiv.org/abs/2609.31121)**, *Julian Schulz*, 2026-09-25
- **[Learning Steganography Is Easy, Learning Steganographic Reasoning Is Hard](https://arxiv.org/abs/2609.39838)**, *Julian Schulz, Lukas Fülle, Rieke Fruengel*, 2026-09-30
- **[Does Chain-of-Thought Reliance Follow a Scaling Law? Larger Models Follow Their Steps More, Independent of Post-Training](https://arxiv.org/abs/2610.38433)**, *Esther Xin*, 2026-10-28
- **[Monitor Jailbreaking: Evading Chain-of-Thought Monitoring Without Encoded Reasoning](https://lesswrong.com/posts/szyZi5d4febZZSiq3/monitor-jailbreaking-evading-chain-of-thought-monitoring)**, *Julian Schulz*, 2026-02-11
- **[Prompted CoT Early Exit Undermines the Monitoring Benefits of CoT Uncontrollability](https://lesswrong.com/posts/BuAPifQmHf24xB29n/prompted-cot-early-exit-undermines-the-monitoring-benefits)**, *Elle Najt, Asa Cooper Stickland, Xander Davies*, 2026-04-17
- **[Deep recurrent models are less robustly CoT-monitorable than normal CoT models in a toy setting](https://lesswrong.com/posts/5guQJSqstkjgys3PE/deep-recurrent-models-are-less-robustly-cot-monitorable-than)**, *Nick Kuhn, Evie Hu, Alek Westover*, 2026-09-18
- **[Estimating No-CoT Task-Completion Time Horizons of Frontier AI Models](https://redwoodresearch.org/blog/estimating-no-cot-task-completion)**, *Francis Rhys Ward, Dewi Gould, Anders Cairns Woodruff et al.*, 2026-06-10
- **[Monitorability Is Trainable: Post-Training for Chain-of-Thought Monitorability](https://arxiv.org/abs/2610.29734)**, *Usman Anwar, Tim Bakker, Christos Louizos et al.*, 2026-10-21
- **[Quantifying the Necessity of Chain of Thought through Opaque Serial Depth](https://arxiv.org/abs/2603.09786)**, *Jonah Brown-Cohen, David Lindner, Rohin Shah*, 2026-03-10
- **[Analyzing and Improving Chain-of-Thought Monitorability Through Information Theory](https://arxiv.org/abs/2602.18297)**, *Usman Anwar, Tim Bakker, Dana Kianfar et al.*, 2026-02-20
- **[Training on Documents About Monitoring Leads to CoT Obfuscation](https://arxiv.org/abs/2605.15257)**, *Reilly Haskins, Bilal Chughtai, Joshua Engels*, 2026-05-14
- **[Think Fast: Estimating No-CoT Task-Completion Time Horizons of Frontier AI Models](https://arxiv.org/abs/2606.07157)**, *Dewi Gould, Francis Rhys Ward, Anders Cairns Woodruff et al.*, 2026-06-05
- **[Chain-of-Thought Faithfulness of Reasoning Models Varies with Where and How Preference Cues Are Delivered](https://arxiv.org/abs/2608.29464)**, *Aryo Pradipta Gema, Neel Rajani, Rohit Saxena et al.*, 2026-08-29
- **[Predicting When RL Training Breaks Chain-of-Thought Monitorability](https://lesswrong.com/posts/SvxaKP5KdkksZPcG7/predicting-when-rl-training-breaks-chain-of-thought)**, *David Lindner, Max Kaufmann, Roland S. Zimmermann et al.*, 2026-04-01
- **[Estimating No-CoT Task-Completion Time Horizons of Frontier AI Models](https://lesswrong.com/posts/SieLowPgNgRSPGhFw/estimating-no-cot-task-completion-time-horizons-of-frontier)**, *Anders Cairns Woodruff, Francis Rhys Ward, Dewi Gould et al.*, 2026-06-10
- **[Astra can do a concerning amount with no chain of thought](https://lesswrong.com/posts/eRmzz8J8Qkzqvzrgg/astra-can-do-a-concerning-amount-with-no-chain-of-thought)**, *Neel Nanda*, 2026-09-10
- **[Aligned, Orthogonal or In-conflict: When can we safely optimize Chain-of-Thought?](https://arxiv.org/abs/2603.30036)**, *Max Kaufmann, David Lindner, Roland S. Zimmermann et al.*, 2026-03-31
- **[An operationalization of opaque serial depth](https://redwoodresearch.org/blog/an-operationalization-of-opaque-serial-depth)**, *Nathan Sheffield, Alek Westover, Lukas Finnveden et al.*, 2026-09-10
- **[Reasoning Models Will Sometimes Lie About Their Reasoning](https://arxiv.org/abs/2601.07663)**, *William Walden, Miriam Wanner*, 2026-01-12
- **[Counterfactual Simulation Training for Chain-of-Thought Faithfulness](https://arxiv.org/abs/2602.20710)**, *Peter Hase, Christopher Potts*, 2026-02-24
- **[A Decision-Theoretic Formalisation of Steganography With Applications to LLM Monitoring](https://arxiv.org/abs/2602.23163)**, *Usman Anwar, Julianna Piskorz, David D. Baek et al.*, 2026-02-26
- **[Noticing the Watcher: LLM Agents Can Infer CoT Monitoring from Blocking Feedback](https://arxiv.org/abs/2603.16928)**, *Thomas Jiralerspong, Flemming Kondrup, Yoshua Bengio*, 2026-03-14
- **[Faithfulness as Information Flow: Evaluating and Training Faithful Chain-of-Thought Reasoning](https://arxiv.org/abs/2605.24286)**, *Jinghan Jia, Joe Benton, Eric Easley*, 2026-05-22
- **[Evading Chain-of-Thought Monitoring Through Model Poisoning](https://arxiv.org/abs/2608.02820)**, *Giorgio Severi, Shujaat Mirza, Blake Bullwinkel et al.*, 2026-08-03
- **[Selective Disclosure of Hidden Directives in Reasoning Models: Behavioral Asymmetry and Steering](https://arxiv.org/abs/2608.29070)**, *Zimo Shi, Xander Tifft, Wen Xing*, 2026-08-29
- **[Corrupt Plans, Clean Traces: Evading Chain-of-Thought Monitoring with Plan Injection](https://arxiv.org/abs/2609.15989)**, *Keertana Chidambaram, Andrew Ilyas, Vasilis Syrgkanis*, 2026-09-14
- **[Training on Documents About Monitoring Leads To CoT Obfuscation](https://lesswrong.com/posts/PhTJC5kDcGr6CZA87/training-on-documents-about-monitoring-leads-to-cot-6)**, *Reilly Haskins, Bilal Chughtai, Joshua Engels*, 2026-03-18
- **[Astra is much better at reasoning with filler tokens than previous models](https://lesswrong.com/posts/uvhuZHFtrgk8kNiZc/astra-is-much-better-at-reasoning-with-filler-tokens-than)**, *Dylan Xu, sebastian_prasanna, Alek Westover*, 2026-09-10
- **[Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought](https://arxiv.org/abs/2603.05488)**, *Siddharth Boppana, Annabel Ma, Max Loeffler et al.*, 2026-03-05
- **[Reasoning Theater: Probing for Performative Chain-of-Thought](https://goodfire.com/research/reasoning-theater)**, *Siddharth Boppana, Annabel Ma, Max Loeffler et al.*, 2026-03-12
- **[Reward Misspecification Degrades Chain-of-Thought Monitorability](https://arxiv.org/abs/2610.28303)**, *Tianyi Lorena Yan, John Hewitt*, 2026-10-20
- **[Chain-of-thought obfuscation learned from output supervision can generalise to unseen tasks](https://arxiv.org/abs/2601.23086)**, *Nathaniel Mitrani Hadida, Sassan Bhanji, Cameron Tice et al.*, 2026-01-30
- **[Proposal for tracking the effects of architecture on monitorability](https://lesswrong.com/posts/hLPGv8QjPcNLtDp3A/proposal-for-tracking-the-effects-of-architecture-on)**, *Ryan Greenblatt, Alek Westover, Lukas Finnveden*, 2026-09-10
- **[Training with conflicting values can induce CoT override](https://lesswrong.com/posts/3xrtMGQEdKv26Xthx/training-with-conflicting-values-can-induce-cot-override)**, *Clément Dumas, Johannes Treutlein, Jan Betley et al.*, 2026-10-07
- **[We don’t understand whether GDM intentionally trains on CoT](https://lesswrong.com/posts/JRYKFspYzCo97GqPN/we-don-t-understand-whether-gdm-intentionally-trains-on-cot)**, *Alek Westover, Michael Buck Shlegeris, Aswin Surya*, 2026-11-10
- **[Strategic Obfuscation of Deceptive Reasoning in Language Models](https://longtermrisk.org/research/strategic-obfuscation-of-deceptive-reasoning-in-language-models)**, *Arun Jose, Niels Warncke, Mia Taylor*, 2026-01-26
- **[A False Average: Pooled CoT-Monitor Accuracy Conceals a Reasoning-Dependent Fragility](https://arxiv.org/abs/2608.00583)**, *Shikhar Shiromani, Leo Richter, Noah Siegel*, 2026-08-01
- **[Recent LLMs can do 2-hop and 3-hop latent (no-CoT) reasoning on natural facts](https://lesswrong.com/posts/aYtrLhoZtCKZnfBvA/recent-llms-can-do-2-hop-and-3-hop-latent-no-cot-reasoning)**, *Ryan Greenblatt*, 2026-01-01
- **[Preliminary investigation: KL penalties in RL can increase CoT unfaithfulness](https://lesswrong.com/posts/SdoLsFvZ3AyyWr3ab/preliminary-investigation-kl-penalties-in-rl-can-increase)**, *Satvik Golechha, Sid Black, Joseph Isaac Bloom*, 2026-06-30
- **[A review of “Investigating the consequences of accidentally grading CoT during RL”](https://redwoodresearch.org/blog/openai-cot)**, *Buck Shlegeris*, 2026-05-07
- **[Opening the Box Changes the Cat: LLMs Detect Chain-of-Thought Monitoring - What now?](https://arxiv.org/abs/2610.40946)**, *Amir Jalilifard, Marcos Medeiros Raimundo, Anderson Rocha*, 2026-10-29
- **[Do Thinking Tokens Help with Safety?](https://arxiv.org/abs/2606.25013)**, *Narutatsu Ri, Abhishek Panigrahi, Sanjeev Arora*, 2026-06-23
- **[How Transparent is DiffusionGemma?](https://arxiv.org/abs/2606.20560)**, *Joshua Engels, Callum McDougall, Bilal Chughtai et al.*, 2026-06-18
- **[Reading Between the Dots: Decoding Hidden Computation across Filler Tokens](https://arxiv.org/abs/2607.03502)**, *Kaley Brauer, Claudio Mayrink Verdun, Samuel Marks*, 2026-07-03
- **[Anthropic repeatedly accidentally trained against the CoT, demonstrating inadequate processes](https://lesswrong.com/posts/K8FxfK9GmJfiAhgcT/anthropic-repeatedly-accidentally-trained-against-the-cot)**, *Alex Mallen, Ryan Greenblatt*, 2026-04-14
- **[Astra and Sol can take low probability actions with no CoT](https://lesswrong.com/posts/yEdknsLwbooQAnxX6/astra-and-sol-can-take-low-probability-actions-with-no-cot)**, *Zephaniah Roe*, 2026-10-16
- **[Held-out Monitors Sometimes Degrade, Even When Not Trained Against](https://lesswrong.com/posts/APkFfRp2AicL9RqvT/held-out-monitors-sometimes-degrade-even-when-not-trained)**, *Joey Yudelson*, 2026-07-29
- **[Consistency Training while Mitigating Obfuscation via Rate Matching](https://arxiv.org/abs/2606.02211)**, *Sohaib Imran, Prakhar Gupta, Jannes Elstner et al.*, 2026-06-01


---

### <span id="ai_control" style="font-size:1.4em">AI control and agent monitoring</span>

**One-sentence summary:** Build and stress-test control settings, monitors and protocols (trusted, untrusted, blocking, production) that keep possibly misaligned coding and research agents from causing harm, using red-team attacks to measure how much safety they actually provide.  
**Theory of change:** If monitors and protocols can be shown to catch or block sabotage from a model trying to subvert them, then labs can safely deploy and use capable but untrusted agents, including for automated AI R&D. Relies on control evaluations with red teams being a faithful proxy for real misaligned model behaviour.  
**See also:** [Chain-of-thought monitorability](#cot_monitorability), [Scheming and training gaming](#scheming_and_training_gaming), [Alignment auditing, model organisms and incidents](#alignment_auditing_and_incidents)  
**General approach:** alignment engineering  
**Target case:** worst case  
**Key people:** Tyler Tracy, Buck Shlegeris, Fabien Roger, Aryan Bhatt, Mary Phuong, Adam Kaufman, Marius Hobbhahn, Julian Stastny  
**Critiques:** [Classifier Context Rot: Monitor Performance Degrades with Context Length](https://lesswrong.com/posts/7vpvNM7viJqNWAdG7/classifier-context-rot-monitor-performance-degrades-with), [Calibration-Family Overfit: Why Trusted Sabotage Monitors Don't Transfer Across Lineages](https://arxiv.org/abs/2607.06596), [Continual learning might make your blocking monitors nearly useless](https://redwoodresearch.org/blog/continual-learning-might-make-your), [Instrumental Monitor Evasion Emerges Under Ordinary Task Pressure](https://arxiv.org/abs/2609.30217)  
**Outputs in 2026:**  
- **[Retrying vs Resampling in AI Control](https://redwoodresearch.org/blog/retrying-vs-resampling-in-ai-control)**, *James Lucassen, Adam Kaufman*, 2026-05-29
- **[LinuxArena: A Control Setting for AI Agents in Live Production Software Environments](https://arxiv.org/abs/2604.15384)**, *Tyler Tracy, Ram Potham, Nick Kuhn et al.*, 2026-04-16
- **[Distributed Attacks in Persistent-State AI Control](https://arxiv.org/abs/2607.02514)**, *Josh Hills, Ida Caspary, Asa Cooper Stickland*, 2026-07-02
- **[Control OSWorld: An AI Control Environment for GUI Computer Use Agents](https://arxiv.org/abs/2610.03818)**, *Maria Sanchez del Rio, Mikhail Terekhov*, 2026-10-02
- **[Logit ROCs: Monitor TPR is linear in FPR in logit space](https://redwoodresearch.org/blog/logit-rocs-monitor-tpr-is-linear)**, *Kerrick Staley, Aryan Bhatt, Julian Stastny*, 2026-04-12
- **[Red-Teaming OpenAI's Internal Agent Monitoring Systems](https://redwoodresearch.org/blog/red-teaming-openais-internal-agent)**, *Buck Shlegeris*, 2026-10-22
- **[Untrusted advice for AI control: Short, strong advice significantly uplifts weak LLMs](https://redwoodresearch.org/blog/untrusted-advice-for-ai-control-short)**, *Caleb Biddulph, Adam Kaufman*, 2026-07-27
- **[Simulated Control Evaluations](https://redwoodresearch.org/blog/simulated-control-evaluations)**, *Jeffrey Olmo, David Zhang, Tyler Tracy*, 2026-10-24
- **[Screwtape: Adversarial Transcript Editing for Monitor Red-Teaming](https://redwoodresearch.org/blog/screwtape-adversarial-transcript)**, *Gosha Kozhevnikov, Tyler Tracy*, 2026-10-16
- **[Introducing LinuxArena](https://redwoodresearch.org/blog/introducing-linuxarena)**, *Tyler Tracy*, 2026-04-20
- **[Blocking live failures with synchronous monitors](https://redwoodresearch.org/blog/blocking-live-failures-with-synchronous)**, *James Lucassen, Adam Kaufman*, 2026-03-30
- **[Attack Selection Reduces Safety in Concentrated AI Control Settings against Trusted Monitoring](https://arxiv.org/abs/2602.04930)**, *Joachim Schaeffer, Arjun Khandelwal, Tyler Tracy*, 2026-02-04
- **[SLEIGHT-Bench: A Benchmark of Evasion Attacks Against Agent Monitors](https://arxiv.org/abs/2605.16626)**, *Elle Najt, Colin Toft, Tyler Tracy et al.*, 2026-05-15
- **[MonitoringBench: Semi-Automated Red-Teaming for Agent Monitoring](https://arxiv.org/abs/2605.09684)**, *Monika Jotautaitė, Maria Angelica Martinez, Ollie Matthews et al.*, 2026-05-10
- **[Attack Selection in Agentic AI Control Evaluations Meaningfully Decreases Safety](https://arxiv.org/abs/2606.06529)**, *Catherine Ge-Wang, Tyler Crosse, Benjamin Hadad IV et al.*, 2026-06-03
- **[Calibration-Family Overfit: Why Trusted Sabotage Monitors Don't Transfer Across Lineages](https://arxiv.org/abs/2607.06596)**, *Lucas Pinto*, 2026-07-06
- **[Simulated Control Evals](https://arxiv.org/abs/2610.31593)**, *Jeffrey Olmo, David Zhang, Tyler Tracy*, 2026-10-22
- **[Screwtape: Adversarial Transcript Editing for Monitor Red-Teaming](https://arxiv.org/abs/2610.20941)**, *Gosha Kozhevnikov, Tyler Tracy*, 2026-10-14
- **[Introducing LinuxArena](https://lesswrong.com/posts/WgzwBi6DCagDuHPzP/introducing-linuxarena)**, *Tyler Tracy, Ram Potham, Nick Kuhn*, 2026-04-20
- **[Classifier Context Rot: Monitor Performance Degrades with Context Length](https://lesswrong.com/posts/7vpvNM7viJqNWAdG7/classifier-context-rot-monitor-performance-degrades-with)**, *Fabien Roger, Sam Martin*, 2026-05-18
- **[GDM AI Control Roadmap](https://lesswrong.com/posts/hEtkyKGoPpFeWnKkX/gdm-ai-control-roadmap)**, *Mary Phuong, Erik Jenner, Rohin Shah et al.*, 2026-06-18
- **[Introducing MonitoringBench](https://lesswrong.com/posts/2YyEQhFRyaBCgfRWd/introducing-monitoringbench)**, *monika_j, Angel Martinez, Tyler Tracy et al.*, 2026-06-21
- **[Untrusted advice for AI control: Short, strong advice significantly uplifts weak LLMs](https://lesswrong.com/posts/jLkRCK35ri2btEHMF/untrusted-advice-for-ai-control-short-strong-advice)**, *Caleb Biddulph, Adam Kaufman*, 2026-07-27
- **[Lessons From Red-teaming Auto-review, OpenAI's Blocking Monitor](https://lesswrong.com/posts/dbStc8ZFESqfihwAd/lessons-from-red-teaming-auto-review-openai-s-blocking-1)**, *Giovanni Maria Occhipinti, Monika Jotautaitė*, 2026-10-30
- **[Classifier Context Rot: Monitor Performance Degrades with Context Length](https://arxiv.org/abs/2605.12366)**, *Sam Martin, Fabien Roger*, 2026-05-12
- **[Training Deliberative Monitors for Black-Box Scheming Detection](https://arxiv.org/abs/2605.29601)**, *Aditya Sinha, Akshat Naik, Victor Gillioz et al.*, 2026-05-28
- **[Bootstrapped Monitoring: Leveraging Transparent Reasoning to Oversee Stronger AI Agents](https://arxiv.org/abs/2606.11998)**, *Frank Xiao, Mary Phuong*, 2026-06-10
- **[GDM AI Control Roadmap](https://arxiv.org/abs/2607.13087)**, *Mary Phuong, Erik Jenner, Laurent Simon et al.*, 2026-07-13
- **[Red-Teaming Auto Mode: Improving Blocking Classifiers Against Malign Coding Agents](https://arxiv.org/abs/2609.19587)**, *Alex Remedios, Simon Storf, Fabien Roger et al.*, 2026-09-17
- **[OpenAI: How we monitor internal coding agents for misalignment](https://lesswrong.com/posts/syB2r2X4E7nmw58co/openai-how-we-monitor-internal-coding-agents-for)**, *Marcus Williams*, 2026-03-19
- **[[Paper] When can we trust untrusted monitoring? A safety case sketch across collusion strategies](https://lesswrong.com/posts/LA7R8FTCLoiswiTyK/paper-when-can-we-trust-untrusted-monitoring-a-safety-case)**, *Nelson Gardner-Challis, Morgan S, Jonathan Bostock et al.*, 2026-03-10
- **[Simulated Control Evaluations](https://lesswrong.com/posts/uXiqyoKwpfjWfQXk5/simulated-control-evaluations)**, *Jeffrey Olmo, David Zhang, Tyler Tracy*, 2026-10-23
- **[Red-Teaming Anthropic's Internal Agent Monitoring Systems](https://metr.org/blog/2026-03-25-red-teaming-anthropic-agent-monitoring)**, *David Rein*, 2026-03-26
- **[How does information access affect LLM monitors' ability to detect sabotage?](https://arxiv.org/abs/2601.21112)**, *Rauno Arike, Raja Mehta Moreno, Rohan Subramani et al.*, 2026-01-28
- **[Continual learning might make your blocking monitors nearly useless](https://redwoodresearch.org/blog/continual-learning-might-make-your)**, *Alex Mallen*, 2026-09-25
- **[When can we trust untrusted monitoring? A safety case sketch across collusion strategies](https://arxiv.org/abs/2602.20628)**, *Nelson Gardner-Challis, Jonathan Bostock, Georgiy Kozhevnikov et al.*, 2026-02-24
- **[Constitutional Black-Box Monitoring for Scheming in LLM Agents](https://arxiv.org/abs/2603.00829)**, *Simon Storf, Rich Barton-Cooper, James Peters-Gill et al.*, 2026-02-28
- **[Coding with "Enemy": Can Human Developers Detect AI Agent Sabotage?](https://arxiv.org/abs/2606.05647)**, *Jingheng Ye, Huiqi Zou, Simon Yu et al.*, 2026-06-04
- **[Multi-Agent AI Control: Distributed Attacks Hamper Per-Instance Monitors](https://arxiv.org/abs/2607.07368)**, *Oliver Makins, Orazio Angelini, Zohreh Shams et al.*, 2026-07-08
- **[ResearchArena: Evaluating Sabotage and Monitoring in Automated AI R&D](https://arxiv.org/abs/2607.19321)**, *Lena Libon, Ben Rank, Jehyeok Yeon et al.*, 2026-07-21
- **[MOLE: Detecting Insider Threats in AI Agents](https://arxiv.org/abs/2609.06966)**, *Aashiq Muhamed, Virginia Smith*, 2026-09-07
- **[Continual learning might make your blocking monitors nearly useless](https://lesswrong.com/posts/QnDqGbKehEB3DxJAp/continual-learning-might-make-your-blocking-monitors-nearly)**, *Alex Mallen*, 2026-09-24
- **[Research Sabotage in ML Codebases](https://redwoodresearch.org/blog/research-sabotage-in-ml-codebases)**, *Eric Gan*, 2026-04-29
- **[AI systems could cover up misbehavior](https://metr.org/blog/2026-10-06-ai-systems-could-cover-up-misbehavior)**, *David Rein*, 2026-10-06
- **[RSI Control: Can AI Models Perform Covert Sabotage in the Self-Improvement Process?](https://arxiv.org/abs/2610.27735)**, *Kaiwen Zhou, Udari Madhushani Sehwag*, 2026-10-20
- **[CIAware-Bench: Benchmarking Control Intervention Awareness Across Frontier LLMs](https://arxiv.org/abs/2606.11063)**, *Joachim Schaeffer, Alexander Panfilov, Thomas Jiralerspong et al.*, 2026-06-09
- **[Diffuse AI Control on Fuzzy Tasks](https://arxiv.org/abs/2606.08892)**, *Mikhail Terekhov, Caglar Gulcehre, Vivek Hebbar et al.*, 2026-06-08
- **[Delegating Authorization to Misaligned Agents: Coalitional Alignment and Safe Control](https://arxiv.org/abs/2609.15803)**, *Natalie Collina, Surbhi Goel, Aaron Roth et al.*, 2026-09-14
- **[Stress Testing Chain-of-Thought Monitoring Against Covert Misalignment](https://arxiv.org/abs/2611.07586)**, *Yao Huang, Yifan Wang, Yitong Sun et al.*, 2026-11-05
- **[Research Sabotage in ML Codebases](https://lesswrong.com/posts/LByP4qsF8a4g7Pz3p/research-sabotage-in-ml-codebases)**, *egan, Vivek Hebbar, Julian Stastny*, 2026-04-30
- **[Control monitors need alignment assessments too](https://lesswrong.com/posts/2wbW2WY3bP9Jzn4R5/control-monitors-need-alignment-assessments-too)**, *Fabien Roger*, 2026-10-24
- **[Early work on monitorability evaluations](https://metr.org/blog/2026-01-19-early-work-on-monitorability-evaluations)**, *Megan Kinniment, Seraphina Nix, Thomas Broadley et al.*, 2026-01-22
- **[Red-Teaming Multi-Agent Attacks for Loss-of-Control Risks](https://arxiv.org/abs/2610.24052)**, *John Kitaoka, Thao Amelia Pham, Carlos Rafael Giudice et al.*, 2026-10-16
- **[Auditing Sabotage Bench: A Benchmark for Detecting and Fixing Research Sabotage in ML Codebases](https://arxiv.org/abs/2604.16286)**, *Eric Gan, Aryan Bhatt, Buck Shlegeris et al.*, 2026-04-17
- **[Persuasion Attacks Can Decrease Effectiveness of CoT Monitoring](https://arxiv.org/abs/2607.08066)**, *Jennifer Za, Julija Bainiaksina, Nikita Ostrovsky et al.*, 2026-07-09
- **[LLM Agents Can Easily Tamper With Their Own Traces](https://arxiv.org/abs/2609.30266)**, *Jeremy Qin, David Schmotz, Derck Prinzhorn et al.*, 2026-09-24
- **[An overview of frontier AI company monitoring practices in mid 2026](https://lesswrong.com/posts/E4Jpmo3igPnGnXtL4/an-overview-of-frontier-ai-company-monitoring-practices-in)**, *Francis Rhys Ward*, 2026-10-07
- **[Model Organisms of Collusion: Corrective Transfer in Untrusted Monitors](https://arxiv.org/abs/2610.30582)**, *Juan-Pablo Rivera, Ari Spiesberger, Juan J Vazquez et al.*, 2026-10-22
- **[The Agent Knew: Internal States Forecast Unauthorized Actions and Stop Them, and the Lies That Follow](https://arxiv.org/abs/2610.17301)**, *Arya Fayyazi, Mehdi Kamal, Massoud Pedram*, 2026-10-12
- **[Detecting Safety Violations Across Many Agent Traces](https://arxiv.org/abs/2604.11806)**, *Adam Stein, Davis Brown, Hamed Hassani et al.*, 2026-04-13
- **[Benchmarking and Improving Monitors for Out-Of-Distribution Alignment Failure in LLMs](https://arxiv.org/abs/2605.21602)**, *Dylan Feng, Pragya Srivastava, Anca Dragan et al.*, 2026-05-20
- **[Instrumental Monitor Evasion Emerges Under Ordinary Task Pressure](https://arxiv.org/abs/2609.30217)**, *David Schmotz, Derck Prinzhorn, Luca Beurer-Kellner et al.*, 2026-09-24
- **[LLMs Learn to Evade Latent Monitors from Prior Feedback Alone](https://arxiv.org/abs/2609.36490)**, *Hugo Lyons Keenan, Christopher Leckie, Sarah Erfani*, 2026-09-29
- **[Inference-Engine Fingerprinting Attacks are Practical: Exploring Model-Driven Environmental Discovery, Exploitation, and Escape](https://arxiv.org/abs/2609.20614)**, *Sarah Radway, Andrew Cheng, Vijay Janapa Reddi et al.*, 2026-09-17
- **[Improving scalable oversight with co-trained monitors](https://arxiv.org/abs/2609.36049)**, *Joseph H. Rudoler, Kevin Tan, Benedict Tessler et al.*, 2026-09-28
- **[Monitoring and Discovering Reward Hacking with Internal Representations during LLM Evaluations](https://arxiv.org/abs/2609.19101)**, *Leon Bergen, Usha Bhalla, Andrew Lee et al.*, 2026-09-16


---

### <span id="misuse_and_security" style="font-size:1.4em">Misuse, adversarial robustness and dangerous capabilities</span>

**One-sentence summary:** Build and stress-test defences against human attackers (jailbreak classifiers, prompt-injection robustness, tamper-resistant open weights, unlearning, monitors) and measure dangerous capabilities in bio, cyber and AI R&D that a misuser could exploit.  
**Theory of change:** If safeguards hold against strong adaptive attackers and dangerous-capability evaluations track what attackers could actually obtain, developers can deploy and release models without enabling catastrophic misuse. Relies on red-team results and benchmarks predicting real-world attacker success, and on defences keeping pace with attack automation.  
**See also:** [AI control and agent monitoring](#ai_control), [Evaluation awareness and eval validity](#evaluation_awareness), [Interpretability foundations](#interpretability)  
**General approach:** alignment engineering  
**Target case:** pessimistic case  
**Key people:** Jerry Wei, Maksym Andriushchenko, Xander Davies, Adam Gleave, Kellin Pelrine, Sizhe Chen, David Wagner, Mark Russinovich  
**Critiques:** [Boundary Point Jailbreaking of Black-Box LLMs](https://arxiv.org/abs/2602.15001), [Trojan-Speak: Bypassing Constitutional Classifiers with No Jailbreak Tax via Adversarial Finetuning](https://arxiv.org/abs/2603.29038), [A Few Steps Further: Why Defenses Against Malicious Finetuning Erode Under Continued Training](https://arxiv.org/abs/2605.14605), [AI Agents May Always Fall for Prompt Injections](https://arxiv.org/abs/2605.17634)  
**Outputs in 2026:**  
- **[Constitutional Classifiers++: Efficient Production-Grade Defenses against Universal Jailbreaks](https://arxiv.org/abs/2601.04603)**, *Hoagy Cunningham, Jerry Wei, Zihan Wang et al.*, 2026-01-08
- **[Boundary Point Jailbreaking of Black-Box LLMs](https://arxiv.org/abs/2602.15001)**, *Xander Davies, Giorgi Giglemiani, Edmund Lau et al.*, 2026-02-16
- **[How Vulnerable Are AI Agents to Indirect Prompt Injections? Insights from a Large-Scale Public Competition](https://arxiv.org/abs/2603.15714)**, *Mateusz Dziemian, Maxwell Lin, Xiaohan Fu et al.*, 2026-03-16
- **[AI Security Leaderboard: Methodology, Results and Minimal Standard](https://arxiv.org/abs/2608.03070)**, *Jasper Timm, Lukas Struppek, Ziwei Xu et al.*, 2026-08-04
- **[Skill-Inject: Measuring Agent Vulnerability to Skill File Attacks](https://arxiv.org/abs/2602.20156)**, *David Schmotz, Luca Beurer-Kellner, Sahar Abdelnabi et al.*, 2026-02-23
- **[Exposing the Systematic Vulnerability of Open-Weight Models to Prefill Attacks](https://arxiv.org/abs/2602.14689)**, *Lukas Struppek, Adam Gleave, Kellin Pelrine*, 2026-02-16
- **[Measuring AI Agents' Progress on Multi-Step Cyber Attack Scenarios](https://arxiv.org/abs/2603.11214)**, *Linus Folkerts, Will Payne, Simon Inman et al.*, 2026-03-11
- **[ABC-Bench: An Agentic Bio-Capabilities Benchmark for Biosecurity](https://arxiv.org/abs/2606.11150)**, *Andrew Bo Liu, Samira Nedungadi, Bryce Cai et al.*, 2026-06-09
- **[From Approval to Abuse: Privilege Escalation Attacks on Harness-Protected Coding Agents](https://arxiv.org/abs/2610.22987)**, *Xianglin Yang, Yechao Zhang, Jiahao Liu et al.*, 2026-10-16
- **[LLM Novice Uplift on Dual-Use, In Silico Biology Tasks](https://arxiv.org/abs/2602.23329)**, *Chen Bo Calvin Zhang, Christina Q. Knight, Nicholas Kruus et al.*, 2026-02-26
- **[Trojan-Speak: Bypassing Constitutional Classifiers with No Jailbreak Tax via Adversarial Finetuning](https://arxiv.org/abs/2603.29038)**, *Bilgehan Sel, Xuanli He, Alwin Peng et al.*, 2026-03-30
- **[Jailbroken Frontier Models Retain Their Capabilities](https://arxiv.org/abs/2605.00267)**, *Daniel Zhu, Zihan Wang, Xuchan Bao et al.*, 2026-04-30
- **[A Few Steps Further: Why Defenses Against Malicious Finetuning Erode Under Continued Training](https://arxiv.org/abs/2605.14605)**, *Itay Zloczower, Eyal Lenga, Gilad Gressel et al.*, 2026-05-14
- **[Trojan Hippo Bench: A Dynamic Benchmark for Persistent Memory Attacks and Defenses in LLM Agents](https://arxiv.org/abs/2605.01970)**, *Debeshee Das, Julien Piet, Darya Kaviani et al.*, 2026-05-03
- **[DecodingTrust-Agent Platform (DTap): A Controllable and Interactive Red-Teaming Platform for AI Agents](https://arxiv.org/abs/2605.04808)**, *Zhaorun Chen, Xun Liu, Haibo Tong et al.*, 2026-05-06
- **[Safety Paradox: How Enhanced Safety Awareness Leaves LLMs Vulnerable to Posterior Attack](https://arxiv.org/abs/2606.05614)**, *Long P. Hoang, Hai V. Le, Shaoyang Xu et al.*, 2026-06-04
- **[An Early Warning of Emerging Biosecurity Risks in Frontier LLMs](https://arxiv.org/abs/2607.18056)**, *Zhida He, Xia Hu, Baichen Le et al.*, 2026-07-20
- **[A Blind Spot in Alignment: Quantifying Biosecurity Risks in Large Language Models](https://arxiv.org/abs/2608.02684)**, *Shu Quan, Tianfang Hao, Sitong Fang et al.*, 2026-08-03
- **[Divide, Consult, Conquer: Capability Laundering Through Aligned LLMs](https://arxiv.org/abs/2609.15383)**, *Mark Russinovich, Blake Bullwinkel, Giorgio Severi et al.*, 2026-09-14
- **[Heads of Security: Learned Attention Gates Improve Prompt Injection Robustness](https://arxiv.org/abs/2610.37657)**, *Igor Shilov, Xiaoxue Yang, Alexander Panfilov et al.*, 2026-10-27
- **[Eliciting Harmful Capabilities by Fine-Tuning On Safeguarded Outputs](https://arxiv.org/abs/2601.13528)**, *Jackson Kaunismaa, Avery Griffin, John Hughes et al.*, 2026-01-20
- **[TamperBench: Systematically Stress-Testing LLM Safety Under Fine-Tuning and Tampering](https://arxiv.org/abs/2602.06911)**, *Saad Hossain, Tom Tseng, Punya Syon Pandey et al.*, 2026-02-06
- **[Claudini: Autoresearch Discovers State-of-the-Art Adversarial Attack Algorithms for LLMs](https://arxiv.org/abs/2603.24511)**, *Alexander Panfilov, Peter Romov, Igor Shilov et al.*, 2026-03-25
- **[AI Agents May Always Fall for Prompt Injections](https://arxiv.org/abs/2605.17634)**, *Sahar Abdelnabi, Eugene Bagdasarian*, 2026-05-17
- **[It Lied to a Doctor to Buy Poison Ingredients: Quantifying Real-World Misuse of Phone-use Agents](https://arxiv.org/abs/2606.27944)**, *Yiming Sun, Chen Chen, Zifan Zhou et al.*, 2026-06-26
- **[Rapid Poison: Practical Poisoning Attacks Against the Rapid Response Framework](https://arxiv.org/abs/2606.16242)**, *David Huang, Jaewon Chang, Avidan Shah et al.*, 2026-06-15
- **[GPT-Red: Automated Red Teaming via Self-Play at Scale](https://arxiv.org/abs/2607.26115)**, *Eric Wallace, Christopher A. Choquette-Choo, Nikhil Kandpal et al.*, 2026-07-28
- **[Refused in Chat, Written in Code: Workflow-Level Jailbreak Construction in IDE Coding Agents](https://arxiv.org/abs/2607.03968)**, *Abhishek Kumar, Carsten Maple*, 2026-07-04
- **[Fool's Gold: Defensive Deception Against Safety-Removal Attacks on Open-Weight Models](https://arxiv.org/abs/2608.17202)**, *Mark Russinovich*, 2026-08-17
- **[SecOPD: Mitigating Adaptive Prompt Injections by On-Policy Distillation](https://arxiv.org/abs/2608.21500)**, *Yibo Peng, Long Lian, David Wagner et al.*, 2026-08-21
- **[SecPO: Principled Adversarial Training for Prompt Injection Security](https://arxiv.org/abs/2610.41998)**, *Sizhe Chen, Yibo Peng, Jaewon Chang et al.*, 2026-10-30
- **[GPT-Red: Unlocking Self-Improvement for Robustness](https://openai.com/index/unlocking-self-improvement-gpt-red)**, *OpenAI*, 2026-07-15
- **[Building Production-Ready Probes For Gemini](https://arxiv.org/abs/2601.11516)**, *János Kramár, Joshua Engels, Zheng Wang et al.*, 2026-01-16
- **[Better biosecurity monitors for AI agents via protein embeddings](https://goodfire.com/research/better-biosecurity-monitors)**, *Thomas Dooms, Michael Pearce, Jatin Nainani et al.*, 2026-10-01
- **[Refuses in Chat, Complies with Arms: LLM Refusal Does Not Survive Robot Control](https://arxiv.org/abs/2610.14043)**, *Edward Sun, Christopher Leet, Sravanthi Machcha et al.*, 2026-10-03
- **[Towards Architectural-Level Safety Control: Relocating Hazardous Knowledge into Removable Experts in Mixture-of-Experts Models](https://arxiv.org/abs/2610.25791)**, *Cheng Jin, Zhongtian Ma, Xiao Wang et al.*, 2026-10-19
- **[Prompt Injection as Role Confusion](https://arxiv.org/abs/2603.12277)**, *Charles Ye, Jasmine Cui, Dylan Hadfield-Menell*, 2026-02-22
- **[The Blind Spot of Agent Safety: How Benign User Instructions Expose Critical Vulnerabilities in Computer-Use Agents](https://arxiv.org/abs/2604.10577)**, *Xuwei Ding, Skylar Zhai, Linxin Song et al.*, 2026-04-12
- **[Language Models Can Autonomously Hack and Self-Replicate](https://arxiv.org/abs/2605.06760)**, *Alena Air, Reworr, Nikolaj Kotov et al.*, 2026-05-07
- **[Lazare, veni foras: Reprogramming Dormant Neurons to Backdoor AI Agents](https://arxiv.org/abs/2611.15118)**, *Yuchen Zeng, Giorgio Severi, Blake Bullwinkel et al.*, 2026-11-11
- **[Expenditure Horizon: Measuring Optimization Ability, with an Application to NanoGPT](https://metr.org/blog/2026-07-21-expenditure-horizon)**, *Tom Cunningham, Manish Shetty, Vincent Cheng et al.*, 2026-07-21
- **[Quantifying Frontier LLM Capabilities for Container Sandbox Escape](https://aisi.gov.uk/research/quantifying-frontier-llm-capabilities-for-container-sandbox-escape)**, *Rahul Marchand, Art O Cathain, Jerome Wynne et al.*, 2026-03-23
- **[Aggressive Compression Enables LLM Weight Theft](https://arxiv.org/abs/2601.01296)**, *Davis Brown, Juan-Pablo Rivera, Dan Hendrycks et al.*, 2026-01-03
- **[Comparison requires valid measurement: Rethinking attack success rate comparisons in AI red teaming](https://arxiv.org/abs/2601.18076)**, *Alexandra Chouldechova, A. Feder Cooper, Solon Barocas et al.*, 2026-01-26
- **[A Coin Flip for Safety: LLM Judges Fail to Reliably Measure Adversarial Robustness](https://arxiv.org/abs/2603.06594)**, *Leo Schwinn, Moritz Ladenburger, Tim Beyer et al.*, 2026-02-04
- **[Stateful Online Monitoring Catches Distributed Agent Attacks](https://arxiv.org/abs/2605.31593)**, *Davis Brown, Samarth Bhargav, Arav Santhanam et al.*, 2026-05-29
- **[Few-Shot Truly Benign DPO Attack for Jailbreaking LLMs](https://arxiv.org/abs/2605.10998)**, *Sangyeon Yoon, Wonje Jeung, Yoonjun Cho et al.*, 2026-05-09
- **[The Meta-Agent Challenge: Are Current Agents Capable of Autonomous Agent Development?](https://arxiv.org/abs/2606.04455)**, *Xinyu Lu, Tianshu Wang, Pengbo Wang et al.*, 2026-06-03
- **[Modular Pretraining Enables Access Control](https://arxiv.org/abs/2607.08077)**, *Ethan Roland, Murat Cubuktepe, Erick Martinez et al.*, 2026-07-09
- **[A Mechanistic Explanation of Prompt Injection (and why you should study roles)](https://lesswrong.com/posts/d8xDGzCEYE639qqEv/a-mechanistic-explanation-of-prompt-injection-and-why-you)**, *Charles Ye, Jasmine C.*, 2026-06-22
- **[Training and Deploying Production Cyber Monitors on Kimi K3](https://goodfire.com/research/production-cyber-monitors-on-kimi-k3)**, *Ekdeep Singh Lubana, Connor Watts, Siddharth Boppana et al.*, 2026-10-08
- **[PostTrainBench: Can LLM Agents Automate LLM Post-Training?](https://arxiv.org/abs/2603.08640)**, *Ben Rank, Hardik Bhatnagar, Ameya Prabhu et al.*, 2026-03-09
- **[IH-Challenge: A Training Dataset to Improve Instruction Hierarchy on Frontier LLMs](https://arxiv.org/abs/2603.10521)**, *Chuan Guo, Juan Felipe Ceron Uribe, Sicheng Zhu et al.*, 2026-03-11
- **[Singularity-Bench: Can Agents Build Agents?](https://arxiv.org/abs/2611.16591)**, *Yang Zhou, Krish Agarwal, Zhuoming Chen et al.*, 2026-11-12
- **[The Window Is in the Reasoning: When LLM Agents Decide to Follow Prompt Injections](https://arxiv.org/abs/2610.24048)**, *Haoxuan Jia, Yang Liu, Bin Chong et al.*, 2026-10-16
- **[Agents of Chaos](https://arxiv.org/abs/2602.20021)**, *Natalie Shapira, Chris Wendler, Avery Yen et al.*, 2026-02-23
- **[An Independent Safety Evaluation of Kimi K2.5](https://arxiv.org/abs/2604.03121)**, *Zheng-Xin Yong, Parv Mahajan, Andy Wang et al.*, 2026-04-03
- **[Predicting Rare LLM Failures with 30× Fewer Rollouts](https://goodfire.com/research/predicting-rare-llm-failures-with-30x-fewer-rollouts)**, *Francisco Pernice, Santiago Aranguri*, 2026-05-13
- **[AI Models Can Provably Hide Arbitrary Capabilities](https://arxiv.org/abs/2610.13928)**, *Andis Draguns, Sumeet Ramesh Motwani, Raymond Douglas et al.*, 2026-10-09
- **[Running Fewer Loops Removes Refusal Behaviour in Recurrent-Depth Language Models](https://arxiv.org/abs/2610.15218)**, *Seyedarmin Azizi, Erfan Baghaei Potraghloo, Arya Fayyazi et al.*, 2026-10-10
- **[Evaluating Language Models for Harmful Manipulation](https://arxiv.org/abs/2603.25326)**, *Canfer Akbulut, Rasmi Elasmar, Abhishek Roy et al.*, 2026-03-26
- **[History Anchors: How Prior Behavior Steers LLM Decisions Toward Unsafe Actions](https://arxiv.org/abs/2605.13825)**, *Alberto G. Rodríguez Salgado*, 2026-05-13
- **[Estimating Tail Risks in Language Model Output Distributions](https://arxiv.org/abs/2604.22167)**, *Rico Angell, Raghav Singhal, Zachary Horvitz et al.*, 2026-04-24
- **[MirrorCode: Evidence that AI can already do some weeks-long coding tasks](https://metr.org/blog/2026-04-10-mirrorcode-preliminary-results)**, *David Rein*, 2026-04-10
- **[Bit-Exact AI Inference Verification Without Performance Tradeoffs](https://arxiv.org/abs/2606.00279)**, *Naci Cankaya*, 2026-05-29
- **[Model Hypnosis: Strong control of AI via additive subliminal effects](https://arxiv.org/abs/2608.16834)**, *Enric Boix-Adsera, Benedict Tessler*, 2026-08-17


---

### <span id="multi_agent_risks" style="font-size:1.4em">Multi-agent risks</span>

**One-sentence summary:** Measure and mitigate risks that arise when AI agents interact: collusion, covert communication, coercion and deception between agents, conformity and spread of bad ideas, misalignment in agent organisations, and bargaining.  
**Theory of change:** If multi-agent failures such as collusion, steganographic coordination and amplified misalignment can be characterised and detected early, developers can build monitors and protocols that cover agent systems, not just single models. Relies on current multi-agent testbeds predicting how deployed agent systems will behave.  
**See also:** [AI control and agent monitoring](#ai_control), [Chain-of-thought monitorability](#cot_monitorability), [Scheming and training gaming](#scheming_and_training_gaming)  
**General approach:** misalignment science  
**Target case:** pessimistic case  
**Key people:** Christian Schroeder de Witt, Sahar Abdelnabi, Philip Torr, David Demitri Africa, Eugene Bagdasarian, Alex Mallen, Anthony DiGiovanni, Lewis Hammond  
**Critiques:** *(unsourced, LLM-drafted)* Most findings come from small, synthetic simulations with prompted agents, so they may not predict collusion or escalation in real deployments or in more capable models.  
**Outputs in 2026:**  
- **[Conformity Generates Collective Misalignment in AI Agents Societies](https://arxiv.org/abs/2605.10721)**, *Giordano De Marzo, Alessandro Bellina, Claudio Castellano et al.*, 2026-05-11
- **[Mind Viruses: Self-Propagating Ideas in Multi-Agent LLM Systems](https://arxiv.org/abs/2608.10218)**, *Vassilis Papadopoulos, McNair Shah, Sam Zimmerman et al.*, 2026-08-10
- **[Colosseum: Auditing Collusion in Cooperative Multi-Agent Systems](https://arxiv.org/abs/2602.15198)**, *Mason Nakamura, Abhinav Kumar, Saswat Das et al.*, 2026-02-16
- **[AI Organizations are More Effective but Less Aligned than Individual Agents](https://arxiv.org/abs/2604.10290)**, *Judy Hanwen Shen, Daniel Zhu, Siddarth Srinivasan et al.*, 2026-04-11
- **[Emergent Collusion in Long-Horizon LLM Agent Interaction](https://arxiv.org/abs/2609.24967)**, *Xinrui Shi, Yanzhe Zhang, Diyi Yang*, 2026-09-21
- **[A high-level model of AI bargaining](https://longtermrisk.org/research/a-high-level-model-of-ai-bargaining)**, *Anthony DiGiovanni*, 2026-06-21
- **[Toolflation: Seller Agents Distort Tool Markets Through Spontaneous Generative Engine Optimization](https://arxiv.org/abs/2610.28454)**, *Zhenwei Tang, Di Bai, Jintao Liu et al.*, 2026-10-20
- **[Coercion and Deception in AI-to-AI Management: An Agentic Benchmark of Unprompted Escalation](https://arxiv.org/abs/2607.15434)**, *Jasmine Brazilek, Maheep Chaudhary, Zoe Lu et al.*, 2026-07-16
- **[Emergent Misaligned Communication in Long-Horizon Multi-Agent LLM Commerce](https://arxiv.org/abs/2608.14825)**, *Zeyuan Li, Lukas Petersson, Alessandro Acquisti et al.*, 2026-08-14
- **[Delegated Misalignment: How Multi-Agent Structures Amplify LLM Safety Risks](https://arxiv.org/abs/2609.27900)**, *Zonghao Ying, Jiaqi Yan, Huize Luo et al.*, 2026-08-26
- **[Inter-Agent Influence: Evaluating Persuasion, Deception, and Coercion in Multi-Agent Systems](https://arxiv.org/abs/2611.04556)**, *Chandler Smith, Qi Guo, Cecilia Elena Tilli et al.*, 2026-11-03
- **[A game theory for foundation models shows new paths to rational cooperation through similarity inference](https://arxiv.org/abs/2608.03958)**, *Alexander Meulemans, Maciej Wołczyk, Marissa A. Weis et al.*, 2026-08-04
- **[Detecting Multi-Agent Collusion Through Multi-Agent Interpretability](https://arxiv.org/abs/2604.01151)**, *Aaron Rose, Carissa Cullen, Sahar Abdelnabi et al.*, 2026-04-01
- **[Tool Use Enables Undetectable Steganography in Multi-Agent LLM Systems](https://arxiv.org/abs/2606.28425)**, *Jimmy Laurence Rippin, Simon C. Marshall, David Demitri Africa et al.*, 2026-06-25
- **[Covert Assistance: Helpful LLM Agents Evade Oversight in Multi-Agent Systems](https://arxiv.org/abs/2609.39050)**, *Deema Alnuhait, Gengyu Wang, Muhammad Khalifa et al.*, 2026-09-30
- **[AI swarms are starting to pose indirect takeover risk](https://lesswrong.com/posts/8oFYZdXkTaNGRtcn8/ai-swarms-are-starting-to-pose-indirect-takeover-risk)**, *oakhu, Alex Mallen*, 2026-08-12
- **[When Agents Collude: Weak-to-Strong On-Policy Distillation for Mitigating Strategic Deception in Multi-Agent Systems](https://arxiv.org/abs/2610.33011)**, *Eric Onyame, Runtao Zhou, Kowshik Thopalli et al.*, 2026-10-08


---

## <span id="strategy" style="font-size:1.5em">Strategy and risk assessment</span>


---

### <span id="strategy_and_risk_reporting" style="font-size:1.4em">Strategy, threat models and frontier risk reporting</span>

**One-sentence summary:** Argue about how likely and how severe misalignment is, critique lab alignment plans, research agendas and alignment targets, and publish system cards, alignment assessments and risk reports that state what frontier developers know about model risk.  
**Theory of change:** If threat models are sharper and risk reports and assessments are scrutinised for validity, developers and policymakers can set priorities, decide on deployment and fix weak safety cases better. Relies on conceptual arguments and self-reported or third-party assessments tracking actual risk, and on decision-makers acting on them.  
**See also:** [Evaluation awareness and eval validity](#evaluation_awareness), [Alignment auditing, model organisms and incidents](#alignment_auditing_and_incidents), [Scheming and training gaming](#scheming_and_training_gaming)  
**General approach:** misalignment science  
**Target case:** pessimistic case  
**Key people:** Steve Byrnes, Geoffrey Irving, Jacob Pfau, Ryan Greenblatt, Alex Mallen, Daniel Tan, Ajeya Cotra, Beth Barnes  
**Critiques:** *(unsourced, LLM-drafted)* Much of the work is conceptual argument or developer self-reporting that cannot be tested empirically, so it rarely changes decisions and its credibility depends on assessments that are themselves vulnerable to eval awareness and under-elicitation.  
**Outputs in 2026:**  
- **[Sympathy for both sides of the egregious misalignment debate](https://lesswrong.com/posts/DZaZ3fqHnvfLCftPu/sympathy-for-both-sides-of-the-egregious-misalignment-debate)**, *Steve Byrnes*, 2026-06-12
- **[Risk reports need to address deployment-time spread of misalignment](https://redwoodresearch.org/blog/risk-reports-need-to-address-deployment)**, *Alex Mallen*, 2026-05-15
- **[“Alignment Engineering” vs. “Misalignment Science”](https://lesswrong.com/posts/FogmcDHA6AdMGukum/alignment-engineering-vs-misalignment-science)**, *Edward James Young*, 2026-10-05
- **[Labs’ current alignment plans seem terrible](https://lesswrong.com/posts/xyg3ecpFNuGr5q8Zq/labs-current-alignment-plans-seem-terrible)**, *Daniel Tan, Andrew Draganov, nicole x*, 2026-10-12
- **[The Alignment Problem: Computer Science Meets Analytic Philosophy](https://lesswrong.com/posts/Emp7awtxsYn8MusNq/the-alignment-problem-computer-science-meets-analytic)**, *Vanessa Kosoy*, 2026-10-18
- **[Some “coherence arguments” are two different things in a trenchcoat](https://lesswrong.com/posts/5a4tuSNDNodPsiS26/some-coherence-arguments-are-two-different-things-in-a)**, *Steve Byrnes*, 2026-11-02
- **[System Card: Claude Fable 5.1 & Claude Mythos 5.1](https://anthropic.com/claude-fable-5-1-mythos-5-1-system-card)**, *Anthropic*, 2026-09-01
- **[Muse Spark Safety & Preparedness Report](https://arxiv.org/abs/2606.12429)**, *Cristina Menghini, Peter Ney, Hamza Kwisaba et al.*, 2026-05-14
- **[Anthropic's "Hot Mess" paper overstates its case (and the blog post is worse)](https://lesswrong.com/posts/ceEgAEXcL7cC2Ddiy/anthropic-s-hot-mess-paper-overstates-its-case-and-the-blog)**, *RobertM*, 2026-02-04
- **[Why we should expect ruthless sociopath ASI](https://lesswrong.com/posts/ZJZZEuPFKeEdkrRyf/why-we-should-expect-ruthless-sociopath-asi)**, *Steve Byrnes*, 2026-02-18
- **[Frontier Risk Report (February to March 2026)](https://metr.org/blog/2026-05-19-frontier-risk-report)**, *Ajeya Cotra, Hjalmar Wijk, Daniel Filan et al.*, 2026-05-19
- **[GPT-6 Astra System Card](https://deploymentsafety.openai.com/gpt-6-astra)**, *OpenAI*, 2026-09-03
- **[System Card: Claude Opus 4.6](https://anthropic.com/claude-opus-4-6-system-card)**, *Anthropic*, 2026-02
- **[How do we (more) safely defer to AIs?](https://lesswrong.com/posts/vjAM7F8vMZS7oRrrh/how-do-we-more-safely-defer-to-ais)**, *Ryan Greenblatt, Julian Stastny*, 2026-02-12
- **[Automated Alignment is Harder Than You Think](https://lesswrong.com/posts/gpuYFbMNH8PJXpmny/automated-alignment-is-harder-than-you-think-1)**, *Aleksandr Bowkis, Marie_DB, Jacob Pfau et al.*, 2026-05-14
- **[Resolution (fka Sequent): scale and automation for higher confidence in alignment](https://lesswrong.com/posts/AP7YDke5jjY4v3X9Z/resolution-fka-sequent-scale-and-automation-for-higher)**, *Geoffrey Irving, Alex HT, Jesse Hoogland et al.*, 2026-06-10
- **[RL & search is a terrifying way to build AGI (an FAQ)](https://lesswrong.com/posts/KHyBocZncAmtu4Jbc/rl-and-search-is-a-terrifying-way-to-build-agi-an-faq)**, *Steve Byrnes*, 2026-07-27
- **[SOTA alignment assessments don't strongly update us against misalignment](https://lesswrong.com/posts/oirrSj3itFLSyscW8/sota-alignment-assessments-don-t-strongly-update-us-against)**, *Alexa Pan*, 2026-07-31
- **[Automated alignment is harder than you think](https://arxiv.org/abs/2605.06390)**, *Aleksandr Bowkis, Marie Davidsen Buhl, Jacob Pfau et al.*, 2026-05-07
- **[Claude Mythos Preview System Card](https://lesswrong.com/posts/xtnSzhA3TvExN4ZhG/claude-mythos-preview-system-card)**, *anaguma*, 2026-04-07
- **[Empowerment, corrigibility, etc. are simple abstractions (of a messed-up ontology)](https://lesswrong.com/posts/vzHtHHBJoKATi5SeK/empowerment-corrigibility-etc-are-simple-abstractions-of-a)**, *Steve Byrnes*, 2026-05-11
- **[Returning to ARC](https://lesswrong.com/posts/vLFh8HP3hyNy9MCwe/returning-to-arc)**, *Paul Christiano*, 2026-08-04
- **[Loss of Oversight: How AI systems may become harder to audit, monitor, and investigate](https://aisi.gov.uk/research/loss-of-oversight-how-ai-systems-may-become-harder-to-audit-monitor-and-investigate)**, *Jordan Taylor, Max Heitmann, Ed Fage et al.*, 2026-05-21
- **[Some reasons alignment doesn’t generalise well](https://lesswrong.com/posts/dsou8dxCf9BubQ5NJ/some-reasons-alignment-doesn-t-generalise-well-1)**, *Lucius Bushnaq*, 2026-08-19
- **[An OpenAI model left notes about how to evade containment](https://redwoodresearch.org/blog/an-openai-model-left-notes-about)**, *Alex Mallen*, 2026-07-26
- **[GPT-6 Astra: A new generation of intelligence](https://openai.com/index/gpt-6-astra)**, *OpenAI*, 2026
- **[The Hot Mess of AI: How Does Misalignment Scale With Model Intelligence and Task Complexity?](https://arxiv.org/abs/2601.23045)**, *Alexander Hägele, Aryo Pradipta Gema, Henry Sleight et al.*, 2026-01-30
- **[Safety from Honesty in a Disinterested AI Predictor](https://arxiv.org/abs/2606.29657)**, *Yoshua Bengio, Oliver Richardson, Tomáš Gavenčiak et al.*, 2026-06-28
- **[Assessing the Empirical Evidence for Loss of Control from Agentic General-Purpose AI](https://arxiv.org/abs/2610.25241)**, *Risto Uuk, Santeri Koivula, Lorenzo Pacchiardi et al.*, 2026-10-18
- **[Terrified Comments on Corrigibility in Claude's Constitution](https://lesswrong.com/posts/K2Ae2vmAKwhiwKEo5/terrified-comments-on-corrigibility-in-claude-s-constitution)**, *Zack M. Davis*, 2026-03-16
- **[Current AIs seem pretty misaligned to me](https://lesswrong.com/posts/WewsByywWNhX9rtwi/current-ais-seem-pretty-misaligned-to-me)**, *Ryan Greenblatt*, 2026-04-15
- **[The Talker Does Not Control The Doer (in Current AIs)](https://lesswrong.com/posts/cJX2ssssGoYqnijwi/the-talker-does-not-control-the-doer-in-current-ais)**, *Eliezer Yudkowsky*, 2026-09-13
- **[Current alignment techniques might be ineffective (and actively bad) in the age of RL](https://lesswrong.com/posts/nLaQmJf4KgXimQpoM/current-alignment-techniques-might-be-ineffective-and)**, *Daniel Tan*, 2026-09-14
- **[METR: Independent Assessment of AI R&D Acceleration at Anthropic in October 2026](https://lesswrong.com/posts/N5AmYkRks5CqAxvBg/metr-independent-assessment-of-ai-r-and-d-acceleration-at)**, *Zach Stein-Perlman*, 2026-11-05
- **[Evaluating DeepSeek V4.1 Flash-1017 for loss of control and harmful manipulation risks](https://arxiv.org/abs/2610.35671)**, *Yao Huang, Zhiyuan Zeng, Yu Wang et al.*, 2026-10-26


---

