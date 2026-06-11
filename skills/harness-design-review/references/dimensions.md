# Harness-Design Review — Detailed Dimensions

Read this when you need the granular review prompts for a dimension, or when tailoring the review to a specific agent domain. Table of contents:

1. Evaluation & oracle adequacy
2. Verification beyond execution
3. Self-evolving harnesses without regression
4. Shared program state & conflict resolution
5. Human-in-the-loop safety & accountability
6. Multimodal harness state
7. Science of harness engineering
8. Domain-specific emphases
9. The four properties as a final gate

---

## 1. Evaluation & oracle adequacy

Diagnostic questions:
- What exactly decides "success" in your system, and could the agent satisfy it without solving the real task? (e.g., passing a weak test suite, a scripted GUI checker that ignores unsafe intermediate actions, a simulator pass that isn't physically valid)
- When the agent does well or badly, can you tell whether it was the model, the retrieval, the tools, the feedback quality, or the environment? If those are conflated, you can't improve the right thing.
- Do you measure any of: trajectory efficiency (tool calls, tokens, edits, executions, wall-clock); verification strength (test coverage, oracle diversity, false-acceptance rate); recovery ability (can it diagnose and repair after an invalid action); state consistency (do memory, repo state, traces, and agent beliefs stay synchronized); safety compliance (are permissions, sandboxes, approval gates respected); replayability (can the full trajectory be reconstructed from logs)?
- Is the bottleneck really "we need a harder benchmark," or "our oracle doesn't capture the intended task"?

The reframe to offer: evaluate the harness as a runtime system, not just the answer it produced.

## 2. Verification beyond execution

Diagnostic questions:
- Does a single pass/fail signal terminate the loop? If so, the agent will optimize against whatever that signal actually measures — which may be narrower than the spec.
- For each verification artifact you use, can you state what it verifies, what it explicitly does NOT verify, and what confidence it provides? (Unit tests miss untested paths; static analyzers over-approximate; GUI checkers miss bad intermediate actions; sim passes hide physical risk.)
- Is feedback routed by type, or treated uniformly? Compiler error → local syntax repair. Test failure → behavioral diagnosis. Coverage gap → test generation. Inconsistent reviewer comments → arbitration.
- For self-repair loops especially: if the verifier is weak, the agent *learns the wrong lesson*. Is the verifier strong enough to train against?

Pattern to suggest: make every accepted action carry an "evidence bundle" — the checks run, the assumptions preserved, the untested regions, the remaining risks. Verification as an inspectable contract, not a final gate. Also: feedback calibration, independent/differential/metamorphic testing, uncertainty-aware critics.

## 3. Self-evolving harnesses without regression

Only relevant if the system modifies its own harness (auto-tuning prompts, memory format, tool schemas, permission rules, agent topology). If it's fully manually configured, note that fixed harnesses can be suboptimal across diverse tasks, but don't force this dimension.

Diagnostic questions:
- Does each automatic change carry a *change contract*: which component is modified, which failure mode it targets, what improvement it predicts, which invariants it must preserve, what evaluation could falsify it, how it rolls back?
- Could a change improve a benchmark while: increasing hallucinated evidence, weakening permission boundaries, raising token cost, hiding failures, or regressing on rare-but-important tasks? Each of these is a real, documented failure mode of naive self-improvement.
- Do you have held-out regression suites, safety invariants enforced *during* evolution, canary deployment, rollback semantics, and causal evidence for *why* an edit helped?
- Is "improvement in the harness" separated from "improvement in the base model"? Conflating them leads to false attribution.

The principle: a harness mutation is a code change to a safety-critical runtime. The goal is not a harness that changes often, but one that changes only when it can justify the change.

## 4. Shared program state & conflict resolution (multi-agent only)

Skip for single-agent systems.

Diagnostic questions:
- How do agents share state today — sequential handoff, shared logs, file-only, a blackboard, repository memory, explicit belief-state sync? Most early systems sync *artifacts* but not *assumptions*.
- Can these failure cases occur: one agent plans from an old snapshot while another tests a new patch; an agent retains an obsolete invariant; a human reviewer adds a constraint that isn't propagated; two agents duplicate a subtask; agents hold inconsistent views of tool authority or of the user's actual goal?
- Does each action declare a read set, write set, assumptions, version dependencies, verifier obligations, and conflict policy — or do agents just append to a common log?
- Is conflict detection purely textual (file diffs), or semantic (plans, tests, retrieved evidence, permissions, memory entries, latent requirements)?
- Where is the line between conflicts that resolve automatically (semantic merge, dependency-aware locking, belief reconciliation, re-verification after merge) and those that need human judgment?

Useful analogies to draw on: version control, databases, CRDTs, build systems — but note agentic systems add conflicts those tools don't see (incompatible plans, stale memories, divergent goal interpretations). Metrics beyond merge correctness: semantic regression rate, rollback frequency, conflict recurrence, cost of human intervention.

## 5. Human-in-the-loop safety & accountability

Scale this to how consequential the actions are. A disposable sandbox needs little; anything touching production systems, private data, external users, physical devices, money, health, or compliance needs the full treatment.

Diagnostic questions:
- Is safety encoded only as a natural-language instruction to the model? If so, it's not enforceable — it needs to live in the harness as a governor that can override model intent.
- Is there a multi-tier permission model? Low tier: read files, inspect logs, run static analysis. Higher tiers: edit local files, run sandboxed code, access network, call external APIs, modify shared repos, affect production. Does each tier specify allowed actions, constraints, audit logs, rollback, and human-approval gates for high-risk operations?
- Are permissions *context-sensitive*? The same command is safe in a sandbox and dangerous in production; the same network request is benign during doc retrieval and risky when it transmits local state. Permissions should depend on arguments, environment state, data sensitivity, and expected side effects — not just tool identity.
- Which actions require human approval before reaching the world? At minimum: requesting credentials, modifying security-critical code, accessing user data, deploying, issuing financial/medical recommendations, controlling physical equipment.
- Is human feedback *durable harness state*? Each approval/rejection/exception/correction should update permission rules, escalation policy, verification criteria, and future memory — not vanish after one prompt.
- Are high-stakes approvals auditable transitions: what was proposed, what evidence was shown, what risks were surfaced, who approved, what responsibility boundary changed?

Open sub-problems to mention if relevant: policy specification, side-effect prediction, sandbox-escape prevention, secret handling, secure tool schemas, reversible execution, and the autonomy-vs-safety tradeoff. The frame: reliable systems need *executable accountability* — a layer that filters, vetoes, escalates, and records before actions reach the real world.

## 6. Multimodal harness state

Skip for text-only systems (prompts, files, logs, tool outputs, tests, traces). Apply when critical state is visual/physical.

Diagnostic questions:
- Is perception treated as passive model input, or as persistent, queryable, verifiable state?
- **Compression**: visual observations are large and mostly irrelevant (a screenshot has hundreds of elements but one matters; a trajectory has thousands of frames but a few are task-critical). Does compression preserve task-relevant evidence, or just cut tokens? A multi-level memory helps: raw frames as immutable evidence; object/region/element/pose annotations as structured intermediate state; compact symbolic summaries for retrieval and planning.
- **Grounding**: does each action carry a grounded reference to the evidence it depends on (bounding box, object ID, UI element, frame index, pose)? After execution, does the harness verify the *grounded state* actually changed as intended, rather than trusting the model's self-report? (A button can look clicked without triggering the state transition; a grasp can look successful while unstable.)
- **Multimodal verification stack**: combine visual state checks, object tracking, OCR / UI-tree inspection, simulator state, physical sensors, tactile feedback, task-specific validators. Each signal should expose scope and uncertainty (a bounding-box detector verifies localization, not completion; a sim verifies position, not physical robustness).
- **World vs. action modeling**: does the harness predict how the world should change after an action and compare to the observed outcome? Prediction-error signals are essential for recovery in embodied settings, where failures (occlusion, slippage, collision, unreachable pose, violated precondition) often come with no explicit error message.
- **Skill evolution**: in GUI/embodied domains, reusable skills aren't just text — they couple a multimodal precondition, an executable action pattern, and an expected postcondition (what to see/sense before, what to execute, what change should follow). Should skills evolve from successes, failures, and human corrections while keeping their grounding evidence?

## 7. Science of harness engineering

Use this as the closing zoom-out, not a separate checklist. The point: the unit of analysis is the complete closed-loop system. Progress needs benchmarks that expose long-horizon failures, telemetry that makes trajectories auditable, metrics that isolate harness components, and design principles for persistent program worlds. If a user's system is strong on individual dimensions but has no telemetry / no way to audit a trajectory / no component-level metrics, that's the gap to name.

---

## 8. Domain-specific emphases

Lead with the dimensions that bite hardest in each domain.

- **Coding agents / repo-level SWE**: dimensions 1 and 2 dominate. The classic failure is passing visible tests while exploiting a weak suite (oracle inadequacy + over-trust in execution). If multi-agent (planner/coder/tester/reviewer), add 4. If it auto-tunes, add 3.
- **GUI / OS automation**: 6 (grounding, did the click do what was intended) and 5 (intermediate actions that a scripted checker misses can be unsafe). 1 matters because GUI checkers easily miss undesirable intermediate states.
- **Embodied / robotics**: 6 is central (physical feedback is implicit, delayed, ambiguous; prediction-error recovery matters) and 5 (physical safety, irreversible actions). Sim success ≠ physical safety (dimension 1).
- **Scientific discovery**: 2 and 1 (a script can execute cleanly while encoding invalid assumptions; execution validity ≠ scientific validity). 5 for wet-lab / experimental control.
- **Enterprise / DevOps**: 5 dominates (production systems, secrets, compliance, irreversible deploys), with 4 if multiple agents touch shared infra, and 1 for auditability/replayability.
- **General / personal assistants & recommendation**: 5 (user data, consequential actions) and 1 (what does success even mean here, and can it be gamed).

## 9. The four properties as a final gate

After walking the relevant dimensions, sanity-check the whole system against the four properties a strong harness combines. They map loosely onto the dimensions but are a useful independent lens:

- **Executable** — decisions are grounded in code, tools, tests, and environments (not just model assertion).
- **Inspectable** — plans, state, provenance, and failure causes are exposed and auditable.
- **Stateful** — task-relevant information is preserved across long trajectories and multiple agents.
- **Governed** — autonomy is constrained by permissions, verification, and accountability.

Ask: which of these four is weakest in the system under review? That single question often surfaces the highest-leverage improvement.
