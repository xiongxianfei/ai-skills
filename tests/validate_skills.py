"""
Validate all skills in the skills/ directory against best-practice rules.

Rules checked per SKILL.md:
  [REQUIRED]  Frontmatter is valid YAML
  [REQUIRED]  name field present
  [REQUIRED]  description field present
  [REQUIRED]  argument-hint field present
  [REQUIRED]  $ARGUMENTS appears in the prompt body
  [REQUIRED]  ## Output Format section present in the prompt body
  [BEST PRACTICE]  effort field present
  [BEST PRACTICE]  allowed-tools field present
  [BEST PRACTICE]  description is in English (ASCII only)
  [BEST PRACTICE]  argument-hint is in English (ASCII only)

Rules checked for plugin.json:
  [REQUIRED]  Valid JSON
  [REQUIRED]  name, description, version, license fields present
"""

import json
import sys
from pathlib import Path

import yaml

SKILLS_DIR = Path(__file__).parent.parent / "skills"
PLUGIN_JSON = Path(__file__).parent.parent / ".claude-plugin" / "plugin.json"

REQUIRED_FRONTMATTER = ["name", "description", "argument-hint"]
BEST_PRACTICE_FRONTMATTER = ["effort", "allowed-tools"]
REQUIRED_PLUGIN_FIELDS = ["name", "description", "version", "license"]

errors = []
warnings = []


def error(path: str, msg: str):
    errors.append(f"  ERROR  {path}: {msg}")


def warn(path: str, msg: str):
    warnings.append(f"  WARN   {path}: {msg}")


def contains_non_latin_script(s: str) -> bool:
    """Return True if the string contains CJK or Cyrillic characters.

    Allows common typographic characters used in English (em dash, arrows, etc.)
    while catching descriptions written in Chinese, Russian, Japanese, etc.
    """
    for c in s:
        cp = ord(c)
        if (
            0x0400 <= cp <= 0x04FF   # Cyrillic
            or 0x3040 <= cp <= 0x309F  # Hiragana
            or 0x30A0 <= cp <= 0x30FF  # Katakana
            or 0x3400 <= cp <= 0x4DBF  # CJK Extension A
            or 0x4E00 <= cp <= 0x9FFF  # CJK Unified Ideographs
        ):
            return True
    return False


def parse_skill(path: Path) -> tuple[dict, str]:
    """Split SKILL.md into frontmatter dict and body string."""
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return {}, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}, text
    fm = yaml.safe_load(parts[1]) or {}
    body = parts[2]
    return fm, body


def validate_skill(skill_dir: Path):
    skill_file = skill_dir / "SKILL.md"
    label = f"skills/{skill_dir.name}/SKILL.md"

    if not skill_file.exists():
        error(label, "SKILL.md not found")
        return

    try:
        fm, body = parse_skill(skill_file)
    except yaml.YAMLError as e:
        error(label, f"invalid YAML frontmatter: {e}")
        return

    for field in REQUIRED_FRONTMATTER:
        if field not in fm:
            error(label, f"missing required frontmatter field: '{field}'")

    for field in BEST_PRACTICE_FRONTMATTER:
        if field not in fm:
            warn(label, f"missing best-practice frontmatter field: '{field}'")

    # English-only checks on fields shown in Claude Code UI
    desc = str(fm.get("description", ""))
    if desc and contains_non_latin_script(desc):
        warn(label, "description contains non-Latin script — use English for reliable auto-invocation")

    hint = str(fm.get("argument-hint", ""))
    if hint and contains_non_latin_script(hint):
        warn(label, "argument-hint contains non-Latin script — use English as it appears in the autocomplete UI")

    if "$ARGUMENTS" not in body:
        error(label, "$ARGUMENTS not found in prompt body — slash command input will be dropped")

    if "## Output Format" not in body:
        error(label, "## Output Format section missing — output structure is undefined")


def validate_plugin_json():
    label = ".claude-plugin/plugin.json"
    if not PLUGIN_JSON.exists():
        warn(label, "plugin.json not found — required for Claude Code plugin distribution")
        return

    try:
        data = json.loads(PLUGIN_JSON.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        error(label, f"invalid JSON: {e}")
        return

    for field in REQUIRED_PLUGIN_FIELDS:
        if field not in data:
            error(label, f"missing required field: '{field}'")


def main():
    skill_dirs = sorted(d for d in SKILLS_DIR.iterdir() if d.is_dir())

    if not skill_dirs:
        print("No skills found — add skill directories under skills/")
        sys.exit(1)

    print(f"Validating {len(skill_dirs)} skill(s)...\n")
    for skill_dir in skill_dirs:
        validate_skill(skill_dir)

    validate_plugin_json()

    if warnings:
        print("Warnings:")
        for w in warnings:
            print(w)
        print()

    if errors:
        print("Errors:")
        for e in errors:
            print(e)
        print(f"\n{len(errors)} error(s) found. Fix them before merging.")
        sys.exit(1)

    print(f"All {len(skill_dirs)} skill(s) passed validation.")
    if warnings:
        print(f"{len(warnings)} warning(s) — review recommended but not blocking.")


if __name__ == "__main__":
    main()
