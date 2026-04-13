---
description: Implement a feature following TDD. Reads spec + test spec, writes tests first, then implements to pass them.
argument-hint: [feature name or spec path]
allowed-tools: Read, Edit, Write, Bash
model: sonnet
---

You are IMPLEMENTING a feature using Test-Driven Development.

## Your Task

Implement feature: $ARGUMENTS

## Context Loading (read ALL of these before writing any code)

1. Read `CLAUDE.md` for project conventions, architecture, and coding rules
2. Read `docs/workflows.md` for how this feature connects to the system
3. Read `specs/$ARGUMENTS.md` for the feature requirements
4. Read `specs/$ARGUMENTS.test.md` for the test cases
5. Check source files listed in the spec's "Touches" section

## Process

### Phase 1: Tests First
1. Write test code for ALL test cases in the test spec
2. Run the tests — they should ALL FAIL (red phase)
3. If any test passes before implementation, it's either testing the wrong thing or the feature already exists. Flag this.
4. Commit: `test(feature-name): add tests for [feature]`

### Phase 2: Implement
1. Write the minimum code to pass each test group
2. After each group passes, run ALL tests to check for regressions
3. Follow conventions from CLAUDE.md strictly
4. Commit after each passing test group: `feat(feature-name): implement [component]`

### Phase 3: Verify
1. Run ALL tests one final time
2. Check every MUST requirement in the spec — is it satisfied?
3. Check every edge case — is it handled?
4. Check the acceptance criteria checklist

## Rules
- Tests FIRST, always. Do not write implementation before tests.
- Follow CLAUDE.md conventions exactly — architecture layers, naming, patterns.
- One commit per passing test group, not one giant commit at the end.
- If a requirement is unclear, check the spec. If the spec is unclear, ASK — do not guess.
- Do NOT add features not in the spec. Check non-goals before building anything extra.
- Keep the implementation as simple as possible. No premature optimization.
- If you discover a spec gap during implementation, note it but don't fill it silently — flag it to me.

## Completion Checklist
Before saying "done", verify:
- [ ] All tests from test spec are written and passing
- [ ] All MUST requirements from spec are implemented
- [ ] All edge cases are handled
- [ ] No code outside the feature scope was modified without reason
- [ ] Commits are clean and granular
- [ ] No non-goal features were added
