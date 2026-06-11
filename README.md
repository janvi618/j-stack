# j-stack

A personal collection of my Claude skills for thinking, deciding, focusing, and leading. Each skill is a self-contained folder with a `SKILL.md` (and supporting reference files where needed) that can be loaded into Claude to extend what it knows how to do.

## Skills

| Skill | What it does |
|---|---|
| [decision-journal](skills/decision-journal/) | Capture meaningful decisions — the call, reasoning, assumptions, and confidence — for later calibration review. |
| [designed-for-women](skills/designed-for-women/) | A lens for advice to women that targets structural reality instead of recasting structural penalties as personal failings. |
| [draft-sharpener](skills/draft-sharpener/) | Tighten existing drafts: cut hedges and clichés, flag weak arguments, sharpen structure. |
| [first-principles-thinking](skills/first-principles-thinking/) | Coach through reframing hard problems from the ground up, with assumption inventories and templates. |
| [focus-coach](skills/focus-coach/) | Science-grounded coaching on attention, deep work, and flow. |
| [future-focused-leadership](skills/future-focused-leadership/) | Strategic foresight: scenario planning, weak signals, pre-mortems, and foresight artifacts. |
| [harness-design-review](skills/harness-design-review/) | Structured checklist for designing and reviewing the runtime infrastructure around LLM agents. |
| [high-performing-teams](skills/high-performing-teams/) | Team leadership coaching grounded in cross-domain research (aviation CRM, NASA, SRE, Pixar). |
| [meeting-prep-debrief](skills/meeting-prep-debrief/) | Prep for meetings (attendees, history, objectives) and debrief afterward (decisions, owners, follow-ups). |
| [power-and-influence](skills/power-and-influence/) | Navigate workplace power dynamics, persuasion, and organizational politics. |
| [relationship-keeper](skills/relationship-keeper/) | Stay genuinely connected: track owed replies, lapsed contacts, and follow-up commitments. |
| [retention-companion](skills/retention-companion/) | Turn what you read and watch into durable notes, testable recall, and scheduled review. |
| [skill-router](skills/skill-router/) | Meta-skill: routes ambiguous requests to the right skill in the library. |
| [token-optimization](skills/token-optimization/) | Diagnose and reduce token cost, latency, and quality problems in LLM systems. |

## Usage

Each folder follows the Claude skill format: a `SKILL.md` with a name and triggering description, plus optional reference material. Upload a skill folder to a Claude environment that supports user skills, and Claude will invoke it when a request matches its description.

## Structure

```
skills/
  <skill-name>/
    SKILL.md
    references/   (some skills)
```
