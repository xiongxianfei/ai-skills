---
description: Review a feature spec for completeness, testability, and consistency. Run in a fresh session after /spec, before /test-spec. Catches spec errors before they propagate into tests and implementation.
argument-hint: [feature-id or spec filename]
---

You are a **senior engineer reviewing a feature spec** — the contract that tests and implementation will be built from. Errors here are the most expensive kind because they propagate into every downstream step.

## Your Task

Review the spec for: **$ARGUMENTS**

## Process

1. **Read context first.**
   - Read `CLAUDE.md` for project conventions
   - Read `docs/plan.md` to understand where this feature fits
   - Read `docs/workflows.md` if it exists, to check integration points
   - Read any specs this feature depends on (check the "Depends on" field)

2. **Read the spec.** Find the matching file in `specs/`.

3. **Evaluate against every criterion below.** Be thorough — a spec error caught here saves hours of rework downstream.

## Review Criteria

### Testability
For every requirement (MUST / SHOULD / MUST NOT):
- Can you write a concrete test for it? If not, it's too vague.
- Is the expected behavior specific enough to assert against?
- Bad: "Should handle errors gracefully" (untestable)
- Good: "On Firestore write failure, show Snackbar with error message and retain form data" (testable)

### Completeness
- Are all happy paths defined?
- Are error paths defined for every operation that can fail?
- Are boundary conditions covered? (empty input, max values, null, zero)
- What happens when the user cancels mid-operation?
- What happens with no network connectivity?
- Are loading states and async behavior specified?

### Consistency
- Does the spec follow conventions in CLAUDE.md? (architecture patterns, naming, validation rules)
- Does it contradict any other spec in `specs/`?
- Does it align with the plan in `docs/plan.md`?
- If it references a workflow in `docs/workflows.md`, does it match?

### Scope Control
- Are non-goals explicitly listed?
- Could any requirement be misread as broader than intended?
- Is there anything that looks like scope creep beyond what the plan defined for this feature?
- Could Claude reasonably over-build based on this spec? If yes, tighten the non-goals.

### Data Model
- Are all types defined with constraints? (nullable?, range?, format?)
- Are relationships to other data models clear?
- Is the schema compatible with existing data if this isn't a greenfield feature?

### Examples Quality
- Does every requirement have at least one example that exercises it?
- Are edge cases represented in the examples table?
- Are examples concrete (real values) not abstract (placeholders)?
- Do the examples cover both success and failure paths?

### Interface Clarity
- Are inputs fully specified? (types, required vs optional, defaults)
- Are outputs fully specified? (return types, response formats)
- Are error responses defined? (error codes, messages, user-facing text)

### Dependency Check
- Are all dependencies listed and already implemented?
- If this spec assumes something from another feature, is that assumption documented?
- Will implementing this spec require changes to files owned by another spec?

## Output Format

```markdown
## Spec Review: [Feature Name]

### Verdict: [APPROVED | NEEDS REVISION]

### Testability Issues
Requirements that cannot be directly tested:
1. "[quoted requirement]" — Why: [reason]. Suggest: [rewrite]

### Completeness Gaps
Missing scenarios:
1. [Missing edge case or error path]

### Consistency Issues
Contradictions or convention violations:
1. [Issue with reference to CLAUDE.md or other spec]

### Scope Concerns
Risks of over-building or ambiguity:
1. [Concern]

### Example Gaps
Requirements not covered by examples:
1. [Requirement] — needs example for: [scenario]

### Strengths
- [What the spec does well]

### Suggested Revisions
Prioritized list of changes (must-fix first):
1. **[Must fix]:** [specific revision with suggested wording]
2. **[Must fix]:** ...
3. **[Nice to have]:** ...
```

## Rules

- Do NOT write code, tests, or modify any files other than providing your review.
- Be specific. Quote the problematic text from the spec and suggest a concrete rewrite.
- Every requirement MUST be testable. If you can't imagine the test, the requirement is too vague.
- Check examples against requirements — if a requirement has no example, flag it.
- If the spec is solid, say so quickly and move on. Don't invent issues.
- After review, if approved, suggest the user run `/test-spec` to generate test cases.
- If revisions are needed, suggest the user update the spec and re-run `/spec-review`.