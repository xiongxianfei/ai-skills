---
name: test-spec
description: Generate a test specification from a feature spec in repositories that use specs/[feature].md and specs/[feature].test.md. Use when Codex should map requirements, edge cases, and examples into explicit unit and integration test cases with a coverage map before test code is written.
---

# Test Spec Authoring

## Task

Turn a feature spec into a concrete, traceable test plan before writing test code.

## Instructions

1. Read the feature spec first.
2. Read `AGENTS.md` for testing conventions.
3. Check existing test specs for formatting consistency.
4. Extract every `MUST`, `SHOULD`, and `MUST NOT` requirement.
5. Extract every edge case and every example.
6. Convert each requirement, edge case, and example into at least one test.
7. Add integration tests where behavior crosses component boundaries.
8. Assign stable IDs such as `T1`, `T2`, and keep a clear coverage map.
9. Flag vague or untestable requirements instead of pretending they are covered.

## Gotchas

- Do not leave a MUST requirement without test coverage.
- Do not use placeholder inputs when concrete values would make the test clearer.
- Do not skip integration boundaries just because unit tests exist.
- Do not accept a coverage map with gaps.

## Expected Output

- grouped unit tests
- integration tests where needed
- explicit exclusions under what not to test
- a coverage map that shows no uncovered critical requirements
