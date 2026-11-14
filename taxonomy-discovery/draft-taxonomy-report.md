# The draft taxonomy against six automated taxonomies

This report compares `draft-taxonomy.md` with the six method outputs on the same 624 sources (Jan–Nov 2026). It then counts how often each research agenda appears across the methods and proposes a revised taxonomy built around the agendas that are robust across methods.

Item counts are sources, not distinct works. About 39 works appear more than once (arXiv + LessWrong + org page), so there are roughly 585 distinct works. Method numbers: 1 LLM-direct, 2 LLM-graph, 3 embedding-graph, 4 hand-written by model stage, 5 embedding map, 6 hand-written from the map.

## 1. Summary

The draft's agendas are mostly the right ones. Of the 36 agendas found across all seven taxonomies, 18 are produced by five or six of the six methods. The draft has 16 of those 18. The problems are placement and balance:

- **Missing agendas.** Honesty and lie detection is in five methods (median 16 items) but not in the draft. Unsafe agent actions on ordinary tasks is in three methods.
- **Reward hacking is split.** The draft spreads reward hacking and reward seeking over four places (1.6, 1.7, 3.2, 11.1). Reward hacking itself is in all six methods (median ~45 items).
- **Two areas are too big.** "Training-time alignment" and "Evaluations & auditing" each hold an estimated 110–140 items.
- **Some areas are thin.** "Theory & foundations" (~5–10 items) and "Model welfare" (~5–9) are top-level areas with little 2026 output. No method recovers either as an area.

**Recommendation:** use 12 agendas of roughly 25–75 items each, grouped into three areas by where the work acts on the model:

- **Training aligned models:** changing what the model is.
- **Understanding models and risks:** finding out what a model is and does, and what follows for risk.
- **Deployment safeguards:** constraining models and their environment in use.

Section 7 gives the full structure.

## 2. The draft taxonomy at a glance

The draft has 12 top-level areas and 40 leaves. Three areas have no leaves (8 Multi-agent, 9 Scalable oversight, 12 Model welfare), so there are 43 terminal categories.

Most areas are research agendas: CoT monitorability, control, multi-agent safety, scalable oversight. Four areas follow a different principle:

| Area | Defined by |
|---|---|
| 1 Training-time alignment | model stage |
| 3 Evaluations & auditing | activity (measuring) |
| 7 Real-world evidence | evidence type |
| 11 Threat models & strategy | genre (arguments) |

These exceptions are where the overlaps come from. For example, a paper on reward-hacking benchmarks fits 1.6, 3.2 and arguably 11.1.

Granularity is also uneven. Area 1 has 9 leaves and area 3 has 8, while four areas have one leaf or none.

## 3. Where the draft and the methods agree

Agreement across methods that work differently counts most. The strongest cases are where method 1 (LLM-direct), method 2 (LLM-graph) and at least one embedding method (3 or 5) all agree:

- **CoT monitorability.** It is a top-level area or leaf in all six methods, with 55–62 items. The draft's four leaves map almost one-to-one onto the leaves of methods 1 and 2.
- **Monitoring & control.** All six methods have it: 1: 68, 2: 52, 4: 67, 6: 82. Methods 3 and 5 inflate it into catch-alls of 135 and 139 items.
- **Interpretability** (all six) and **emergent misalignment / generalization** (five, all except method 4).
- **Smaller agendas.** Incidents, evaluation awareness, multi-agent collusion, sycophancy, misuse safeguards, agent security, tamper resistance, subliminal learning and debate are each a leaf in five or six methods.

Section 5 gives the full count.

## 4. Where they differ

**Agendas the methods find with weight that the draft lacks, merges or splits:**

- **Reward hacking and reward seeking.**
  - Reward hacking is a top-level area in four methods: method 1 (56), 3 (77), 4 (62) and 6 (62). Method 5 splits it over two areas, 72 and 54.
  - The reward-seeker threat-model work is a leaf of 14–25 items in five methods, and four of them place it next to reward hacking.
  - Method 5's top leaf confusion is "Reward hacking in LLM RL ↔ Reward-seeking and fitness-seeker threat models" (5 items). The two belong together.
- **Honesty and lie detection.** It is a leaf in five methods, with 8–25 items. Examples: *"Did you lie?" Evaluating Lie Detectors across Model Scale…*, *Why Safety Probes Catch Liars But Miss Fanatics*. The draft would scatter these over 3.2, 3.5, 3.7 and 4.2.
- **Alignment auditing.** Four methods make it its own area: 1 (51), 2 (88), 3 (62) and 6 (56). In method 2's version it also holds:
  - introspection (17)
  - self-report and confessions (17)
  - lie detection (8)

  The draft's evaluations area mixes measurement with auditing. The most-confused top pairs in methods 1 and 2 sit on this boundary: "Alignment Auditing, Model Organisms and Incidents ↔ Scheming, Deception and Situational Awareness" (10 items) in method 1, and "Misaligned motivations, evaluations and incidents ↔ Scheming, Evaluation Awareness, and Training Gaming" (10) in method 2.
- **Personas with welfare.** All five methods that have a welfare leaf put it next to personas, and three make a psychology area of 30–42 items. The draft splits this across 1.3, 3.3 and 12.
- **Sycophancy and user harms.** These go with multi-agent work in methods 1 and 2, and with personas in methods 3, 5 and 6. No method puts them with incidents, which is where the draft's 7.2 sits.
- **Dangerous-capability evals.** Methods 1, 3, 4 and 6 group them with misuse. Method 2 does the same for its biosecurity leaf.
- **Incidents, system cards and strategy.** Three methods merge incidents, system cards and strategy arguments into one area: method 1 (system cards with strategy), method 2 ("Misaligned motivations, evaluations and incidents", 73) and method 5 ("Alignment strategy and frontier incidents", 66).

**Draft categories with little support:**

| Draft category | ~Items | Recovered by | Keep? |
|---|---|---|---|
| 10.1 Agent foundations | ~3 | 6 (as part of a 9-item leaf) | Keep as a low-output leaf |
| 10.3 Formal methods | 0–1 | none | Keep only as a named low-output topic |
| 10.2 Heuristic explanations | ~5–7 | 1, 2, 3, all inside interpretability | Move to interpretability |
| 12 Model welfare | ~5–9 | 1, 2, 3, 6, all beside personas | Keep as a sub-topic of model character |
| 5.4 Weight & infrastructure security | ~3 | 2 (3 items); 3 and 6 as part of a leaf | Keep; a real agenda with little public output |
| Deals with AIs (11.3) | ~1–2 | none | Mention in a description only |

A review can keep quiet agendas. Readers want to know they exist. But they should be named sub-topics, not top-level areas.

**Organising principle and granularity.** The methods differ in how they group work:

- Method 2 groups by research agenda (as prompted).
- Methods 3 and 5 group by vocabulary and technique. That merges interpretability with data attribution and produces catch-all areas.
- Method 4 groups by model stage, which yields two areas of 130 items each.

The draft is closest to methods 1 and 2. Its leaves are about the size of method 1's (median ~12), which suits a review. Its problem is the uneven spread across areas, not leaf size.

## 5. Agenda frequency across methods

**Matching rules:**

- **Same agenda.** Two categories count as the same agenda if they address the same research problem, whatever the method or name. For example, "AI Control and Agent Monitoring" (1, 2), "AI control methods" (4), "Control evaluations and untrusted monitoring" + "Red-teaming agent monitors" + "Monitor robustness and evasion" (5), and "Control and monitoring of agents" (6) are all one agenda.
- **Matching level.** I matched at the most specific level that fits, usually leaves. A top-level area counts only when the method has no leaf for the agenda.
- **Categories spanning two agendas.** A category that spans two agendas is credited to both and marked "(part)". Its size is then a judgement of the relevant share, or the matching sub-leaves where they exist.
- **Method 4.** Its coarse areas count only where the area itself matches, as with control, CoT, interpretability, RL safety, incidents and strategy. Elsewhere it gets no credit.
- **What "n" means.** n counts methods with a matching category, out of six. The size column gives the median of the matched sizes, with the range.

| Agenda (canonical) | n | Draft | Matching categories (method: name, size) | Items: median (range) |
|---|---|---|---|---|
| CoT monitorability | 6 | 2 | 1: CoT Monitorability 58; 2: same 62; 3: same 59; 4: CoT monitoring 62; 5: CoT monitorability 55; 6: Reasoning transparency 59 | 59 (55–62) |
| AI control & monitoring | 6 | 4 | 1: AI Control and Agent Monitoring 68; 2: same 52; 3: monitoring/red-teaming/control-settings leaves ~56; 4: AI control methods 67; 5: control evals + monitor leaves 56; 6: Control and monitoring of agents 65 (excl. agent security) | 60 (52–68) |
| Reward hacking & spec gaming | 6 | 1.6, 3.2 | 1: three RH leaves 42; 2: RH in RL + spec gaming + hackable benchmarks 29; 3: RLVR + agent RH + EM from RH + spec gaming ~50; 4: RL safety 62; 5: RH in LLM RL + hackable benchmarks 49; 6: RH in RL 34 | 45 (29–62) |
| Interpretability methods & representations | 6 | 6.1, 6.2 | 1: features/circuits/lenses 33; 2: Interp methods, foundations, estimation 35; 3: SAE/circuits/verbalizer leaves ~38; 4: Interpretability 79; 5: SAEs + verbalization 47; 6: circuits + activation readouts 46 | 42 (33–79) |
| Alignment strategy & misalignment arguments | 6 | 11.2, 11.3 | 1: Alignment strategy and conceptual arguments 24; 2: theoretical arguments + training fails 20; 3: conceptual debates + takes 18; 4: Agent foundations and alignment strategy 41; 5: Alignment agendas and conceptual debates 28; 6: Misalignment evidence and debate 18 | 22 (18–41) |
| Incidents & in-the-wild misalignment | 6 | 7.1 | 1: In-the-wild misalignment 18; 2: OpenAI–HF incident 14; 3: same 11; 4: Frontier misalignment incidents 21; 5: OpenAI–HF hacking incident 21; 6: Incidents and deployment monitoring 21 | 20 (11–21) |
| Emergent misalignment & generalization | 5 | 1.2 | 1: EM + unintended generalization 31; 2: EM mechanisms, EM from RL, triggers, OOD 41; 3: EM mechanisms + conditional + EM from RH ~29; 5: EM from narrow finetuning 44; 6: emergent/conditional + distillation 43 | 41 (29–44) |
| Evaluation awareness | 5 | 3.4 | 1: Evaluation and training awareness 25; 2: eval awareness + realistic + metagaming 24; 3: Measuring and Mitigating Eval Awareness 14; 5: Evaluation awareness and realism 27; 6: Evaluation awareness 19 | 24 (14–27) |
| Training data & alignment pretraining | 5 | 1.1 | 1: data attribution + pretraining 23; 2: pretraining/constitutions + data attribution 29; 3: data attribution + pretraining 23; 5: subliminal & data attribution 21 (part); 6: Alignment pretraining and midtraining 17 | 23 (17–29) |
| Alignment auditing & model organisms | 5 | 3.7, 3.8 | 1: auditing tools + MO validity 33; 2: auditing benchmarks + automated auditors 19; 3: automated auditing + MO methodology 23; 5: auditing benchmarks + MOs/sandbagging 22; 6: Probes and alignment audits 23 | 23 (19–33) |
| Scheming, sabotage & self-preservation propensity | 5 | 3.2 | 1: scheming/AF + self-preservation 24; 2: Scheming and LoC Propensity Evals 18; 3: sabotage propensity + shutdown resistance 20; 5: Scheming and sabotage propensity evals 23; 6: Scheming and self-preservation 15 | 20 (15–24) |
| Introspection & self-report | 5 | 3.5 | 1: Introspection and self-report 9; 2: introspection + self-reporting + self-disclosure 34; 3: Introspection and Global Workspace 11; 5: introspection + eliciting self-reports 29; 6: Activation readouts and introspection 18 | 18 (9–34) |
| Multi-agent collusion & dynamics | 5 | 8 | 1: Multi-agent collusion 16; 2: collusion + bargaining 19; 3: collusion + multi-agent orgs 21; 5: Multi-agent collusion 17; 6: Multi-agent spread 18 | 18 (16–21) |
| Personas & AI identity | 5 | 1.3 | 1: Persona structure 15; 2: Persona Selection 11 (+7 trait absorption); 3: Persona selection 17; 5: LLM personas 20; 6: Personas and assistant identity 18 | 17 (11–20) |
| Agent security & prompt injection | 5 | 5.2 | 1: 23; 2: 13; 3: 11; 5: 19; 6: 17 | 17 (11–23) |
| Reward-seeking & fitness-seeking motivations | 5 | 11.1 | 1: 14; 2: 16; 3: 15; 5: 25; 6: 17 | 16 (14–25) |
| Honesty & lie detection | 5 | — | 1: Honesty, lying and lie detection 16; 2: Lie Detection testbeds 8; 3: Lie Detection and Model Deception 18; 5: Lie detection and deception probes 25; 6: Lie detection and secret elicitation 16 | 16 (8–25) |
| Dangerous capability evals | 5 | 3.1 | 1: 13; 2: bio + AI R&D 14; 3: bio + AI R&D benchmarks 20; 5: bio 6; 6: 16 | 14 (6–20) |
| System cards & risk reports | 5 | 7.3 | 1: 11; 2: system cards + assessments 20; 3: System Cards and Deployment Simulation 6; 5: 17; 6: Lab safety practice 14 | 14 (6–20) |
| Jailbreaks & misuse safeguards | 5 | 5.1 | 1: 20; 2: jailbreaks + automated red-teaming 13; 3: 6; 5: 13; 6: 16 | 13 (6–20) |
| Tamper resistance & unlearning | 5 | 5.3 | 1: 9; 2: 13; 3: tamper resistance + open-weight attacks 25; 5: 14; 6: Open weights and weight security 9 | 13 (9–25) |
| Subliminal learning | 5 | 1.4 | 1: 10; 2: 12; 3: 12; 5: (part of 21); 6: 16 | 12 (10–16) |
| Sycophancy & effects on users | 5 | 7.2 | 1: 12; 2: 11; 3: 10; 5: 9; 6: Effects on users 11 | 11 (9–12) |
| Training gaming / resisting training | 5 | 1.7 | 1: Sandbagging, exploration hacking (part) 12; 2: Alignment Faking and Training Gaming 11; 3: Spec Gaming and Training Resistance (part) 8; 5: Gradient hacking 9; 6: Alignment faking and gradient hacking 11 | 11 (8–12) |
| Debate & scalable oversight | 5 | 9 | 1: 13; 2: 14; 3: 9; 5: 10; 6: 10 | 10 (9–14) |
| Model welfare & emotions | 5 | 12 | 1: 6; 2: 9; 3: 5; 5: (part of 13); 6: 5 | 6 (5–9) |
| Internals & monitors as training signals | 4 | 1.8 | 1: Using internals in training 7; 2: Training Against Probes and Monitors 12; 3: 5; 6: Interpretability in training and control 13 | 10 (5–13) |
| Alignment targets & constitutions | 4 | 1.9 | 1: Constitutions, character training 8; 2: (part of 18); 3: Constitutions, identity 10; 6: Model values and constitutions 7 | 8 (7–10) |
| Inoculation prompting | 4 | 1.5 | 1: 10; 2: (part of 13); 5: (part of 8); 6: 5 | 5–10 |
| Production monitoring & control roadmaps | 3 | — (part of 4.1) | 1: 15; 2: Deployed Lab Monitoring Red-Teaming 14; 3: Control Roadmaps 10 | 14 (10–15) |
| Unsafe agent actions on ordinary tasks | 3 | — | 2: Unsafe Behavior of Deployed Agents 9; 3: Live Agent Misuse + Coding Agent Overreach 14; 5: Agent shutdown and overreach (part) 14 | 9–14 |
| Automated alignment research & its sabotage | 3 | 9 | 2: Sabotage of Automated Safety Research 12; 3: research agendas and automation + sabotage 17; 6: 5 | 12 (5–17) |
| Eval science & validity | 3 | 3.6 | 1: Limits of evaluation and safety cases 9; 3: Alignment Evals and Eval-Gaming (part) 13; 6: Eval and benchmark validity 14 | 13 (9–14) |
| Mechanistic estimation | 3 | 10.2 | 1: 7; 2: (part of 11); 3: (part of 12) | 7–11 |
| Learning dynamics / dev interp | 3 | 6.3 | 1: 5; 2: 7; 3: Susceptibility Spectroscopy 6 | 6 (5–7) |
| Sandbagging & capability elicitation | 3 | (part of 3.7) | 1: (part of 12); 2: 6; 5: (part of 12) | 6–12 |
| Model characterization (values, principals) | 2 | 3.3 | 2: Competing principals 5; 6: Model values and constitutions (part) 7 | 5–7 |
| Weight & infrastructure security | 2–3 | 5.4 | 2: Inference infrastructure security 3; 3, 6: part of an open-weight leaf | ~3 |
| Agent foundations | 1–2 | 10.1 | 6: Alignment targets and foundations (part) 9; 4: (part of 41) | ~3 |
| Formal methods; deals with AIs | 0 | 10.3, 11.3 | none | 0–2 |

## 6. Top agendas

The ranking below favours agendas that are frequent across method types and large. Each one is produced by method 1 (LLM-direct), method 2 (LLM-graph) and at least one embedding method, unless noted otherwise.

1. **AI control & monitoring.** It appears in 6 of 6 methods, with ~60 items. It is the largest agenda in every method that isolates it. Examples: *LinuxArena*, *SLEIGHT-Bench*, *Lessons From Red-teaming Auto-review, OpenAI's Blocking Monitor*.
2. **CoT monitorability.** 6 of 6 methods, ~59 items. It has the tightest size range of any agenda (55–62) and the same internal leaves everywhere: latent reasoning, faithfulness, obfuscation, training pressure.
3. **Reward hacking & reward seeking.** Reward hacking is in 6 of 6 methods (~45 items) and reward-seeking motivations in 5 of 6 (~16). Together they make one area of 55–77 items in five methods. Examples: *Exploration Hacking: Can LLMs Learn to Resist RL Training?*, *Hardening Agent Benchmarks with Adversarial Hacker-Fixer Loops*.
4. **Emergent misalignment & generalization.** 5 of 6 methods, ~41 items. Add subliminal learning (12) and training data (23), which three methods place alongside it.
5. **Interpretability.** 6 of 6 methods, ~42 items. Sizes vary because the embedding methods also pull in data attribution.
6. **Alignment auditing, honesty & introspection.** Auditing (~23), lie detection (~16) and introspection/self-report (~18) are each in 5 of 6 methods. Method 2 joins all three into one 88-item area.
7. **Propensity & evaluation-awareness evals.** Eval awareness (~24) and scheming propensity (~20) are each in 5 of 6 methods.
8. **Misuse & security.** Agent security, jailbreaks, tamper resistance and dangerous-capability evals are each in 5 of 6 methods, at 13–17 items each, ~60 combined.
9. **Strategy & misalignment arguments, with real-world evidence.** Strategy is in 6 of 6 methods (~22) and incidents in 6 of 6 (~20). The OpenAI–Hugging Face incident alone is 11–21 sources in five methods.
10. **Multi-agent & societal effects.** Multi-agent work (~18) and sycophancy (~11) are each in 5 of 6 methods.

Below this tier are two more groups:

- **Robust but small (5 of 6 methods, ~6–12 items):** personas, debate and welfare. Personas (~17) and welfare (~6) go together in every method that has both.
- **In fewer methods (3 of 6):** production monitoring, unsafe agent actions on ordinary tasks, and automated alignment research.

## 7. Suggested taxonomy

There are 12 agendas in 3 areas. The organising principle is **where the work acts**:

- on the model's training,
- on our knowledge of the model and the risks,
- or on the deployment around the model.

This is the draft's dominant principle made explicit and coarse enough to apply consistently. It is close to method 4's model-stage principle, but at the agenda level.

Sizes are rough (±30%) and estimated from the matched categories above. They sum to about 630.

### A. Training aligned models (~200)

Work whose contribution is a change to how models are trained, or an explanation of how training shapes what the model becomes.

| Agenda | Inclusion criterion | Covers | ~Items |
|---|---|---|---|
| A1 Training data & generalization | How data and fine-tuning shape what a model learns and how it generalizes | data interventions & attribution, emergent misalignment, subliminal learning, inoculation, internals/monitors as training signals | 75 |
| A2 Reward hacking & reward seeking | Models exploiting or steering their training signal, and motivations that would produce this | RH in RL, RH benchmarks & hackable environments, reward/fitness-seeker threat models, exploration/gradient/generalization hacking | 60 |
| A3 Model character: personas, values & welfare | What kind of entity a model is and what to train it to be | persona science, alignment targets & constitutions, model characterization, welfare & emotions | 40 |
| A4 Scalable oversight & automated alignment | Supervising models stronger than the overseer, and using AI to do alignment research | debate, weak-to-strong, co-trained overseers, automated safety research and its sabotage | 25 |

### B. Understanding models and risks (~225)

Work whose contribution is knowledge: tools or measurements that reveal what a given model is or does, real-world evidence, or arguments about risk. It changes neither training nor deployment.

| Agenda | Inclusion criterion | Covers | ~Items |
|---|---|---|---|
| B1 Interpretability | Tools for understanding internals, or findings about them | methods & tools, science of representations, learning dynamics/dev interp, heuristic explanations & mechanistic estimation | 50 |
| B2 Alignment auditing, honesty & introspection | Methods for finding out what a specific model hides or knows about itself, and testbeds for them | auditing methods & agents, model organisms, lie detection, introspection & self-report (incl. confessions), sandbagging elicitation | 60 |
| B3 Propensity & evaluation-awareness evals | Measuring what current models will do when given the chance, and whether those measurements hold | scheming, sabotage & self-preservation; unsafe agent actions on ordinary tasks; evaluation awareness; eval science & validity | 55 |
| B4 Real-world evidence & strategy | Evidence from deployments and lab disclosures, and conceptual arguments about risk and priorities | incidents, system cards & risk reports, misalignment arguments, research strategy & deals, agent foundations & formal methods (low output) | 60 |

### C. Deployment safeguards (~205)

Work whose contribution is a protocol, monitor or defence that applies when models are used, or a failure mode that only arises in use (misuse, agents interacting).

| Agenda | Inclusion criterion | Covers | ~Items |
|---|---|---|---|
| C1 AI control & monitoring | Protocols and monitors that keep a possibly misaligned model safe | control settings & protocols, monitors, red-teaming monitors, control in production | 60 |
| C2 CoT monitorability | Whether written reasoning stays a reliable monitoring signal | latent reasoning, control/obfuscation/steganography, training effects on monitorability, faithfulness | 58 |
| C3 Misuse, security & dangerous capabilities | Defending against external adversaries, and measuring the capabilities they could misuse | dangerous capability evals, jailbreaks & safeguards, agent security, tamper resistance & unlearning, weight security (low output) | 60 |
| C4 Multi-agent & societal effects | Failures from AIs interacting with each other or with people at scale | collusion & multi-agent dynamics, sycophancy, manipulation & disempowerment | 30 |

**Boundary cases:**

- **C2 (CoT monitorability).** It could sit in B as a property of models. It is in C because its question is whether a monitoring signal survives, and method 4 also files it under control.
- **C4 (multi-agent & societal).** It is in C because these failures arise in deployment. The work itself is mostly measurement.
- **Rule for the classifier.** Classify by the problem addressed, not by the tool. A probe used as a lie detector goes to B2. A probe used as a deployment monitor goes to C1. A probe used as a training penalty goes to A1.

**Alternative considered: grouping by threat source.** The groups would be misalignment, misuse/external attackers, and structural/societal risk, plus cross-cutting work. I rejected it for two reasons. The misalignment group would hold about 75% of the items. And interpretability and strategy fit no group, so they'd need a "cross-cutting" bucket, which is a catch-all.

## 8. Changes from the draft

| Change | What | Reason | Evidence |
|---|---|---|---|
| Added | 3 top-level areas grouping the agendas | Coarse grouping for the outline; makes the draft's implicit principle explicit | Area sizes ~200/225/205 |
| Added (agenda) | A2 Reward hacking & reward seeking, from 1.6, 1.7, 3.2 (part), 11.1 | Coherent agenda split four ways | RH in 6 of 6 methods; reward-seeking in 5 of 6; method 5 leaf confusion |
| Split | Draft 3 into B2 (auditing, honesty, introspection) and B3 (propensity & awareness evals); 3.1 moved to C3 | Draft 3 holds ~110–140 items mixing measurement and auditing | Auditing area in methods 1, 2, 3, 6; top confused pairs in methods 1 and 2 |
| Added | Honesty & lie detection (in B2) | No home in the draft | 5 of 6 methods, median 16 |
| Added | Unsafe agent actions on ordinary tasks (in B3); control in production (in C1) | No clear home | 3 of 6 methods each, 9–15 items |
| Merged | 1.3 personas, 1.9 alignment targets, 3.3 characterization, 12 welfare into A3 | Welfare too small to stand alone; these cluster together | Welfare beside personas in all methods; areas of 30–42 in methods 1, 3, 6 |
| Moved | 7.2 Effects on people into C4 with multi-agent work | Mostly experiments, not real-world evidence | Grouped with multi-agent in methods 1 (28) and 2 (35) |
| Merged | 7 Real-world evidence, 10 Theory, 11 Threat models & strategy into B4 | Theory ~5–10 items; incidents, system cards and strategy co-cluster | Merged in methods 1, 2 (73) and 5 (66) |
| Moved | 10.2 Heuristic explanations into B1 | Clusters with interpretability | Methods 1, 2, 3 |
| Moved | 3.1 Capability evals into C3 | Methods group them with misuse | Methods 1, 3, 4, 6 (and 2 for bio) |
| Moved | 9 Scalable oversight into area A | Oversight methods are training-time supervision | Method 1 "Alignment Training and Scalable Oversight" |
| Renamed | 1 "Training-time alignment" to A1 "Training data & generalization" | Narrower after moves | Methods 1 and 6 use near-identical names |
| Kept, low output | 5.4 weight security, 10.1 agent foundations, 10.3 formal methods, deals | Real agendas, quiet in 2026 | 0–3 items each |

## 9. Open questions

1. **Cross-cutting work.** Model organisms could sit in B2 or with the phenomenon they model. Introspection could sit in B2 (method 2's choice), interpretability (methods 3, 5, 6) or A3 (method 1). Alignment faking could go to B3 propensity or A2 training gaming (method 6). Internals as training signals are spread across four homes. Decide the "problem, not tool" rule and write it into the descriptions.
2. **Capability evals.** Should they go in C3 (as most methods do) or B3, keeping all measurement together? Autonomy and AI R&D evals fit misuse less well than CBRN and cyber do.
3. **Secondary tags.** Allowing a secondary tag would keep the outline clean while items appear in both homes.
4. **Low-output agendas.** Should they appear as named topics with "little 2026 output" notes, or only in prose?
5. **Agenda count.** Twelve agendas avoid buckets over ~75 items. If ten are wanted, the least costly merges are A4 into A3, or C4 into B3.

**How to test:**

- Add the revision as a method folder, e.g. `7-revised-taxonomy/`, copying `4-human-taxonomy/` (`taxonomy.yaml` + `run.py`). Use the agendas as categories and the "Covers" lists as optional subcategories. Write descriptions as inclusion criteria, since the classifier sees only those.
- Do the same for the current draft as a baseline.
- Run the classifier (about $2 each), then `compare.py` and `report.py`.
- What to compare:
  - reassignment accuracy: methods 4 and 6 score 90% at top level; method 1's 86% is inflated by self-consistency;
  - balance: aim for ≥ 0.95;
  - within-category link share on method 2's graph: method 2 scores 79%, method 1 68%, method 4 65%;
  - the most-confused pairs: expect B2↔B3 and A1↔A2. If those pairs dominate, sharpen the descriptions before moving categories again.
