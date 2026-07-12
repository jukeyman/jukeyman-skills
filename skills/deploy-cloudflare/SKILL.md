---
name: deploy-cloudflare
description: Deploy any project to Cloudflare Workers or Pages. Use when Rick says deploy, ship, or push to production.
disable-model-invocation: true
allowed-tools: Bash, Read, Write, Edit
---

# Deploy to Cloudflare

## Pre-Deploy Checklist
1. Verify `wrangler.toml` exists with correct account_id
2. Run `pnpm build` — must pass cleanly
3. Run `pnpm test` if tests exist
4. Verify no secrets in code (check .env is gitignored)

## Deploy Commands

### For Workers:
```bash
wrangler deploy
```

### For Pages:
```bash
wrangler pages deploy ./out --project-name=$ARGUMENTS
```

### For D1 Database Migrations:
```bash
wrangler d1 migrations apply <database-name>
```

## Post-Deploy
1. Verify deployment URL is live
2. Test critical paths (homepage, auth, API health)
3. Push to GitHub with deployment URL in commit message
4. Report deployment URL to Rick

## Cloudflare Config
- Account ID: 58250b56ae5b45d940cd6e4b64314c01
- Zone: rickjeffersonsolutions.com (18e1ffe3c8a6b6c965860aa0bae60357)
