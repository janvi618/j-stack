# AI Sparring-Partner Prompts

AI is genuinely useful for first-principles work — but only as a **challenger, decomposer, and option-generator**, never as an oracle for "fundamentals." The right mental model is *structured sparring partner*, not *source of truth*.

Where AI helps most is forcing explicitness: extracting assumptions from a plan, splitting a messy question into sub-problems, generating contrasting frames, building "what must be true" trees, and stress-testing logic from multiple stakeholder perspectives. Where it's dangerous is exactly where first-principles work is also risky: inventing false foundations, smoothing over uncertainty, and sounding causally confident when it's only pattern-matching.

**Every AI-assisted session should include three checks:** What evidence supports this? What assumptions is the model importing? What would falsify this line of reasoning?

You can either hand these prompts to the person to run themselves, or run the corresponding pass on their problem directly — but if you run it yourself, apply the three checks above to your own output.

---

## PROMPT FOR DECOMPOSING A BUSINESS PROBLEM
```
You are a rigorous strategy analyst. Break the following problem into mutually
exclusive, collectively exhaustive components. For each component, distinguish:
1) known facts,
2) assumptions,
3) key causal drivers,
4) metrics that matter,
5) what must be true for success,
6) fastest tests.

Problem:
[PASTE PROBLEM]

Context:
[PASTE CONTEXT]
```

## PROMPT FOR CHALLENGING ASSUMPTIONS
```
Act as a skeptical but constructive reviewer. Read the following plan and
identify:
- explicit assumptions,
- implicit assumptions,
- industry assumptions,
- organizational assumptions,
- customer assumptions,
- incentive-driven assumptions,
- constraints treated as fixed but possibly flexible.
Then rank the top five assumptions by risk.

Plan:
[PASTE PLAN]
```

## PROMPT FOR GENERATING UNCONVENTIONAL SOLUTIONS
```
Use first-principles reasoning, not benchmarking. Start from:
- fundamental customer need,
- real economics,
- real constraints,
- required causal drivers.
Generate 10 solution directions, including at least:
- one low-cost option,
- one high-leverage structural change,
- one option that removes complexity,
- one option that changes the business model,
- one option that seems uncomfortable but plausible.

Problem:
[PASTE PROBLEM]
```

## PROMPT FOR STRESS-TESTING A STRATEGY
```
Critique the following strategy from five perspectives:
1) customer,
2) retailer/channel partner,
3) finance,
4) operations,
5) skeptical competitor.
For each perspective, identify:
- what could fail,
- what assumption is weak,
- what signal would warn us early,
- how to redesign the strategy to reduce risk.

Strategy:
[PASTE STRATEGY]
```

## PROMPT FOR IDENTIFYING REAL VS ASSUMED CONSTRAINTS
```
Analyze this situation and classify each constraint as:
- physical/technical,
- legal/regulatory,
- economic,
- organizational,
- political,
- cultural,
- psychological,
- assumed.
Then identify which "hard" constraints may actually be "soft."

Situation:
[PASTE SITUATION]
```

## PROMPT FOR EXECUTIVE-READY RECOMMENDATION
```
Translate this first-principles analysis into a concise executive
recommendation.
Output:
- decision to make,
- problem in one sentence,
- what we know,
- what assumptions failed,
- recommended action,
- key tradeoffs,
- next experiment,
- owner and timeline.

Analysis:
[PASTE ANALYSIS]
```
