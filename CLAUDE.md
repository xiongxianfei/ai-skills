# ai-skills

Reusable AI prompt skills for writing, translation, and productivity. Each skill is a SKILL.md file with YAML frontmatter — works with any AI model, installable as Claude Code slash commands.

## Build & Validate

```
python tests/validate_skills.py
```

CI runs this on every push/PR to main. All errors must be fixed before merge.

## Skill File Format

Every skill lives at `skills/<skill-name>/SKILL.md`. Required structure:

```yaml
---
name: <lowercase-hyphenated>
description: >
  English only, under 250 chars. Must be "pushy" — include explicit
  "Use this skill whenever..." phrasing to prevent undertriggering.
argument-hint: <English, describes expected user input>
effort: high
allowed-tools: ""
---
```

Body must contain:
- `$ARGUMENTS` placeholder (so slash command input flows through)
- `## Output Format` section (enforced by CI)

## Key Rules

- Descriptions MUST be English — skill bodies can be any language
- Descriptions should be trigger-phrase-forward and "pushy" per Anthropic's official guidance: tell Claude when to auto-invoke, including indirect/casual user phrasing
- `effort: high` for all skills (they are multi-step reasoning tasks)
- `allowed-tools: ""` for all skills (pure prompt, no tool use)
- No emojis in Output Format headers

## Workflow

- All changes via PR to `main` (branch protection enabled)
- Branch naming: `feat/`, `fix/`, `docs/`, `improve/`
- Squash merge, delete branch after merge
- IMPORTANT: Always branch from latest `main` — never stack PRs from the same base to avoid README conflicts
- When adding a new skill, also add it to the README skills table

## Project Structure

```
skills/*/SKILL.md          ← the skills (10 currently)
tests/validate_skills.py   ← CI validator (errors block merge, warnings don't)
install.sh                 ← one-command installer (supports --target flag)
.claude-plugin/plugin.json ← plugin manifest (update version when releasing)
```

## Common Mistakes

- Forgetting `$ARGUMENTS` in the body → CI error
- Missing `## Output Format` → CI error
- Non-English description or argument-hint → CI warning (CJK/Cyrillic detected)
- Using passive descriptions ("Triggers when...") instead of pushy ("Use this skill whenever...") → skill won't auto-invoke reliably
