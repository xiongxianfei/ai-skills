---
name: implement
description: >
  Implement a feature milestone by milestone using the active execution plan
  as the source of truth in repositories that use `AGENTS.md`,
  `docs/workflows.md`, `docs/plans/`, `specs/[feature].md`, and
  `specs/[feature].test.md`. Use when Codex should write tests first,
  implement the minimum code to pass, run validation after each milestone,
  and keep the living plan updated as work proceeds.
---

# Milestone-driven implementation

## Task

Implement a feature by following the concrete plan, spec, and test spec
strictly, with tests written before implementation.

## Instructions

1. Read all required context before editing:
   - `AGENTS.md`
   - `docs/plan.md`, then the concrete active plan file
   - `docs/workflows.md` when relevant
   - the feature spec
   - the test spec
   - the existing files listed in the plan or spec touch points
2. Treat the concrete plan file as the source of truth for milestone order.
3. Work one milestone at a time. Do not expand scope to later milestones.
4. Start each milestone with tests:
   - write or update tests for the milestone
   - run them and confirm they fail for the right reason when appropriate
5. Implement the minimum code needed to satisfy the failing group.
6. Re-run the relevant suite after each meaningful step.
7. Run the milestone validation commands from the plan before moving on.
8. If validation fails, stop and fix the failure before continuing.
9. Verify every `MUST` requirement, edge case, and acceptance criterion
   before closing the feature.
10. Update the active plan as you go:
    - `Progress`
    - `Decision Log`
    - `Surprises & Discoveries`
    - `Validation Notes`
11. Keep diffs scoped, and do not add features listed as non-goals.
12. If the task changes externally observable behavior and no spec exists,
    stop and create or request a spec first.

## Gotchas

- Do not write implementation before the tests exist.
- Do not treat a prematurely passing test as success; it may indicate the
  wrong assertion or already-existing behavior.
- Do not skip plan updates and leave the living plan stale.
- Do not silently compensate for spec ambiguity with guesses.

## Expected output

- tests written first
- minimal implementation to satisfy the current milestone
- milestone validation results
- an updated living plan
- a note on any spec gaps or unresolved ambiguity
