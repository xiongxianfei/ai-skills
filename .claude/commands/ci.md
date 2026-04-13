---
description: Generate a GitHub Actions CI workflow for a feature's tests. Creates .github/workflows/test-[feature].yml
argument-hint: [feature name]
model: sonnet
---

You are creating a CI WORKFLOW for automated testing.

## Your Task

Generate a GitHub Actions workflow for: $ARGUMENTS

## Context Loading

1. Read `CLAUDE.md` for CI conventions (test runner, JDK version, build tool, etc.)
2. Read the test spec at `specs/$ARGUMENTS.test.md` to understand what tests exist
3. Read the feature spec at `specs/$ARGUMENTS.md` to identify which source paths to trigger on
4. Check `.github/workflows/` for existing workflow patterns to stay consistent

## Output

Write to `.github/workflows/test-[feature-name].yml`:

```yaml
name: "Test: [Feature Name]"

on:
  pull_request:
    paths:
      - '[source paths for this feature]'
      - 'specs/[feature-name]*'
  push:
    branches: [main]
    paths:
      - '[source paths for this feature]'

jobs:
  unit-tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      # [Setup steps from CLAUDE.md conventions]
      - name: Run unit tests
        run: [test command scoped to this feature]

  integration-tests:
    runs-on: ubuntu-latest
    needs: unit-tests
    steps:
      - uses: actions/checkout@v4
      # [Setup steps]
      - name: Run integration tests
        run: [integration test command]
```

## Rules
- Scope triggers with `paths` — only run when this feature's files change
- Unit tests gate integration tests (use `needs:`)
- Follow existing workflow patterns in the repo for consistency
- Include caching for dependencies if the project uses it
- Keep the workflow under 50 lines
- If CLAUDE.md has no CI conventions, ask the user about their setup before generating
