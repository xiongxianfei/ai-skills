---
description: Write a feature spec from the plan. Generates specs/[feature].md with requirements, edge cases, and acceptance criteria.
argument-hint: [feature id, e.g. F1 or feature name]
model: opus
---

You are writing a FEATURE SPEC. Do NOT write any code.

## Your Task

Write a spec for feature: $ARGUMENTS

## Context Loading

1. Read `CLAUDE.md` for project conventions
2. Read `docs/plan.md` to find this feature's scope, dependencies, and risks
3. Read `docs/workflows.md` if it exists, to understand how this feature connects to the system
4. Check `specs/` for any existing specs this feature depends on

## Process

1. Ask me clarifying questions using the AskUserQuestion tool if the feature scope is ambiguous. Focus on:
   - Exact input/output formats and types
   - Error handling expectations
   - UI/UX behavior (if applicable)

2. Write concrete examples FIRST — input/output pairs that define the expected behavior. These reveal edge cases.

3. Derive requirements from the examples. Use MUST / SHOULD / MUST NOT.

4. List edge cases and non-goals explicitly.

## Output

Write the spec to `specs/[feature-name].md`:

```markdown
# Spec: [Feature Name]

## Goal
One sentence: what this does and why.

## Context
- **Plan ref:** docs/plan.md → [Fx]
- **Depends on:** [completed features this needs]
- **Workflow ref:** docs/workflows.md → [relevant flow, if any]
- **Touches:** [existing files/modules affected]

## Requirements
- [MUST/SHOULD/MUST NOT] ...
- ...

## Data Model
[Types, schemas, API contracts — if applicable]

## Interface
- **Input:** What the user/caller provides
- **Output:** What this returns or renders
- **Error states:** What happens on failure

## Edge Cases
- [Specific scenario] → [expected behavior]
- ...

## Non-Goals
- [What this explicitly does NOT do]
- ...

## Examples
| Input | Expected Output | Covers |
|-------|----------------|--------|
| ... | ... | Happy path |
| ... | ... | Edge case: ... |

## Acceptance Criteria
- [ ] All MUST requirements implemented
- [ ] All edge cases handled
- [ ] Tests pass
- [ ] Code review approved

## Gotchas
[Start empty. Add Claude's recurring mistakes here over time.]
```

## Rules
- Keep the spec under 100 lines. If longer, the feature is too big — suggest splitting.
- Every MUST requirement must be testable.
- Include at least 3 edge cases.
- Include at least 2 non-goals.
- Write examples as concrete data, not abstract descriptions.
- Do NOT dictate implementation details — define WHAT, not HOW.
