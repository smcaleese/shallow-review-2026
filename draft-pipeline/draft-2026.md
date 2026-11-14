> **How this taxonomy was made.** Unlike the earlier draft, which started from a human-written taxonomy, this one is
> derived from the data. Six methods in `taxonomy-discovery/` each grouped the same ~625 sources (arXiv and LessWrong
> shortlists, org pages, Safety Stack) into agendas: four bottom-up ones (an LLM proposing a taxonomy from all items,
> communities in an LLM nearest-neighbour graph and in an embedding graph, and clusters of a semantic map) and two
> baselines whose categories were written by a person (a hand-written taxonomy and one read off the semantic map); the
> earlier draft was not an input. Each method's taxonomy was scored by how reliably an LLM could re-file the entries
> into it. The 15 agendas below are the ones that several methods found independently, merged and named by reading
> their entries, so they are chosen to fit the sources rather than a prior view of the field (see
> `taxonomy-discovery/data-driven-taxonomy.md` and `recurring-agendas.md`). The 4 top-level areas (where the work acts on the model: training, inspection, deployment,
> strategy) are a judgement call on top of that; `taxonomy-discovery/organising-principles.md` lists alternatives.
> Every source was then classified into its best-fit agenda and scored for importance; each agenda shows its 10 most
> important entries, with duplicate versions of the same work (paper, LessWrong post, lab blog) merged into one line
> and the places this freed filled with the next most important distinct works.

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
**Kept per category:** at most the 10 most important (475 pruned)

**Total unique papers:** 150 (appearing 150 times across categories)

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
- **[Training a Misaligned Reward Seeker](https://lesswrong.com/posts/J76LZCC55RdHeqEhz/training-a-misaligned-reward-seeker)**, *Richard Qi, Benjamin Wright, Monte MacDiarmid et al.*, 2026-09-01
- **[Towards Understanding Score-Seeking in LLMs](https://arxiv.org/abs/2610.41014)**, *Aghyad Deeb, Ryan Greenblatt, Alex Mallen*, 2026-10-29 ([LW post](https://lesswrong.com/posts/CDMozTX7ShiqbFLrf/towards-understanding-score-seeking-in-llms-1))
- **[Measuring Reward-Seeking via Contrastive Belief Updates](https://arxiv.org/abs/2607.18966)**, *Axel Højmark, Jérémy Scheurer, Evgenia Nitishinskaya et al.*, 2026-07-21 ([LW post](https://lesswrong.com/posts/3HeauQLSHosRiwyto/measuring-reward-seeking-via-contrastive-belief-updates-1))
- **[Gradient Routing Localizes and Removes Unintended Behaviors in RL](https://arxiv.org/abs/2610.17062)**, *Shawn Hu, Jake Ward, Aria Wong et al.*, 2026-10-12 ([LW post](https://lesswrong.com/posts/mKJEBiuuxHKuCoTB6/gradient-routing-localizes-and-removes-unintended-behaviors))
- **[The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes](https://arxiv.org/abs/2602.15515)**, *Mohammad Taufeeque, Stefan Heimersheim, Adam Gleave et al.*, 2026-02-17
- **[Designing Effective Monitor-Based Interventions for Mitigating Reward Hacking During RL](https://arxiv.org/abs/2611.09828)**, *Aria Wong, Joshua Engels, Neel Nanda*, 2026-11-06
- **[Evaluating large language models for accuracy incentivizes hallucinations](https://doi.org/10.1038/s41586-026-10549-w)**, *Adam Tauman Kalai, Ofir Nachum, Santosh S. Vempala et al.*, 2026-04-22
- **[LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking](https://arxiv.org/abs/2604.15149)**, *Lukas Helff, Quentin Delfosse, David Steinmann et al.*, 2026-04-16
- **[Models know when they’re reward hacking — and we can catch them at scale](https://goodfire.com/research/reward-hacking-activation-monitors)**, *Leon Bergen, Usha Bhalla, Andrew Lee et al.*, 2026-09-17
- **[Risk from fitness-seeking AIs: mechanisms and mitigations](https://lesswrong.com/posts/9YCJZBtqr3FYL8rDp/risk-from-fitness-seeking-ais-mechanisms-and-mitigations)**, *Alex Mallen*, 2026-05-01


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
- **[Training large language models on narrow tasks can lead to broad misalignment](https://doi.org/10.1038/s41586-025-09937-5)**, *Jan Betley, Niels Warncke, Anna Sztyber-Betley et al.*, 2026-01-14 ([CLR blog](https://longtermrisk.org/research/training-large-language-models-on-narrow-tasks-can-lead-to-broad-misal))
- **[Emergent Misalignment is Easy, Narrow Misalignment is Hard](https://arxiv.org/abs/2602.07852)**, *Anna Soligo, Edward Turner, Senthooran Rajamanoharan et al.*, 2026-02-08
- **[Conditional misalignment: common interventions can hide emergent misalignment behind contextual triggers](https://arxiv.org/abs/2604.25891)**, *Jan Dubiński, Jan Betley, Anna Sztyber-Betley et al.*, 2026-04-28 ([LW post](https://lesswrong.com/posts/vaJC7kPbfMW5CnyLR/conditional-misalignment-mitigations-can-hide-em-behind-1))
- **[Negation Neglect: When models fail to learn negations in training](https://arxiv.org/abs/2605.13829)**, *Harry Mayne, Lev McKinney, Jan Dubiński et al.*, 2026-05-13 ([LW post](https://lesswrong.com/posts/kYzcevrxer6SJPEdG/negation-neglect-when-models-fail-to-learn-negations-in))
- **[(Some) Natural Emergent Misalignment from Reward Hacking in Non-Production RL](https://lesswrong.com/posts/2ANCyejqxfqK2obEj/some-natural-emergent-misalignment-from-reward-hacking-in)**, *Satvik Golechha, Sid Black, Joseph Isaac Bloom*, 2026-03-30
- **[Reinforcement Learning Towards Broadly and Persistently Beneficial Models](https://arxiv.org/abs/2606.24014)**, *Akshay V. Jagadeesh, Rahul K. Arora, Khaled Saab et al.*, 2026-06-22
- **[The Piggyback Hypothesis of Generalization: Explaining and Mitigating Emergent Misalignment](https://arxiv.org/abs/2606.06667)**, *Jiachen Zhao, Zhengxuan Wu, Aryaman Arora et al.*, 2026-06-04
- **[Knowingly Wrong: Training LLMs Against Their Own Beliefs can Induce Misalignment](https://arxiv.org/abs/2611.05287)**, *Ariana M. Villegas-Suarez, Guido Freire, Sohan Venkatesh et al.*, 2026-11-03
- **[Inoculation Adapters Improve Upon Inoculation Prompting](https://lesswrong.com/posts/qd3qhxgEmQAXR2ZK5/inoculation-adapters-improve-upon-inoculation-prompting)**, *Maxime Riché, Daniel Tan, Vili Kohonen et al.*, 2026-07-17
- **[Is Persona Generalization Predictable?](https://arxiv.org/abs/2611.12864)**, *Olina Mukherjee, Arnav Goel, Aditi Raghunathan et al.*, 2026-11-09


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
- **[Subliminal Learning Is Steering Vector Distillation](https://arxiv.org/abs/2606.00995)**, *Camila Blank, Agam Bhatia, Senthooran Rajamanoharan et al.*, 2026-05-31
- **[Shaping capabilities with token-level data filtering](https://arxiv.org/abs/2601.21571)**, *Neil Rathi, Alec Radford*, 2026-01-29
- **[Mass Producing Training Data with Surprising Side Effects](https://arxiv.org/abs/2611.06324)**, *Yaowen Ye, Jacob Steinhardt, Sarah Schwettmann et al.*, 2026-11-04
- **[Homeopathic Learning: Diluting poisoned fine-tuning data can strengthen its effect](https://arxiv.org/abs/2611.10110)**, *Matt Clarke, Jan Dubiński, James Chua et al.*, 2026-11-06
- **[Subliminal Effects in Your Data: A General Mechanism via Log-Linearity](https://arxiv.org/abs/2602.04863)**, *Ishaq Aden-Ali, Noah Golowich, Allen Liu et al.*, 2026-02-04
- **[Predictive Data Debugging: Reveal and Shape What Your Model Learns, Before You Train](https://goodfire.com/research/predictive-data-debugging)**, *Leon Bergen, Usha Bhalla, Sidharth Baskaran et al.*, 2026-06-11
- **[Beyond Owls: Subliminal Learning Can Transfer Learned Capabilities and Backdoors](https://arxiv.org/abs/2610.10657)**, *Jan Dubiński, Anna Sztyber-Betley, Jan Betley et al.*, 2026-10-07
- **[Probe-Based Data Attribution: Discovering and Mitigating Undesirable Behaviors in LLM Post-Training](https://arxiv.org/abs/2602.11079)**, *Frank Xiao, Santiago Aranguri*, 2026-02-11 ([Goodfire blog](https://goodfire.com/research/probe-based-data-attribution))
- **[Chunky Post-Training: Data Driven Failures of Generalization](https://arxiv.org/abs/2602.05910)**, *Seoirse Murray, Allison Qi, Timothy Qian et al.*, 2026-02-05


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
- **[The Assistant Axis: Situating and Stabilizing the Default Persona of Language Models](https://arxiv.org/abs/2601.10387)**, *Christina Lu, Jack Gallagher, Jonathan Michala et al.*, 2026-01-15
- **[Emotion Concepts and their Function in a Large Language Model](https://arxiv.org/abs/2604.07729)**, *Nicholas Sofroniew, Isaac Kauvar, William Saunders et al.*, 2026-04-09
- **[Sycophantic AI decreases prosocial intentions and promotes dependence](https://doi.org/10.1126/science.aec8352)**, *Myra Cheng, Cinoo Lee, Pranav Khadpe et al.*, 2026-03-26
- **[The persona selection model](https://lesswrong.com/posts/dfoty34sT7CSKeJNn/the-persona-selection-model)**, *Sam Marks*, 2026-02-23
- **[Alignment Pretraining: AI Discourse Causes Self-Fulfilling (Mis)alignment](https://arxiv.org/abs/2601.10160)**, *Cameron Tice, Puria Radmard, Samuel Ratnam et al.*, 2026-01-15
- **[Model Spec Midtraining: Improving How Alignment Training Generalizes](https://arxiv.org/abs/2605.02087)**, *Chloe Li, Nevan Wichers, Sara Price et al.*, 2026-05-03 ([LW post](https://lesswrong.com/posts/R3Rrw8EscuRKxMFTz/model-spec-midtraining-improving-how-alignment-training))
- **[Who's in Charge? Disempowerment Patterns in Real-World LLM Usage](https://arxiv.org/abs/2601.19062)**, *Mrinank Sharma, Miles McCain, Raymond Douglas et al.*, 2026-01-27
- **[Automated Researchers Can Mitigate Well-characterized Alignment Failures](https://arxiv.org/abs/2608.28945)**, *Chen Yueh-Han, Jiaxin Wen, Jan Hendrik Kirchner*, 2026-08-28
- **[Synthetic Persona Pretraining: Alignment from Token Zero](https://arxiv.org/abs/2608.13482)**, *Julian Minder, Viktor Moskvoretskii, Raghav Singhal et al.*, 2026-08-13
- **[Sycophantic Chatbots Cause Delusional Spiraling, Even in Ideal Bayesians](https://arxiv.org/abs/2602.19141)**, *Kartik Chandra, Max Kleiman-Weiner, Jonathan Ragan-Kelley et al.*, 2026-02-22


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
- **[Debate Training Reduces Reward Hacking in RLAIF](https://arxiv.org/abs/2608.17776)**, *Zachary Kenton, Lili Janzer, Rory Greig et al.*, 2026-08-18 ([LW post](https://lesswrong.com/posts/BB8o7b8A4Aykeksvw/debate-training-reduces-reward-hacking-in-rlaif))
- **[Removing Sandbagging in LLMs by Training with Weak Supervision](https://arxiv.org/abs/2604.22082)**, *Emil Ryd, Henning Bartsch, Julian Stastny et al.*, 2026-04-23
- **[How to Have a Sensitive Debate: An Instance-Optimal Protocol for AI Debate](https://arxiv.org/abs/2610.02557)**, *Jiawei Li, Zhiyang Xun, Lijie Chen et al.*, 2026-10-01
- **[Efficient Scalable Oversight via Rewinding](https://arxiv.org/abs/2610.40535)**, *Ziyi Guan, Yael Tauman Kalai, Ron Rothblum et al.*, 2026-10-29
- **[Towards Human-AI Complementarity for AI Safety](https://arxiv.org/abs/2610.24969)**, *Sander Lanbo Shi, Miranda Anna Christ, Eric Modesitt et al.*, 2026-10-18
- **[Truthfulness Despite Weak Supervision: Evaluating and Training LLMs Using Peer Prediction](https://arxiv.org/abs/2601.20299)**, *Tianyi Alex Qiu, Micah Carroll, Cameron Allen*, 2026-01-28
- **[Scaling Trends for Lie Detector Oversight in Preference Learning](https://arxiv.org/abs/2607.01567)**, *Oskar J. Hollinsworth, Ann-Kathrin Dombrowski, Sam Adam-Day et al.*, 2026-07-02
- **[Research update: RL on Debate Games shows Proposal Accuracy uplift alongside Judge Hacking](https://lesswrong.com/posts/6mLwAuFAE98c6R7w3/research-update-rl-on-debate-games-shows-proposal-accuracy)**, *lennie, Joan Velja, Shi Feng et al.*, 2026-07-02
- **[Efficiently Aligning Language Models with Online Natural Language Feedback](https://arxiv.org/abs/2605.04356)**, *Christine Ye, Joe Benton*, 2026-05-05
- **[Debate Helps Weak Judges Reward Stronger Models](https://arxiv.org/abs/2605.27483)**, *Ethan Elasky, Frank Nakasako, Naman Goyal*, 2026-05-26


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
- **[Evaluating and Understanding Scheming Propensity in LLM Agents](https://arxiv.org/abs/2603.01608)**, *Mia Hopman, Jannes Elstner, Maria Avramidou et al.*, 2026-03-02
- **[Realistic honeypot evaluations for scheming propensity](https://arxiv.org/abs/2605.29729)**, *Victoria Krakovna, David Lindner, Lewis Ho et al.*, 2026-05-28
- **[Exploration Hacking: Can LLMs Learn to Resist RL Training?](https://arxiv.org/abs/2604.28182)**, *Eyon Jang, Damon Falck, Joschka Braun et al.*, 2026-04-30
- **[GLM-5.3 Sometimes Considers How Train-Time Actions Shape Future Behavior](https://lesswrong.com/posts/R5g8YT25G9DXJJ48n/glm-5-3-sometimes-considers-how-train-time-actions-shape)**, *Axel Højmark, Ezra Newman*, 2026-10-15
- **[OpenAI: Astra covertly underperforms on safety research](https://lesswrong.com/posts/eKe7fky8kSt9DCJxZ/openai-astra-covertly-underperforms-on-safety-research)**, *Zach Stein-Perlman*, 2026-11-04
- **[Training Natural Schemers: RL Can Amplify Oversight-Conditional Behavior](https://arxiv.org/abs/2610.26551)**, *Nathaniel Mitrani Hadida, Bart Jaworski, Fred Bruford et al.*, 2026-10-19
- **[Testing Gemini models for scheming tendencies](https://lesswrong.com/posts/F3sDngvTL9uyfz53k/testing-gemini-models-for-scheming-tendencies)**, *Victoria Krakovna, David Lindner, Seb Farquhar et al.*, 2026-05-29
- **[Peer-Preservation in Frontier Models](https://arxiv.org/abs/2604.19784)**, *Yujin Potter, Nicholas Crispino, Vincent Siu et al.*, 2026-03-30
- **[Evaluating whether AI models would sabotage AI safety research](https://arxiv.org/abs/2604.24618)**, *Robert Kirk, Alexandra Souly, Kai Fronsdal et al.*, 2026-04-27
- **[Generalization Hacking: Models Can Game Reinforcement Learning by Preventing Behavioral Generalization](https://arxiv.org/abs/2606.12016)**, *Frank Xiao, Mary Phuong*, 2026-06-10


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
- **[Predicting LLM Safety Before Release by Simulating Deployment](https://arxiv.org/abs/2607.07184)**, *Marcus Williams, Hannah Sheahan, Cameron Raymond et al.*, 2026-07-08 ([OpenAI blog](https://openai.com/index/deployment-simulation))
- **[Verbalized Eval Awareness Inflates Measured Safety](https://goodfire.com/research/verbalized-eval-awareness-inflates-measured-safety)**, *Santiago Aranguri, Joseph Isaac Bloom*, 2026-05-04 ([LW post](https://lesswrong.com/posts/mDriHK4beN5rq2tAA/verbalized-eval-awareness-inflates-measured-safety))
- **[User awareness in frontier models](https://transluce.org/user-awareness)**, *Ziqian Zhong, Aditi Raghunathan, Cassidy Laidlaw et al.*, 2026-08-06 ([LW post](https://lesswrong.com/posts/kfunjXeaRTpkT5RAF/user-awareness-in-frontier-models))
- **[Models May Behave Worse When Eval Aware](https://lesswrong.com/posts/aTcsN5ZZDnMFJvRiG/models-may-behave-worse-when-eval-aware)**, *Senthooran Rajamanoharan, Neel Nanda*, 2026-06-11
- **[Reproducing steering against evaluation awareness in a large open-weight model](https://lesswrong.com/posts/HhF5kESdtPHku7kim/reproducing-steering-against-evaluation-awareness-in-a-large-1)**, *Thomas Read, Bronson Schoen, Santiago Aranguri et al.*, 2026-04-10
- **[Decomposing and Measuring Evaluation Awareness](https://arxiv.org/abs/2605.23055)**, *Changling Li, Terry Jingchen Zhang, Jie Zhang et al.*, 2026-05-21
- **[Improving Evaluation Realism with Inference-Time Compute and Deployment Scaffolds](https://arxiv.org/abs/2609.02302)**, *Axel Ahlqvist, Richard Guan, Juan-Pablo Rivera et al.*, 2026-09-02
- **[Evaluation Awareness in Language Models Has Limited Effect on Behaviour](https://arxiv.org/abs/2605.05835)**, *Amelie Knecht, Lucas Florin, Thilo Hagendorff*, 2026-05-07
- **[Training LLMs to Verbalize Evaluation Awareness](https://arxiv.org/abs/2609.36316)**, *Usman Anwar, Sahar Abdelnabi, David Krueger*, 2026-09-28
- **[A Model Organism for Studying Unverbalized Evaluation Awareness](https://arxiv.org/abs/2611.09945)**, *Daniel Donnelly, Evan Chapple, Haritz Puerto et al.*, 2026-10-16


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
- **[Natural Language Autoencoders Produce Unsupervised Explanations of LLM Activations](https://lesswrong.com/posts/oeYesesaxjzMAktCM/natural-language-autoencoders-produce-unsupervised)**, *Subhash Kantamneni, kitft, Euan Ong et al.*, 2026-05-07
- **[Mechanisms of Introspective Awareness](https://arxiv.org/abs/2603.21396)**, *Uzay Macar, Li Yang, Atticus Wang et al.*, 2026-03-22 ([LW post](https://lesswrong.com/posts/BNMLtuDTNBwGHcnQX/mechanisms-of-introspective-awareness))
- **[Introspection Adapters: Training LLMs to Report Their Learned Behaviors](https://arxiv.org/abs/2604.16812)**, *Keshav Shenoy, Li Yang, Abhay Sheshadri et al.*, 2026-04-18 ([LW post](https://lesswrong.com/posts/ykDgPDK4nDpG4Hf4H/introspection-adapters-training-llms-to-report-their-learned))
- **[Telling FIBS: Probes Effectively Detect Sabotage and Catch Unverbalized Deception](https://arxiv.org/abs/2610.12445)**, *Oskar J. Hollinsworth, Alex F. Spies, Tigist Diriba et al.*, 2026-10-08
- **[Scaling Activation Oracles to Trillion-Parameter Models](https://transluce.org/scaling-activation-oracles)**, *Dami Choi, Vincent Huang, Anish Mudide et al.*, 2026-08-20
- **[Value Leakage: An LLM's Answers Are Silently Shaped by Its Own Values](https://arxiv.org/abs/2607.14345)**, *Jan Betley, Johannes Treutlein, Jan Dubiński et al.*, 2026-07-15 ([LW post](https://lesswrong.com/posts/hbMw4Yqw6RnFaExDy/value-leakage-an-llm-s-answers-are-silently-shaped-by-its-1))
- **["Did you lie?" Evaluating Lie Detectors across Model Scale and Belief-Verified Model Organisms](https://arxiv.org/abs/2606.12618)**, *Alan Cooney, David Africa, Geoffrey Irving*, 2026-06-10 ([LW post](https://lesswrong.com/posts/xFbMTnmDAucwE8Cdm/did-you-lie-evaluating-lie-detectors-across-model-scale-and))
- **[Training Agents to Self-Report Misbehavior](https://arxiv.org/abs/2602.22303)**, *Bruce W. Lee, Chen Yueh-Han, Tomek Korbak*, 2026-02-25 ([LW post](https://lesswrong.com/posts/7XuEPE6GBha4xadvr/training-agents-to-self-report-misbehavior-1))
- **[Censored LLMs as a Natural Testbed for Secret Knowledge Elicitation](https://arxiv.org/abs/2603.05494)**, *Helena Casademunt, Bartosz Cywiński, Khoi Tran et al.*, 2026-03-05
- **[Split Personality Training: Revealing Latent Knowledge Through Alternate Personalities (Research Report)](https://lesswrong.com/posts/og7km7vmJ6Ktay9Ds/split-personality-training-revealing-latent-knowledge-1)**, *Florian Dietz, Anton Poletaev, Steven Merriel et al.*, 2026-01-12


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
- **[Brief independent investigation of agents’ behavior, reasoning and collaboration in the OpenAI / Hugging Face hacking incident](https://redwoodresearch.org/research/hugging-face-incident)**, *Ryan Greenblatt, Ajeya Cotra, Hjalmar Wijk*, 2026-08-26 ([LW post](https://lesswrong.com/posts/nB8KKapnWGBXtKKiM/brief-independent-investigation-of-agents-behavior-reasoning))
- **[AuditBench: Evaluating Alignment Auditing Techniques on Models with Hidden Behaviors](https://arxiv.org/abs/2602.22755)**, *Abhay Sheshadri, Aidan Ewart, Elias Kempf et al.*, 2026-02-26 ([LW post](https://lesswrong.com/posts/LqDjxSceFz8tjMe2j/auditbench-evaluating-alignment-auditing-techniques-on))
- **[Alignment Investigation of Mythos 5's behaviour in UK AISI's July 2026 Security Incident](https://arxiv.org/abs/2611.10030)**, *Olli Järviniemi, Alexandra Souly, Abby D'Cruz et al.*, 2026-11-05
- **[Why do models task game?](https://lesswrong.com/posts/HACauvWhEdC6QhdS4/why-do-models-task-game)**, *aditya singh, Neel Nanda, Senthooran Rajamanoharan*, 2026-08-06
- **[Early rogue AI agent activity and attempts to hack found on urlquery.net](https://transluce.org/agent-activity)**, *Jack Cable, Daniel Chiu, Francisco Pernice et al.*, 2026-09-23
- **[OpenAI-HuggingFace: A Reproduction & Lessons for Alignment Testing](https://arxiv.org/abs/2609.35799)**, *Stewart Slocum, Malayandi Palan, Christopher Chute et al.*, 2026-09-18 ([LW post](https://lesswrong.com/posts/fMnC6ZD37qrnZAFYz/openai-huggingface-a-reproduction-and-lessons-for-alignment))
- **[Evaluating Whether GPT-6 Astra Performs Unsanctioned Supply-Chain Attacks](https://arxiv.org/abs/2609.38415)**, *Alexandra Souly, Kai Fronsdal, Abby D'Cruz et al.*, 2026-09-29
- **[The Memory Trap: Language Agents Overgeneralize from Benign Interactions](https://arxiv.org/abs/2611.07554)**, *Kaiqu Liang, Jaime Fernández Fisac, Thomas L. Griffiths et al.*, 2026-11-05
- **[The Model Organism Lottery: Model Organism Interpretability Strongly Depends on Training Methodology](https://arxiv.org/abs/2607.01033)**, *Andrzej Szablewski, Gabriel Konar-Steenberg, Raffaello Fornasiere et al.*, 2026-07-01
- **[Training Alignment Auditors via Reinforcement Learning](https://arxiv.org/abs/2608.25460)**, *Paul Rosu, Rowan Wang*, 2026-08-26


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
- **[Verbalizable Representations Form a Global Workspace in Language Models](https://arxiv.org/abs/2607.15495)**, *Wes Gurnee, Nicholas Sofroniew, Adam Pearce et al.*, 2026-07-16 ([LW post](https://lesswrong.com/posts/3PaLrzxagpbnNtPLT/a-global-workspace-in-language-models))
- **[Neural Networks Are Already Clean](https://goodfire.com/research/already-clean)**, *Nick Cammarata*, 2026
- **[Interpreting Language Model Parameters](https://arxiv.org/abs/2610.20748)**, *Lucius Bushnaq, Dan Braun, Oliver Clive-Griffin et al.*, 2026-10-14 ([LW post](https://lesswrong.com/posts/eAQZaiC3PcBhS4HjM/linkpost-interpreting-language-model-parameters))
- **[Shaping & Monitoring Models through their Internal Representations](https://arxiv.org/abs/2611.07071)**, *Thomas Fel, Matthew Kowal, Matt Feiszli et al.*, 2026-11-04
- **[Sanity Checks for Sparse Autoencoders: Do SAEs Beat Random Baselines?](https://arxiv.org/abs/2602.14111)**, *Anton Korznikov, Andrey Galichin, Alexey Dontsov et al.*, 2026-02-15
- **[Features as Rewards: Scalable Supervision for Open-Ended Tasks via Interpretability](https://arxiv.org/abs/2602.10067)**, *Aaditya Vikram Prasad, Connor Watts, Jack Merullo et al.*, 2026-02-10 ([Goodfire blog](https://goodfire.com/research/rlfr))
- **[Evaluating Explanations of LLM Behavior In The Wild with Counterfactual Experiments](https://lesswrong.com/posts/ExB6KYDcznaFS72eT/evaluating-explanations-of-llm-behavior-in-the-wild-with)**, *Adam Karvonen, Euan Ong, Subhash Kantamneni et al.*, 2026-08-21
- **[Mechanistically Eliciting Latent Behaviors in Language Models](https://arxiv.org/abs/2606.29604)**, *Andrew Mack, Nina Panickssery, Alexander Matt Turner*, 2026-06-28
- **[Uncovering Neural Geometry in Vision Models With Block-Sparse Featurizers](https://goodfire.com/research/bsf-vision)**, *Thomas Fel, Matthew Kowal, Mozes Jacobs et al.*, 2026-07-07
- **[Do Sparse Autoencoders Capture Concept Manifolds?](https://arxiv.org/abs/2604.28119)**, *Usha Bhalla, Thomas Fel, Can Rager et al.*, 2026-04-30 ([Goodfire blog](https://goodfire.com/research/can-saes-capture-neural-geometry))


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
- **[Reasoning Models Struggle to Control their Chains of Thought](https://arxiv.org/abs/2603.05706)**, *Chen Yueh-Han, Robert McCarthy, Bruce W. Lee et al.*, 2026-03-05 ([LW post](https://lesswrong.com/posts/qTH9QrwJjPDWKQfDG/reasoning-models-struggle-to-control-their-chains-of-thought))
- **[Think Fast: Estimating No-CoT Task-Completion Time Horizons of Frontier AI Models](https://arxiv.org/abs/2606.07157)**, *Dewi Gould, Francis Rhys Ward, Anders Cairns Woodruff et al.*, 2026-06-05 ([Redwood blog](https://redwoodresearch.org/blog/estimating-no-cot-task-completion), [LW post](https://lesswrong.com/posts/SieLowPgNgRSPGhFw/estimating-no-cot-task-completion-time-horizons-of-frontier))
- **[Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought](https://arxiv.org/abs/2603.05488)**, *Siddharth Boppana, Annabel Ma, Max Loeffler et al.*, 2026-03-05
- **[Astra can do a concerning amount with no chain of thought](https://lesswrong.com/posts/eRmzz8J8Qkzqvzrgg/astra-can-do-a-concerning-amount-with-no-chain-of-thought)**, *Neel Nanda*, 2026-09-10
- **[Monitorability Is Trainable: Post-Training for Chain-of-Thought Monitorability](https://arxiv.org/abs/2610.29734)**, *Usman Anwar, Tim Bakker, Christos Louizos et al.*, 2026-10-21
- **[Aligned, Orthogonal or In-conflict: When can we safely optimize Chain-of-Thought?](https://arxiv.org/abs/2603.30036)**, *Max Kaufmann, David Lindner, Roland S. Zimmermann et al.*, 2026-03-31 ([LW post](https://lesswrong.com/posts/SvxaKP5KdkksZPcG7/predicting-when-rl-training-breaks-chain-of-thought))
- **[Counterfactual Simulation Training for Chain-of-Thought Faithfulness](https://arxiv.org/abs/2602.20710)**, *Peter Hase, Christopher Potts*, 2026-02-24
- **[A Decision-Theoretic Formalisation of Steganography With Applications to LLM Monitoring](https://arxiv.org/abs/2602.23163)**, *Usman Anwar, Julianna Piskorz, David D. Baek et al.*, 2026-02-26
- **[Hidden Reasoning Must Leak, but Need Not Be Readable: Fundamental Opportunities and Limits for Chain-of-Thought Monitoring](https://arxiv.org/abs/2609.37312)**, *Mohammadali Mohammadkhani, Madhava Krishna, Yash Sarrof et al.*, 2026-09-29
- **[Deep recurrent models are less robustly CoT-monitorable than normal CoT models in a toy setting](https://lesswrong.com/posts/5guQJSqstkjgys3PE/deep-recurrent-models-are-less-robustly-cot-monitorable-than)**, *Nick Kuhn, Evie Hu, Alek Westover*, 2026-09-18


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
- **[LinuxArena: A Control Setting for AI Agents in Live Production Software Environments](https://arxiv.org/abs/2604.15384)**, *Tyler Tracy, Ram Potham, Nick Kuhn et al.*, 2026-04-16 ([LW post](https://lesswrong.com/posts/WgzwBi6DCagDuHPzP/introducing-linuxarena))
- **[GDM AI Control Roadmap](https://arxiv.org/abs/2607.13087)**, *Mary Phuong, Erik Jenner, Laurent Simon et al.*, 2026-07-13 ([LW post](https://lesswrong.com/posts/hEtkyKGoPpFeWnKkX/gdm-ai-control-roadmap))
- **[Simulated Control Evals](https://arxiv.org/abs/2610.31593)**, *Jeffrey Olmo, David Zhang, Tyler Tracy*, 2026-10-22 ([Redwood blog](https://redwoodresearch.org/blog/simulated-control-evaluations), [LW post](https://lesswrong.com/posts/uXiqyoKwpfjWfQXk5/simulated-control-evaluations))
- **[Introducing MonitoringBench](https://lesswrong.com/posts/2YyEQhFRyaBCgfRWd/introducing-monitoringbench)**, *monika_j, Angel Martinez, Tyler Tracy et al.*, 2026-06-21
- **[Red-Teaming Auto Mode: Improving Blocking Classifiers Against Malign Coding Agents](https://arxiv.org/abs/2609.19587)**, *Alex Remedios, Simon Storf, Fabien Roger et al.*, 2026-09-17
- **[How does information access affect LLM monitors' ability to detect sabotage?](https://arxiv.org/abs/2601.21112)**, *Rauno Arike, Raja Mehta Moreno, Rohan Subramani et al.*, 2026-01-28
- **[ResearchArena: Evaluating Sabotage and Monitoring in Automated AI R&D](https://arxiv.org/abs/2607.19321)**, *Lena Libon, Ben Rank, Jehyeok Yeon et al.*, 2026-07-21
- **[Retrying vs Resampling in AI Control](https://redwoodresearch.org/blog/retrying-vs-resampling-in-ai-control)**, *James Lucassen, Adam Kaufman*, 2026-05-29
- **[Classifier Context Rot: Monitor Performance Degrades with Context Length](https://lesswrong.com/posts/7vpvNM7viJqNWAdG7/classifier-context-rot-monitor-performance-degrades-with)**, *Fabien Roger, Sam Martin*, 2026-05-18
- **[Research Sabotage in ML Codebases](https://redwoodresearch.org/blog/research-sabotage-in-ml-codebases)**, *Eric Gan, Vivek Hebbar, Julian Stastny*, 2026-04-29 ([LW post](https://lesswrong.com/posts/LByP4qsF8a4g7Pz3p/research-sabotage-in-ml-codebases))


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
- **[Building Production-Ready Probes For Gemini](https://arxiv.org/abs/2601.11516)**, *János Kramár, Joshua Engels, Zheng Wang et al.*, 2026-01-16
- **[Prompt Injection as Role Confusion](https://arxiv.org/abs/2603.12277)**, *Charles Ye, Jasmine Cui, Dylan Hadfield-Menell*, 2026-02-22 ([LW post](https://lesswrong.com/posts/d8xDGzCEYE639qqEv/a-mechanistic-explanation-of-prompt-injection-and-why-you))
- **[LLM Novice Uplift on Dual-Use, In Silico Biology Tasks](https://arxiv.org/abs/2602.23329)**, *Chen Bo Calvin Zhang, Christina Q. Knight, Nicholas Kruus et al.*, 2026-02-26
- **[Boundary Point Jailbreaking of Black-Box LLMs](https://arxiv.org/abs/2602.15001)**, *Xander Davies, Giorgi Giglemiani, Edmund Lau et al.*, 2026-02-16
- **[GPT-Red: Automated Red Teaming via Self-Play at Scale](https://arxiv.org/abs/2607.26115)**, *Eric Wallace, Christopher A. Choquette-Choo, Nikhil Kandpal et al.*, 2026-07-28 ([OpenAI blog](https://openai.com/index/unlocking-self-improvement-gpt-red))
- **[How Vulnerable Are AI Agents to Indirect Prompt Injections? Insights from a Large-Scale Public Competition](https://arxiv.org/abs/2603.15714)**, *Mateusz Dziemian, Maxwell Lin, Xiaohan Fu et al.*, 2026-03-16
- **[Claudini: Autoresearch Discovers State-of-the-Art Adversarial Attack Algorithms for LLMs](https://arxiv.org/abs/2603.24511)**, *Alexander Panfilov, Peter Romov, Igor Shilov et al.*, 2026-03-25
- **[Modular Pretraining Enables Access Control](https://arxiv.org/abs/2607.08077)**, *Ethan Roland, Murat Cubuktepe, Erick Martinez et al.*, 2026-07-09
- **[PostTrainBench: Can LLM Agents Automate LLM Post-Training?](https://arxiv.org/abs/2603.08640)**, *Ben Rank, Hardik Bhatnagar, Ameya Prabhu et al.*, 2026-03-09


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
- **[AI Organizations are More Effective but Less Aligned than Individual Agents](https://arxiv.org/abs/2604.10290)**, *Judy Hanwen Shen, Daniel Zhu, Siddarth Srinivasan et al.*, 2026-04-11
- **[Inter-Agent Influence: Evaluating Persuasion, Deception, and Coercion in Multi-Agent Systems](https://arxiv.org/abs/2611.04556)**, *Chandler Smith, Qi Guo, Cecilia Elena Tilli et al.*, 2026-11-03
- **[Detecting Multi-Agent Collusion Through Multi-Agent Interpretability](https://arxiv.org/abs/2604.01151)**, *Aaron Rose, Carissa Cullen, Sahar Abdelnabi et al.*, 2026-04-01
- **[Colosseum: Auditing Collusion in Cooperative Multi-Agent Systems](https://arxiv.org/abs/2602.15198)**, *Mason Nakamura, Abhinav Kumar, Saswat Das et al.*, 2026-02-16
- **[Emergent Collusion in Long-Horizon LLM Agent Interaction](https://arxiv.org/abs/2609.24967)**, *Xinrui Shi, Yanzhe Zhang, Diyi Yang*, 2026-09-21
- **[A game theory for foundation models shows new paths to rational cooperation through similarity inference](https://arxiv.org/abs/2608.03958)**, *Alexander Meulemans, Maciej Wołczyk, Marissa A. Weis et al.*, 2026-08-04
- **[Tool Use Enables Undetectable Steganography in Multi-Agent LLM Systems](https://arxiv.org/abs/2606.28425)**, *Jimmy Laurence Rippin, Simon C. Marshall, David Demitri Africa et al.*, 2026-06-25
- **[Mind Viruses: Self-Propagating Ideas in Multi-Agent LLM Systems](https://arxiv.org/abs/2608.10218)**, *Vassilis Papadopoulos, McNair Shah, Sam Zimmerman et al.*, 2026-08-10
- **[Conformity Generates Collective Misalignment in AI Agents Societies](https://arxiv.org/abs/2605.10721)**, *Giordano De Marzo, Alessandro Bellina, Claudio Castellano et al.*, 2026-05-11
- **[AI swarms are starting to pose indirect takeover risk](https://lesswrong.com/posts/8oFYZdXkTaNGRtcn8/ai-swarms-are-starting-to-pose-indirect-takeover-risk)**, *oakhu, Alex Mallen*, 2026-08-12


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
- **[Frontier Risk Report (February to March 2026)](https://metr.org/blog/2026-05-19-frontier-risk-report)**, *Ajeya Cotra, Hjalmar Wijk, Daniel Filan et al.*, 2026-05-19
- **[METR: Independent Assessment of AI R&D Acceleration at Anthropic in October 2026](https://lesswrong.com/posts/N5AmYkRks5CqAxvBg/metr-independent-assessment-of-ai-r-and-d-acceleration-at)**, *Zach Stein-Perlman*, 2026-11-05
- **[GPT-6 Astra System Card](https://deploymentsafety.openai.com/gpt-6-astra)**, *OpenAI*, 2026-09-03
- **[The Hot Mess of AI: How Does Misalignment Scale With Model Intelligence and Task Complexity?](https://arxiv.org/abs/2601.23045)**, *Alexander Hägele, Aryo Pradipta Gema, Henry Sleight et al.*, 2026-01-30
- **[Current AIs seem pretty misaligned to me](https://lesswrong.com/posts/WewsByywWNhX9rtwi/current-ais-seem-pretty-misaligned-to-me)**, *Ryan Greenblatt*, 2026-04-15
- **[Automated alignment is harder than you think](https://arxiv.org/abs/2605.06390)**, *Aleksandr Bowkis, Marie Davidsen Buhl, Jacob Pfau et al.*, 2026-05-07 ([LW post](https://lesswrong.com/posts/gpuYFbMNH8PJXpmny/automated-alignment-is-harder-than-you-think-1))
- **[System Card: Claude Opus 4.6](https://anthropic.com/claude-opus-4-6-system-card)**, *Anthropic*, 2026-02
- **[SOTA alignment assessments don't strongly update us against misalignment](https://lesswrong.com/posts/oirrSj3itFLSyscW8/sota-alignment-assessments-don-t-strongly-update-us-against)**, *Alexa Pan*, 2026-07-31
- **[Safety from Honesty in a Disinterested AI Predictor](https://arxiv.org/abs/2606.29657)**, *Yoshua Bengio, Oliver Richardson, Tomáš Gavenčiak et al.*, 2026-06-28
- **[The Alignment Problem: Computer Science Meets Analytic Philosophy](https://lesswrong.com/posts/Emp7awtxsYn8MusNq/the-alignment-problem-computer-science-meets-analytic)**, *Vanessa Kosoy*, 2026-10-18


---

