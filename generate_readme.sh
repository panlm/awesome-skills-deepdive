#!/bin/bash
# Generate README.md for a single skill
# Usage: bash generate_readme.sh "Category Name" "skill_name"

CATEGORY="$1"
SKILL="$2"
BASE_DIR="$HOME/openclaw-skill/awesome-skills-deepdive"
SKILL_DIR="$BASE_DIR/$CATEGORY/$SKILL"

if [ ! -d "$SKILL_DIR" ]; then
  echo "ERROR: $SKILL_DIR not found"
  exit 1
fi

# Already done?
if [ -f "$SKILL_DIR/README.md" ]; then
  echo "SKIP: $SKILL already has README.md"
  exit 0
fi

# Read metadata
META=""
OWNER=""
SLUG=""
DISPLAY=""
if [ -f "$SKILL_DIR/_meta.json" ]; then
  META=$(cat "$SKILL_DIR/_meta.json")
  OWNER=$(echo "$META" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('owner','unknown'))" 2>/dev/null)
  SLUG=$(echo "$META" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('slug',''))" 2>/dev/null)
  DISPLAY=$(echo "$META" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('displayName',''))" 2>/dev/null)
fi

[ -z "$OWNER" ] && OWNER="unknown"
[ -z "$SLUG" ] && SLUG="$SKILL"
[ -z "$DISPLAY" ] && DISPLAY="$SKILL"

CLAWHUB_URL="https://clawskills.sh/skills/${OWNER}-${SLUG}"
GITHUB_URL="https://github.com/openclaw/skills/tree/main/skills/${OWNER}/${SLUG}"

echo "PROCESS: $CATEGORY/$SKILL (owner=$OWNER)"
