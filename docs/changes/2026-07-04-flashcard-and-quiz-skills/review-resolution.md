# Review Resolution: Flashcard And Quiz Generator Skills

## Summary

- Closeout status: closed
- Review source: PR #32 human review, received 2026-07-05
- Material findings: 2
- Accepted: 2
- Rejected: 0
- Deferred: 0
- Partially accepted: 0
- Needs decision: 0

Both material findings were accepted. The resolution updates only the two new skill prompts and related evidence/lifecycle artifacts.

## Resolution Overview

| Finding ID | Severity | Disposition | Resolution | Validation |
| --- | --- | --- | --- | --- |
| F-PR32-SKILL-001 | major | accepted | Aligned canonical JSON examples with schema-valid `source.kind` values, added explicit `source`/`inferred` rules, and changed flashcard card type spelling to `example-non-example`. | `python tests/validate_skills.py`; unit tests; README sync; JSON/YAML parse; `git diff --check`; line count check. |
| F-PR32-SKILL-002 | major | accepted | Added compact combined-request fallback sections to both skills for single-skill invocation while preserving separate artifact sections and JSON payloads. | `python tests/validate_skills.py`; unit tests; README sync; `git diff --check`; line count check. |

## Finding Details

### F-PR32-SKILL-001

- Finding ID: F-PR32-SKILL-001
- Severity: major
- Location:
  - `skills/flashcard-generator/SKILL.md`
  - `skills/flashcard-generator/schemas/flashcard.schema.json`
  - `skills/quiz-generator/SKILL.md`
  - `skills/quiz-generator/schemas/quiz-item.schema.json`
- Evidence: Prompt examples used `"source|inferred"` as a literal placeholder while schemas require `"source"` or `"inferred"`. Flashcard prompt used `example/non-example` while the schema enum uses `example-non-example`.
- Required outcome: Prompt examples and wording must demonstrate schema-valid canonical JSON values.
- Safe resolution path: Update both prompt JSON examples to use `"source"`, add plain-language `source`/`inferred` rules, and align flashcard type spelling with the schema.
- Final disposition: accepted and fixed.
- Files changed:
  - `skills/flashcard-generator/SKILL.md`
  - `skills/quiz-generator/SKILL.md`

### F-PR32-SKILL-002

- Finding ID: F-PR32-SKILL-002
- Severity: major
- Location:
  - `skills/flashcard-generator/SKILL.md`
  - `skills/quiz-generator/SKILL.md`
  - `specs/flashcard-and-quiz-skills.md`
  - eval fixtures
- Evidence: Both prompts preserved separate sections and JSON payloads for combined flashcard-and-quiz requests, but neither documented enough compact fallback structure for the other artifact when only one skill is active.
- Required outcome: Combined-output fallback must be implementable without turning the two skills into one broad skill.
- Safe resolution path: Add compact combined-request sections to both skills that prefer composition when available, otherwise produce a small fallback section for the other artifact with separate JSON payloads.
- Final disposition: accepted and fixed.
- Files changed:
  - `skills/flashcard-generator/SKILL.md`
  - `skills/quiz-generator/SKILL.md`

## Shared Validation Evidence

Working directory: `/home/xiongxianfei/data/20260525-skillsmith`

| Command | Result | Notes |
| --- | --- | --- |
| `python tests/validate_skills.py` | passed | Passed for 13 skills with the known non-blocking grandfathered-evals warning for unrelated older skills. |
| `python -m unittest discover tests` | passed | Ran 31 tests. |
| `python tests/check_readme_sync.py` | passed | README sync check passed. |
| `git diff --check` | passed | No whitespace errors. |
| `python - <<'PY' ... json/yaml ok` | passed | Parsed change metadata, eval fixtures, and reference schemas. |
| `wc -l skills/flashcard-generator/SKILL.md skills/quiz-generator/SKILL.md` | passed | `flashcard-generator` 149 lines; `quiz-generator` 170 lines. |

## Closeout Checklist

- [x] Every material finding has a final disposition.
- [x] No finding has `needs-decision`.
- [x] Accepted findings have concrete file changes.
- [x] Validation evidence is recorded.
- [x] Review log is updated.
- [x] No `review-resolution.md` item remains open.
