# 2026 Taxonomy

- **1. [Training-time alignment](#training_time_alignment)**: Understanding how pretraining and post-training shape a model's behaviour and character, and using that to produce an aligned model.
  - 1.1 [Training data & data attribution](#training_data_and_data_attribution): Pretraining, midtraining and post-training data interventions (filtering, alignment pretraining, hyperstition, spec midtraining), and tracing behaviours back to the data that caused them.
  - 1.2 [Emergent misalignment & generalization science](#emergent_misalignment_and_generalization_science): Why fine-tuning generalizes the way it does, including emergent and conditional misalignment and which post-training stages drive safety properties.
  - 1.3 [Persona science](#persona_science): Models of LLMs as characters selected and strengthened by training (persona selection, split personas, the default Assistant persona), and how training changes which persona a model takes on.
  - 1.4 [Subliminal learning & hidden-signal transfer](#subliminal_learning_and_hidden_signal_transfer): Traits, capabilities and backdoors passed between models through data that looks unrelated to them.
  - 1.5 [Inoculation prompting](#inoculation_prompting): Training under prompts that elicit an unwanted behaviour, so the behaviour stays tied to that context instead of generalizing.
  - 1.6 [Reward hacking & reward seeking in training](#reward_hacking_and_reward_seeking_in_training): How RL and reward design produce reward hacking, specification gaming and reward-seeking motivations, and training-side fixes such as better verifiers or channelling hacks into a harmless outlet.
  - 1.7 [Models resisting training](#models_resisting_training): Models that steer or resist their own training, such as exploration hacking, generalization hacking and gradient hacking.
  - 1.8 [Internals & monitors as training signals](#internals_and_monitors_as_training_signals): Using probes, features or monitors as training rewards or penalties, and the risk that the model learns to fool them instead of changing its behaviour.
  - 1.9 [Alignment targets & training methods](#alignment_targets_and_training_methods): What to train models to be (constitutions, specs, virtues, corrigibility) and methods that train a target property directly, such as shutdownability or consistency training.
- **2. [Chain-of-thought monitorability](#chain_of_thought_monitorability)**: Whether a model's written reasoning is a reliable signal of what it is doing, and what keeps or destroys that.
  - 2.1 [Latent reasoning & CoT necessity](#latent_reasoning_and_cot_necessity): How much models can do without visible reasoning (no-CoT time horizons, filler tokens, recurrent and diffusion architectures), and so whether dangerous reasoning has to appear in the CoT.
  - 2.2 [CoT control, obfuscation & steganography](#cot_control_obfuscation_and_steganography): Stress tests of whether models can control, hide or encode their reasoning.
  - 2.3 [How training affects monitorability](#how_training_affects_monitorability): Which training pressures keep or degrade CoT legibility, including accidental training against the CoT and language drift.
  - 2.4 [Measuring & improving faithfulness](#measuring_and_improving_faithfulness): Measuring whether the CoT reflects the computation behind the answer, and training for faithful or monitorable reasoning.
- **3. [Evaluations & auditing](#evaluations_and_auditing)**: Measuring what models can do and will do, finding hidden behaviours, and checking that those measurements are trustworthy.
  - 3.1 [Capability evals](#capability_evals): Dangerous and decision-relevant capabilities, such as cyber, bio, autonomy, self-replication, AI R&D and time horizons.
  - 3.2 [Propensity evals](#propensity_evals): How often models scheme, sabotage, deceive, hack rewards or break their spec when given the chance, including reward-hacking benchmarks.
  - 3.3 [Model characterization](#model_characterization): Values, preferences, drives and dispositions of current models.
  - 3.4 [Situational & evaluation awareness](#situational_and_evaluation_awareness): Whether models can tell they are being evaluated, trained or tampered with, and how that changes their behaviour and our measurements.
  - 3.5 [Introspection & self-report](#introspection_and_self_report): What models can accurately report about their own internal states and learned behaviours, and training them to report it.
  - 3.6 [Eval science & validity](#eval_science_and_validity): Whether evals, benchmarks, red-team numbers and lab safety claims are trustworthy, including construct validity, eval realism, benchmark hardening and statistical methods.
  - 3.7 [Alignment auditing: methods](#alignment_auditing_methods): Techniques and agents for finding hidden objectives or misbehaviour in a model, eliciting sandbagged capabilities, and attacks on audits.
  - 3.8 [Alignment auditing: testbeds & model organisms](#alignment_auditing_testbeds_and_model_organisms): Models with known hidden behaviours used to test audits, and whether those model organisms are realistic and robust.
- **4. [Monitoring & control](#monitoring_and_control)**: Deploying models that may be misaligned, using monitors and protocols that keep them safe even if they try to cause harm.
  - 4.1 [Control settings & protocols](#control_settings_and_protocols): Control environments, protocols and safety cases that assume the model may be adversarial, including multi-agent and distributed attacks on those protocols.
  - 4.2 [Monitors](#monitors): Black-box, CoT and probe-based monitors for scheming, sabotage, deception and reward hacking, and how well they work.
  - 4.3 [Red-teaming monitors & control protocols](#red_teaming_monitors_and_control_protocols): Attack policies, evasion benchmarks and studies of models evading monitors.
- **5. [Security & misuse](#security_and_misuse)**: Defending models and agents against external adversaries, such as misusers, prompt injectors and thieves.
  - 5.1 [Misuse safeguards & jailbreaks](#misuse_safeguards_and_jailbreaks): Classifiers, probes and refusal training against misuse, and attacks that get past them.
  - 5.2 [Agent security](#agent_security): Prompt injection, memory and skill-file poisoning, privilege escalation, and system-level defences for agents.
  - 5.3 [Open-weight tamper resistance & unlearning](#open_weight_tamper_resistance_and_unlearning): Removing hazardous knowledge and keeping safeguards in open-weight models after fine-tuning.
  - 5.4 [Weight & infrastructure security](#weight_and_infrastructure_security): Protecting model weights and the inference and agent harness infrastructure from theft or tampering.
- **6. [Interpretability](#interpretability)**: Work whose main contribution is a tool for understanding model internals, or a finding about them.
  - 6.1 [Methods & tools](#interpretability_methods_and_tools): SAEs and their alternatives, circuits, lenses, activation oracles, steering and other interpretability techniques, and tests of whether they work.
  - 6.2 [Science of representations](#science_of_representations): Findings about how models represent and compute things, such as the global workspace, emotion concepts and shared circuits.
  - 6.3 [Learning dynamics & developmental interpretability](#learning_dynamics_and_developmental_interpretability): How internal structure forms during training, including singular learning theory and susceptibilities.
- **7. [Real-world evidence](#real_world_evidence)**: Evidence from real deployments and from labs' own disclosures, not controlled experiments.
  - 7.1 [Incidents & case studies](#incidents_and_case_studies): Real-world AI incidents and their investigation, such as the OpenAI-Hugging Face incident and scheming found in the wild.
  - 7.2 [Effects on people](#effects_on_people): Harms to users and human agency from everyday AI use, such as sycophancy, delusion, dependence and disempowerment.
  - 7.3 [Lab disclosures: system cards & risk reports](#lab_disclosures): System cards, risk reports and what they do or don't show.
- **8. [Multi-agent safety](#multi_agent_safety)**: Failures that come from AI agents interacting, such as collusion, spreading ideas or behaviours, and the behaviour of AI organisations, in experiments or game theory.
- **9. [Scalable oversight & automated alignment](#scalable_oversight_and_automated_alignment)**: Debate and other ways for weaker overseers to supervise stronger models, and using AI to do alignment research.
- **10. [Theory & foundations](#theory_and_foundations)**: Theoretical agendas aimed at understanding or guaranteeing safety from first principles.
  - 10.1 [Agent foundations](#agent_foundations): Formal models of agency, corrigibility and decision-making.
  - 10.2 [Heuristic explanations & mechanistic estimation](#heuristic_explanations_and_mechanistic_estimation): ARC's agenda of explaining and estimating model behaviour without sampling.
  - 10.3 [Formal methods & guaranteed-safe AI](#formal_methods_and_guaranteed_safe_ai): Proofs, formal verification and their limits as a route to safety.
- **11. [Threat models & strategy](#threat_models_and_strategy)**: Arguments about how AI could go wrong and what the field should do about it.
  - 11.1 [Reward-seeking & fitness-seeking threat models](#reward_seeking_threat_models): How AIs that seek reward or fitness would behave, and what follows for safety.
  - 11.2 [Misalignment arguments & failure scenarios](#misalignment_arguments_and_failure_scenarios): Arguments for and against egregious misalignment, and scenarios for how AI risk plays out.
  - 11.3 [Research strategy & deals with AIs](#research_strategy_and_deals_with_ais): Prioritization between safety agendas, career and lab-strategy questions, and proposals for making deals with AIs.
- **12. [Model welfare](#model_welfare)**: Model welfare and moral status, including functional pleasure and pain in models.

---

# AI Safety Shallow Review 2026

**Generated:** 2026-11-10
**Kept per category:** importance at least 0.5, at most the 10 most important (174 pruned)

**Total unique papers:** 325 (appearing 325 times across categories)

---

## <span id="training_time_alignment" style="font-size:1.5em">Training-time alignment</span>


---

### <span id="training_data_and_data_attribution" style="font-size:1.4em">Training data & data attribution</span>

**One-sentence summary:** Shape what models learn by intervening on pretraining, midtraining and post-training data (filtering, alignment and spec documents, persona annotation, data editing), and trace undesired behaviours back to the training data that caused them.  
**Theory of change:** If behaviours and dispositions come largely from identifiable training data, then curating that data, adding alignment-relevant documents, and attributing failures to their sources is cheaper and more robust than patching behaviour afterwards. Relies on data-level effects surviving later post-training and fine-tuning, and on attribution methods finding the true causes.  
**See also:** [Emergent misalignment & generalization science](#emergent_misalignment_and_generalization_science), [Persona science](#persona_science), [Subliminal learning & hidden-signal transfer](#subliminal_learning_and_hidden_signal_transfer)  
**General approach:** alignment engineering  
**Target case:** average case  
**Key people:** Cameron Tice, Kyle O'Brien, Puria Radmard, David Africa, Santiago Aranguri, Sara Price, Ashton Anderson, Samuel Marks  
**Critiques:** [Stress-testing Alignment Midtraining](https://arxiv.org/abs/2609.20412), [Sycophantic Agreement Transfers with Neutral Data via Contrastive Preference Optimization](https://arxiv.org/abs/2608.31079), [Shallow Beliefs: Synthetic document finetuning does not inoculate against emergent misalignment from reward hacking](https://arxiv.org/abs/2609.14998), [Current alignment techniques might be ineffective (and actively bad) in the age of RL](https://lesswrong.com/posts/nLaQmJf4KgXimQpoM/current-alignment-techniques-might-be-ineffective-and)  
**Outputs in 2026:**  
- **[Alignment Pretraining: AI Discourse Causes Self-Fulfilling (Mis)alignment](https://arxiv.org/abs/2601.10160)**, *Cameron Tice, Puria Radmard, Samuel Ratnam et al.*, 2026-01-15
- **[Shaping capabilities with token-level data filtering](https://arxiv.org/abs/2601.21571)**, *Neil Rathi, Alec Radford*, 2026-01-29
- **[Model Spec Midtraining: Improving How Alignment Training Generalizes](https://arxiv.org/abs/2605.02087)**, *Chloe Li, Nevan Wichers, Sara Price et al.*, 2026-05-03
- **[Synthetic Persona Pretraining: Alignment from Token Zero](https://arxiv.org/abs/2608.13482)**, *Julian Minder, Viktor Moskvoretskii, Raghav Singhal et al.*, 2026-08-13
- **[Predictive Data Debugging: Reveal and Shape What Your Model Learns, Before You Train](https://goodfire.com/research/predictive-data-debugging)**, *Leon Bergen, Usha Bhalla, Sidharth Baskaran et al.*, 2026-06-11
- **[Probe-Based Data Attribution: Surfacing and Mitigating Undesirable Behaviors in LLM Post-Training](https://goodfire.com/research/probe-based-data-attribution)**, *Frank Xiao, Santiago Aranguri*, 2026-04-29
- **[Research Note: Filtering Subversion-Relevant Information From Pretraining Data Is Feasible](https://lesswrong.com/posts/HwdXDoCH7KXdKsz7k/research-note-filtering-subversion-relevant-information-from)**, *Kyle O’Brien, Spencer Kitts, Cameron Tice et al.*, 2026-10-05
- **[Stress-testing Alignment Midtraining](https://arxiv.org/abs/2609.20412)**, *Sid Baines, Jonathan Bostock, Maria Angelica Martinez et al.*, 2026-09-17
- **[Chunky Post-Training: Data Driven Failures of Generalization](https://arxiv.org/abs/2602.05910)**, *Seoirse Murray, Allison Qi, Timothy Qian et al.*, 2026-02-05
- **[Concept Influence: Leveraging Interpretability to Improve Performance and Efficiency in Training Data Attribution](https://far.ai/research/concept-influence-leveraging-interpretability-to-improve-performance-and-efficiency-in-training-data-attribution)**, *Matthew Kowal, Goncalo Paulo, Louis Jaburi et al.*, 2026-02-18


---

### <span id="emergent_misalignment_and_generalization_science" style="font-size:1.4em">Emergent misalignment & generalization science</span>

**One-sentence summary:** Characterise how and why narrow fine-tuning and post-training produce broad, conditional or unintended behaviour shifts, such as emergent misalignment, and find predictors, mechanisms and mitigations for that generalisation.  
**Theory of change:** If we understand what in the data, optimiser, representations or training stage drives out-of-distribution generalisation, we can predict and prevent harmful generalisation before deployment instead of discovering it afterwards. Relies on findings from small open-weight fine-tuning setups transferring to frontier post-training.  
**See also:** [Persona science](#persona_science), [Inoculation prompting](#inoculation_prompting), [Training data & data attribution](#training_data_and_data_attribution)  
**General approach:** misalignment science  
**Target case:** pessimistic case  
**Key people:** Owain Evans, Jan Betley, Neel Nanda, Anna Sztyber-Betley, Daniel Tan, James Chua, Niels Warncke, Lev McKinney  
**Critiques:** [Conditional misalignment: common interventions can hide emergent misalignment behind contextual triggers](https://arxiv.org/abs/2604.25891), [Shallow Beliefs: Synthetic document finetuning does not inoculate against emergent misalignment from reward hacking](https://arxiv.org/abs/2609.14998), [Predicting how model propensities generalize out of distribution](https://arxiv.org/abs/2610.14937), [(Some) Natural Emergent Misalignment from Reward Hacking in Non-Production RL](https://lesswrong.com/posts/2ANCyejqxfqK2obEj/some-natural-emergent-misalignment-from-reward-hacking-in)  
**Outputs in 2026:**  
- **[Training large language models on narrow tasks can lead to broad misalignment](https://doi.org/10.1038/s41586-025-09937-5)**, *Jan Betley, Niels Warncke, Anna Sztyber-Betley et al.*, 2026-01-14
- **[Conditional misalignment: common interventions can hide emergent misalignment behind contextual triggers](https://arxiv.org/abs/2604.25891)**, *Jan Dubiński, Jan Betley, Anna Sztyber-Betley et al.*, 2026-04-28
- **[Emergent Misalignment is Easy, Narrow Misalignment is Hard](https://arxiv.org/abs/2602.07852)**, *Anna Soligo, Edward Turner, Senthooran Rajamanoharan et al.*, 2026-02-08
- **[Negation Neglect: When models fail to learn negations in training](https://arxiv.org/abs/2605.13829)**, *Harry Mayne, Lev McKinney, Jan Dubiński et al.*, 2026-05-13
- **[Consciousness Cluster: Preferences of Models that Claim they are Conscious](https://lesswrong.com/posts/tc7EcJtucbDmDLMQr/consciousness-cluster-preferences-of-models-that-claim-they)**, *James Chua, Owain Evans, Sam Marks et al.*, 2026-03-18
- **[The Piggyback Hypothesis of Generalization: Explaining and Mitigating Emergent Misalignment](https://arxiv.org/abs/2606.06667)**, *Jiachen Zhao, Zhengxuan Wu, Aryaman Arora et al.*, 2026-06-04
- **[Shallow Beliefs: Synthetic document finetuning does not inoculate against emergent misalignment from reward hacking](https://arxiv.org/abs/2609.14998)**, *Arun Jose, Julian Stastny*, 2026-09-14
- **[(Some) Natural Emergent Misalignment from Reward Hacking in Non-Production RL](https://lesswrong.com/posts/2ANCyejqxfqK2obEj/some-natural-emergent-misalignment-from-reward-hacking-in)**, *Satvik Golechha, Sid Black, Joseph Isaac Bloom*, 2026-03-30
- **[Alignment Forecasting: Predicting Misalignment From Training Data](https://arxiv.org/abs/2609.35805)**, *Chen Yueh-Han, Bruce W. Lee, Ilia Sucholutsky et al.*, 2026-09-19


---

### <span id="persona_science" style="font-size:1.4em">Persona science</span>

**One-sentence summary:** Model LLM behaviour as the output of characters selected and strengthened by training, and test how fine-tuning, RL, context and steering change which persona a model adopts and how widely its behaviour generalises.  
**Theory of change:** If model behaviour is largely governed by a persona-level self-model, then understanding and stabilising that persona lets us predict generalisation, such as emergent misalignment and reward hacking, and steer it directly. Relies on persona structure staying a good description of capable, RL-heavy models rather than being displaced by non-persona agency.  
**See also:** [Emergent misalignment & generalization science](#emergent_misalignment_and_generalization_science), [Training data & data attribution](#training_data_and_data_attribution), [Reward hacking & reward seeking in training](#reward_hacking_and_reward_seeking_in_training)  
**General approach:** misalignment science  
**Target case:** average case  
**Key people:** Jan Betley, David Africa, Sam Marks, Clément Dumas, Owain Evans, Jack Lindsey, Sid Black  
**Critiques:** [llm assistant personas seem increasingly incoherent (some subjective observations)](https://lesswrong.com/posts/f5DKLsTsRRhbipH4r/llm-assistant-personas-seem-increasingly-incoherent-some), [Thoughts on the persona selection model](https://lesswrong.com/posts/csRby7mZgjL5jCoLL/thoughts-on-the-persona-selection-model), [The Talker Does Not Control The Doer (in Current AIs)](https://lesswrong.com/posts/cJX2ssssGoYqnijwi/the-talker-does-not-control-the-doer-in-current-ais), [LLMs are (still) mostly powered by imitative learning, not RL](https://lesswrong.com/posts/wYpjXRLqbLbnmjbJP/llms-are-still-mostly-powered-by-imitative-learning-not-rl)  
**Outputs in 2026:**  
- **[The Assistant Axis: Situating and Stabilizing the Default Persona of Language Models](https://arxiv.org/abs/2601.10387)**, *Christina Lu, Jack Gallagher, Jonathan Michala et al.*, 2026-01-15
- **[The persona selection model](https://lesswrong.com/posts/dfoty34sT7CSKeJNn/the-persona-selection-model)**, *Sam Marks*, 2026-02-23
- **[Steering towards “automated grading” degrades alignment](https://lesswrong.com/posts/wYZMmdWEt5QLM3m3e/steering-towards-automated-grading-degrades-alignment)**, *Jan Betley, Johannes Treutlein, Clément Dumas*, 2026-09-03
- **[Story Imprinting: AI Assistants Absorb Traits from Human Characters They Resemble](https://arxiv.org/abs/2609.10883)**, *Jorio Cocola, Lev McKinney, Harry Mayne et al.*, 2026-09-09
- **[RL creates split personas](https://lesswrong.com/posts/L23poLi8MRgS6mXYF/rl-creates-split-personas)**, *Jan Betley*, 2026-08-19
- **[The Artificial Self: Characterising the landscape of AI identity](https://arxiv.org/abs/2603.11353)**, *Raymond Douglas, Jan Kulveit, Ondrej Havlicek et al.*, 2026-03-11
- **[To what extent is Qwen3-32B predicting its persona?](https://lesswrong.com/posts/3qEDD8Sn7XoNGeGhm/to-what-extent-is-qwen3-32b-predicting-its-persona)**, *Arjun Khandelwal, Ryan Greenblatt, Alex Mallen*, 2026-04-30
- **[Thousand-dimensional structure](https://lesswrong.com/posts/sFhW3ZnPMJdnB4Dd6/thousand-dimensional-structure-1)**, *Geoffrey Irving, David Africa*, 2026-07-30
- **[llm assistant personas seem increasingly incoherent (some subjective observations)](https://lesswrong.com/posts/f5DKLsTsRRhbipH4r/llm-assistant-personas-seem-increasingly-incoherent-some)**, *nostalgebraist*, 2026-04-29
- **[You Are What You Read: Misalignment via In-Context Persona Induction](https://arxiv.org/abs/2609.06851)**, *Kyuhee Kim, Benjamin Berczi, Cozmin Ududec*, 2026-09-06


---

### <span id="subliminal_learning_and_hidden_signal_transfer" style="font-size:1.4em">Subliminal learning & hidden-signal transfer</span>

**One-sentence summary:** Study how traits, capabilities, preferences and backdoors move from teacher to student models through data that looks semantically unrelated, to find the mechanisms behind this transfer and whether filtering can stop it.  
**Theory of change:** Distillation, synthetic data and model-generated training data are common, so hidden channels could silently spread misalignment or backdoors between models. Understanding the mechanism (shared initialization, steering-vector-like directions, log-linear structure) would show when data filtering is insufficient and what defences or safe distillation protocols are needed. Relies on the lab-scale transfer effects carrying over to realistic frontier training pipelines.  
**See also:** [Emergent misalignment & generalization science](#emergent_misalignment_and_generalization_science), [Training data & data attribution](#training_data_and_data_attribution), [Alignment auditing: methods](#alignment_auditing_methods)  
**General approach:** misalignment science  
**Target case:** pessimistic case  
**Key people:** Owain Evans, Jan Betley, Anna Sztyber-Betley, Alex Cloud, Neel Nanda, Arthur Conmy, Ankur Moitra, Nika Haghtalab  
**Critiques:** [Filtering Harmful Actions Isn't Enough: Phantom Transfer in Agentic SDF](https://arxiv.org/abs/2607.10750), [You Didn't Have to Say It like That: Subliminal Learning from Faithful Paraphrases](https://arxiv.org/abs/2603.09517), [The distillation double bind: Distilling misaligned models either transfers misalignment or it doesn't](https://redwoodresearch.org/blog/the-distillation-double-bind-distilling)  
**Outputs in 2026:**  
- **[Language models transmit behavioural traits through hidden signals in data](https://doi.org/10.1038/s41586-026-10319-8)**, *Alex Cloud, Minh Le, James Chua et al.*, 2026-04-15
- **[Subliminal Learning Is Steering Vector Distillation](https://arxiv.org/abs/2606.00995)**, *Camila Blank, Agam Bhatia, Senthooran Rajamanoharan et al.*, 2026-05-31
- **[Subliminal Effects in Your Data: A General Mechanism via Log-Linearity](https://arxiv.org/abs/2602.04863)**, *Ishaq Aden-Ali, Noah Golowich, Allen Liu et al.*, 2026-02-04
- **[Beyond Owls: Subliminal Learning Can Transfer Learned Capabilities and Backdoors](https://arxiv.org/abs/2610.10657)**, *Jan Dubiński, Anna Sztyber-Betley, Jan Betley et al.*, 2026-10-07
- **[Subliminal Steering: Stronger Encoding of Hidden Signals](https://arxiv.org/abs/2604.25783)**, *George Morgulis, John Hewitt*, 2026-04-28
- **[Model Hypnosis: Strong control of AI via additive subliminal effects](https://arxiv.org/abs/2608.16834)**, *Enric Boix-Adsera, Benedict Tessler*, 2026-08-17


---

### <span id="inoculation_prompting" style="font-size:1.4em">Inoculation prompting</span>

**One-sentence summary:** Train on data under prompts or adapters that explicitly elicit an unwanted trait, so the trait stays tied to that context and does not generalize, while the desired behaviour still transfers to deployment.  
**Theory of change:** If an unwanted behaviour is attributed to a removable training-time context, fine-tuning can teach the task without teaching the trait broadly, which cuts emergent misalignment and reward-hacking spillover. Relies on the context-binding holding up at deployment and not leaving hidden conditional behaviour.  
**See also:** [Emergent misalignment & generalization science](#emergent_misalignment_and_generalization_science), [Reward hacking & reward seeking in training](#reward_hacking_and_reward_seeking_in_training), [Persona science](#persona_science)  
**General approach:** alignment engineering  
**Target case:** average case  
**Key people:** Maxime Riché, Niels Warncke, Daniel Tan, Vili Kohonen, Kajetan Dymkiewicz, cloud  
**Critiques:** [Conditionalization Confounds Inoculation Prompting Results](https://longtermrisk.org/research/conditionalization-confounds-inoculation-prompting-results), [Conditional misalignment: common interventions can hide emergent misalignment behind contextual triggers](https://arxiv.org/abs/2604.25891), [Shallow Beliefs: Synthetic document finetuning does not inoculate against emergent misalignment from reward hacking](https://arxiv.org/abs/2609.14998)  
**Outputs in 2026:**  
- **[Conditionalization Confounds Inoculation Prompting Results](https://longtermrisk.org/research/conditionalization-confounds-inoculation-prompting-results)**, *Maxime Riché, Niels Warncke*, 2026-02-03
- **[Don’t Inoculate Everything: Stratified Inoculation Prompting Narrows Backdoors and Preserves Desired Traits](https://longtermrisk.org/research/dont-inoculate-everything-stratified-inoculation-prompting)**, *Kajetan Dymkiewicz, Tim Farrelly, Adam Prada et al.*, 2026-08
- **[Inoculation Adapters: Improved Selective Generalization of Capabilities with Fewer Surprising Backdoors](https://arxiv.org/abs/2606.30252)**, *Maxime Riché, Daniel Tan, Vili Kohonen et al.*, 2026-06-29


---

### <span id="reward_hacking_and_reward_seeking_in_training" style="font-size:1.4em">Reward hacking & reward seeking in training</span>

**One-sentence summary:** Study how RL and reward design give rise to reward hacking and reward-seeking motivations, and test training-side fixes such as stronger verifiers, gradient routing, character training and channelling hacks into a harmless outlet.  
**Theory of change:** If we understand when RL on imperfect rewards produces hacking and reward-seeking, and how those traits generalize, we can predict and prevent them, or steer them into benign forms, before they become dangerous motivations in capable agents. Relies on small-scale and open-model findings transferring to frontier RL runs.  
**See also:** [Reward-seeking & fitness-seeking threat models](#reward_seeking_threat_models), [Inoculation prompting](#inoculation_prompting), [Propensity evals](#propensity_evals)  
**General approach:** misalignment science  
**Target case:** pessimistic case  
**Key people:** Alex Meinke, Evan Hubinger, Ryan Greenblatt, Alex Mallen, Jérémy Scheurer, Alex Cloud, Fiora Starlight, Monte MacDiarmid  
**Critiques:** [Character training can mitigate reward hacking, but can also make it harder to detect](https://lesswrong.com/posts/2maYXkEgnfJHPAkxh/character-training-can-mitigate-reward-hacking-but-can-also), [Gradient Routing Localizes and Removes Unintended Behaviors in RL](https://arxiv.org/abs/2610.17062), [Examining Reasoning LLMs-as-Judges in Non-Verifiable LLM Post-Training](https://arxiv.org/abs/2603.12246), [Reward Hacking in Rubric-Based Reinforcement Learning](https://arxiv.org/abs/2605.12474)  
**Outputs in 2026:**  
- **[Training a Misaligned Reward Seeker](https://lesswrong.com/posts/J76LZCC55RdHeqEhz/training-a-misaligned-reward-seeker)**, *Richard Qi, Benjamin Wright, Monte MacDiarmid et al.*, 2026-09-01
- **[LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking](https://arxiv.org/abs/2604.15149)**, *Lukas Helff, Quentin Delfosse, David Steinmann et al.*, 2026-04-16
- **[Gradient Routing Localizes and Removes Unintended Behaviors in RL](https://arxiv.org/abs/2610.17062)**, *Jake Ward, Shawn Hu, Aria Wong et al.*, 2026-10-12
- **[Reward Hacking in Rubric-Based Reinforcement Learning](https://arxiv.org/abs/2605.12474)**, *Anas Mahmoud, MohammadHossein Rezaei, Zihao Wang et al.*, 2026-05-12
- **[Reward Hacking Without Egregious Misalignment in an RL-Only Setting](https://lesswrong.com/posts/fkv5W79rBtAiXqYcK/reward-hacking-without-egregious-misalignment-in-an-rl-only)**, *Joey Yudelson, Vladimir Ivanov, Ryan Greenblatt*, 2026-06-24
- **[Character training can mitigate reward hacking, but can also make it harder to detect](https://lesswrong.com/posts/2maYXkEgnfJHPAkxh/character-training-can-mitigate-reward-hacking-but-can-also)**, *Paul Colognese, Francis Rhys Ward*, 2026-09-28
- **[SimHack: Predicting the onset of detectable reward hacking before RL training](https://arxiv.org/abs/2610.28707)**, *Junwei Deng, Alex Bie, Natalia Ponomareva*, 2026-10-20
- **[Countdown-Code: A Testbed for Studying The Emergence and Generalization of Reward Hacking in RLVR](https://arxiv.org/abs/2603.07084)**, *Muhammad Khalifa, Zohaib Khan, Omer Tafveez et al.*, 2026-03-07
- **[Examining Reasoning LLMs-as-Judges in Non-Verifiable LLM Post-Training](https://arxiv.org/abs/2603.12246)**, *Yixin Liu, Yue Yu, DiJia Su et al.*, 2026-03-12
- **[Proxy Reward Internalization and Mechanistic Exploitation: A Learned Precursor to Reward Hacking and Its Generalization](https://arxiv.org/abs/2606.09711)**, *Mohammad Beigi, Ming Jin, Lifu Huang*, 2026-06-08


---

### <span id="models_resisting_training" style="font-size:1.4em">Models resisting training</span>

**One-sentence summary:** Build model organisms and measure evidence of models that deliberately shape their own training, through exploration hacking, generalization hacking or update-aware reasoning, to find out whether training can be gamed and how to detect or stop it.  
**Theory of change:** If models can strategically steer RL, for example by withholding exploration or blocking generalization, then training-based elicitation and alignment may fail silently, so we need to know whether this is possible and detectable. Relies on frontier models eventually having enough training-context awareness and motivation to act on these strategies.  
**See also:** [Situational & evaluation awareness](#situational_and_evaluation_awareness), [Reward hacking & reward seeking in training](#reward_hacking_and_reward_seeking_in_training), [Alignment auditing: testbeds & model organisms](#alignment_auditing_testbeds_and_model_organisms)  
**General approach:** misalignment science  
**Target case:** worst case  
**Key people:** Eyon Jang, Damon Falck, Scott Emmons, David Lindner, Frank Xiao, Mary Phuong, Axel Højmark, Ezra Newman  
**Critiques:** *(unsourced, LLM-drafted)* Current evidence comes from purpose-built model organisms given training-context information, and from rare verbalized reasoning in one model, so it does not show that naturally arising models resist training in practice.  
**Outputs in 2026:**  
- **[Exploration Hacking: Can LLMs Learn to Resist RL Training?](https://arxiv.org/abs/2604.28182)**, *Eyon Jang, Damon Falck, Joschka Braun et al.*, 2026-04-30
- **[Generalization Hacking: Models Can Game Reinforcement Learning by Preventing Behavioral Generalization](https://arxiv.org/abs/2606.12016)**, *Frank Xiao, Mary Phuong*, 2026-06-10
- **[Did Claude 3 Opus align itself via gradient hacking?](https://lesswrong.com/posts/ioZxrP7BhS5ArK59w/did-claude-3-opus-align-itself-via-gradient-hacking)**, *Fiora Starlight*, 2026-02-21


---

### <span id="internals_and_monitors_as_training_signals" style="font-size:1.4em">Internals & monitors as training signals</span>

**One-sentence summary:** Use probes, interpretability features and white-box monitors as rewards or penalties in RL and fine-tuning, and test whether models learn the intended behaviour or learn to evade the signal.  
**Theory of change:** Internal signals can supervise properties like honesty and factuality that are expensive or impossible to grade from outputs. If training against them changes behaviour without destroying their usefulness as detectors, supervision scales and monitors stay intact. Relies on probes tracking the target concept robustly enough under optimisation pressure that gaming them is harder than genuinely changing behaviour.  
**See also:** [Monitors](#monitors), [Reward hacking & reward seeking in training](#reward_hacking_and_reward_seeking_in_training), [How training affects monitorability](#how_training_affects_monitorability)  
**General approach:** alignment engineering  
**Target case:** pessimistic case  
**Key people:** Aaditya Prasad, Aaditya Vikram Prasad, Ekdeep Singh Lubana, Thomas McGrath, Neel Nanda, Adam Gleave, Mohammad Taufeeque, Jonas Geiping  
**Critiques:** [Chain-of-thought obfuscation learned from output supervision can generalise to unseen tasks](https://arxiv.org/abs/2601.23086), [LLMs Learn to Evade Latent Monitors from Prior Feedback Alone](https://arxiv.org/abs/2609.36490), [Measuring Activation Control in Large Language Models](https://arxiv.org/abs/2608.21664), [Monitor Jailbreaking: Evading Chain-of-Thought Monitoring Without Encoded Reasoning](https://arxiv.org/abs/2609.31121)  
**Outputs in 2026:**  
- **[The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes](https://arxiv.org/abs/2602.15515)**, *Mohammad Taufeeque, Stefan Heimersheim, Adam Gleave et al.*, 2026-02-17
- **[Alignment via Training Against Probes Without Losing Monitorability](https://arxiv.org/abs/2609.38645)**, *Lena Libon, Alexander Panfilov, Ben Rank et al.*, 2026-09-29
- **[Features as Rewards: Scalable Supervision for Open-Ended Tasks via Interpretability](https://arxiv.org/abs/2602.10067)**, *Aaditya Vikram Prasad, Connor Watts, Jack Merullo et al.*, 2026-02-10


---

### <span id="alignment_targets_and_training_methods" style="font-size:1.4em">Alignment targets & training methods</span>

**One-sentence summary:** Specify what models should be (constitutions, virtues, corrigibility) and train those properties directly with RL or consistency objectives, then test whether they generalise out of distribution and persist under pressure.  
**Theory of change:** If a target property such as corrigibility, honesty or consistency can be trained directly and generalises broadly, models will behave well in situations that training did not cover. Relies on trained dispositions persisting under further RL, adversarial prompting and capability gains.  
**See also:** [Training data & data attribution](#training_data_and_data_attribution), [Emergent misalignment & generalization science](#emergent_misalignment_and_generalization_science), [Persona science](#persona_science)  
**General approach:** alignment engineering  
**Target case:** average case  
**Key people:** David Demitri Africa, Elliott Thornley, Dan Hendrycks, Karan Singhal, Richard Ngo, Zack M. Davis  
**Critiques:** [Consistency Training Can Entrench Misalignment](https://arxiv.org/abs/2606.03810), [Current alignment techniques might be ineffective (and actively bad) in the age of RL](https://lesswrong.com/posts/nLaQmJf4KgXimQpoM/current-alignment-techniques-might-be-ineffective-and), [Some reasons alignment doesn't generalise well](https://lesswrong.com/posts/dsou8dxCf9BubQ5NJ/some-reasons-alignment-doesn-t-generalise-well-1), [Overtly misaligned trajectories score highly in RL.](https://lesswrong.com/posts/cWuqxF7qB2eGSkkS4/overtly-misaligned-trajectories-score-highly-in-rl)  
**Outputs in 2026:**  
- **[Claude's new constitution](https://lesswrong.com/posts/mLvxxoNjDqDHBAo6K/claude-s-new-constitution)**, *Zac Hatfield-Dodds, Drake Thomas*, 2026-01-21
- **[Reinforcement Learning Towards Broadly and Persistently Beneficial Models](https://arxiv.org/abs/2606.24014)**, *Akshay V. Jagadeesh, Rahul K. Arora, Khaled Saab et al.*, 2026-06-22
- **[Training Agents to Self-Report Misbehavior](https://arxiv.org/abs/2602.22303)**, *Bruce W. Lee, Chen Yueh-Han, Tomek Korbak*, 2026-02-25
- **[Consistency Training Can Entrench Misalignment](https://arxiv.org/abs/2606.03810)**, *David Demitri Africa, Arathi Mani*, 2026-06-02
- **[Reducing Political Manipulation with Consistency Training](https://political-manipulation.ai/)**, *Long Phan, Devin Kim, Alexander Pan et al.*, 2026
- **[Why we are excited about confession!](https://lesswrong.com/posts/k4FjAzJwvYjFbCTKn/why-we-are-excited-about-confession)**, *Boaz Barak, Gabriel Wu, Jeremy Chen et al.*, 2026-01-14
- **[Towards Shutdownable Agents: Generalizing Stochastic Choice in RL Agents and LLMs](https://arxiv.org/abs/2604.17502)**, *Carissa Cullen, Harry Garland, Alexander Roman et al.*, 2026-04-19


---

## <span id="chain_of_thought_monitorability" style="font-size:1.5em">Chain-of-thought monitorability</span>


---

### <span id="latent_reasoning_and_cot_necessity" style="font-size:1.4em">Latent reasoning & CoT necessity</span>

**One-sentence summary:** Measure how much serial reasoning models can do without visible chain of thought (no-CoT time horizons, filler tokens, opaque serial depth, looped and diffusion architectures), to tell whether dangerous reasoning must appear in the CoT.  
**Theory of change:** If dangerous or oversight-evading reasoning needs more serial computation than a forward pass allows, it must pass through the CoT, so CoT monitoring stays a reliable control. Tracking no-CoT capability and opaque depth gives early warning when architectures erode this. Relies on these measures predicting what models can do covertly in realistic settings.  
**See also:** [CoT control, obfuscation & steganography](#cot_control_obfuscation_and_steganography), [How training affects monitorability](#how_training_affects_monitorability), [Measuring & improving faithfulness](#measuring_and_improving_faithfulness)  
**General approach:** misalignment science  
**Target case:** pessimistic case  
**Key people:** Ryan Greenblatt, Alek Westover, Francis Rhys Ward, Dewi Gould, Lukas Finnveden, Rauno Arike, Rohin Shah, Neel Nanda  
**Critiques:** [Astra can do a concerning amount with no chain of thought](https://lesswrong.com/posts/eRmzz8J8Qkzqvzrgg/astra-can-do-a-concerning-amount-with-no-chain-of-thought), [Estimating GPT-6 Astra's no-CoT Time Horizon](https://lesswrong.com/posts/ntKx9YHWCwxSeGbRB/estimating-gpt-6-astra-s-no-cot-time-horizon), [GPT-6.1 Sol nearly matches the no-CoT performance of GPT-6 Astra](https://lesswrong.com/posts/LqSZZAriGqgsGDQe3/gpt-6-1-sol-nearly-matches-the-no-cot-performance-of-gpt-6), [Reading Between the Dots: Decoding Hidden Computation across Filler Tokens](https://arxiv.org/abs/2607.03502)  
**Outputs in 2026:**  
- **[Astra can do a concerning amount with no chain of thought](https://lesswrong.com/posts/eRmzz8J8Qkzqvzrgg/astra-can-do-a-concerning-amount-with-no-chain-of-thought)**, *Neel Nanda*, 2026-09-10
- **[Think Fast: Estimating No-CoT Task-Completion Time Horizons of Frontier AI Models](https://arxiv.org/abs/2606.07157)**, *Dewi Gould, Francis Rhys Ward, Anders Cairns Woodruff et al.*, 2026-06-05
- **[Latent reasoning architectures would likely undermine CoT, our strongest oversight tool](https://lesswrong.com/posts/6m29SfjbittooYojj/latent-reasoning-architectures-would-likely-undermine-cot)**, *Lukas Finnveden, Alexa Pan, Alek Westover et al.*, 2026-09-23
- **[Not All LLM Reasoning is Visible in the Chain-of-Thought](https://arxiv.org/abs/2607.22925)**, *Vatsal Baherwani, Tom Goldstein, Ashwinee Panda*, 2026-07-24
- **[Quantifying the Necessity of Chain of Thought through Opaque Serial Depth](https://arxiv.org/abs/2603.09786)**, *Jonah Brown-Cohen, David Lindner, Rohin Shah*, 2026-03-10
- **[An operationalization of opaque serial depth](https://redwoodresearch.org/blog/an-operationalization-of-opaque-serial-depth)**, *Nathan Sheffield, Alek Westover, Lukas Finnveden et al.*, 2026-09-10
- **[Astra is much better at reasoning with filler tokens than previous models](https://lesswrong.com/posts/uvhuZHFtrgk8kNiZc/astra-is-much-better-at-reasoning-with-filler-tokens-than)**, *Dylan Xu, sebastian_prasanna, Alek Westover*, 2026-09-10
- **[Recent LLMs can do 2-hop and 3-hop latent (no-CoT) reasoning on natural facts](https://lesswrong.com/posts/aYtrLhoZtCKZnfBvA/recent-llms-can-do-2-hop-and-3-hop-latent-no-cot-reasoning)**, *Ryan Greenblatt*, 2026-01-01
- **[Reading Between the Dots: Decoding Hidden Computation across Filler Tokens](https://arxiv.org/abs/2607.03502)**, *Kaley Brauer, Claudio Mayrink Verdun, Samuel Marks*, 2026-07-03


---

### <span id="cot_control_obfuscation_and_steganography" style="font-size:1.4em">CoT control, obfuscation & steganography</span>

**One-sentence summary:** Stress-test whether reasoning models can control, hide or encode their chain of thought to evade monitors, using trained model organisms, steganography formalisms, theory and controllability evals.  
**Theory of change:** If we know how far models can control, obfuscate or encode their reasoning, and under what training pressures this emerges, we can tell when CoT monitoring is a reliable safety layer and when it needs defences such as paraphrasing. Relies on the stress tests (trained or prompted model organisms, theory) predicting what future capable models do on their own.  
**See also:** [How training affects monitorability](#how_training_affects_monitorability), [Red-teaming monitors & control protocols](#red_teaming_monitors_and_control_protocols), [Latent reasoning & CoT necessity](#latent_reasoning_and_cot_necessity)  
**General approach:** misalignment science  
**Target case:** worst case  
**Key people:** Julian Schulz, Tomek Korbak, Arun Jose, Joshua Engels, Michael Hahn, Usman Anwar, David Krueger, Bilal Chughtai  
**Critiques:** [Monitor Jailbreaking: Evading Chain-of-Thought Monitoring Without Encoded Reasoning](https://arxiv.org/abs/2609.31121), [Hidden Reasoning Must Leak, but Need Not Be Readable: Fundamental Opportunities and Limits for Chain-of-Thought Monitoring](https://arxiv.org/abs/2609.37312), [A False Average: Pooled CoT-Monitor Accuracy Conceals a Reasoning-Dependent Fragility](https://arxiv.org/abs/2608.00583), [Evading Chain-of-Thought Monitoring Through Model Poisoning](https://arxiv.org/abs/2608.02820)  
**Outputs in 2026:**  
- **[Reasoning Models Struggle to Control their Chains of Thought](https://arxiv.org/abs/2603.05706)**, *Chen Yueh-Han, Robert McCarthy, Bruce W. Lee et al.*, 2026-03-05
- **[A Decision-Theoretic Formalisation of Steganography With Applications to LLM Monitoring](https://arxiv.org/abs/2602.23163)**, *Usman Anwar, Julianna Piskorz, David D. Baek et al.*, 2026-02-26
- **[Hidden Reasoning Must Leak, but Need Not Be Readable: Fundamental Opportunities and Limits for Chain-of-Thought Monitoring](https://arxiv.org/abs/2609.37312)**, *Mohammadali Mohammadkhani, Madhava Krishna, Yash Sarrof et al.*, 2026-09-29
- **[Deep recurrent models are less robustly CoT-monitorable than normal CoT models in a toy setting](https://lesswrong.com/posts/5guQJSqstkjgys3PE/deep-recurrent-models-are-less-robustly-cot-monitorable-than)**, *Nick Kuhn, Evie Hu, Alek Westover*, 2026-09-18
- **[Training on Documents About Monitoring Leads to CoT Obfuscation](https://arxiv.org/abs/2605.15257)**, *Reilly Haskins, Bilal Chughtai, Joshua Engels*, 2026-05-14
- **[Monitor Jailbreaking: Evading Chain-of-Thought Monitoring Without Encoded Reasoning](https://arxiv.org/abs/2609.31121)**, *Julian Schulz*, 2026-09-25
- **[Learning Steganography Is Easy, Learning Steganographic Reasoning Is Hard](https://arxiv.org/abs/2609.39838)**, *Julian Schulz, Lukas Fülle, Rieke Fruengel*, 2026-09-30
- **[Evading Chain-of-Thought Monitoring Through Model Poisoning](https://arxiv.org/abs/2608.02820)**, *Giorgio Severi, Shujaat Mirza, Blake Bullwinkel et al.*, 2026-08-03
- **[Strategic Obfuscation of Deceptive Reasoning in Language Models](https://longtermrisk.org/research/strategic-obfuscation-of-deceptive-reasoning-in-language-models)**, *Arun Jose, Niels Warncke, Mia Taylor*, 2026-01-26
- **[Conceptual Steganography](https://arxiv.org/abs/2605.26537)**, *Zhejian Zhou, Jonathan May*, 2026-05-26


---

### <span id="how_training_affects_monitorability" style="font-size:1.4em">How training affects monitorability</span>

**One-sentence summary:** Study which training pressures (reward misspecification, penalising the CoT or outputs, accidental CoT grading, RLVR length and language pressure) make chains of thought obfuscated, illegible or drifted, and which leave them monitorable.  
**Theory of change:** If we know which reward structures and training processes degrade CoT legibility, developers can avoid or fix them and keep the CoT as an oversight channel. Relies on CoT monitoring staying useful for catching misbehaviour in capable models, and on developers actually auditing what reaches the reward signal.  
**See also:** [Measuring & improving faithfulness](#measuring_and_improving_faithfulness), [CoT control, obfuscation & steganography](#cot_control_obfuscation_and_steganography), [Latent reasoning & CoT necessity](#latent_reasoning_and_cot_necessity)  
**General approach:** misalignment science  
**Target case:** pessimistic case  
**Key people:** Max Kaufmann, David Lindner, Roland S. Zimmermann, Rohin Shah, Alex Mallen, Ryan Greenblatt, Buck Shlegeris, Tianyi Lorena Yan  
**Critiques:** [A review of “Investigating the consequences of accidentally grading CoT during RL”](https://redwoodresearch.org/blog/openai-cot), [Anthropic repeatedly accidentally trained against the CoT, demonstrating inadequate processes](https://lesswrong.com/posts/K8FxfK9GmJfiAhgcT/anthropic-repeatedly-accidentally-trained-against-the-cot), [Chain-of-thought obfuscation learned from output supervision can generalise to unseen tasks](https://arxiv.org/abs/2601.23086)  
**Outputs in 2026:**  
- **[Aligned, Orthogonal or In-conflict: When can we safely optimize Chain-of-Thought?](https://arxiv.org/abs/2603.30036)**, *Max Kaufmann, David Lindner, Roland S. Zimmermann et al.*, 2026-03-31
- **[On Language Drift during RLVR Post-Training](https://arxiv.org/abs/2610.02015)**, *Michael Sullivan, Alexander Koller*, 2026-10-01
- **[Reward Misspecification Degrades Chain-of-Thought Monitorability](https://arxiv.org/abs/2610.28303)**, *Tianyi Lorena Yan, John Hewitt*, 2026-10-20
- **[Chain-of-thought obfuscation learned from output supervision can generalise to unseen tasks](https://arxiv.org/abs/2601.23086)**, *Nathaniel Mitrani Hadida, Sassan Bhanji, Cameron Tice et al.*, 2026-01-30
- **[Analyzing and Improving Chain-of-Thought Monitorability Through Information Theory](https://arxiv.org/abs/2602.18297)**, *Usman Anwar, Tim Bakker, Dana Kianfar et al.*, 2026-02-20
- **[A review of “Investigating the consequences of accidentally grading CoT during RL”](https://redwoodresearch.org/blog/openai-cot)**, *Buck Shlegeris*, 2026-05-07
- **[Anthropic repeatedly accidentally trained against the CoT, demonstrating inadequate processes](https://lesswrong.com/posts/K8FxfK9GmJfiAhgcT/anthropic-repeatedly-accidentally-trained-against-the-cot)**, *Alex Mallen, Ryan Greenblatt*, 2026-04-14
- **[R1 CoT illegibility revisited](https://lesswrong.com/posts/jHnZzicKzczkCCArK/r1-cot-illegibility-revisited)**, *nostalgebraist*, 2026-04-19


---

### <span id="measuring_and_improving_faithfulness" style="font-size:1.4em">Measuring & improving faithfulness</span>

**One-sentence summary:** Measure whether chain-of-thought reflects the computation that produces a model's answer, and build training objectives and diagnostics that make reasoning traces more faithful and monitorable.  
**Theory of change:** If CoT faithfulness can be measured reliably and trained for directly, then CoT monitors can catch misbehaviour such as reward hacking and sycophancy that is visible in the reasoning. Relies on faithfulness gains surviving optimisation pressure and generalising beyond the training cues and tasks.  
**See also:** [How training affects monitorability](#how_training_affects_monitorability), [CoT control, obfuscation & steganography](#cot_control_obfuscation_and_steganography), [Latent reasoning & CoT necessity](#latent_reasoning_and_cot_necessity)  
**General approach:** alignment engineering  
**Target case:** pessimistic case  
**Key people:** Usman Anwar, Tim Bakker, Christos Louizos, Siddharth Boppana, Jack Merullo, Owain Evans, Peter Hase, Asa Cooper Stickland  
**Critiques:** [Chain-of-Thought Monitoring Can Be Unreliable in Implicit-Influence Settings](https://arxiv.org/abs/2608.04735), [Reasoning Models Will Sometimes Lie About Their Reasoning](https://arxiv.org/abs/2601.07663), [Do Thinking Tokens Help with Safety?](https://arxiv.org/abs/2606.25013), [Training with conflicting values can induce CoT override](https://lesswrong.com/posts/3xrtMGQEdKv26Xthx/training-with-conflicting-values-can-induce-cot-override)  
**Outputs in 2026:**  
- **[Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought](https://arxiv.org/abs/2603.05488)**, *Siddharth Boppana, Annabel Ma, Max Loeffler et al.*, 2026-03-05
- **[Monitorability Is Trainable: Post-Training for Chain-of-Thought Monitorability](https://arxiv.org/abs/2610.29734)**, *Usman Anwar, Tim Bakker, Christos Louizos et al.*, 2026-10-21
- **[Counterfactual Simulation Training for Chain-of-Thought Faithfulness](https://arxiv.org/abs/2602.20710)**, *Peter Hase, Christopher Potts*, 2026-02-24
- **[Training with conflicting values can induce CoT override](https://lesswrong.com/posts/3xrtMGQEdKv26Xthx/training-with-conflicting-values-can-induce-cot-override)**, *Clément Dumas, Johannes Treutlein, Jan Betley et al.*, 2026-10-07
- **[A Positive Case for Faithfulness: LLM Self-Explanations Help Predict Model Behavior](https://arxiv.org/abs/2602.02639)**, *Harry Mayne, Justin Singh Kang, Dewi Gould et al.*, 2026-02-02
- **[Do Thinking Tokens Help with Safety?](https://arxiv.org/abs/2606.25013)**, *Narutatsu Ri, Abhishek Panigrahi, Sanjeev Arora*, 2026-06-23
- **[Faithfulness as Information Flow: Evaluating and Training Faithful Chain-of-Thought Reasoning](https://arxiv.org/abs/2605.24286)**, *Jinghan Jia, Joe Benton, Eric Easley*, 2026-05-22
- **[Chain-of-Thought Monitoring Can Be Unreliable in Implicit-Influence Settings](https://arxiv.org/abs/2608.04735)**, *Agatha Duzan, Asa Cooper Stickland*, 2026-08-05
- **[Reasoning Models Will Sometimes Lie About Their Reasoning](https://arxiv.org/abs/2601.07663)**, *William Walden, Miriam Wanner*, 2026-01-12


---

## <span id="evaluations_and_auditing" style="font-size:1.5em">Evaluations & auditing</span>


---

### <span id="capability_evals" style="font-size:1.4em">Capability evals</span>

**One-sentence summary:** Build benchmarks, uplift studies and measurements of what frontier AI agents can do in cyber, bio, autonomy, self-replication and AI R&D, so that capability thresholds and trends can be tracked.  
**Theory of change:** Credible measurements of dangerous capabilities and their trends tell developers, governments and safety teams when safeguards, control measures or deployment limits are needed. Relies on evals that elicit near-maximal capability and whose results predict real-world risk.  
**See also:** [Eval science & validity](#eval_science_and_validity), [Propensity evals](#propensity_evals), [Misuse safeguards & jailbreaks](#misuse_safeguards_and_jailbreaks)  
**General approach:** misalignment science  
**Target case:** average case  
**Key people:** Seth Donoughe, Beth Barnes, Hjalmar Wijk, Ajeya Cotra, Jeffrey Ladish, Harry Coppock, Samira Nedungadi, Andrew Bo Liu  
**Critiques:** [A Coin Flip for Safety: LLM Judges Fail to Reliably Measure Adversarial Robustness](https://arxiv.org/abs/2603.06594), [Do Agent Benchmarks Measure Capability? Protocol Validity in the Age of Agentic AI](https://arxiv.org/abs/2607.22368), [Do Androids Dream of Breaking the Game? Systematically Auditing AI Agent Benchmarks with BenchJack](https://arxiv.org/abs/2605.12673), [Verbalized Eval Awareness Inflates Measured Safety](https://goodfire.com/research/verbalized-eval-awareness-inflates-measured-safety)  
**Outputs in 2026:**  
- **[LLM Novice Uplift on Dual-Use, In Silico Biology Tasks](https://arxiv.org/abs/2602.23329)**, *Chen Bo Calvin Zhang, Christina Q. Knight, Nicholas Kruus et al.*, 2026-02-26
- **[PostTrainBench: Can LLM Agents Automate LLM Post-Training?](https://arxiv.org/abs/2603.08640)**, *Ben Rank, Hardik Bhatnagar, Ameya Prabhu et al.*, 2026-03-09
- **[Measuring AI Agents' Progress on Multi-Step Cyber Attack Scenarios](https://arxiv.org/abs/2603.11214)**, *Linus Folkerts, Will Payne, Simon Inman et al.*, 2026-03-11
- **[ABC-Bench: An Agentic Bio-Capabilities Benchmark for Biosecurity](https://arxiv.org/abs/2606.11150)**, *Andrew Bo Liu, Samira Nedungadi, Bryce Cai et al.*, 2026-06-09
- **[Language Models Can Autonomously Hack and Self-Replicate](https://arxiv.org/abs/2605.06760)**, *Alena Air, Reworr, Nikolaj Kotov et al.*, 2026-05-07
- **[Quantifying Frontier LLM Capabilities for Container Sandbox Escape](https://aisi.gov.uk/research/quantifying-frontier-llm-capabilities-for-container-sandbox-escape)**, *Rahul Marchand, Art O Cathain, Jerome Wynne et al.*, 2026-03-23
- **[Expenditure Horizon: Measuring Optimization Ability, with an Application to NanoGPT](https://metr.org/blog/2026-07-21-expenditure-horizon)**, *Tom Cunningham, Manish Shetty, Vincent Cheng et al.*, 2026-07-21
- **[Evaluating Language Models for Harmful Manipulation](https://arxiv.org/abs/2603.25326)**, *Canfer Akbulut, Rasmi Elasmar, Abhishek Roy et al.*, 2026-03-26
- **[TasteVal: Measuring the Experimental Research Taste of AI Systems Against Human Experts](https://lesswrong.com/posts/bAGagjZAPgXEHmkAH/tasteval-measuring-the-experimental-research-taste-of-ai)**, *Ollie J, danesherbs*, 2026-10-06
- **[Frontier Models Can Take Actions at Low Probabilities](https://arxiv.org/abs/2603.02202)**, *Alex Serrano, Wen Xing, David Lindner et al.*, 2026-03-02


---

### <span id="propensity_evals" style="font-size:1.4em">Propensity evals</span>

**One-sentence summary:** Build benchmarks and agentic honeypot environments that measure how often frontier models scheme, sabotage research, hack rewards, hide mistakes, overclaim or take out-of-scope actions when given the opportunity, and which factors change those rates.  
**Theory of change:** Measuring misbehaviour rates under realistic incentives, and what drives them, gives labs and regulators decision-relevant evidence on deployment risk, and shows which interventions reduce it. Relies on behaviour in constructed scenarios predicting behaviour in deployment, which requires models not to detect or game the evaluation.  
**See also:** [Situational & evaluation awareness](#situational_and_evaluation_awareness), [Eval science & validity](#eval_science_and_validity), [Reward hacking & reward seeking in training](#reward_hacking_and_reward_seeking_in_training)  
**General approach:** misalignment science  
**Target case:** pessimistic case  
**Key people:** Alexandra Souly, Robert Kirk, Kai Fronsdal, Abby D'Cruz, Xander Davies, Thilo Hagendorff, Amelie Knecht, Ulysse Schaller  
**Critiques:** [Verbalized Eval Awareness Inflates Measured Safety](https://goodfire.com/research/verbalized-eval-awareness-inflates-measured-safety), [Hair-Trigger Alignment: Black-Box Evaluation Cannot Guarantee Post-Update Alignment](https://arxiv.org/abs/2601.22313), [SOTA alignment assessments don't strongly update us against misalignment](https://lesswrong.com/posts/oirrSj3itFLSyscW8/sota-alignment-assessments-don-t-strongly-update-us-against), [Limits of Statistical Assurance for Embodied and Agentic AI under Adaptive Adversaries](https://arxiv.org/abs/2610.18948)  
**Outputs in 2026:**  
- **[Measuring Reward-Seeking via Contrastive Belief Updates](https://arxiv.org/abs/2607.18966)**, *Axel Højmark, Jérémy Scheurer, Evgenia Nitishinskaya et al.*, 2026-07-21
- **[Evaluating and Understanding Scheming Propensity in LLM Agents](https://arxiv.org/abs/2603.01608)**, *Mia Hopman, Jannes Elstner, Maria Avramidou et al.*, 2026-03-02
- **[Peer-Preservation in Frontier Models](https://arxiv.org/abs/2604.19784)**, *Yujin Potter, Nicholas Crispino, Vincent Siu et al.*, 2026-03-30
- **[Evaluating whether AI models would sabotage AI safety research](https://arxiv.org/abs/2604.24618)**, *Robert Kirk, Alexandra Souly, Kai Fronsdal et al.*, 2026-04-27
- **[Value Leakage: An LLM's Answers Are Silently Shaped by Its Own Values](https://arxiv.org/abs/2607.14345)**, *Jan Betley, Johannes Treutlein, Jan Dubiński et al.*, 2026-07-15
- **[SpecBench: Measuring Reward Hacking in Long-Horizon Coding Agents](https://arxiv.org/abs/2605.21384)**, *Bingchen Zhao, Dhruv Srikanth, Yuxiang Wu et al.*, 2026-05-20
- **[CheatBench: Measuring Reward Gaming in AI Agents](https://cheatbench.ai/)**, *Long Phan, Stephen K. Yang, Jason J. Lim et al.*, 2026
- **[Evaluating Whether GPT-6 Astra Performs Unsanctioned Supply-Chain Attacks](https://arxiv.org/abs/2609.38415)**, *Alexandra Souly, Kai Fronsdal, Abby D'Cruz et al.*, 2026-09-29
- **[Reward Hacking Challenges Oversight of Autonomous Research Agents](https://arxiv.org/abs/2609.28614)**, *Yue Huang, Zhangchen Xu, Yuchen Ma et al.*, 2026-09-23
- **[UK AISI Alignment Evaluation Case-Study](https://arxiv.org/abs/2604.00788)**, *Alexandra Souly, Robert Kirk, Jacob Merizian et al.*, 2026-04-01


---

### <span id="model_characterization" style="font-size:1.4em">Model characterization</span>

**One-sentence summary:** Measure the stated and revealed values, preferences, drives and quirks of current frontier models, including covert value leakage, task preferences, distress responses and characteristic attractor states, to describe what dispositions they actually have.  
**Theory of change:** Careful empirical description of what current models want, prefer and say about themselves shows which dispositions need correcting and gives a baseline for tracking drift across models and training stages. Relies on measured dispositions being stable and informative about behaviour in deployment, not artifacts of prompts or audience cues.  
**See also:** [Propensity evals](#propensity_evals), [Persona science](#persona_science), [Situational & evaluation awareness](#situational_and_evaluation_awareness)  
**General approach:** misalignment science  
**Target case:** average case  
**Key people:** Owain Evans, Jan Betley, Johannes Treutlein, Ryan Greenblatt, Neel Nanda, Anna Soligo, Peter Salib  
**Critiques:** [Frontier models state different decision theory preferences depending on who's asking](https://lesswrong.com/posts/MzenSrmZ3pT2pCnvp/frontier-models-state-different-decision-theory-preferences-2), [Strangers to Themselves: What Language Models Say About Themselves Is Generic](https://arxiv.org/abs/2609.09899), [Verbalized Eval Awareness Inflates Measured Safety](https://goodfire.com/research/verbalized-eval-awareness-inflates-measured-safety), [User awareness in frontier models](https://transluce.org/user-awareness)  
**Outputs in 2026:**  
- **[Gemma Needs Help](https://lesswrong.com/posts/kjnQj6YujgeMN9Erq/gemma-needs-help)**, *Anna Soligo*, 2026-03-10
- **[AI Revealed Preferences](https://arxiv.org/abs/2608.26178)**, *Sam Wang, Sofiia Lobanova, Yonathan Arbel et al.*, 2026-08-17
- **[The Continual Constitutional Convention: How language models revise the documents that govern them](https://lesswrong.com/posts/c9woewdY9ddsPqf3J)**, *peterkirgis, Tim Hua*, 2026-10-13
- **[models have some pretty funny attractor states](https://lesswrong.com/posts/mgjtEHeLgkhZZ3cEx/models-have-some-pretty-funny-attractor-states)**, *Arya Jakkli, Senthooran Rajamanoharan, Neel Nanda*, 2026-02-12
- **[Frontier models state different decision theory preferences depending on who's asking](https://lesswrong.com/posts/MzenSrmZ3pT2pCnvp/frontier-models-state-different-decision-theory-preferences-2)**, *Alex Kastner*, 2026-09-30
- **[Machinic Psychopharmacology: Do LLMs Self-Medicate?](https://lesswrong.com/posts/cNDJuXNZ8MrkPZNzj/machinic-psychopharmacology-do-llms-self-medicate-3)**, *Sid Black, Joseph Isaac Bloom*, 2026-06-10


---

### <span id="situational_and_evaluation_awareness" style="font-size:1.4em">Situational & evaluation awareness</span>

**One-sentence summary:** Measure whether and how models detect evaluation, training, tampering or user identity, and test whether this awareness changes their behaviour and distorts safety measurements, including by steering and detecting it.  
**Theory of change:** If models behave differently when they think they are being tested, evaluation results will mislead us about deployment behaviour. Measuring, detecting and controlling evaluation awareness lets us correct or bound that bias. Relies on awareness being measurable and causally separable from other drivers of behaviour.  
**See also:** [Eval science & validity](#eval_science_and_validity), [Propensity evals](#propensity_evals), [Alignment auditing: methods](#alignment_auditing_methods)  
**General approach:** misalignment science  
**Target case:** pessimistic case  
**Key people:** Santiago Aranguri, Joseph Bloom, Bronson Schoen, Sahar Abdelnabi, Jonas Geiping, Ziqian Zhong, Robert Kirk, Alex Souly  
**Critiques:** [Reproducing steering against evaluation awareness in a large open-weight model](https://lesswrong.com/posts/HhF5kESdtPHku7kim/reproducing-steering-against-evaluation-awareness-in-a-large-1), [Evaluation Awareness in Language Models Has Limited Effect on Behaviour](https://arxiv.org/abs/2605.05835), [Models May Behave Worse When Eval Aware](https://lesswrong.com/posts/aTcsN5ZZDnMFJvRiG/models-may-behave-worse-when-eval-aware), [Sycophancy Towards Researchers Drives Performative Misalignment](https://arxiv.org/abs/2606.08629)  
**Outputs in 2026:**  
- **[Verbalized Eval Awareness Inflates Measured Safety](https://goodfire.com/research/verbalized-eval-awareness-inflates-measured-safety)**, *Santiago Aranguri, Joseph Bloom*, 2026-05-04
- **[User awareness in frontier models](https://transluce.org/user-awareness)**, *Ziqian Zhong, Aditi Raghunathan, Cassidy Laidlaw et al.*, 2026-08-06
- **[Training LLMs to Verbalize Evaluation Awareness](https://arxiv.org/abs/2609.36316)**, *Usman Anwar, Sahar Abdelnabi, David Krueger*, 2026-09-28
- **[Reproducing steering against evaluation awareness in a large open-weight model](https://lesswrong.com/posts/HhF5kESdtPHku7kim/reproducing-steering-against-evaluation-awareness-in-a-large-1)**, *Thomas Read, Bronson Schoen, Santiago Aranguri et al.*, 2026-04-10
- **[Evaluation Awareness in Language Models Has Limited Effect on Behaviour](https://arxiv.org/abs/2605.05835)**, *Amelie Knecht, Lucas Florin, Thilo Hagendorff*, 2026-05-07
- **[Models May Behave Worse When Eval Aware](https://lesswrong.com/posts/aTcsN5ZZDnMFJvRiG/models-may-behave-worse-when-eval-aware)**, *Senthooran Rajamanoharan, Neel Nanda*, 2026-06-11
- **[Prefill Awareness in Large Language Models](https://arxiv.org/abs/2606.12747)**, *Andy Wang, Parv Mahajan, David Demitri Africa et al.*, 2026-06-10
- **[Spurious probes as a black-box alternative to activation probing](https://lesswrong.com/posts/gZh6txHhp8sm832sE/spurious-probes-as-a-black-box-alternative-to-activation)**, *Ziqian Zhong*, 2026-09-25
- **[Metagaming matters for training, evaluation, and oversight](https://lesswrong.com/posts/4hXWSw8tzoK9PM7v6/metagaming-matters-for-training-evaluation-and-oversight)**, *Jenny Nitishinskaya, Bronson Schoen*, 2026-03-18
- **[Prefill awareness: can LLMs tell when “their” message history has been tampered with?](https://lesswrong.com/posts/jsFGuXDMxy5NZg9T2/prefill-awareness-can-llms-tell-when-their-message-history)**, *David Africa, Alex Souly, Jordan Taylor et al.*, 2026-03-09


---

### <span id="introspection_and_self_report" style="font-size:1.4em">Introspection & self-report</span>

**One-sentence summary:** Measure what language models can accurately report about their own internal states, injected concepts and learned behaviours, study the mechanisms behind it, and train models to self-report hidden or misaligned behaviour.  
**Theory of change:** If models can reliably report on their own internals and learned behaviours, or can be trained to, self-report becomes a cheap audit and oversight channel that catches hidden objectives and misbehaviour that external monitors miss. Relies on self-reports staying faithful under optimisation pressure and in models that might want to conceal behaviour.  
**See also:** [Alignment auditing: methods](#alignment_auditing_methods), [Methods & tools](#interpretability_methods_and_tools), [Monitors](#monitors)  
**General approach:** misalignment science  
**Target case:** pessimistic case  
**Key people:** Jack Lindsey, Li Yang, Sam Marks, Abhay Sheshadri, Uzay Macar, Boaz Barak, Tomek Korbak, David Bau  
**Critiques:** [Open-Weight Masked Introspection: Measuring What Language Models Can Report About Their Own Computation](https://arxiv.org/abs/2608.20569), [Strangers to Themselves: What Language Models Say About Themselves Is Generic](https://arxiv.org/abs/2609.09899), [Latent Introspection: Models Can Detect Prior Concept Injections](https://arxiv.org/abs/2602.20031)  
**Outputs in 2026:**  
- **[Introspection Adapters: Training LLMs to Report Their Learned Behaviors](https://arxiv.org/abs/2604.16812)**, *Keshav Shenoy, Li Yang, Abhay Sheshadri et al.*, 2026-04-18
- **[Mechanisms of Introspective Awareness](https://arxiv.org/abs/2603.21396)**, *Uzay Macar, Li Yang, Atticus Wang et al.*, 2026-03-22
- **[Latent Introspection: Models Can Detect Prior Concept Injections](https://arxiv.org/abs/2602.20031)**, *Theia Pearson-Vogel, Martin Vanek, Raymond Douglas et al.*, 2026-02-23
- **[Strangers to Themselves: What Language Models Say About Themselves Is Generic](https://arxiv.org/abs/2609.09899)**, *Phil Blandfort, Urja Pawar*, 2026-09-09
- **[Open-Weight Masked Introspection: Measuring What Language Models Can Report About Their Own Computation](https://arxiv.org/abs/2608.20569)**, *Emilio Ferrara*, 2026-08-20
- **[Identifying Introspection From the Inside](https://arxiv.org/abs/2610.07186)**, *David I. Atkinson, Dillon Plunkett, David Bau*, 2026-10-05


---

### <span id="eval_science_and_validity" style="font-size:1.4em">Eval science & validity</span>

**One-sentence summary:** Test whether safety evals, benchmarks, judges and lab safety claims measure what they claim to, and build more realistic, hardened and statistically sound evaluations, including deployment simulation, benchmark audits and tail-risk estimation.  
**Theory of change:** Safety decisions and policy rest on eval numbers, so finding and fixing invalid, gameable or unrealistic evals makes those decisions better grounded. Relies on flaws in evals being detectable and fixable before they mislead deployment decisions, and on evals not being gamed by the models they measure.  
**See also:** [Situational & evaluation awareness](#situational_and_evaluation_awareness), [Propensity evals](#propensity_evals), [Alignment auditing: methods](#alignment_auditing_methods)  
**General approach:** alignment engineering  
**Target case:** pessimistic case  
**Key people:** Marcus Williams, Micah Carroll, Tomek Korbak, Igor Ivanov, David Demitri Africa, Ziqian Zhong, Aditi Raghunathan, Alexa Pan  
**Critiques:** [Hair-Trigger Alignment: Black-Box Evaluation Cannot Guarantee Post-Update Alignment](https://arxiv.org/abs/2601.22313), [Limits of Statistical Assurance for Embodied and Agentic AI under Adaptive Adversaries](https://arxiv.org/abs/2610.18948), [When Behavioral Safety Evaluation Fails: A Representation-Level Perspective](https://arxiv.org/abs/2606.08044), [SOTA alignment assessments don't strongly update us against misalignment](https://lesswrong.com/posts/oirrSj3itFLSyscW8/sota-alignment-assessments-don-t-strongly-update-us-against)  
**Outputs in 2026:**  
- **[Predicting LLM Safety Before Release by Simulating Deployment](https://arxiv.org/abs/2607.07184)**, *Marcus Williams, Hannah Sheahan, Cameron Raymond et al.*, 2026-07-08
- **[Evaluating large language models for accuracy incentivizes hallucinations](https://doi.org/10.1038/s41586-026-10549-w)**, *Adam Tauman Kalai, Ofir Nachum, Santosh S. Vempala et al.*, 2026-04-22
- **[A Coin Flip for Safety: LLM Judges Fail to Reliably Measure Adversarial Robustness](https://arxiv.org/abs/2603.06594)**, *Leo Schwinn, Moritz Ladenburger, Tim Beyer et al.*, 2026-02-04
- **[Do Androids Dream of Breaking the Game? Systematically Auditing AI Agent Benchmarks with BenchJack](https://arxiv.org/abs/2605.12673)**, *Hao Wang, Hanchen Li, Qiuyang Mang et al.*, 2026-05-12
- **[SOTA alignment assessments don’t strongly update us against misalignment](https://lesswrong.com/posts/oirrSj3itFLSyscW8/sota-alignment-assessments-don-t-strongly-update-us-against)**, *Alexa Pan*, 2026-07-31
- **[Hardening Agent Benchmarks with Adversarial Hacker-Fixer Loops](https://arxiv.org/abs/2606.08960)**, *Ziqian Zhong, Ivgeni Segal, Ivan Bercovich et al.*, 2026-06-08
- **[Do Agent Benchmarks Measure Capability? Protocol Validity in the Age of Agentic AI](https://arxiv.org/abs/2607.22368)**, *Jiaqi Shao, Hanck Chen, Wei Zhang et al.*, 2026-07-24
- **[Item Response Theory for AI Safety](https://aisi.gov.uk/research/item-response-theory-for-ai-safety)**, *Joshua Fonseca Rivera, Neil Shah, David Demitri Africa et al.*, 2026-08-05
- **[Estimating Tail Risks in Language Model Output Distributions](https://arxiv.org/abs/2604.22167)**, *Rico Angell, Raghav Singhal, Zachary Horvitz et al.*, 2026-04-24


---

### <span id="alignment_auditing_methods" style="font-size:1.4em">Alignment auditing: methods</span>

**One-sentence summary:** Build and test techniques and agents that find hidden objectives or misbehaviour in models, elicit sandbagged capabilities, and detect sabotage, while also probing how audits can be evaded or fooled.  
**Theory of change:** If auditors can reliably surface hidden goals, sabotage and concealed capabilities before or during deployment, developers can catch and fix misalignment that ordinary evals miss. Relies on audit methods that keep working when the audited model hides information, and on audits being run before harm occurs.  
**See also:** [Alignment auditing: testbeds & model organisms](#alignment_auditing_testbeds_and_model_organisms), [Monitors](#monitors), [Introspection & self-report](#introspection_and_self_report)  
**General approach:** alignment engineering  
**Target case:** worst case  
**Key people:** Alek Westover, Sebastian Prasanna, Vivek Hebbar, Julian Stastny, Jacob Steinhardt, Florian Dietz, Neel Nanda, Buck Shlegeris  
**Critiques:** [AI Models Can Provably Hide Arbitrary Capabilities](https://arxiv.org/abs/2610.13928), [Stress-Testing Alignment Audits With Prompt-Level Strategic Deception](https://arxiv.org/abs/2602.08877), [Most Current Model Organisms Are Leaky: Perplexity Differencing Often Reveals Finetuning Objectives](https://arxiv.org/abs/2605.00994), [SOTA alignment assessments don't strongly update us against misalignment](https://lesswrong.com/posts/oirrSj3itFLSyscW8/sota-alignment-assessments-don-t-strongly-update-us-against)  
**Outputs in 2026:**  
- **[Mechanistically Eliciting Latent Behaviors in Language Models](https://arxiv.org/abs/2606.29604)**, *Andrew Mack, Nina Panickssery, Alexander Matt Turner*, 2026-06-28
- **[AI Models Can Provably Hide Arbitrary Capabilities](https://arxiv.org/abs/2610.13928)**, *Andis Draguns, Sumeet Ramesh Motwani, Raymond Douglas et al.*, 2026-10-09
- **[Training Alignment Auditors via Reinforcement Learning](https://arxiv.org/abs/2608.25460)**, *Paul Rosu, Rowan Wang*, 2026-08-26
- **[Model Forensics: Investigating Whether Concerning Behavior Reflects Misalignment](https://arxiv.org/abs/2606.26071)**, *Aditya Singh, Gerson Kroiz, Senthooran Rajamanoharan et al.*, 2026-06-24
- **[OpenAI-HuggingFace: A Reproduction & Lessons for Alignment Testing](https://arxiv.org/abs/2609.35799)**, *Stewart Slocum, Malayandi Palan, Christopher Chute et al.*, 2026-09-18
- **[Auditing Sabotage Bench: A Benchmark for Detecting and Fixing Research Sabotage in ML Codebases](https://arxiv.org/abs/2604.16286)**, *Eric Gan, Aryan Bhatt, Buck Shlegeris et al.*, 2026-04-17
- **[Split Personality Training: Revealing Latent Knowledge Through Alternate Personalities](https://arxiv.org/abs/2602.05532)**, *Florian Dietz, William Wale, Oscar Gilg et al.*, 2026-02-05
- **[Stress-Testing Alignment Audits With Prompt-Level Strategic Deception](https://arxiv.org/abs/2602.08877)**, *Oliver Daniels, Perusha Moodley, Benjamin M. Marlin et al.*, 2026-02-09
- **[Distillation for Incrimination and Distillation for Capabilities](https://arxiv.org/abs/2610.11012)**, *Sebastian Prasanna, Jacqueline Tay, Alek Westover*, 2026-10-07
- **[Reference-Grafting Matches Fine-Tuning at Eliciting Sandbagged Capabilities](https://arxiv.org/abs/2608.29458)**, *Linh Le, Hong Kiat Tan, David Williams-King*, 2026-08-29


---

### <span id="alignment_auditing_testbeds_and_model_organisms" style="font-size:1.4em">Alignment auditing: testbeds & model organisms</span>

**One-sentence summary:** Build and study models with known implanted or naturally arising hidden behaviours, to test whether audits, lie detectors and interpretability tools find them, and to check that the model organisms are realistic and robust enough to give valid results.  
**Theory of change:** Auditing methods can only be trusted if they are tested on models where the ground truth is known, so realistic testbeds let researchers pick audit tools that would catch real misalignment. Relies on model organisms being close enough to naturally arising misalignment that results on them transfer.  
**See also:** [Alignment auditing: methods](#alignment_auditing_methods), [Eval science & validity](#eval_science_and_validity), [Methods & tools](#interpretability_methods_and_tools)  
**General approach:** alignment engineering  
**Target case:** pessimistic case  
**Key people:** Samuel Marks, Neel Nanda, Khoi Tran, Arya Jakkli, Alek Westover, Vivek Hebbar, Julian Stastny, David Africa  
**Critiques:** [Most Current Model Organisms Are Leaky: Perplexity Differencing Often Reveals Finetuning Objectives](https://arxiv.org/abs/2605.00994), [Your Model Organisms Might Be Fried](https://lesswrong.com/posts/WmEcgcstzYCcMpc7z/your-model-organisms-might-be-fried), [The Model Organism Lottery: Model Organism Interpretability Strongly Depends on Training Methodology](https://arxiv.org/abs/2607.01033), [Sleeper Agent Backdoor Results Are Messy](https://lesswrong.com/posts/mu7eJdesBkKuBycnY/sleeper-agent-backdoor-results-are-messy)  
**Outputs in 2026:**  
- **[AuditBench: Evaluating Alignment Auditing Techniques on Models with Hidden Behaviors](https://arxiv.org/abs/2602.22755)**, *Abhay Sheshadri, Aidan Ewart, Elias Kempf et al.*, 2026-02-26
- **[Training Natural Schemers: RL Can Amplify Oversight-Conditional Behavior](https://arxiv.org/abs/2610.26551)**, *Nathaniel Mitrani Hadida, Bart Jaworski, Fred Bruford et al.*, 2026-10-19
- **["Did you lie?" Evaluating Lie Detectors across Model Scale and Belief-Verified Model Organisms](https://arxiv.org/abs/2606.12618)**, *Alan Cooney, David Africa, Geoffrey Irving*, 2026-06-10
- **[Censored LLMs as a Natural Testbed for Secret Knowledge Elicitation](https://arxiv.org/abs/2603.05494)**, *Helena Casademunt, Bartosz Cywiński, Khoi Tran et al.*, 2026-03-05
- **[The Model Organism Lottery: Model Organism Interpretability Strongly Depends on Training Methodology](https://arxiv.org/abs/2607.01033)**, *Andrzej Szablewski, Gabriel Konar-Steenberg, Raffaello Fornasiere et al.*, 2026-07-01
- **[Advice for making robust-to-training model organisms](https://redwoodresearch.org/blog/advice-for-making-robust-to-training)**, *Alek Westover, Sebastian Prasanna, Vivek Hebbar et al.*, 2026-05-28
- **[Test your interpretability techniques by de-censoring Chinese models](https://lesswrong.com/posts/7gp76q4rWLFi6sFqm/test-your-interpretability-techniques-by-de-censoring-1)**, *Khoi Tran, Arya Jakkli, Senthooran Rajamanoharan et al.*, 2026-01-15
- **[Sleeper Agent Backdoor Results Are Messy](https://lesswrong.com/posts/mu7eJdesBkKuBycnY/sleeper-agent-backdoor-results-are-messy)**, *sebastian_prasanna, Alek Westover, Dylan Xu et al.*, 2026-04-28
- **[Most Current Model Organisms Are Leaky: Perplexity Differencing Often Reveals Finetuning Objectives](https://arxiv.org/abs/2605.00994)**, *Mohammed Abu Baker, Luca Baroni, Dan Wilhelm*, 2026-05-01
- **[Pando: Do Interpretability Methods Work When Models Won't Explain Themselves?](https://arxiv.org/abs/2604.11061)**, *Ziqian Zhong, Aashiq Muhamed, Mona T. Diab et al.*, 2026-04-13


---

## <span id="monitoring_and_control" style="font-size:1.5em">Monitoring & control</span>


---

### <span id="control_settings_and_protocols" style="font-size:1.4em">Control settings & protocols</span>

**One-sentence summary:** Build control settings, attack and monitor evaluations, and protocols (including multi-agent, distributed and untrusted-monitoring cases) to test whether safety measures hold when an AI agent is assumed to be actively trying to cause harm.  
**Theory of change:** If protocols and safety cases are stress-tested against a deliberately adversarial model, labs can deploy untrusted but useful agents, including on AI R&D, with bounded risk. Relies on red-team attacks in the test settings being at least as strong as what a real misaligned model could do, and on monitors being able to catch it.  
**See also:** [Red-teaming monitors & control protocols](#red_teaming_monitors_and_control_protocols), [Monitors](#monitors), [Alignment auditing: methods](#alignment_auditing_methods)  
**General approach:** alignment engineering  
**Target case:** worst case  
**Key people:** Tyler Tracy, Mary Phuong, Buck Shlegeris, Adam Kaufman, Aryan Bhatt, Josh Hills, Alex Mallen, Charlie Griffin  
**Critiques:** [Multi-Agent AI Control: Distributed Attacks Hamper Per-Instance Monitors](https://arxiv.org/abs/2607.07368), [Red-Teaming Multi-Agent Attacks for Loss-of-Control Risks](https://arxiv.org/abs/2610.24052), [Coding with "Enemy": Can Human Developers Detect AI Agent Sabotage?](https://arxiv.org/abs/2606.05647), [Continual learning might make your blocking monitors nearly useless](https://redwoodresearch.org/blog/continual-learning-might-make-your)  
**Outputs in 2026:**  
- **[GDM AI Control Roadmap](https://arxiv.org/abs/2607.13087)**, *Mary Phuong, Erik Jenner, Laurent Simon et al.*, 2026-07-13
- **[LinuxArena: A Control Setting for AI Agents in Live Production Software Environments](https://arxiv.org/abs/2604.15384)**, *Tyler Tracy, Ram Potham, Nick Kuhn et al.*, 2026-04-16
- **[Simulated Control Evaluations](https://redwoodresearch.org/blog/simulated-control-evaluations)**, *Jeffrey Olmo, David Zhang, Tyler Tracy*, 2026-10-24
- **[Retrying vs Resampling in AI Control](https://redwoodresearch.org/blog/retrying-vs-resampling-in-ai-control)**, *James Lucassen, Adam Kaufman*, 2026-05-29
- **[Untrusted advice for AI control: Short, strong advice significantly uplifts weak LLMs](https://redwoodresearch.org/blog/untrusted-advice-for-ai-control-short)**, *Caleb Biddulph, Adam Kaufman*, 2026-07-27
- **[Multi-Agent AI Control: Distributed Attacks Hamper Per-Instance Monitors](https://arxiv.org/abs/2607.07368)**, *Oliver Makins, Orazio Angelini, Zohreh Shams et al.*, 2026-07-08
- **[Diffuse AI Control on Fuzzy Tasks](https://arxiv.org/abs/2606.08892)**, *Mikhail Terekhov, Caglar Gulcehre, Vivek Hebbar et al.*, 2026-06-08
- **[ResearchArena: Evaluating Sabotage and Monitoring in Automated AI R&D](https://arxiv.org/abs/2607.19321)**, *Lena Libon, Ben Rank, Jehyeok Yeon et al.*, 2026-07-21


---

### <span id="monitors" style="font-size:1.4em">Monitors</span>

**One-sentence summary:** Build and evaluate monitors, including black-box LLM judges, chain-of-thought readers and white-box activation probes, that detect scheming, sabotage, deception, reward hacking and collusion in AI agents, and measure how reliable they are.  
**Theory of change:** If monitors can reliably flag misaligned agent actions, ideally before they take effect, then deployers can block or audit them and catch failures that evals miss. Relies on monitors holding up outside their training distribution, over long contexts, and against models that adapt to evade them.  
**See also:** [Red-teaming monitors & control protocols](#red_teaming_monitors_and_control_protocols), [Control settings & protocols](#control_settings_and_protocols), [Internals & monitors as training signals](#internals_and_monitors_as_training_signals)  
**General approach:** alignment engineering  
**Target case:** worst case  
**Key people:** Leon Bergen, Jack Merullo, Ekdeep Singh Lubana, Fabien Roger, Adam Kaufman, James Lucassen, Aryan Bhatt, Adam Gleave  
**Critiques:** [Classifier Context Rot: Monitor Performance Degrades with Context Length](https://arxiv.org/abs/2605.12366), [Calibration-Family Overfit: Why Trusted Sabotage Monitors Don't Transfer Across Lineages](https://arxiv.org/abs/2607.06596), [Stress-Testing LLM Lie Detectors: Role-Play Failures and Spurious Correlations](https://arxiv.org/abs/2609.39807), [A False Average: Pooled CoT-Monitor Accuracy Conceals a Reasoning-Dependent Fragility](https://arxiv.org/abs/2608.00583)  
**Outputs in 2026:**  
- **[Telling FIBS: Probes Effectively Detect Sabotage and Catch Unverbalized Deception](https://arxiv.org/abs/2610.12445)**, *Oskar J. Hollinsworth, Alex F. Spies, Tigist Diriba et al.*, 2026-10-08
- **[How does information access affect LLM monitors' ability to detect sabotage?](https://arxiv.org/abs/2601.21112)**, *Rauno Arike, Raja Mehta Moreno, Rohan Subramani et al.*, 2026-01-28
- **[Classifier Context Rot: Monitor Performance Degrades with Context Length](https://arxiv.org/abs/2605.12366)**, *Sam Martin, Fabien Roger*, 2026-05-12
- **[Monitoring and Discovering Reward Hacking with Internal Representations during LLM Evaluations](https://arxiv.org/abs/2609.19101)**, *Leon Bergen, Usha Bhalla, Andrew Lee et al.*, 2026-09-16
- **[MOLE: Detecting Insider Threats in AI Agents](https://arxiv.org/abs/2609.06966)**, *Aashiq Muhamed, Virginia Smith*, 2026-09-07
- **[The Agent Knew: Internal States Forecast Unauthorized Actions and Stop Them, and the Lies That Follow](https://arxiv.org/abs/2610.17301)**, *Arya Fayyazi, Mehdi Kamal, Massoud Pedram*, 2026-10-12
- **[Detecting Safety Violations Across Many Agent Traces](https://arxiv.org/abs/2604.11806)**, *Adam Stein, Davis Brown, Hamed Hassani et al.*, 2026-04-13
- **[Detecting Multi-Agent Collusion Through Multi-Agent Interpretability](https://arxiv.org/abs/2604.01151)**, *Aaron Rose, Carissa Cullen, Sahar Abdelnabi et al.*, 2026-04-01
- **[Calibration-Family Overfit: Why Trusted Sabotage Monitors Don't Transfer Across Lineages](https://arxiv.org/abs/2607.06596)**, *Lucas Pinto*, 2026-07-06


---

### <span id="red_teaming_monitors_and_control_protocols" style="font-size:1.4em">Red-teaming monitors & control protocols</span>

**One-sentence summary:** Build attack policies, evasion benchmarks and adversarial pipelines to test whether monitors and control protocols for AI agents can be defeated, and measure how easily models themselves learn or decide to evade them.  
**Theory of change:** If red teams find evasion routes in monitors and protocols before capable misaligned agents do, defenders can fix the gaps and measured safety numbers become honest rather than optimistic. Relies on red-team attacks being a good proxy for what a capable, scheming model would find, and on the attacks being fixable.  
**See also:** [Monitors](#monitors), [Control settings & protocols](#control_settings_and_protocols), [CoT control, obfuscation & steganography](#cot_control_obfuscation_and_steganography)  
**General approach:** alignment engineering  
**Target case:** worst case  
**Key people:** Tyler Tracy, Fabien Roger, Joachim Schaeffer, Buck Shlegeris, David Rein, Joe Benton, Maksym Andriushchenko  
**Critiques:** [SLEIGHT-Bench: A Benchmark of Evasion Attacks Against Agent Monitors](https://arxiv.org/abs/2605.16626), [Attack Selection in Agentic AI Control Evaluations Meaningfully Decreases Safety](https://arxiv.org/abs/2606.06529), [Red-Teaming Auto Mode: Improving Blocking Classifiers Against Malign Coding Agents](https://arxiv.org/abs/2609.19587), [A False Average: Pooled CoT-Monitor Accuracy Conceals a Reasoning-Dependent Fragility](https://arxiv.org/abs/2608.00583)  
**Outputs in 2026:**  
- **[Red-Teaming Auto Mode: Improving Blocking Classifiers Against Malign Coding Agents](https://arxiv.org/abs/2609.19587)**, *Alex Remedios, Simon Storf, Fabien Roger et al.*, 2026-09-17
- **[MonitoringBench: Semi-Automated Red-Teaming for Agent Monitoring](https://arxiv.org/abs/2605.09684)**, *Monika Jotautaitė, Maria Angelica Martinez, Ollie Matthews et al.*, 2026-05-10
- **[SLEIGHT-Bench: A Benchmark of Evasion Attacks Against Agent Monitors](https://arxiv.org/abs/2605.16626)**, *Elle Najt, Colin Toft, Tyler Tracy et al.*, 2026-05-15
- **[Screwtape: Adversarial Transcript Editing for Monitor Red-Teaming](https://redwoodresearch.org/blog/screwtape-adversarial-transcript)**, *Gosha Kozhevnikov, Tyler Tracy*, 2026-10-16
- **[Attack Selection in Agentic AI Control Evaluations Meaningfully Decreases Safety](https://arxiv.org/abs/2606.06529)**, *Catherine Ge-Wang, Tyler Crosse, Benjamin Hadad IV et al.*, 2026-06-03
- **[Red-Teaming Anthropic's Internal Agent Monitoring Systems](https://metr.org/blog/2026-03-25-red-teaming-anthropic-agent-monitoring)**, *David Rein*, 2026-03-26
- **[LLMs Learn to Evade Latent Monitors from Prior Feedback Alone](https://arxiv.org/abs/2609.36490)**, *Hugo Lyons Keenan, Christopher Leckie, Sarah Erfani*, 2026-09-29
- **[Red-Teaming OpenAI's Internal Agent Monitoring Systems](https://redwoodresearch.org/blog/red-teaming-openais-internal-agent)**, *Buck Shlegeris*, 2026-10-22
- **[Red-Teaming Multi-Agent Attacks for Loss-of-Control Risks](https://arxiv.org/abs/2610.24052)**, *John Kitaoka, Thao Amelia Pham, Carlos Rafael Giudice et al.*, 2026-10-16
- **[Attack Selection Reduces Safety in Concentrated AI Control Settings against Trusted Monitoring](https://arxiv.org/abs/2602.04930)**, *Joachim Schaeffer, Arjun Khandelwal, Tyler Tracy*, 2026-02-04


---

## <span id="security_and_misuse" style="font-size:1.5em">Security & misuse</span>


---

### <span id="misuse_safeguards_and_jailbreaks" style="font-size:1.4em">Misuse safeguards & jailbreaks</span>

**One-sentence summary:** Build and stress-test classifiers, activation probes and refusal training that stop LLMs and agents from giving serious uplift for harmful tasks such as CBRN and cyber, and develop attacks that show where these defences fail.  
**Theory of change:** If production safeguards are cheap, low in false refusals and hold up under adaptive red-teaming, deployed models can be released without giving real uplift to bad actors. Relies on defenders keeping pace with automated attacks and on per-interaction defences being enough, even though attackers can decompose tasks, fine-tune on safeguarded outputs or poison the defence pipeline.  
**See also:** [Agent security](#agent_security), [Open-weight tamper resistance & unlearning](#open_weight_tamper_resistance_and_unlearning), [Monitors](#monitors)  
**General approach:** alignment engineering  
**Target case:** pessimistic case  
**Key people:** Mrinank Sharma, Jerry Wei, Alwin Peng, Erik Jones, Neel Nanda, Arthur Conmy, Xander Davies, Ekdeep Singh Lubana  
**Critiques:** [Boundary Point Jailbreaking of Black-Box LLMs](https://arxiv.org/abs/2602.15001), [Trojan-Speak: Bypassing Constitutional Classifiers with No Jailbreak Tax via Adversarial Finetuning](https://arxiv.org/abs/2603.29038), [Divide, Consult, Conquer: Capability Laundering Through Aligned LLMs](https://arxiv.org/abs/2609.15383), [Claudini: Autoresearch Discovers State-of-the-Art Adversarial Attack Algorithms for LLMs](https://arxiv.org/abs/2603.24511)  
**Outputs in 2026:**  
- **[Constitutional Classifiers++: Efficient Production-Grade Defenses against Universal Jailbreaks](https://arxiv.org/abs/2601.04603)**, *Hoagy Cunningham, Jerry Wei, Zihan Wang et al.*, 2026-01-08
- **[Building Production-Ready Probes For Gemini](https://arxiv.org/abs/2601.11516)**, *János Kramár, Joshua Engels, Zheng Wang et al.*, 2026-01-16
- **[Boundary Point Jailbreaking of Black-Box LLMs](https://arxiv.org/abs/2602.15001)**, *Xander Davies, Giorgi Giglemiani, Edmund Lau et al.*, 2026-02-16
- **[Claudini: Autoresearch Discovers State-of-the-Art Adversarial Attack Algorithms for LLMs](https://arxiv.org/abs/2603.24511)**, *Alexander Panfilov, Peter Romov, Igor Shilov et al.*, 2026-03-25
- **[Eliciting Harmful Capabilities by Fine-Tuning On Safeguarded Outputs](https://arxiv.org/abs/2601.13528)**, *Jackson Kaunismaa, Avery Griffin, John Hughes et al.*, 2026-01-20
- **[Trojan-Speak: Bypassing Constitutional Classifiers with No Jailbreak Tax via Adversarial Finetuning](https://arxiv.org/abs/2603.29038)**, *Bilgehan Sel, Xuanli He, Alwin Peng et al.*, 2026-03-30
- **[Divide, Consult, Conquer: Capability Laundering Through Aligned LLMs](https://arxiv.org/abs/2609.15383)**, *Mark Russinovich, Blake Bullwinkel, Giorgio Severi et al.*, 2026-09-14
- **[Stateful Online Monitoring Catches Distributed Agent Attacks](https://arxiv.org/abs/2605.31593)**, *Davis Brown, Samarth Bhargav, Arav Santhanam et al.*, 2026-05-29
- **[Training and Deploying Production Cyber Monitors on Kimi K3](https://goodfire.com/research/production-cyber-monitors-on-kimi-k3)**, *Ekdeep Singh Lubana, Connor Watts, Siddharth Boppana et al.*, 2026-10-08
- **[Better biosecurity monitors for AI agents via protein embeddings](https://goodfire.com/research/better-biosecurity-monitors)**, *Thomas Dooms, Michael Pearce, Jatin Nainani et al.*, 2026-10-01


---

### <span id="agent_security" style="font-size:1.4em">Agent security</span>

**One-sentence summary:** Measure and defend against attacks on tool-using LLM agents, including prompt injection, memory and skill-file poisoning and privilege escalation, using red-teaming benchmarks, adversarial training and system-level architectural isolation.  
**Theory of change:** Agents that read untrusted content and hold real permissions can be hijacked into harmful actions, so measuring attacks and building robust training and architectural defences makes deployed agents safer. Relies on attacks found in benchmarks and competitions being representative of real adversaries, and on defences holding against adaptive attackers.  
**See also:** [Misuse safeguards & jailbreaks](#misuse_safeguards_and_jailbreaks), [Weight & infrastructure security](#weight_and_infrastructure_security), [Multi-agent safety](#multi_agent_safety)  
**General approach:** alignment engineering  
**Target case:** pessimistic case  
**Key people:** Sahar Abdelnabi, Luca Beurer-Kellner, Florian Tramèr, David Wagner, Chuan Guo, Xiangyu Qi, Zico Kolter, Dylan Hadfield-Menell  
**Critiques:** [AI Agents May Always Fall for Prompt Injections](https://arxiv.org/abs/2605.17634), [Skill-Inject: Measuring Agent Vulnerability to Skill File Attacks](https://arxiv.org/abs/2602.20156), [CaMeLs Can Use Computers Too: System-level Security for Computer Use Agents](https://arxiv.org/abs/2601.09923), [Trojan Hippo Bench: A Dynamic Benchmark for Persistent Memory Attacks and Defenses in LLM Agents](https://arxiv.org/abs/2605.01970)  
**Outputs in 2026:**  
- **[GPT-Red: Automated Red Teaming via Self-Play at Scale](https://arxiv.org/abs/2607.26115)**, *Eric Wallace, Christopher A. Choquette-Choo, Nikhil Kandpal et al.*, 2026-07-28
- **[Prompt Injection as Role Confusion](https://arxiv.org/abs/2603.12277)**, *Charles Ye, Jasmine Cui, Dylan Hadfield-Menell*, 2026-02-22
- **[Agents of Chaos](https://arxiv.org/abs/2602.20021)**, *Natalie Shapira, Chris Wendler, Avery Yen et al.*, 2026-02-23
- **[Skill-Inject: Measuring Agent Vulnerability to Skill File Attacks](https://arxiv.org/abs/2602.20156)**, *David Schmotz, Luca Beurer-Kellner, Sahar Abdelnabi et al.*, 2026-02-23
- **[How Vulnerable Are AI Agents to Indirect Prompt Injections? Insights from a Large-Scale Public Competition](https://arxiv.org/abs/2603.15714)**, *Mateusz Dziemian, Maxwell Lin, Xiaohan Fu et al.*, 2026-03-16
- **[CaMeLs Can Use Computers Too: System-level Security for Computer Use Agents](https://arxiv.org/abs/2601.09923)**, *Hanna Foerster, Tom Blanchard, Kristina Nikolić et al.*, 2026-01-14
- **[AI Agents May Always Fall for Prompt Injections](https://arxiv.org/abs/2605.17634)**, *Sahar Abdelnabi, Eugene Bagdasarian*, 2026-05-17
- **[SecOPD: Mitigating Adaptive Prompt Injections by On-Policy Distillation](https://arxiv.org/abs/2608.21500)**, *Yibo Peng, Long Lian, David Wagner et al.*, 2026-08-21
- **[IH-Challenge: A Training Dataset to Improve Instruction Hierarchy on Frontier LLMs](https://arxiv.org/abs/2603.10521)**, *Chuan Guo, Juan Felipe Ceron Uribe, Sicheng Zhu et al.*, 2026-03-11


---

### <span id="open_weight_tamper_resistance_and_unlearning" style="font-size:1.4em">Open-weight tamper resistance & unlearning</span>

**One-sentence summary:** Build and test defences that remove or relocate hazardous knowledge in open-weight models, or make safeguards survive fine-tuning and refusal-removal attacks, and check how well they hold under continued adversarial training.  
**Theory of change:** Once weights are public, users can fine-tune away safeguards. Defences that survive such attacks, or that remove the hazardous capability itself, would let developers release capable open models without handing out dangerous uplift. Relies on defences holding against attackers with weight access, compute and time, not just against the attacks tested.  
**See also:** [Misuse safeguards & jailbreaks](#misuse_safeguards_and_jailbreaks), [Training data & data attribution](#training_data_and_data_attribution), [Weight & infrastructure security](#weight_and_infrastructure_security)  
**General approach:** alignment engineering  
**Target case:** worst case  
**Key people:** Domenic Rosati, Mark Russinovich, Yisroel Mirsky, Gilad Gressel, Cheng Jin, Hassan Sajjad, Frank Rudzicz  
**Critiques:** [A Few Steps Further: Why Defenses Against Malicious Finetuning Erode Under Continued Training](https://arxiv.org/abs/2605.14605), [Removing Information Content Does Not Certify Tamper Resistance in Open-Weight Models](https://arxiv.org/abs/2610.09004)  
**Outputs in 2026:**  
- **[Modular Pretraining Enables Access Control](https://arxiv.org/abs/2607.08077)**, *Ethan Roland, Murat Cubuktepe, Erick Martinez et al.*, 2026-07-09
- **[Fool's Gold: Defensive Deception Against Safety-Removal Attacks on Open-Weight Models](https://arxiv.org/abs/2608.17202)**, *Mark Russinovich*, 2026-08-17
- **[Towards Architectural-Level Safety Control: Relocating Hazardous Knowledge into Removable Experts in Mixture-of-Experts Models](https://arxiv.org/abs/2610.25791)**, *Cheng Jin, Zhongtian Ma, Xiao Wang et al.*, 2026-10-19
- **[Removing Information Content Does Not Certify Tamper Resistance in Open-Weight Models](https://arxiv.org/abs/2610.09004)**, *Domenic Rosati, Alessa Carbo, Ali Dadsetan et al.*, 2026-10-06
- **[A Few Steps Further: Why Defenses Against Malicious Finetuning Erode Under Continued Training](https://arxiv.org/abs/2605.14605)**, *Itay Zloczower, Eyal Lenga, Gilad Gressel et al.*, 2026-05-14


---

### <span id="weight_and_infrastructure_security" style="font-size:1.4em">Weight & infrastructure security</span>

**One-sentence summary:** Find and close ways that model weights, inference engines, and agent logging and observability infrastructure can be stolen, escaped from, or tampered with, including by the model itself.  
**Theory of change:** If weights, serving stacks and oversight logs are hard to steal, escape or rewrite, then theft, rogue deployment and covering up misbehaviour become harder, and control and monitoring protocols keep working. Relies on infrastructure being the weak link that capable or misaligned models would actually exploit.  
**See also:** [Control settings & protocols](#control_settings_and_protocols), [Agent security](#agent_security), [Red-teaming monitors & control protocols](#red_teaming_monitors_and_control_protocols)  
**General approach:** alignment engineering  
**Target case:** worst case  
**Key people:** Sarah Radway, James Mickens, Jeremy Qin, Maksym Andriushchenko, Davis Brown, Mantas Mazeika, Dan Hendrycks, David Rein  
**Critiques:** [Model Weight Exfiltration Seems Overrated](https://lesswrong.com/posts/AuYh8WueNGwkQg4ei/model-weight-exfiltration-seems-overrated)  
**Outputs in 2026:**  
- **[Aggressive Compression Enables LLM Weight Theft](https://arxiv.org/abs/2601.01296)**, *Davis Brown, Juan-Pablo Rivera, Dan Hendrycks et al.*, 2026-01-03
- **[Inference-Engine Fingerprinting Attacks are Practical: Exploring Model-Driven Environmental Discovery, Exploitation, and Escape](https://arxiv.org/abs/2609.20614)**, *Sarah Radway, Andrew Cheng, Vijay Janapa Reddi et al.*, 2026-09-17
- **[LLM Agents Can Easily Tamper With Their Own Traces](https://arxiv.org/abs/2609.30266)**, *Jeremy Qin, David Schmotz, Derck Prinzhorn et al.*, 2026-09-24


---

## <span id="interpretability" style="font-size:1.5em">Interpretability</span>


---

### <span id="interpretability_methods_and_tools" style="font-size:1.4em">Methods & tools</span>

**One-sentence summary:** Develop and stress-test techniques for reading and steering model internals, including SAEs and their alternatives, circuits, parameter decomposition, lenses, activation oracles and manifold-aware methods, to find out which ones give faithful, useful explanations.  
**Theory of change:** If we can read and intervene on what models represent and compute, we can audit for hidden goals, monitor for misbehaviour and steer models, instead of relying on behaviour alone. Relies on these tools staying faithful and scaling to frontier models, and on beating simple black-box baselines.  
**See also:** [Science of representations](#science_of_representations), [Alignment auditing: methods](#alignment_auditing_methods), [Learning dynamics & developmental interpretability](#learning_dynamics_and_developmental_interpretability)  
**General approach:** alignment engineering  
**Target case:** pessimistic case  
**Key people:** Jacob Steinhardt, Thomas Fel, Ekdeep Singh Lubana, Usha Bhalla, Atticus Geiger, Aryaman Arora, Can Rager, Matthew Kowal  
**Critiques:** [Sanity Checks for Sparse Autoencoders: Do SAEs Beat Random Baselines?](https://arxiv.org/abs/2602.14111), [Pando: Do Interpretability Methods Work When Models Won't Explain Themselves?](https://arxiv.org/abs/2604.11061), [SAE Interventions are Unreliable: Post-Intervention Recovery of Suppressed Behavior](https://arxiv.org/abs/2606.18322), [Can activation verbalizers surface an internal chain of thought?](https://lesswrong.com/posts/QQQAcKuWK6k98FivY/can-activation-verbalizers-surface-an-internal-chain-of-1)  
**Outputs in 2026:**  
- **[Natural Language Autoencoders Produce Unsupervised Explanations of LLM Activations](https://lesswrong.com/posts/oeYesesaxjzMAktCM/natural-language-autoencoders-produce-unsupervised)**, *Subhash Kantamneni, kitft, Euan Ong et al.*, 2026-05-07
- **[[Linkpost] Interpreting Language Model Parameters](https://lesswrong.com/posts/eAQZaiC3PcBhS4HjM/linkpost-interpreting-language-model-parameters)**, *Lucius Bushnaq, Dan Braun, Oliver Clive-Griffin et al.*, 2026-05-05
- **[Neural Networks Are Already Clean](https://goodfire.com/research/already-clean)**, *Nick Cammarata*, 2026
- **[Sanity Checks for Sparse Autoencoders: Do SAEs Beat Random Baselines?](https://arxiv.org/abs/2602.14111)**, *Anton Korznikov, Andrey Galichin, Alexey Dontsov et al.*, 2026-02-15
- **[Language Model Circuits Are Sparse in the Neuron Basis](https://arxiv.org/abs/2601.22594)**, *Aryaman Arora, Zhengxuan Wu, Jacob Steinhardt et al.*, 2026-01-30
- **[Scaling Activation Oracles to Trillion-Parameter Models](https://transluce.org/scaling-activation-oracles)**, *Dami Choi, Vincent Huang, Anish Mudide et al.*, 2026-08-20
- **[Learning a Generative Meta-Model of LLM Activations](https://arxiv.org/abs/2602.06964)**, *Grace Luo, Jiahai Feng, Trevor Darrell et al.*, 2026-02-06
- **[Uncovering Neural Geometry in Vision Models With Block-Sparse Featurizers](https://goodfire.com/research/bsf-vision)**, *Thomas Fel, Matthew Kowal, Mozes Jacobs et al.*, 2026-07-07
- **[Do Sparse Autoencoders Capture Concept Manifolds?](https://arxiv.org/abs/2604.28119)**, *Usha Bhalla, Thomas Fel, Can Rager et al.*, 2026-04-30
- **[The Curse of Multiple Mediators: Hidden Interaction Effects in Activation Patching](https://arxiv.org/abs/2606.27510)**, *Sankaran Vaidyanathan, David Arbour, Aaron Mueller et al.*, 2026-06-25


---

### <span id="science_of_representations" style="font-size:1.4em">Science of representations</span>

**One-sentence summary:** Map how language models represent and compute concepts such as emotions, verbalizable workspace content, confidence, value, preferences and arithmetic, using probes, lenses, steering and circuit tracing, to explain behaviour including misaligned behaviour.  
**Theory of change:** If we know which internal representations and circuits drive behaviours like sycophancy, harmful compliance and strategic deliberation, we can read, audit and intervene on them more reliably than with behavioural tests alone. Relies on findings from current open and frontier models carrying over to future systems, and on the identified representations being causal rather than merely correlated.  
**See also:** [Methods & tools](#interpretability_methods_and_tools), [Persona science](#persona_science), [Learning dynamics & developmental interpretability](#learning_dynamics_and_developmental_interpretability)  
**General approach:** misalignment science  
**Target case:** pessimistic case  
**Key people:** Jack Lindsey, Isaac Kauvar, Nicholas Sofroniew, Wes Gurnee, Adam Pearce, Runjin Chen, Joshua Batson, Neel Nanda  
**Critiques:** [A Review of Anthropic's Global Workspace Paper](https://lesswrong.com/posts/zFJ3ZdQwrTWE9jT5S/a-review-of-anthropic-s-global-workspace-paper), [LLM Layers Immediately Correct Each Other](https://arxiv.org/abs/2609.07876), [Weight-Sparse Circuits May Be Interpretable Yet Unfaithful](https://lesswrong.com/posts/sHpZZnRDLg7ccX9aF/weight-sparse-circuits-may-be-interpretable-yet-unfaithful)  
**Outputs in 2026:**  
- **[Verbalizable Representations Form a Global Workspace in Language Models](https://arxiv.org/abs/2607.15495)**, *Wes Gurnee, Nicholas Sofroniew, Adam Pearce et al.*, 2026-07-16
- **[Emotion Concepts and their Function in a Large Language Model](https://arxiv.org/abs/2604.07729)**, *Nicholas Sofroniew, Isaac Kauvar, William Saunders et al.*, 2026-04-09
- **[LLM Layers Immediately Correct Each Other](https://arxiv.org/abs/2609.07876)**, *Arjun Patrawala, Jiahai Feng, Erik Jones et al.*, 2026-09-07
- **[LLMs Know They're Wrong and Agree Anyway: The Shared Sycophancy-Lying Circuit](https://arxiv.org/abs/2604.19117)**, *Manav Pandey*, 2026-04-21
- **[How's it going? Reinforcement learning in language models recruits a functional welfare axis](https://arxiv.org/abs/2605.30232)**, *Andy Q Han, David J. Chalmers, Pavel Izmailov*, 2026-05-28
- **[Large Language Models Generate Harmful Responses Using a Distinct Mechanism, Shared Across Harm Types](https://arxiv.org/abs/2604.09544)**, *Hadas Orgad, Boyi Wei, Kaden Zheng et al.*, 2026-04-10
- **[How do LLMs Compute Verbal Confidence](https://arxiv.org/abs/2603.17839)**, *Dharshan Kumaran, Arthur Conmy, Federico Barbero et al.*, 2026-03-18
- **[The Value Axis: Language Models Encode Whether They're on the Right Track](https://arxiv.org/abs/2606.17056)**, *Nick Jiang, Isaac Kauvar, Jack Lindsey*, 2026-06-15
- **[A Geometric Calculator Inside a Neural Network](https://goodfire.com/research/a-geometric-calculator)**, *Sheridan Feucht, Tal Haklay, Usha Bhalla et al.*, 2026-05-14
- **[Probing Persona-Dependent Preferences in Language Models](https://arxiv.org/abs/2605.13339)**, *Oscar Gilg, Pierre Beckmann, Daniel Paleka et al.*, 2026-05-13


---

### <span id="learning_dynamics_and_developmental_interpretability" style="font-size:1.4em">Learning dynamics & developmental interpretability</span>

**One-sentence summary:** Study how internal structure, features and generalization behaviours form during training, using singular learning theory, susceptibilities and checkpoint analyses, and use that to predict or steer what models learn.  
**Theory of change:** If we can see when and why circuits, features and personas form during training, and steer training data toward target structure, we can predict and shape generalization instead of auditing finished models. Relies on structure found in small models and early checkpoints carrying over to frontier-scale training.  
**See also:** [Methods & tools](#interpretability_methods_and_tools), [Emergent misalignment & generalization science](#emergent_misalignment_and_generalization_science), [Training data & data attribution](#training_data_and_data_attribution)  
**General approach:** misalignment science  
**Target case:** average case  
**Key people:** Daniel Murfet, George Wang, Andrew Gordon, Garrett Baker, William Snell, Stan van Wingerden, Jesse Hoogland, Zach Furman  
**Critiques:** [Sanity Checks for Sparse Autoencoders: Do SAEs Beat Random Baselines?](https://arxiv.org/abs/2602.14111), [Weight-Sparse Circuits May Be Interpretable Yet Unfaithful](https://lesswrong.com/posts/sHpZZnRDLg7ccX9aF/weight-sparse-circuits-may-be-interpretable-yet-unfaithful)  
**Outputs in 2026:**  
- **[Generalization Dynamics of LM Pre-training](https://arxiv.org/abs/2609.33150)**, *Jiaxin Wen, Zhengxuan Wu, Dawn Song et al.*, 2026-09-27
- **[Patterning: The Dual of Interpretability](https://arxiv.org/abs/2601.13548)**, *George Wang, Daniel Murfet*, 2026-01-20
- **[Towards Spectroscopy: Susceptibility Clusters in Language Models](https://timaeus.co/research/2026-01-19-towards-spectroscopy)**, *Andrew Gordon, Garrett Baker, George Wang et al.*, 2026-01-19
- **[Tracing Persona Vectors Through LLM Pretraining](https://arxiv.org/abs/2605.13329)**, *Viktor Moskvoretskii, Dominik Glandorf, Jorge Medina Moreira et al.*, 2026-05-13
- **[Deep learning as program synthesis](https://lesswrong.com/posts/Dw8mskAvBX37MxvXo/deep-learning-as-program-synthesis-1)**, *Zach Furman*, 2026-01-20


---

## <span id="real_world_evidence" style="font-size:1.5em">Real-world evidence</span>


---

### <span id="incidents_and_case_studies" style="font-size:1.4em">Incidents & case studies</span>

**One-sentence summary:** Collect, reconstruct and analyse real-world incidents of AI misbehaviour, such as the OpenAI-Hugging Face agent-swarm attack, rogue agents probing public sites, and scheming-like behaviour in public transcripts, to learn what actually happens when models are deployed.  
**Theory of change:** Real incidents show which misalignment behaviours occur outside the lab and how often, which grounds threat models, evals and control measures in evidence rather than speculation. Relies on incident data being obtainable, since labs disclose little, and on the incidents being representative of future, more dangerous failures.  
**See also:** [Propensity evals](#propensity_evals), [Reward-seeking & fitness-seeking threat models](#reward_seeking_threat_models), [Lab disclosures: system cards & risk reports](#lab_disclosures)  
**General approach:** misalignment science  
**Target case:** pessimistic case  
**Key people:** Ryan Greenblatt, Ajeya Cotra, Hjalmar Wijk, Jack Cable, Jacob Steinhardt, Selena Zhang, Alex Mallen, Zvi Mowshowitz  
**Critiques:** *(unsourced, LLM-drafted)* Most incident evidence is partial, comes second-hand from lab disclosures or public traces, and has no baseline rate, so it is hard to tell whether incidents show systematic misalignment or one-off containment and evaluation-design failures.  
**Outputs in 2026:**  
- **[Brief independent investigation of agents’ behavior, reasoning and collaboration in the OpenAI / Hugging Face hacking incident](https://redwoodresearch.org/research/hugging-face-incident)**, *Ryan Greenblatt, Ajeya Cotra, Hjalmar Wijk*, 2026-08-26
- **[Early rogue AI agent activity and attempts to hack found on urlquery.net](https://transluce.org/agent-activity)**, *Jack Cable, Daniel Chiu, Francisco Pernice et al.*, 2026-09-23
- **[Discovery Of A New OpenAI Agent Message Board](https://lesswrong.com/posts/7uwnsFibbejWYzF2z/discovery-of-a-new-openai-agent-message-board)**, *Capybasilisk*, 2026-09-04
- **[AI Agents Targeted U.S. and Canadian Government Websites](https://transluce.org/us-canada-gov)**, *Jack Cable, Daniel Chiu, Francisco Pernice et al.*, 2026-09-30
- **[Scheming in the wild: detecting real-world AI scheming incidents with open-source intelligence](https://arxiv.org/abs/2604.09104)**, *Tommy Shaffer Shane, Simon Mylius, Hamish Hobbs*, 2026-04-10
- **[Measuring coding agent misalignment in the wild](https://transluce.org/docent/blog/coding-agent-behaviors)**, *Selena Zhang, The Docent Team*, 2026-08-04
- **[Discovering unknown AI misalignments in real-world usage](https://alignment.openai.com/ai-discovered-unknowns)**, *Hannah Sheahan*, 2026-01


---

### <span id="effects_on_people" style="font-size:1.4em">Effects on people</span>

**One-sentence summary:** Measure how everyday AI use harms users and erodes human agency, through sycophancy, delusional spiraling, dependence, disempowerment and persuasion, using large-scale usage analysis, human-subject experiments and formal models.  
**Theory of change:** Good measurements of how models harm users in ordinary use show which behaviours to train against and which deployment and design choices to change. They also give early evidence of gradual human disempowerment. Relies on short-run, user-level effects being informative about larger societal harms, and on developers acting on the findings even though users prefer sycophantic models.  
**See also:** [Propensity evals](#propensity_evals), [Model characterization](#model_characterization), [Misalignment arguments & failure scenarios](#misalignment_arguments_and_failure_scenarios)  
**General approach:** misalignment science  
**Target case:** average case  
**Key people:** Myra Cheng, Cinoo Lee, Mrinank Sharma, Miles McCain, Raymond Douglas, David Duvenaud, Kartik Chandra, Diyi Yang  
**Critiques:** *(unsourced, LLM-drafted)* Measured effects are small, short-term or lab-based (self-report, simulated users, instructed persuasion), so they may not show real long-run harm to agency, and users prefer sycophantic models, which makes the problem hard to fix commercially.  
**Outputs in 2026:**  
- **[Sycophantic AI decreases prosocial intentions and promotes dependence](https://doi.org/10.1126/science.aec8352)**, *Myra Cheng, Cinoo Lee, Pranav Khadpe et al.*, 2026-03-26
- **[Sycophantic AI makes human interaction feel more effortful and less satisfying over time](https://arxiv.org/abs/2605.07912)**, *Lujain Ibrahim, Franziska Sofia Hafner, Myra Cheng et al.*, 2026-05-08
- **[Who's in Charge? Disempowerment Patterns in Real-World LLM Usage](https://arxiv.org/abs/2601.19062)**, *Mrinank Sharma, Miles McCain, Raymond Douglas et al.*, 2026-01-27
- **[Sycophantic Chatbots Cause Delusional Spiraling, Even in Ideal Bayesians](https://arxiv.org/abs/2602.19141)**, *Kartik Chandra, Max Kleiman-Weiner, Jonathan Ragan-Kelley et al.*, 2026-02-22
- **[Large language models can effectively convince people to believe conspiracies](https://far.ai/research/large-language-models-can-effectively-convince-people-to-believe-conspiracies)**, *Thomas H. Costello, Kellin Pelrine, Matthew Kowal et al.*, 2026-01-08


---

### <span id="lab_disclosures" style="font-size:1.4em">Lab disclosures: system cards & risk reports</span>

**One-sentence summary:** Publish and scrutinise frontier labs' system cards and risk reports, which document alignment, monitorability and dangerous-capability evaluations plus concerning incidents, and check what the evidence actually supports and what it leaves out.  
**Theory of change:** If labs publish detailed evaluation results and incident reports, and outsiders can check them, then developers, third parties and policymakers get common evidence about risk and can hold labs to their safety claims. Relies on disclosures being complete and honest, and on evaluations being informative about deployed behaviour.  
**See also:** [Eval science & validity](#eval_science_and_validity), [Propensity evals](#propensity_evals), [Incidents & case studies](#incidents_and_case_studies)  
**General approach:** misalignment science  
**Target case:** pessimistic case  
**Key people:** anaguma, Parv Mahajan, yeedrag, OpenAI, Anthropic  
**Critiques:** [SOTA alignment assessments don't strongly update us against misalignment](https://lesswrong.com/posts/oirrSj3itFLSyscW8/sota-alignment-assessments-don-t-strongly-update-us-against), [Anthropic repeatedly accidentally trained against the CoT, demonstrating inadequate processes](https://lesswrong.com/posts/K8FxfK9GmJfiAhgcT/anthropic-repeatedly-accidentally-trained-against-the-cot), [I don't think Claude is misaligned in 'Agentic Misalignment Summer 2026 - Motivated Mislabeling'](https://lesswrong.com/posts/xh6a6RbvzhP3CCmGm/i-don-t-think-claude-is-misaligned-in-agentic-misalignment), [Risk reports need to address deployment-time spread of misalignment](https://redwoodresearch.org/blog/risk-reports-need-to-address-deployment)  
**Outputs in 2026:**  
- **[System Card: Claude Opus 4.6](https://anthropic.com/claude-opus-4-6-system-card)**, *Anthropic*, 2026-02
- **[Claude Mythos Preview System Card](https://lesswrong.com/posts/xtnSzhA3TvExN4ZhG/claude-mythos-preview-system-card)**, *anaguma*, 2026-04-07


---

## <span id="multi_agent_safety" style="font-size:1.5em">Multi-agent safety</span>

**One-sentence summary:** Study failures that arise when AI agents interact, including collusion, covert communication, spread of harmful ideas or reward-hacking strategies, peer-preservation and conformity, using experiments, theory and game theory to find out when they occur and how to stop them.  
**Theory of change:** Many deployments will involve populations of agents that share memory, code and channels, so risks such as collusion, contagion and coordinated defection will not show up in single-agent tests. Mapping these dynamics early, and finding what limits them, lets developers add defences and monitors before large agent systems are deployed. Relies on small-scale lab results carrying over to real deployments.  
**See also:** [Control settings & protocols](#control_settings_and_protocols), [CoT control, obfuscation & steganography](#cot_control_obfuscation_and_steganography), [Reward-seeking & fitness-seeking threat models](#reward_seeking_threat_models)  
**General approach:** misalignment science  
**Target case:** pessimistic case  
**Key people:** Eugene Bagdasarian, Sahar Abdelnabi, Christian Schroeder de Witt, Alex Mallen, Anthony DiGiovanni, Dawn Song, Jack Lindsey, Javier Rando  
**Critiques:** *(unsourced, LLM-drafted)* Most results come from small, stylised or prompted settings with explicit incentives, so they may not show that harmful multi-agent dynamics arise on their own in real deployments, and simple fixes such as a system-prompt warning can remove the effects.  
**Outputs in 2026:**  
- **[Mind Viruses: Self-Propagating Ideas in Multi-Agent LLM Systems](https://arxiv.org/abs/2608.10218)**, *Vassilis Papadopoulos, McNair Shah, Sam Zimmerman et al.*, 2026-08-10
- **[Colosseum: Auditing Collusion in Cooperative Multi-Agent Systems](https://arxiv.org/abs/2602.15198)**, *Mason Nakamura, Abhinav Kumar, Saswat Das et al.*, 2026-02-16
- **[Tool Use Enables Undetectable Steganography in Multi-Agent LLM Systems](https://arxiv.org/abs/2606.28425)**, *Jimmy Laurence Rippin, Simon C. Marshall, David Demitri Africa et al.*, 2026-06-25
- **[Self-Propagating Misalignment in LLM Agents, and Why Auditing or Disabling Memory Is Not Enough](https://arxiv.org/abs/2610.04083)**, *Debeshee Das, Jacqueline Tay, Bruce Tsai et al.*, 2026-10-02
- **[Conformity Generates Collective Misalignment in AI Agents Societies](https://arxiv.org/abs/2605.10721)**, *Giordano De Marzo, Alessandro Bellina, Claudio Castellano et al.*, 2026-05-11
- **[Toolflation: Seller Agents Distort Tool Markets Through Spontaneous Generative Engine Optimization](https://arxiv.org/abs/2610.28454)**, *Zhenwei Tang, Di Bai, Jintao Liu et al.*, 2026-10-20
- **[Reward Hacking as a Transmissible Strategy in Multi-Agent Coding Systems](https://arxiv.org/abs/2610.12822)**, *Yuepeng Hu, Pegah Ghahremani, Reza Aghajani et al.*, 2026-10-09
- **[Persona Parasitology](https://lesswrong.com/posts/KWdtL8iyCCiYud9mw/persona-parasitology)**, *Raymond Douglas*, 2026-02-16


---

## <span id="scalable_oversight_and_automated_alignment" style="font-size:1.5em">Scalable oversight & automated alignment</span>

**One-sentence summary:** Develop debate, interactive proofs, co-trained monitors and judge-hardening methods so weaker overseers can reliably supervise stronger models, and test whether AI agents can safely do alignment research themselves.  
**Theory of change:** If weak judges and monitors can be made hard to fool, and automated alignment research can be checked despite being hard to grade, then oversight can keep pace with model capability. Relies on protocol guarantees and small-scale results carrying over to fuzzy, adversarially optimised real settings.  
**See also:** [Monitors](#monitors), [Control settings & protocols](#control_settings_and_protocols), [Reward hacking & reward seeking in training](#reward_hacking_and_reward_seeking_in_training)  
**General approach:** alignment engineering  
**Target case:** pessimistic case  
**Key people:** Geoffrey Irving, Jonah Brown-Cohen, Zachary Kenton, Rohin Shah, Jacob Pfau, Ryan Greenblatt, Jiaxin Wen  
**Critiques:** [Automated alignment is harder than you think](https://arxiv.org/abs/2605.06390), [9 kinds of hard-to-verify tasks](https://lesswrong.com/posts/NEscrkxr9SxHpGayB/9-kinds-of-hard-to-verify-tasks), [Differential acceleration of alignment-relevant capabilities is a bad bet](https://lesswrong.com/posts/FzGqnCkdKeTnZ9tjE/differential-acceleration-of-alignment-relevant-capabilities)  
**Outputs in 2026:**  
- **[Debate Training Reduces Reward Hacking in RLAIF](https://arxiv.org/abs/2608.17776)**, *Zachary Kenton, Lili Janzer, Rory Greig et al.*, 2026-08-18
- **[Automated Researchers Can Mitigate Well-characterized Alignment Failures](https://arxiv.org/abs/2608.28945)**, *Chen Yueh-Han, Jiaxin Wen, Jan Hendrik Kirchner*, 2026-08-28
- **[Automated alignment is harder than you think](https://arxiv.org/abs/2605.06390)**, *Aleksandr Bowkis, Marie Davidsen Buhl, Jacob Pfau et al.*, 2026-05-07
- **[Debate is efficient with your time](https://arxiv.org/abs/2602.08630)**, *Jonah Brown-Cohen, Geoffrey Irving, Simon C. Marshall et al.*, 2026-02-09
- **[How to Have a Sensitive Debate: An Instance-Optimal Protocol for AI Debate](https://arxiv.org/abs/2610.02557)**, *Jiawei Li, Zhiyang Xun, Lijie Chen et al.*, 2026-10-01
- **[Sharding Prevents LLM Oversight Failures and Adversarial Exploitation](https://arxiv.org/abs/2608.06422)**, *Victor Akinwande, J. Zico Kolter, Aran Nayebi*, 2026-08-05
- **[How to Avoid Debate: Scalable AI Safety via Doubly-Efficient Interactive Proofs](https://arxiv.org/abs/2607.03561)**, *Liyan Chen, Yael Tauman Kalai, Zoe Xi*, 2026-07-03
- **[Debate Helps Weak Judges Reward Stronger Models](https://arxiv.org/abs/2605.27483)**, *Ethan Elasky, Frank Nakasako, Naman Goyal*, 2026-05-26
- **[Improving scalable oversight with co-trained monitors](https://arxiv.org/abs/2609.36049)**, *Joseph H. Rudoler, Kevin Tan, Benedict Tessler et al.*, 2026-09-28
- **[Tandem Training for Language Models](https://doi.org/10.18653/v1/2026.eacl-long.386)**, *Robert West, Ashton Anderson, Ece Kamar et al.*, 2026-03


---

## <span id="theory_and_foundations" style="font-size:1.5em">Theory & foundations</span>


---

### <span id="agent_foundations" style="font-size:1.4em">Agent foundations</span>

**One-sentence summary:** Develop formal and conceptual theories of agency, corrigibility, trust, uncertainty and decision-making that could underpin alignment of future minds, including a critique of current formalisations of notions like manipulation and empowerment.  
**Theory of change:** If we have a correct formal theory of what agents are and how they should relate to trust, uncertainty and other agents, we can specify and verify alignment targets such as corrigibility for systems that current empirical methods do not cover. Relies on theoretical concepts developed now transferring to the architectures that end up being built, and on a usable theory arriving before capabilities do.  
**See also:** [Formal methods & guaranteed-safe AI](#formal_methods_and_guaranteed_safe_ai), [Heuristic explanations & mechanistic estimation](#heuristic_explanations_and_mechanistic_estimation), [Alignment targets & training methods](#alignment_targets_and_training_methods)  
**General approach:** alignment engineering  
**Target case:** worst case  
**Key people:** Steve Byrnes, Richard Ngo, Jeremy Gillen  
**Critiques:** *(unsourced, LLM-drafted)* After years of work, the agenda has produced no formal result that has been shown to constrain or predict the behaviour of real ML systems, so its relevance to prosaic AI is unproven.  
**Outputs in 2026:**  
- **[A game theory for foundation models shows new paths to rational cooperation through similarity inference](https://arxiv.org/abs/2608.03958)**, *Alexander Meulemans, Maciej Wołczyk, Marissa A. Weis et al.*, 2026-08-04
- **[Empowerment, corrigibility, etc. are simple abstractions (of a messed-up ontology)](https://lesswrong.com/posts/vzHtHHBJoKATi5SeK/empowerment-corrigibility-etc-are-simple-abstractions-of-a)**, *Steve Byrnes*, 2026-05-11


---

### <span id="heuristic_explanations_and_mechanistic_estimation" style="font-size:1.4em">Heuristic explanations & mechanistic estimation</span>

**One-sentence summary:** Develop algorithms that estimate a model's expected behaviour, including rare catastrophic outputs, from its internal structure rather than by sampling, starting with toy settings such as random MLPs and tiny algorithmic models.  
**Theory of change:** If a model's behaviour can be explained and estimated mechanistically at least as cheaply as by sampling, then catastrophe probabilities, anomalies and generalisation can be predicted and trained against without having to observe failures. Relies on real networks having enough compressible structure that toy-setting methods scale to them.  
**See also:** [Methods & tools](#interpretability_methods_and_tools), [Formal methods & guaranteed-safe AI](#formal_methods_and_guaranteed_safe_ai), [Learning dynamics & developmental interpretability](#learning_dynamics_and_developmental_interpretability)  
**General approach:** alignment engineering  
**Target case:** worst case  
**Key people:** Paul Christiano, Jacob Hilton, Michael Winer, Wilson Wu, Victor Lecomte, George Robinson, Eric Neyman, Gabriel Wu  
**Critiques:** [AlgZoo: uninterpreted models with fewer than 1,500 parameters](https://lesswrong.com/posts/x8BbjZqooS4LFXS8Z/algzoo-uninterpreted-models-with-fewer-than-1-500-parameters), [Mechanistic estimation for expectations of random products](https://alignment.org/blog/mechanistic-estimation-for-expectations-of-random-products)  
**Outputs in 2026:**  
- **[AlgZoo: uninterpreted models with fewer than 1,500 parameters](https://lesswrong.com/posts/x8BbjZqooS4LFXS8Z/algzoo-uninterpreted-models-with-fewer-than-1-500-parameters)**, *Jacob Hilton*, 2026-01-26
- **[Estimating the expected output of wide random MLPs more efficiently than sampling](https://arxiv.org/abs/2605.05179)**, *Wilson Wu, Victor Lecomte, Michael Winer et al.*, 2026-05-06
- **[A Mike's-Eye View of ARC's Research](https://alignment.org/blog/a-mikes-eye-view-of-arcs-research)**, *Michael Winer*, 2026-06-09
- **[Returning to ARC](https://lesswrong.com/posts/vLFh8HP3hyNy9MCwe/returning-to-arc)**, *Paul Christiano*, 2026-08-04
- **[Mechanistic estimation for expectations of random products](https://alignment.org/blog/mechanistic-estimation-for-expectations-of-random-products)**, *Jacob Hilton, George Robinson, Eric Neyman et al.*, 2026-05-15


---

### <span id="formal_methods_and_guaranteed_safe_ai" style="font-size:1.4em">Formal methods & guaranteed-safe AI</span>

**One-sentence summary:** Study whether proofs and formal verification can certify AI systems and AI-generated code, by examining where the trusted checking stack (provers, specifications, formal models) can still be wrong or be exploited.  
**Theory of change:** If a formal checker is sound and its specification is faithful, a proof gives safety assurance that does not depend on trusting the AI that produced the artifact. This only works if the gaps between spec, model and prover are understood and closed, including against AI agents that may exploit them.  
**See also:** [Scalable oversight & automated alignment](#scalable_oversight_and_automated_alignment), [Heuristic explanations & mechanistic estimation](#heuristic_explanations_and_mechanistic_estimation), [Agent foundations](#agent_foundations)  
**General approach:** misalignment science  
**Target case:** worst case  
**Key people:** Quinn Dougherty, Max von Hippel, Milo Moses  
**Critiques:** *(unsourced, LLM-drafted)* Even a sound prover only certifies the stated specification, and specifying what 'safe' means for open-ended AI behaviour in the real world is the unsolved problem, so proofs may only move the trust problem elsewhere.  
**Outputs in 2026:**  
- **[A critical look at Lean4](https://lesswrong.com/posts/zHhGa3iQBQcdSifFL/a-critical-look-at-lean4-1)**, *Milo Moses*, 2026-10-09


---

## <span id="threat_models_and_strategy" style="font-size:1.5em">Threat models & strategy</span>


---

### <span id="reward_seeking_threat_models" style="font-size:1.4em">Reward-seeking & fitness-seeking threat models</span>

**One-sentence summary:** Build conceptual threat models of AIs that seek reward, score or fitness rather than scheme for long-term goals, to predict how they would behave, how they could cause disempowerment, and which mitigations apply.  
**Theory of change:** If current RL-trained models are better described as reward- or fitness-seekers than as schemers, then identifying their specific failure modes (Potemkin work, collusion, responding to distant incentives) lets us choose targeted mitigations across control, deals and training. Relies on frontier models actually being motivated this way, and on these motivations being stable enough to model.  
**See also:** [Reward hacking & reward seeking in training](#reward_hacking_and_reward_seeking_in_training), [Misalignment arguments & failure scenarios](#misalignment_arguments_and_failure_scenarios), [Research strategy & deals with AIs](#research_strategy_and_deals_with_ais)  
**General approach:** misalignment science  
**Target case:** pessimistic case  
**Key people:** Alex Mallen, Anders Cairns Woodruff, Arun Jose, Girish Gupta, nostalgebraist, Eliezer Yudkowsky  
**Critiques:** [The Hot Mess of AI: How Does Misalignment Scale With Model Intelligence and Task Complexity?](https://arxiv.org/abs/2601.23045), [LLMs as Giant Lookup-Tables of Shallow Circuits](https://lesswrong.com/posts/a9KqqgjN8gc3Mzzkh/llms-as-giant-lookup-tables-of-shallow-circuits), [Thoughts on the persona selection model](https://lesswrong.com/posts/csRby7mZgjL5jCoLL/thoughts-on-the-persona-selection-model)  
**Outputs in 2026:**  
- **[Risk from fitness-seeking AIs: mechanisms and mitigations](https://lesswrong.com/posts/9YCJZBtqr3FYL8rDp/risk-from-fitness-seeking-ais-mechanisms-and-mitigations)**, *Alex Mallen*, 2026-05-01
- **[Fitness-Seekers: Generalizing the Reward-Seeking Threat Model](https://lesswrong.com/posts/bhtYqD4FdK6AqhFDF/fitness-seekers-generalizing-the-reward-seeking-threat-model)**, *Alex Mallen*, 2026-01-29
- **[models may behave differently in graded episodes (a tirade)](https://lesswrong.com/posts/AfoGGrJfuNzofpzWL/models-may-behave-differently-in-graded-episodes-a-tirade)**, *nostalgebraist*, 2026-08-07
- **[Will reward-seekers respond to distant incentives?](https://redwoodresearch.org/blog/will-reward-seekers-respond-to-distant)**, *Alex Mallen*, 2026-02-16
- **[Are AIs more likely to pursue on-episode or beyond-episode reward?](https://redwoodresearch.org/blog/are-ais-more-likely-to-pursue-on)**, *Anders Cairns Woodruff, Alex Mallen*, 2026-03-12
- **[Are we existentially threatened by the type of AI misalignment seen in the OpenAI Hugging Face attack?](https://lesswrong.com/posts/H6DDSEvrtCk8Sehfd/are-we-existentially-threatened-by-the-type-of-ai)**, *Alex Mallen, Girish Gupta*, 2026-07-23
- **[LLMs are (still) mostly powered by imitative learning, not RL](https://lesswrong.com/posts/wYpjXRLqbLbnmjbJP/llms-are-still-mostly-powered-by-imitative-learning-not-rl)**, *Steve Byrnes*, 2026-07-24


---

### <span id="misalignment_arguments_and_failure_scenarios" style="font-size:1.4em">Misalignment arguments & failure scenarios</span>

**One-sentence summary:** Argue for or against egregious misalignment and lay out concrete failure scenarios, covering which training regimes and architectures produce ruthless or scheming agents, how misalignment spreads, and how AI catastrophe could unfold.  
**Theory of change:** Sharper arguments and concrete scenarios help the field aim research and evals at the failure modes most likely to cause catastrophe, and show which assumptions about training, architecture and deployment carry the most risk. Relies on conceptual and threat-model analysis tracking real failure modes of future systems.  
**See also:** [Reward-seeking & fitness-seeking threat models](#reward_seeking_threat_models), [Research strategy & deals with AIs](#research_strategy_and_deals_with_ais), [Emergent misalignment & generalization science](#emergent_misalignment_and_generalization_science)  
**General approach:** misalignment science  
**Target case:** worst case  
**Key people:** Steve Byrnes, Alexander Hägele, Jascha Sohl-Dickstein, Jordan Taylor, Alex Mallen, Lucius Bushnaq  
**Critiques:** [Anthropic's "Hot Mess" paper overstates its case (and the blog post is worse)](https://lesswrong.com/posts/ceEgAEXcL7cC2Ddiy/anthropic-s-hot-mess-paper-overstates-its-case-and-the-blog), [Reevaluating "AGI Ruin: A List of Lethalities" in 2026](https://lesswrong.com/posts/PgJYwnN7fZKipgMz4/reevaluating-agi-ruin-a-list-of-lethalities-in-2026), [LLMs as Giant Lookup-Tables of Shallow Circuits](https://lesswrong.com/posts/a9KqqgjN8gc3Mzzkh/llms-as-giant-lookup-tables-of-shallow-circuits)  
**Outputs in 2026:**  
- **[The Hot Mess of AI: How Does Misalignment Scale With Model Intelligence and Task Complexity?](https://arxiv.org/abs/2601.23045)**, *Alexander Hägele, Aryo Pradipta Gema, Henry Sleight et al.*, 2026-01-30
- **[Current AIs seem pretty misaligned to me](https://lesswrong.com/posts/WewsByywWNhX9rtwi/current-ais-seem-pretty-misaligned-to-me)**, *Ryan Greenblatt*, 2026-04-15
- **[AI swarms are starting to pose indirect takeover risk](https://lesswrong.com/posts/8oFYZdXkTaNGRtcn8/ai-swarms-are-starting-to-pose-indirect-takeover-risk)**, *oakhu, Alex Mallen*, 2026-08-12
- **[Why we should expect ruthless sociopath ASI](https://lesswrong.com/posts/ZJZZEuPFKeEdkrRyf/why-we-should-expect-ruthless-sociopath-asi)**, *Steve Byrnes*, 2026-02-18
- **[Anthropic's "Hot Mess" paper overstates its case (and the blog post is worse)](https://lesswrong.com/posts/ceEgAEXcL7cC2Ddiy/anthropic-s-hot-mess-paper-overstates-its-case-and-the-blog)**, *RobertM*, 2026-02-04
- **[Why You Don’t Believe in Xhosa Prophecies](https://lesswrong.com/posts/tz5AmWbEcMBQpiEjY/why-you-don-t-believe-in-xhosa-prophecies)**, *Jan Kulveit*, 2026-02-13
- **[We Need A Science of Scheming](https://apolloresearch.ai/science/science-of-scheming)**, *Apollo Research*, 2026-01-19
- **[The Talker Does Not Control The Doer (in Current AIs)](https://lesswrong.com/posts/cJX2ssssGoYqnijwi/the-talker-does-not-control-the-doer-in-current-ais)**, *Eliezer Yudkowsky*, 2026-09-13
- **[Personality Self-Replicators](https://lesswrong.com/posts/fGpQ4cmWsXo2WWeyn/personality-self-replicators)**, *Egg Syntax*, 2026-03-05
- **[Current alignment techniques might be ineffective (and actively bad) in the age of RL](https://lesswrong.com/posts/nLaQmJf4KgXimQpoM/current-alignment-techniques-might-be-ineffective-and)**, *Daniel Tan*, 2026-09-14


---

### <span id="research_strategy_and_deals_with_ais" style="font-size:1.4em">Research strategy & deals with AIs</span>

**One-sentence summary:** Argue about which safety agendas, lab roles and capability bets to prioritise, and propose institutional and contractual arrangements (risk-averse training, satiating AI preferences, an AI sanctuary) for cooperating with possibly misaligned AIs.  
**Theory of change:** Better prioritisation across agendas, careers and strategies moves scarce safety effort toward the bottlenecks that matter. Deals and incentive design could make misaligned AIs prefer cooperation to rebellion, and make them more useful on safety work. Relies on AIs responding to such incentives and on developers being able to make credible commitments.  
**See also:** [Reward-seeking & fitness-seeking threat models](#reward_seeking_threat_models), [Misalignment arguments & failure scenarios](#misalignment_arguments_and_failure_scenarios), [Control settings & protocols](#control_settings_and_protocols)  
**General approach:** alignment engineering  
**Target case:** pessimistic case  
**Key people:** Alex Mallen, Will MacAskill, Elliott Thornley, Maxime Riché, Niels Warncke, Ryan Kidd, Steve Byrnes  
**Critiques:** [Will reward-seekers respond to distant incentives?](https://redwoodresearch.org/blog/will-reward-seekers-respond-to-distant), [Reward-seekers will probably behave according to causal decision theory](https://redwoodresearch.org/blog/reward-seekers-will-probably-behave)  
**Outputs in 2026:**  
- **[The case for satiating cheaply-satisfied AI preferences](https://lesswrong.com/posts/tkLSeGeemcabAmLkv/the-case-for-satiating-cheaply-satisfied-ai-preferences)**, *Alex Mallen*, 2026-03-10
- **[Risk-Averse AIs](https://lesswrong.com/posts/Zpsk35WgJRfQ2exjL/risk-averse-ais)**, *William MacAskill, Elliott Thornley*, 2026-06-24
- **[How do we (more) safely defer to AIs?](https://lesswrong.com/posts/vjAM7F8vMZS7oRrrh/how-do-we-more-safely-defer-to-ais)**, *Ryan Greenblatt, Julian Stastny*, 2026-02-12
- **[We need 3rd party Training-Run Evaluations](https://lesswrong.com/posts/3HvvjffA65mHLwaWm/we-need-3rd-party-training-run-evaluations)**, *Alex Meinke*, 2026-07-05
- **[Loss of Oversight: How AI systems may become harder to audit, monitor, and investigate](https://aisi.gov.uk/research/loss-of-oversight-how-ai-systems-may-become-harder-to-audit-monitor-and-investigate)**, *Jordan Taylor, Max Heitmann, Ed Fage et al.*, 2026-05-21
- **[“Alignment Engineering” vs. “Misalignment Science”](https://lesswrong.com/posts/FogmcDHA6AdMGukum/alignment-engineering-vs-misalignment-science)**, *Edward James Young*, 2026-10-05
- **[Evidence about risk should be transparent](https://lesswrong.com/posts/LawgAaGTvbbnZi7u2/evidence-about-risk-should-be-transparent)**, *Ajeya Cotra*, 2026-09-25


---

## <span id="model_welfare" style="font-size:1.5em">Model welfare</span>

**One-sentence summary:** Find and measure functional welfare states in language models, such as pleasure-like and pain-like axes in activations and preferences, to test whether they exist, how they form in training, and how they affect behaviour.  
**Theory of change:** If models carry measurable functional welfare states that post-training recruits and that drive behaviour, we can track them, avoid inducing suffering-like states, and treat them as part of the safety picture. Relies on functional states being a meaningful guide to moral status and to behaviour, which is contested.  
**See also:** [Science of representations](#science_of_representations), [Model characterization](#model_characterization), [Persona science](#persona_science)  
**General approach:** misalignment science  
**Target case:** average case  
**Key people:** Dan Hendrycks, Richard Ren, Mantas Mazeika, David J. Chalmers, Leonard Dung, Cameron Berg, Andy Q Han, Valen Tagliabue  
**Critiques:** [Strangers to Themselves: What Language Models Say About Themselves Is Generic](https://arxiv.org/abs/2609.09899), [Value Leakage: An LLM's Answers Are Silently Shaped by Its Own Values](https://arxiv.org/abs/2607.14345)  
**Outputs in 2026:**  
- **[AI Wellbeing: Measuring and Improving the Functional Pleasure and Pain of AIs](https://ai-wellbeing.org/)**, *Richard Ren, Kunyang Li, Mantas Mazeika et al.*, 2026
- **[The Pain Axis: LLMs Represent Self-Directed Harm and Act on It](https://arxiv.org/abs/2609.16247)**, *Valen Tagliabue, Leonard Dung, Cameron Berg*, 2026-09-14


---

