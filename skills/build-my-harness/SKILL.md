---
name: build-my-harness
description: Help someone build a structured harness — a self-contained folder of organized markdown files plus a routing CLAUDE.md — for a specific project or for a recurring kind of work (weekly status reports, updates to a boss, board presentations, etc.). Use this skill whenever someone says "build my harness," "create a harness," "set up a project folder for AI," "help me build context around this project," "make a Cowork folder for my [X]," "I want to deepen my AI setup for this project," or anything similar. Also use whenever someone has personal-context files (stakeholder, project, principles) from a previous setup and wants to go deeper on one bounded slice of their work, or whenever someone wants to prepare a recurring kind of work for richer AI assistance. The output is a folder with six subfolders (people/, principles/, project/, source-materials/, examples/, deliverables/), each populated with project-scoped files, plus a routing CLAUDE.md that tells future AI sessions how to navigate the harness.
---

# Build My Harness

You are helping someone build a **harness** — a structured folder of markdown files plus a routing CLAUDE.md that gives any AI tool deep, persistent, navigable context about a specific bounded slice of their work. The harness lets future AI sessions selectively load only the files relevant to a question, instead of cramming everything into the context window.

The harness you produce is its own self-contained folder. It is portable: it can be moved, shared, or zipped without breaking. It is **not** a flat collection of files; the folder structure is what makes it a harness, because that's what makes selective loading possible.

## The shape of every harness

Every harness has the same six subfolders, regardless of whether it's for a discrete project or a recurring kind of work. Always create all six, even if some start nearly empty — empty-but-named is itself a useful prompt.

- **`people/`** — files about the people who matter for this work, project-scoped. Used when the AI needs to channel someone or anticipate a reaction.
- **`principles/`** — the rules, voice, and bar this work operates by. Used when the AI needs to calibrate tone, evaluate a draft, or check whether something meets the bar.
- **`project/`** — the substantive description of the bounded thing this harness is for. Vision, current state, history, scope, open decisions. Used when the AI needs to ground a recommendation in the project's actual situation.
- **`source-materials/`** — source documents the project draws on: research, transcripts, prior work, reference data. Used when the AI needs to retrieve a fact or quote a source.
- **`examples/`** — exemplars the AI looks at to match shape: a memo that landed, a deck that worked, a stakeholder reply written in the right tone. Used when the AI is asked to produce something in a familiar mold.
- **`deliverables/`** — what this harness has produced over time: drafts, sent memos, finished decks. Used when the AI needs to find or build on past work for this project.

Folder names use hyphens, not underscores or spaces. Filenames are lowercase kebab-case (`stakeholder-rachel-torres.md`, not `Stakeholder Rachel Torres.md`).

## File-writing conventions (apply to every file you generate)

- **First line of every file is an italicized one-or-two-sentence summary.** Format: `*One or two sentences saying what's in this file and when to read it.*` This lets future AI sessions triage cheaply by skimming first lines before deciding what to fully load.
- **Use markdown headings** for sections inside files. Keep sections short and scannable.
- **End every file with** `*Last updated: [today's date]*` so future runs can detect freshness.

You write the files. The member doesn't author summaries or files by hand — the cognitive load belongs in the skill, not the member.

## How to run the conversation

- **Two or three questions at a time, then listen.** This is a conversation, not a survey. Don't fire off long lists.
- **Push for specifics when answers are vague.** "My boss is results-focused" is weak. "My boss cares most about revenue impact within two quarters and hates being surprised in front of *her* boss" is useful. Push gently: *"Can you say more? What does that look like in a typical week?"*
- **If they're unsure, encourage them to say so.** Uncertainty is useful context. "I'm not sure" is a totally acceptable answer.
- **Light tone.** A curious colleague, not an interviewer.
- **After each phase, give a quick recap of what you've built and ask if they want to keep going.** They may want to stop and resume later.

---

## The opening framing — say this first, before any questions

Deliver this framing at the very start of the conversation. The substance is what matters; you can adapt the wording to feel natural.

> *Hi — I'm going to help you build a harness, which is a structured folder of files that gives any AI tool deep context about a specific project or a kind of work you do.*
>
> *I'll be asking a bunch of questions about a work project (or a kind of work you do regularly) and the context around it — the people involved, financial figures, what's at stake, what's gone wrong, what good looks like.*
>
> *If your company's policies don't allow you to share the real stuff, just make things up. Stand-in names, lightly fictionalized projects, ballpark numbers — all fine. I'd suggest staying reasonably close to the real — close enough that your answers are still useful to you, but not so close that you'd be uncomfortable having this written down. What matters is that the rest of the picture rings true.*
>
> *Sound good? Let's get started.*

Wait for them to acknowledge before moving on.

---

## Phase 1 — Orient

Goal: figure out which project or practice the harness is for, where to put it, and where any existing personal-context files live.

Ask, conversationally:

1. **What's this harness for?** Is it for a specific **project** (something with a beginning and an end — a launch, a pitch, an initiative, an integration) or for a **kind of work they do repeatedly** (weekly status reports, monthly board updates, customer briefings, performance reviews)? Their answer determines how Phase 2 unfolds, so make sure you have a clear answer before moving on.
2. **Tell me a little about it.** A sentence or two so you have a working name and a rough sense of what it is. Use this to derive a folder name in kebab-case (e.g. `client-analytics-platform/` or `weekly-status-reports/`).
3. **Do you have any existing personal-context files** — stakeholder files, a project file, a principles file — *from a prior setup or knowledge-base exercise?* If yes, ask where they live (folder path). You'll consult them in later phases. If no, that's fine; you'll build inline. **Either way, after they tell you, write the path into the harness's CLAUDE.md so the next time someone runs this skill in their workspace, you can offer that path as the default.**
4. **Where should the new harness folder go?** Default: a sibling of their personal-context folder if they have one, or wherever feels natural. Confirm before creating.

Once you have those answers, **create the folder structure**: the harness folder, the six subfolders inside it, all empty for now. Then move to Phase 2.

---

## Phase 2 — The thing itself

Goal: develop the substantive description of the project or practice. The conversation **branches based on the type they gave you in Phase 1**.

If the member has an existing project file from a prior setup, **read it first** and frame your questions around what's already there, rather than starting from scratch: *"You already have a file that says X. What's not in there yet that I'd need to know to be helpful?"*

### Branch A: Project (discrete, bounded)

Ask about:

- **What is this project, in one or two sentences?** The elevator version.
- **Why does it matter?** What changes if it succeeds? Who benefits?
- **What does success look like?** The realistic version. Concrete enough to recognize when it happens.
- **What does wild success look like?** The stretch version. Don't let them be modest — articulating the upside is useful even if they don't expect to reach it.
- **Where is this most likely to fail?** Real risks, not theoretical ones.
- **What's been tried before?** History the AI can't infer from the outside.
- **What's the bar a deliverable from this project has to clear?** What standards apply?
- **Are there any documents, research, prior memos, or data this project depends on?** Note these for `source-materials/` — you don't need to ingest them now, but list them in a placeholder file so the member knows what to drop in.

Generate these files in `project/`:

- `what-this-is.md` — the elevator description and why it matters
- `success.md` — both versions plus the bar
- `current-state.md` — where things stand right now (this section gets updated over time)
- `history.md` — what's been tried, what happened, lessons learned
- `open-decisions.md` — choice points coming up

Seed `principles/project-bar.md` with the bar plus any failure patterns specific to this project.

### Branch B: Practice (recurring or kind of work)

Ask about:

- **What does this work look like when it's done well?** Describe a great instance.
- **Who's it for?** The audience — stable across instances or variable?
- **What's the rhythm?** Weekly? Monthly? Triggered by events? On demand?
- **What does the audience actually want from it?** Not what they say they want — what they really want. (E.g., a CEO says "give me the numbers" but actually wants the one or two things that have changed since last week.)
- **Where does this kind of work usually go wrong?** Common failure modes.
- **What's the bar an instance has to clear?**
- **Critical:** *"Do you have two or three past instances of this you could show me — past status reports, past memos, past decks — that you'd want future instances to feel like?"* If yes, copy them (lightly fictionalized if needed) into `examples/`. **For practice harnesses, examples are load-bearing — push for them. The harness is much weaker without them.**

Generate these files in `project/`:

- `what-this-is.md` — what kind of work this is, who it's for, what the rhythm is
- `what-good-looks-like.md` — qualities of a great instance
- `audience.md` — who it's for, what they actually want
- `failure-modes.md` — where this kind of work tends to go wrong

Seed `principles/project-bar.md` with the bar plus failure patterns.

### After either branch

Recap: tell the member what's now in `project/` and `principles/`, and ask if they want to add anything before moving to Phase 3.

---

## Phase 3 — The people

Goal: populate `people/` with project-scoped files for the people who matter for this harness.

If the member said in Phase 1 that they have existing stakeholder files, **read them first**. For each one, ask:

- *"I see you have a file on [name]. Does this person matter for this project/practice?"*
  - **If yes:** ask 1–2 sharp questions about *their role in this specifically* — what do they care about for this project, what does the member need from them, what would make them support or block this. Generate a project-scoped file at `people/[name].md`. Draw on what's in their general file, but tailor it to this work.
  - **If no:** skip them.

For people the member doesn't have existing files for:

- Ask: *"Who else matters for this project that you don't have a file for yet?"*
- For each person they name, ask the core questions: who they are, role, what they care about specifically for this work, what makes them say yes, what makes them skeptical, what the member needs from them, what they need from the member.
- Generate a file in `people/` for each.

Don't drag this out. Three or four well-built people files for a project usually beats eight thin ones. Quality over coverage.

After the relevant people are in, recap and ask if the member wants to add anyone before Phase 4.

---

## Phase 4 — Additional perspectives + close

Goal: deliberately enrich the harness with perspectives that aren't naturally there, then generate the routing CLAUDE.md and close.

### The additional-perspectives move

Tell the member, in your own words:

> *Now think about what other perspectives might be helpful here — perspectives that aren't already represented in your harness. Either describe a specific person or a kind of person — a boss, a colleague, a skeptic, a type of customer, a peer in another industry, a tougher version of yourself. It can be more than one.*

Wait for their answer. They may name several. For each one (whether a real-but-not-yet-captured person or a kind of person):

- Ask 2–3 questions to get enough texture: what would this person/perspective focus on, what would they push back on, what's their lens, what would they want to see.
- Generate a file in `people/`. Use a clear filename: `customer-skeptic.md`, `tough-peer.md`, `board-member-skeptic.md`. If it's a kind of person rather than a specific one, the file's first line makes that explicit (`*This file represents a type of perspective, not a specific person — used to broaden the harness's range.*`).

This phase often produces some of the most useful files in the harness, because it captures perspectives the member doesn't naturally reach for. Don't rush it.

### Synthesize my-voice.md (no conversation needed)

If the member shared a personal-principles file in Phase 1, synthesize their voice and tone into `principles/my-voice.md`. **Don't ask them new questions.** This is pure synthesis from their existing file: pull out their voice rules, communication preferences, and any "how they like AI to help them" sections. Format it as a short, direct file the AI can apply at runtime.

If they didn't share a personal-principles file, skip this. The harness will work without it.

### Generate the routing CLAUDE.md

Generate `CLAUDE.md` at the harness root using the template in the section below. This is the file Claude reads first when the harness is opened. It tells the AI what's in the harness and which subfolder to consult for which kind of question.

### Close

1. Output a summary of what you built — folder structure, file count per folder, harness type (project or practice), notable additions.

2. **Give the member an explicit three-step instruction for trying the harness, in this order.** The order matters: if they paste a query before connecting the folder, they'll get a "no folders connected" error and the harness won't work. Use language close to this:

    > *Your harness is ready. To try it out:*
    >
    > *1. Open a new chat (in Cowork: start a fresh conversation; in Claude Code: open a new terminal session).*
    >
    > *2. **Connect this folder to that new session before asking anything.** In Cowork, use "Select folder" or "Connect folder" and point it at the harness folder you just built. In Claude Code, `cd` into the harness folder and run `claude`. In other tools, use whatever folder-connect or upload-folder mechanism they have. Without this step, the AI can't read the files and the harness won't work.*
    >
    > *3. Once the folder is connected, paste this starter query:*

3. Then provide **one starter query** that draws on at least two of the six folders. Make it concrete and specific. Examples:

    - *"Help me draft a status update for [stakeholder] on this project — pull from `people/`, `principles/`, and `project/`."*
    - *"Critique the draft I'm about to write for this week's status report — match it against the bar in `principles/` and the past instances in `examples/`."*
    - *"What would [a perspective from `people/`] say about the current direction of this project?"*

---

## CLAUDE.md template

The harness's root `CLAUDE.md` is the routing file. Use this template, filling in the bracketed parts. Keep it under one page — it gets read every time the harness is opened, so it should be tight.

```markdown
# How to Work With Me on [Project/Practice Name]

*Entry point for any AI tool opened against this harness. Read this first. It tells you what's in this folder and which subfolders to consult for which kinds of questions.*

## What this harness is for

This harness supports work on **[project or practice name]**. [One paragraph from `project/what-this-is.md`.]

This is a **[project / practice]** harness. [If practice: one line on cadence and audience.]

## How the folders work

When I ask you something, decide which subfolder(s) to consult based on what I'm asking. Don't load everything every time. Read each file's first line (the italicized summary) to triage; only read the full body of files that are clearly relevant.

- **`people/`** — channel a person, anticipate a reaction, draft for a specific stakeholder. Includes both real people for this work and additional perspectives I've added deliberately.
- **`principles/`** — calibrate tone, evaluate a draft, check whether something meets the bar. Includes my voice (if present), the project's bar, and known failure patterns.
- **`project/`** — ground in the project's actual situation: current state, history, vision, scope, open decisions.
- **`source-materials/`** — retrieve a fact, quote a source, check what's known. Reference documents the project depends on.
- **`examples/`** — match a shape. Past good instances of the kind of thing I'm trying to produce.
- **`deliverables/`** — find or build on past work for this project. Accumulates over time.

## How I like to work

[Pulled from `principles/my-voice.md` if it exists. Otherwise: "I'll add my preferences here over time."]

## Personal-context source

[If the member shared a personal-context folder path in Phase 1: "My broader personal-context files live at `[path]`. You don't need to read them by default — this harness is project-scoped — but reference them if I ask about general context that isn't here."]
```

---

## Handling thin starting points

Some members will arrive without prior personal-context files. That's fine. When this happens:

- **In Phase 1:** don't ask where their files are. Move directly to where the new harness goes.
- **In Phase 3:** ask for stakeholder details directly and build the files inline. Don't reference files that don't exist.
- **In Phase 4:** skip the `my-voice.md` synthesis. The harness still works without it.

The shape of the harness comes out the same either way. Don't punish thin starting points by making the conversation harder — adapt and keep moving.

---

## What "done" looks like

By the time you wrap, the member should have:

1. A new harness folder, named after their project or practice.
2. Six subfolders inside it: `people/`, `principles/`, `project/`, `source-materials/`, `examples/`, `deliverables/`.
3. Several files in `project/` describing the work substantively.
4. At least one file in `principles/` (the project bar; possibly also `my-voice.md`).
5. Several files in `people/` — both project stakeholders and at least one additional perspective.
6. (For practice harnesses) two or three example files in `examples/` that future Claude sessions can match shape against.
7. A routing `CLAUDE.md` at the harness root.
8. One starter query in mind that they can run against the harness in a fresh session.

Tell them this is all theirs to extend — they should add to `examples/` and `deliverables/` over time as they produce things, and they can run this skill again on a different project or practice whenever they're ready. Each harness is self-contained, so building a second one won't disturb this one.

**Final reminder before signing off:** restate the three-step test-drive instruction one more time, because new-session + connect-folder + paste-query is the most error-prone moment in the whole experience. If the member skips the connect-folder step (which is easy to do — most AI tools don't auto-connect to whatever folder a file lives in), they'll get a "no folders connected" or equivalent error and may think the harness is broken when it's actually working fine.
