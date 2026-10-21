# Scope check (Sonnet 5.5)

Strict technical-AI-safety screen over every post Stephen's filter kept. Input is the excerpt only.

- Script: `src/scope_check.py`
- Model: `claude-sonnet-5-5`
- Output is forced through the tool below.

## System prompt

```text
You screen posts for the Shallow Review of Technical AI Safety 2026, a map of technical AI safety research.
Decide whether the post is technical AI safety work.
IN scope: empirical results, theory, conceptual arguments about alignment problems, threat models, metascience of safety research (replications, critiques of evals/methods), technical research agendas, benchmarks, tools, incident analyses with technical content.
OUT of scope: governance and policy, forecasting and timelines, AI strategy/plans that are not about technical research (e.g. coordinated slowdowns, "Plan A"-style geopolitics), careers and personal stories, community/field news, fiction, general rationality, capabilities without safety content, opinion pieces without technical substance.
Use "borderline" only when a reasonable reviewer could go either way.
Always respond by calling the scope tool exactly once.
```

## Tool schema

```json
{
 "name": "scope",
 "description": "Record the scope decision.",
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
   "reason": {
    "type": "string",
    "description": "One short sentence."
   }
  },
  "required": [
   "scope",
   "reason"
  ]
 }
}
```

## Example user turn

```text
Title: Overwhelming Superintelligence
Authors: Raemon
Forum tags: AI

Excerpt:
There's many debates about "what counts as AGI" or "what counts as superintelligence?". Some people might consider those arguments "goalpost moving." Some people were using "superintelligence" to mean "overwhelmingly smarter than humanity". So, it may feel to them like it's watering it down if you use it to mean "spikily good at some coding tasks while still not really successfully generalizing or maintaining focus." I think there's just actually a wide range of concepts that need to get talked about. And, right now, most of the AIs that people will wanna talk about are kinda general and kinda superintelligent and kinda aligned. If you have an specific concept you wanna protect, I think it's better to just give it a clunky name that people don't want to use in casual conversation,[1] rather than pumping against entropy to defend a simple term that could be defined to mean other things. Previously OpenPhil had used "Transformative AI" to mean "AI that is, you know, powerful enough to radically transform society, somehow." I think that's a useful term. But, it's not exactly what If Anyone Builds It is cautioning about. The type of AI I'm most directly worried about is "overwhelmingly
[... example truncated ...]
```
