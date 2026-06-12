---
name: skill-improver
description: Audits and upgrades an existing Claude skill — diagnoses why it under-triggers, over-triggers, produces inconsistent output, or has become bloated, then elicits the missing expert knowledge and rewrites it. Use when the user has a skill that exists but isn't working well, wants a skill reviewed or audited for quality, says a skill "isn't triggering," "fires too often," "gives inconsistent results," or wants to modernize, tighten, or stress-test a skill they or a teammate wrote. Do not use for creating a brand-new skill from scratch (use a skill-creator skill for that), for general prompt advice unrelated to a skill file, or for token-cost/latency tuning of prompts and pipelines that aren't skills (that's a token-optimization concern).
---

# Skill Improver

A skill for taking an existing skill — yours or someone else's — and making it measurably better.

The core belief: most weak skills aren't badly written, they're badly *informed*. They were authored without the expert heuristics, decision rules, and rationale that make the workflow actually work, so they encode plausible-sounding genericism. Improving a skill therefore has two halves: a **mechanical/structural audit** (cheap, fast, catches the fixable-in-an-hour problems) and a **knowledge audit** (finding where the skill is generic because nobody captured the real expertise, then eliciting it). Don't skip the second half — polishing the prose of an under-informed skill produces a well-formatted under-informed skill.

## The workflow

### Step 1: Intake

Get the skill in front of you:

- Locate the skill directory (ask the user for the path or have them upload it). Read SKILL.md **and every supporting file** — references, scripts, assets. You can't audit what you haven't read, and problems often hide in a reference file the SKILL.md never actually points to.
- Installed skill paths are often read-only. Copy the whole skill to a writable location (e.g., `/tmp/<skill-name>/` or the working directory) before editing. Preserve the original directory name and frontmatter `name` unchanged — the output should be `<original-name>.skill`, not `<name>-v2`.
- Snapshot the original (`cp -r`) so you always have a baseline to test against and a rollback path.

Then get the symptom. Ask the user what's actually going wrong, in their words. The five common symptoms map to different root causes (see [references/failure-modes.md](references/failure-modes.md)):

1. Doesn't trigger when it should
2. Triggers when it shouldn't
3. Output is inconsistent or wrong
4. Skill is bloated / slow / expensive
5. Bundled scripts fail in practice

If the user just wants a general review ("is this skill any good?"), run the full audit and report findings by severity. If they have a specific symptom, still run the full audit — but lead your investigation with their symptom.

### Step 2: Mechanical audit

Run the bundled checker first — it catches the deterministic problems so you spend your judgment on the rest:

```bash
python scripts/audit_skill.py <path-to-skill>
```

It checks frontmatter validity, name/directory alignment, description length and density, presence of negative scope, SKILL.md size, broken internal references, reference nesting depth, and common script anti-patterns (interactive prompts, missing `--help`, undeclared non-stdlib imports). It emits findings with severity levels. The script is advisory — a WARN is a prompt for your judgment, not an automatic fix-me.

### Step 3: Qualitative audit

Now read the skill the way the model will, and score it against the rubric in [references/audit-rubric.md](references/audit-rubric.md). Read that file before this step. In brief, the dimensions:

- **Description as router**: does it say what it does, when to trigger (with the artifacts and phrases real users say), and what it's *not* for? Is the first sentence dense enough to survive truncation?
- **Output contract**: is the primary deliverable explicit — what artifact, what required structure, where it goes?
- **Workflow, not essay**: stepwise instructions, real decision points, consistent terminology — and degrees of freedom matched to fragility (exact steps for brittle operations, heuristics for judgment work)?
- **Intent present**: do rules come with their *why*? Bare ALWAYS/NEVER walls are a yellow flag — a skill that explains its reasoning generalizes; one that only commands overfits.
- **Validation loops**: for fragile operations, is there a validate → fix → re-validate step?
- **Progressive disclosure**: is always-needed material in the body and branch-specific detail in references, referenced explicitly, one level deep? Or is everything dumped in SKILL.md?
- **Evidence of expertise**: this is the big one. Does the skill contain heuristics a generic prompt wouldn't produce — specific decision rules, failure warnings, real examples? Or could Claude have written this skill with no input from anyone who does the work?

Produce a findings list, ordered by impact: for each finding, the evidence (quote the skill), why it matters, and the proposed fix.

### Step 4: Knowledge audit and gap elicitation

For every section that scored generic in "evidence of expertise," go get the missing knowledge. This is elicitation work, and direct questions fail at it — experts can't enumerate their heuristics on demand. Anchor in concrete cases instead. Read [references/gap-elicitation.md](references/gap-elicitation.md) for the technique bank; the short version:

- For a generic workflow step: "Walk me through the last time you actually did this part. What did you check that the skill doesn't mention?"
- For a missing decision rule: "The skill says 'choose the appropriate format' — what actually tips you off about which one is appropriate?"
- For a bare rule with no why: "The skill says always do X. What goes wrong when someone doesn't?" Then write the answer into the skill next to the rule.
- For everything: ask for 1–2 gold examples and 1 rejected example of the deliverable, and mine the contrast for rules the skill never states. Confirm each inferred rule with the user before encoding it.

First check **whose judgment the skill encodes**. If the person you're talking to isn't the expert, say so plainly: you can fix the structure, but the knowledge gaps need the expert's input (even just a review pass on the before/after outputs). An improved skill that still encodes nobody's judgment is a nicer-looking version of the same problem.

If the user can't or won't do elicitation, that's their call — fix the structural findings, and mark the knowledge gaps explicitly in your report so they know what's still missing.

### Step 5: Propose, then edit

Before touching the skill, present the improvement plan: findings, proposed changes, and what you'll leave alone. Get sign-off — especially on anything that changes the skill's scope or triggering behavior, since that affects how it interacts with the rest of the user's skill library. Things to ask about: does this skill overlap with others they have installed? Sharpening non-goals on both sides may be part of the fix.

Then edit. Principles while editing:

- **Subtract before you add.** Most skills that need improving need shrinking. Move branch detail to references, delete instructions that aren't pulling their weight, and keep SKILL.md lean. If the body exceeds ~500 lines after your edits, that's a sign to push more into references.
- **Generalize, don't patch.** When fixing a specific reported failure, encode the principle behind the fix (with its why), not a special-case rule for that one input.
- **Preserve what works.** The user came in with a skill that presumably succeeds at something. Don't rewrite voice, structure, or working sections for taste. Diff-sized humility: every change should trace to a finding.
- **Don't break portability silently.** If you add scripts, follow the script standards (non-interactive, `--help`, useful errors, explicit deps). If the skill might run on the Claude API, remember: no network, no runtime package installs — prefer stdlib.

### Step 6: Test before vs. after

An improvement you haven't tested is a hypothesis. Compare the new version against the snapshot:

- Write 2–3 realistic test prompts (the kind a real user would type, with file paths, context, casual phrasing — not toy prompts). Substantive, multi-step prompts: trivial tasks don't trigger skills at all, so they test nothing.
- Run each prompt against both versions. With subagents (Claude Code / Cowork), run old and new in parallel, outputs to separate directories. Without subagents (claude.ai), follow each version's instructions yourself, one at a time, and be honest about the comparison.
- If the symptom was triggering-related, also test the description: a handful of should-trigger and should-not-trigger queries, with the near-misses being the valuable negative cases. If a full skill-creator skill with a description-optimization loop is available in this environment, hand off to it for rigorous trigger optimization rather than duplicating that machinery here.
- Show the user the before/after outputs and let *them* judge. Their feedback on the diffs is another elicitation opportunity: when they say "the new one is better but still misses X," probe what right looks like, generalize, confirm, encode.

Iterate until the user is satisfied or the changes stop producing meaningful improvement.

### Step 7: Deliver

Package the improved skill (zip the folder with SKILL.md at `<skill-name>/SKILL.md` inside the archive; if a `package_skill.py` from a skill-creator skill is available, use it) and present the file. Keep the original name. Include a short change log in your message: what changed, why, and what was tested — that's the audit trail the next improver will thank you for.

If the skill is team/production infrastructure, one sentence on lifecycle: source in Git, pin versions in API production, re-run tests on model upgrades, record an owner. Don't lecture.

## Communicating with the user

Skill authors range from engineers to domain experts who've never opened a terminal. Match their vocabulary. Findings should be readable by the person who wrote the skill: quote the skill's own text as evidence, explain why it matters in plain language, and keep jargon (assertions, frontmatter, progressive disclosure) explained on first use unless the user clearly knows it. Severity-order everything — nobody acts on a flat list of 30 findings.

Be kind about the existing skill. Someone wrote it, possibly the person you're talking to. "This section is generic — let's capture what you actually know" lands better than "this is low quality."

## Reference files

- [references/audit-rubric.md](references/audit-rubric.md) — the full quality rubric with scoring guidance and examples of weak vs. strong for each dimension. Read before Step 3.
- [references/failure-modes.md](references/failure-modes.md) — symptom → root cause → fix mapping for the five common complaints. Read when the user reports a specific symptom.
- [references/gap-elicitation.md](references/gap-elicitation.md) — question banks for extracting the heuristics, intent, and examples a generic skill is missing. Read before Step 4.
- `scripts/audit_skill.py` — deterministic structural checks. Run in Step 2. Stdlib-only, non-interactive, `--help` available.
