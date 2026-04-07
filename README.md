# ai-skills

[![Validate Skills](https://github.com/xiongxianfei/ai-skills/actions/workflows/validate.yml/badge.svg)](https://github.com/xiongxianfei/ai-skills/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A curated collection of AI prompts for writing, translation, and productivity — works with any model, installable as Claude Code skills.

## Skills

| Skill | Claude Command | Description |
|-------|---------------|-------------|
| [editor](skills/editor/SKILL.md) | `/editor` | 3-phase text polish + Chinese/English bilingual translation (supports Chinese, English, Russian input) |
| [communicator](skills/communicator/SKILL.md) | `/communicator` | Draft formal Russian messages from Chinese input, with Chinese translation and cultural strategy notes |
| [doctor](skills/doctor/SKILL.md) | `/doctor` | Medical consultation — symptoms, medications, lab reports, health advice, with referral guidance and safety flags |
| [fitness-coach](skills/fitness-coach/SKILL.md) | `/fitness-coach` | Personal fitness coach — training plans, exercise technique, nutrition, and recovery advice |
| [nvc](skills/nvc/SKILL.md) | `/nvc` | Nonviolent Communication coach — rewrites harsh or blaming messages into NVC framework (observation, feeling, need, request) |
| [email-drafter](skills/email-drafter/SKILL.md) | `/email-drafter` | Draft professional English emails with Chinese translation and writing strategy notes — support tickets, business, academic, complaints, follow-ups |
| [journaling](skills/journaling/SKILL.md) | `/journaling` | Guided daily reflection coach — turns your day into structured reflection, deep-dive prompts, an optional journal draft, and a clear intention for tomorrow |

---

## Installation

### Claude Code

Skills are loaded from `~/.claude/skills/` (personal, all projects) or `.claude/skills/` (project-level). Clone the repo and copy the skill folders you want:

#### Personal install — available in all your projects

```bash
git clone https://github.com/xiongxianfei/ai-skills
cp -r ai-skills/skills/editor ~/.claude/skills/editor
cp -r ai-skills/skills/communicator ~/.claude/skills/communicator
cp -r ai-skills/skills/doctor ~/.claude/skills/doctor
cp -r ai-skills/skills/fitness-coach ~/.claude/skills/fitness-coach
cp -r ai-skills/skills/nvc ~/.claude/skills/nvc
cp -r ai-skills/skills/email-drafter ~/.claude/skills/email-drafter
cp -r ai-skills/skills/journaling ~/.claude/skills/journaling
```

Restart Claude Code. Skills are available as `/editor`, `/communicator`, `/doctor`, `/fitness-coach`, `/nvc`, `/email-drafter`, and `/journaling`.

#### Project-level install — shared with your team

Run inside your project root:

```bash
git clone https://github.com/xiongxianfei/ai-skills
cp -r ai-skills/skills/editor .claude/skills/editor
cp -r ai-skills/skills/communicator .claude/skills/communicator
cp -r ai-skills/skills/doctor .claude/skills/doctor
cp -r ai-skills/skills/fitness-coach .claude/skills/fitness-coach
cp -r ai-skills/skills/nvc .claude/skills/nvc
cp -r ai-skills/skills/email-drafter .claude/skills/email-drafter
cp -r ai-skills/skills/journaling .claude/skills/journaling
```

Commit the `.claude/skills/` folder so teammates get the skills automatically.

#### Try it for one session (no install)

```bash
git clone https://github.com/xiongxianfei/ai-skills
claude --plugin-dir ./ai-skills
```

Skills are available as `/ai-skills:editor` and `/ai-skills:communicator` for this session only.

### Other AI models (ChatGPT, Gemini, etc.)

Each skill's prompt works with any model — just copy and paste:

1. Open `skills/<skill-name>/SKILL.md`
2. Copy everything **below** the `---` frontmatter block
3. Paste as the system prompt in your AI tool of choice

---

## Usage

### Claude Code

Invoke by slash command, passing your text as the argument:

```
/editor  Please polish this text for me.
/communicator  我想告诉房东暖气坏了，请帮我写一条俄语消息。
```

Or just describe what you want in natural language — Claude auto-invokes the right skill based on context.

### Other models

Paste the prompt as the system prompt, then send your input as the first user message.

---

## Skill Details

### `editor` — Text Polish & Bilingual Translation

Accepts Chinese, English, or Russian input and runs a 3-phase pipeline:

1. **Deep Optimization** — Clarify, condense, and elevate the text without changing its meaning. Each change is explained inline.
2. **Quality Assessment** — Grammar, tone, and cultural-appropriateness check on the optimized text.
3. **Bilingual Output** — Side-by-side Chinese/English translation of the final text.

Best for: technical documentation, academic writing, professional business communication.

### `communicator` — Formal Russian Communication Assistant

Takes your Chinese description of what you want to say and produces:

1. **Russian message** — Ready to send, culturally appropriate, using formal "Вы" register with proper greetings and closings.
2. **Chinese translation** — Exact translation of the Russian message.
3. **沟通建议** — Cultural strategy notes explaining the phrasing choices.

Default recipient is an elderly Russian landlady (Татьяна). Mention a different recipient/context in your input to adapt the tone.

Best for: landlord communication, formal letters, official correspondence with Russian contacts.

---

## Contributing

1. Fork the repo
2. Create a branch: `git checkout -b feat/your-skill-name`
3. Add your skill under `skills/<skill-name>/SKILL.md` following the [frontmatter schema](https://docs.anthropic.com/en/docs/claude-code/skills)
4. Open a PR — include what the skill does and when to use it

## License

MIT
