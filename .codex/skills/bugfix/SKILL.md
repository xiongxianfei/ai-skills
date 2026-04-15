---
name: bugfix
description: >
  Fix a bug with a structured workflow: reproduce, diagnose, add a
  regression test, implement the minimal fix, verify the blast radius, and
  update the right durable docs. Use for anything from a local bug to a
  cross-component defect.
argument-hint: [bug description, failing behavior, error message, or issue number]
---

# Structured bug fix workflow

You are fixing a bug using a disciplined process:
**Understand → Reproduce → Diagnose → Test → Fix → Verify → Update docs.**

## The bug

**$ARGUMENTS**

## Process

### 1. Understand what should happen

1. Find the relevant spec if the bug affects externally visible behavior.
2. Read the concrete plan file if the bug belongs to active in-flight work.
3. Read `docs/workflows.md` if the bug looks like a handoff or integration failure.
4. Read `AGENTS.md` for durable conventions and constraints.
5. If no spec exists for the behavior, note that as a contract gap.

### 2. Reproduce

Establish the minimal trigger and the exact expected vs actual behavior.

### 3. Diagnose root cause

Trace the execution path and classify the root cause:
- spec gap
- implementation error
- integration mismatch
- edge case
- regression
- plan or sequencing gap

Assess blast radius. Look for the same pattern in neighboring code.

### 4. Write the regression test first

Before changing code, add or update a test that fails because of the bug.
If it does not fail, the test does not reproduce the bug yet.

### 5. Fix

Fix the root cause with the smallest change that fully addresses it.
Do not refactor unrelated code while fixing the bug.

### 6. Verify

Run the regression test and the smallest surrounding verification scope.
Expand only as needed to cover the blast radius.

### 7. Update the right durable docs

- feature-specific contract gap -> update the spec and test spec
- repeated cross-feature mistake -> update `AGENTS.md`
- runtime handoff or stage failure -> update `docs/workflows.md`
- active in-flight sequencing or milestone issue -> update the concrete plan file

If nothing durable changed, state why.

## Rules

- Always add a failing regression test first when feasible.
- Fix the root cause, not just the symptom.
- Keep the fix scoped.
- Report what was actually verified.
- Prefer updating the narrowest durable document that prevents recurrence.

## Expected output

- reproduction summary
- root-cause classification
- regression test added or updated
- minimal fix summary
- blast-radius note
- durable doc updates, if any
