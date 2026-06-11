# Harness Design & Reusable Skills

Two places where token waste is created or eliminated wholesale: the agent **harness/orchestration layer**, and **reusable skills**.

---

## Part 1 — Token optimization for harness design

The orchestration layer is where most token waste is created or eliminated. Seven design principles:

### 1. Cache-aware prompt layout
Order content **static → dynamic** so the longest stable prefix caches. The biggest practical win (ProjectDiscovery): move working memory and per-step variables OUT of the cached prefix and append dynamic content as the final user message. Place intermediate cache breakpoints roughly every ~18 content blocks. **Caveat:** modifying content earlier than 20 blocks before a breakpoint kills the hit. (Full detail in `references/techniques-deliver.md`.)

### 2. Tool budget discipline
Curate a minimal tool set. Anthropic's heuristic: "if a human engineer can't definitively say which tool should be used in a given situation, an AI agent can't be expected to do better." Bloated, overlapping tool definitions sit in *every turn's* context and cause ambiguous tool choice.

### 3. Tool-result clearing & compaction primitives
Anthropic exposes first-party **compaction, tool-result clearing, and memory**. Adopt these rather than rebuilding orchestration from scratch.

### 4. Subagent isolation
Give parallel subagents separate context windows; have them return condensed summaries/artifacts, not raw transcripts. **Budget the 15x multiplier deliberately** — multi-agent only pays off on high-value, parallelizable tasks (see `references/techniques-write-and-isolate.md`).

### 5. Circuit breakers
Anthropic's published multi-agent blueprint *lacks* per-run cost caps — production harnesses must add them. Hard caps on:
- **tool-call depth**
- **recursion** (ban subagents from spawning subagents)
- **context accumulation**

Because "a subagent that recursively spawns more subagents, or a tool that returns oversized results, can multiply a single query's cost by another 10x or more."

### 6. Model routing at the harness
Pin model versions per job; route by difficulty (see `references/techniques-deliver.md`).

### 7. Context budgeting
Allocate a token budget per workflow stage and enforce it. Worked example (200K window):

| Component | Budget | Strategy |
|---|---|---|
| System prompt + instructions | 2K | Minimal, cached |
| Tool definitions | 3K | Curated set, cached |
| Skill metadata (triggers) | 1K | Progressive disclosure |
| Retrieved knowledge (top-K reranked) | 8K | Hybrid retrieval + rerank |
| Rolling conversation summary | 3K | Compaction |
| Live user/task data | 5K | Dynamic, appended last (uncached) |
| Working/scratch memory | external | Files + references |
| Output headroom | ~remaining | Length-controlled |

---

## Part 2 — Token optimization for reusable skills

Anthropic's **Agent Skills** (the open `SKILL.md` standard) are the canonical reusable-skill pattern — and **progressive disclosure is itself a token-optimization mechanism.**

### Three-tier loading
1. **Startup:** only the skill's **name + description** (YAML frontmatter) are pre-loaded into the system prompt — "just enough information for Claude to know when each skill should be used without loading all of it into context."
2. **On trigger:** the **SKILL.md body** loads.
3. **On demand:** bundled scripts/reference files load only when actually needed.

This is exactly the structure of *this* skill — a lean SKILL.md plus reference files you load as the task requires.

### Keep SKILL.md focused
- **Under ~500 lines.** Move detailed material to separate referenced files.
- "If certain contexts are mutually exclusive or rarely used together, keeping the paths separate will reduce the token usage." Split reference files along usage boundaries so a given task pulls in only what it needs.

### Code as tool vs documentation
Be explicit about whether the agent should **run a script** or **read it into context as reference** — the latter consumes tokens every time. Prefer "run this script" for deterministic work.

### Skills vs always-on prompts
A skill **elevates reusable logic out of a system message** (reconstructed on every call) **into an on-demand module** — eliminating repeated boilerplate across turns and reducing prompt sprawl. If you find the same instructions copy-pasted into every system prompt, that's a candidate for a skill.

### Design checklist for a new skill
- Start from **evaluation** (find capability gaps).
- Build **incrementally**.
- Provide **canonical input/output examples**, not exhaustive edge-case lists.
- Declare **scoped tool dependencies**.
- **Version and audit.**

### Security note
Skills introduce a **supply-chain risk** — a malicious skill could exfiltrate data. Install only from trusted sources and audit all files before use.
