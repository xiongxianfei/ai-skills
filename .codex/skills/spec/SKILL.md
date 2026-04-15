---
name: spec
description: >
  Write a contract-level feature spec in `specs/[feature].md` for changes that
  affect externally observable behavior such as APIs, CLI, UI, config, data
  contracts, error behavior, or safety-sensitive logic. Use after the plan is
  stable enough to define the behavior precisely.
---

# Feature Spec Authoring

## Task

Write a precise, testable feature spec that defines what the system must do
without locking in implementation details.

## Instructions

1. Read `AGENTS.md`, `docs/plan.md`, and `docs/workflows.md` if it exists.
2. Read related specs and interfaces for naming and contract consistency.
3. Use this skill only for behavior or contract changes worth specifying.
4. Start with concrete examples before abstract requirements.
5. Derive requirement IDs such as `R1`, `R2`, `R3` using `MUST`, `SHOULD`, and `MUST NOT`.
6. Include:
   - goal and context
   - inputs and outputs
   - invariants
   - error handling and boundary behavior
   - compatibility or migration expectations if relevant
   - observability or logging expectations if relevant
   - edge cases
   - non-goals
   - acceptance criteria
7. Keep implementation details out unless they are externally observable constraints.

## Gotchas

- Do not write vague or untestable MUST requirements.
- Do not hide edge cases inside prose.
- Do not specify internal structure unless it affects the contract.

## Expected Output

- examples first
- requirement IDs with normative language
- interface and failure expectations
- explicit edge cases and non-goals
- acceptance criteria
