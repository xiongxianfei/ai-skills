---
name: plan-review
description: Critically review a project plan as a staff engineer in repositories that use docs/plan.md and AGENTS.md conventions. Use when Codex should challenge decomposition, dependency accuracy, risk coverage, edge cases, non-goals, and architecture alignment without modifying the plan file.
---

# Staff Plan Review

## Task

Review an implementation plan rigorously and identify gaps before execution begins.

## Instructions

1. Read the plan under review, usually `docs/plan.md`.
2. Read `AGENTS.md` for architectural and project conventions.
3. Evaluate the plan against these dimensions:
   - decomposition quality
   - dependency accuracy
   - risk assessment
   - edge cases and error handling
   - non-goals
   - architecture alignment
4. For each dimension, give a verdict and a specific explanation.
5. Identify missing features, hidden coupling, and places where features should be split.
6. Suggest actionable improvements rather than abstract criticism.

## Gotchas

- Do not rubber-stamp a plan just because the structure looks neat.
- Do not modify the plan file unless the user explicitly asks for edits.
- Do not use vague criticism; point to the exact gap and the suggested fix.
- Do not ignore failure modes at the boundaries between features.

## Expected Output

- summary verdict such as approve, revise, or rethink
- findings per review dimension
- missing features if any
- specific suggested changes
- clarification questions only where needed
