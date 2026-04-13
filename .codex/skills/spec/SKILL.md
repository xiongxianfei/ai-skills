---
name: spec
description: Write a concrete feature specification for spec-driven repositories that use docs/plan.md, docs/workflows.md, and specs/. Use when Codex should define requirements, interface expectations, edge cases, examples, non-goals, acceptance criteria, and gotchas before implementation begins.
---

# Feature Spec Authoring

## Task

Write a feature spec that defines what the system must do without dictating how it must be implemented.

## Instructions

1. Read `AGENTS.md` for project conventions.
2. Read `docs/plan.md` to locate the feature's scope, dependencies, and risks.
3. Read `docs/workflows.md` if it exists to understand system flow.
4. Check related specs in `specs/` for dependencies and naming consistency.
5. Clarify ambiguous inputs, outputs, or error behavior before writing the spec.
6. Start with concrete examples first. Use them to expose edge cases.
7. Derive requirements from the examples using `MUST`, `SHOULD`, and `MUST NOT`.
8. List explicit edge cases and non-goals.
9. Keep the spec compact enough that it remains reviewable.

## Gotchas

- Do not smuggle implementation details into the spec.
- Do not write untestable MUST requirements.
- Do not skip concrete examples; they often reveal missing edge cases.
- Do not leave non-goals implicit.

## Expected Output

- goal and context
- requirements using normative language
- interface and error-state expectations
- at least three edge cases
- at least two non-goals
- concrete examples
- acceptance criteria
- an initially empty or minimal gotchas section
