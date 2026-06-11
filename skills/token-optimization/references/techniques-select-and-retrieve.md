# Select & Retrieve: Controlling What Enters Context

The cheapest token is the one you never send. These techniques reduce or curate what enters the context window. Each entry: *what · when · when NOT · benefits · risks · difficulty · impact.*

---

## 1. System-prompt minimization ("right altitude") — PROVEN

**What:** Write the system prompt at the *right altitude* — minimal but sufficient. Not a laundry list of rules and not so terse it drops necessary signal. "Minimal does not necessarily mean short."

**The anti-pattern:** Stuffing every edge case into the system prompt (it sits in every turn's context, repeated on every call). Move edge cases to a referenced skill file loaded on demand; keep canonical examples, not exhaustive ones.

**When NOT:** Don't strip so far that you lose instructions the model actually needs — measure task success before and after.

**Impact:** Cost ↓ (especially compounded across turns), quality neutral-to-↑ (less distraction).

---

## 2. Few-shot example curation — PROVEN

**What:** Include a few *canonical* examples that capture the pattern, not a long list trying to cover every case.

**When:** The task benefits from demonstration (format-following, tone, structured extraction).

**When NOT:** When the example list is growing to cover edge cases — that's a signal to move to a skill or a different approach, not to keep appending.

**Impact:** Cost ↓, quality ↑ (well-chosen examples beat many mediocre ones).

---

## 3. Just-in-time retrieval — PROVEN

**What:** Instead of pre-loading everything, hold lightweight identifiers (file paths, IDs, links) and load the full content only on demand when the agent actually needs it.

**When:** Agents working over large file systems / knowledge bases where any single task touches only a slice.

**Benefits:** Keeps the working context small; avoids paying for content that's never used.

**Impact:** Cost ↓↓, quality ↑ (less noise), some added orchestration.

---

## 4. RAG optimization: chunking, hybrid retrieval, reranking — PROVEN

This is the big one for large corpora. Retrieve the relevant slice instead of stuffing the whole corpus.

### When to just stuff instead
Anthropic: **if your knowledge base is smaller than ~200,000 tokens (~500 pages), just include the entire thing in the prompt.** RAG's machinery isn't worth it below that. Above it — or for dynamic corpora, cost/latency-sensitive, or precision-critical work — retrieve.

### Chunking
- **Recursive splitting with 200–800 token chunks is the workhorse.** Chroma benchmarks: recursive ~85–90% recall at 400 tokens; semantic chunking ~91–92%.
- **Overlap:** 10–20% is a common starting point, BUT a 2026 systematic analysis found overlap gave *no measurable benefit* on some setups, and reducing it improved efficiency by cutting redundancy. Don't assume overlap helps — test it.
- **Respect document structure:** split on Markdown headers, keep code blocks intact. Fixed 100-char chunks that split sentences mid-thought are a classic failure.

### Hybrid + contextual retrieval
- Combine **vector search + BM25** using **Reciprocal Rank Fusion (RRF)**.
- Anthropic's **Contextual Retrieval** (contextual embeddings + contextual BM25) reduced the top-20-chunk retrieval failure rate by **49% (5.7% → 2.9%)**.
- Adding reranking on top: **67% reduction (5.7% → 1.9%)**.

### Reranking
- A cross-encoder (e.g., Cohere Rerank 4, 32K context) reorders top-N down to top-K, passing fewer, higher-relevance docs to the LLM.
- Improves answer accuracy ~20–35% and *lowers* token usage (fewer docs to the model).
- **When NOT:** Don't add reranking without measuring — it adds latency, and on some setups the NDCG gain is marginal.

**Combined impact:** Cost ↓↓, quality ↑↑ (precision), latency variable.

### Putting it together (good RAG pipeline)
1. Structure-aware recursive chunks, ~400 tokens.
2. Contextual embeddings + contextual BM25, fused with RRF.
3. Rerank top-20 → top-5 with a cross-encoder.
4. Pass only the top-K to the LLM.

Expected: ~49–67% fewer retrieval failures vs naïve vector-only.

---

## Context pruning & tool-result clearing

**What:** Actively remove stale content from the working context — old tool results that are no longer needed, superseded intermediate state. Anthropic exposes first-party **tool-result clearing** as a primitive; adopt it rather than letting results pile up.

**Impact:** Cost ↓↓ (avoids accumulation), quality ↑ (less rot).

See also `references/techniques-compress.md` for compaction (summarizing history) and `references/techniques-write-and-isolate.md` for externalizing state to memory.
