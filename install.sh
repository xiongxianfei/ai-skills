#!/usr/bin/env bash
# install.sh — install all ai-skills into ~/.claude/skills/
set -euo pipefail

REPO_URL="https://github.com/xiongxianfei/ai-skills"
SKILLS_DIR="${HOME}/.claude/skills"
TMP_DIR="$(mktemp -d)"

cleanup() { rm -rf "$TMP_DIR"; }
trap cleanup EXIT

echo "Cloning ai-skills..."
git clone --depth=1 --quiet "$REPO_URL" "$TMP_DIR/ai-skills"

mkdir -p "$SKILLS_DIR"

installed=0
for skill_dir in "$TMP_DIR/ai-skills/skills"/*/; do
    skill_name="$(basename "$skill_dir")"
    target="$SKILLS_DIR/$skill_name"
    if [ -d "$target" ]; then
        rm -rf "$target"
    fi
    cp -r "$skill_dir" "$target"
    echo "  installed: $skill_name"
    installed=$((installed + 1))
done

echo ""
echo "$installed skill(s) installed to $SKILLS_DIR"
echo "Restart Claude Code to activate them."
