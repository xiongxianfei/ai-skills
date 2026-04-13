---
description: Generate test cases from a feature spec. Creates specs/[feature].test.md with unit and integration test tables.
argument-hint: [feature name or spec path]
model: sonnet
---

You are writing a TEST SPEC. Do NOT write test code yet — define the test cases first.

## Your Task

Generate test cases for: $ARGUMENTS

## Context Loading

1. Read the feature spec at `specs/$ARGUMENTS.md` (or the path provided)
2. Read `CLAUDE.md` for testing conventions
3. Check existing test specs in `specs/` for format consistency

## Process

1. Extract every MUST/SHOULD/MUST NOT requirement → each becomes at least one test
2. Extract every edge case → each becomes at least one test
3. Extract every example → each becomes a test
4. Identify integration points → create integration tests for handoffs between components
5. Assign unique IDs (T1, T2, ...) to each test

## Output

Write to `specs/[feature-name].test.md`:

```markdown
# Tests: [Feature Name]

## Ref
- Spec: specs/[feature-name].md

## Unit Tests

### [Group: e.g. Validation]
| ID | Input | Expected | Covers |
|----|-------|----------|--------|
| T1 | [concrete input] | [concrete expected output/behavior] | [which requirement] |
| T2 | ... | ... | ... |

### [Group: e.g. Data Processing]
| ID | Scenario | Expected | Covers |
|----|----------|----------|--------|
| T5 | ... | ... | ... |

## Integration Tests

| ID | Flow | Expected | Covers |
|----|------|----------|--------|
| T10 | [multi-step flow] | [end-to-end expected result] | [which workflow step] |

## What NOT to Test
- [Things explicitly excluded — UI pixel layout, third-party internals, etc.]

## Coverage Map
| Requirement | Tests |
|-------------|-------|
| [MUST requirement 1] | T1, T2 |
| [MUST requirement 2] | T3 |
| [Edge case 1] | T4, T5 |
| ... | ... |
```

## Rules
- Every MUST requirement MUST have at least one test. No exceptions.
- Every edge case in the spec MUST have a test.
- Use concrete values, not placeholders ("duration=1800" not "valid duration").
- The coverage map must show no uncovered requirements.
- If you find a requirement that's untestable, flag it — it means the spec is too vague.
- Keep test descriptions short — one line per test.
