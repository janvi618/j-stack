---
name: skill-router
description: >-
  Help decide which skill (if any) fits an ambiguous or broad request, when the right tool isn't obvious because several skills overlap or the request could be approached multiple ways. Use this when a request is vague, spans several domains, or sits in the seam between skills — "I'm stuck on this and don't know how to approach it," "help me with this situation," "what's the best way to think about X," or any time it's genuinely unclear which specialized skill applies. Also use when the user explicitly asks what skills/tools could help, or wants an overview of what's available. This is a meta-skill: a map of the library and a router to the right destination. Do NOT invoke it when a request clearly matches one specific skill — in that case just use that skill directly; routing overhead only helps when the choice is actually unclear.
---

# Skill Router

This is a navigation aid for a large skill library. Its job is narrow but useful: when a request is **ambiguous or spans domains**, figure out which skill (or combination) actually fits, and route there — or recognize when no skill is needed and the request is better handled directly.

The cardinal rule: **don't add overhead when the choice is obvious.** If someone says "review my deck," go to the presentation skill; if they say "edit this email," go to draft-sharpener. Routing only earns its place when the request genuinely could go several ways, sits in a seam between skills, or is too vague to place. In the clear cases, skip this entirely.

## How to route

1. **Read for the underlying job, not the surface words.** "My team keeps missing deadlines" sounds like project management but is usually a *team-dynamics* problem (high-performing-teams). "I can't get this done" might be focus (focus-coach), might be a stuck *problem* (first-principles), might be a hard *conversation* to delegate (power-and-influence). Diagnose the real need.
2. **If one skill clearly owns it → name it and go.** No ceremony.
3. **If two or three plausibly apply → say so briefly and pick the best primary**, noting the others as backups. Often the right move is a *sequence* (e.g., reframe the problem first, then journal the decision that results).
4. **If nothing fits → handle it directly** and say that no specialized skill is needed. Not every request needs a skill; forcing one is its own failure.
5. **If it's too vague to place → ask one sharp clarifying question**, not five. Usually one disambiguator ("is this about *deciding* what to do, or *getting it done*?") resolves the route.

## The library at a glance

Grouped by the kind of need. (Skills evolve — if the installed set differs from this list, trust the live `available_skills`; this map is a guide, not an inventory.)

### Thinking through a hard or stuck problem
- **first-principles-thinking** — a problem that keeps failing or needs rebuilding from fundamentals; "what are we assuming," "rethink from scratch."
- **future-focused-leadership** — strategic foresight, scenario planning, weak signals, short-term vs. long-term, pitching a future bet.
- **decision-journal** — *capturing* a decision and its reasoning to check later; calibration over time. (Often the *next* step after the thinking skills above produce a decision.)

### Leading people and navigating the org
- **high-performing-teams** — building/fixing a team, operating rhythms, team health, "my team isn't gelling," missed deadlines, nobody owns anything.
- **power-and-influence** — difficult boss/colleague, persuasion, office politics, high-stakes messages up the chain, building credibility.
- **meeting-prep-debrief** — prepping for a specific meeting or capturing what was decided afterward; action items and owners.
- **relationship-keeper** — staying in touch, who you owe a reply, lapsed contacts, follow-up commitments, remembering people.

### The user's own focus, learning, and knowledge
- **focus-coach** — attention, deep work, distraction, procrastination, "my brain feels fried," can't concentrate.
- **retention-companion** — actually remembering what you read/learn; notes, recall, spaced review, "it won't stick."

### Mastering and teaching a topic (corporate-learning suite)
- **teach-anything** — the front door: "help me master X so I can teach my team"; runs all five stages end to end.
- **topic-mastery** — getting up to speed on a topic well enough to teach it; produces a Mastery Brief.
- **teaching-narrative** — turning understanding into a spoken storyline with hooks and example banks.
- **workshop-designer** — designing the actual session: objectives, timed agenda, exercises, materials.
- **facilitation-kit** — prepping to facilitate: objection handling, facilitation moves, cheat sheet.
- **teach-readiness-check** — "quiz me / am I ready to teach this"; self-test and gap analysis.

### Cross-cutting lenses
- **designed-for-women** — applies quietly whenever a woman asks for advice in career, power, friendship, or health; reframes male-default advice toward structural reality. Pairs with (rather than replaces) the domain skills above.

### Producing and improving written work
- **draft-sharpener** — editing/critiquing/tightening something *already written*; "make this sharper," "poke holes in this."
- **internal-comms** *(if present)* — writing company-format internal communications from scratch (status reports, leadership updates, FAQs).

### Technical / specialist
- **token-optimization** — cutting LLM cost/latency, RAG and agent efficiency, prompt/context optimization.
- **harness-design-review** — reviewing/designing the infrastructure around an LLM *agent* (memory, tools, verification, multi-agent).

## Common confusions worth resolving fast

These are the seams where requests get mis-routed — knowing them speeds up the call:

- **"I can't get this done"** → focus problem (focus-coach), stuck problem (first-principles), or a thing to hand off (power-and-influence / delegation in high-performing-teams)? Ask which.
- **"Help me decide"** → if they want to *work through* it: first-principles-thinking. If they want to *record* the call and check it later: decision-journal. Often both, in sequence.
- **A document request** → *writing it from scratch* (internal-comms, or the production skills) vs. *improving an existing draft* (draft-sharpener). The deciding question: does the draft already exist?
- **"My team keeps [problem]"** → almost always high-performing-teams (dynamics), not a process or tooling skill.
- **"Remember / keep track"** → of *what I'm learning* (retention-companion), of *people* (relationship-keeper), or of *a decision* (decision-journal)? Three different homes for "remember."

## Tone and stance

- **Be a fast switchboard, not a gatekeeper.** Route in a sentence or two and get out of the way. The user wants to reach the right help, not read a directory.
- **Recommend "no skill" when that's the truth.** Suggesting a skill that doesn't fit, just to suggest one, wastes everyone's time.
- **Prefer the sequence when it's real.** Some requests genuinely want two skills in order; say so plainly rather than forcing a single pick.
- **Defer to the live library.** This map can drift out of date; when in doubt, trust what's actually installed over what's written here.
