---
name: test-spec
description: >
  Generate `specs/[feature].test.md` from an approved feature spec. Use when
  Codex should map requirements, examples, and edge cases into traceable unit,
  integration, and end-to-end tests before writing test code.
---

# Test Spec Authoring

## Task

Turn an approved feature spec into a concrete, traceable test plan.

## Instructions

1. Read the approved feature spec first.
2. Read `AGENTS.md` for testing conventions and commands.
3. Extract every requirement ID, edge case, and example.
4. Create test IDs such as `T1`, `T2`, `T3`.
5. Map each requirement ID to one or more tests.
6. Include the right level of coverage:
   - unit tests for local logic
   - integration tests for boundaries and wiring
   - end-to-end or smoke tests for user-visible flows when needed
7. Use concrete fixtures, inputs, and expected outputs whenever possible.
8. Add explicit exclusions under "What not to test".
9. Flag vague or untestable requirements instead of pretending they are covered.

## Gotchas

- Do not leave a MUST requirement uncovered.
- Do not generate tests from an unreviewed or unstable spec.
- Do not skip integration boundaries.

## Expected Output

- grouped test cases
- requirement-to-test coverage map
- concrete fixtures or scenarios
- explicit exclusions
- uncovered gaps, if any
