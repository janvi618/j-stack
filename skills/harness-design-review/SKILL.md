---
name: harness-design-review
description: A structured checklist for designing and reviewing the "harness" around an LLM agent — the runtime infrastructure of context, memory, tools, execution, verification, multi-agent coordination, and safety governance that surrounds the base model. Use this skill whenever the user is designing, building, reviewing, critiquing, or debugging an agentic system, agent framework, coding agent, GUI/OS automation agent, embodied agent, or any multi-step LLM pipeline that acts through tools or executes code — even if they don't use the word "harness." Trigger phrases include "review my agent architecture," "what am I missing in my agent design," "help me design an agent system," "why is my agent unreliable," "audit this agentic pipeline," or any discussion of agent planning, memory, tool use, verification, or multi-agent orchestration. Apply it proactively when a user shares an agent design and seems to want to know whether it is sound, complete, or production-ready.
---

# Harness-Design Review

## What this skill is for

When an LLM is embedded in an agent, its behavior is no longer determined by the model alone. It is shaped by the **harness**: the surrounding runtime that decides what context the model sees, which tools it can call, how many retries it gets, what verifies success, how state is shared across agents, and which actions require human approval. Most agent failures in practice are harness failures, not model failures — a weak verifier, stale context, an unsafe tool, or inconsistent shared state.

This skill provides a checklist for evaluating a harness as a first-class system component. Use it to find the gaps that final-task-success metrics hide.

The framework derives from the survey *Code as Agent Harness* (Ning et al., 2026, arXiv:2605.18747) and its seven open-problem dimensions. It is a design lens, not a rigid spec — adapt the depth of each dimension to what the user is building. A single-agent coding helper does not need the multi-agent section; a text-only pipeline does not need the multimodal section.

## How to use it

1. **Understand what they're building first.** Identify the agent's domain (coding, GUI/OS, embodied/robotics, scientific, enterprise/DevOps, general), whether it is single- or multi-agent, whether state is text-only or multimodal, and how consequential its actions are (sandboxed experiment vs. production/financial/physical). This determines which dimensions matter most.

2. **Walk the seven dimensions below**, but don't recite all of them mechanically. Lead with the dimensions most relevant to their system and most likely to be weak. For a review, surface concrete gaps; for a design, offer concrete patterns.

3. **Close against the four properties.** A strong harness is *executable* (decisions grounded in code, tools, tests, environments), *inspectable* (plans, state, provenance, and failure causes are exposed), *stateful* (task-relevant info survives long trajectories and multiple agents), and *governed* (autonomy is bounded by permissions, verification, and accountability). Use these as a final sanity check: which of the four is weakest here?

4. **Be specific and prioritized.** Don't hand back the whole checklist as a wall of bullets. Name the two or three things that matter most for *their* system, explain *why* each is a risk, and give an actionable next step.

For the detailed prompts under each dimension, and for the domain-specific emphases, read `references/dimensions.md`.

## The seven dimensions (summary)

1. **Evaluation & oracle adequacy** — Are you measuring the harness, or just final task success? Final-success metrics conflate model quality, harness quality, tool reliability, and environment difficulty. Look for harness-level signals: trajectory efficiency (tool calls, tokens, edits, wall-clock), verification strength (coverage, false-acceptance rate), recovery ability, state consistency, safety compliance, and replayability. The deeper question is *oracle adequacy*: does the evaluator capture the real task, or a narrow executable proxy the agent can game?

2. **Verification beyond execution** — Execution feedback creates false confidence: a green test is not the full spec. Treat verification as a stack with explicit scope, not a single pass/fail gate. Each check (unit/integration/property tests, fuzzers, static analyzers, type checkers, security scanners, runtime monitors, human review) should declare what it verifies, what it cannot, and how much confidence it gives. Route feedback by type — compiler errors trigger syntax repair, test failures trigger behavioral diagnosis, coverage gaps trigger test generation. The harness should know when a signal is strong enough to act on.

3. **Self-evolving harnesses without regression** — If the harness adapts itself (tuning prompts, memory, tools, topology), treat every change like a code change to a safety-critical runtime. Each mutation should carry a *change contract*: which component changes, which failure it targets, what it predicts, which invariants it must preserve, what would falsify it, and how to roll back. The risk is silent regression — improving a benchmark while weakening safety, raising cost, hiding failures, or breaking rare-but-important cases. Guard with held-out regression suites, safety invariants, canary deployment, and rollback semantics.

4. **Shared program state & conflict resolution (multi-agent)** — When multiple agents read and write shared artifacts, synchronization alone doesn't give consistency: agents sync files but not *assumptions*. One plans from a stale snapshot, another tests a newer patch, a third remembers an obsolete invariant. Push toward transactional state where each action declares its read set, write set, assumptions, version dependencies, and verifier obligations. Conflicts arise not just in file diffs but in plans, tests, retrieved evidence, permissions, and interpretations of the goal — so resolution must be semantic, with a clear line between what merges automatically and what needs human judgment.

5. **Human-in-the-loop safety & accountability** — In consequential settings, safety cannot live in a prompt. The harness must act as a *safety governor* between model intent and real-world effect: classify actions by risk, enforce permission tiers, hard-deny constraint violations, and require human approval for irreversible or externally consequential actions (credentials, security-critical edits, user data, deployment, financial/medical output, physical control). Permissions must be context-sensitive — the same command is safe in a sandbox and unsafe in production. Critically, human decisions should become *durable harness state*: every approval, rejection, and policy exception updates future permissions and is logged as an auditable transition (what was proposed, what evidence was shown, who decided, what changed).

6. **Multimodal harness state** — If the critical state is visual or physical (screenshots, accessibility trees, camera/depth/force/tactile signals, plots, molecular structures), the harness cannot treat perception as passive input. It must manage multimodal observations as persistent, queryable, verifiable state. Watch for: multimodal context compression that keeps *task-relevant* evidence (not just fewer tokens); grounding contracts that tie each action to the visual evidence it depends on (bounding box, element ID, object pose, frame index) and verify the grounded state actually changed; and multimodal verification stacks where each signal exposes its scope and uncertainty (a detector verifies localization, not task completion).

7. **Toward a science of harness engineering** — Step back: the object of study is the whole closed loop — context, memory, tools, execution, feedback, safety, coordination, evaluation — not the model or the program in isolation. Strong systems need benchmarks that expose long-horizon failures, telemetry that makes trajectories auditable, metrics that isolate harness components, and design principles for operating safely in persistent program worlds.

## What good output looks like

For a **review**, structure the response as: (a) a one-line read of what they've built and its risk profile; (b) the two or three weakest dimensions, each with the specific gap, why it bites, and a concrete fix; (c) a closing note on which of the four properties (executable/inspectable/stateful/governed) is most underserved.

For a **design-from-scratch** request, work the other way: start from the domain and risk profile, recommend a baseline for each relevant dimension, and flag the one or two dimensions that will be hardest for their case so they design for them early.

Avoid dumping all seven dimensions when only three are load-bearing. The value is in prioritization and specificity, not coverage.
