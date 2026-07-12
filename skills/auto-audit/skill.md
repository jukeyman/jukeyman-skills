# Auto Security Audit Skill

Runs comprehensive security audit on the current project.

## Usage
```bash
zsh ~/.claude/scripts/auto-security-audit.sh
```

## What it checks:
- .env file exposure
- Hardcoded secrets scanning
- SQL injection vulnerabilities
- XSS vulnerabilities
- Command injection risks
- CORS configuration
- Security headers
- Dependency vulnerabilities (npm audit)

## When to use:
- Before any deployment
- Part of the full pipeline
- After adding new dependencies
