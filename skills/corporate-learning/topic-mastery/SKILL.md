---
name: topic-mastery
description: Help someone deeply understand a topic so they can teach it clearly to others. Produces a "Mastery Brief" — a plain-language overview that leads with why-it-matters, a beginner-friendly mental model and analogy, a core-concepts table, a tiered concept map, and the topic explained at three levels (12-year-old, smart non-expert, skeptical senior leader). Use whenever someone says they need to "get up to speed on," "really understand," "wrap my head around," or "learn X well enough to explain/teach it," or when concepts within a topic and how they relate feel confusing. Trigger this even when the user only says "explain X" but the context is that they will go on to teach or present it. Do NOT use this to design the session itself (that's workshop-designer) or to write the spoken storyline (that's teaching-narrative) — this is the understand-it-first stage.
---

# Topic Mastery — understand it well enough to teach it

The user is preparing to teach this topic, so they need more than a summary: they need a clean *mental architecture* they can hold in their head and hand to others. Build that.

The user is the learner here. Make them fluent; don't perform expertise at them.

## Intake

You need the **topic**, the **audience** they'll eventually teach, the **context / why it matters now**, and their **current level**. Pull these from the conversation first; ask only for what's missing, in one short batch. If you can proceed on a reasonable assumption, state it and continue.

The current-level answer changes how you write: for a confident-at-a-high-level user, spend less time on the basics and more on how the pieces *relate* (where confusion usually lives) and on the misconceptions a teacher must pre-empt.

## Deliverable: the Mastery Brief

Save it as a markdown file the user can keep and reuse (it becomes the backbone of everything downstream). Use this structure. A fuller annotated template is in `references/deliverable-template.md` — read it if you want the section-by-section prompts.

### 1. Executive overview
Plain language, **why-it-matters first**, then the technical part. Include: a simple definition · why the topic is emerging/important now · the problem it solves · what people commonly get wrong · why it matters specifically for the stated audience. Make it land for an intelligent beginner.

### 2. Beginner-friendly mental model
- A one-sentence explanation.
- A simple analogy (concrete, from everyday life).
- A visual structure described in words (ladder, pyramid, flywheel, map, system loop — pick what fits the topic's actual shape).
- The 3–5 most important components.
- How those components connect to each other.

### 3. Core concepts (table)
One row per essential concept, with columns: **Concept · Simple explanation · Why it matters · Example · Common misconception · How to explain to a beginner · A question to check understanding.** Cover only what someone must grasp *before* teaching — resist dumping the whole field.

### 4. Concept map
Tier the ideas: **Foundational → Intermediate → Advanced → Practical applications → Common pitfalls.** Then explicitly mark, for each, whether the facilitator needs to understand it **deeply** (they'll be questioned on it) or just **well enough to facilitate a discussion** (they can hold the conversation without being the world expert). This triage is the most useful part for a busy facilitator — don't skip it.

### 5. Explain it at three levels
The same topic, three ways:
1. **To a 12-year-old** — short words, a vivid image, no jargon.
2. **To a smart business professional with no background** — competent, concrete, respects their intelligence without assuming domain knowledge.
3. **To a skeptical senior leader** — leads with stakes, cost of inaction, and what changes if they act; anticipates "so what?"

## Style

- Lead with meaning, then mechanism. People retain *why* before *what*.
- Prefer plain words to insider terms; when a term is unavoidable, define it in the same breath.
- Use one good analogy consistently rather than five competing ones.
- Be honest about edges: if two concepts are easy to confuse, say so and give the distinguishing test — that's exactly the clarity a teacher needs.
