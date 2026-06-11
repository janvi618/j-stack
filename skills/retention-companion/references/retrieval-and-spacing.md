# Retrieval Practice & Spacing

## Why these two things work (the one-paragraph version)

Memory isn't strengthened by *receiving* information again — it's strengthened by *retrieving* it. Every time you successfully pull something from memory, you make it easier to pull next time and slower to fade. Re-reading skips the retrieval and so builds little durable memory while feeling productive (the "fluency illusion" — familiar text feels like knowledge). **Spacing** works because the optimal moment to retrieve is just as you're about to forget: too soon is wasted effort, too late and it's already gone. Reviewing at expanding intervals keeps catching the memory right at the edge of forgetting, and each catch extends the edge. Together: retrieve, don't reread; space, don't cram.

## Writing recall prompts that actually build memory

The quality of the prompt determines whether retrieval happens at all. The test: **can this be answered without genuinely recalling the idea?** If yes, it's a bad prompt.

**Bad prompts** (no real retrieval):
- *"Spaced repetition is effective. True or false?"* — guessable, tests nothing.
- *"Spaced repetition exploits the ____ curve."* — pure pattern-match; you can fill the blank without understanding.
- *"What did the article say about memory?"* — too open to require any specific recall.

**Good prompts** (force genuine recall):
- *"Why does spacing reviews out over time beat cramming them together?"* — requires reconstructing the mechanism.
- *"You reread your notes three times and feel confident. Why might that confidence be misleading?"* — tests the concept by applying it.
- *"Explain the fluency illusion to someone who's never heard of it."* — explanation-based; gaps become obvious.

Principles for good prompts:
- **One idea per prompt.** A card testing three facts fails on all three when any one is forgotten, and obscures *which* you missed.
- **Ask "why" and "how," not just "what,"** for anything conceptual. Mechanism recall is more durable and more useful than label recall.
- **Prefer prompts that require generation over recognition.** "Recall the four steps" beats "which of these is a step?"
- **For skills, make the prompt a small application,** not a definition: "Here's a draft argument with an unsupported claim — find it" beats "what is an unsupported claim?"

## The expanding-interval review scheme

Don't overthink the algorithm. A simple expanding ladder captures almost all the benefit:

| Review | Timing (after first learning) |
|--------|-------------------------------|
| 1 | ~1 day later |
| 2 | ~3 days later |
| 3 | ~1 week later |
| 4 | ~2–3 weeks later |
| 5 | ~1 month later |
| 6+ | ~2–3 months, then fade to "known" |

Two adjustments that matter more than the exact numbers:

- **Respond to performance.** Recalled it easily and fast → skip ahead / lengthen the next gap. Struggled or missed → drop back to a shorter interval and rebuild. The intervals are a default, not a rule; the real target is "review right before you'd forget," and the user's actual recall tells you where that is better than any table.
- **Expanding, not fixed, is the key feature.** Reviewing every day forever is inefficient; reviewing at growing gaps matches how memory consolidates. The widening is doing the work.

## Tracking what's due

Keep a simple queue — for each item: a short title, the recall prompt(s), the date last reviewed, the current interval, and the next-due date. When the user asks what to review, pull everything whose next-due date has passed, run the prompts as actual quizzes (answer-before-reveal), then update each item's interval and next-due based on how it went.

The queue should stay lean. If it balloons, that's a signal the user is processing more than they can sustainably review — better to be selective about what earns a place than to maintain a backlog that induces guilt and gets abandoned.

## A note on interleaving (optional, for skills)

When the user is practicing a *skill* with multiple related sub-types (e.g., several kinds of problem, several frameworks), mixing them in a review session ("interleaving") beats blocking them one type at a time. Blocked practice feels smoother but builds weaker discrimination; interleaved practice is harder in the moment and sticks better, because it forces the learner to first figure out *which* approach applies — which is the actual skill. Use this for applied material; it's overkill for discrete facts.
