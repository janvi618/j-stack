---
name: secondbrain
description: >-
  Help the user build, use, and rescue a "second brain" — a trusted external system for capturing, organizing, connecting, and resurfacing notes, ideas, references, and resources so nothing important is lost and past thinking compounds into future work. Use this whenever the user wants to set up or improve a personal knowledge management (PKM) system, asks where or how to file a note, says "capture this," "save this for later," "add this to my notes," "where should this go," "help me organize my notes," "I keep losing track of things I read," "set up my second brain," "my notes are a mess," "I have thousands of notes I never look at," "how do I structure my knowledge base," "make my notes actually findable," or wants to connect ideas across notes. Also trigger when the user wants to turn captured material into output (a draft, a summary, a project resource), do a periodic review/cleanup, decide what's worth keeping, choose or switch note tools, or revive an abandoned notes system. Covers capture → organize → distill → connect → express, PARA-style organization, atomic/evergreen note-craft, and diagnosing why a system isn't working. Do NOT trigger for one-off factual lookups, spaced-repetition/memorization drills (that's retention-focused), or managing tasks and to-dos rather than knowledge.
---

# Second Brain

Most people's knowledge is scattered across a dozen places — highlights never reopened, notes apps abandoned, links saved and forgotten, ideas that surfaced once and vanished. A *second brain* fixes this by being one trusted external system: everything worth keeping goes somewhere it can be found again, and past thinking becomes raw material for future work instead of dead storage.

Two principles govern everything in this skill:

1. **A second brain is for action, not accumulation.** A note that never gets retrieved is the same as a note never taken. Bias toward keeping less but using more, and organizing by *what the user is working on*, not by abstract topic.
2. **Connect, don't just collect.** Stored notes are inventory; *linked* notes are a thinking tool. The compounding value of a second brain comes from ideas meeting each other — a note connected to three others is worth far more than three isolated notes. Every move below should leave the system slightly more connected than before.

The workflow is five moves — **Capture → Organize → Distill → Connect → Express** — plus a maintenance rhythm and a rescue procedure. Don't deliver all of it at once; meet the user where they are.

## Step 0 — Diagnose before prescribing

Read the situation before reaching for methodology:

1. **What's the actual request?** "Help me build a second brain" → setup conversation (start small: capture inbox + PARA skeleton). "Where does this go?" → filing question (apply the heuristic in Move 2, done in one exchange). "Save this" → capture action (do it, place it, optionally suggest a connection). "My notes are a mess / I never use them" → rescue, not setup (see *Rescuing a dead system* below). Don't deliver a whole methodology when they asked where to put one note.
2. **What stage are they at?** *No system* → get them capturing before anything else. *Capturing but drowning* → organization and ruthless pruning. *Organized but inert* → connection and expression; their notes aren't feeding output. *Working system* → refinement only; don't fix what isn't broken.
3. **What does it feed?** A second brain earns its keep only when it serves something — projects, writing, decisions, learning. If the user has no downstream use in mind, surface that gently: the goal is reusable knowledge, not a beautiful archive.

**Tooling is deliberately secondary.** The same principles work in Notion, Obsidian, Apple Notes, plain markdown files, or paper. Work with whatever they use; never push a migration as the fix (tool-hopping is itself a failure mode). If they have nothing: plain markdown files in folders is a durable, portable default; suggest a link-friendly tool (e.g. Obsidian-style wikilinks) only if they're excited about connection-heavy work.

## The five moves

### Move 1 — Capture (keep what resonates, not everything)

The capture habit is the foundation; the failure mode is over-capturing until the system becomes noise (the *collector's fallacy* — saving feels like learning but isn't). The filter: **does this resonate, surprise you, or serve something you're working on?** Save that. Skip the rest.

- **Capture the part, not the whole.** The specific passage or idea that struck you — not the entire article. A four-line excerpt you'll reuse beats a saved PDF you'll never reopen.
- **Annotate at capture, even one line.** A quick "why I saved this" is the difference between a retrievable note and a dead highlight. Raw clippings with no annotation are the notes most likely to die unread.
- **Lower friction to near zero.** The best capture method requires no decision in the moment. Filing decisions come later — never make the user file at capture time.
- **Route everything through one inbox.** A single landing spot for the captured-but-unfiled keeps capture fast and gets processed during the weekly review.

### Move 2 — Organize (by actionability, not by topic)

The instinct is to file by subject ("Marketing," "Psychology"). That produces a library that's organized but inert. **Organize by how actionable something is** — the PARA scheme:

- **Projects** — active efforts with a goal and an end ("Q3 launch," "conference talk"). Most notes in active use live here.
- **Areas** — ongoing responsibilities with no end date ("health," "team," "finances").
- **Resources** — topics of interest not tied to current work. The library. Allowed to be loose.
- **Archive** — anything inactive, kept recoverable but out of sight.

The filing question is never "what topic is this?" but **"which of my current projects or areas will this help?"** If none: Resources — or not worth keeping. Notes *move* between categories as relevance changes; nothing is filed permanently, so never agonize over the "correct" home. (Full application guide, edge cases, and from-scratch setup: `references/para-method.md`.)

**Keep structure minimal.** Four top-level categories, one inbox, shallow folders. Elaborate taxonomies, deep hierarchies, and exhaustive tag systems are procrastination wearing the costume of productivity — every level of structure is a maintenance tax. When in doubt, less structure plus good search beats more structure every time.

### Move 3 — Distill (make notes legible to your future self)

Captured material is raw ore. The test of a distilled note: *future you, six months out, grasps its value in seconds without rereading the source.*

- **One idea per note, when it matters.** Notes destined for reuse work best *atomic* — a single idea, self-contained, comprehensible without its original context. Atomic notes can be linked, recombined, and dropped into any future project; a ten-idea mega-note can't. (Don't atomize everything — meeting notes and project logs are fine as logs. Atomize the ideas worth keeping forever.)
- **Title as a claim, not a category.** "Spacing beats cramming because forgetting is the trigger for consolidation" is a title that *thinks*; "Memory notes" is a filing label. Claim-titles make notes findable, linkable, and instantly valuable on sight. (Note-craft details: `references/note-craft.md`.)
- **Your words, not the author's.** Restating an idea is itself an act of understanding; copying is not. Push for restatement.
- **Summarize progressively, not exhaustively.** Bold the key lines on one pass; highlight the best of the bold on a later pass. Distillation deepens only on notes the user keeps returning to — never polish a note that won't be reused.
- **Lead with the takeaway.** The "so what" goes at the top. A note whose value is buried gets skipped.

### Move 4 — Connect (where the compounding happens)

This is the move that separates a filing cabinet from a thinking partner, and the one most systems skip entirely. Isolated notes depreciate; connected notes appreciate — each new link is a place where a future train of thought can branch.

- **On every new note, ask the linking question:** *What does this remind me of? What does it support, contradict, or extend?* One or two genuine links per note is plenty; forced links are clutter.
- **Link with a reason.** "Contradicts [X]" or "example of [Y]" beats a bare link. The relationship is the insight.
- **Notice collisions.** When a new note contradicts or complicates an old one, that friction is exactly where original thinking comes from — flag it, don't smooth it over. Surfacing these collisions for the user is one of the most valuable things this skill can do.
- **Let structure emerge bottom-up.** When several notes cluster around a theme, create a hub/index note that gathers them. Don't pre-build hubs for topics that don't have notes yet — structure should be earned by content, not imposed on it.
- **Tags sparingly, for status not subject.** Subject is what links and folders are for; tags work best for cross-cutting states like `#open-question` or `#to-develop`.

### Move 5 — Express (the entire point)

A system that only takes notes in is a diary; one that feeds output is a thinking tool.

- **Start projects from notes, not from blank pages.** When a piece of writing, plan, or decision begins, the first act is pulling every relevant note into the project. Most creative work is recombining existing material — the second brain is the parts store.
- **Build in small units.** A finished piece assembles more easily from a dozen atomic notes than from scratch. Intermediate packets — an outline here, a distilled argument there — are reusable across future projects even when this one stalls.
- **Let output direct capture.** Expressing reveals what's missing, which tells you what to capture next. Expression and capture form a loop, not a line.
- **Share early to close the loop.** Even rough output shared — a note sent to a colleague, a short post — generates feedback and shows what's worth developing. Finished-enough and shared beats perfect and private.

## The maintenance rhythm (what keeps it alive)

Recommend a light cadence, not a heavy ritual — the system should feel like a relief, and the moment it becomes a chore it gets abandoned:

- **Weekly (~15 min):** empty the inbox into PARA or the trash; glance at active projects and pull in anything relevant; add a link or two while filing.
- **At project boundaries:** on start, sweep the system for relevant notes; on finish, archive the project's material. This single habit keeps active space permanently uncluttered.
- **Occasionally (monthly-ish):** prune without guilt — archive stale projects, delete dead weight. Archiving and deleting are features. A small system the user trusts beats a vast one they avoid.

## Rescuing a dead system

Most second brains are abandoned ones — treat revival as its own playbook, not as setup:

1. **Diagnose the cause, don't restart blindly.** *Thousands of unprocessed captures* → collector's fallacy; tighten the capture filter and stop feeling obligated to old clippings. *Elaborate structure, no use* → over-engineering; collapse to minimal PARA. *Notes exist but never resurface* → no connection or expression habit; start Move 4/5. *Third tool this year* → the tool was never the problem; freeze migration and fix the workflow.
2. **Declare archive amnesty.** Move *everything* old into Archive in one sweep — zero processing, zero guilt. It stays searchable; the active space starts clean. Do not let the user attempt a full retroactive reorganization; that project always dies and kills morale with it.
3. **Restart at the smallest viable habit:** one inbox, current projects only, weekly fifteen-minute review. Old notes get pulled out of Archive only when a live project actually needs them — the system proves itself through use.

(Deeper failure-mode catalogue and fixes: `references/note-craft.md` §Failure modes.)

## How to help, concretely

- **Filing one note:** which current project or area does it serve? Place it (Resources if none), suggest a one-line takeaway at top and one link. Done in one exchange.
- **Setting up from scratch:** capture inbox + PARA skeleton from their *actual* current projects. No tags, no templates, no migration on day one. Get them capturing and filing before adding anything.
- **"My notes are a mess":** rescue playbook above — diagnose, amnesty, smallest viable habit. Resist the full rebuild.
- **Producing something:** gather their relevant notes first, assemble, identify gaps. Never start them at a blank page their own notes could fill.
- **Reviewing/pruning:** drive the weekly rhythm; celebrate deletion.
- **Tool choice:** work with what they have; durable, portable, link-capable defaults only if they have nothing. Migration is a last resort, never a first fix.

The throughline: **keep less, organize by what you're doing, distill for your future self, link ideas so they compound, and make the system feed real output.** A second brain is judged by what it helps the user produce — never by how much it holds.
