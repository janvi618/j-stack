---
name: token-optimization
description: Diagnose and reduce token cost, latency, and quality problems in LLM systems — prompts, RAG pipelines, agents, multi-agent harnesses, and reusable skills. Use this skill whenever the user wants to cut API costs, speed up time-to-first-token, fix "context rot" or quality degradation in long contexts, design a caching or model-routing strategy, optimize a RAG/retrieval setup, tighten tool definitions or tool outputs, budget tokens across an agent workflow, or audit a prompt or pipeline for waste — even if they only say something vague like "this is getting expensive," "my agent burns too many tokens," or "responses are slow." Also trigger for questions about prompt caching, LLMLingua/prompt compression, semantic caching, chunking, reranking, compaction, agent memory, or progressive disclosure. Do not use for skill-quality audits, skill creation, or agent-architecture soundness reviews (other skills cover those) — this skill's lens is strictly token economics — cost, latency, context budget.
---

# Token Optimization for LLM Systems

## Core principle (read this first)

The goal is **not** minimizing tokens. It is maximizing **information density** — the smallest set of *high-signal* tokens that maximize the likelihood of the desired outcome. "Minimal" does not mean "short." A terse prompt that drops necessary signal is worse, not better.

Three facts drive every decision in this skill:

1. **Tokens are cost.** Billing is per-token; output runs ~4–5x the price of input (Claude holds a 1:5 input:output ratio). Agents use ~4x the tokens of chat; multi-agent systems ~15x.
2. **Tokens are latency.** Time-to-first-token scales with input length (the model must prefill the whole prompt). Attention is quadratic in sequence length.
3. **Tokens are quality.** Past a threshold, *more* context makes answers *worse* — "context rot" and "lost in the middle" are measured across every frontier model. Dumping everything into a 1M-token window is both expensive and lower-quality.

So the discipline is **spending tokens where they pay off** and cutting them everywhere else — never optimizing cost blind to quality.

## The anti-pattern you'll see most

**Over-stuffing context** under the belief that "bigger context = better answers": bloated static system prompts, verbose tool returns read token-by-token, full conversation history, full-document injection, every edge case crammed into the system message. Research shows the opposite past a threshold. If the user's problem is cost/latency/quality and they have a large context, suspect over-stuffing first.

## How to use this skill

This is a **diagnostic-and-design** skill, not a fixed pipeline. Figure out where the user is, then reach for the right techniques. The reference files hold the depth; load them as needed (this is itself progressive disclosure — don't pull all of them into context at once).

### What the user should walk away with (output contract)

Unless they ask for something narrower, a token-optimization engagement delivers three things:

1. **A baseline diagnosis** — where the tokens actually go (input vs output, by feature/workflow, p95 and mean), or, if nothing is instrumented, instrumentation as the explicit first recommendation.
2. **Recommendations ranked by leverage**, each carrying its tradeoff: the technique, the expected impact (directional), the when-NOT condition, and the new failure mode it introduces. Never hand over a list of optimizations without their risks — that's how silent quality regressions ship.
3. **A sequenced rollout plan** following the leverage ordering below, with each step gated on a quality eval, plus what to monitor afterward (e.g., cache hit rate, p95 cost, task success).

A response that names techniques without the diagnosis, the tradeoffs, or the measurement gates is incomplete.

### Step 1 — Diagnose before prescribing

Never optimize what you haven't measured. Establish (or ask the user for) a baseline:

- **Where do the tokens go?** Break down by input vs output, by feature, by model. Track **p95, not just the mean** — a workload where 5% of requests hit 50K tokens looks cheap on average and expensive on the invoice.
- **Which workflows cost most?** Rank by `volume × tokens × price`. Agent pipelines first — a task that costs $0.10 in isolation can cost $2–5 through an agent loop.
- **What's the quality baseline?** Answer quality, hallucination rate, task success. You cannot safely cut what you haven't measured.

If the user hasn't instrumented anything, that *is* the first recommendation. See `references/metrics-and-evaluation.md`.

### Step 2 — Match the symptom to the technique

| If the symptom is… | Reach for… | Proven? |
|---|---|---|
| High cost, stable repeated prefix | **Prompt caching** (90% input discount) | Proven, highest leverage |
| High cost, mixed query difficulty | **Model routing** (small/large orchestration) | Proven |
| Cost + quality on a large corpus | **RAG**: chunking, hybrid retrieval, reranking | Proven |
| Agent reads huge tool blobs | **Compact structured tool outputs** (IDs/refs/schemas) | Proven |
| Long sessions degrading (rot) | **Compaction / rolling summaries** | Proven |
| Long-horizon / unbounded tasks | **Agent memory / externalization** | Proven→emerging |
| Long, repetitive, low-stakes prompts | **Prompt compression** (LLMLingua) | Emerging, higher variance |
| Repetitive FAQ-style queries | **Semantic / response caching** | Emerging, correctness risk |
| Async, non-urgent batch work | **Batch API** (flat 50% off) | Proven |
| Slow TTFT on long prompts | **Caching** (keeps latency ~proportional to output) | Proven |
| Bloated multi-agent harness | **Subagent isolation + circuit breakers** | Proven |
| Reusable logic in every prompt | **Skills with progressive disclosure** | Proven |

**Sequencing recommendation** (highest leverage / lowest risk first): instrument → minimize & reorder the prompt for caching → add caching → fix tool outputs → optimize retrieval → add routing → add compaction/memory → (only if warranted) compression/semantic caching. Gate each step behind an eval.

### Step 3 — Read the relevant reference, then apply

The four context "buckets" (Anthropic's framing) organize the techniques:
- **Select** what enters context (pruning, retrieval, minimal prompts) → `references/techniques-select-and-retrieve.md`
- **Compress** (summarization, compaction, prompt compression, compact outputs) → `references/techniques-compress.md`
- **Write/externalize** (memory, artifacts) → `references/techniques-write-and-isolate.md`
- **Isolate** (subagents, decomposition) → `references/techniques-write-and-isolate.md`

Plus the delivery layer (**cache, route, batch**) → `references/techniques-deliver.md`

Each technique entry follows the same shape: *what it is · when to use · when NOT to · benefits · risks · difficulty · impact.* Always surface the **when-NOT** and the **risk** — most token "optimizations" add a failure mode, and the user needs to know the tradeoff.

## Reference files

Load only what the task needs.

- **`references/techniques-deliver.md`** — Prompt caching (cache-aware layout, the static→dynamic ordering rule, the "relocation trick," breakpoint mechanics), model routing (RouteLLM and friends), batch API, avoiding long-context surcharges. **Start here for cost problems.**
- **`references/techniques-select-and-retrieve.md`** — System-prompt minimization ("right altitude"), few-shot curation, just-in-time retrieval, and full RAG optimization (chunking, hybrid + contextual retrieval, RRF, reranking, the <200K-token "just stuff it" threshold).
- **`references/techniques-compress.md`** — Compact structured tool outputs & function calling, summarization/compaction, token-level prompt compression (LLMLingua family).
- **`references/techniques-write-and-isolate.md`** — Agent memory (MemGPT tiers, artifact pattern), subagent isolation, multi-step decomposition, and semantic/response caching.
- **`references/harness-and-skills.md`** — Designing the agent harness for token efficiency (cache-aware layout, tool-budget discipline, circuit breakers, the 15x multi-agent tax, context budgeting) **and** building reusable skills with progressive disclosure (three-tier loading, <500-line SKILL.md, code-as-tool-vs-docs).
- **`references/metrics-and-evaluation.md`** — What to measure (token/cost/latency/quality metrics per task), OpenTelemetry GenAI conventions, observability tooling (LangSmith, Langfuse, Helicone), and the full step-by-step implementation playbook.
- **`references/examples-and-checklists.md`** — Concrete before/after rewrites (bloated prompt, verbose tool result, poor chunking, bloated skill, multi-agent redesign), a worked context-budget table, the review checklist, and the architecture-pattern tradeoff table.

## Architecture tradeoffs (quick reference)

The full table with "when A wins / when B wins" is in `references/examples-and-checklists.md`. The key tension: **every optimization that externalizes or compresses adds engineering complexity and a new failure mode.** The 1M-token window is a convenience, not a license. On genuinely hard, parallelizable tasks, spending more tokens *does* buy quality (token usage alone explained ~80% of the variance in Anthropic's multi-agent research performance) — so the art is paying where it pays off.

## What to remember

1. Optimize for **information density**, not token count.
2. **More context can hurt** — context rot and lost-in-the-middle are real and universal.
3. **Caching is the highest-leverage cost lever** — but only with a stable prefix; static content first, dynamic last; monitor the hit rate.
4. **Route by difficulty** — most queries don't need your most expensive model.
5. **Compact, structured tool outputs** — IDs and schemas, not blobs.
6. **Retrieve, don't stuff** — hybrid + contextual RAG with reranking beats full-context on cost, latency, and precision for large corpora.
7. **Externalize memory and compact history** for long-horizon agents.
8. **Progressive disclosure for skills** — load triggers, not full bodies.
9. **Budget the agentic tax** (~4x agents, ~15x multi-agent) and add circuit breakers + per-run cost caps.
10. **Measure quality before and after.** A good dashboard number hiding a silent quality regression is a failure, not a win.

> **Currency rule (active, not a disclaimer):** Specific prices, context-window sizes, model names, and benchmark figures in this skill and its references date from mid-2026 and rot quickly. Before quoting a price, discount rate, or model name in an actual recommendation, **verify it against the provider's official pages if web access is available in the session.** If it isn't, present figures explicitly as "directional, as of mid-2026 — verify before budgeting," and never let a stale number anchor a cost projection the user will take to a stakeholder. Benchmark results (RouteLLM, retrieval-failure reductions, LLMLingua ratios) are workload-dependent — directional always, guaranteed never. OpenTelemetry GenAI conventions are still experimental and attribute names may change.
