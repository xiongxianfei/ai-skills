---
name: code-review
description: >
  Perform an independent staff-level implementation review for
  spec-driven repositories using `AGENTS.md`, the concrete plan file,
  feature specs, and test specs. Use when Codex should review an
  implementation with fresh eyes against the contract, the actual diff,
  tests, and runtime-flow risks.
---

# Independent implementation review

## Task

Review an implementation rigorously against its plan, spec, test spec, and
project conventions.

## Instructions

1. Prefer a fresh session or otherwise treat the task as an independent
   review.
2. Read:
   - `AGENTS.md`
   - `docs/plan.md`, then the concrete plan file
   - `docs/workflows.md` when relevant
   - the feature spec
   - the test spec
   - the changed source files
   - the reported test or validation results
3. Run or reason through the relevant tests when possible.
4. Check every `MUST` requirement for compliance.
5. Check every named edge case in both the code and the tests.
6. Evaluate:
   - spec compliance
   - milestone acceptance
   - error handling
   - regression risk
   - test quality
   - scope discipline
   - unnecessary complexity
   - whether the living plan and docs were updated appropriately
7. Classify issues by severity and provide concrete fix suggestions.
8. Reinforce good patterns when they are present.

## Gotchas

- Do not spot-check only a few requirements.
- Do not confuse passing tests with actual compliance.
- Do not collapse all issues into one generic verdict.
- Do not skip positive notes when the code demonstrates good patterns worth
  repeating.

## Expected output

- verdict such as approve, request changes, or block
- requirement-by-requirement compliance findings
- edge case handling and test coverage findings
- issues by severity with specific fix suggestions
- positive notes and optional improvements
