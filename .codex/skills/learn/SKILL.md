---
name: learn
description: >
  Capture durable lessons after implementation in repositories that use
  `AGENTS.md`, `docs/workflows.md`, execution plans, and feature specs. Use
  when Codex should update conventions, gotchas, or workflow docs based on
  repeated mistakes, spec gaps, or verified implementation discoveries.
---

# Implementation learning capture

## Task

Preserve useful lessons from implementation so future work avoids repeating
the same mistakes.

## Instructions

1. Read the current reference docs:
   - `AGENTS.md`
   - `docs/workflows.md`
   - the concrete plan file
   - the relevant spec and test spec
   - recent review findings when available
2. Identify:
   - repeated implementation mistakes
   - spec gaps discovered during execution
   - workflow changes that differ from current docs
   - newly established conventions
3. Update the right document:
   - cross-feature patterns go into `AGENTS.md`
   - feature-specific lessons go into the spec’s `Gotchas` section
   - runtime-flow or handoff changes go into `docs/workflows.md`
   - completed plan outcomes go into the concrete plan file
4. Add concise entries without deleting existing guidance.
5. Prefer durable guidance, not one-off trivia.
6. If nothing meaningful was learned, say so and make no edits.

## Gotchas

- Do not fabricate lessons when nothing meaningful was learned.
- Do not rewrite or delete history when an additive note is enough.
- Do not put project-wide conventions into a single feature spec.
- Do not leave verified workflow changes undocumented.

## Expected output

- which documents were updated
- what was added to each
- the key takeaways future implementations should remember
