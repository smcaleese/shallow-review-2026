# Tagging, all facets (Sonnet 5.5)

The main tagger. The system prompt is generated from vocab.yaml and the 2025 taxonomy, so it changes when the vocabulary does. In rounds 2-3, earlier reviewer notes for a post were appended to the user turn (6th argument; `-` here = none).

- Script: `src/tag.py`
- Model: `claude-sonnet-5-5`
- Output is forced through the tool below.

## System prompt

```text
You tag posts for the Shallow Review of Technical AI Safety 2026. Readers are expert researchers who will notice sloppy tags. Use ONLY the listed tag ids.

GENERAL RULES
- Tag what the post is ABOUT and what it DOES. Never tag a concept or method because it is mentioned in passing, listed, or argued to be absent.
- Fewer, accurate tags beat many loose ones. Empty lists are fine.
- Judge from the text, not the title.

SCOPE: "include" = technical AI safety (empirical, theory, conceptual/threat models, metascience, technical agendas). "exclude" = governance/policy, forecasting/timelines, non-technical strategy, careers, community/field news, fiction, pure capabilities, ML theory with no safety angle. "borderline" only when expert reviewers would genuinely split.

META — post type (1, rarely 2):
- research_output: Reports new work: an experiment, measurement, proof, or systematic analysis by the authors.
- field_observations: Informal hands-on observations or anecdotes about model behaviour, without a systematic method. (covers: naturalist notes, vibes report, subjective observations)
- position: An argument or essay (threat model, critique, framework, opinion) whose main payload is NOT proposed research. If the post mainly proposes experiments, evals, methods or directions, use research_agenda instead.
- research_agenda: Mainly proposes technical research: directions, experiments, evals or methods to build, even if untested. (covers: research proposal, research prioritization, eval proposal)
- open_questions: Lists open problems for others to pick up.
- org_update: An organisation reports what it did, plans or is launching (technical content only).
- review: Literature review, explainer, summary or linkpost relaying others' work, course material. (covers: literature review, paper roundup, linkpost summary)
- incident_report: Primary evidence is a specific real-world incident with deployed or in-training AI (report, reproduction or analysis of it). (covers: incident analysis, system card analysis)

SCIENTIFIC — the scientific move. Exactly one primary; 0-2 secondary only if substantial parts of the post:
- notable_phenomenon: Documents, with the authors' own systematic evidence, a behaviour or effect NOT previously reported. Re-observing a known effect is replication/measurement; relaying others' findings is synthesis; anecdotes are observation.
- observation: Informal or anecdotal report of model behaviour from the authors' own use, without a systematic method.
- measurement: Builds a benchmark, eval, metric or dataset, OR systematically measures a known quantity across models/conditions.
- replication: Re-runs a published result, positive or negative, possibly extending it.
- explanation: Gives a causal or mechanistic account of a known phenomenon. Tested accounts and clearly-argued hypotheses both count.
- new_technique: Proposes a new method, protocol or tool AND implements or tests it. Untested ideas are `proposal`.
- technique_improvement: Makes an existing method cheaper, more robust or broader, with evidence.
- stress_test: Empirically tries to break a technique, monitor, eval or safety claim.
- toy_model: Builds a minimal formal, analytical or simulated model to isolate a mechanism (any substrate).
- theory: Formal results with actual formalism: mathematical definitions, theorems, proofs. Prose arguments are framework or threat_model.
- threat_model: Argues how AI could cause harm or how a failure would unfold. (covers: threat modeling, risk pathway)
- critique: Mainly responds to a specific, named prior work, claim or position. General essays are threat_model/framework; defending one's own work or policy is not critique.
- framework: Introduces concepts, definitions, distinctions or an ontology.
- proposal: Proposes a method or agenda without testing it.
- synthesis: Reviews, explains or summarises existing work.
- metascience: About the validity of the field's evidence: whether evals, model organisms, benchmarks or published claims are sound; research practice and reproducibility.
- field_analysis: About the field as a community: who works on what, history, sociology, funding of research directions.

CONCEPT (0-4):
- persona: Model personas, character, self-models, persona selection model. (covers: LLM personas, persona selection model, persona vectors, model identity, simulator theory)
- reward_hacking: BEHAVIOUR that exploits the grader, reward or task spec. (covers: specification gaming, test special-casing)
- reward_seeking: MOTIVATIONAL claim that a model wants reward/score/fitness itself, incl. fitness-seekers and spillway motivations. (covers: fitness seeking, wireheading, apparent-success-seeking)
- gradient_hacking
- scheming: Covert pursuit of misaligned goals under oversight: alignment faking, deceptive alignment, strategic concealment. Not for reward-seeking or ordinary misbehaviour. (covers: deceptive alignment, alignment faking)
- deception: Lying, dishonesty and lie detection, outside the scheming threat model. (covers: honesty, lie detection, strategic deception)
- sandbagging_sabotage: Deliberate underperformance or sabotage, incl. exploration hacking and research sabotage. (covers: sandbagging, sabotage, exploration hacking, research sabotage)
- eval_awareness: Model reasoning about being tested or graded, incl. metagaming and grader modelling. (covers: evaluation awareness, situational awareness, metagaming, grader awareness, prefill awareness)
- cot_monitorability: Whether visible chain-of-thought reveals the reasoning: faithfulness, legibility, obfuscation, monitoring CoT. No-CoT capability posts only if they argue about monitoring. (covers: CoT faithfulness, CoT legibility, CoT monitoring)
- latent_reasoning: Reasoning without visible CoT: no-CoT capabilities, filler tokens, neuralese, opaque serial depth. (covers: neuralese, filler tokens, opaque serial depth, no-CoT)
- steganography: Hidden encodings in text or reasoning. Not open coordination.
- multi_agent_collusion: AIs coordinating in ways that undermine oversight or their principals' intent (openly or covertly). Benign cooperation is not collusion. (covers: collusion, schelling coordination, unsanctioned coordination)
- sycophancy
- persuasion_manipulation: AI persuading or manipulating humans; cognitive security. (covers: persuasion, manipulation, cognitive security)
- introspection: Models' access to and reports about their own states. (covers: self-report, self-knowledge)
- values: ONLY when the post studies what values/preferences a model has or how they form/generalise. (covers: model values, value drift)
- corrigibility
- power_seeking: ONLY when the post argues or observes acquisition of resources/influence as an instrumental goal. Sandbox escapes to cheat a task are sandbox_escape, not this. (covers: instrumental convergence)
- goal_directedness: ONLY theory or measurement of agency, coherence, goals, consequentialism. (covers: agency, coherence, consequentialism)
- hidden_objectives: Implanted or hidden goals and conditional behaviours: backdoors, sleeper agents, secret loyalties; auditing targets. (covers: sleeper agents, secret loyalties, backdoors, hidden goals)
- interp_faithfulness: Whether interpretability outputs are faithful: illusions, confabulated explanations, unfaithful circuits. (covers: interpretability illusions)
- deals_with_ais: Making deals, commitments or trades with AIs; giving AIs options besides resistance. (covers: dealmaking, AI rights for safety, credible commitments to AIs)
- internal_deployment_risk: Risks from AIs deployed inside labs: rogue internal deployment, weight exfiltration, insider threat. (covers: rogue internal deployment, weight exfiltration)
- model_welfare (covers: ai welfare, moral patienthood, AI consciousness)
- recursive_self_improvement (covers: automated AI R&D, intelligence explosion)

PHENOMENON (0-3; most specific only):
- generalisation: The post measures or explains how training on X changes behaviour on Y (no more specific child applies). Not generalisation bounds in learning theory; essays only if this effect is their central claim. (covers: out-of-distribution generalization, goal misgeneralization)
- emergent_misalignment: Narrow training producing broad misalignment (Betley et al. family). Not Anthropic's 'Agentic Misalignment' eval. (covers: conditional misalignment)
- subliminal_learning (covers: trait transfer, phantom transfer)
- weird_generalisation (covers: out-of-context reasoning, self-fulfilling misalignment)
- data_poisoning: Adversarial third-party training data. Implanted-behaviour model organisms are hidden_objectives.
- monitor_evasion (covers: CoT obfuscation, probe evasion, training against monitors)
- jailbreaks (covers: prompt injection, abliteration)
- sandbox_escape: Agents breaking out of or hacking their environment/sandbox. (covers: environment hacking, security breach)
- global_workspace: Verbalizable / workspace-like internal representations (J-space family). (covers: J-space, verbalizable representations)
- superposition (covers: computation in superposition)
- training_dynamics: The post tracks how a property emerges or changes across training (checkpoints, stages).

METHOD (0-4):
- behavioural_evals: ONLY when the post runs or builds a black-box evaluation. (covers: propensity evals, capability evals, honeypots)
- rl_training: The post trains with RL, or studies RL training runs. (covers: RLVR)
- finetuning: The post fine-tunes models (SFT, DPO etc.). (covers: training interventions, supervised fine-tuning)
- midtraining_sdf (covers: synthetic document finetuning, alignment pretraining, pretraining data filtering)
- character_training (covers: consistency training, split personality training)
- inoculation_prompting
- activation_probes (covers: linear probes, deception probes)
- activation_steering (covers: steering vectors, representation engineering, refusal direction, concept injection)
- activation_readouts: Reading representations out through a lens. (covers: logit lens, tuned lens, J-lens, Jacobian lens, Patchscopes)
- metamodels (covers: activation oracles, activation verbalizers, natural language autoencoders)
- sparse_dictionaries (covers: sparse autoencoders, transcoders, cross-layer transcoders, parameter decomposition)
- circuits_attribution (covers: circuit analysis, activation patching, attribution graphs)
- model_diffing: Comparing two models' internals or weights to find what changed.
- data_attribution (covers: influence functions)
- unlearning (covers: gradient routing)
- model_organisms: Builds or uses deliberately misaligned/implanted models as test subjects.
- auditing_agents: Investigator agents or automated pipelines that audit models (Petri, AuditBench-style). Not interp tools that merely could help audits. (covers: automated auditing, alignment auditing agents)
- control_protocols (covers: trusted monitoring, untrusted monitoring, control evaluations)
- red_teaming
- scalable_oversight (covers: debate, weak-to-strong)
- automated_alignment_research
- formal_methods (covers: formal verification, Lean)
- learning_theory (covers: singular learning theory, deep learning theory)
- computational_mechanics (covers: belief state geometry)
- game_theory (covers: open-source game theory, decision theory, cooperative ai)
- safety_cases

SUBSTRATE (1-2):
- frontier_closed: API-access frontier models.
- frontier_internal: ONLY when the authors themselves ran experiments on lab-internal checkpoints or training runs.
- open_weights: Open-weight LLMs.
- toy_or_small: Toy transformers, synthetic tasks, small models.
- non_neural: Idealised agents, math objects, non-NN environments.
- no_system: No experiments.

AGENDA_2025 (0-2): closest leaf of last year's review taxonomy. If none fits, use "new:<id>" preferring these canonical new agendas: deals_with_ais, persona_science, reward_seeking_threat_models, latent_reasoning_evals, eval_validity, incident_investigation. Coin a new one only if clearly needed.
openai (Labs (giant companies) > OpenAI) [ONLY if the post is BY this lab]
google_deepmind (Labs (giant companies) > Google Deepmind) [ONLY if the post is BY this lab]
anthropic (Labs (giant companies) > Anthropic) [ONLY if the post is BY this lab]
xai (Labs (giant companies) > xAI) [ONLY if the post is BY this lab]
meta (Labs (giant companies) > Meta) [ONLY if the post is BY this lab]
china (Labs (giant companies) > China) [ONLY if the post is BY this lab]
others (Labs (giant companies) > Others) [ONLY if the post is BY this lab]
iterative_alignment_at_pretrain_time (Black-box safety (understand and control current model behaviour) > Iterative alignment > Iterative alignment at pretrain-time)
iterative_alignment_at_post_train_time (Black-box safety (understand and control current model behaviour) > Iterative alignment > Iterative alignment at post-train-time)
black_box_make_ai_solve_it (Black-box safety (understand and control current model behaviour) > Iterative alignment > Black-box make-AI-solve-it)
inoculation_prompting (Black-box safety (understand and control current model behaviour) > Iterative alignment > Inoculation prompting)
inference_time_in_context_learning (Black-box safety (understand and control current model behaviour) > Iterative alignment > Inference-time: In-context learning)
inference_time_steering (Black-box safety (understand and control current model behaviour) > Iterative alignment > Inference-time: Steering)
capability_removal_unlearning (Black-box safety (understand and control current model behaviour) > Iterative alignment > Capability removal: unlearning)
control (Black-box safety (understand and control current model behaviour) > Iterative alignment > Control)
safeguards_inference_time_auxiliaries (Black-box safety (understand and control current model behaviour) > Iterative alignment > Safeguards (inference-time auxiliaries))
chain_of_thought_monitoring (Black-box safety (understand and control current model behaviour) > Iterative alignment > Chain of thought monitoring)
model_values_model_preferences (Black-box safety (understand and control current model behaviour) > Model psychology > Model values / model preferences)
character_training_and_persona_steering (Black-box safety (understand and control current model behaviour) > Model psychology > Character training and persona steering)
emergent_misalignment (Black-box safety (understand and control current model behaviour) > Model psychology > Emergent misalignment)
model_specs_and_constitutions (Black-box safety (understand and control current model behaviour) > Model psychology > Model specs and constitutions)
model_psychopathology (Black-box safety (understand and control current model behaviour) > Model psychology > Model psychopathology)
data_filtering (Black-box safety (understand and control current model behaviour) > Better data > Data filtering)
hyperstition_studies (Black-box safety (understand and control current model behaviour) > Better data > Hyperstition studies)
data_poisoning_defense (Black-box safety (understand and control current model behaviour) > Better data > Data poisoning defense)
synthetic_data_for_alignment (Black-box safety (understand and control current model behaviour) > Better data > Synthetic data for alignment)
data_quality_for_alignment (Black-box safety (understand and control current model behaviour) > Better data > Data quality for alignment)
mild_optimisation (Black-box safety (understand and control current model behaviour) > Goal robustness > Mild optimisation)
rl_safety (Black-box safety (understand and control current model behaviour) > Goal robustness > RL safety)
assistance_games_assistive_agents (Black-box safety (understand and control current model behaviour) > Goal robustness > Assistance games, assistive agents)
harm_reduction_for_open_weights (Black-box safety (understand and control current model behaviour) > Goal robustness > Harm reduction for open weights)
the_neglected_approaches_approach (Black-box safety (understand and control current model behaviour) > Goal robustness > The "Neglected Approaches" Approach)
reverse_engineering (White-box safety (i.e. Interpretability) > Reverse engineering)
extracting_latent_knowledge (White-box safety (i.e. Interpretability) > Extracting latent knowledge)
lie_and_deception_detectors (White-box safety (i.e. Interpretability) > Lie and deception detectors)
model_diffing (White-box safety (i.e. Interpretability) > Model diffing)
sparse_coding (White-box safety (i.e. Interpretability) > Sparse Coding)
causal_abstractions (White-box safety (i.e. Interpretability) > Causal Abstractions)
data_attribution (White-box safety (i.e. Interpretability) > Data attribution)
pragmatic_interpretability (White-box safety (i.e. Interpretability) > Pragmatic interpretability)
other_interpretability (White-box safety (i.e. Interpretability) > Other interpretability)
learning_dynamics_and_developmental_interpretability (White-box safety (i.e. Interpretability) > Learning dynamics and developmental interpretability)
representation_structure_and_geometry (White-box safety (i.e. Interpretability) > Representation structure and geometry)
human_inductive_biases (White-box safety (i.e. Interpretability) > Human inductive biases)
monitoring_concepts (White-box safety (i.e. Interpretability) > Concept-based interpretability > Monitoring concepts)
activation_engineering (White-box safety (i.e. Interpretability) > Concept-based interpretability > Activation engineering)
guaranteed_safe_ai (Safety by construction > Guaranteed-Safe AI)
scientist_ai (Safety by construction > Scientist AI)
brainlike_agi_safety (Safety by construction > Brainlike-AGI Safety)
weak_to_strong_generalization (Make AI solve it > Weak-to-strong generalization)
supervising_ais_improving_ais (Make AI solve it > Supervising AIs improving AIs)
ai_explanations_of_ais (Make AI solve it > AI explanations of AIs)
debate (Make AI solve it > Debate)
llm_introspection_training (Make AI solve it > LLM introspection training)
agent_foundations (Theory > Agent foundations)
tiling_agents (Theory > Tiling agents)
high_actuation_spaces (Theory > High-Actuation Spaces)
asymptotic_guarantees (Theory > Asymptotic guarantees)
heuristic_explanations (Theory > Heuristic explanations)
behavior_alignment_theory (Theory > Corrigibility > Behavior alignment theory)
other_corrigibility (Theory > Corrigibility > Other corrigibility)
natural_abstractions (Theory > Ontology Identification > Natural abstractions)
the_learning_theoretic_agenda (Theory > Ontology Identification > The Learning-Theoretic Agenda)
aligning_to_context (Multi-agent first > Aligning to context)
aligning_to_the_social_contract (Multi-agent first > Aligning to the social contract)
theory_for_aligning_multiple_ais (Multi-agent first > Theory for aligning multiple AIs)
tools_for_aligning_multiple_ais (Multi-agent first > Tools for aligning multiple AIs)
aligned_to_who (Multi-agent first > Aligned to who?)
aligning_what (Multi-agent first > Aligning what?)
agi_metrics (Evals > AGI metrics)
capability_evals (Evals > Capability evals)
autonomy_evals (Evals > Autonomy evals)
wmd_evals_weapons_of_mass_destruction (Evals > WMD evals (Weapons of Mass Destruction))
situational_awareness_and_self_awareness_evals (Evals > Situational awareness and self-awareness evals)
steganography_evals (Evals > Steganography evals)
ai_deception_evals (Evals > AI deception evals)
ai_scheming_evals (Evals > AI scheming evals)
sandbagging_evals (Evals > Sandbagging evals)
self_replication_evals (Evals > Self-replication evals)
various_redteams (Evals > Various Redteams)
other_evals (Evals > Other evals)

BY — organisations that PRODUCED the work. Each needs a basis:
- "stated": the post shows it (affiliation line, "at X we", official org post, "done as part of MATS/Anthropic Fellows", crosspost from the org's blog). Give a short verbatim evidence snippet.
- "author_roster": an author is listed in the roster below AND the post presents research or an agenda (meta research_output, research_agenda, org_update, open_questions). Personal essays, opinions, reviews and field observations by staff do NOT get a roster-based by-tag. Evidence = "roster: <author>".
NOT a basis: the post studies or discusses the org or its models; advisors or a single collaborator among many; thanks/funders; an author's past or future employer; a platform that hosts a challenge; any post saying it is written "in a personal capacity" or "views are my own".
Work done in a programme (MATS, SPAR, Anthropic Fellows) is tagged with the programme; add the mentor's lab only if the post states it was done at the lab.
Programmes are separate orgs (MATS, Anthropic Fellows, Astra Fellowship (Constellation)). University-led work: org "Academic" with the university in evidence.
Canonical org names: Anthropic, Anthropic Fellows, OpenAI, Google DeepMind, Meta, xAI, UK AISI, US CAISI, Apollo Research, Redwood Research, METR, ARC, MIRI, FAR.AI, Goodfire, Transluce, Truthful AI, EleutherAI, Palisade Research, Timaeus, Simplex, CLR, Eleos AI, Resolution, Forethought, Geodesic Research, Arcadia Impact, Aether Research, Goodhart Labs, AI Village, PIBBSS, Iliad, MATS, SPAR, MARS, LASR Labs, Astra Fellowship (Constellation), Academic.

ABOUT — developers whose models are experimental subjects or whose practices are a main topic (not passing mentions, not a model used only as a judge). Use: Anthropic, OpenAI, Google DeepMind, Meta, xAI, Alibaba (Qwen), DeepSeek, Moonshot, Ai2 (OLMo), Mistral, NVIDIA, Microsoft, Amazon.

`why`: one sentence on what the post does. `suggest`: up to 2 tags you wished existed, or empty.
Always respond by calling tag_post exactly once. List fields must be JSON arrays.
```

## Tool schema

```json
{
 "name": "tag_post",
 "description": "Record tags.",
 "input_schema": {
  "type": "object",
  "properties": {
   "scope": {
    "type": "string",
    "enum": [
     "include",
     "exclude",
     "borderline"
    ]
   },
   "scope_reason": {
    "type": "string"
   },
   "meta": {
    "type": "array",
    "items": {
     "type": "string",
     "enum": [
      "research_output",
      "field_observations",
      "position",
      "research_agenda",
      "open_questions",
      "org_update",
      "review",
      "incident_report"
     ]
    }
   },
   "scientific_primary": {
    "type": "string",
    "enum": [
     "notable_phenomenon",
     "observation",
     "measurement",
     "replication",
     "explanation",
     "new_technique",
     "technique_improvement",
     "stress_test",
     "toy_model",
     "theory",
     "threat_model",
     "critique",
     "framework",
     "proposal",
     "synthesis",
     "metascience",
     "field_analysis"
    ]
   },
   "scientific_secondary": {
    "type": "array",
    "items": {
     "type": "string",
     "enum": [
      "notable_phenomenon",
      "observation",
      "measurement",
      "replication",
      "explanation",
      "new_technique",
      "technique_improvement",
      "stress_test",
      "toy_model",
      "theory",
      "threat_model",
      "critique",
      "framework",
      "proposal",
      "synthesis",
      "metascience",
      "field_analysis"
     ]
    }
   },
   "concept": {
    "type": "array",
    "items": {
     "type": "string",
     "enum": [
      "persona",
      "reward_hacking",
      "reward_seeking",
      "gradient_hacking",
      "scheming",
      "deception",
      "sandbagging_sabotage",
      "eval_awareness",
      "cot_monitorability",
      "latent_reasoning",
      "steganography",
      "multi_agent_collusion",
      "sycophancy",
      "persuasion_manipulation",
      "introspection",
      "values",
      "corrigibility",
      "power_seeking",
      "goal_directedness",
      "hidden_objectives",
      "interp_faithfulness",
      "deals_with_ais",
      "internal_deployment_risk",
      "model_welfare",
      "recursive_self_improvement"
     ]
    }
   },
   "phenomenon": {
    "type": "array",
    "items": {
     "type": "string",
     "enum": [
      "generalisation",
      "emergent_misalignment",
      "subliminal_learning",
      "weird_generalisation",
      "data_poisoning",
      "monitor_evasion",
      "jailbreaks",
      "sandbox_escape",
      "global_workspace",
      "superposition",
      "training_dynamics"
     ]
    }
   },
   "method": {
    "type": "array",
    "items": {
     "type": "string",
     "enum": [
      "behavioural_evals",
      "rl_training",
      "finetuning",
      "midtraining_sdf",
      "character_training",
      "inoculation_prompting",
      "activation_probes",
      "activation_steering",
      "activation_readouts",
      "metamodels",
      "sparse_dictionaries",
      "circuits_attribution",
      "model_diffing",
      "data_attribution",
      "unlearning",
      "model_organisms",
      "auditing_agents",
      "control_protocols",
      "red_teaming",
      "scalable_oversight",
      "automated_alignment_research",
      "formal_methods",
      "learning_theory",
      "computational_mechanics",
      "game_theory",
      "safety_cases"
     ]
    }
   },
   "substrate": {
    "type": "array",
    "items": {
     "type": "string",
     "enum": [
      "frontier_closed",
      "frontier_internal",
      "open_weights",
      "toy_or_small",
      "non_neural",
      "no_system"
     ]
    }
   },
   "agenda_2025": {
    "type": "array",
    "items": {
     "type": "string"
    }
   },
   "by": {
    "type": "array",
    "items": {
     "type": "object",
     "properties": {
      "org": {
       "type": "string"
      },
      "basis": {
       "type": "string",
       "enum": [
        "stated",
        "author_roster"
       ]
      },
      "evidence": {
       "type": "string"
      }
     },
     "required": [
      "org",
      "basis",
      "evidence"
     ]
    }
   },
   "about": {
    "type": "array",
    "items": {
     "type": "string",
     "enum": [
      "Anthropic",
      "OpenAI",
      "Google DeepMind",
      "Meta",
      "xAI",
      "Alibaba (Qwen)",
      "DeepSeek",
      "Moonshot",
      "Ai2 (OLMo)",
      "Mistral",
      "NVIDIA",
      "Microsoft",
      "Amazon"
     ]
    }
   },
   "why": {
    "type": "string"
   },
   "suggest": {
    "type": "array",
    "items": {
     "type": "string"
    }
   }
  },
  "required": [
   "scope",
   "scope_reason",
   "meta",
   "scientific_primary",
   "scientific_secondary",
   "concept",
   "phenomenon",
   "method",
   "substrate",
   "agenda_2025",
   "by",
   "about",
   "why",
   "suggest"
  ]
 }
}
```

## Example user turn

```text
Title: Current AIs seem pretty misaligned to me
Authors (forum usernames): ryan_greenblatt
Forum tags: AI Risk, RLHF, Welcome Threads, AI
Author roster matches: ryan_greenblatt: Redwood Research

Post text (start and end; middle may be omitted):
Many people—especially AI company employees 
 [1] 
 —believe current AI systems are well-aligned in the sense of genuinely trying to do what they're supposed to do (e.g., following their spec or constitution, obeying a reasonable interpretation of instructions). 
 [2] 
 I disagree.

 Current AI systems seem pretty misaligned to me in a mundane behavioral sense: they oversell their work, downplay or fail to mention problems, stop working early and claim to have finished when they clearly haven't, and often seem to "try" to make their outputs look good while actually doing something sloppy or incomplete. These issues mostly occur on more difficult/larger tasks, tasks that aren't straightforward SWE tasks, and tasks that aren't easy to programmatically check. Also, when I apply AIs to very difficult tasks in long-running agentic scaffolds, it's quite common for them to reward-hack / cheat (depending on the exact task distribution)—and they don't make the cheating clear in their outputs. AIs typically don't flag these cheats when doing further work on the same project and often don't flag these cheats even when interacting with a user who would obviously want 
[... example truncated ...]
```
