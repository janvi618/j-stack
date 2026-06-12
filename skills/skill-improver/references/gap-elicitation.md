# Gap Elicitation: Filling a Generic Skill with Real Knowledge

Use this when the audit finds sections that score Weak on "evidence of expertise" — places where the skill says things any competent generalist would say, because nobody captured what the actual expert knows.

## The core problem

Experts know more than they can tell. Their knowledge is compiled into pattern recognition; asked directly for their heuristics, they produce platitudes. The skill you're improving is often the fossil record of exactly that failure: someone asked "how do you do X?", got the platitudes, and wrote them down. Re-asking the same question gets the same answer. The fix is to anchor every question in concrete, remembered reality — and in the existing skill's specific gaps.

## Gap-targeted questions

Unlike from-scratch elicitation, you have an artifact to push against. Use it:

- **For a generic step**: Quote it. "The skill says 'review the data for issues.' Walk me through the last time you actually reviewed data for this — what specifically did you look at first, and what did you ignore?"
- **For a hidden decision rule**: "The skill says 'choose the appropriate format.' What actually tips you off about which format is appropriate? Give me the last two times you chose differently and why."
- **For a bare rule**: "The skill says always do X, with no reason. What goes wrong when someone skips it? Has that ever actually happened?" If nothing ever goes wrong, consider deleting the rule. If something does, write the why next to the rule.
- **For a suspiciously smooth workflow**: "This reads like the happy path. Where does this actually go sideways in practice? What's the step where new people mess up?"
- **For the boundary**: "What requests look like they're for this skill but actually aren't? What did the last false-positive look like?"  → feeds the description's negative scope.

## The general technique bank

When the gap-targeted questions open a vein, follow it with the standard tools:

- **Recent-instance walk-through**: "Walk me through the last real time, start to finish — not how it's supposed to go, how it went."
- **Critical incidents**: "Tell me about a time someone got this wrong. What did they miss?" Failure stories disclose the heuristics success stories hide.
- **Counterfactuals**: "Half the deadline / different audience / messier input — what changes, what never changes?" Invariants become constraints; the flexes become decision branches.
- **Why-chains**: For each rule, ask why until the answer grounds in audience, risk, or outcome. That grounding goes into the skill.

## Artifact mining

Stronger than any interview: ask for 1–2 **gold examples** of the deliverable (real ones, not idealized), 1 **rejected/mediocre example** with what was wrong, and if possible an **edit diff** — a draft and the expert's revision. The contrast carries the rules the skill never states. Extract them explicitly and confirm each as a testable claim: "Every gold example quantifies impact in the first sentence — rule or coincidence?" Inferred-and-confirmed beats invented. Confirmed gold examples often belong in the improved skill as references/examples.md.

## The expert-pairing check

Establish whose judgment the skill is supposed to encode:

- **Your user is the expert**: run the questions above directly; their review feedback in the test loop is a second elicitation channel.
- **Your user is a proxy** (they maintain the skill; someone else does the work): fix structure now, but say plainly that the knowledge gaps need the expert — even just a 20-minute review of before/after outputs. Offer to prepare specific questions the user can take to the expert.
- **No expert exists / nobody will engage**: fix what's fixable, and mark the generic sections explicitly in your change log so the gap is visible rather than papered over. A skill honest about its limits beats one that performs confidence.

## During the test loop

Every piece of before/after feedback is elicitation material. The protocol:

1. Symptom: "the new version is better but the tone is still off."
2. Probe: "What would right sound like? Rewrite one sentence the way you'd want it."
3. Generalize: "So the principle is: state the conclusion before the caveats when writing for sales — did I get that right?"
4. Confirm, then encode the principle with its why — not a one-off patch for that test case.

Terse or frustrated feedback usually means the expert sees the problem but hasn't articulated it. That is precisely when the probe step earns its keep.
