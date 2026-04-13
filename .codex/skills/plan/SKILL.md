---
name: plan
description: Decompose a product requirement into small implementation features, dependencies, risks, build order, and non-goals for repositories that use a spec-driven workflow with AGENTS.md, docs/plan.md, docs/workflows.md, and specs/. Use when Codex should create or refine a one-page implementation plan before code is written.
---

# Spec-Driven Feature Planning

## Task

Turn a requirement into a small, buildable plan with explicit dependencies, risks, and non-goals.

## Instructions

1. Read `AGENTS.md` first for project conventions and architectural rules.
2. Read `docs/workflows.md` if it exists to understand how the feature fits into the larger system.
3. Clarify ambiguity before planning. Focus on:
   - who the requirement serves
   - hard constraints such as tech stack, compatibility, privacy, or performance
   - what is explicitly out of scope
4. Decompose the requirement into features that are each small enough for a single PR.
5. For each feature, capture:
   - scope
   - dependencies
   - risk
   - size
6. Determine build order from the dependencies.
7. List explicit non-goals to prevent scope creep.

## Gotchas

- Do not jump into implementation details too early.
- Do not create features that are too large for one reviewable PR.
- Do not hide cross-feature dependencies inside vague wording.
- Do not omit non-goals just because they seem obvious.

## Expected Output

- a concise overview
- a feature list with scope, dependencies, risk, and size
- explicit build order
- architecture decisions only when they affect all features
- at least two non-goals
