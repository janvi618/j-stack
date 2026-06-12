# Failure Modes: Symptom → Root Cause → Fix

Start from the user's complaint. Each symptom has a small set of likely causes — check them in order of probability, gathering evidence before fixing. The general rule: diagnose with the cheapest test first (read the description, read the body), and confirm fixes empirically (before/after runs), not by inspection alone.

## 1. "It doesn't trigger when it should"

Most common failure. Likely causes, most probable first:

- **Description lacks the user's actual vocabulary.** The description says "processes financial workbooks"; users say "my xlsx," "spreadsheet," "add a profit margin column." Fix: add the artifact words (file extensions, document types) and natural intent phrases. Pushiness helps: "use whenever the user mentions X, Y, or Z, even if they don't explicitly ask for [the formal term]."
- **The test prompts are too trivial.** Claude only consults skills for tasks it can't trivially handle alone. "Read this PDF" won't trigger a PDF skill no matter how good the description is. Before concluding the description is broken, check whether the failing prompts are substantive, multi-step asks. If the user's real-world usage is genuinely simple one-liners, the honest answer may be that a skill is the wrong tool.
- **A sibling skill is winning the route.** Another installed skill shares the trigger vocabulary and Claude picks it instead. Fix on both sides: sharpen each description's primary deliverable and non-goals so the boundary is explicit.
- **"When to use" info is buried in the body.** Triggering decisions are made from name + description only; the body isn't read until after the skill triggers. Move all trigger context up into the description.

## 2. "It triggers when it shouldn't"

- **Description is too broad / keyword-baity.** A skill described as "helps with documents" will fire on everything documentish. Fix: anchor the description on the primary deliverable and add explicit negative scope ("Do not use for X, Y").
- **Genuine overlap with an adjacent skill.** Two skills legitimately cover neighboring territory. Fix: negotiate the boundary in both descriptions, or consolidate the skills.
- **The skill should be manual-only.** Some workflows should never auto-fire (destructive operations, expensive pipelines). In Claude Code, `disable-model-invocation: true` exists for exactly this — but it's a Claude Code-only extension; on other surfaces the fix is description precision.

## 3. "Output is inconsistent or wrong"

- **No output contract.** The skill never defines done, so each invocation invents its own. Fix: add an explicit deliverable, required structure, save location, and report-back expectations.
- **No workflow or decision points.** The body is descriptive prose; the model improvises a different path each time. Fix: stepwise default workflow with explicit branches.
- **No validation loop on a fragile operation.** Errors happen and nothing catches them. Fix: validate → fix → re-validate, with a script where the check is programmatic.
- **Rules without rationale failing on unlisted cases.** The skill handles its enumerated examples and breaks on variants. Fix: replace patch-rules with principles plus the why.
- **The expertise is missing.** The skill is structurally fine but generically informed, so outputs are correct-but-mediocre. This is the elicitation case — see gap-elicitation.md. No amount of formatting fixes it.

## 4. "It's bloated / slow / expensive"

- **Everything in SKILL.md.** The whole body loads on every trigger (and in Claude Code it persists in context for the session, surviving compaction). Fix: keep always-needed material in the body, move branch detail to explicitly-pointed-to references one level deep.
- **Dead weight.** Sections that aren't pulling their weight — read the transcripts of real runs; if an instruction never changes behavior, or sends the model on unproductive detours, cut it and test.
- **Repeated improvised work.** If every invocation writes the same helper code from scratch, bundle it once as a script. Script output costs context; script source doesn't.

## 5. "The bundled scripts fail"

- **Interactive prompts.** The agent hangs at "continue? [y/n]". Fix: flags and arguments only.
- **Hidden dependencies.** Works on the author's machine; fails where pandas isn't installed. Fix: declare deps explicitly, check-and-report at runtime, prefer stdlib if the skill targets the Claude API (no network, no runtime installs there).
- **Unhelpful errors.** A bare traceback gives the agent nothing to self-correct with. Fix: catch foreseeable failures and emit what-went-wrong + what-to-do.
- **Wrong environment assumptions.** Paths, OS, or tool availability assumed from the authoring environment. Fix: test on the surface the skill actually runs on.

## When the symptom is "all of the above"

A skill failing on every axis is usually a knowledge problem wearing structural symptoms — it was written fast by someone without the expertise, padded with generic best practice to look complete. The efficient path is not to fix the findings one by one but to re-elicit: treat the existing skill as a draft interview transcript, run the gap-elicitation process with the real expert, and rewrite around what you learn. Tell the user this honestly; it saves them three polish iterations on a hollow core.
