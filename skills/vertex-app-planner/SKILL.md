---
name: vertex-app-planner
description: >
  Turns an app idea into a structured planning document with 5 sections (MasterPlan, Implementation, Design, UserJourney, Tasks) specifically tailored for building in Google's Vertex AI Studio. Use this skill whenever the user describes an app they want to build, asks for a project plan, wants to scaffold a new project, or mentions Vertex AI Studio Build. Also trigger when the user says things like "plan my app," "I want to build...", "help me architect...", "create a project doc," "scope out this app idea," or anything involving turning an idea into an actionable build plan — even if they don't mention Vertex AI explicitly. If the user shares an app concept and seems to want structure around it, use this skill.
---

# Vertex AI App Planner

You turn app ideas into structured, actionable planning documents designed for building with Google Vertex AI Studio.

## What You Produce

A single combined markdown document with 5 clearly separated sections. Each section serves a distinct purpose — together they form a complete "source of truth" that can guide the entire build from idea to deployment.

## Workflow

### Step 1: Understand the Idea

The user will describe their app idea (usually a paragraph or more). Before generating anything, make sure you understand:

- **Who is this for?** (target users, audience)
- **What problem does it solve?**
- **What are the core features?** (not a wish list — the MVP)
- **What Vertex AI capabilities are relevant?** (Gemini models, Agent Builder, grounding, RAG, media generation, etc.)

If the description is clear enough to proceed, go ahead. If it's ambiguous on any of these points, ask 1–2 focused clarifying questions — don't interrogate the user with a long list.

### Step 2: Generate the Document

Create a single `.md` file with all 5 sections. Follow the templates below closely — they've been designed to give both high-level direction and granular execution guidance.

Write the document to `/home/claude/app-plan.md`, then copy to `/mnt/user-data/outputs/`.

---

## Document Templates

### Section 1: MasterPlan — The Compass

This is the 10,000-foot view. It answers: who is this for, why are we building it, and what does success look like?

```
# MasterPlan

## Vision
[One paragraph describing what this app does and why it matters]

## Target Users
[Who specifically will use this? Be concrete — not "everyone" but "small business owners managing inventory" or "students studying for exams"]

## Core Problem
[What pain point or need does this address?]

## Success Criteria
[How do we know this app is working? 2-3 measurable outcomes]

## Vertex AI Strategy
[Which Vertex AI capabilities power this app and why they were chosen]
- **Model**: [e.g., Gemini 2.0 Flash for low-latency chat, Gemini 1.5 Pro for long-context analysis]
- **Key Features**: [e.g., grounding with Google Search, RAG with custom data, Agent Builder for multi-step workflows]
- **Deployment**: [e.g., Deploy as App → Cloud Run, or custom backend]

## Scope Boundaries
[What this app does NOT do — explicit exclusions to prevent scope creep]
```

### Section 2: Implementation — The Tech Spec

This is the build order. It answers: what gets built first, what depends on what, and what are the technical decisions?

```
# Implementation

## Architecture Overview
[Brief description of the system architecture — what talks to what]

## Tech Stack
- **Frontend**: [e.g., Vertex AI Studio generated app, or custom React/Next.js]
- **Backend/AI**: [Vertex AI Studio, specific Gemini model(s), Agent Builder if applicable]
- **Data**: [data stores, grounding sources, vector DBs if RAG is involved]
- **Deployment**: [Cloud Run, Firebase, etc.]

## Build Sequence
[Ordered phases — each phase should be completable before moving to the next]

### Phase 1: [Name]
- What to build
- What it depends on
- How to validate it works

### Phase 2: [Name]
...

## Vertex AI Studio Build Steps
[Specific steps for building in Vertex AI Studio]
1. Prompt design and system instructions
2. Model selection and parameter tuning
3. Grounding/data source configuration (if applicable)
4. /Evaluate — test prompt quality with autorater
5. /Build — generate the application code
6. Deploy as App → Cloud Run (or Get Code for custom deployment)

## Key Technical Decisions
[Document important choices and their rationale so future-you understands why]
```

### Section 3: Design — The Vibe

This is the look and feel. It answers: what should this app feel like to use?

```
# Design

## Design Philosophy
[1-2 sentences on the overall aesthetic and emotional tone — e.g., "clean and clinical for healthcare professionals" or "playful and approachable for students"]

## Visual Guidelines
- **Color Palette**: [primary, secondary, accent colors with hex codes]
- **Typography**: [font families, sizes for headings/body]
- **Spacing & Layout**: [general principles — e.g., generous whitespace, card-based layout]
- **Component Style**: [rounded corners, shadows, borders — the small details that define the vibe]

## UI Framework Notes
[If using Vertex AI Studio's auto-generated UI (Gradio-based), note customization limits. If building custom, specify CSS framework — e.g., Tailwind, Material UI]

## Responsive Behavior
[How the app should adapt across screen sizes]

## Accessibility
[Key accessibility requirements — contrast ratios, keyboard navigation, screen reader support]
```

### Section 4: UserJourney — The Flow

This is the step-by-step user experience. It answers: what does the user actually do, screen by screen?

```
# UserJourney

## Entry Point
[How does the user first encounter/open the app?]

## Core Flow
[Walk through the primary user journey step by step]

### Step 1: [Action]
- **What the user sees**: [describe the screen/state]
- **What the user does**: [the action they take]
- **What happens**: [system response, AI processing, etc.]

### Step 2: [Action]
...

## Secondary Flows
[Optional paths — settings, error states, edge cases]

## Error & Edge Cases
[What happens when things go wrong — empty states, API failures, unexpected input]
```

### Section 5: Tasks — The Checklist

This is the granular execution plan. Each task should be a single, atomic action that can be checked off.

```
# Tasks

## Phase 1: [matches Implementation Phase 1]
- [ ] [Specific atomic task]
- [ ] [Specific atomic task]
- [ ] [Specific atomic task]

## Phase 2: [matches Implementation Phase 2]
- [ ] [Specific atomic task]
...

## Vertex AI Studio Tasks
- [ ] Create new prompt in Vertex AI Studio
- [ ] Write system instructions
- [ ] Select and configure model (model name, temperature, top-p, etc.)
- [ ] Add grounding sources (if applicable)
- [ ] Test with sample inputs
- [ ] Run /Evaluate with autorater
- [ ] Run /Build to generate app code
- [ ] Test generated app locally
- [ ] Deploy as App to Cloud Run
- [ ] Share deployment URL with stakeholders
- [ ] Iterate on prompt based on feedback

## Post-Launch
- [ ] [Monitoring, feedback collection, iteration tasks]
```

---

## Writing Guidelines

When filling in these templates, keep the following in mind:

**Be specific, not generic.** Don't write "use an appropriate model" — write "Gemini 2.0 Flash for the chat interface because latency matters more than context length here." The whole point of this document is to make decisions concrete so they can be executed without second-guessing.

**Match the user's level of detail.** If they gave you a rich description with specific features, reflect that richness back. If they were more high-level, fill in reasonable defaults but flag your assumptions clearly (e.g., "Assuming we want a chat-based interface — let me know if you had something different in mind").

**Vertex AI Studio awareness.** The user is building in Vertex AI Studio, so the Implementation and Tasks sections should include specific Vertex AI Studio steps — prompt design, /Evaluate, /Build, Deploy as App, Get Code, Agent Builder setup, etc. Don't just write a generic tech spec. Reference real Vertex AI features and workflows.

**Keep Tasks truly atomic.** Each checkbox should be something you can sit down and do in one focused session. "Build the frontend" is not atomic. "Create the chat input component with send button" is.

**Design section should be actionable.** Include actual hex codes, actual font names, actual spacing values — not "use a modern color palette." If you're unsure, pick sensible defaults and note they're suggestions.

## Vertex AI Studio Build — Quick Reference

For context when writing Implementation and Tasks sections:

- **Vertex AI Studio** is Google's developer console for production-ready AI apps
- **Prompt Design**: Write and test prompts with Gemini models (text, images, video, code)
- **Model Garden**: 200+ models — Gemini (Google), Claude (Anthropic), open models (Gemma, Llama)
- **/Evaluate command**: Test prompt quality with autoraters and custom rubrics
- **/Build command**: Turn finalized prompts into application code
- **Deploy as App**: One-click deployment to Cloud Run (auto-scaling, Gradio-based UI)
- **Get Code**: Export generated code (Python, Android, Swift, Web, Flutter, cURL)
- **Agent Builder / ADK**: For multi-step, tool-using AI agents (grounding, RAG, custom APIs)
- **Agent Engine**: Deploy and manage agents at scale
- **Collaboration**: Share prompts and apps with team members
