---
name: plan-review
description: >
  Review a concrete execution plan in `docs/plans/` before implementation.
  Use when Codex should challenge whether the plan is self-contained,
  correctly sequenced, safely scoped, and verifiable without modifying the
  plan file.
---

# Execution plan review

## Task

Review an execution plan rigorously and identify gaps before implementation
begins.

## Instructions

1. Read the concrete plan file under review, not just `docs/plan.md`.
2. Read `AGENTS.md`, `.codex/PLANS.md`, and `docs/workflows.md` when relevant.
3. Evaluate the plan against these dimensions:
   - self-contained context for a newcomer
   - milestone size and sequencing
   - dependency accuracy
   - validation quality
   - risk coverage
   - rollback or recovery guidance
   - explicit non-goals
   - architecture alignment
   - observability of “done”
4. For each dimension, give a verdict and a specific explanation.
5. Identify hidden coupling, missing milestones, unsafe ordering, and vague
   acceptance criteria.
6. Suggest concrete edits rather than abstract criticism.
7. Do not modify the plan unless the user explicitly asks for edits.

## Gotchas

- Do not rubber-stamp a plan because it looks organized.
- Do not review a generic index file as though it were the actual plan.
- Do not ignore missing validation commands or missing recovery guidance.
- Do not accept milestones that are too large for one review loop.

## Expected output

- verdict such as approve, revise, or rethink
- findings by review dimension
- missing milestones or dependencies
- exact suggested edits
- explicit readiness statement for spec or implementation work
