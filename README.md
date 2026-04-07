# claude-skills

A curated collection of Claude Code skills for text polishing, bilingual translation, and writing assistance.

## Skills

| Skill | Command | Description |
|-------|---------|-------------|
| [editor](skills/editor/SKILL.md) | `/ai-skills:editor` | 3-phase text polish + Chinese/English bilingual translation (supports Chinese, English, Russian input) |
| [communicator](skills/communicator/SKILL.md) | `/ai-skills:communicator` | Draft culturally appropriate Russian Telegram messages for formal/elderly recipients, with Chinese translation and strategy notes |

## Installation

### Option 1 — Project-level (recommended for teams)

Clone into your project's `.claude/` directory:

```bash
git clone https://github.com/xiongxianfei/ai-skills .claude/plugins/ai-skills
```

Then launch Claude Code — skills are auto-discovered.

### Option 2 — Personal (available in all projects)

Clone into your personal Claude directory:

```bash
git clone https://github.com/xiongxianfei/ai-skills ~/.claude/plugins/ai-skills
```

### Option 3 — Dev / try it out

Point Claude Code at the local directory directly:

```bash
claude --plugin-dir ./claude-skills
```

## Usage

Once installed, invoke a skill via its slash command:

```
/claude-skills:editor <your text here>
```

Or just paste text and ask Claude to polish/translate it — the skill's description guides auto-invocation.

## Skill Details

### `editor` — Text Polish & Bilingual Translation

Accepts Chinese, English, or Russian input and runs a structured 3-phase pipeline:

1. **Deep Optimization** — Clarify, condense, and elevate the text without changing its meaning. Each change is explained.
2. **Quality Assessment** — Grammar, tone, and cultural-appropriateness check on the optimized text.
3. **Bilingual Output** — Side-by-side Chinese/English translation of the final text.

Designed for technical documentation, academic writing, and professional business communication.

## Contributing

1. Fork the repo
2. Add your skill under `skills/<skill-name>/SKILL.md`
3. Follow the frontmatter schema (see [Claude Code Skills docs](https://docs.anthropic.com/en/docs/claude-code/skills))
4. Open a PR with a brief description of what the skill does and when to use it

## License

MIT
