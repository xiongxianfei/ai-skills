---
name: spec-review
description: >
  Review a feature spec before test planning or implementation. Use when
  Codex should challenge requirement clarity, completeness, ambiguity,
  compatibility, observability, edge cases, non-goals, and testability
  without reviewing code.
---

# Spec review

## Task

Review `specs/[feature].md` as an independent reviewer before test-spec
generation or implementation.

## Instructions

1. Read the feature spec, the concrete plan file it references, related
   specs, and `AGENTS.md`.
2. Read `docs/workflows.md` when the feature touches an existing runtime
   flow.
3. Evaluate:
   - requirement clarity
   - completeness
   - ambiguity
   - compatibility and migration impact
   - edge cases
   - error behavior
   - observability requirements
   - acceptance quality
   - non-goals
   - testability
4. Classify findings as:
   - blocking
   - major
   - minor
5. Suggest exact wording or missing requirements precisely.
6. Reject requirements that cannot be tested or observed.
7. Do not review changed code; review the contract only.

## Gotchas

- Do not assume examples cover all edge cases.
- Do not let vague acceptance criteria pass.
- Do not collapse contract review into a code review.
- Do not approve a spec that fails to reference the concrete plan it follows.

## Expected output

- verdict
- findings by severity
- exact spec fixes
- explicit statement on readiness for `test-spec`
