# Write (Externalize) & Isolate

Two of Anthropic's four context buckets: move state *out* of the window (write), and split work across *separate* windows (isolate). Plus semantic/response caching, which fits naturally here. Each entry: *what · when · when NOT · benefits · risks · difficulty · impact.*

---

## 1. Agent memory / externalization — PROVEN → EMERGING

**What:** Store state outside the context window (files, scratchpads, databases) and page it in on demand.

**MemGPT** (Packer et al., 2023) formalized OS-style virtual context tiers:
- **Main context** = RAM (what's in the window now)
- **Recall storage** = disk (recent, retrievable)
- **Archival storage** = cold storage

The LLM calls functions like `archival_memory_search` to move data between tiers — treating the context window like a memory hierarchy.

**The artifact pattern (Anthropic multi-agent research system):** subagents write findings to a filesystem and **return lightweight references**, not raw payloads. The LeadResearcher saves its plan to memory to persist context, "since if the context window exceeds 200,000 tokens it will be truncated."

**When:** Long-horizon or unbounded tasks; multi-agent systems where passing full transcripts would explode token use.

**Risks / cost:** Adds orchestration complexity. Worth it specifically when the task horizon exceeds what a single window can hold.

**Impact:** Enables unbounded-horizon tasks; adds engineering complexity.

Anthropic exposes memory as a first-party primitive (alongside compaction and tool-result clearing) — prefer it over a bespoke build. Tooling: **Letta** (the MemGPT lineage).

---

## 2. Subagent isolation — PROVEN

**What:** Give parallel subagents **separate context windows**; have them return condensed summaries / artifacts, not raw transcripts.

**When:** Decomposable, high-value, parallelizable tasks. On Anthropic's internal research eval, a multi-agent system beat single-agent Opus 4 by 90.2% — at ~15x the token cost.

**When NOT:** Anthropic is explicit — "domains that require all agents to share the same context or involve many dependencies between agents are not a good fit for multi-agent systems today," and the economics only work "where the value of the task is high enough to pay for the increased performance." Don't pay the 15x tax on simple or non-parallelizable work.

**Risks:** Runaway recursion. "A subagent that recursively spawns more subagents, or a tool that returns oversized results, can multiply a single query's cost by another 10x or more." **Ban subagents from spawning subagents; enforce per-run cost caps** (see `references/harness-and-skills.md`).

**Impact:** Quality ↑↑ on the right tasks, cost ↑↑↑ — spend deliberately.

---

## 3. Multi-step decomposition — PROVEN

**What:** Break a complex task into sequential focused steps, each with a clean, minimal context, rather than one giant prompt carrying everything.

**When:** Tasks with separable sub-problems. Pairs naturally with subagent isolation and memory.

**When NOT:** Simple/low-value tasks where the decomposition overhead and inter-step token passing aren't justified.

**Impact:** Quality ↑ (focus), cost variable — watch inter-step token passing; use references not full payloads between steps.

---

## 4. Semantic / response caching — EMERGING, correctness risk

**What:** **GPTCache** (Bang, NLP-OSS 2023) stores responses keyed by *query embedding*; semantically similar queries hit the cache — 2–10x faster on a hit. Distinct from prompt caching (which caches a processed prefix); this caches whole *responses* by semantic similarity.

**When:** Repetitive FAQ-style traffic where many queries are near-duplicates.

**When NOT:** Queries needing real-time/fresh data; anything where a near-miss wrong answer is costly.

**Risks:** **Adversarial / near-miss false hits** — minor lexical variation can trigger a *wrong* cached answer. Staleness. This is the correctness-risk technique; tune the similarity threshold carefully and exclude anything time-sensitive.

**Impact:** Cost ↓↓↓ on repetitive FAQs, latency ↓↓, **correctness risk.** Tooling: GPTCache, Redis-based caches.
