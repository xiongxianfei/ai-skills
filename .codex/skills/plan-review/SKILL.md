---
name: plan-review
description: >
  Critically review `docs/plan.md` before implementation or major replanning.
  Use when Codex should challenge milestone sizing, dependency order, risk
  handling, validation coverage, non-goals, and rollout readiness without
  modifying the plan file.
---

# Plan Review

## Task

Review an execution plan rigorously and identify gaps before implementation begins.

## Instructions

1. Read the plan under review, usually `docs/plan.md`.
2. Read `AGENTS.md`, `docs/workflows.md` if it exists, and any referenced specs.
3. Evaluate the plan against these dimensions:
   - goal and context clarity
   - milestone decomposition
   - dependency accuracy and build order
   - validation strategy
   - risk coverage
   - edge cases and rollback concerns
   - non-goals and scope control
4. Classify findings as:
   - blocking
   - major
   - minor
5. Identify missing milestones, hidden coupling, oversized PRs, and weak validation steps.
6. Suggest specific plan changes rather than abstract criticism.

## Gotchas

- Do not rubber-stamp a plan because the structure looks neat.
- Do not modify the plan file unless the user explicitly asks for edits.
- Do not ignore execution risks at boundaries between milestones or systems.
- Do not accept milestones without a concrete validation path.

## Expected Output

- verdict
- findings by severity
- exact plan changes or milestone splits
- explicit statement on readiness for implementation
