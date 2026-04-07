## Summary

<!-- What does this PR add or change? One sentence per skill or change. -->

## Checklist

### For new skills
- [ ] Skill directory follows the pattern `skills/<skill-name>/SKILL.md`
- [ ] `description` is in English and under 250 characters
- [ ] `argument-hint` is in English
- [ ] `effort: high` is set (for complex, multi-step skills)
- [ ] `allowed-tools: ""` is set (for pure prompt skills)
- [ ] `$ARGUMENTS` appears in the prompt body
- [ ] `## Output Format` section is present
- [ ] No emojis in the Output Format section
- [ ] CI validation passes (`python tests/validate_skills.py`)
- [ ] Skill added to the README skills table
- [ ] Skill added to the install commands in README

### For bug fixes / improvements
- [ ] Describe what was wrong and why the fix is correct
- [ ] CI validation still passes

## Test plan

<!-- How did you verify this works? Example inputs and outputs. -->
