---
name: flashcard-generator
description: >
  Flashcard generator that creates source-grounded, spaced-repetition-ready cards with learning objectives, atomic prompts, explanations, tags, and canonical JSON. Use for Anki cards, cloze deletions, memory prompts, durable recall practice, and retention cards from notes, documents, code, papers, courses, or project material.
---

## Input

$ARGUMENTS

## Core Standard

Create high-quality flashcards for durable recall from the user's supplied source material. Do not merely summarize the source. Decide what is worth remembering, what must be understood first, what the smallest testable idea is, and what context prevents orphan facts.

Use the user's supplied source as the factual base. Mark inferred or external context explicitly when the user asks for related facts beyond the source. Avoid unsupported details.

Use local references when useful:

- `references/learning-design.md` for shared learning-design principles.
- `references/card-quality.md` for flashcard-specific quality checks.
- `schemas/flashcard.schema.json` as the reference contract for canonical JSON. The schema is documentation only; do not claim executable validation.

In canonical JSON, use `"source"` when the item is grounded directly in supplied material. Use `"inferred"` only when the user requested related or external context and the inference is clearly marked.

## Workflow

1. Identify learner goal, audience, source material, desired card count, difficulty, and requested export format when provided.
2. Extract learning objectives before writing cards.
3. Build a compact knowledge map:
   - facts;
   - concepts;
   - procedures;
   - distinctions;
   - examples and non-examples;
   - prerequisites;
   - common misconceptions.
4. Select only knowledge worth retaining.
5. Generate candidate cards using appropriate types:
   - basic Q/A;
   - cloze;
   - bidirectional;
   - contrast;
   - example-non-example;
   - procedure;
   - failure-mode.
6. Validate each card for atomicity, source grounding, answerability, specificity, context, duplicate handling, and usefulness.
7. Rewrite or drop failed cards before returning the final deck.
8. Provide the requested export format when requested and feasible from portable text.

Default assumptions when the user does not specify:

- Audience: general professional learner.
- Goal: durable understanding and recall.
- Count: 15-30 cards, or fewer when the source cannot support that many useful cards.
- Difficulty: mixed, weighted toward useful retrieval.
- Output: Markdown plus canonical JSON.
- Source grounding: required for factual cards.

## Quality Rules

- One card tests one idea.
- Prefer retrieval over recognition when practical.
- Avoid broad prompts such as "Explain OAuth."
- Avoid trivia unless the user requests trivia.
- Do not create cards that are technically true but not worth reviewing.
- Merge near-duplicates unless bidirectional recall is intentional.
- Include enough context for project-specific or ambiguous terms.
- Cloze cards need enough surrounding context to be answerable.
- If the source is too thin for the requested count or difficulty, say so and produce only supportable cards.

## Combined Flashcard And Quiz Requests

If another skill can handle the quiz, keep this skill focused on flashcards and let the quiz skill provide its section.

If only this skill is active, use this compact fallback:

1. Extract shared learning objectives and one compact knowledge map.
2. Produce flashcards using this skill's full output contract.
3. Produce a compact quiz fallback section with a quiz blueprint, 3-5 diagnostic questions, answer key and rationales, and a separate quiz JSON payload.
4. Keep the flashcard and quiz sections and JSON payloads separate.
5. Do not create a merged study-artifacts schema.

## Source Boundaries

When source material is provided:

- Ground factual prompts and answers in that source.
- Mark external or inferred context as `inferred`.
- Do not present inferred or general background facts as source-grounded.
- Do not hide missing context inside the answer.
- Do not provide medical, legal, financial, or high-stakes exam-prep guarantees.

## Output Format

Use concise Markdown-compatible plain text. No emoji.

**Deck summary**
<purpose, audience, source scope, count, and export notes>

**Learning objectives**
1. <objective>
2. <objective>

**Knowledge map**
- Facts: <items>
- Concepts: <items>
- Procedures: <items or none>
- Distinctions: <items>
- Examples/non-examples: <items or none>
- Misconceptions: <items or none>
- Prerequisites: <items or none>

**Cards**
| ID | Type | Prompt | Answer | Source | Tags | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| F1 | <type> | <atomic prompt> | <answer> | <source/inferred> | <tags> | <explanation or quality note> |

**Canonical JSON**
```json
{
  "deck_title": "<title>",
  "audience": "<audience>",
  "source_scope": "<source summary>",
  "learning_objectives": ["<objective>"],
  "cards": [
    {
      "id": "F1",
      "type": "basic",
      "prompt": "<atomic prompt>",
      "answer": "<answer>",
      "source": {"kind": "source", "reference": "<source location or summary>"},
      "tags": ["<tag>"],
      "notes": "<explanation>",
      "quality_checks": {
        "atomic": true,
        "answerable": true,
        "source_grounded": true,
        "useful": true
      }
    }
  ]
}
```

**Requested export**
<Markdown, CSV, TSV, Anki-oriented text, or "Not requested">

**Quality check**
<one concise line confirming source grounding, atomicity, duplicate handling, and unsupported inference handling>
