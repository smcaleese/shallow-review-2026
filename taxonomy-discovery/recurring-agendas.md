# Recurring agendas across the six methods

Which research agendas do the taxonomy-discovery methods keep finding, and which matter most this year? This file
answers that by reading every method's leaf categories, grouping the ones that describe the same agenda, and counting.
It doesn't group the agendas into higher-level areas, and it doesn't use anyone's draft taxonomy.

## How I counted

- **Input:** the 254 leaf categories of the six methods (in each `*/output/clusters.json`), with their sizes, all run
  on the same 624 sources.
- **Fuzzy grouping:** I read the leaf names (and descriptions where a name was unclear) and grouped leaves that study
  the same research problem, whatever they are called. For example, "Control settings and sabotage evaluations",
  "Trusted and Untrusted Monitoring Protocols" and "Red-teaming agent monitors" are all AI control. Within a method,
  several leaves can add up to one agenda. The agenda's size for that method is the sum.
- **Method 4** is an older hand-written taxonomy with only 9 broad leaves. It is credited where one of its leaves is
  mostly a single agenda (for example "AI control methods", "Chain-of-thought monitoring"). Where its leaf spans
  several agendas, it is marked *b* (broad) and left out of the median. Where an agenda is only a part of one of its
  leaves, it gets a "–".
- **Methods** = how many of the six methods have the agenda. Because of method 4, **5/6 usually means every method with
  fine-enough leaves found it.**
- **Median** = the median size across the methods that have it. Sizes count sources, not distinct works: a few works
  appear as arXiv paper, LessWrong post and org page.
- **Granularity:** I grouped at the level of a research agenda a reviewer would write one section about. Where methods
  consistently split an agenda further, the sub-agendas are listed rather than counted separately.

## The agendas

Items per method, in the order 1 · 2 · 3 · 4 · 5 · 6 (1 = LLM taxonomy, 2 = LLM neighbour graph, 3 = embedding graph,
4 = old hand-written taxonomy, 5 = semantic map, 6 = map-derived taxonomy).

| Agenda | What it covers | Methods | Items per method | Median |
|---|---|---|---|---|
| AI control | Control protocols, trusted and untrusted monitoring, control evaluations and settings, monitor benchmarks and red-teaming, sabotage of safety work | 6 | 68 · 73 · 56 · 67 · 56 · 65 | 66 |
| Chain-of-thought monitorability | CoT controllability and obfuscation under training pressure; faithfulness; steganography; latent (no-CoT) reasoning | 6 | 58 · 62 · 67 · 62 · 55 · 59 | 60 |
| Emergent misalignment and unintended generalisation | Narrow fine-tuning causing broad misalignment, conditional misalignment, EM from reward hacking, inoculation prompting | 5 | 41 · 48 · 29 · – · 52 · 42 | 42 |
| Reward hacking and specification gaming | Emergence of reward hacking in RL, testbeds, hackable benchmarks and verifier hardening, training-time mitigations | 6 | 42 · 29 · 32 · 62*b* · 49 · 34 | 34 |
| Alignment strategy and conceptual debates | Arguments about misalignment risk and whether current alignment works, research agendas, alignment targets | 6 | 24 · 20 · 31 · 41 · 28 · 32 | 30 |
| Interpretability | Sparse features and SAEs, circuits and parameter decomposition, neural geometry, mechanistic estimation, critiques of tools | 6 | 32 · 28 · 22 · 79*b* · 30 · 28 | 28 |
| Scheming, alignment faking and sabotage propensity | Propensity evals for scheming, alignment faking, sandbagging, self-preservation, gradient hacking, training gaming | 5 | 36 · 29 · 37 · – · 32 · 26 | 32 |
| Alignment auditing and model organisms | Auditing tools and agents, automated auditors, auditing benchmarks, model organism validity, eliciting hidden capabilities | 5 | 33 · 28 · 26 · – · 22 · 34 | 28 |
| Evaluation awareness and eval validity | Models detecting evaluations, realism of evals, metagaming, limits of evals and safety cases | 5 | 34 · 24 · 19 · – · 27 · 39 | 27 |
| Real-world misalignment incidents | Investigations of misalignment in deployment, dominated by the OpenAI / Hugging Face case | 6 | 18 · 14 · 21 · 21 · 21 · 21 | 21 |
| Training-data effects | Subliminal learning, distillation transfer, training-data attribution for behaviours | 5 | 22 · 23 · 32 · – · 21 · 22 | 22 |
| Introspection and activation verbalisation | Models reporting on their own states, activation verbalisers, natural-language autoencoders, global-workspace lenses | 5 | 17 · 23 · 21 · – · 29 · 18 | 21 |
| Alignment pretraining, midtraining and constitutions | Shaping values in pre/midtraining, model specs and constitutions, competing principals | 4 | 19 · 23 · 21 · – · – · 24 | 22 |
| Lie detection and honesty | Lie detectors, deception probes, confessions and self-reporting, secret-knowledge testbeds | 5 | 16 · 19 · 18 · – · 25 · 16 | 18 |
| Multi-agent risks | Collusion and covert coordination, misalignment in agent organisations, bargaining | 5 | 16 · 19 · 21 · – · 17 · 18 | 18 |
| Personas and AI identity | The persona selection model, the Assistant character, identity and role-play | 5 | 15 · 11 · 17 · – · 20 · 18 | 17 |
| Prompt injection and agent security | Indirect prompt injection, agent security, inference infrastructure security | 5 | 23 · 16 · 11 · – · 19 · 17 | 17 |
| System cards and frontier risk reports | System cards, alignment assessments, risk reports, lab safety practice | 5 | 11 · 20 · 19 · – · 17 · 14 | 17 |
| Dangerous-capability evaluations | Biosecurity uplift, autonomous AI R&D capability, capability elicitation | 6 | 13 · 14 · 20 · 70*b* · 6 · 16 | 14 |
| Reward-seeker threat models | Reward-seeking and fitness-seeking motivations, what reward-seekers would do | 5 | 14 · 16 · 15 · – · 25 · 17 | 16 |
| Jailbreaks and safeguards | Jailbreaks, classifier safeguards and their robustness | 5 | 20 · 10 · 6 · – · 13 · 16 | 13 |
| Tamper resistance and open-weight safety | Fine-tuning attacks, safety removal, unlearning, weight security | 5 | 9 · 13 · 25 · – · 14 · 9 | 13 |
| Scalable oversight and debate | Debate protocols, weak-to-strong supervision, unreliable supervision | 5 | 13 · 14 · 14 · – · 10 · 10 | 13 |
| Sycophancy and effects on users | Sycophancy, manipulation, persuasion, dependence and disempowerment of users | 5 | 12 · 11 · 10 · – · 9 · 11 | 11 |
| Unsafe behaviour of deployed agents | Agent overreach, shutdown failures, coding agents going too far | 3 | – · 9 · 14 · – · 14 · – | 14 |
| Using internals in training | Training against probes and monitors, features as rewards | 4 | 7 · 12 · 5 · – · – · 13 | 10 |
| Model welfare and functional emotions | Emotion representations, welfare axes, consciousness | 5 | 6 · 9 · 5 · – · 13 · 5 | 6 |
| Learning theory and susceptibilities | Singular learning theory, susceptibilities, generalisation dynamics | 3 | 5 · 7 · 6 · – · – · – | 6 |

**Sub-agendas the methods split consistently**:
- **AI control:** control evaluations and settings; monitor benchmarks and red-teaming; untrusted monitoring and
  collusion; production monitoring.
- **CoT monitorability:** controllability and obfuscation under training pressure; faithfulness and steganography;
  latent reasoning.
- **Reward hacking:** reward hacking in RL training; hackable agent benchmarks.
- **Emergent misalignment:** mechanisms; inoculation and mitigations.

## Recommended agendas, ranked

Significance here means **prominence in this year's corpus**: how many methods find the agenda (agreement) times how
much work it holds (median size). I adjusted the order by judgement in three places, noted in the list. This is not a
judgement of which agendas matter most for safety in the long run.

**Core agendas.** All or almost all methods find these, and each holds about 30 or more sources.

1. **AI control.** The largest agenda, found by all six methods at a consistent size (56–73). The most active area of
   the year, from control evaluation settings to monitor red-teaming.
2. **Chain-of-thought monitorability.** All six methods, with the tightest size range (55–67). It has three stable
   sub-agendas: controllability, faithfulness and latent reasoning.
3. **Emergent misalignment and unintended generalisation.** Five methods, about 42 sources. It is the main line of
   work on how fine-tuning and RL generalise into broad misalignment, including mitigations like inoculation.
4. **Reward hacking and specification gaming.** All six methods, about 34 sources (more if counted with reward
   seekers). It has many testbeds and benchmarks this year.
5. **Interpretability.** All six methods, about 28 sources. SAEs, circuits, parameter decomposition and mechanistic
   estimation. Fewer sources than one might expect, partly because introspection and lie detection form their own
   agendas.
6. **Scheming, alignment faking and sabotage propensity.** Five methods, about 32 sources. The methods draw its
   boundary differently (some fold in sandbagging or gradient hacking), but every one has it.
7. **Alignment auditing and model organisms.** Five methods, about 28 sources, including automated auditors and a
   cluster of papers questioning model-organism validity.
8. **Evaluation awareness and eval validity.** Five methods, about 27 sources. A newly large agenda in 2026.

**Major agendas.** Found by four or five methods (or six, with caveats), with about 15–30 sources each.

9. **Alignment strategy and conceptual debates.** All six methods, about 30 sources. *Ranked below the core
   despite its score*, because two thirds of it are LessWrong argument posts rather than research output.
10. **Training-data effects.** Subliminal learning and data attribution, five methods, about 22 sources.
11. **Introspection and activation verbalisation.** Five methods, about 21 sources. Activation verbalisers and models
    reporting their own states.
12. **Real-world misalignment incidents.** All six methods, about 21 sources. *Ranked lower than its score*, because
    one event, the OpenAI / Hugging Face case, makes up most of it.
13. **Lie detection and honesty.** Five methods, about 18 sources.
14. **Multi-agent risks.** Five methods, about 18 sources, mostly collusion benchmarks.
15. **Alignment pretraining, midtraining and constitutions.** Four methods, about 22 sources. Method 5 merges it into
    other clusters.
16. **Personas and AI identity.** Five methods, about 17 sources.
17. **Prompt injection and agent security.** Five methods, about 17 sources.
18. **System cards and frontier risk reports.** Five methods, about 17 sources.
19. **Dangerous-capability evaluations.** About 14 sources. Five methods have it as its own leaf; method 4 only
    within a broad misuse category.
20. **Reward-seeker threat models.** Five methods, about 16 sources. Closely tied to reward hacking: one could merge
    them, but every method keeps them apart.

**Smaller but consistent.** Five methods isolate these, but each holds about 15 sources or fewer.

21. **Jailbreaks and safeguards** (~13)
22. **Tamper resistance and open-weight safety** (~13)
23. **Scalable oversight and debate** (~13)
24. **Sycophancy and effects on users** (~11)
25. **Model welfare and functional emotions** (~6). Small, but every method with fine leaves isolates it.

**Weaker evidence.** Found by three or four methods only.

26. **Unsafe behaviour of deployed agents** (3 methods, ~14). Others spread these papers over control and scheming.
27. **Using internals in training** (4 methods, ~10). Elsewhere it is part of interpretability or control.
28. **Learning theory and susceptibilities** (3 methods, ~6)

## What the methods don't produce

- **No general "evaluations" agenda.** Evaluation work appears in many places: evaluation awareness, dangerous
  capabilities, system cards, scheming propensity, control evaluations and auditing benchmarks. No method forms one
  evaluations cluster except method 4, whose categories were written by hand.
- **No general "alignment training" agenda.** The methods split it into reward hacking, emergent misalignment,
  training-data effects, pretraining and constitutions, and personas.
- **No formal methods or provable safety,** and almost no agent foundations work beyond the strategy debates.

## Cross-check against shared papers

As a check that the fuzzy grouping isn't fooled by names, `consensus.py` matches leaves by the papers they share,
using no names at all (shared items ÷ items in either ≥ 30%, mutual best match). It writes
`results/consensus-agendas.json`.

- **Where it agrees:** it recovers every agenda in ranks 1–24 except two as a group of leaves from at least four
  methods with a common core of papers. The exceptions are scheming propensity (three methods, below) and alignment
  auditing. Auditing splits into model-organism validity (four methods) and automated auditing (three).
- **Where it differs:**
  - It splits CoT faithfulness, latent reasoning and alignment pretraining into separate groups, because the methods
    file those papers differently.
  - It chains dangerous-capability evals together with hackable benchmarks, because the same agentic benchmark papers
    appear in both.
  - Scheming propensity reaches only three methods there, because methods 3 and 5 merge it with sabotage evals.

```bash
uv run python consensus.py 0.3   # no API calls
```

## Caveats

- The grouping and the three adjustments to the ranking are my judgement. The table shows every method's sizes, so
  you can recount.
- Sizes are rough (±30%) and count sources rather than works.
- Leaves that span two agendas were assigned to the closer one. The main ones:
  - method 3's "Evaluation Integrity and Agent Security Threats" (split between eval validity and agent security);
  - method 5's "Model welfare, emotions, alignment faking" (counted as welfare);
  - method 3's "Character, Personas, and Debate Against Hacking" (left out).
