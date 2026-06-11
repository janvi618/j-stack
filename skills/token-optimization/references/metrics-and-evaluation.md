# Metrics, Evaluation & Implementation Playbook

You cannot safely cut what you haven't measured. This file covers what to track, how to standardize it, the tooling, and the step-by-step rollout.

---

## The implementation playbook (step-by-step)

Run these roughly in order. **Gate every optimization behind an eval.**

1. **Audit current usage.** Instrument tracing; break tokens down by feature/user/model and by input/output. Track **p95, not just mean** — a workload where 5% of requests hit 50,000 tokens "can look cheap on average and expensive on the invoice."
2. **Categorize prompt components.** Static (cacheable) vs dynamic; necessary vs boilerplate vs stale.
3. **Identify high-cost workflows.** Rank by `volume × tokens × price`. **Agent pipelines first** — a task that costs $0.10 in isolation can cost $2–5 through an agent pipeline.
4. **Measure quality baselines BEFORE optimizing** — answer quality, hallucination rate, task success. You cannot safely cut what you haven't measured.
5. **Redesign prompts & skills.** Minimize system prompt to "right altitude"; move edge cases to skills; reorder static→dynamic for caching.
6. **Optimize retrieval.** Right-size chunks, add hybrid + contextual retrieval, add reranking — each gated by an eval.
7. **Add caching.** Mark stable prefixes; verify cache-hit rate (if below 20% after a week, the prefix is the problem, not the model). Add batch for async work.
8. **Add model routing.** Start with rules; graduate to a trained router (RouteLLM/LiteLLM); cap strong-model share.
9. **Add telemetry** (see below), including cache hit rate and per-step breakdowns.
10. **Run evaluations against the baseline** — cost AND quality. A/B test.
11. **Roll out safely.** Staged rollout, circuit breakers, cost caps, monitoring, rollback path.

---

## What to measure (per task, aggregated by feature/user/model/prompt-version)

- Input tokens, output tokens, total tokens, billable tokens
- **Total cost per *successful* task** (not per call — a cheap call that fails and retries isn't cheap)
- Latency: TTFT, time-per-output-token, p50/p99
- Tool calls per task; tool error rate
- Retrieval: precision@k, recall, NDCG@5, MRR
- Answer quality (LLM-as-judge + human spot checks), hallucination rate
- User satisfaction (thumbs, CSAT)
- Cache hit rate; compression loss rate; escalation rate to larger models

### Telemetry attribute map

| Metric | Source/attribute |
|---|---|
| Input tokens / task | `gen_ai.usage.input_tokens` |
| Output tokens / task | `gen_ai.usage.output_tokens` |
| Cache read / write tokens | `gen_ai.usage.cache_read.input_tokens` |
| Cost / successful task | computed from token counts × model price |
| Latency (TTFT, p50/p99) | `gen_ai.client.operation.time_to_first_chunk` |
| Tool calls / task | span count |
| Cache hit rate | `cache_read ÷ input` |
| Retrieval precision@k / NDCG@5 | offline eval set |
| Escalation rate to large model | router logs |

---

## Standardize on OpenTelemetry GenAI conventions

For portability across tools. Per the OTel spec:
- `gen_ai.usage.input_tokens` **SHOULD include all input tokens, including cached tokens.**
- Dedicated nested attributes: `gen_ai.usage.cache_read.input_tokens` and `gen_ai.usage.cache_creation.input_tokens`.
- Metrics include `gen_ai.client.token.usage` (filterable by `gen_ai.token.type`) and `gen_ai.client.operation.duration`.
- When a system reports both used and billable tokens, instrumentation **MUST report billable tokens.**

**Caveat:** these conventions remain in "Development"/experimental status (as of semconv v1.41.1) — attribute names may change.

---

## Observability tooling

- **LangSmith** (LangChain): trace tree shows total usage for the whole trace plus aggregated values per parent run and token/cost breakdowns per child run; supports separate pricing per token type (including cached); aggregates costs across threads via thread metadata.
- **Langfuse** (MIT, OTel-based): tracks usage and costs with breakdowns by usage type (input/output plus arbitrary types like `cached_tokens`, `cache_read_input_tokens`); cost and latency broken down by user, session, geography, feature, model, and prompt version via typed observations.
- **Helicone** (Apache 2.0): cost per request from token counts × pricing; segments by custom properties; recommends tracking tokens/request, cost/request, request frequency by endpoint, and cache hit rates as core metrics; includes Anthropic cached-prompt-token analysis. **Note:** third-party blogs report Helicone entered maintenance mode after a 2026 Mintlify acquisition — verify before adopting for greenfield work.
- Also: **OpenLLMetry** (Traceloop), and the OpenTelemetry GenAI conventions directly.

---

## The cardinal rule

**Measure quality before and after — never optimize cost blind.** A good dashboard number hiding a silent quality regression is a failure, not a win. Every step in the playbook is gated by an eval for exactly this reason.
