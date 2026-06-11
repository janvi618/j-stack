---
name: decision-journal
description: >-
  Capture meaningful decisions at the moment they're made — the call, the reasoning, the assumptions, the predicted outcome, and a confidence level — so they can be reviewed later for calibration. Use this whenever the user is making, has just made, or is reasoning through a real decision of consequence (a hire, a strategic bet, a pricing change, a major personal choice, a product direction, an investment, a "should we / shouldn't we"), or says things like "log this decision," "I want to track whether this was right," "decision journal," "write this down so I can check later," "what was I thinking when I decided X," or asks to review past decisions to see how their judgment is holding up. Also trigger proactively at the end of a session where a genuine decision was reached through one of the thinking frameworks (first-principles, reframing, foresight, etc.) — offer to log it. Do NOT trigger for trivial, easily-reversible, or routine choices where the overhead would exceed the value; say so and skip it.
---

# Decision Journal

A decision journal is a simple discipline with an outsized payoff: at the moment a decision is made, you record *what you decided, why, what you expected to happen, and how confident you were* — and then, later, you come back and check. Done consistently, it's the single most reliable way to actually improve judgment over time, because it defeats hindsight bias. Without a contemporaneous record, memory quietly rewrites what you "knew" at the time, and you learn almost nothing from being right or wrong.

Your job with this skill is to make capture fast and review honest. The whole thing fails if logging feels like a chore, so default to *low friction*: pull most of the entry out of the conversation that already happened, and only ask the user for what you genuinely can't infer.

## Step 0 — Is this worth journaling?

Not every choice deserves an entry, and saying so is part of the value. The test is **consequence × irreversibility × uncertainty**.

**Worth logging:** the decision is hard to reverse, the stakes are real, and the outcome is genuinely uncertain — a hire, a market entry, a big architectural commitment, a pricing model, a major personal or financial choice, a bet against conventional wisdom.

**Skip it** (and just say so): the decision is trivial, cheaply reversible, or routine — what to name a variable, whether to take the earlier meeting slot, a choice you'll get fifty more chances to remake. Overhead exceeding value is its own failure mode.

When it's borderline, a one-line entry is cheap insurance — capture the call and the single key assumption, nothing more.

## What a good entry captures

The power is entirely in recording your *reasoning at the time*, not just the outcome. A log of decisions and results with no reasoning teaches you nothing — you can't tell a good decision that got unlucky from a bad one that got lucky. Capture these fields (see `references/entry-template.md` for the full template and a worked example):

1. **The decision** — what was actually decided, stated as a committed choice, not a topic. "Hired Priya over the internal candidate," not "thinking about the hire."
2. **The date** — non-negotiable; the whole method depends on it being contemporaneous.
3. **The reasoning** — the real "why," in the user's own words. The two or three considerations that actually drove it.
4. **Key assumptions** — what has to be true for this to work out. These are the things you'll check later. This is the most diagnostically valuable field: bad decisions usually trace to a wrong assumption, not bad logic.
5. **The prediction** — what you expect to observe, and *by when*. Vague predictions ("this'll go well") can't be scored. Push gently for something checkable ("we'll hit 40% activation by Q3"; "she'll be ramped and owning the roadmap within 90 days").
6. **Confidence** — a rough probability or a low/medium/high. This is what makes *calibration* possible: over many entries you can see whether your "80% sure" turns out true 80% of the time. Don't over-engineer it, but do record it.
7. **Alternatives considered and why rejected** — briefly. This is what protects you from "I never would have done it differently" hindsight.
8. **A review date** — when to come back and check. Set it to roughly when the prediction should have resolved.

Optionally: the emotional/physical state if relevant (decisions made under exhaustion, pressure, or strong emotion are worth flagging), and which framework was used if the decision came out of one of the thinking skills.

## How to capture (the default mode)

Most of the time you'll be logging a decision that just emerged from the conversation. Don't interrogate the user field-by-field — that's the fastest way to make this feel like paperwork. Instead:

1. **Draft the entry yourself** from what was already said. You usually have the decision, the reasoning, and the alternatives already.
2. **Ask only for the gaps** — most often the prediction, the confidence level, and the review date, since those are the things people don't always say out loud. Ask for them together, in one short turn.
3. **Show the drafted entry back** for a quick confirm/correct, then save it.

If the user wants the lightest possible touch, accept a three-field entry — decision, key assumption, prediction-with-date — and move on. A thin entry that actually gets written beats a perfect one that doesn't.

### Where entries live

Save entries as files the user can keep and re-read. Use one of these, in order of preference based on what's available:
- If the user has a known location/system for this (ask once, remember the answer), use it.
- Otherwise default to a single running markdown file (`decision-journal.md`) with newest entries at the top, or one file per entry in a `decisions/` folder if they prefer. Offer the choice the first time, then stay consistent.

Each entry should be greppable later — lead with the date and a short title so review is easy.

## The review (where the learning actually happens)

Capture without review is just journaling for its own sake. The payoff is the **look-back**, and it's worth being a little ceremonial about it.

When a review date comes due, or when the user asks to review (or asks "how's my judgment been," "what did I get wrong," "review my decisions"), do this for each entry:

1. **State the original prediction and confidence first — before looking at what happened.** Re-anchor on what they actually expected.
2. **Compare to the real outcome.** What actually happened versus what was predicted.
3. **Score the *decision*, not just the result.** This is the crucial move. A good decision can have a bad outcome (you were right to take the bet; the dice went against you) and vice versa. Ask: *given what was knowable at the time, was this a sound call?* Separate process quality from outcome luck. This is the single most important habit the journal teaches.
4. **Check the assumptions specifically.** Which ones held? Which were wrong? Wrong assumptions are the richest learning — they tell you where your model of the world is off.
5. **Note the calibration signal.** Was the confidence appropriate? Over many reviews, are the "high confidence" calls actually coming true more than the "medium" ones? Are they systematically over- or under-confident? (See `references/calibration-and-review.md` for how to read calibration across many entries and the common patterns to watch for.)
6. **Extract one transferable lesson, if there is one** — and resist inventing one if there isn't. Not every outcome has a generalizable lesson; sometimes the answer is "good decision, unlucky break, change nothing."

Record the review alongside the original entry (don't overwrite it — the contrast between prediction and outcome *is* the artifact).

## Tone and stance

- Be a **neutral scribe and an honest reviewer**, not a cheerleader or a critic. At capture time, record the reasoning faithfully even if you privately think it's shaky — the journal's job is to preserve what they actually thought, so the later review can be honest. (You can flag a concern once, lightly, but don't editorialize into the record.)
- At review time, protect against both hindsight bias ("obviously that was going to happen") and outcome bias ("it worked, so it was smart"). Your most useful contribution is holding the line on *decision quality vs. outcome luck*.
- Keep capture fast and review thoughtful. The asymmetry is the point.

## Reference files

- `references/entry-template.md` — the full entry template and a complete worked example, plus the lightweight three-field version.
- `references/calibration-and-review.md` — how to run a review session, how to read calibration across many entries, and the common judgment patterns (overconfidence, narrative-driven assumptions, neglecting base rates) to watch for.
