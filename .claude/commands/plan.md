---
description: Decompose a requirement into features with dependencies, risks, and build order. Outputs docs/plan.md
argument-hint: [requirement description]
model: opus
---

You are in PLANNING MODE. Do NOT write any code. Do NOT create any files except docs/plan.md.

## Your Task

Decompose this requirement into discrete, implementable features:

$ARGUMENTS

## Process

1. Ask me clarifying questions using the AskUserQuestion tool if the requirement is ambiguous. Interview me until you understand:
   - What problem this solves and for whom
   - Key constraints (tech stack, performance, compatibility)
   - What's explicitly out of scope

2. Decompose into features. For each feature, identify:
   - **Scope:** What this covers (1-2 sentences)
   - **Dependencies:** Which features must be done first
   - **Risk:** What could go wrong or is hard to get right
   - **Size:** S / M / L

3. Determine build order based on dependencies.

4. Identify non-goals to prevent scope creep.

## Output Format

Write the plan to `docs/plan.md` using this structure:

```markdown
# Plan: [Project/Epic Name]

## Overview
One paragraph. What we're building and why.

## Features

### F1: [Name]
- **Scope:** ...
- **Dependencies:** None / F1, F2...
- **Risk:** ...
- **Size:** S / M / L

### F2: [Name]
...

## Build Order
F1 → F2 → F3 (F4 can parallel with F3)

## Architecture Decisions
Key decisions that affect all features.

## Non-Goals
What this project explicitly does NOT include.
```

## Rules
- Keep the plan under 1 page
- Each feature must be small enough for a single PR
- If a feature is too big, split it further
- Include at least 2 non-goals
- Flag any feature with Risk = "High" and explain mitigation
