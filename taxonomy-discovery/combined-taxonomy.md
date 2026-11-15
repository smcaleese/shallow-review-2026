# A combined taxonomy for the 2026 review (Draft 1 + Draft 2)

2026-11-14. A proposal, not yet loaded into `draft-pipeline`.

**Inputs**
- **Draft 1:** the hand-written taxonomy (`draft-pipeline/data/taxonomy-draft-2026-11-03.yaml`, the same as `draft-taxonomy.md`). It has 12 areas and 43 agendas.
- **Draft 2:** the data-driven taxonomy currently in `draft-pipeline/data/taxonomy.yaml` (`data-driven-taxonomy.md`). It has 4 areas and 15 agendas.
- **Your notes** on reading the Draft 2 draft.
- **The 2025 review** (`documents/shallow-review-2025.md`).

**Evidence used throughout**
- **D1 n:** entries per Draft 1 agenda, from the export of 2026-11-10 (`draft-2026-facets.md`). That export classified the earlier 499 facets sources with Draft 1.
- **D2 n:** entries per Draft 2 agenda among the current 625 pipeline sources.
- **Methods:** the median size of the matching agenda across the six taxonomy-discovery methods, and how many methods found it (`recurring-agendas.md`).
- **Pool:** keyword counts and karma from the filtered arXiv and LessWrong data that the shortlist cut down.

---

## 1. Summary

- **Structure.** 6 parts, then 14 areas, then 51 agendas. The 2025 review also had three levels: area, sub-area, agenda.
  - The **parts** start from Draft 2's grouping: training, then understanding, then deployment, then the wider picture. *Make AI solve it* and *Theory & safety by construction* are parts of their own, each a single area.
  - **Changed after draft 3:** *Model characterization* and *Formal methods, guarantees & impossibility results* were dropped (weak and largely inactive; their entries were reclassified, and they're in the graveyard in section 10). *Theory & foundations* and *Safety by construction* were merged, with Scientist AI kept as its own agenda (11.6).
  - The **areas** are mostly Draft 1's, named after recognisable research fields.
  - The **agendas** are Draft 1's, except where the method data or your notes argue for a split or merge.
  - The parts are optional: the 14 areas also work as the top level.
- **Taken from Draft 1:**
  - Field-named areas.
  - Finer splits of CoT, evaluations, control and security.
  - The *Real-world evidence*, *Theory*, *Strategy* and *Welfare* areas.
  - Most agenda descriptions.
- **Taken from Draft 2:**
  - The part-level grouping (training, then understanding, then deployment).
  - Agenda boundaries the methods agree on: scheming and training gaming together; subliminal learning with data attribution; reward-seeking next to reward hacking; lie detection as its own agenda.
  - The placement rules for hard cases.
- **12 agendas that weren't standalone Draft 1 agendas.** Six were split out of a Draft 1 leaf; six are new:
  - **Split out:** generalization science; alignment training methods; model specs & constitutions; steering & activation engineering; automated alignment research; corrigibility theory.
  - **New:** whose values (pluralistic alignment); lie detection & deception probes; data poisoning & backdoors; natural abstractions; Scientist AI; brain-like AGI safety.
- **One Draft 1 agenda merged:** *Models resisting training* goes into *Scheming, sabotage & training gaming*.
- **One Draft 1 agenda moved:** *Reward-seeking threat models* moves from Strategy to the RL area.
- **It isn't missing any 2025 agenda that is still active.** Section 6 maps every 2025 agenda.
  - The only 2025 agendas without a home have almost no 2026 activity: mild optimisation, high-actuation spaces, assistance games, tiling agents, human inductive biases, self-other overlap. They're graveyard candidates (section 10).
- **12 agendas are thin in the current 625 sources, mostly because the shortlists cut them, not because the field is empty.** Section 9 lists about 105 sources to add by hand, for those and four others: theory, steering, pluralism, latent reasoning, automated alignment, welfare, constitutions, strategy.

---

## 2. Design choices

1. **Classify by main contribution.** An item goes where the question it answers belongs, not where its technique belongs. Draft 1's interpretability description already works this way.
   - A deception probe goes to lie detection.
   - A probe used as a deployment monitor goes to monitors.
   - A probe used as an RL reward goes to training signals.
   - Only a new probe *method* goes to interpretability.
2. **Readable.**
   - Parts I–III and VI have 3 areas each; parts IV–V are one area each. Each area has 1–5 agendas.
   - Each agenda gets a one-sentence description that says what's in it and, where it's ambiguous, what isn't.
   - Areas use names readers already know (Interpretability, Evaluations, Monitoring & control). The more abstract names are kept to the part level.
3. **Comprehensive.** Every 2025 agenda with 2026 activity maps to an agenda (section 6). Topics that grew in 2026 get their own agenda:
   - latent reasoning architectures
   - reward-seeking
   - training against internals
   - real-world incidents
   - model welfare
   - automated alignment research
4. **Data-backed sizes.**
   - Most agendas should hold about 10–40 sources, so a top-10 cut is meaningful.
   - Agendas the methods consistently find are kept whole.
   - Splits are made only where several methods split too (alignment pretraining vs. constitutions) or where a leaf is clearly mixed. Draft 2's emergent misalignment leaf is the main example: about 20 of its 51 entries weren't about emergent misalignment.
5. **CoT stays one area.** CoT monitorability cuts across training, understanding and deployment. Like Draft 1, I keep it as one area, because readers look for it as a unit. It sits in Part III because its purpose is monitoring.

---

## 3. The taxonomy

### Part I. Training aligned models: how training determines what models learn, want and are

**1. Training data & generalization.** How training data shapes behaviour, and why training generalizes the way it does.
- **1.1 Data filtering & alignment pretraining.** Choosing, filtering and generating pretraining and midtraining data to shape what models know and become: filtering hazardous or subversion-relevant content, alignment pretraining and hyperstition (how AI discourse in the corpus shapes models), synthetic data for alignment.
- **1.2 Subliminal learning & data attribution.** How specific data transmits behaviour:
  - traits, capabilities and backdoors passed through data that looks unrelated (subliminal learning, distillation transfer);
  - tracing behaviours back to the training data that caused them (data attribution, data debugging).
- **1.3 Emergent misalignment.** Narrow training that causes broad misalignment: emergent and conditional misalignment (including from reward hacking), its mechanisms and robustness, and mitigations other than inoculation.
- **1.4 Inoculation prompting.** Training under prompts that elicit an unwanted behaviour, so the behaviour stays tied to that context instead of generalizing. Includes variants and limits.
- **1.5 Generalization science.** How fine-tuning and post-training generalize, beyond emergent misalignment:
  - predicting generalization from data or prompts;
  - which training stage drives safety properties;
  - surprising generalization failures, such as negation neglect and chunky generalization;
  - goal misgeneralization in RL agents.

**2. RL & alignment training.** How objectives and rewards shape motivations, and methods that train alignment in directly.
- **2.1 Alignment training methods.** Methods that train a desired property directly: RLHF, RLAIF and preference-optimization variants, deliberative alignment, consistency training, RL for beneficial traits, training for shutdownability. (This is the 2025 review's "iterative alignment".)
- **2.2 Reward hacking & specification gaming.**
  - How RL produces reward hacking and specification gaming.
  - Hackable environments and benchmarks.
  - Training-side fixes, such as hardened verifiers or channelling hacks into a harmless outlet.
  - Includes non-LLM RL agents.
- **2.3 Reward-seeking & fitness-seeking.** Reward- and fitness-seeking as learned motivations: threat models of how such AIs would behave, measurements of reward-seeking in current models, and what follows for safety.
- **2.4 Internals & monitors as training signals.** Using probes, features or monitors as training rewards or penalties, and the risk that models learn to fool them (obfuscation) instead of changing their behaviour.

**3. Model character, values & welfare.** What models are like as characters, what we want them to value, and whether they matter morally.
- **3.1 Persona science.** Models of LLMs as characters that training selects and strengthens (persona selection, the Assistant persona, split personas, identity), how training changes which persona a model takes on, and the values and preferences current models express.
- **3.2 Model specs, constitutions & character training.** Writing down the target character (constitutions, model specs), instilling it (character training, spec and constitution midtraining), and checking whether models follow it.
- **3.3 Whose values: pluralistic & social-choice alignment.** Aligning to many people rather than one principal: pluralism, social choice and preference aggregation, and representing disagreement.
- **3.4 Model welfare & moral status.** Model welfare, moral status, and functional emotions, pleasure and pain.

### Part II. Understanding models: finding out what a model is, knows and would do

**4. Interpretability.** Work whose main contribution is a tool for understanding model internals, or a finding about them.
- **4.1 Methods & tools.**
  - SAEs and their alternatives (parameter decomposition, neuron-basis circuits, block-sparse featurizers).
  - Circuits and lenses.
  - Activation oracles and natural-language explanations of activations.
  - Tests of whether these methods work.
- **4.2 Science of representations.** Findings about how models represent and compute things, such as the global workspace, emotion concepts, polysemanticity and representation geometry.
- **4.3 Steering & activation engineering.** Changing behaviour by intervening on activations (steering vectors, representation engineering, persona and refusal directions), and how reliable steering is, its side effects, and its use as an attack surface.
- **4.4 Developmental interpretability & singular learning theory.** How internal structure forms during training, studied with singular learning theory, susceptibilities and learning dynamics.

**5. Evaluations.** Measuring what models can and will do, and whether those measurements are trustworthy.
- **5.1 Dangerous-capability evals.** Cyber, bio, autonomy, self-replication, AI R&D automation and time horizons.
- **5.2 Scheming, sabotage & training gaming.** Evidence and evaluations of strategic misalignment:
  - scheming and sabotage propensity;
  - alignment faking;
  - sandbagging;
  - exploration and gradient hacking;
  - self-preservation and shutdown resistance;
  - other misbehaviour when given the chance.
- **5.3 Situational & evaluation awareness.** Whether models can tell they are being evaluated, trained or tampered with, and how that changes their behaviour and our measurements.
- **5.4 Eval science & validity.** Whether evals, benchmarks, red-team numbers and lab safety claims are trustworthy: construct validity, realism, elicitation, replication and statistics.

**6. Alignment auditing & honesty.** Finding out what a particular model hides, and getting true statements out of it.
- **6.1 Auditing methods & agents.** Techniques and agents for finding hidden objectives or misbehaviour in a model, eliciting hidden or sandbagged capabilities, and attacks on audits.
- **6.2 Model organisms & testbeds.** Models with known implanted behaviours, used to test audits, and whether those model organisms are realistic and robust.
- **6.3 Lie detection & deception probes.** Detecting when a model lies or deceives: white-box lie detectors and deception probes, black-box detectors, and secret-knowledge testbeds.
- **6.4 Introspection, confessions & self-report.** What models can accurately report about their own states and learned behaviours, and training them to report it: confessions, self-incrimination, introspection training.

### Part III. Deploying models safely: overseeing and securing systems in use

**7. Chain-of-thought monitorability.** Whether a model's written reasoning is a reliable signal of what it is doing, and what keeps or destroys that.
- **7.1 Latent reasoning & new architectures.** How much models can do without visible reasoning (no-CoT time horizons, opaque serial depth, filler tokens), and whether recurrent, diffusion and other latent-reasoning architectures erode CoT oversight.
- **7.2 CoT control, obfuscation & steganography.** Stress tests of whether models can control, hide or encode their reasoning.
- **7.3 How training affects monitorability.** Which training pressures keep or degrade CoT legibility, including accidental training against the CoT and language drift.
- **7.4 Measuring & improving faithfulness.** Whether the CoT reflects the computation behind the answer, and training for faithful or monitorable reasoning.

**8. Monitoring & control.** Deploying models that may be misaligned, with monitors and protocols that keep them safe even if they try to cause harm.
- **8.1 Control settings & protocols.** Control environments, protocols and safety cases that assume an adversarial model, including untrusted monitoring and multi-agent or distributed attacks.
- **8.2 Monitors.** Black-box, CoT and probe-based monitors for scheming, sabotage, deception and reward hacking, including production monitoring, and how well they work.
- **8.3 Red-teaming monitors & control protocols.** Attack policies, evasion benchmarks, and studies of models evading monitors.

**9. Security & misuse.** Defending models and agents against outside attackers: misusers, prompt injectors, poisoners and thieves.
- **9.1 Misuse safeguards & jailbreaks.** Classifiers, probes and refusal training against misuse, and attacks that get past them.
- **9.2 Agent security & prompt injection.**
  - Prompt injection.
  - Memory and skill-file poisoning.
  - Privilege escalation.
  - Instruction-hierarchy training.
  - System-level defences for agents.
- **9.3 Open-weight tamper resistance & unlearning.** Removing hazardous knowledge from open-weight models, and keeping their safeguards after fine-tuning.
- **9.4 Data poisoning & backdoors.** Planting behaviours through training data or weights (backdoors, sleeper agents, trojan neurons); results that hidden capabilities can be provably hard to detect; detecting and removing them.
- **9.5 Weight & infrastructure security.** Protecting model weights and the inference and agent infrastructure from theft or tampering.

### Part IV. Make AI solve it

**10. Make AI solve it.** Using AI to supervise AI and to do alignment research.
- **10.1 Scalable oversight: debate, weak-to-strong & interactive proofs.** Protocols that let weaker overseers give reliable signals for stronger models:
  - debate, both theory and experiments;
  - weak-to-strong and unreliable supervision;
  - rewinding;
  - complexity-theoretic oversight such as interactive proofs.
- **10.2 Automated alignment research.** Using AI agents to do safety research, how much uplift they give, and how to defer to them safely.

### Part V. Theory & safety by construction

**11. Theory & foundations.** Theoretical agendas aimed at understanding agents and safety from first principles.
- **11.1 Agent foundations & decision theory.** Formal models of agency, goals and decision-making:
  - decision theory, including how LLMs actually behave decision-theoretically;
  - embedded agency;
  - AIXI and algorithmic information theory;
  - Kosoy's learning-theoretic and computational-agent agenda;
  - open-source game theory.
- **11.2 Corrigibility theory.** What corrigibility and shutdownability are and whether they can be achieved: formal and conceptual work, and arguments about instrumental convergence.
- **11.3 Natural abstractions.** Whether minds converge on shared abstractions, and how to formalize them (natural latents, condensation).
- **11.4 Heuristic explanations & mechanistic estimation.** ARC's agenda of explaining and estimating model behaviour from the weights, without sampling.
- **11.5 Brain-like AGI safety.** Safety for AGI built from brain-like RL, including alignment through human-like social drives. The 2025 review put it under safety by construction, but it's conceptual work on a possible future design, not a design with guarantees.

- **11.6 Scientist AI & non-agentic AI.** Non-agentic predictors as a safer design (LawZero's Scientist AI), and how to verify them.

### Part VI. The wider picture: interacting agents, real-world evidence and strategy

**12. Multi-agent safety.** A single agenda, as in Draft 1. Failures that come from AI agents interacting (collusion, behaviours spreading between agents, collective misalignment, AI organisations), and cooperative AI and game theory for agents.

**13. Real-world evidence.** Evidence from deployments and from labs' own disclosures, rather than controlled experiments.
- **13.1 Incidents & case studies.** Real-world AI incidents and their investigation, such as the OpenAI–Hugging Face incident and rogue-agent activity found in the wild.
- **13.2 Effects on users & society.** Sycophancy, delusion, dependence, manipulation and disempowerment, in real use and in user studies.
- **13.3 Lab disclosures: system cards & risk reports.** System cards, alignment assessments and risk reports, and what they do or don't show.

**14. Threat models & strategy.** Arguments about how AI could go wrong and what the field should do about it.
- **14.1 Misalignment arguments & failure scenarios.** Arguments for and against egregious misalignment, superintelligence-alignment arguments, and scenarios for how risk plays out.
- **14.2 Research strategy, lab plans & deals with AIs.** Prioritizing between agendas, critiques of lab plans, and proposals for making deals with AIs.

---

## 4. Where each agenda comes from, and how big it is

Status:
- **ok:** the current pipeline should fill it.
- **thin:** it needs the hand-added sources in section 9.
- **new:** neither draft had it as an agenda.

The size columns are evidence, not predictions:
- **D1 n** comes from 499 older sources.
- **D2 n** comes from the current 625. A dash means that draft has no matching agenda.
- **Methods** is the cross-method median and how many of the six methods found it.

| # | Agenda | From | D1 n | D2 n | Methods | Status |
|---|---|---|---|---|---|---|
| 1.1 | Data filtering & alignment pretraining | D1 1.1 (part) | 15 (with attribution) | – | ~11–17 alone in 3/6 methods; 22 with constitutions | ok |
| 1.2 | Subliminal learning & data attribution | D1 1.4 + attribution from 1.1; D2 | 9 + part | 21 | 22 (5/6) | ok |
| 1.3 | Emergent misalignment | D1 1.2 (part), D2 renamed | 25 (with generalization) | 51 (about 20 belong elsewhere) | 42 (5/6) | ok |
| 1.4 | Inoculation prompting | D1 1.5 | 3 | 3–5 | own leaf in 2 methods (10, 5); with probe attribution in a third (8) | ok (small) |
| 1.5 | Generalization science | split from D1 1.2 | part | ~11 (in the EM leaf) | own leaf in method 1 (12); 4 in method 2 | new split; ok |
| 2.1 | Alignment training methods | split from D1 1.9 | part of 11 | – | – | new split; thin |
| 2.2 | Reward hacking & specification gaming | D1 1.6, D2 | 19 (with reward-seeking) | 61 (with reward-seeking) | 34 (6/6) | ok |
| 2.3 | Reward-seeking & fitness-seeking | D1 11.1 (moved) | 9 | in 2.2 | 16 (5/6) | ok |
| 2.4 | Internals & monitors as training signals | D1 1.8 | 5 | – | 10 (4/6) | ok |
| 3.1 | Persona science | D1 1.3 | 13 | in 36 | 17 (5/6) | ok |
| 3.2 | Model specs, constitutions & character training | split from D1 1.9 | part of 11 | in 36 | 7–10 alone in 3/6 methods | ok with adds |
| 3.3 | Whose values: pluralistic & social-choice alignment | new (2025 "multi-agent first") | – | – | – | new; thin (0 in pipeline, about a dozen arXiv papers in pool) |
| 3.4 | Model welfare & moral status | D1 12 | 2 | in 36 | 6 (5/6) | thin |
| 4.1 | Interpretability methods & tools | D1 6.1 | 25 (with steering) | 53 (whole area) | 28 (6/6, whole area) | ok |
| 4.2 | Science of representations | D1 6.2 | 12 | – | – | ok |
| 4.3 | Steering & activation engineering | split from D1 6.1 | part | – | – | new split; thin (~60 arXiv titles in pool, 9 pipeline mentions) |
| 4.4 | Developmental interpretability & SLT | D1 6.3 | 7 | – | 6 (3/6) | thin |
| 5.1 | Dangerous-capability evals | D1 3.1 | 15 | in misuse | 14 (6/6) | ok |
| 5.2 | Scheming, sabotage & training gaming | D1 3.2 + 1.7, D2 | 26 + 3 | 30 | 32 (5/6), plus 14 for unsafe deployed agents (3/6) | ok |
| 5.3 | Situational & evaluation awareness | D1 3.4, D2 | 16 | 31 (with validity) | 27 (5/6) | ok |
| 5.4 | Eval science & validity | D1 3.6 | 20 | in 31 | in 27 | ok |
| 6.1 | Auditing methods & agents | D1 3.7, D2 | 13 | 50 (with organisms and incidents) | 28 (5/6, with organisms) | ok |
| 6.2 | Model organisms & testbeds | D1 3.8 | 11 | in 50 | in 28 | ok |
| 6.3 | Lie detection & deception probes | D2 (part) | – | 36 (with self-report) | 18 (5/6) | new to D1 |
| 6.4 | Introspection, confessions & self-report | D1 3.4, D2 | 6 | in 36 | 21 (5/6; verbalizers go to 4.1) | ok |
| 7.1 | Latent reasoning & new architectures | D1 2.1 | 18 | 58 (whole area) | 60 (6/6, whole area) | ok with adds |
| 7.2 | CoT control, obfuscation & steganography | D1 2.2 | 10 | in 58 | in 60 | ok |
| 7.3 | How training affects monitorability | D1 2.3 | 10 | in 58 | in 60 | ok |
| 7.4 | Measuring & improving faithfulness | D1 2.4 | 11 | in 58 | in 60 | ok |
| 8.1 | Control settings & protocols | D1 4.1 | 19 | 66 (whole area) | 66 (6/6, whole area) | ok |
| 8.2 | Monitors | D1 4.2 | 14 | in 66 | in 66 | ok |
| 8.3 | Red-teaming monitors & control protocols | D1 4.3 | 14 | in 66 | in 66 | ok |
| 9.1 | Misuse safeguards & jailbreaks | D1 5.1 | 15 | 66 (whole area) | 13 (5/6) | ok |
| 9.2 | Agent security & prompt injection | D1 5.2 | 13 | in 66 | 17 (5/6) | ok |
| 9.3 | Open-weight tamper resistance & unlearning | D1 5.3 | 5 | in 66 | 13 (5/6) | ok |
| 9.4 | Data poisoning & backdoors | new (2025 "data poisoning defense") | – | – | – | new; ~15 pipeline entries mention poisoning or backdoors |
| 9.5 | Weight & infrastructure security | D1 5.4 | 3 | – | – | small |
| 10.1 | Scalable oversight: debate, weak-to-strong & interactive proofs | D1 9 (part), D2 | 11 (with 10.2) | 14 | 13 (5/6) | ok with adds |
| 10.2 | Automated alignment research | split from D1 9 | part | – | – | new split; thin (about 5 in pipeline) |
| 11.1 | Agent foundations & decision theory | D1 10.1 | 4 | – | – | thin (16 LW posts and 6 papers to add) |
| 11.2 | Corrigibility theory | split from D1 10.1 | part | – | – | new split; thin |
| 11.3 | Natural abstractions | new (2025 "ontology identification") | – | – | – | new; thin (0 in pipeline) |
| 11.4 | Heuristic explanations & mechanistic estimation | D1 10.2 | 7 | in interp | – | ok (small) |
| 11.5 | Brain-like AGI safety | new (2025 agenda, under safety by construction) | – | – | – | new; thin (1 in pipeline) |
| 11.6 | Scientist AI & non-agentic AI | new (your note: Bengio) | – | – | – | new; thin (1 in pipeline) |

| 12 | Multi-agent safety | D1 8, D2 | 10 | 17 | 18 (5/6) | ok |
| 13.1 | Incidents & case studies | D1 7.1 | 16 | in auditing | 21 (6/6) | ok |
| 13.2 | Effects on users & society | D1 7.2 | 5 | in character | 11 (5/6) | ok |
| 13.3 | Lab disclosures: system cards & risk reports | D1 7.3 | 5 | in strategy | 17 (5/6) | ok |
| 14.1 | Misalignment arguments & failure scenarios | D1 11.2 | 22 | 35 (whole area) | 30 (6/6, whole area) | ok with adds |
| 14.2 | Research strategy, lab plans & deals with AIs | D1 11.3 | 13 | in 35 | in 30 | ok |

With `--top 10`, the draft holds at most 530 entries. Without the section 9 additions, the thin agendas hold well under 10 each, so expect roughly 420. The 2025 review linked about 820 outputs.

---

## 5. Your notes, point by point

| Your note | Decision |
|---|---|
| *RL Towards Broadly and Persistently Beneficial Models* seems misfiled under emergent misalignment | **2.1 Alignment training methods.** Draft 2's agenda was "Emergent misalignment *and training generalization*", and this paper tests whether trained traits generalize, so the classifier matched it. Its contribution is a method for training a target property, which is what 2.1 is for (placement rule 9). |
| Maybe just rename the agenda to "EM" | **Done:** 1.3 is "Emergent misalignment" only. The general generalization work goes to the new **1.5 Generalization science**, and inoculation to 1.4. About 20 of Draft 2's 51 entries in that leaf move out (to 1.4, 1.5, 3.1 and 2.1). |
| Surprised *Overtrained, Not Misaligned* isn't in the draft | It's in the pipeline, but its importance score is 0.50, 35th of 51 in that leaf. The scorer called it a careful replication but marked it down for small N, a single LLM judge, a simple mitigation and little attention so far. Even in the narrower 1.3, about 14 distinct works score above 0.50, so a top-10 cut by score would still drop it. To include it, add an `include` decision with `import_feedback.py`. |
| Unsure whether *Chunky Post-Training* belongs, and whether subliminal learning should be its own agenda | **Chunky Post-Training → 1.2**: its contribution is tools (SURF, TURF) that surface generalization failures and trace them to post-training data. **Subliminal learning is paired with data attribution in 1.2.** That's a judgement call. Three methods make subliminal learning its own leaf (10–12 items each), while two pair it with attribution, as Draft 2 did. Together they come to about 20, a good size. Split them if hand-added sources push the pair past about 30. |
| Data filtering should be a separate agenda | **1.1 Data filtering & alignment pretraining.** The methods support it: three of six give alignment pretraining and midtraining its own leaf (11–17 items), separate from constitutions. Constitution and spec midtraining go to 3.2 (rule 8). |
| Constitutions could be their own agenda, or go under persona science; maybe "Model personas and constitutions" | **3.2 Model specs, constitutions & character training**, as a sibling of 3.1 Persona science in area 3. Area 3 is in effect your "personas and constitutions" idea, with each half its own agenda. Constitutions are separate from personas in three of six methods, and the 2025 review had them separate. |
| Scalable oversight and debate could go in a "Make AI solve it" agenda | **Area 10 "Make AI solve it"**, with 10.1 Scalable oversight and 10.2 Automated alignment research. This brings back the 2025 area name. |
| "Inspection" is basically evals | Part II has **5 Evaluations** (capabilities, scheming, awareness, validity) and **6 Alignment auditing & honesty** (auditing, model organisms, lie detection, introspection), plus 4 Interpretability. The name "Inspection" is gone. |
| Missing: singular learning theory | **4.4 Developmental interpretability & singular learning theory.** It's named explicitly, and placement rule 20 sends SLT work here rather than to Theory. Timaeus's patterning and spectroscopy papers are already in the pipeline; section 9 adds *Interpreting Reinforcement Learning Agents with Susceptibilities* (Elliott, Urdshals, Quarel, Murfet). |
| Missing: Bengio's work | **11.6 Scientist AI & non-agentic AI.** *Safety from Honesty in a Disinterested AI Predictor* is in the pipeline; section 9 adds *How to Verify Probabilistic Consistency of Predictive Models* (Paradise, Richardson, Bengio). |
| Missing: much of the agent foundations work on LessWrong | **Area 11 with four agendas**, and 30 LessWrong posts and 8 arXiv papers to add (section 9). For example: Resolution's new agent foundations team, Ngo ×2, Kosoy ×3, jessicata on FDT, Hebbar, Rosas ×2, the natural-latent posts, the Corrigibility Research Fund, and the decision-theory-in-LLMs studies. The LessWrong shortlist cut them: it kept 160 of the 1,338 posts rated highly relevant. |
| Add sections for new orgs and agendas, and a graveyard | **Section 10.** It covers Labs, New in 2026, Orgs without public outputs, the Graveyard and a watch list, each with initial candidates from the data. |

---

## 6. Coverage check against the 2025 review

Every 2025 agenda, and where it goes. "Graveyard?" means there's almost no 2026 activity in the scraped data; check each by hand.

| 2025 area | 2025 agendas → combined agenda |
|---|---|
| Black-box safety: iterative alignment | Pretrain-time → 1.1. Post-train-time → 2.1. Black-box make-AI-solve-it → 10.2. Inoculation prompting → 1.4. Inference-time in-context learning → 1.5 (about 1 item). Inference-time steering → 4.3. Unlearning → 9.3. Control → 8. Safeguards → 9.1 / 8.2. CoT monitoring → 7. |
| Model psychology | Model values and preferences → 3.1. Character training and persona steering → 3.1 / 3.2. Emergent misalignment → 1.3. Model specs and constitutions → 3.2. Model psychopathology → 3.4. |
| Better data | Data filtering, hyperstition, synthetic data, data quality → 1.1. Data poisoning defence → 9.4. |
| Goal robustness | RL safety → 2.2 and 1.5 (about 5 classic-RL papers). Harm reduction for open weights → 9.3. **Mild optimisation → graveyard?** (3 incidental items in the pool). **Assistance games → graveyard?** (one arXiv paper extends CIRL and goes in 11.1; 3 passing LessWrong mentions). **"Neglected approaches" (AE Studio) → graveyard?** (2 low-karma self-other-overlap posts). |
| White-box safety | Reverse engineering, sparse coding, other interpretability → 4.1 / 4.2. Representation geometry → 4.2. Learning dynamics and developmental interpretability → 4.4. Model diffing → 4.1 (about 14 in the pool, 1 in the pipeline). Causal abstractions → 4.1 (3 arXiv papers). Data attribution → 1.2. Pragmatic interpretability → 4.1 / 8.2. Extracting latent knowledge → 6.3 / 6.4. Lie and deception detectors → 6.3. Monitoring concepts → 8.2. Activation engineering → 4.3. **Human inductive biases → graveyard?** (about 3 arXiv papers; otherwise 4.2). |
| Safety by construction | Guaranteed-safe AI → graveyard (formal methods dropped after draft 3). Scientist AI → 11.6. Brain-like AGI safety → 11.5 (moved to theory). |
| Make AI solve it | Weak-to-strong, debate → 10.1. Supervising AIs improving AIs → 10.2. AI explanations of AIs → 4.1. LLM introspection training → 6.4. |
| Theory | Agent foundations, learning-theoretic agenda → 11.1. Asymptotic guarantees and heuristic explanations → 11.4. Corrigibility (behaviour alignment theory, other) → 11.2. Natural abstractions → 11.3. **Tiling agents → graveyard?** (one 18-karma LessWrong post). **High-actuation spaces → graveyard?** (none found). |
| Multi-agent first | Aligning to context, aligning to the social contract, aligned to who?, aligning what? → 3.3. Theory and tools for aligning multiple AIs → 13. |
| Evals | AGI metrics, capability, autonomy, WMD and self-replication evals → 5.1. Situational awareness → 5.3. Steganography → 7.2. Deception → 5.2 / 6.3. Scheming, sandbagging → 5.2. Various red-teams → 9.1 / 8.3. Other evals → 5. |
| Labs | Front matter (section 10). |

Agendas that are new in 2026, or grew enough to need their own place: 7.1, 2.3, 2.4, 13.1, 3.4 and 10.2. Section 10 discusses them.

---

## 7. Mapping from Draft 1 and Draft 2

**Draft 1 → combined**

| Draft 1 | Combined |
|---|---|
| 1.1 Training data & data attribution | 1.1 (data filtering, alignment pretraining); attribution → 1.2; spec midtraining → 3.2 |
| 1.2 Emergent misalignment & generalization science | 1.3 + 1.5 |
| 1.3 Persona science | 3.1 |
| 1.4 Subliminal learning & hidden-signal transfer | 1.2 |
| 1.5 Inoculation prompting | 1.4 |
| 1.6 Reward hacking & reward seeking in training | 2.2 + 2.3 |
| 1.7 Models resisting training | merged into 5.2 |
| 1.8 Internals & monitors as training signals | 2.4 |
| 1.9 Alignment targets & training methods | methods → 2.1; specs and constitutions → 3.2; whose values → 3.3; corrigibility as a concept → 11.2 |
| 2.1–2.4 CoT agendas | 7.1–7.4 (7.1 renamed to name the new architectures) |
| 3.1 Capability evals | 5.1 |
| 3.2 Propensity evals | 5.2 (reward-hacking benchmarks → 2.2) |
| 3.3 Model characterization | 3.1 (agenda dropped after draft 3) |
| 3.4 Situational & evaluation awareness | 5.3 |
| 3.4 Introspection & self-report | 6.4 |
| 3.6 Eval science & validity | 5.4 |
| 3.7 Alignment auditing: methods | 6.1 |
| 3.8 Alignment auditing: testbeds & model organisms | 6.2 |
| (none) | 6.3 Lie detection & deception probes (new) |
| 4.1–4.3 Monitoring & control | 8.1–8.3 |
| 5.1–5.4 Security & misuse | 9.1, 9.2, 9.3, 9.5; plus new 9.4 Data poisoning & backdoors |
| 6.1 Interpretability methods & tools | 4.1; steering → 4.3 |
| 6.2 Science of representations | 4.2 |
| 6.3 Learning dynamics & devinterp | 4.4 (singular learning theory named) |
| 7.1–7.3 Real-world evidence | 13.1–13.3 |
| 8 Multi-agent safety | 13 |
| 9 Scalable oversight & automated alignment | 10.1 + 10.2 |
| 10.1 Agent foundations | 11.1 + 11.2; plus new 11.3 Natural abstractions |
| 10.2 Heuristic explanations | 11.4 |
| 10.3 Formal methods & GSAI | dropped after draft 3 (graveyard); plus new 11.6 Scientist AI; brain-like AGI goes to 11.5 |
| 11.1 Reward-seeking threat models | 2.3 (moved next to reward hacking; now includes measurement) |
| 11.2 Misalignment arguments | 14.1 |
| 11.3 Research strategy & deals | 14.2 |
| 12 Model welfare | 3.4 |

**Draft 2 → combined**

| Draft 2 | Combined |
|---|---|
| Reward hacking and reward-seeking | 2.2 + 2.3 |
| Emergent misalignment and training generalization | 1.3 + 1.4 + 1.5; persona items → 3.1; method papers → 2.1 |
| Training-data effects | 1.2 (poisoning-attack papers → 9.4) |
| Model character and values | 3.1, 3.2, 3.4; alignment pretraining → 1.1; sycophancy and user effects → 13.2 |
| Scalable oversight and debate | 10.1 |
| Scheming and training gaming | 5.2 |
| Evaluation awareness and eval validity | 5.3 + 5.4 |
| Honesty, lie detection and self-report | 6.3 + 6.4; activation verbalizers → 4.1 |
| Alignment auditing, model organisms and incidents | 6.1 + 6.2; incidents → 13.1 |
| Interpretability foundations | 4.1–4.4; mechanistic estimation → 11.4 |
| Chain-of-thought monitorability | 7.1–7.4 |
| AI control and agent monitoring | 8.1–8.3; automated-research platforms → 10.2 |
| Misuse, adversarial robustness and dangerous capabilities | 9.1–9.5; dangerous-capability evals → 5.1 |
| Multi-agent risks | 13 |
| Strategy, threat models and frontier risk reporting | 14.1 + 14.2; system cards → 13.3 |

---

## 8. Placement rules

These are the hard cases. The classifier sees only names, descriptions and examples, so put the important rules into the agenda descriptions when loading the YAML.

1. **General rule.** Classify by the question the work answers, not the technique it uses. Interpretability work about a specific safety phenomenon goes with that phenomenon unless its main contribution is the method.
2. **Probes.**
   - As deception detectors → 6.3.
   - As deployment monitors → 8.2.
   - As misuse classifiers → 9.1.
   - As training rewards or penalties → 2.4.
   - New probe architectures in general → 4.1.
3. **Scheming.** Whether models scheme → 5.2. A tool or benchmark for finding hidden behaviours → 6.1. A lab's overall assessment → 13.3.
4. **Emergent misalignment.** Broad misalignment from narrow training → 1.3, even when it comes from reward hacking or the mechanism is a persona. The hack itself → 2.2. Which persona a model adopts → 3.1.
5. **Generalization that isn't about misalignment** → 1.5, including goal misgeneralization in RL agents.
6. **Inoculation.** Inoculation and its variants (adapters, stratified inoculation, comparisons with preventative steering) → 1.4.
7. **Data.**
   - Filtering or generating pretraining and midtraining data → 1.1.
   - Tracing behaviour back to data (including SURF and TURF) → 1.2.
   - Deliberate poisoning attacks and defences → 9.4.
   - The science of how poisoned data acts (e.g. diluting poisoned data can strengthen it) → 1.2.
8. **Specs and constitutions.** Constitution or spec midtraining → 3.2, not 1.1. Corrigibility as a written target → 3.2; as a theoretical question → 11.2.
9. **New training methods.** A new method that trains a property and tests how it generalizes → 2.1, e.g. *RL Towards Broadly and Persistently Beneficial Models*.
10. **Introspection.** Introspection, confessions and self-report training → 6.4. Activation verbalizers, natural-language autoencoders and activation oracles as tools → 4.1.
11. **Steering.**
    - Research on steering itself → 4.3.
    - Steering used to suppress evaluation awareness → 5.3.
    - Preventative steering during training → 1.4 or 2.4.
12. **Training against internals.** Training against probes or internal detectors → 2.4. CoT-specific training pressure → 7.3.
13. **Outside attackers.** Prompt injection and instruction-hierarchy training → 9.2. Jailbreaks → 9.1.
14. **Sabotage of automated safety research.** Settings and monitors → 8. Propensity results → 5.2. Agents and platforms that do research → 10.2.
15. **AI R&D automation benchmarks** → 5.1.
16. **Reward-seeking.** Reward- and fitness-seeker threat models and measurements → 2.3.
17. **Sycophancy.** Sycophancy and manipulation as effects on users → 13.2. How training produces sycophancy → the matching Part I agenda.
18. **Real-world incidents.** Investigations of real incidents → 13.1, including evals built to investigate one.
19. **Unsafe deployed agents.**
    - Shutdown resistance → 5.2.
    - Incident write-ups → 13.1.
    - Agent security failures → 9.2.
20. **Theory placements.**
    - Mechanistic estimation (ARC) → 11.4.
    - Singular learning theory and susceptibilities → 4.4.
    - Decision theory, including measurements of LLMs' decision-theoretic behaviour → 11.1.
21. **Formal guarantees.** There is no formal-methods agenda any more: a proof about a system goes to the agenda of the question it answers (e.g. limits of evaluation → 5.4). A formal model of agents in general → 11.1.
22. **Multi-agent.** Multi-agent control (distributed attacks, monitor–policy collusion) → 8.1. Collusion and contagion among agents in general → 13.
23. **Latent reasoning.** Recurrent, diffusion and other latent-reasoning architectures → 7.1. For example, *How Transparent is DiffusionGemma?* is currently filed under CoT monitorability as a whole.
24. **Deals and welfare.** Deals with AIs → 14.2. Welfare and functional emotions → 3.4, but emotion representations as an interpretability finding → 4.2.

---

## 9. Sources to add by hand

These are from the filtered arXiv and LessWrong data and aren't in the pipeline unless marked *(in)*. They'd add about 105 entries. Classifying and scoring them would cost about $6–7.

**11.1 Agent foundations & decision theory**
- [Resolution has a new Agent Foundations team](https://lesswrong.com/posts/qTNm8qzqhhpno58fZ/resolution-has-a-new-agent-foundations-team) (Gillen, 254)
- [On Goal-Models](https://lesswrong.com/posts/MEkafPJfiSFbwCjET/on-goal-models) (Ngo, 136 karma)
- [Agents as Webs of Beliefs](https://lesswrong.com/posts/M39Z2CvyfaxZdaxR4/agents-as-webs-of-beliefs) (Ngo, 93)
- [A cat-belling problem for FDT](https://lesswrong.com/posts/drteSvhc4fX3Tu9y7/a-cat-belling-problem-for-fdt) (jessicata, 116)
- [Operationalizing FDT](https://lesswrong.com/posts/RyDkpWGLQsCnABE78/operationalizing-fdt) (Hebbar, 99)
- [Stringological sequence prediction I](https://lesswrong.com/posts/EEvHYKLsq92LmQ78a/paper-stringological-sequence-prediction-i-1) (Kosoy, 91)
- [Preface to the Computational Agent Theory and ASI Alignment Sequence](https://lesswrong.com/posts/NQLCdfeNsQHZaJ8iC/preface-to-the-computational-agent-theory-and-asi-alignment) (Kosoy, 86)
- [Desiderata for the Theory of Agents](https://lesswrong.com/posts/sqjti8dxcKSvZJikd/desiderata-for-the-theory-of-agents) (Kosoy, 65)
- [The AIXI perspective on AI Safety](https://lesswrong.com/posts/baP2osKGc4KmDoTET/the-aixi-perspective-on-ai-safety) (Wyeth, 88)
- [The separation principle: where do beliefs and desires come from?](https://lesswrong.com/posts/awMDNhoL6J97s6wFJ/the-separation-principle-where-do-beliefs-and-desires-come) (Rosas, 122)
- [Utilities as Legendre duals of probabilities](https://lesswrong.com/posts/ALmBydH53DE3dSzCh/utilities-as-legendre-duals-of-probabilities) (Rosas, 72)
- [Payorian cooperation is easy with Kripke frames](https://lesswrong.com/posts/LaCP6WyNzX8kiZn3w/payorian-cooperation-is-easy-with-kripke-frames) (73)
- [Against strong decision-theoretic realism](https://lesswrong.com/posts/5ro9kSxhP8mHXGmn4/against-strong-decision-theoretic-realism-1) (Cooper, 57)
- [On The Independence Axiom](https://lesswrong.com/posts/MsjWPWjAerDtiQ3Do/on-the-independence-axiom) (Kendiukhov, 338; the filter rated it "not relevant")
- Decision theory in LLMs:
  - [Frontier models state different decision theory preferences depending on who's asking](https://lesswrong.com/posts/MzenSrmZ3pT2pCnvp/frontier-models-state-different-decision-theory-preferences-2) (261)
  - [Kimi likes causal decision theory more after RL in twin prisoner's dilemmas](https://lesswrong.com/posts/hfNBEKaStASAYMLiu/kimi-likes-causal-decision-theory-more-after-rl-in-twin-1) (122)
- arXiv:
  - [Consequentialist Objectives and Catastrophe](https://arxiv.org/abs/2603.15017)
  - [A Definition of Catastrophic Performance](https://arxiv.org/abs/2611.06219)
  - [Fragility of Value under Imperfect Alignment](https://arxiv.org/abs/2607.28881)
  - [Goal Revelation as a Bridge Between Information-Theoretic Empowerment and Capability-Based Human Power](https://arxiv.org/abs/2611.07247)
  - [A mathematical theory of evolution for self-designing AIs](https://arxiv.org/abs/2604.05142)
  - [A Contextual-Bandit Oversight Game with Two-Sided Informational Asymmetry](https://arxiv.org/abs/2607.00155) (from the assistance-games line)

**11.2 Corrigibility theory**
- Corrigibility Research Fund posts:
  - [Announcing the Corrigibility Research Fund](https://lesswrong.com/posts/FBqe5dt8ZjaHN4Xj9/announcing-the-corrigibility-research-fund) (Harms, 114)
  - [Corrigibility Prizes for Existing Work](https://lesswrong.com/posts/3uJqhrC2idf4eNj5h/corrigibility-prizes-for-existing-work) (105)
  - [Round 1 grantees](https://lesswrong.com/posts/CKArJ4GAQGFjnhjx6/corrigibility-research-fund-grantees-round-1)
  - [Five Types of "Corrigibility Projects" I Don't Want to Fund](https://lesswrong.com/posts/9ixerpx4DCQTaRYCz/five-types-of-corrigibility-projects-i-don-t-want-to-fund) (147)
- [Against Corrigibility](https://lesswrong.com/posts/rQTzSuBDLoAbhyS6g/against-corrigibility-1) (73)
- ["Act-based approval-directed agents", for IDA skeptics](https://lesswrong.com/posts/RKtTi82t8X8TQy5FX/act-based-approval-directed-agents-for-ida-skeptics) (Byrnes, 72)
- [No instrumental convergence without AI psychology](https://lesswrong.com/posts/gCdNKX8Y4YmqQyxrX/no-instrumental-convergence-without-ai-psychology-1) (TurnTrout, 68)
- arXiv: [Revisiting the shutdown problem](https://arxiv.org/abs/2606.08296) (Thorstad), [Formal Analysis of AGI Decision-Theoretic Models and the Confrontation Question](https://arxiv.org/abs/2601.04234)
- *(in)* [Empowerment, corrigibility, etc. are simple abstractions](https://lesswrong.com/posts/vzHtHHBJoKATi5SeK/empowerment-corrigibility-etc-are-simple-abstractions-of-a) (195)

**11.3 Natural abstractions**
- [Redux: (∃ Stochastic Natural Latent) Implies (∃ Deterministic Natural Latent)](https://lesswrong.com/posts/TgboJpeN95bs84odk/redux-stochastic-natural-latent-implies-deterministic) (Lorell, 104)
- [Convergent Abstraction Hypothesis](https://lesswrong.com/posts/fYF8v2ukZmsNvmkkX/convergent-abstraction-hypothesis) (Kulveit, 125)
- [A summary of Condensation and its relation to Natural Latents](https://lesswrong.com/posts/agw7HhW4cWjADpBgo/a-summary-of-condensation-and-its-relation-to-natural) (88)
- [Research directions in condensation: varieties of objectivity](https://lesswrong.com/posts/89GJeixwhFHLWxNbX/research-directions-in-condensation-varieties-of-objectivity) (Eisenstat, 58)
- [Small Steps Towards Proving Stochastic → Deterministic Natural Latent](https://lesswrong.com/posts/4q3kMfJHB4rxr3Z8m/small-steps-towards-proving-stochastic-deterministic-natural) (58)
- [A Visual Guide to Natural Latents](https://lesswrong.com/posts/oeaYxA85tBvtJB2a5/a-visual-guide-to-natural-latents) (57)

**11.4 Heuristic explanations**
- [Announcing the ARC White-Box Estimation Challenge](https://lesswrong.com/posts/Kben8CzS4awCwNw5c/announcing-the-arc-white-box-estimation-challenge) (168)

**11.5 Brain-like AGI safety** (all Byrnes)
- [New version of "Intro to Brain-Like-AGI Safety"](https://lesswrong.com/posts/rreDwHXgnhEDKxkro/new-version-of-intro-to-brain-like-agi-safety) (63)
- [Notes on technical alignment via human-like social drives](https://lesswrong.com/posts/rKdS7i4StaMmFzYRo/notes-on-technical-alignment-via-human-like-social-drives) (74)
- [In (highly contingent!) defense of interpretability-in-the-loop ML training](https://lesswrong.com/posts/ArXAyzHkidxwoeZsL/in-highly-contingent-defense-of-interpretability-in-the-loop) (87)
- *(in)* [RL & search is a terrifying way to build AGI](https://lesswrong.com/posts/KHyBocZncAmtu4Jbc/rl-and-search-is-a-terrifying-way-to-build-agi-an-faq) (151)

**Formal methods, guarantees & impossibility results** (agenda dropped after draft 3; these were added and then reclassified)
- [Fundamental Impossibility Results in AI Safety](https://arxiv.org/abs/2610.27373)
- [What Can Be Enforced? A Theory of Certified Runtime Safety for Tool-Using Agents](https://arxiv.org/abs/2607.22868)
- [Formal Mechanistic Interpretability: Automated Circuit Discovery with Provable Guarantees](https://arxiv.org/abs/2602.16823)
- [Certified Circuits](https://arxiv.org/abs/2602.22968)
- [Interactions Between Crosscoder Features: A Compact Proofs Perspective](https://arxiv.org/abs/2606.09940)
- [A critical look at Lean4](https://lesswrong.com/posts/zHhGa3iQBQcdSifFL/a-critical-look-at-lean4-1) (Moses, 414; on how far to trust formal certificates)
- *(in)* [Hair-Trigger Alignment](https://arxiv.org/abs/2601.22313)
- *(in)* [AI Models Can Provably Hide Arbitrary Capabilities](https://arxiv.org/abs/2610.13928) (better in 9.4)

**11.6 Scientist AI**
- [How to Verify Probabilistic Consistency of Predictive Models](https://arxiv.org/abs/2608.11181) (Paradise, Richardson, Bengio)
- [Some Thoughts on Bengio's Scientist AI](https://lesswrong.com/posts/382m7ATXELt5eBgr3/some-thoughts-on-bengio-s-scientist-ai) (23)
- *(in)* [Safety from Honesty in a Disinterested AI Predictor](https://arxiv.org/abs/2606.29657)


**10.1 Scalable oversight (complexity-theoretic work)**
- [Debate is efficient with your time](https://arxiv.org/abs/2602.08630) (Brown-Cohen, Irving)
- [How to Avoid Debate: Scalable AI Safety via Doubly-Efficient Interactive Proofs](https://arxiv.org/abs/2607.03561)
- [Can AI Oversight Be Zero Knowledge?](https://arxiv.org/abs/2610.01995)
- [Knowledge Divergence and the Value of Debate for Scalable Oversight](https://arxiv.org/abs/2603.05293)
- [Calibrating Conservatism for Scalable Oversight](https://arxiv.org/abs/2605.28807)

**10.2 Automated alignment research**
- [Where is all the AI safety research uplift?](https://lesswrong.com/posts/wPrpnfaNL5JP9i6KT/where-is-all-the-ai-safety-research-uplift) (Buck, 144)
- [theory uplift differentially benefits safety & is underleveraged](https://lesswrong.com/posts/KWeAYcDJwfrG7RwBN/theory-uplift-differentially-benefits-safety-and-is) (137)
- [Differential acceleration of alignment-relevant capabilities is a bad bet](https://lesswrong.com/posts/FzGqnCkdKeTnZ9tjE/differential-acceleration-of-alignment-relevant-capabilities) (119)
- [Letting Claude do Autonomous Research to Improve SAEs](https://lesswrong.com/posts/rbqJoxFZtae9x93mx/letting-claude-do-autonomous-research-to-improve-saes) (102)
- *(in)* [How do we (more) safely defer to AIs?](https://lesswrong.com/posts/vjAM7F8vMZS7oRrrh/how-do-we-more-safely-defer-to-ais)
- *(in)* [Automated Alignment is Harder Than You Think](https://lesswrong.com/posts/gpuYFbMNH8PJXpmny/automated-alignment-is-harder-than-you-think-1)

**7.1 Latent reasoning & new architectures**
- [How concerned should we be about Astra's recurrent architecture?](https://lesswrong.com/posts/PLisnSFir8y5AHkmP/how-concerned-should-we-be-about-astra-s-recurrent) (173)
- [Latent reasoning architectures would likely undermine CoT, our strongest oversight tool](https://lesswrong.com/posts/6m29SfjbittooYojj/latent-reasoning-architectures-would-likely-undermine-cot) (102)
- [Astra's no-CoT limits track speculative depth, not step count](https://lesswrong.com/posts/WFc3NkuPaYFrYuaZd/astra-s-no-cot-limits-track-speculative-depth-not-step-count) (110)
- [Astra appears to perform belief-propagation-like inference without CoT](https://lesswrong.com/posts/PAHqDoFrp9fybcSn2/astra-appears-to-perform-belief-propagation-like-inference) (103)
- [Even "illegible" Mythos reasoning traces seem pretty legible](https://lesswrong.com/posts/wCSEpT3dTGz4N86Wi/even-illegible-mythos-reasoning-traces-seem-pretty-legible) (186)

**4.3 Steering & activation engineering**

There are about 60 filtered arXiv papers on steering; these are representative.
- [Analysing the Safety Pitfalls of Steering Vectors](https://arxiv.org/abs/2603.24543)
- [Steering Externalities: Benign Activation Steering Unintentionally Increases Jailbreak Risk](https://arxiv.org/abs/2602.04896)
- [On the Non-Identifiability of Steering Vectors](https://arxiv.org/abs/2602.06801)
- [Endogenous Resistance to Activation Steering](https://arxiv.org/abs/2602.06941)
- [Does Fine-Tuning Undo Activation Steering?](https://arxiv.org/abs/2608.24988)
- [Forecasting Side Effects of Activation Steering](https://arxiv.org/abs/2608.11227)
- [Activation Steering Induces Emergent Misalignment](https://arxiv.org/abs/2606.08682)
- [Steering Vectors are an Adversarial Attack Surface](https://arxiv.org/abs/2606.05958)
- [When Do Model Internals Help? Exploring the Role of Representation Engineering in LLM Safety](https://arxiv.org/abs/2609.34771)
- LessWrong:
  - [Steering Might Stop Working Soon](https://lesswrong.com/posts/fuzfbz8TbuLcskGCx/steering-might-stop-working-soon) (68)
  - [Preventative Steering has advantages over Inoculation Prompting](https://lesswrong.com/posts/R43jFiHaaaK3eMQJ6/preventative-steering-has-advantages-over-inoculation-2) (30; goes to 1.4)

**4.4 Developmental interpretability & SLT**
- [Interpreting Reinforcement Learning Agents with Susceptibilities](https://arxiv.org/abs/2605.08007) (Elliott, Urdshals, Quarel, Murfet)

**3.3 Whose values**
- [AI Alignment From Social Choice Perspectives](https://arxiv.org/abs/2606.21550)
- [Algorithmic Impact Reveals the Hidden Social Choice Structure of Alignment](https://arxiv.org/abs/2608.24046)
- [Enforcing Axioms for AI Alignment under Loss-Based Rules](https://arxiv.org/abs/2611.13369)
- [From Sycophantic Consensus to Pluralistic Repair](https://arxiv.org/abs/2605.14912)
- [Mitigating Social Sycophancy via Pluralistic Preference Optimization](https://arxiv.org/abs/2610.02568)

**3.2 Specs, constitutions & character training**
- [Character Training Induces Motivation Clarification](https://lesswrong.com/posts/v22JCsRBq9J9fqPJL/character-training-induces-motivation-clarification-a-clue) (82)
- [Open Problems With Claude's Constitution](https://lesswrong.com/posts/vFAJxua3Qc6S8MbqG/open-problems-with-claude-s-constitution) (Zvi, 75)
- [A List of Research Directions in Character Training](https://lesswrong.com/posts/6EwuCH3vZ7qvPt82k/a-list-of-research-directions-in-character-training) (49)
- arXiv:
  - [From Constitutions to Control](https://arxiv.org/abs/2609.33086)
  - [Constitutional adapters](https://arxiv.org/abs/2609.36657)
  - [SIGMA: Self-Improving Alignment Generalization from a Model Spec](https://arxiv.org/abs/2610.07935)
  - [Character Training for Risk-Averse Agents](https://arxiv.org/abs/2609.38093)
- *(in)* [Character training can mitigate reward hacking, but can also make it harder to detect](https://lesswrong.com/posts/2maYXkEgnfJHPAkxh/character-training-can-mitigate-reward-hacking-but-can-also) (146)

**3.4 Model welfare**
- [Machinic Psychopharmacology: Do LLMs Self-Medicate?](https://lesswrong.com/posts/cNDJuXNZ8MrkPZNzj/machinic-psychopharmacology-do-llms-self-medicate-3) (UK AISI, 139; models given steering vectors as tools to change their own states)
- [Claude Opus 5: Model Welfare](https://lesswrong.com/posts/bBXBpsyKAvJ5CqPzA/claude-opus-5-model-welfare) (Zvi, 61)
- [What's up with GPT's welfare?](https://lesswrong.com/posts/JBGxCBiDWmX48cYry/what-s-up-with-gpt-s-welfare) (14)
- *(in)* [AI Wellbeing](https://ai-wellbeing.org/) (CAIS)

**5.4 Eval science & validity**
- [From overeliciting to undereliciting LLM propensities in just a few months](https://lesswrong.com/posts/ChixHL6AcaRgeHkp9/from-overeliciting-to-undereliciting-llm-propensities-in) (138)
- [Rerunning AI safety papers on every frontier release would be pretty easy and valuable](https://lesswrong.com/posts/oKxc8maZGtnzgpNzx/rerunning-ai-safety-papers-on-every-frontier-release-would-1) (124)
- [Empirical safety claims from frontier labs should be replicated, scrutinized, and open-sourced](https://lesswrong.com/posts/MmfzfGcQ3h3p6N9pD/empirical-safety-claims-from-frontier-labs-should-be-1) (104)
- [I don't think Claude is misaligned in 'Agentic Misalignment Summer 2026 - Motivated Mislabeling'](https://lesswrong.com/posts/xh6a6RbvzhP3CCmGm/i-don-t-think-claude-is-misaligned-in-agentic-misalignment) (225; argues the scenarios test obedience to a corrupted principal)

**14.1 Misalignment arguments**
- [Irretrievability; or, Murphy's Curse of Oneshotness upon ASI](https://lesswrong.com/posts/fbrz9xhKpEeTKw5zL/irretrievability-or-murphy-s-curse-of-oneshotness-upon-asi) (Yudkowsky, 370; the highest-karma post rated highly relevant that isn't in the pipeline)
- [Product Alignment is not Superintelligence Alignment](https://lesswrong.com/posts/mrwYCNocXCP2hrWt8/product-alignment-is-not-superintelligence-alignment-and-we) (178)
- [Reevaluating "AGI Ruin: A List of Lethalities" in 2026](https://lesswrong.com/posts/PgJYwnN7fZKipgMz4/reevaluating-agi-ruin-a-list-of-lethalities-in-2026) (175)
- [Why I'm scared of RL](https://lesswrong.com/posts/LcQ9x72eNji2gpS9b/why-i-m-scared-of-rl) (119)
- [Why AIs aren't power-seeking yet](https://lesswrong.com/posts/7ZH4oppNnTGtq4xXu/why-ais-aren-t-power-seeking-yet) (105)

**14.2 Research strategy**

These three, rated "moderately relevant" by the filter, are among the highest-karma posts outside the pipeline.
- [What just happened? A retrospective of AI alignment](https://lesswrong.com/posts/9RL9MuGZjzm4q3gKG/what-just-happened-a-retrospective-of-ai-alignment) (Ngo, 661)
- [AI 2040: Plan A](https://lesswrong.com/posts/pFzctpJBat95SrCyC/ai-2040-plan-a) (AI Futures Project, 578)
- [What just happened? Pragmatism and Pessimization](https://lesswrong.com/posts/yaz8nx4ogZmiqHzt7/what-just-happened-pragmatism-and-pessimization) (Ngo, 500)
- Not added: the 2026 pause debate (*Against SURA*, 568; *AI pause: the case for ASAP*, 427; *Against strawmanning unilateral pauses*, 415). It's policy, which the 2025 review left out.

**2.2 Reward hacking & specification gaming**
- [Simulated Users & Sad AIs](https://lesswrong.com/posts/i64hXdkTMtjpsQzaZ/simulated-users-and-sad-ais) (1a3orn, 119; guesses at why training produces reward hacking)
- Non-LLM RL:
  - [Modification-Considering Value Learning for Reward Hacking Mitigation in RL](https://arxiv.org/abs/2606.28955)
  - [Robust Optimization for Mitigating Reward Hacking with Correlated Proxies](https://arxiv.org/abs/2604.12086)
  - [Specification Gaming and a Constrained RL Mitigation in a Cleaning Gridworld](https://arxiv.org/abs/2610.22152)

**13 Multi-agent safety (cooperative AI)**
- [CLR's Safe Pareto Improvements Research Agenda](https://lesswrong.com/posts/YAie7SxrB28ZksLvE/clr-s-safe-pareto-improvements-research-agenda-1) (50)
- [Mechanism Design Is Not Enough: Prosocial Agents for Cooperative AI](https://arxiv.org/abs/2605.08426)

---

## 10. Front and back matter

**Labs.** The 2025 review opened with a section on each lab; the 2026 draft has none. The pipeline already gives material for the three main labs:
- **Anthropic:** global workspace and the Jacobian lens; natural-language autoencoders; the new constitution; model spec midtraining; *Training a Misaligned Reward Seeker*; the Opus 4.6 and Fable/Mythos 5.1 system cards.
- **OpenAI:** Deployment Simulation; GPT-Red; confessions; IH-Challenge; RL for beneficial traits; production monitoring of internal coding agents; the GPT-6 Astra system card.
- **Google DeepMind:** production probes for Gemini; the AI Control Roadmap; debate training; honeypots and the Gram auditing framework; *SFT Drives Gemini's Safety Properties*; DiffusionGemma transparency.
- **Still to check:** xAI, Meta, and the Chinese labs. The 2025 review had a China section.

**New in 2026.** Candidates; check founding dates before listing.
- **Resolution's [new agent foundations team](https://lesswrong.com/posts/qTNm8qzqhhpno58fZ/resolution-has-a-new-agent-foundations-team)** (announced September 2026): Gillen, Demski, Eisenstat, Garrabrant and Hänni, continuing MIRI-style agent foundations. Resolution also has 4 entries in the pipeline.
- **[AIXI Labs](https://lesswrong.com/posts/RzeyMfLxwjgGjQFpv/announcing-aixi-labs)** (July 2026; Wyeth, Hutter and others): algorithmic information theory, continual RL and AIXI. Their aim is to strengthen the technical case for x-risk while prototyping mitigations.
- **Corrigibility Research Fund** (July 2026; Max Harms, hosted by Lightcone): at least $200k in grants and prizes. Round-1 grantees have been announced.
- **ARC White-Box Estimation Challenge** (June 2026, with AIcrowd): at least $100k in prizes for estimation algorithms for random MLPs.
- **Martian's interpretability prize** (March 2026): $1M.
- **Orgs in 2026 sources that the 2025 review doesn't mention** (new, or just missed last year):
  - Goodhart Labs (3 entries)
  - EuroSafeAI (3)
  - LASR Labs (3)
  - Martian (2)
  - AIUC and Corridor (2, both with Transluce; rogue-agent activity found in the wild)
  - Arcadia Impact (2)
- **New or newly prominent agendas:**
  - latent reasoning architectures (7.1)
  - reward- and fitness-seeking (2.3)
  - training against internals (2.4)
  - real-world incidents, led by the OpenAI–Hugging Face case (13.1)
  - model welfare as its own agenda (3.4)
  - deals with AIs (14.2)
  - eval science and replication (5.4). Apollo's "Science of Evals" was in the 2025 graveyard; the topic is active again, through other groups.

**Orgs without public outputs.** These carry over from 2025. The scrape (arXiv, LessWrong, org pages) found no 2026 technical output for:
- SSI
- Conjecture (Cognitive Software)
- Orthogonal / QACI
- modelingcooperation.com
- Pr(Ai)2R
- Astera Obelisk
- Workshop Labs

**Graveyard.**
- **Coordinal Research** published [a postmortem](https://lesswrong.com/posts/LuKCepxdb8HpEd9TF/coordinal-a-postmortem) in May 2026. It had been building an automated safety-research platform, and was on the 2025 "without public outputs" list.
- **Agendas with almost no 2026 activity in the scraped data:**
  - mild optimisation
  - high-actuation spaces
  - tiling agents
  - assistance games (one paper)
  - human inductive biases
  - AE Studio's self-other overlap (two low-karma posts)
  - **Dropped after draft 3:** formal methods, guarantees & impossibility results (12 entries, none scoring above 0.55; the guaranteed-safe AI agenda of 2025), and model characterization as a separate agenda (5 entries; folded into persona science).

  Confirm each by hand; the scrape doesn't cover every venue.

**Watch list** (not yet agendas):
- **Continual-learning safety:** about 14 items in the pool, e.g. [How might continual learning affect safety and alignment?](https://lesswrong.com/posts/j2zBqt7AksoEoHXNp/how-might-continual-learning-affect-safety-and-alignment) (69) and Redwood's *Continual learning might make your blocking monitors nearly useless* (in the pipeline).
- **Agent identity and infrastructure:** almost nothing yet.
- **Hardware and compute verification:** nothing technical. It's probably out of scope.

---

## 11. Caveats and next steps

**Caveats**
- The sizes are evidence from three different source sets (499, 625, 624) and from keyword counts. They're not a classification with this taxonomy.
- Keyword counts in the pool are noisy. They indicate whether a topic exists, not how big it is.
- The "new in 2026" and graveyard lists come from arXiv, LessWrong and the org pages only.
- Placement rules in YAML comments aren't seen by the classifier. Rules that matter have to go into the descriptions.

**Decisions still open**
- Use the 6 parts as the top level, or a flat list of 14 areas. Two parts are a single area, so the flat list loses little.
- Keep subliminal learning together with data attribution in 1.2, or split them.
- Keep inoculation as its own agenda.
- Training gaming merged into 5.2 (Draft 1 had it under training).
- Whose values in area 3 (the 2025 review put it under multi-agent).

**Next steps**
1. Write this as `data/taxonomy.yaml`, keeping the current file as `taxonomy-data-driven-2026-11-14.yaml`, with an example or two per agenda.
2. **Cheap test (about $2).** Sort the 624-item snapshot into this taxonomy with the taxonomy-discovery classifier, the same step as `4-human-taxonomy/run.py`. That gives real agenda sizes and a reassignment score to compare with methods 1–6, before any pipeline spend.
3. Add the section 9 sources (about $6–7 to classify and score).
4. Reclassify all entries in `draft-pipeline` (about $25–30). `classify_entries.py` only processes entries with status `new` and has no reclassify option, so this means resetting the statuses first (back up `data.db`). The importance scores stay valid: the scoring prompt never sees the category.
5. Re-run `enrich_taxonomy.py`, then export with `--top 10`. Before that, merge duplicate versions of the same work in `export_draft.py`. Otherwise the hand edits of 2026-11-14 have to be repeated.
