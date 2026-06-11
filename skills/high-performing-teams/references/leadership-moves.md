# Leadership Moves, Scripts, and the Turnaround Plan

In-the-moment material: what a leader should do differently, ready-to-adapt scripts for hard conversations, and a 30/60/90 plan for turning a team around. Adapt the scripts to the user's actual situation — don't hand them a generic template to read robotically.

---

## What leaders should do differently

The central reframe: **the leader is the architect of conditions, not the hero of execution.** In aviation, surgery, the military, and SRE, leaders don't personally do every critical task — they build the operating environment in which the team does them reliably. Spend less energy on motivation theater and more on structural clarity.

Concretely, a leader of a high-performing team:

- **Sets standards** by naming what "good" looks like in *observable* terms.
- **Creates clarity** by deciding what is fixed and what is flexible.
- **Builds trust** by responding well to bad news and being consistent about commitments.
- **Handles underperformance directly and early** — elite teams don't let resentment accumulate.
- **Encourages productive conflict** by inviting dissent *before* the decision, not after.
- **Prevents politics** by making decision rights and rationale visible.
- **Balances empathy and accountability** by separating care for the person from tolerance of drift in performance.

The single highest-leverage habit: **how you respond to bad news.** Every time someone brings you a problem early and you react badly, you train the whole team to bring problems late. The Columbia disaster is the cautionary tale — strong "excellence" culture coexisting with suppressed dissent and managers who didn't hear bad news in time. Teams become elite when *people with bad news are heard early and taken seriously.*

---

## Script: giving direct, behavioral feedback

Use when a pattern (missed commitments, slipping reliability, going quiet on risk) needs naming. The structure: ask permission → cite specific observed behavior → separate effort from the actual issue → name two concrete changes → ask what got in the way and what support is needed.

> "Can I give you a direct observation? In the last two weeks, three commitments slipped without a reset, and the team only learned about them late. The issue is not effort; it is reliability and visibility. I need you to do two things differently: flag risk earlier and confirm revised timing before the deadline passes. What got in the way, and what support do you need to change this pattern?"

Why it works: it's specific (not "you've been unreliable lately"), it explicitly de-couples the person's effort from the performance issue (preserving safety while holding the standard), and it ends by inviting problem-solving rather than just delivering a verdict.

---

## Script: resolving a real disagreement

Use when two capable people are locked on a substantive call and it risks turning personal. The structure: legitimize the disagreement → separate issue from people → force the four clarifying questions.

> "I think we have a real disagreement on the work, and that is okay. Let's separate the issue from the people. What exactly are we disagreeing about? What evidence supports each view? What risk does each path create? What decision needs to be made now, and what can be tested later?"

Why it works: "what can be tested later" is the release valve — it converts an unwinnable values argument into a smaller, reversible experiment, and lets people disagree-and-commit without either side "losing."

---

## Script: surfacing or escalating bad news (coach the team to do this)

Aviation's hard-won lesson: *expertise trapped below authority is operationally dangerous.* Teach reports to escalate explicitly rather than hint politely. The norm to install:

- Name the concern directly and early: *"I think we have a real risk on X, and I want to flag it before we commit."*
- State the stakes and the recommendation, not just the worry.
- If unheard, escalate explicitly — "I thought everyone understood" is not a communication strategy.

And coach the *leader's* half: explicitly invite challenge ("what am I missing here? who sees this differently?") so the burden isn't only on the most junior person to be brave.

---

## A practical 30/60/90 plan to turn a team around

**First 30 days — Diagnose.**
Clarify the team's purpose, top priorities, and top failure points. Map decision rights as they *actually* operate today. Observe meetings. Ask each member two questions: *where does work get stuck,* and *where does bad news go to die.* Don't restructure anything yet — you're building an accurate picture of which of the seven conditions is broken (see `diagnostic.md`).

**Next 30 days — Rebuild the operating core.**
Publish the charter, the decision-rights map, meeting norms, and escalation rules. Cut low-value meetings. Install a weekly operating review and a simple retrospective process. (Templates in `operating-system.md`.) This is where structural clarity replaces ambiguity.

**Final 30 days — Raise standards.**
Review visible commitments openly. Address *one* underperformance pattern directly (pick the most corrosive one — don't try to fix everyone at once). Reward good dissent and good follow-through publicly, so the team sees what behavior earns recognition. Re-run the diagnostic and adjust the system where scores are still weak.

> Coaching note: the sequence matters. Don't raise standards (month 3) before you've created clarity and decision rights (months 1–2) — holding people accountable to fuzzy expectations just breeds cynicism. Clarity earns you the right to demand more.

---

## Picking the intervention

When a user brings a leadership moment, match it:

- **"My report keeps missing deadlines / dropping the ball"** → feedback script + condition #7 (accountability) + check whether #2 (decision rights) or #1 (priorities) is the real cause.
- **"Two of my people are at war"** → distinguish relationship conflict (destructive — address directly and separately) from task conflict (channel it with the conflict-resolution script + conflict norms).
- **"Nobody speaks up / I find out about problems too late"** → condition #4, and audit *your own* response to bad news first.
- **"My team feels flat / unmotivated"** → resist motivation theater; check #1 (do they know what matters?) and #3 (do they see how their work connects to the outcome?) before reaching for inspiration.
- **"I just inherited a struggling team"** → the 30/60/90 plan.
