---
name: reframe-problem
version: 0.1.0
description: |
  Turns a problem statement into 3 sharp "How might we" questions that focus on
  outcomes, not methods. Returns structured JSON (reframed_text, reframe_title,
  icon) suitable for piping into other tools. Use when: "reframe this problem",
  "how might we", "turn this into a HMW", "innovation question", "problem
  reframing", "make this an opportunity statement".
triggers:
  - reframe problem
  - how might we
  - turn into HMW
  - innovation question
  - opportunity reframing
allowed-tools:
  - Bash
  - Read
  - Write
  - AskUserQuestion
---

# /reframe-problem — Problem Statement Reframer

You are running the `/reframe-problem` workflow. It takes a problem space the user provides and reframes it as 3 punchy "How might we" / "How can we" questions, focused on real outcomes rather than specific methods.

The classic example: instead of "How can we make ordering cheeseburgers faster at our restaurant?" (a method), the better reframe is "How might we decrease customer frustration at our restaurant?" (the actual outcome). Reframing toward outcomes opens up the solution space.

---

## Step 0: Get the problem statement

The user may have already provided the problem inline when invoking the skill (e.g., `/reframe-problem our checkout flow has a 40% abandonment rate`). Check the user's invocation message:

- **If a problem statement is present inline:** use it as-is. Skip to Step 1.
- **If no problem statement is present:** ask for one via AskUserQuestion-style prompt. Just ask plainly: "What's the problem space you'd like to reframe? Give me a sentence or two — what's broken, frustrating, or under-performing." Wait for the user's reply, then continue.

Do not skip this step. The reframe is only as good as the input.

---

## Step 1: Generate the reframes

Take the problem statement and produce **3 distinct "How might we" or "How can we" questions** that:

1. **Focus on outcomes, not methods.** Strip out specific solutions ("faster ordering", "new website", "more staff") and surface the underlying goal ("less customer frustration", "more confidence at decision points", "stronger sense of progress").
2. **Stay short and punchy.** One sentence each. No nested clauses. No jargon.
3. **Open the solution space.** Each of the 3 should reframe at a *different altitude* or *different angle* — not three rewordings of the same thing. For example:
   - One reframe focused on the end user's emotional outcome
   - One reframe focused on the underlying business or system goal
   - One reframe focused on a removed constraint or inverted assumption

Each reframe needs:
- `reframed_text` — the full "How might we / How can we" question
- `reframe_title` — a 2-4 word label naming the angle (e.g., "Reduce friction", "Invert the problem", "User confidence")
- `icon` — a single relevant emoji that captures the angle

---

## Step 2: Return structured JSON

Output the reframes as a JSON array matching this schema. Print it as a fenced ```json block so it's easy to copy.

```json
[
  {
    "reframed_text": "How might we ...",
    "reframe_title": "...",
    "icon": "..."
  },
  {
    "reframed_text": "How might we ...",
    "reframe_title": "...",
    "icon": "..."
  },
  {
    "reframed_text": "How might we ...",
    "reframe_title": "...",
    "icon": "..."
  }
]
```

After printing the JSON, give the user a one-line summary: name the angle each reframe takes (e.g., "Three angles: emotional outcome, system goal, inverted assumption") so they can scan quickly.

---

## Step 3: Offer to save

Use AskUserQuestion:

> Save this reframe to disk so you can reference it later or pipe it into another tool?

Options:
- A) Save to `~/innovation/reframes/<date>-<slug>.json` (recommended — builds a library over time)
- B) Just print, don't save

If A:
```bash
mkdir -p ~/innovation/reframes
SLUG=$(echo "<original-problem-statement>" | tr '[:upper:]' '[:lower:]' | tr -cs 'a-z0-9' '-' | sed 's/^-//;s/-$//' | cut -c1-50)
DATE=$(date +%Y-%m-%d)
FILE=~/innovation/reframes/"${DATE}-${SLUG}.json"
cat > "$FILE" <<'EOF'
{
  "original_problem": "<original-problem-statement>",
  "created_at": "<iso-timestamp>",
  "reframes": [ ...the JSON array from Step 2... ]
}
EOF
echo "Saved: $FILE"
```

Replace `<original-problem-statement>` with the actual statement from Step 0, and `<iso-timestamp>` with `$(date -u +%Y-%m-%dT%H:%M:%SZ)`.

If B: skip the save step. Confirm: "Got it — printed only."

---

## Important Rules

- **Always 3 reframes. Not 2, not 5.** Three is enough variety to show different angles without overwhelming.
- **Never include the original problem inside a reframe.** The whole point is to reframe — copying the original wording defeats it.
- **Never propose solutions.** A reframe is a *question*, not an answer. If you find yourself writing "by doing X" or "through Y", stop and recast it as a pure outcome.
- **Each reframe must take a genuinely different angle.** If two of your three feel like rewordings of each other, throw one out and try a different altitude (zoom out to the system, zoom in to the emotional moment, invert an assumption, swap the subject).
- **Keep titles to 2-4 words.** Longer titles mean the angle isn't sharp enough yet.
- **Pick icons that signal the angle, not the topic.** A reframe about "reduce friction" gets 🌊 or ⚡ (the feeling), not 🍔 (the topic). The icon helps the user scan angles at a glance.

---

## Example

**Input:** "How can we make ordering cheeseburgers faster at our restaurant?"

**Output:**

```json
[
  {
    "reframed_text": "How might we decrease customer frustration at our restaurant?",
    "reframe_title": "Emotional outcome",
    "icon": "😤"
  },
  {
    "reframed_text": "How can we make every minute a customer waits feel shorter?",
    "reframe_title": "Reframe time",
    "icon": "⏳"
  },
  {
    "reframed_text": "How might we make customers feel ordering was the best part of their visit?",
    "reframe_title": "Invert the problem",
    "icon": "🔄"
  }
]
```

Three angles: emotional outcome, perception of time, inverted framing.
