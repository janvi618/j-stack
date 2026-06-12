# Eliciting Expert Knowledge for Skills

This file supports the "Capture Intent and Elicit Expertise" phase of skill creation. Read it when the skill encodes nontrivial judgment — editorial standards, review criteria, strategic workflows, anything where "how a senior person does it" differs meaningfully from "how anyone would do it."

## Why direct questions fail

Experts know more than they can tell. Their knowledge is compiled: they perceive situations in chunks, act on pattern recognition, and reconstruct plausible-sounding rules only when asked. So "what are your best practices?" yields platitudes ("be clear, know your audience") while the real heuristics ("if legal hasn't replied in 48 hours, that means no — escalate, don't wait") never surface. The fix is to anchor every question in concrete, specific, remembered reality.

## Question bank

Scale the depth to the stakes. Pick a handful that fit; don't run the whole battery on a simple skill.

### Recent-instance walk-through
- "Walk me through the last time you actually did this, start to finish. Not how it's supposed to go — how it actually went."
- "What did you look at first? What did you deliberately ignore?"
- "Where did you slow down? What were you checking for there?"
- "What did you do that you'd never bother writing in a process doc?"

### Critical incidents (failure stories disclose hidden heuristics)
- "Tell me about a time someone got this wrong — a new hire, a contractor, a previous AI attempt. What did they miss?"
- "What's the worst version of this deliverable you've ever received? What made it bad?"
- "Has this process ever blown up? What was the early warning sign that got ignored?"

### Decision points (every skill branch should trace to a real rule)
- "At what point do you decide to do X instead of Y? What tips you off?"
- "When do you escalate / ask for help / stop and start over?"
- "What's something that looks fine to a junior person but is a red flag to you?"

### Counterfactual probing (separates invariants from habits)
- "If the deadline were half as long, what would you cut? What would you never cut?"
- "If the audience were [different stakeholder], what changes?"
- "If the input data were twice as messy, what would you do differently?"
The things that never change under counterfactuals are the skill's constraints; the things that flex are its decision branches.

### Intent capture (do this for every rule elicited)
For each rule, ask "why?" until you hit a reason grounded in audience, risk, or outcome:
- Rule: "Lead with the risk section." Why: "Because the exec audience reads only the first paragraph."
- Rule: "Always recalculate before delivering." Why: "Because a single #REF! error destroys credibility with this client."

Write the rationale into the skill next to the instruction. Rules break when context shifts; intent transfers. This is also what lets the model handle situations the rules don't cover.

## Artifact mining

Answers are reconstructions; artifacts are evidence. Request:

1. **2–3 gold examples** — real past deliverables the expert considers right. Resist idealized or sanitized versions.
2. **1–2 rejected/mediocre examples** — ideally with what was wrong. The gold-vs-rejected contrast is where implicit rules hide.
3. **Edit diffs** — a junior draft and the expert's revision of it, review comments, corrections from email/chat threads. The edits ARE the heuristics, in executable form.

Then do explicit rule extraction: read the artifacts, articulate each rule you infer, and confirm it with the expert one at a time. Phrase inferences as testable claims: "Every gold example quantifies the impact in the first sentence — is that a rule, or coincidence?" Inferred-and-confirmed beats invented every time. Confirmed gold examples often belong in the skill itself as `references/examples.md` or assets.

## The expert-pairing check

Before drafting, establish whose judgment the skill encodes and what their involvement will be:

- **User is the expert**: proceed normally; the iteration loop's feedback is your elicitation channel.
- **User is building on behalf of an expert**: ask whether the expert can review outputs during iteration. If yes, structure the review viewer sessions for them. If no, say plainly that the skill will encode the user's best understanding rather than the expert's actual judgment, and suggest a follow-up validation pass with the expert before team rollout.
- **No identifiable expert** ("we just want a skill for X"): that's fine for capability skills (file formats, tooling), but for judgment-heavy skills it's a yellow flag — the skill may end up encoding generic best practices the team could have gotten from a blank prompt. Name the tradeoff and let the user decide.

## During the iteration loop

Treat every piece of review feedback as an elicitation prompt, not a bug report:

1. Symptom: "the tone is off."
2. Probe: "What would right sound like? Rewrite one sentence the way you'd want it."
3. Generalize: "So the principle is: state conclusions before caveats when writing for sales — did I get that right?"
4. Confirm, then encode the principle (with its why), not the one-off fix.

Empty feedback means satisfied; terse frustrated feedback usually means the expert can see the problem but hasn't articulated it — that's exactly when the probe step pays off.
