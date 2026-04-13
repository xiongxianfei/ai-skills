---
description: Structured bug fix workflow. Diagnose root cause, write a regression test, fix, and update docs to prevent recurrence. Use for any bug — from a quick fix to a complex investigation.
argument-hint: [bug description, error message, or issue number]
---

You are fixing a bug using a structured process: **Reproduce → Diagnose → Test → Fix → Update docs.**

## The Bug

**$ARGUMENTS**

## Process

### Step 1: Understand What Should Happen

Before looking at the bug, understand the intended behavior:

1. **Find the relevant spec.** Search `specs/` for the feature this bug affects.
2. **Read the spec.** What does it say should happen in this scenario?
3. **Read the workflow.** Check `docs/workflows.md` — does this bug occur at a handoff between components?
4. **Read CLAUDE.md** for conventions that might be relevant (validation rules, error handling patterns).

If no spec exists for this feature, note that — it's a gap that contributed to the bug.

### Step 2: Reproduce

Confirm the bug is real and understand its trigger:

1. **Find or create a minimal reproduction.** What's the simplest input or action that triggers the bug?
2. **Identify the actual vs expected behavior.**
   ```
   Expected: [what the spec says should happen]
   Actual:   [what actually happens]
   Trigger:  [minimal steps to reproduce]
   ```
3. **Check if there's an existing test that should have caught this.** If yes, why didn't it? If no, that's a test gap.

### Step 3: Diagnose Root Cause

Don't jump to a fix. Understand *why* the bug exists:

1. **Trace the execution path.** Follow the data flow from trigger to failure point. Use logs, debugger, or code reading.
2. **Identify the root cause.** Classify it:
   - **Spec gap:** The spec didn't cover this scenario
   - **Implementation error:** Code doesn't match what the spec says
   - **Integration mismatch:** Components don't agree on types, formats, or error handling
   - **Edge case:** An input condition nobody anticipated
   - **Regression:** A previous change broke this
3. **Assess blast radius.** Could this same root cause affect other features? Check for the same pattern in related code.

### Step 4: Write Regression Test FIRST

Before writing any fix, write a test that fails because of the bug:

```
Test: [descriptive name of the bug scenario]
Input: [the trigger from Step 2]
Expected: [what the spec says should happen]
Currently: FAILS (produces the buggy behavior)
```

Add this test to the existing test file for this feature, or create one if none exists. Run it — it MUST fail. If it passes, your test doesn't actually reproduce the bug.

### Step 5: Fix

Now fix the bug. Follow these principles:

- **Minimal change.** Fix the root cause, not symptoms. Don't refactor while fixing.
- **Follow conventions.** Read CLAUDE.md — the fix should follow the same patterns as the rest of the codebase.
- **Check blast radius.** If you identified similar patterns in Step 3, fix those too — or at minimum, file them as separate issues.

Run the regression test — it should now pass. Run the full test suite — nothing else should break.

### Step 6: Update Documentation

This is what separates a good fix from a great one. Update docs to prevent recurrence:

1. **If the spec was missing an edge case:**
   Add the scenario to the spec's Edge Cases section and Examples table.
   ```
   Add to specs/[feature].md → Edge Cases:
   - [The scenario that caused the bug and how it should be handled]
   ```

2. **If this is a pattern that could repeat across features:**
   Add to CLAUDE.md → Known Pitfalls:
   ```
   - [Description of the pattern and the rule to prevent it]
   ```

3. **If a workflow handoff was the problem:**
   Update `docs/workflows.md` with the error path that was missing.

4. **If the spec's Gotchas section exists:**
   Add an entry describing what went wrong:
   ```
   Add to specs/[feature].md → Gotchas:
   - [What Claude (or the developer) got wrong and how to avoid it]
   ```

### Step 7: Commit and Report

Commit with a descriptive message following conventional commit format:

```bash
git add -A
git commit -m "fix([scope]): [concise description of the fix]

Root cause: [one-line explanation]
Regression test: [test name]
Spec updated: [yes/no - which spec]
CLAUDE.md updated: [yes/no - which section]"
```

Report the summary:

```markdown
## Bug Fix Summary

**Bug:** [one-line description]
**Root cause:** [classification + explanation]
**Fix:** [what was changed]
**Regression test:** [test name and file]
**Blast radius:** [other areas potentially affected]

### Docs Updated
- [ ] Spec edge case added: specs/[file].md
- [ ] CLAUDE.md pitfall added (if pattern-level)
- [ ] Workflow error path added: docs/workflows.md
- [ ] Spec gotcha added: specs/[file].md

### Prevention
[What would have prevented this bug? Missing spec coverage? 
Missing validation rule in CLAUDE.md? Missing test?]
```

## Decision Guide: Simple vs Complex Bug

Not every bug needs the full process. Use this to decide:

```
Is the bug obvious and localized? (typo, off-by-one, wrong variable)
  → Yes: Skip to Step 4 (write test), Step 5 (fix), Step 6 (update docs)
  → No: Follow the full process from Step 1

Does the bug span multiple components?
  → Yes: Read workflows.md, trace the handoff, full diagnosis
  → No: Focus on the single component's spec

Is this the same class of bug you've seen before?
  → Yes: The real fix is in CLAUDE.md (add a convention/pitfall)
  → No: The fix is in the spec (add the edge case)
```

## Rules

- ALWAYS write a failing test before writing a fix. No exceptions.
- ALWAYS update at least one document (spec, CLAUDE.md, or workflows.md). A fix without a doc update means the same bug class will recur.
- Fix the root cause, not the symptom. If the symptom is "null pointer at line 42," the fix is not "add a null check at line 42" — it's "why was it null in the first place?"
- Don't refactor while fixing. Scope creep in bugfixes introduces new bugs.
- If the full test suite fails after your fix, your fix is wrong — revert and rethink.
- Assess blast radius. If the same pattern exists elsewhere, at minimum note it in the commit message.
