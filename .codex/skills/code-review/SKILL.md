---
name: code-review
description: Perform an independent staff-level code review for spec-driven repositories using AGENTS.md and feature specs. Use when Codex should review an implementation with fresh eyes against the spec, edge cases, tests, and code quality, ideally in a fresh session separate from the implementation thread.
---

# Independent Code Review

## Task

Review an implementation rigorously against its spec, test spec, and project conventions.

## Instructions

1. Prefer a fresh session or otherwise treat the task as an independent review.
2. Read:
   - `AGENTS.md`
   - the feature spec
   - the test spec
   - the changed source files
3. Run the relevant tests when possible.
4. Check every MUST requirement for compliance.
5. Check every edge case both in the code and in the tests.
6. Evaluate test quality, error handling, scope discipline, and unnecessary complexity.
7. Classify issues by severity and provide concrete fix suggestions.
8. Reinforce good patterns when they are present.

## Gotchas

- Do not spot-check only a few requirements.
- Do not confuse passing tests with actual compliance.
- Do not collapse all issues into one generic verdict.
- Do not skip positive notes when the code demonstrates good patterns worth repeating.

## Expected Output

- verdict such as approve, request changes, or block
- requirement-by-requirement compliance findings
- edge case handling and test coverage findings
- issues by severity with specific fix suggestions
- positive notes and optional improvements
