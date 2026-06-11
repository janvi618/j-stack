# Delivery-Layer Techniques: Cache, Route, Batch

These techniques deliver the same work more cheaply without changing what enters context. Start here for cost problems — caching especially is the single highest-leverage lever.

Each entry: *what · when · when NOT · benefits · risks · difficulty · impact.*

---

## 1. Prompt caching — PROVEN, highest leverage

**What:** Reuse a processed static prefix (system prompt, tool definitions, documents) across calls. The provider stores the processed prefix server-side; subsequent calls that share that exact prefix skip re-processing it.

**When:** A stable prefix is reused ≥2x within the TTL (5-min default; 1-hour available on Anthropic). Ideal for RAG, code assistants, multi-step agents, document Q&A — anything that re-sends the same large preamble.

**When NOT:** Low reuse, or the prefix changes every call. Anthropic's 1-hour cache *write* costs 2x base; low-reuse workloads lose money on the write premium.

**Benefits:**
- Anthropic cache reads = **0.1x input (90% off)**.
- OpenAI: up to ~50–90% input savings; cookbook reports caching "can reduce time-to-first-token latency by up to 80% and input token costs by up to 90%," and ~67% faster TTFT on 150K+ token prompts.
- Gemini implicit caching: 0.25x.
- Real-world: ProjectDiscovery reported caching saved 59% on LLM costs, rising to 66% post-optimization and 70% over their last 10 days.

**Risks — this is where people fail:**
- **Silent cache misses.** A single changed character — or one dynamic value buried in the prefix — invalidates everything after it. The cache breaks quietly; you just stop seeing savings.
- **The fix — cache-aware layout:** put **static content first, variable content last.** Move dynamic working memory / per-step variables OUT of the cached prefix and append them as the final user message. ProjectDiscovery's "relocation trick" (doing exactly this) "took our rate from 7% to 74% in a single deployment."
- Cache *writes* cost a premium (Anthropic: 1.25x for 5-min, 2x for 1-hour). You only win after enough reuse.

**Difficulty:** Low (OpenAI/Gemini automatic for prompts ≥1,024 tokens) to Medium (Anthropic explicit breakpoints; note the 20-content-block limit before a breakpoint, and that modifying content earlier than 20 blocks before a breakpoint kills the hit).

**Impact:** Cost ↓↓↓, latency ↓↓, quality neutral.

**Monitoring:** Track cache hit rate = `cache_read ÷ input`. If it's below 20% after a week, the prefix is the problem, not the model.

---

## 2. Model routing / small-large orchestration — PROVEN

**What:** Route each query to the cheapest model that can handle it. High-volume classification/extraction → small models (Haiku, GPT-5-mini/nano); genuinely hard reasoning → the large model.

**When:** Heterogeneous query difficulty at scale.

**When NOT:** Uniformly hard tasks; when routing-misclassification risk exceeds the savings; when you can't monitor quality (routing without quality tracking is dangerous — see risk below).

**Benefits:** RouteLLM (ICLR 2025; UC Berkeley/Anyscale/Canva) reported cost reductions of **over 85% on MT Bench, 45% on MMLU, 35% on GSM8K, while still achieving 95% of GPT-4's performance.** Its matrix-factorization router hit 95% of GPT-4 performance using only 26% of GPT-4 calls — a 48% cost reduction (75% with data augmentation).

**Risks:** Optimizing cost without tracking quality "produces a number that looks good in a dashboard while users quietly leave." Routing adds a classifier dependency and some latency.

**Difficulty:** Medium. Tools: RouteLLM, LiteLLM, vLLM Semantic Router, Gemini Model Optimizer, Martian.

**Impact:** Cost ↓↓↓, latency ↓ (smaller models are faster), quality variable — **monitor escalation rate and quality.**

**Practical rollout:** Start with simple rules; graduate to a trained router. Always cap the strong-model share.

---

## 3. Batch API — PROVEN

**What:** Submit async, non-urgent work for a flat discount.

**When:** Workloads tolerant of latency (≤24h), e.g., bulk classification, offline enrichment, evals.

**Benefits:** Flat **50% discount** (OpenAI and Anthropic). **Stacks with caching** — e.g., Anthropic Sonnet 4.6 drops to $1.50/$7.50 with both.

**Impact:** Cost ↓↓, latency irrelevant (async by definition).

Also relevant: OpenAI **Flex processing** for cheaper, slower synchronous calls.

---

## 4. Avoid long-context surcharges

**What:** Don't cross provider thresholds that trigger premium pricing unless the task genuinely needs it.

- GPT-5.x: crossing >272K tokens triggers **2x input / 1.5x output for the whole session.**
- Legacy Claude Sonnet: >200K surcharge.
- The current **Claude 4.6 family includes the full 1M window at flat rates with no surcharge.**

**Practical:** If a workflow hovers near a threshold, aggressively trim or retrieve rather than spilling over — the surcharge applies to the entire session, not just the overage.

**Impact:** Cost ↓↓ (avoids a cliff), no quality cost.

---

## Cache-aware prompt layout (the rule that ties this together)

Order content **static → dynamic** so the longest stable prefix caches:

```
[system prompt]        ← static, cached
[tool definitions]     ← static, cached
[retrieved documents]  ← semi-static, cached if reused
[rolling summary]      ← changes slowly
[live user/task data]  ← dynamic, appended LAST, uncached
```

For agents, place intermediate cache breakpoints roughly every ~18 content blocks (Anthropic's 20-block limit gives headroom). The single biggest practical win is keeping working memory and per-step variables out of the cached prefix.
