---
name: deploy
description: Build and deploy to Cloudflare or Vercel
argument-hint: <target: cf|vercel>
---

# Deploy Workflow

1. Run: pnpm typecheck && pnpm lint && pnpm test
2. Run: pnpm audit --audit-level critical
3. If target=cf: wrangler deploy
4. If target=vercel: vercel --prod
5. Verify deployment URL returns 200
6. Check Sentry for new errors (wait 2 min)
7. Report deployment status with live URL
