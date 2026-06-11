# Before/After Examples, Tradeoffs & Review Checklist

Concrete rewrites to imitate, the architecture-pattern tradeoff table, and the audit checklist.

---

## Before / after rewrites

### Bloated → optimized prompt
**Before** (≈350 tokens, repeated every call): "You are a helpful, friendly, knowledgeable assistant. Please always be polite. When the user asks a question, think step by step. Always be accurate. Do not make things up. If you don't know say so. [+ 20 edge-case rules + 5 verbose examples]…"

**After** (high-signal, cache-friendly): A tight `<instructions>` block at the "right altitude" + **2 canonical examples**, with all stable content placed first (cacheable) and the user's dynamic query last. Edge cases moved to a referenced skill file loaded on demand.

### Verbose → compact tool result
**Before:** Tool returns full JSON for all 200 contacts (thousands of tokens) that the agent reads token-by-token.

**After:** `search_contacts(query)` returns the top 3 matches as `{id, name, match_score}`; the full record is fetched by ID only if needed. Add `response_format: concise|detailed` and truncate at ~25K tokens with pagination.

### Poor → improved RAG chunking
**Before:** Fixed 100-char chunks, no overlap, splitting sentences mid-thought; pure vector search.

**After:** Recursive/structure-aware ~400-token chunks respecting headers; contextual embeddings + contextual BM25 with RRF fusion; Cohere rerank top-20→top-5. Expected: ~49–67% fewer retrieval failures.

### Bloated → progressive-disclosure skill
**Before:** One 1,500-line `SKILL.md` always loaded.

**After:** A <500-line `SKILL.md` with name/description frontmatter for the trigger; detailed workflows and examples in separate referenced files loaded only when the skill fires.

### Multi-agent redesign
**Before:** Single agent reads full files into context, accumulating noise → context rot; cost balloons.

**After:** Orchestrator decomposes the task; subagents with isolated windows do focused subtasks and return short summaries + artifact references; orchestrator keeps a concise filtered history; recursion banned; per-run cost cap enforced. (Anthropic's research system beat single-agent Opus 4 by 90.2% at ~15x token cost — worth it only for high-value, parallelizable work.)

---

## Architecture pattern tradeoff table

| Pattern A | Pattern B | When A wins | When B wins |
|---|---|---|---|
| Large static system prompt | Modular skill loading (progressive disclosure) | Tiny, stable behavior | Many capabilities, large org library |
| Long-context prompting | RAG | KB < ~200K tokens, one-shot | Large/dynamic corpora; cost/latency-sensitive; precision-critical |
| Full-document injection | Targeted retrieval | Doc needs holistic reasoning, fits comfortably | Doc >> needed slice; repeated queries |
| Agentic multi-step | Single-pass | Decomposable, high-value, parallel | Simple/low-value tasks (avoid 4–15x token tax) |
| Verbose tool outputs | Compact structured outputs | Almost never | Nearly always — IDs/refs/schemas |
| Full history | Rolling summary / compaction | Short sessions | Long-horizon sessions (avoid rot + cost) |
| Prompt compression | No compression | Long, repetitive, low-stakes wording | Short prompts; exact-wording/high-stakes |
| Aggressive caching | Real-time freshness | Stable reused context | Rapidly changing data; correctness-critical |
| One large model | Model routing | Uniformly hard tasks | Mixed difficulty at scale |

**Key tension:** every optimization that externalizes or compresses adds engineering complexity and a potential failure mode. But on hard, parallelizable tasks, spending more tokens *does* buy quality — Anthropic found token usage alone explained ~80% of the variance in research performance. The discipline is spending them where they pay off. The 1M-token window is a convenience, not a license.

---

## Review checklist (prompts, skills, workflows)

- [ ] Is static content first and dynamic content last (cache-friendly)?
- [ ] Is the system prompt at the "right altitude" — minimal but sufficient?
- [ ] Are examples canonical and few, not exhaustive edge-case lists?
- [ ] Are tools minimal, namespaced, search-focused, and token-efficient?
- [ ] Do tool outputs return IDs/refs/structured JSON, with pagination/truncation (~25K cap)?
- [ ] Is retrieval used instead of full-document injection where the corpus is large (>~200K tokens)?
- [ ] Are chunks right-sized (200–800 tokens) and structure-aware; is reranking justified by eval?
- [ ] Is long history compacted/summarized; is memory externalized?
- [ ] Are skills using progressive disclosure (<500-line SKILL.md, referenced files)?
- [ ] Is caching enabled and hit-rate monitored (>20%)?
- [ ] Is routing in place with a capped strong-model share?
- [ ] Are circuit breakers / cost caps / recursion bans enforced?
- [ ] Are token/cost/latency/quality metrics tracked per task with attribution?
- [ ] Was a quality baseline measured BEFORE optimizing?

---

## Common anti-patterns to flag

1. Over-stuffing context ("bigger is better") → context rot, cost, latency.
2. Dynamic content early in the prompt → silent cache misses.
3. Verbose tool outputs read token-by-token.
4. Stuffing every edge case into the system prompt instead of curated examples.
5. Optimizing cost without monitoring quality.
6. Bloated/overlapping tool sets causing ambiguous tool choice.
7. Storing full conversation history instead of compacting.
8. Multi-agent everywhere — paying the 15x tax on low-value or non-parallelizable tasks.
9. No circuit breakers → runaway recursive token spend.
10. Compressing/summarizing lossy content without an eval to catch dropped facts.
11. Adding reranking/compression without measuring net benefit.
12. Treating the 1M window as a reason to abandon retrieval.
