# Authoring Guide: Scripts, Portability, Naming, and Lifecycle

Read this when bundling scripts into a skill, or when the skill is destined for team or production use rather than personal use.

## Script quality standards

Scripts exist in skills to make fragile operations deterministic. A script that's flaky or hostile to agents defeats the purpose. Standards:

- **Non-interactive.** No prompts mid-run, no "press y to continue." Take everything as arguments or flags. An agent stuck at an interactive prompt just hangs.
- **Working `--help`.** The agent will often read `--help` instead of the source. Make it accurate and include an example invocation.
- **Useful errors.** Fail with a message that says what was wrong and what to do ("missing column 'revenue' — expected columns: revenue, costs, region"), not a bare traceback. Good errors let the agent self-correct; bad ones cause improvised workarounds.
- **Clean structured output to stdout.** If downstream steps consume the output, make it JSON or clearly delimited. Diagnostics go to stderr.
- **Explicit dependencies.** Declare imports at the top, list non-stdlib requirements in the skill (compatibility frontmatter or a comment block). Never assume a package is present.
- **Solve, don't punt.** If the operation can be fully handled in the script, handle it there — don't emit half a result and instructions for the model to finish manually.

## Runtime environments differ across surfaces

This is the most common silent portability failure:

| Surface | Network | Package installs | Notes |
|---|---|---|---|
| Claude API (code execution) | **None** | **None at runtime** | Stdlib-only or pre-bundled code only |
| claude.ai | Limited/allowlisted | Often available (pip/npm) | Varies by org settings |
| Claude Code | Host-style access | Available | Avoid global installs; respect the user's environment |

Practical rule: if the skill might ever be uploaded to the API, write scripts stdlib-only where feasible. If a dependency is essential, name it loudly in the skill body and have the workflow check for it before relying on it ("if pandas is missing, say so explicitly before proceeding").

Claude Code-specific frontmatter (`when_to_use`, `disable-model-invocation`, `user-invocable`, `allowed-tools`, `paths`, `context: fork`, `agent`) is powerful but non-portable. Use it only when deliberately building a Claude Code-only skill; otherwise stay on the open standard (explicit `name` + `description`, markdown body, one-level-deep references).

## Naming conventions

- Lowercase, hyphenated: `finance-modeling`, not `FinanceModeling` or `finance_modeling`.
- Directory name and frontmatter `name` should be identical — different surfaces derive the invocation name from different places, and keeping them aligned avoids surprises.
- Avoid vague names: `helper`, `utils`, `tools`, `assistant`. Gerund or noun-phrase names describing the work are best: `processing-pdfs`, `repo-review`, `brand-comms`.

## Lifecycle and maintenance (team/production skills)

A skill library without maintenance becomes an authoritative record of how things *used* to be done — worse than no record, because it's trusted. Minimum viable lifecycle:

- **Source in Git.** The `.skill` file is a build artifact; the repo is the source of truth.
- **Owner and last-reviewed date.** Record them (in the repo, a registry, or a comment in SKILL.md). Unowned skills rot invisibly.
- **Pin versions in API production.** Custom API skills are versioned; production pipelines should pin and promote deliberately, re-running the eval suite before promotion, with a rollback path.
- **Re-validate on model upgrades.** Skills are tuned against model behavior; behavior shifts between model versions. Re-run the eval set (this skill's testing loop makes that cheap) whenever the underlying model changes, and on a recurring cadence (quarterly is a sane default) for skills encoding business processes.
- **Watch for overlap.** As a library grows, skills start competing for the same triggers, and recall degrades — too many simultaneously active skills dilute each other in the metadata listing. When adding a skill, check which existing descriptions share its trigger vocabulary; sharpen non-goals on both sides, or consolidate. Should-not-trigger eval queries are the cheap regression test for this.
- **Audit before installing third-party skills.** Review scripts, references, and any network behavior. Skills execute code and shape model behavior; treat them with the same suspicion as any dependency.
