---
name: plan
description: >
  Create or update a living execution plan in `docs/plan.md` for complex
  features, refactors, migrations, or risky fixes in repositories that use
  `AGENTS.md`, `docs/workflows.md`, and `specs/`. Use when the task spans
  multiple files or subsystems, should be split into reviewable PRs, or needs
  explicit validation and sequencing.
---

# Living Execution Plan

## Task

Turn a requirement into a self-contained, milestone-based execution plan that a
new contributor can follow from design to working, verified behavior.

## Instructions

1. Read `AGENTS.md` first for conventions, commands, architecture, and done criteria.
2. Read `docs/workflows.md` if it exists.
3. Read the most relevant code, interfaces, tests, and existing specs.
4. Restate the needed context inside the plan so the plan is self-contained.
5. Start the plan with:
   - goal
   - context
   - constraints
   - done when
   - explicit non-goals
6. Break the work into milestones small enough for one reviewable PR each.
7. For each milestone, include:
   - scope
   - files or components touched
   - dependencies
   - risk
   - size
   - validation commands
   - expected observable result
8. Explain build order from real dependencies.
9. Add living sections and keep them current when revising the plan:
   - Progress
   - Decision Log
   - Surprises & Discoveries
   - Validation Notes
10. Prefer proof-of-concept milestones for risky unknowns before full implementation.

## Gotchas

- Do not make the plan depend on unstated prior discussion.
- Do not create milestones that are too large to review safely.
- Do not omit validation commands or acceptance checks.
- Do not leave major ambiguity unresolved if it affects sequencing or scope.

## Expected Output

- self-contained overview
- goal, context, constraints, done when, non-goals
- milestone breakdown with dependencies, risks, and validation
- explicit build order
- living progress and decision sections
