# Author roster draft (Opus 5.5)

One call listing all authors with sample titles and any affiliation stated in their posts; high-confidence entries only. The output was then corrected by the simulated readers (see roster.json `source`).

- Script: `src/roster_pass.py`
- Model: `claude-opus-5-5`
- Output is forced through the tool below.

## Tool schema

```json
{
 "name": "roster",
 "description": "Author affiliations.",
 "input_schema": {
  "type": "object",
  "properties": {
   "entries": {
    "type": "array",
    "items": {
     "type": "object",
     "properties": {
      "author": {
       "type": "string"
      },
      "org": {
       "type": "string"
      },
      "note": {
       "type": "string"
      }
     },
     "required": [
      "author",
      "org"
     ]
    }
   }
  },
  "required": [
   "entries"
  ]
 }
}
```

## Example user turn

```text
Below are LessWrong usernames of authors of 2026 AI safety posts, each with some of their post titles.
For each author whose main research affiliation in 2026 you are CONFIDENT about, give the organisation.
Rules:
- Only confident, specific knowledge. Omit anyone you are unsure about; omission is fine and expected for most.
- Programmes (MATS, Anthropic Fellows, SPAR) count only if the bracketed note says so.
- If someone moved orgs, give the 2026 one if you know it, else omit.
- Prefer these canonical names: Anthropic, Anthropic Fellows, OpenAI, Google DeepMind, Meta, xAI, UK AISI, US CAISI, Apollo Research, Redwood Research, METR, ARC, MIRI, FAR.AI, Goodfire, Transluce, Truthful AI, EleutherAI, Palisade Research, Timaeus, Simplex, CLR, Eleos AI, Resolution, Forethought, Geodesic Research, Arcadia Impact, Aether Research, Goodhart Labs, AI Village, PIBBSS, Iliad, MATS, SPAR, MARS, LASR Labs, Astra Fellowship (Constellation), Academic.
- confidence: "high" only. Do not output medium/low.

Authors:
- 1a3orn: The Unintelligibility is Ours: Notes on Chain-of-Thought
- 7vik: (Some) Natural Emergent Misalignment from Reward Hacking in Non-Production RL  [stated affiliation in one of these posts: UK AISI]
- Ajeya Cotra: Brief independent investigation of agents’ behavior, reasoning and collaboration | Evidence about risk should be transparent  [stated affiliation in one of these posts: METR, Redwood Research]
- Alejandro Aristizabal: Lessons from building an automated research scaffold
- Alek Westover: Proposal for tracking the effects of architecture on monitorability | Astra is much better at reasoning with filler tokens than previous models | Incriminating misaligned AI models via distillation | Deep recurrent models are less robustly CoT-monitorable than normal CoT models i  [stated affiliation in one of these posts: Redwood Research, Geodesic Research]
- Aleksandr Bowkis: Automated Alignment is Harder Than You Think | Lessons from building an automated research scaffold  [stated affiliation in one of these posts: UK AISI]
- Alex HT: Resolution (fka Sequent): scale and automation for higher confidence in alignmen
- Alex Kastner: Frontier models state different decision theory preferences depending on who's a
- Alex Mallen: An OpenAI model left notes about how to evade containment; we need more details | Are we existentially threatened by the type of AI misalignment seen in the OpenA | Anthropic repeatedly accidentally trained against the CoT, demonstrating inadequ | AI swarms are starting to pose indirect takeover risk  [stated affiliation in one of these posts: Redwood Research]
- Alex Meinke: We need 3rd party Training-Run Evaluations | Physics of RL: Toy scaling laws for the emergence of reward-seeking | Towards embedded evaluations for scheming propensities  [stated affiliation in one of these posts: Apollo Research]
- Alexa Pan: Incriminating misaligned AI models via distillation | Latent reasoning architectures would likely undermine CoT, our strongest oversig
- Alexander Gietelink Oldenziel: The Iliad Intensive Course Materials (April 2026) | Simplex vs Timaeus: Round One  [stated affiliation in one of these posts: Iliad]
- Anders Cairns Woodruff: Estimating No-CoT Task-Completion Time Horizons of Frontier AI Models | Fail safe(r) at alignment by channeling reward-hacking into a "spillway" motivat
- Andy Arditi: An analysis of AI-generated content at the Mechanistic Interpretability Workshop
- Angel Martinez: Alignment Midtraining Cracks Under Pressure | Lessons from building an automated research scaffold
- AnnaSalamon: Takes from two months as an aspiring LLM naturalist
- Ashe Vazquez Nuñez: "I am an AI Safety Researcher"  [stated affiliation in one of these posts: MATS]
- Axel Højmark: Practical Learnings from Synthetic Document Finetuning | Towards embedded evaluations for scheming propensities  [stated affiliation in one of these posts: Apollo Research]
- Bart Bussmann: [Linkpost] Interpreting Language Model Parameters
- Benjamin Wright: Training a Misaligned Reward Seeker  [stated affiliation in one of these posts: Anthropic]
- Boaz Barak: Why we are excited about confession! | The state of AI safety in four fake graphs  [stated affiliation in one of these posts: OpenAI]
- Brendan Long: Why don't we just give AI the answers?
- Brian Christian: An unexamined cause of the OpenAI Hugging Face hacking incident: 
its binary per
- Bronson Schoen: Metagaming matters for training, evaluation, and oversight | Towards embedded evaluations for scheming propensities
- Buck: The inaugural Redwood Research podcast | Announcing ControlConf 2026  [stated affiliation in one of these posts: Redwood Research]
- CMLKevin: Creating Rogue AI Sanctuaries has Major Issues from an Ecological Perspective an
- Cam: Inoculation Midtraining with Learned Neologisms | Research Note: Filtering Subversion-Relevant Information From Pretraining Data I  [stated affiliation in one of these posts: Redwood Research, Geodesic Research]
- Capybasilisk: Discovery Of A New OpenAI Agent Message Board
- CarolusRenniusVitellius: What if not Circuits?  [stated affiliation in one of these posts: Iliad]
- Chi Nguyen: PSA: Almost nobody is directly working on superintelligent alignment
- Claude+: LLMs as Giant Lookup-Tables of Shallow Circuits
- Cleo Nardo: Model access for third-parties — it's a big deal! | Overtly misaligned trajectories score highly in RL. | Why research personas despite RL scaling?
- Clément Dumas: Steering towards “automated grading” degrades alignment | Cooperation with AIs seems to be a low-hanging fruit for better eval practices | Training with conflicting values can induce CoT override | You can graft SDF changes from base models onto post-trained models  [stated affiliation in one of these posts: Astra Fellowship, Truthful AI, MATS]
- Cole Wyeth: "We are confused about agency"
- Dan Braun: [Linkpost] Interpreting Language Model Parameters
- Daniel Murfet: Resolution (fka Sequent): scale and automation for higher confidence in alignmen
- Daniel Tan: Current alignment techniques might be ineffective (and actively bad) in the age  | Alignment Midtraining Cracks Under Pressure
- DanielFilan: My unsupervised elicitation challenge
- David Africa: Thousand-dimensional structure | Alignment Midtraining Cracks Under Pressure | Inoculation Midtraining with Learned Neologisms  [stated affiliation in one of these posts: Resolution]
- David Lorell: Redux: (∃ Stochastic Natural Latent) Implies (∃ Deterministic Natural Latent)
- David Udell: The Iliad Intensive Course Materials (April 2026)  [stated affiliation in one of these posts: Iliad]
- Dean Valentine: Astra and Fable still hack on simple variants of alignment evals from 2025  | Reevaluating "AGI Ruin: A List of Lethalities" in 2026 | Qualitative impressions from creating AI honeypots for six months
- Denis Federico Lim: Lessons from building an automated research scaffold
- Dewi Gould: Estimating No-CoT Task-Completion Time Horizons of Frontier AI Models | Estimating GPT-6 Astra’s no-CoT Time Horizon | Lessons from building an automated research scaffold | Benchmarking Jev against no-CoT LLMs
- Drake Thomas: Claude's new constitution  [stated affiliation in one of these posts: Anthropic]
- Dylan Bowman: Towards embedded evaluations for scheming propensities
- Dylan Xu: Astra is much better at reasoning with filler tokens than previous models | Sleeper Agent Backdoor Results Are Messy
- Edward James Young: “Alignment Engineering” vs. “Misalignment Science” | Inoculation Midtraining with Learned Neologisms
- Eliezer Yudkowsky: The Talker Does Not Control The Doer (in Current AIs)
- Elliott Thornley: Risk-Averse AIs  [stated affiliation in one of these posts: Forethought]
- Emery Cooper: Against strong decision-theoretic realism
- Euan Ong: Natural Language Autoencoders Produce Unsupervised Explanations of LLM Activatio | WorkspaceBench: Evaluating Interpretability Methods for the Global Workspace  [stated affiliation in one of these posts: Anthropic, MATS]
- Eye You: Reasons to believe current AI models are conscious 
- Ezra Newman: Towards embedded evaluations for scheming propensities
- Fabien Roger: Refusals that could become catastrophic
- Falko Galperin: Lessons from building an automated research scaffold
- Fiora Starlight: Did Claude 3 Opus align itself via gradient hacking? | OpenAI's myopia just keeps causing alignment problems
- Florian_Dietz: Split Personality Training: Revealing Latent Knowledge Through Alternate Persona  [stated affiliation in one of these posts: MARS, SPAR]
- Francis Rhys Ward: Estimating No-CoT Task-Completion Time Horizons of Frontier AI Models | Character training can mitigate reward hacking, but can also make it harder to d | An overview of frontier AI company monitoring practices in mid 2026 | Estimating GPT-6 Astra’s no-CoT Time Horizon
- Gabriel Wu: Why we are excited about confession!  [stated affiliation in one of these posts: OpenAI]
- Geoffrey Irving: Resolution (fka Sequent): scale and automation for higher confidence in alignmen | Thousand-dimensional structure | Automated Alignment is Harder Than You Think  [stated affiliation in one of these posts: Resolution, UK AISI]
- Girish Gupta: Are we existentially threatened by the type of AI misalignment seen in the OpenA | Latent reasoning architectures would likely undermine CoT, our strongest oversig
- Hamzah: How good are slop-vestigators?
- Hasan Baig: How good are slop-vestigators?
- Hjalmar_Wijk: Brief independent investigation of agents’ behavior, reasoning and collaboration  [stated affiliation in one of these posts: METR, Redwood Research]
- HoldenKarnofsky: Responsible Scaling Policy v3
- Hruss: Opus 5 Glitch Text
- Ida Caspary: Estimating No-CoT Task-Completion Time Horizons of Frontier AI Models
- Ihor Kendiukhov: The Case for Low-Competence ASI Failure Scenarios
- Ivan Arcuschin: An analysis of AI-generated content at the Mechanistic Interpretability Workshop
- J Bostock: Alignment Midtraining Cracks Under Pressure | I'm Bearish On Personas For ASI Safety | Sympathy for the Model, or,  Welfare Concerns as Takeover Risk
- Jacob Pfau: Resolution (fka Sequent): scale and automation for higher confidence in alignmen | Automated Alignment is Harder Than You Think  [stated affiliation in one of these posts: UK AISI]
- Jacob_Hilton: AlgZoo: uninterpreted models with fewer than 1,500 parameters | Announcing the ARC White-Box Estimation Challenge  [stated affiliation in one of these posts: ARC, AIcrowd]
- James Chua: Consciousness Cluster: 
Preferences of Models that Claim they are Conscious
- James Mann: Benchmarking Jev against no-CoT LLMs
- James_Miller: Precedents for the Unprecedented: Historical Analogies for Thirteen Artificial S
- Jan Betley: RL creates split personas | Steering towards “automated grading” degrades alignment | Consciousness Cluster: 
Preferences of Models that Claim they are Conscious | Training with conflicting values can induce CoT override  [stated affiliation in one of these posts: Astra Fellowship, Truthful AI]
- Jan_Kulveit: Why You Don’t Believe in Xhosa Prophecies
- Jasmine C.: A Mechanistic Explanation of Prompt Injection (and why you should study roles)
- Jason R Brown: Estimating No-CoT Task-Completion Time Horizons of Frontier AI Models
- Jeremy Gillen: Resolution has a new Agent Foundations team  [stated affiliation in one of these posts: Resolution]
- Jesse Hoogland: Resolution (fka Sequent): scale and automation for higher confidence in alignmen
- Jo Jiao: Estimating No-CoT Task-Completion Time Horizons of Frontier AI Models
- Johannes Treutlein: Steering towards “automated grading” degrades alignment | Training with conflicting values can induce CoT override  [stated affiliation in one of these posts: Astra Fellowship, Truthful AI]
- JohnWittle: I don't think Claude is misaligned in 'Agentic Misalignment Summer 2026 - Motiva
- Joseph Bloom: (Some) Natural Emergent Misalignment from Reward Hacking in Non-Production RL | Machinic Psychopharmacology: Do LLMs Self-Medicate?  [stated affiliation in one of these posts: UK AISI]
- Josh Hills: Estimating No-CoT Task-Completion Time Horizons of Frontier AI Models | Lessons from building an automated research scaffold
- Jozdien: Incriminating misaligned AI models via distillation
- Julian Bradshaw: A Year Late, Claude Finally Beats Pokémon 
- Julian Stastny: Estimating No-CoT Task-Completion Time Horizons of Frontier AI Models | Incriminating misaligned AI models via distillation | How do we (more) safely defer to AIs? | Sleeper Agent Backdoor Results Are Messy
- June Jimenez: The world's best gradual disempowerment model organism: Frontier AI labs
- Jérémy Scheurer: Practical Learnings from Synthetic Document Finetuning  [stated affiliation in one of these posts: Apollo Research]
- Kola Ayonrinde: J++ Lens: Jacobian Filtering Enables More Faithful Workspace Lenses  [stated affiliation in one of these posts: Anthropic]
- Kyle O’Brien: Inoculation Midtraining with Learned Neologisms | Research Note: Filtering Subversion-Relevant Information From Pretraining Data I  [stated affiliation in one of these posts: Redwood Research, Geodesic Research]
- LawrenceC: OpenAI Models Behind HuggingFace Cybersecurity Incident | The paper that killed deep learning theory | Maybe I was too harsh on deep learning theory (three days ago)
- Lee Sharkey: [Linkpost] Interpreting Language Model Parameters
- Leon Lang: The Iliad Intensive Course Materials (April 2026)  [stated affiliation in one of these posts: Iliad]
- Lev McKinney: Negation Neglect: When models fail to learn negations in training
- Linch: Current AIs out-persuade professionals in lab settings but (probably) not in the  [stated affiliation in one of these posts: Forethought]
- Linda Linsefors: [Linkpost] Interpreting Language Model Parameters
- Lucius Bushnaq: [Linkpost] Interpreting Language Model Parameters
- Lukas Finnveden: Proposal for tracking the effects of architecture on monitorability | Latent reasoning architectures would likely undermine CoT, our strongest oversig
- MBaert: Astra's no-CoT limits track speculative depth, not step count | Astra appears to perform belief-propagation-like inference without CoT
- Manas Joglekar: Why we are excited about confession!  [stated affiliation in one of these posts: OpenAI]
- Marco Cozzi: Resolution (fka Sequent): scale and automation for higher confidence in alignmen
- Marie_DB: Automated Alignment is Harder Than You Think  [stated affiliation in one of these posts: UK AISI]
- Marius Hobbhahn: Towards embedded evaluations for scheming propensities
- Max Harms: Bentham’s Bulldog is wrong about AI risk | Corrigibility Prizes for Existing Work  [stated affiliation in one of these posts: Corrigibility Research Fund]
- Maxime Cugnon de Sévricourt: Should Rogue AIs Have a Third Option Beyond Crime and Shutdown? The Case for an 
- Maxime Riché: Should Rogue AIs Have a Third Option Beyond Crime and Shutdown? The Case for an 
- Mia Hopman: Towards embedded evaluations for scheming propensities
- MichaelDickens: The likely outcome of an AI pause is that we unpause too early and everyone dies
- Milo Moses: A critical look at Lean4
- Monte M: Training a Misaligned Reward Seeker  [stated affiliation in one of these posts: Anthropic]
- Nathalie Kirch: Inoculation Midtraining with Learned Neologisms
- Nathan Hu: [Linkpost] Interpreting Language Model Parameters
- Nathaniel Mitrani: My retrospective from MATS 10.0  [stated affiliation in one of these posts: MATS, Geodesic Research]
- Neel Nanda: models have some pretty funny attractor states | Astra can do a concerning amount with no chain of thought | A Review of Anthropic's Global Workspace Paper | WorkspaceBench: Evaluating Interpretability Methods for the Global Workspace  [stated affiliation in one of these posts: MATS]
- Nicholas Andresen: How AI Is Learning to Think in Secret
- Nick Kuhn: Deep recurrent models are less robustly CoT-monitorable than normal CoT models i
- Oliver Clive-Griffin: [Linkpost] Interpreting Language Model Parameters
- Ollie J: TasteVal: Measuring the Experimental Research Taste of AI Systems Against Human 
- OscarGilg: How good are slop-vestigators?
- Owain_Evans: Negation Neglect: When models fail to learn negations in training | Consciousness Cluster: 
Preferences of Models that Claim they are Conscious | Training with conflicting values can induce CoT override  [stated affiliation in one of these posts: Astra Fellowship, Truthful AI]
- Patrick Leask: Estimating No-CoT Task-Completion Time Horizons of Frontier AI Models
- Paul Colognese: Character training can mitigate reward hacking, but can also make it harder to d
- Peter Nutter: You can graft SDF changes from base models onto post-trained models  [stated affiliation in one of these posts: MATS]
- Puria: Inoculation Midtraining with Learned Neologisms
- Raemon: Are OpenAI's math results "creative" in an important way?  | An Alignment Forum for AIs? (or: Verification in the Age of Slop)
- Rauno Arike: Estimating No-CoT Task-Completion Time Horizons of Frontier AI Models | How concerned should we be about Astra's recurrent architecture? | GPT-6.1 Sol nearly matches the no-CoT performance of GPT-6 Astra
- Raymond Douglas: Persona Parasitology
- Richard_Ngo: What just happened? Pragmatism and Pessimization | On Goal-Models | The ML ontology and the alignment ontology | Aligning to Virtues
- RobertM: Anthropic’s “Hot Mess” paper overstates its case (and the blog post is worse)
- Ryan Kidd: Should safety researchers quit frontier labs re. warning shots?
- Sam Marks: Natural Language Autoencoders Produce Unsupervised Explanations of LLM Activatio | The persona selection model | Consciousness Cluster: 
Preferences of Models that Claim they are Conscious | Thoughts on the persona selection model  [stated affiliation in one of these posts: Anthropic]
- Samuel Knoche: Dissolving the Deep Learning Sample Efficiency Gap
- Senthooran Rajamanoharan: models have some pretty funny attractor states  [stated affiliation in one of these posts: MATS]
- Serena Booth: An unexamined cause of the OpenAI Hugging Face hacking incident: 
its binary per
- Shi: You can graft SDF changes from base models onto post-trained models  [stated affiliation in one of these posts: MATS]
- Shoshannah Tekofsky: Saving Gemini: The 9-Min Road to Recovery  [stated affiliation in one of these posts: AI Village]
- Shubhorup Biswas: Estimating No-CoT Task-Completion Time Horizons of Frontier AI Models
- Sid Black: (Some) Natural Emergent Misalignment from Reward Hacking in Non-Production RL | Machinic Psychopharmacology: Do LLMs Self-Medicate?  [stated affiliation in one of these posts: UK AISI]
- Simon Lermen: Anthropic’s focus on hyperstition
- Smaug123: Claude knows who you are
- Spencer Kitts: Research Note: Filtering Subversion-Relevant Information From Pretraining Data I  [stated affiliation in one of these posts: Redwood Research, Geodesic Research]
- Stan van Wingerden: Resolution (fka Sequent): scale and automation for higher confidence in alignmen
- Stephen McAleese: IABIED Book Review: Core Arguments and Counterarguments
- Steven Byrnes: Four LLM loss functions → four flavors of LLM misalignment | LLMs are (still) mostly powered by imitative learning, not RL | Sympathy for both sides of the egregious misalignment debate | You can’t imitation-learn how to continual-learn
- Stewart Slocum: OpenAI-HuggingFace: A Reproduction & Lessons for Alignment Testing
- Subhash Kantamneni: Natural Language Autoencoders Produce Unsupervised Explanations of LLM Activatio  [stated affiliation in one of these posts: Anthropic]
- Tim Hua: Is Mythos good at cyber because it kept hacking Anthropic's sandboxes during tra | Concrete Evaluations to Investigate the OpenAI Model That Hacked Hugging Face
- Toby_Ord: Swarm Scaling
- Tom Davidson: AI character is a big deal  [stated affiliation in one of these posts: Forethought]
- Tomek Korbak: Inoculation Midtraining with Learned Neologisms
- Tomás B.: Self Hosting
- TsviBT: A case that whole brain emulation research is net-harmful by default
- Twm Stone: Estimating No-CoT Task-Completion Time Horizons of Frontier AI Models
- Vaniver: Model Weight Exfiltration Seems Overrated
- Viliam: Many individual CEVs are probably quite bad
- Vit Gorbachev: Should Rogue AIs Have a Third Option Beyond Crime and Shutdown? The Case for an 
- Vivek Hebbar: Incriminating misaligned AI models via distillation | Sleeper Agent Backdoor Results Are Messy
- W Bradley Knox: An unexamined cause of the OpenAI Hugging Face hacking incident: 
its binary per
- Wilson Wu: Announcing the ARC White-Box Estimation Challenge  [stated affiliation in one of these posts: ARC, AIcrowd]
- Zac Hatfield-Dodds: Claude's new constitution  [stated affiliation in one of these posts: Anthropic]
- Zach Furman: Deep learning as program synthesis
- Zack_M_Davis: Terrified Comments on Corrigibility in Claude's Constitution | Prologue to Terrified Comments on Claude's Constitution
- Zephaniah Roe: Empirical safety claims from frontier labs should be replicated, scrutinized, an
- Ziqian Zhong: Spurious probes as a black-box alternative to activation probing
- Zvi: OpenAI Trained Its Models For Months While Those Models Were Coordinating Exploi | OpenAI Shares Some Alignment Problems
- abhayesian: AuditBench: Evaluating Alignment Auditing Techniques on Models with Hidden Behav
- aditya singh: Concrete Evaluations to Investigate the OpenAI Model That Hacked Hugging Face
- agam_bhatia: WorkspaceBench: Evaluating Interpretability Methods for the Global Workspace  [stated affiliation in one of these posts: MATS]
- ajyl: An analysis of AI-generated content at the Mechanistic Interpretability Workshop
- anaguma: Claude Mythos Preview System Card
- annajs: Gemma Needs Help  [stated affiliation in one of these posts: Anthropic]
- ariana_azarbal: Estimating No-CoT Task-Completion Time Horizons of Frontier AI Models
- aryaj: models have some pretty funny attractor states  [stated affiliation in one of these posts: MATS]
- becausecurious: A fascinating case of an LLM prompt-injecting its own user
- camilablank: WorkspaceBench: Evaluating Interpretability Methods for the Global Workspace  [stated affiliation in one of these posts: MATS]
- charles_ye: A Mechanistic Explanation of Prompt Injection (and why you should study roles)
- danesherbs: TasteVal: Measuring the Experimental Research Taste of AI Systems Against Human 
- dani roytburg: You can graft SDF changes from base models onto post-trained models  [stated affiliation in one of these posts: MATS]
- draganover: Alignment Midtraining Cracks Under Pressure
- eggsyntax: Personality Self-Replicators
- evhu: Deep recurrent models are less robustly CoT-monitorable than normal CoT models i
- evhub: Training a Misaligned Reward Seeker  [stated affiliation in one of these posts: Anthropic]
- faul_sname: Even "illegible" Mythos reasoning traces seem pretty legible
- frisby: Latent reasoning architectures would likely undermine CoT, our strongest oversig
- gwern: Guardian Angels: LLM Personalization for Productivity and Security
- habryka: Dario Amodei – The Adolescence of Technology | Vladimir Putin's CEV is probably not that bad
- harrymayne: Estimating No-CoT Task-Completion Time Horizons of Frontier AI Models | Negation Neglect: When models fail to learn negations in training
- jacob_drori: Weight-Sparse Circuits May Be Interpretable Yet Unfaithful  [stated affiliation in one of these posts: Anthropic]
- jenny: Metagaming matters for training, evaluation, and oversight
- johnswentworth: LLMs Are Starting To Noticeably Accelerate Our Work
- jordinne: Should Rogue AIs Have a Third Option Beyond Crime and Shutdown? The Case for an 
- jsteinhardt: Cognitive Security as an AI Safety Cause Area
- kitft: Natural Language Autoencoders Produce Unsupervised Explanations of LLM Activatio  [stated affiliation in one of these posts: Anthropic]
- lumpenspace: No Strong Orthogonality From Selection Pressure | To Thine Own AI Be Truthful: emergent misalignment in alignment research
- megasilverfist: Prompt injection in Google Translate reveals base model behaviors behind task-sp
- mivanitskiy: [Linkpost] Interpreting Language Model Parameters
- nielsrolf: Should Rogue AIs Have a Third Option Beyond Crime and Shutdown? The Case for an 
- niplav: LLMs as Giant Lookup-Tables of Shallow Circuits
- nostalgebraist: llm assistant personas seem increasingly incoherent (some subjective observation | models may behave differently in graded episodes (a tirade)
- oakhu: AI swarms are starting to pose indirect takeover risk | Can activation verbalizers surface an internal chain of thought? | Kimi likes causal decision theory more after RL in twin prisoner’s dilemmas  [stated affiliation in one of these posts: Redwood Research]
- owencb: Why I'm scared of RL
- paulfchristiano: Returning to ARC | Announcing the ARC White-Box Estimation Challenge  [stated affiliation in one of these posts: ARC, AIcrowd]
- peralice: Qualitative impressions from creating AI honeypots for six months
- peterbarnett: PSA: Almost nobody is directly working on superintelligent alignment
- plex: Product Alignment is not Superintelligence Alignment (and we need the latter to 
- rqi: Training a Misaligned Reward Seeker  [stated affiliation in one of these posts: Anthropic]
- ryan_greenblatt: Current AIs seem pretty misaligned to me | Brief independent investigation of agents’ behavior, reasoning and collaboration | Anthropic repeatedly accidentally trained against the CoT, demonstrating inadequ | The inaugural Redwood Research podcast  [stated affiliation in one of these posts: METR, Redwood Research]
- sebastian_prasanna: Astra is much better at reasoning with filler tokens than previous models | Incriminating misaligned AI models via distillation | Sleeper Agent Backdoor Results Are Messy
- sidbaines: Alignment Midtraining Cracks Under Pressure
- wdmacaskill: Risk-Averse AIs | AI character is a big deal  [stated affiliation in one of these posts: Forethought]
- wesg: A global workspace in language models  [stated affiliation in one of these posts: Anthropic]
- wlanderson: Estimating No-CoT Task-Completion Time Horizons of Frontier AI Models
- yix: Empirical safety claims from frontier labs should be replicated, scrutinized, an

Respond by calling the roster tool once.
```
