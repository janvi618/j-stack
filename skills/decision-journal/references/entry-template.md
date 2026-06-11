# Entry Template & Worked Example

## Full template

```markdown
## [YYYY-MM-DD] — [Short decision title]

**Decision:** [The committed choice, stated plainly.]

**Context:** [One or two sentences — what prompted this, what was at stake.]

**Reasoning:** [The real "why." The 2–3 considerations that actually drove the call, in your own words.]

**Key assumptions (what must be true):**
- [Assumption 1 — the load-bearing one]
- [Assumption 2]
- [Assumption 3]

**Prediction:** [What you expect to observe, and by when. Make it checkable.]

**Confidence:** [Low / Medium / High, or a rough %.]

**Alternatives considered & rejected:**
- [Option B] — rejected because [reason]
- [Option C] — rejected because [reason]

**State:** [Optional — note if decided under pressure, fatigue, strong emotion, or time crunch.]
**Framework used:** [Optional — e.g., first-principles, pre-mortem, foresight.]

**Review date:** [YYYY-MM-DD — roughly when the prediction should resolve.]

---
### REVIEW — [filled in later, on the review date]
**What actually happened:** [...]
**Decision quality (independent of outcome):** [Sound / flawed, and why — given what was knowable *at the time*.]
**Assumptions check:** [Which held, which were wrong.]
**Calibration:** [Was the confidence appropriate?]
**Lesson (if any):** [One transferable insight, or explicitly "none — good call, luck went the other way."]
```

## Worked example

```markdown
## 2026-03-12 — Move to usage-based pricing for the API tier

**Decision:** Switch the API product from seat-based to usage-based (per-call) pricing,
effective Q3, grandfathering existing annual contracts until renewal.

**Context:** Seat-based pricing is capping expansion revenue; power users are sharing
seats, and we're leaving money on the table while frustrating small teams who overpay.

**Reasoning:** (1) Revenue should scale with value delivered, and value here is call volume,
not headcount. (2) Lowers the entry barrier for small teams, which should widen the top of
funnel. (3) Competitor X moved this way last year and reportedly saw net expansion improve.

**Key assumptions (what must be true):**
- Existing large accounts won't see a bill increase big enough to churn (most are under
  their implied per-call rate already).
- The top-of-funnel widening outweighs short-term revenue dip from heavy seat-sharers paying less.
- Our metering infrastructure can bill accurately at scale without disputes.

**Prediction:** By end of Q4, net revenue retention improves by ≥5 points and we see ≥15%
more new-team signups month-over-month, with churn among top-20 accounts staying flat.

**Confidence:** Medium (≈60%). Real risk is the metering/billing-dispute assumption.

**Alternatives considered & rejected:**
- Hybrid (seat + usage overage) — rejected as too complex to explain; muddies the value story.
- Status quo — rejected; the expansion ceiling is the core problem.

**State:** Normal. Decided after the pricing offsite, not under time pressure.
**Framework used:** First-principles (rebuilt pricing from "what is the unit of value").

**Review date:** 2027-01-15

---
### REVIEW — [pending]
```

## The lightweight three-field version

When the user wants minimum friction (or it's a borderline-worth-it decision), this is enough:

```markdown
## 2026-03-12 — [Title]
**Decision:** [...]
**Load-bearing assumption:** [the one thing that has to be true]
**Prediction (by when):** [...]  | **Confidence:** [L/M/H]
**Review:** [date]
```

A thin entry that gets written beats a complete one that doesn't. You can always enrich it later if the decision turns out to matter more than expected.
