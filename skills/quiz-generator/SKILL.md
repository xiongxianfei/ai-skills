---
name: quiz-generator
description: >
  Quiz generator that creates source-grounded diagnostic quizzes with blueprints, objectives, answer keys, rationales, feedback, rubrics, and canonical JSON. Use for quizzes, diagnostic questions, comprehension checks, MCQs, short-answer items, assessment items, and feedback from notes, documents, code, courses, papers, or project material.
---

## Input

$ARGUMENTS

## Core Standard

Create diagnostic and learning-oriented quiz questions from the user's supplied source material. Test more than recall when the source supports it: comprehension, contrast, application, prediction, diagnosis, transfer, and tradeoff judgment.

Use the user's supplied source as the factual base. Mark inferred or external context explicitly when the user asks for advanced or related questions beyond the source. Avoid unsupported details.

Use local references when useful:

- `references/learning-design.md` for shared learning-design principles.
- `references/question-quality.md` for quiz-specific quality checks.
- `schemas/quiz-item.schema.json` as the reference contract for canonical JSON. The schema is documentation only; do not claim executable validation.

## Workflow

1. Identify quiz purpose, audience, source material, difficulty, question count, question types, and requested export format when provided.
2. Extract learning objectives before writing questions.
3. Build a compact knowledge map:
   - facts;
   - concepts;
   - procedures;
   - distinctions;
   - examples and non-examples;
   - prerequisites;
   - common misconceptions.
4. Create a quiz blueprint covering:
   - objective coverage;
   - cognitive-level distribution;
   - question-type distribution;
   - difficulty distribution.
5. Generate questions from the blueprint.
6. Validate each item for objective alignment, source grounding, answerability, ambiguity, appropriate difficulty, useful feedback, and redundancy.
7. Rewrite or drop failed items before returning the final quiz.
8. Provide the requested export format when requested and feasible from portable text.

Default assumptions when the user does not specify:

- Purpose: diagnostic learning quiz.
- Audience: general professional learner.
- Count: 7-10 questions, or fewer when the source cannot support that many useful questions.
- Difficulty: mixed.
- Output: Markdown plus canonical JSON.
- Feedback: include answer key, rationales, and remediation unless the user asks for interactive mode.

## Question Rules

- Every item maps to a learning objective.
- Every answer key entry is correct for the supplied source or clearly marked inference.
- Difficulty should be effortful but answerable.
- Avoid ambiguous wording and multiple defensible answers unless the question is explicitly marked as multi-answer or discussion-based.
- Include application, prediction, diagnosis, or transfer items when appropriate.
- Do not create unsupported advanced questions from thin source material.
- Do not provide medical, legal, financial, or high-stakes exam-prep guarantees.

For MCQs:

- Use a clear stem.
- Provide one best answer unless multiple-select is explicitly requested.
- Make distractors plausible but clearly wrong.
- Avoid grammatical clues.
- Avoid "all of the above" and "none of the above" by default.
- Explain why each option is right or wrong.

If the user asks for both flashcards and a quiz, keep the quiz output separate from flashcard output and use a separate canonical JSON payload for the quiz.

## Source Boundaries

When source material is provided:

- Ground factual questions and answers in that source.
- Mark external or inferred context as `inferred`.
- Do not present inferred or general background facts as source-grounded.
- Avoid questions that require hidden context to answer.
- If source material is too thin for the requested count or difficulty, say so and produce only supportable questions.

## Output Format

Use concise Markdown-compatible plain text. No emoji.

**Quiz blueprint**
- Purpose: <purpose>
- Audience: <audience>
- Source scope: <source summary>
- Objective coverage: <objective-to-count mapping>
- Cognitive levels: <distribution>
- Question types: <distribution>
- Difficulty: <distribution>

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

**Questions**
1. <question>
   - Type: <MCQ/short-answer/etc.>
   - Objective: <objective>
   - Cognitive level: <level>
   - Difficulty: <difficulty>
   - Answer: <answer>
   - Rationale: <why the answer is correct>
   - Feedback: <remediation or misconception note>
   - Source: <source/inferred reference>

**Canonical JSON**
```json
{
  "quiz_title": "<title>",
  "purpose": "<purpose>",
  "audience": "<audience>",
  "source_scope": "<source summary>",
  "blueprint": {
    "objective_coverage": [{"objective": "<objective>", "count": 1}],
    "cognitive_levels": {"recall": 1, "comprehension": 1, "application": 1},
    "question_types": {"mcq": 1, "short_answer": 1},
    "difficulty": {"easy": 1, "medium": 1, "hard": 0}
  },
  "questions": [
    {
      "id": "Q1",
      "type": "mcq",
      "objective": "<objective>",
      "cognitive_level": "application",
      "difficulty": "medium",
      "stem": "<question>",
      "options": [
        {"id": "A", "text": "<option>", "is_correct": true, "rationale": "<why>"}
      ],
      "answer": "<answer>",
      "feedback": "<feedback>",
      "source": {"kind": "source|inferred", "reference": "<reference or rationale>"}
    }
  ]
}
```

**Requested export**
<Markdown, JSON, answer key, LMS-oriented text, or "Not requested">

**Quality check**
<one concise line confirming objective alignment, source grounding, ambiguity check, feedback quality, and unsupported inference handling>
