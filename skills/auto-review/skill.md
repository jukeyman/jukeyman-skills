# Auto Code Review Skill

Runs automatic code review on the current project.

## Usage
```bash
zsh ~/.claude/scripts/auto-code-review.sh
```

## What it checks:
- TypeScript type errors
- console.log / debug statements
- TODO / FIXME / HACK comments
- Potential secrets in code
- Import validation

## When to use:
- After writing any code
- Before committing changes
- Part of the full pipeline
