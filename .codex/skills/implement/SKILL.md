---
name: implement
description: Implement a feature using a strict test-driven workflow in repositories that use AGENTS.md, docs/workflows.md, specs/[feature].md, and specs/[feature].test.md. Use when Codex should read the spec and test spec, write tests first, implement the minimum code to pass, and verify acceptance criteria without adding non-goal features.
---

# TDD Feature Implementation

## Task

Implement a feature by following the spec and test spec strictly, with tests written before implementation.

## Instructions

1. Read all required context before editing:
   - `AGENTS.md`
   - `docs/workflows.md`
   - the feature spec
   - the test spec
   - the existing files listed in the spec touch points
2. Start with tests:
   - write tests for all specified cases
   - run them and confirm they fail for the right reason
3. Implement the minimum code needed to satisfy each failing group.
4. Re-run the relevant suite after each meaningful step to catch regressions early.
5. Verify every MUST requirement, edge case, and acceptance criterion before closing the task.
6. Flag spec gaps instead of silently inventing behavior.

## Gotchas

- Do not write implementation before the tests exist.
- Do not treat a prematurely passing test as success; it may indicate the wrong assertion or an already-existing feature.
- Do not add features listed as non-goals.
- Do not silently compensate for spec ambiguity with guesses.

## Expected Output

- tests written first
- minimal implementation to satisfy the spec
- explicit verification against requirements and edge cases
- a note on any spec gaps or unresolved ambiguity
