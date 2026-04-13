---
name: learn
description: Capture lessons learned after implementation in repositories that use AGENTS.md, docs/workflows.md, and feature specs. Use when Codex should update conventions, gotchas, or workflow docs based on mistakes, spec gaps, or repeated implementation problems without deleting existing guidance.
---

# Implementation Learning Capture

## Task

Preserve useful lessons from implementation so future work avoids repeating the same mistakes.

## Instructions

1. Read the current reference docs such as:
   - `AGENTS.md`
   - `docs/workflows.md`
   - the relevant feature spec
   - recent history if it helps identify what changed
2. Identify:
   - repeated implementation mistakes
   - spec gaps discovered during execution
   - workflow changes that differ from current docs
   - newly established conventions
3. Update the right document:
   - cross-feature patterns go into `AGENTS.md`
   - feature-specific lessons go into the spec's gotchas section
   - system-flow changes go into `docs/workflows.md`
4. Add concise entries without deleting existing guidance.
5. Date-stamp feature-specific gotchas when useful.

## Gotchas

- Do not fabricate lessons when nothing meaningful was learned.
- Do not rewrite or delete history when an additive note is enough.
- Do not put project-wide conventions into a single feature spec.
- Do not leave discovered workflow changes undocumented.

## Expected Output

- which documents were updated
- what was added to each
- the key takeaways future implementations should remember
