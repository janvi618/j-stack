# Compress: Same Meaning, Fewer Tokens

These techniques shrink content that must stay in context. Each entry: *what · when · when NOT · benefits · risks · difficulty · impact.*

---

## 1. Compact structured tool outputs & function calling — PROVEN

**What:** Return IDs, references, and schema-constrained JSON instead of verbose blobs. Use structured outputs / constrained decoding so the model emits exactly the schema you need.

**The classic failure mode:** a tool that "returns ALL contacts and then has to read through each one token-by-token… wasting its limited context space." Verbose tool returns are one of the biggest silent token sinks in agentic systems.

**Best practices (from Anthropic, *Writing effective tools for agents*):**
- **Few high-leverage tools**, not many overlapping ones.
- **Namespacing** to disambiguate.
- **Search-focused tools, not list-all** — return matches, not the whole table.
- **Pagination / truncation / filtering** built in.
- A **`response_format` enum** (`"concise"` / `"detailed"`) so the caller controls verbosity.
- **Restrict responses to ~25,000 tokens.**

**Why structured outputs matter:** OpenAI reports `gpt-4o-2024-08-06` with Structured Outputs scores a perfect 100% on complex JSON-schema following via constrained decoding, vs <40% for `gpt-4-0613`. Reliability *and* token savings.

**Before/after:** Instead of `get_contacts()` returning full JSON for all 200 contacts, use `search_contacts(query)` returning the top 3 as `{id, name, match_score}`, fetching a full record by ID only if needed.

**Impact:** Cost ↓↓, reliability ↑↑, latency ↓.

---

## 2. Summarization / compaction / rolling summaries — PROVEN

**What:** Distill conversation/tool history into a high-fidelity summary when it grows long. Anthropic's **compaction** "distills the contents of a context window into a high-fidelity summary, letting the agent continue with minimal performance degradation when the conversation gets long." A *rolling summary* updates incrementally as the session proceeds.

**When:** Long-horizon sessions where full history would trigger rot and balloon cost.

**When NOT:** Short sessions where history fits comfortably — compaction adds a step and some loss for no benefit.

**Risks:** **Lossy** — can drop details needed later. Tune the compaction prompt to preserve exactly what your agent needs downstream, and **eval it** to catch dropped facts (this is anti-pattern #10 — compressing lossy content without an eval).

**Impact:** Cost ↓↓, quality ↑ (avoids rot), some info-loss risk.

Anthropic exposes compaction as a first-party primitive — adopt it rather than rebuilding orchestration.

---

## 3. Token-level prompt compression (LLMLingua family) — EMERGING, higher variance

**What:** Use a small model (GPT-2 / LLaMA-7B class) to drop low-information tokens from a prompt before sending it to the large model.

- **LLMLingua** (Microsoft, EMNLP 2023): up to **20x compression with little performance loss.**
- **LongLLMLingua:** improves RAG performance by up to 21.4% using only 1/4 of the tokens.
- **LLMLingua-2:** task-agnostic, 3–6x faster.

**When:** Long, repetitive, low-stakes-wording prompts where exact phrasing doesn't matter.

**When NOT:** Already-short prompts; when human-readability is required; high-stakes exact wording. The compressed prompt is not meant for human eyes.

**Risks:** Information loss at high ratios; adds a preprocessing-model dependency and latency. **Task-dependent — always evaluate the quality delta before adopting.**

**Difficulty:** Medium (extra model in the path). Available as a library and as an Azure Prompt Flow tool.

**Impact:** Cost ↓↓, quality usually neutral but task-dependent.

---

## Also a form of compression: schema/ID/reference/state-object encoding

Rather than passing full objects between steps, pass a compact state object or a reference ID and rehydrate on demand. Overlaps heavily with compact tool outputs (above) and the artifact pattern (see `references/techniques-write-and-isolate.md`).
