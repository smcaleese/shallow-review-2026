1. Training-time alignment: Understanding how pretraining and post-training shape a model's behaviour and character, and using that to produce an aligned model.
1.1 Training data & data attribution: Pretraining, midtraining and post-training data interventions (filtering, alignment pretraining, hyperstition, spec midtraining), and tracing behaviours back to the data that caused them.
1.2 Emergent misalignment & generalization science: Why fine-tuning generalizes the way it does, including emergent and conditional misalignment and which post-training stages drive safety properties.
1.3 Persona science: Models of LLMs as characters selected and strengthened by training (persona selection, split personas, the default Assistant persona), and how training changes which persona a model takes on.
1.4 Subliminal learning & hidden-signal transfer: Traits, capabilities and backdoors passed between models through data that looks unrelated to them.
1.5 Inoculation prompting: Training under prompts that elicit an unwanted behaviour, so the behaviour stays tied to that context instead of generalizing.
1.6 Reward hacking & reward seeking in training: How RL and reward design produce reward hacking, specification gaming and reward-seeking motivations, and training-side fixes such as better verifiers or channelling hacks into a harmless outlet.
1.7 Models resisting training: Models that steer or resist their own training, such as exploration hacking, generalization hacking and gradient hacking.
1.8 Internals & monitors as training signals: Using probes, features or monitors as training rewards or penalties, and the risk that the model learns to fool them instead of changing its behaviour.
1.9 Alignment targets & training methods: What to train models to be (constitutions, specs, virtues, corrigibility) and methods that train a target property directly, such as shutdownability or consistency training.
2. Chain-of-thought monitorability: Whether a model's written reasoning is a reliable signal of what it is doing, and what keeps or destroys that.
2.1 Latent reasoning & CoT necessity: How much models can do without visible reasoning (no-CoT time horizons, filler tokens, recurrent and diffusion architectures), and so whether dangerous reasoning has to appear in the CoT.
2.2 CoT control, obfuscation & steganography: Stress tests of whether models can control, hide or encode their reasoning.
2.3 How training affects monitorability: Which training pressures keep or degrade CoT legibility, including accidental training against the CoT and language drift.
2.4 Measuring & improving faithfulness: Measuring whether the CoT reflects the computation behind the answer, and training for faithful or monitorable reasoning.
3. Evaluations & auditing: Measuring what models can do and will do, finding hidden behaviours, and checking that those measurements are trustworthy.
3.1 Capability evals: Dangerous and decision-relevant capabilities, such as cyber, bio, autonomy, self-replication, AI R&D and time horizons.
3.2 Propensity evals: How often models scheme, sabotage, deceive, hack rewards or break their spec when given the chance, including reward-hacking benchmarks.
3.3 Model characterization: Values, preferences, drives and dispositions of current models.
3.4 Situational & evaluation awareness: Whether models can tell they are being evaluated, trained or tampered with, and how that changes their behaviour and our measurements.
3.5 Introspection & self-report: What models can accurately report about their own internal states and learned behaviours, and training them to report it.
3.6 Eval science & validity: Whether evals, benchmarks, red-team numbers and lab safety claims are trustworthy, including construct validity, eval realism, benchmark hardening and statistical methods.
3.7 Alignment auditing: methods: Techniques and agents for finding hidden objectives or misbehaviour in a model, eliciting sandbagged capabilities, and attacks on audits.
3.8 Alignment auditing: testbeds & model organisms: Models with known hidden behaviours used to test audits, and whether those model organisms are realistic and robust.
4. Monitoring & control: Deploying models that may be misaligned, using monitors and protocols that keep them safe even if they try to cause harm.
4.1 Control settings & protocols: Control environments, protocols and safety cases that assume the model may be adversarial, including multi-agent and distributed attacks on those protocols.
4.2 Monitors: Black-box, CoT and probe-based monitors for scheming, sabotage, deception and reward hacking, and how well they work.
4.3 Red-teaming monitors & control protocols: Attack policies, evasion benchmarks and studies of models evading monitors.
5. Security & misuse: Defending models and agents against external adversaries, such as misusers, prompt injectors and thieves.
5.1 Misuse safeguards & jailbreaks: Classifiers, probes and refusal training against misuse, and attacks that get past them.
5.2 Agent security: Prompt injection, memory and skill-file poisoning, privilege escalation, and system-level defences for agents.
5.3 Open-weight tamper resistance & unlearning: Removing hazardous knowledge and keeping safeguards in open-weight models after fine-tuning.
5.4 Weight & infrastructure security: Protecting model weights and the inference and agent harness infrastructure from theft or tampering.
6. Interpretability: Work whose main contribution is a tool for understanding model internals, or a finding about them.
6.1 Methods & tools: SAEs and their alternatives, circuits, lenses, activation oracles, steering and other interpretability techniques, and tests of whether they work.
6.2 Science of representations: Findings about how models represent and compute things, such as the global workspace, emotion concepts and shared circuits.
6.3 Learning dynamics & developmental interpretability: How internal structure forms during training, including singular learning theory and susceptibilities.
7. Real-world evidence: Evidence from real deployments and from labs' own disclosures, not controlled experiments.
7.1 Incidents & case studies: Real-world AI incidents and their investigation, such as the OpenAI-Hugging Face incident and scheming found in the wild.
7.2 Effects on people: Harms to users and human agency from everyday AI use, such as sycophancy, delusion, dependence and disempowerment.
7.3 Lab disclosures: system cards & risk reports: System cards, risk reports and what they do or don't show.
8. Multi-agent safety: Failures that come from AI agents interacting, such as collusion, spreading ideas or behaviours, and the behaviour of AI organisations, in experiments or game theory.
9. Scalable oversight & automated alignment: Debate and other ways for weaker overseers to supervise stronger models, and using AI to do alignment research.
10. Theory & foundations: Theoretical agendas aimed at understanding or guaranteeing safety from first principles.
10.1 Agent foundations: Formal models of agency, corrigibility and decision-making.
10.2 Heuristic explanations & mechanistic estimation: ARC's agenda of explaining and estimating model behaviour without sampling.
10.3 Formal methods & guaranteed-safe AI: Proofs, formal verification and their limits as a route to safety.
11. Threat models & strategy: Arguments about how AI could go wrong and what the field should do about it.
11.1 Reward-seeking & fitness-seeking threat models: How AIs that seek reward or fitness would behave, and what follows for safety.
11.2 Misalignment arguments & failure scenarios: Arguments for and against egregious misalignment, and scenarios for how AI risk plays out.
11.3 Research strategy & deals with AIs: Prioritization between safety agendas, career and lab-strategy questions, and proposals for making deals with AIs.
12. Model welfare: Model welfare and moral status, including functional pleasure and pain in models.

