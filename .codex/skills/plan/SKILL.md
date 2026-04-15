---
name: plan
description: >
  Create or revise a living execution plan for complex work in repositories
  that use `AGENTS.md`, `docs/plan.md`, `docs/plans/`, `docs/workflows.md`,
  and `specs/`. Use when the task spans multiple files or subsystems,
  changes architecture or behavior, is risky or ambiguous, or should be
  split into reviewable PR-sized milestones. New initiatives must create a
  new file under `docs/plans/YYYY-MM-DD-slug.md` and update `docs/plan.md`
  instead of overwriting an older plan.
---

# Living execution plan

## Task

Turn a requirement into a self-contained, milestone-based execution plan that
a new contributor can follow from design to working, verified behavior.

## Instructions

1. Read `AGENTS.md` first for conventions, constraints, and done criteria.
2. Read `docs/workflows.md` if the task touches an existing flow or handoff.
3. Read `docs/plan.md` to understand current active and superseded work.
4. Read the most relevant code, interfaces, tests, and existing specs.
5. Decide whether the request is:
   - a new initiative that needs a new file in `docs/plans/`, or
   - a revision to an existing concrete plan file.
6. Never start a new initiative by overwriting an older plan file.
7. Make the plan self-contained. Restate the needed repo context inside the
   plan instead of assuming prior chat context.
8. Follow `.codex/PLANS.md` and include:
   - purpose / big picture
   - context and orientation
   - constraints
   - done when
   - milestone-by-milestone work
   - progress
   - surprises & discoveries
   - decision log
   - validation and acceptance
   - validation notes
   - idempotence and recovery
   - outcomes & retrospective
9. Keep milestones small enough for one reviewable PR each.
10. For each milestone, name the files or components touched, dependencies,
    risk, validation commands, and expected observable result.
11. Update `docs/plan.md` so it points at the active concrete plan file and
    records completed or superseded plans.
12. If the task is still only an idea and not approved, prefer
    `docs/roadmap.md` over creating a full plan file.

## Gotchas

- Do not write a one-page summary that lacks commands, acceptance checks, or
  file paths.
- Do not rely on `docs/plan.md` as the plan body.
- Do not create milestones that are too large to review safely.
- Do not omit recovery steps for risky changes.
- Do not leave major ambiguity unresolved if it affects scope or sequencing.

## Expected output

- a concrete target plan file path
- a self-contained living plan
- an updated `docs/plan.md` index entry
- explicit milestones, validation commands, and non-goals
