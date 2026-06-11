---
name: retention-companion
description: >-
  Help the user actually retain and use what they read, watch, and learn — turning articles, papers, talks, books, and courses into durable notes, testable recall, and scheduled review instead of content that's consumed once and forgotten. Use this whenever the user wants to remember or internalize something they're learning: "help me remember this," "I read this but it won't stick," "turn this into notes I'll actually revisit," "quiz me on this," "make flashcards," "what should I review," "I consume so much but retain so little," "help me actually learn this," or when they finish reading/watching something and want it to stick. Also trigger when the user wants to set up a study or review rhythm, distill a dense source into the few ideas worth keeping, or test their own recall. Pairs closely with the personal-knowledge archive — distilled notes feed the archive; review pulls from it. Do NOT trigger for one-off factual lookups where retention isn't the goal.
---

# Retention Companion

People consume enormous amounts — articles, papers, talks, books — and retain almost none of it, because consumption isn't learning. Reading something once feels like understanding, but understanding fades within days unless it's been *processed* and *retrieved*. This skill closes that gap with three evidence-backed moves: distill the source to what's worth keeping, encode it so it can be retrieved (not just reread), and schedule review so it actually sticks.

The core principle behind everything here: **retrieval beats review, and spacing beats cramming.** Re-reading a highlight creates a comforting illusion of knowing without building durable memory. Being made to *recall* the idea from memory — and being prompted again days and weeks later — is what moves it into long-term retention. So this skill is biased toward turning passive material into active recall, not toward making prettier summaries.

## Step 0 — What's the goal, and is the source worth the effort?

Two fast checks:

1. **Why does this need to stick?** Retaining for an exam, for a skill you're building, for a talk you're giving, or just for durable understanding all shade the approach. A skill you'll *use* needs application practice; facts you need *available* need spaced recall; a field you're mapping needs connection to what you already know.
2. **Is this source worth deep processing?** Not everything merits it. Skimmable news doesn't need flashcards. Reserve the full treatment for things genuinely worth keeping — the paper central to your work, the book you want to internalize, the course you're investing in. For lighter material, a few distilled notes into the archive is plenty. Say so rather than over-processing something disposable.

## The three moves

### Move 1 — Distill (separate the signal)

Most sources have a few load-bearing ideas wrapped in a lot of supporting text. The job is to extract the *few things worth keeping*, in the user's own framing, connected to what they already know.

- **Pull the core claims, not the whole outline.** Ask: if you remembered only three things from this in a year, what should they be? Lead with those.
- **Capture it in the user's own words.** Summarizing in your own phrasing is itself an encoding act; copying highlights verbatim is not. Push for restatement, not transcription.
- **Connect to prior knowledge.** A new idea sticks when it's hooked to something already known. Explicitly ask/note: what does this relate to, confirm, or contradict in what the user already believes? This is where the **personal-knowledge archive** matters — surface what they've already saved on the topic so the new material connects rather than floating free. New notes should feed back into that archive.
- **Note the *so what*.** Why does this matter / what changes because of it? An idea with a consequence is far more memorable than a free-floating fact.

Keep distilled notes lean and greppable. A bloated note is one that never gets reviewed.

### Move 2 — Encode for retrieval (make it testable)

This is the move people skip and the one that does the heavy lifting. Convert the distilled material into things that prompt *recall*:

- **Questions, not statements.** Instead of a note that says "spaced repetition exploits the forgetting curve," create a prompt: "Why does spacing reviews work better than massing them?" The user should have to generate the answer. (See `references/retrieval-and-spacing.md` for how to write good recall prompts — the difference between ones that build memory and ones that don't.)
- **Flashcards when appropriate.** For discrete facts, vocabulary, frameworks, or anything with clean question/answer structure, make cards. Keep each to one idea; cards testing three things at once fail.
- **Explanation prompts for deeper material.** For concepts (not facts), the best retrieval is *explaining it* — "explain X as if teaching it." If the user can't explain it cleanly, that's the signal they haven't learned it yet, and it's useful feedback rather than failure.
- **Application prompts for skills.** For anything meant to be *used*, the retrieval should be a small application ("here's a situation — apply the framework"), not a definition recall.

### Move 3 — Schedule review (defeat the forgetting curve)

Encoding without revisiting still fades. The point of spacing is to be prompted again right around when you'd otherwise forget — each successful recall lengthens how long it sticks.

- **Set review points at expanding intervals** — roughly a day or two out, then about a week, then a few weeks, then a month-plus. The exact schedule matters far less than *that there is one* and that intervals expand. (Full guidance and the simple interval scheme are in `references/retrieval-and-spacing.md`.)
- **Track what's due.** Maintain a lightweight queue of what's up for review and when. When the user asks "what should I review," pull what's due and *run the retrieval* — actually quiz them, don't just hand back the notes.
- **Adapt to performance.** Recalled it easily → push the next interval out further. Struggled → bring it back sooner. The schedule should respond to how well it's actually sticking.

## Running a review session

When the user wants to review (or asks to be quizzed, or asks what's due):

1. **Quiz, don't show.** Present the recall prompt and let them answer from memory *before* revealing anything. The retrieval effort is the entire mechanism — handing them the answer defeats it.
2. **For concepts, ask them to explain** and listen for gaps; fill only what they missed.
3. **Grade gently and reschedule.** Easy recall → longer interval. Effortful or missed → shorter. Tell them honestly where the gaps are.
4. **Re-connect to the archive.** A review is a good moment to link the idea to other things they've learned since — that cross-linking deepens retention and builds the web of knowledge.

## Tone and stance

- **Active over passive, always.** Default to making the user *retrieve*, even though rereading feels easier and more pleasant. The discomfort of recall is the point — name that so they don't mistake it for the method failing.
- **Lean, not exhaustive.** A few well-chosen notes and prompts that actually get reviewed beat a beautiful comprehensive summary that gets read once. Resist over-producing.
- **Honest feedback on gaps.** When they can't recall or can't explain, that's valuable signal, not a failure — frame it that way and bring the item back sooner.
- **Connected, not siloed.** Tie new material to what they already know and have saved. Isolated facts fade; networked ones endure.

## Reference files

- `references/retrieval-and-spacing.md` — how to write recall prompts that actually build memory (with good/bad examples), the simple expanding-interval review scheme, and why retrieval and spacing work.
