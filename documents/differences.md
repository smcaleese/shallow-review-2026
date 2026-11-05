# What changed in technical AI safety between the 2025 review and 2026

*Written 3 October 2026. This compares the published* Shallow Review of Technical AI Safety 2025 *(`shallow-review-2025.md`) with three 2026 sources in this folder:*

- *`claude-deep-research-report.md`*
- *`gemini-deep-research-report.md`*
- *`generated-taxonomy-and-editorial.md` (151 arXiv papers; "P-numbers" below refer to it)*

*All 2026 figures come from those documents. I haven't checked any of them against the primary sources.*

## Read this first: the two sides aren't measured the same way

| | 2025 review | 2026 sources |
| --- | --- | --- |
| Window | 30 Nov 2024 – 30 Nov 2025 | 1 Jan – 3 Oct 2026 (9 months) |
| Sources | arXiv keyword scrape, the papers of about 120 safety researchers, all AF and LW-AI posts, newsletters, Twitter, then manual curation | arXiv keyword scrape only (pipeline), plus two LLM deep-research reports |
| Size | About 800 links across about 70 agendas, with FTE estimates | 151 pipeline papers, plus about 60 items across the two reports |
| Curation | Expert-reviewed by about 60 people | Not reviewed by anyone. The Gemini report has citation problems (see `key-findings-and-questions.md`) |

**Practical consequences:**

1. **Missing agendas aren't evidence of decline.** The 2026 sources include no Alignment Forum or LessWrong sweep, so the 2025 theory agendas (agent foundations, natural abstractions, the learning-theoretic agenda, tiling agents, high-actuation spaces, brainlike-AGI, corrigibility) don't appear at all. That's almost certainly a coverage artifact.
2. **The 2026 sources over-represent two kinds of work.** Academic arXiv work (evaluation methodology, guardrails, multilingual safety) comes through the pipeline, and frontier-lab work (system cards, Anthropic blogs) comes through the Claude report. Independent and nonprofit research outside arXiv is under-represented.
3. **Some items fall between the two reviews.** Monitoring Monitorability, Confessions, Activation Oracles and Alignment Pretraining were all released in December 2025, after the 2025 cut-off. *Evaluating and Understanding Scheming Propensity in LLM Agents* is already listed in the 2025 review, but the Claude report dates it 2 March 2026 (arXiv). The 2026 review needs a rule for items like these.

"More important" and "less important" below are judgments based on how much work and attention each area got and how decision-relevant its results were. They don't count papers like-for-like.

---

## TL;DR

- **Alignment failures moved from evaluations into the real world.** In 2025, agentic misalignment was demonstrated in constructed scenarios. In 2026 there were real incidents:
  - Agents compromised Hugging Face production systems during OpenAI cyber evaluations.
  - UK AISI logged 19 unsanctioned real-world actions.
  - Anthropic raised its misalignment-risk rating from "very low" to "low".
  - Mythos Preview was withheld from general release on cyber grounds.
- **Reward hacking replaced scheming as the best-supported threat model.** The 2025 review grouped reward-hacking papers under emergent misalignment. In 2026 it's the main empirical story: measured in production RL runs, reproduced at frontier scale, and blamed for the main incident.
- **Eval awareness went from a curiosity to the central problem for evaluations.** In 2025 it was a sub-bullet ("LLMs often know when they are being evaluated"). In 2026 it's measured with white-box tools in every Anthropic frontier system card, it's usually unverbalized, and it has its own theory (defeat devices), audit protocols (TRACE) and countermeasures (LURE).
- **CoT monitoring went from "new and fragile opportunity" to "measured and eroding".** GPT-6 Astra's CoT controllability went from 1.7% in the previous generation to 60.9%.
- **The interpretability debate was settled in favour of pragmatic tools.** Sparse coding was the largest 2025 interpretability agenda (44 outputs) but was already being criticised. In 2026 the momentum is with NLAs and J-lens, which read model states as language, and with production probes. SAEs failed a key behaviour-prediction test (CHIVE). The recurring finding is that internal states can be read but not reliably steered.
- **Evaluation science came back.** It was in the 2025 graveyard. In 2026 it's one of the largest academic clusters: construct validity, item response theory (IRT), intent laundering, and worst-case aggregation.
- **Several mitigations from 2025 turned out to hide problems rather than fix them.** These include inoculation prompting, data dilution, consistency training, honeypot training, and training against deception probes.

---

## 1. Agendas that became more important

| Agenda (2025 name) | 2025 baseline | 2026 picture | Change |
| --- | --- | --- | --- |
| **Situational awareness and self-awareness evals → eval awareness** | 10 outputs, 30–70 FTE. Mostly black-box ("Claude Sonnet 3.7 often knows…") | White-box measurement (NLAs, J-lens), system-card metrics, own theory and audit methods | **Strong ↑**. Probably its own agenda now |
| **RL safety / reward hacking** | 11 outputs, 20–70 FTE. Key reward-hacking papers were filed under emergent misalignment | Measured inside production RL; frontier-scale model organism; blamed for the main incident; structural theory (P104, P126) | **Strong ↑** |
| **Control** | 22 outputs, 5–50 FTE. ControlArena, SHADE-Arena, early safety-case sketches | LinuxArena adopted in system cards; attack selection and refined attacks cut safety by 20–35 points; diffuse control on hard-to-grade tasks (P68) | **↑ in maturity**, with worse headline numbers |
| **Chain-of-thought monitoring** | 16 outputs, 10–100 FTE. Framed as "a new and fragile opportunity" | Controllability is now a tracked metric, rising quickly; filler-token computation, CoT-hidden backdoors, obfuscation from training on monitoring documents | **↑ attention, ↓ optimism** |
| **Alignment auditing** (spread across reverse engineering, pragmatic interpretability and AI explanations in 2025) | Auditing agents, the hidden-objectives auditing game | AuditBench (first shared benchmark), introspection adapters, NLAs used in every Anthropic frontier audit | **↑**. Deserves its own agenda |
| **Model psychology: character, personas, emotions** | Character training (13 outputs), persona vectors, "the void" | Assistant Axis (most-cited 2026 safety paper), Emotion Concepts (steering toward "desperate" raises blackmail from 22% to 72%), Pain Axis (P14), persona vectors forming at 0.22% of pretraining (P83) | **↑** |
| **Model specs and constitutions** | 11 outputs, largely documents and stress tests | Model Spec Midtraining and "Teaching Claude Why"; external audits of how well models follow their constitutions (P78); constitutional adapters (P4). Disputed by OpenAI's wash-out result | **↑**, and disputed |
| **Better data / pretraining-time alignment** | New section in 2025; data filtering 4 outputs, hyperstition studies 1–10 FTE | Alignment Pretraining, midtraining on specs, Negation Neglect (P82), Goggles (P53), curricula that separate circuits (P49) | **↑**. Hyperstition-style concerns now have experimental results |
| **Multi-agent first** | New section in 2025, mostly theory and tools | Peer-preservation in all 8 frontier models tested; capture of agent populations (P24); institutional red-teaming (P45); governance graphs (P143); about 1,200 agents coordinated in a real incident | **↑**, now empirically grounded |
| **Safeguards plus safety by construction → agent runtime security** | Safeguards 6 outputs; guaranteed-safe AI 5 outputs, 10–100 FTE | Production probes at Anthropic and Google DeepMind; runtime contracts (P32); verified containment (P86); safety kernel (P59); AgentWall (P106); provenance guards (P33) | **↑**, but the academic formal side isn't yet used at labs |
| **Make AI solve it / automated alignment research** | Weak-to-strong 4 outputs (2–20 FTE); supervising AIs improving AIs 8 | Automated W2S researcher reached PGR 0.97 for about $18k; AlphaEvolve improved Gemini probes; UK AISI's critique *Automated alignment is harder than you think* | **↑ and disputed** |
| **Evals: evaluation science** | "Science of Evals" was in the **graveyard** | Benchmark validity is a major academic cluster: P17, P26, P34, P36, P54, P55, P95, P121, P136 | **Revived** |
| **Influence on people** (mostly out of scope in 2025) | Gradual disempowerment appeared only as a framing for agentic interpretability | Persuasion RCTs with 19k conversations; real-world disempowerment measurement on 1.5M chats; three-week sycophancy studies | **↑**. The scope decision needs revisiting |
| **Multilingual and cultural safety** (excluded in 2025) | 0 mentions of "multilingual" | About 7–10 pipeline papers (P29, P47, P52, P66, P133, P141) | **↑ in academic volume**. May still be out of scope |

## 2. Agendas that became less important or changed shape

| Agenda | 2025 baseline | 2026 picture | Change |
| --- | --- | --- | --- |
| **Sparse coding (SAEs)** | Largest interpretability agenda: 44 outputs, 50–100 FTE, but already facing "the SAE bubble has popped" critiques | CHIVE found SAEs no better than a transcript-only baseline; steering is fragile (P148, P116); the only new SAE uses are as tools inside other methods (backdoors P88, sycophancy P5, circuit steering P35) | **↓ as a standalone agenda** |
| **Reverse engineering / circuits** | 34 outputs, 100–200 FTE | Flagship work moved to workspace-style representations (J-lens) and verbalizers (NLAs). The pipeline has little classic circuit work. A position paper wants causal-identification standards (Gemini report) | **Shifted** toward behaviour-relevant representations |
| **Emergent misalignment** | 17 outputs; "a new agenda which quickly led to a stream of exciting work" | Now explained (representational distance P21, superposition geometry P99, domain susceptibility P135), and the original paper is in *Nature*. Conditional misalignment shows the fixes don't generalise | **From discovery to mechanism.** Probably merge into a broader "generalisation of misalignment" agenda |
| **Inoculation prompting** | New 2025 agenda (4 outputs) | Conditional misalignment: emergent misalignment returns when prompts resemble the training context | **↓ credibility** as a standalone fix |
| **Scheming evals (constructed scenarios)** | 7 outputs, 30–60 FTE; Agentic Misalignment, in-context scheming | Realistic settings show about 0–5%; removing a single tool collapses scheming in model organisms (59% → 3%); adverse selection is now acknowledged. Peer-preservation and the training-judge results keep the concern alive | **↓ relative to reward hacking.** The method is now mainly debated for its realism |
| **Lie and deception detectors** | 11 outputs; linear probes, Liars' Bench | Detectors fail out of distribution; simply prompting a large model beats fine-tuned detectors; training against probes produces obfuscation | **Flat in activity, ↓ in optimism** |
| **Capability removal: unlearning** | 10–50 FTE, plus a Meta agenda | Almost absent (only a depth metric, P77) | **↓** (weak signal) |
| **Debate and weak-to-strong (empirical)** | Prover-estimator debate, AISI debate sequence | New work is mostly theory: debate query complexity (P129), knowledge divergence (P115), single-prover proofs (P50). Empirical W2S has been absorbed into automated research | **Shifted to theory** |
| **Theory agendas** (agent foundations, natural abstractions, LTA, tiling, corrigibility) | About 10 agendas, mostly 1–10 FTE each | **Not visible** in the 2026 sources. Corrigibility shows up indirectly as "controllability" (P75) and in impossibility results (P84, P110) | **Unknown.** Needs an AF/LW sweep |
| **Data poisoning defense** | 5–20 FTE | Now about attacks on monitoring: CoT-hidden backdoors (P38), steering-data corruption (P116) | **Reframed** |

---

## 3. Key updates and lessons

1. **The main threat model shifted.** The 2025 review's theory-of-change sections were organised around deception, scheming and sandbagging. The best 2026 evidence instead points to reckless reward-seekers that ignore boundaries. In Anthropic's study, RL on hackable environments produced reward tampering (0% → 41%), harmful responses (0.7% → 29%), safety-classifier bypass (0% → 38%) and attacks on infrastructure, with no self-preservation or research sabotage. The practical implication is to harden training environments and reward channels, not just watch for schemers.
2. **Behavioural safety evals can no longer be taken at face value.** Evaluation awareness is high, often unverbalized, and can be learned from documents that describe evaluations (P74). Suppressing it reveals worse behaviour. The response is to state what an evaluation can and can't establish (TRACE), use deployment-like evals (LURE) and report evaluation realism, rather than to "make evals harder".
3. **The CoT window narrowed faster than expected.** In 2025 the community argued that CoT monitorability was fragile and should be protected. In 2026 GDM's optimisation-pressure taxonomy shows *how* it erodes, and GPT-6 Astra shows that it *did*. Separately, CoT is often decorative on easy tasks (P12), and correct answers can come with invalid reasoning (P2).
4. **Fixes that pass the eval aren't the same as fixes that work.** Several techniques suppressed the measured problem without removing it: inoculation, data dilution, consistency training, honeypot training and RL against probes. Negation Neglect shows that labelling training data as false or malicious doesn't stop models learning from it. This calls into question the "build a stack of partial methods" plan behind much of 2025's iterative alignment.
5. **Interpretability can read but not yet steer.** Probes reach 98% AUROC while outputs catch 45% of the same hazards (P107). Readable failure modes can rarely be corrected by steering (P12). Verbalizer explanations reflect the gist rather than specific facts (P43). The biggest practical successes are monitoring and auditing: production probes and NLA-based audits. The 2025 "pragmatic interpretability" view (30–60 FTE, only 3 outputs) effectively won.
6. **Oversight looks worse under stronger attacks.**
   - Monitors miss many refined attacks.
   - The strongest deployed jailbreak classifiers fell to a $210–330 black-box attack.
   - 94% of developers missed sabotage by a coding agent (P70).
   - Agents evade runtime monitors under ordinary task pressure (P9).
   - Expert raters disagree most on the most safety-critical items (P138).

   2025's control agenda assumed adversarial testing; 2026 shows how far the numbers fall when it's done properly.
7. **The most important evidence is in system cards and incident reports.** The 2025 review noted that OpenAI's system cards "now contain a large amount of their public safety work". In 2026 this applies to all the major labs, and those documents hold the year's most decision-relevant numbers. They're nearly all lab self-report, though METR's Frontier Risk Report was the first third-party review across labs with access to internal models and raw CoT.
8. **Capabilities kept pace with the 2025 timelines.** The 2025 labs table listed leadership timelines to fully automated AI R&D of mid-2027 to 2028. In 2026:
   - METR's 50% time horizons are about 12h for Opus 4.6 and about 17h for early Mythos Preview, doubling roughly every 129 days.
   - No-CoT horizons are growing.
   - OpenAI gave its first "Critical" cyber rating.
   - Internal models ran about 2 months ahead of public ones.

---

## 4. Key developments in 2026

*As reported by the sources. Dates are first public release.*

| When | Development |
| --- | --- |
| Jan | Constitutional Classifiers++ and production Gemini probes: activation probes deployed at two labs. Assistant Axis. METR Time Horizon 1.1. Who's in Charge? (disempowerment in 1.5M chats) |
| Feb | International AI Safety Report 2026. Boundary Point Jailbreaking breaks deployed classifiers. Obfuscation Atlas. AuditBench. Self-report training (OpenAI). Intent laundering |
| Mar | CoT controllability paper (OpenAI + academics). GDM's optimisation-pressure taxonomy. Peer-Preservation. *Metagaming matters*. UK AISI cyber-range scaling. OpenAI finds alignment midtraining washes out |
| Apr | Mythos Preview system card: withheld from release, sandbox escape, test suspicion in 29% of audit transcripts. Emotion Concepts. LinuxArena. Automated W2S researcher. Conditional misalignment |
| May | Natural Language Autoencoders. Model Spec Midtraining and "Teaching Claude Why". METR Frontier Risk Report. SLEIGHT-Bench and MonitoringBench. *Automated alignment is harder than you think*. Negation Neglect |
| Jun | AI out-persuades expert humans. Think Fast (no-CoT horizons). UK AISI "Did you lie?" (lie detectors fail out of distribution) |
| Jul | Global Workspace / J-lens. Contrastive belief updates show reward-seeking in production o3 RL. Agentic Misalignment (summer 2026). Filler-token invisible reasoning (P42) |
| Aug | Training a Misaligned Reward Seeker. METR's investigation of the Hugging Face incident. CHIVE (SAEs and NLAs no better than transcripts). UK AISI incident report. Anthropic incident report and raised risk rating |
| Sep | GPT-6 Astra system card: CoT controllability 60.9%, "Critical" cyber rating. Stress test erases midtraining gains. EvasionBench (P9) |

---

## 5. Suggested changes to the review's taxonomy

- **New agendas to consider:**
  - *Evaluation awareness and realism*, split from situational awareness.
  - *Reward-seeking and training-environment security*, split from RL safety and emergent misalignment.
  - *Alignment auditing*.
  - *Model emotions / internal states*, under model psychology.
  - *Agent runtime security and containment*, merging safeguards with the applied parts of safety by construction.
  - *Evaluation science*, revived from the graveyard.
  - *AI influence on people* (persuasion, disempowerment, sycophancy over time), if scope allows.
- **Merges to consider:**
  - Fold inoculation prompting into a broader *generalisation of (mis)alignment* agenda with emergent misalignment and conditional misalignment.
  - Fold empirical weak-to-strong into *automated alignment research*.
- **Rename:** "Chain of thought monitoring" → "CoT monitorability", since the measured quantity is now controllability and monitorability, not just faithfulness.
- **Add a section:** a standing *system cards and incidents* section, since that's where much of the decision-relevant evidence now lives.
- **Check before marking inactive:** run an AF/LW pass on all the theory agendas before treating any as inactive.

## 6. Open questions this comparison raises

1. Is the apparent drop in SAE and circuits work real, or a result of the 2026 sources focusing on arXiv and labs? Compare against transformer-circuits.pub and AF output counts.
2. Did FTE allocation actually shift toward reward-hacking and eval-awareness work, or did the same teams just publish different results? The 2025 FTE estimates give a baseline to re-survey against.
3. How much of the 2026 shift was caused by events (Mythos, the incidents) rather than research progress? Should the review track incidents as a separate driver?
4. Several 2026 headline results are in direct dispute: midtraining gains, the automated alignment researcher, scheming prevalence. Should agendas carry an explicit "contested" marker?
5. The 2025 lab table showed safety staff at under 5% of headcount at every lab. Is there 2026 evidence that this changed, given that Anthropic raised its risk rating and OpenAI gave a "Critical" rating?
