#!/bin/bash
# Elite Planning Skill
# Usage: /plan [project-name] [type]

PLAN_TYPE="${1:-fullstack}"
PROJECT_NAME="${2:-my-project}"

source ~/.claude/rj-plan.sh 2>/dev/null
rj-plan "$PROJECT_NAME" "$PLAN_TYPE"
