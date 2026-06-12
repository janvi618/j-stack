# Audit Rubric

Score each dimension Strong / Adequate / Weak, with quoted evidence from the skill. Lead the report with the Weak findings that most plausibly explain the user's symptom.

## 1. Description as router

The description is the primary trigger mechanism — Claude decides whether to consult the skill from name + description alone.

- **Strong**: First sentence densely states what the skill does and its primary deliverable. Includes the artifacts (file types, document types) and natural phrases real users say. States non-goals ("Do not use for...") anchored on the primary deliverable. Well under 1024 characters total.
- **Adequate**: What + when present but vague on trigger vocabulary, or missing negative scope.
- **Weak**: Generic ("Helps with documents"), first-person, describes the skill's philosophy instead of its triggers, or so broad it collides with everything.

Weak → strong example:
- Weak: `Helps with financial documents.`
- Strong: `Creates or revises spreadsheet-based financial analyses with formulas, formatting standards, and validation checks. Use when the primary deliverable is an .xlsx/.csv output — building models, adding calculated columns, fixing formula errors. Do not use when the deliverable is a Word memo, HTML report, or standalone script.`

Note the balance: pushy on triggers (fights under-triggering, the more common failure), precise on non-goals (fights over-triggering). Both, not either.

## 2. Output contract

- **Strong**: The skill states the primary deliverable, its required sections/fields, where to save it, and what to report back.
- **Weak**: The skill describes a process but never says what artifact should exist at the end. Symptom downstream: inconsistent outputs, because every invocation invents its own definition of done.

## 3. Workflow, not essay

- **Strong**: Stepwise default workflow; explicit decision points ("if X, read references/branch-x.md"); consistent terminology throughout; degrees of freedom matched to fragility — exact commands for brittle operations (file format internals, migrations), heuristics for judgment work (reviews, synthesis).
- **Weak**: Paragraphs of background and philosophy; "be thorough and careful" filler; rigid checklists imposed on high-variance judgment tasks, or vague vibes offered for brittle ones.

## 4. Intent present (the why)

- **Strong**: Rules carry their rationale ("lead with the risk section because the exec audience reads only the first paragraph"). The model can extrapolate to unlisted situations.
- **Weak**: Walls of ALWAYS/NEVER with no reasoning. These overfit: they handle the listed cases and fail the unlisted ones, and they tend to accumulate as patch-fixes over time. An all-caps MUST is a yellow flag to investigate, not automatically a defect — some constraints really are absolute — but each one should be checked: would explaining the why serve better?

## 5. Validation loops

- **Strong**: Fragile operations end with validate → fix → re-validate, ideally with a bundled script doing the deterministic check (Anthropic's docx and xlsx skills are the model: validate-and-repair, recalculate-and-check-error-cells).
- **Weak**: Fragile operations with no check (silent corruption risk) — or the inverse defect, validation gates bolted onto subjective work where human judgment is the real check.

## 6. Progressive disclosure

- **Strong**: SKILL.md body contains only always-needed material (roughly ≤500 lines); branch-specific detail lives in references; every reference is explicitly pointed to from SKILL.md with guidance on *when* to read it; references are one level deep; long reference files (>300 lines) have a table of contents.
- **Weak**: Everything in one giant SKILL.md (expensive on every invocation, and in Claude Code the body stays in context for the whole session); or orphan reference files never mentioned in SKILL.md (dead weight, never loaded); or references nested several levels deep (the model gets lost).

## 7. Script quality (if scripts are bundled)

- **Strong**: Non-interactive; accurate `--help` with example invocation; useful errors that say what went wrong and what to do; clean structured output to stdout, diagnostics to stderr; dependencies explicit; stdlib-preferred if the skill might run on the Claude API (no network, no runtime installs there).
- **Weak**: Interactive prompts (an agent hangs on these); bare tracebacks; undeclared imports; scripts that solve half the problem and punt the rest to improvisation.

## 8. Evidence of expertise — the decisive dimension

The test: **could Claude have written this skill with zero input from anyone who actually does the work?** If yes, the skill adds little over a blank prompt, no matter how well-structured it is.

- **Strong**: Specific decision rules that surprise an outsider ("if legal hasn't replied in 48 hours, treat it as a no and escalate"); failure warnings from real incidents; real gold examples; thresholds and tells that only experience produces; named non-obvious edge cases.
- **Adequate**: Some real specifics mixed with generic best practice.
- **Weak**: Could be the first page of any business book. "Know your audience. Be concise. Check your work."

Weak here cannot be fixed by editing — it requires elicitation (Step 4 of the workflow). Flag it honestly: "Sections 2 and 4 are generic; the fix is a 20-minute conversation with whoever does this task, not a rewrite by me."

## Reporting format

For each finding: dimension, severity, quoted evidence, why it matters (one sentence), proposed fix. Order by impact on the user's reported symptom, then by severity. Cap the headline report at the ~7 findings that matter; park the rest in a "minor" section.
