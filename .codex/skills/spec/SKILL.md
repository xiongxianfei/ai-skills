---
name: spec
description: >
  Write a contract-level feature spec in `specs/[feature].md` for changes
  that affect externally observable behavior such as UI, APIs, config, data
  contracts, error behavior, or safety-sensitive logic. Use after a concrete
  execution plan exists and is stable enough to define the behavior
  precisely.
---

# Feature spec authoring

## Task

Write a precise, testable feature spec that defines what the system must do
without locking in unnecessary implementation details.

## Instructions

1. Read `AGENTS.md`.
2. Read `docs/plan.md`, then open the concrete plan file this spec follows.
3. Read `docs/workflows.md` if the feature touches an existing flow.
4. Read related specs and interfaces for naming and contract consistency.
5. Use this skill only for behavior or contract changes worth specifying.
6. Start with concrete examples before abstract requirements.
7. Derive requirement IDs such as `R1`, `R2`, `R3` and use normative terms
   like `MUST`, `SHOULD`, and `MUST NOT`.
8. Include:
   - goal and context
   - related plan reference
   - inputs and outputs
   - invariants
   - error handling and boundary behavior
   - compatibility or migration expectations if relevant
   - observability expectations if relevant
   - explicit edge cases
   - explicit non-goals
   - acceptance criteria
9. Keep implementation details out unless they are externally observable
   constraints.
10. If the plan is still unstable, say so instead of freezing a shaky spec.

## Gotchas

- Do not write vague or untestable `MUST` requirements.
- Do not hide edge cases inside prose.
- Do not specify internal class structure unless it affects the contract.
- Do not derive a spec from only `docs/plan.md` if the real plan is in
  `docs/plans/`.

## Expected output

- examples first
- requirement IDs with normative language
- interface and failure expectations
- explicit edge cases and non-goals
- acceptance criteria
- reference to the concrete plan file
