# Note-Craft — Atomic Notes, Linking, and Failure Modes

How to write individual notes that stay valuable for years, how to link them so knowledge compounds, and how to diagnose a system that's gone wrong. Load this when the work goes beyond filing — when the user is writing notes meant to last, building connections, or rescuing a broken system.

## Atomic notes: one idea, self-contained

An atomic note carries exactly one idea and makes sense on its own, without the source or the surrounding conversation. Atomicity is what makes a note *reusable*: it can be linked to anything related, dropped into any future project, and recombined endlessly. A note containing five ideas can only ever be used as that bundle.

**Two ways to atomize:**
- **Split** a sprawling capture into its distinct ideas, one note each.
- **Compress** several fragments that are really one idea into a single note.

**The self-containment test:** could a stranger (or you in two years) read this note alone and get the idea? If it depends on "the article I read Tuesday" or "what we discussed above," it isn't self-contained yet — add the missing context or the source.

**What to atomize — and what not to.** Atomic treatment is for *ideas worth keeping indefinitely*: concepts, arguments, principles, recurring patterns, hard-won lessons. It is overkill for meeting notes, project logs, working scratch, and journals — those are fine as chronological logs. Pushing everything into atomic form is one of the ways systems collapse under their own maintenance cost; the skill is knowing which 5% of captures deserve promotion to permanent notes.

**Evergreen, not write-once.** The best permanent notes are revisited and revised as understanding deepens — they accumulate refinements, links, and counterexamples over years. Treat a permanent note as a living claim, not a finished record. When new material complicates an old note, update the note (or link a new note that contests it) rather than letting the old version silently go stale.

## Titles: claims, not categories

The single highest-leverage habit in note-craft. A title should state the note's *idea*, not its *topic*:

| Category title (weak) | Claim title (strong) |
|---|---|
| Notes on habits | Habits form around cues, not goals |
| Pricing thoughts | Customers anchor on the first price they see |
| Feedback stuff | Feedback lands better when it's asked for than when it's offered |
| Memory article | Forgetting is the trigger that makes review effective |

Why this matters so much:
- **Findability** — you search for ideas in the words you'd think them in; a claim matches, a label doesn't.
- **Linkability** — in link-capable tools, a claim-title reads as a sentence fragment inside other notes ("this fails because [[customers anchor on the first price they see]]"), which makes linking natural and links self-explanatory.
- **Instant value** — a list of claim-titles is itself a summary of everything you know; a list of labels is a filing cabinet's spine.
- **Honesty check** — if you can't title the note as a claim, you may not yet know what the note is saying. That's useful feedback: distill further before filing.

Questions work too, for genuinely open notes: "Why do small teams outship big ones?" is a fine title for a note collecting evidence toward an unresolved question.

## Linking: where compounding lives

A second brain's value grows roughly with its *connections*, not its size. Linking practice:

**The linking pass.** On creating (or touching) a note, ask: *what does this remind me of? what does it support, contradict, extend, or exemplify?* Spend sixty seconds; add one or two genuine links. Search the system for related terms if nothing comes to mind — the search itself often surfaces forgotten neighbors.

**Typed links beat bare links.** A bare link says "related, somehow"; a typed link carries the relationship:
- *supports / evidence for* — strengthens an existing claim
- *contradicts / tension with* — challenges one (the most valuable type; see below)
- *example of / instance of* — concrete case of an abstract idea
- *extends / refines* — adds nuance or scope
- *prompted by* — provenance, where this thought came from

In plain-text tools this is just a phrase before the link: "Contradicts [[feedback lands better when asked for]]: in crisis settings, unsolicited correction outperforms."

**Collisions are the product.** When a new note contradicts an old one, you've found the exact spot where your understanding is incomplete — which is where original thinking starts. Never resolve a collision by quietly ignoring one side. Make the tension explicit (a note titled "When does X *not* hold?" is a great move) and let it sit until experience or further reading settles it. When helping a user file new material, actively check whether it collides with anything they already have — surfacing those collisions is among the most valuable assistance possible.

**Hubs emerge; they aren't planned.** When four or five notes cluster around a theme, create a *hub note* (also called an index or Map of Content): a short note that lists and briefly situates the cluster's members. Hubs are tables of contents that grow bottom-up. Building hub structure *before* the notes exist is empty scaffolding — let content earn its structure.

**Tags: status, not subject.** Subject organization is what folders (PARA) and links already do; duplicating it in tags creates a third taxonomy to maintain. Tags earn their keep for *cross-cutting status*: `#open-question`, `#to-develop`, `#needs-source`, `#seedling`. A handful, used consistently, beats a sprawling vocabulary used once each.

## A workable note template (keep it minimal)

For permanent/atomic notes — adapt freely, never enforce rigidly:

```
# <Claim as title>

<The idea in 2–6 sentences, own words, self-contained.>

Why it matters: <one line — the "so what".>

Links: supports [[...]] · contradicts [[...]] · example of [[...]]
Source: <where it came from, if anywhere>
```

Capture notes need none of this — a line of text and a "why I saved it" is enough until/unless the note is promoted.

## Failure modes — diagnosis and repair

Most second brains fail. The patterns are few and recognizable; match the symptom, apply the fix, and resist the urge to fix by starting over in a new app.

**1. The collector's fallacy** — *symptom:* thousands of clippings, highlights, and bookmarks; almost nothing in the user's own words; saving feels productive but nothing resurfaces. *Cause:* capturing substitutes for processing — the save *feels* like learning. *Fix:* radically tighten the capture filter (resonance + usefulness to current work); add the one-line annotation rule; declare amnesty on the backlog (archive it all, unprocessed, guilt-free) rather than attempting to process it.

**2. Over-structuring** — *symptom:* deep folder trees, elaborate tag taxonomies, intricate templates — and dread of filing anything because every note triggers a classification puzzle. *Cause:* structure-building is more fun than note-making, and it masquerades as productivity. *Fix:* collapse to minimal PARA + one inbox; delete the tag vocabulary except status tags; let any further structure be earned by actual note clusters (hubs), never pre-built.

**3. Write-only memory** — *symptom:* a real, organized collection that the user never opens; notes go in, nothing comes out. *Cause:* no connection or expression habit — the system has an input pipe but no output pipe. *Fix:* install the linking pass on every new note; make "pull relevant notes first" the mandatory opening act of every new project; add the weekly review so old notes get touched.

**4. Tool-hopping** — *symptom:* third notes app this year; each migration consumes weeks; enthusiasm spikes and collapses with each move. *Cause:* misdiagnosis — attributing a workflow failure to the tool. The new tool's honeymoon *is* the brief workflow it imposes. *Fix:* freeze migration for six months; identify which actual failure mode (1–3) keeps recurring and fix that in the current tool. Migrate only ever for concrete missing capabilities, not for a fresh start.

**5. The perfect-note paralysis** — *symptom:* very few notes, each laboriously polished; capture has slowed to nothing because every note must be "done right." *Cause:* treating every capture as a permanent note. *Fix:* re-split the pipeline — capture is allowed to be messy and fast; only the few notes that prove useful get promoted and polished. Progressive distillation, not up-front perfection.

**6. The orphaned archive** — *symptom:* a once-good system gone stale after a life change (new job, finished degree); old structure no longer matches current work. *Cause:* PARA categories weren't updated when the work changed. *Fix:* project-boundary hygiene — archive the old projects wholesale, instantiate folders for the *current* real projects, and let notes migrate out of Archive on demand.

**The universal prescription** behind every fix: shrink the system until it's trustworthy, route it through current real work, and let use — not ambition — drive its growth.
