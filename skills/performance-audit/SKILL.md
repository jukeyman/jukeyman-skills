---
name: performance-audit
description: Full performance audit with Core Web Vitals
---

# Performance Audit Protocol

1. Run Lighthouse CI (if configured)
2. Check bundle size: pnpm build && check .next/analyze/
3. Verify: LCP < 2.5s, INP < 200ms, CLS < 0.1
4. Check for: unoptimized images, render-blocking scripts,
   unnecessary client components, missing suspense boundaries
5. Check API p95 latency < 500ms
6. Identify top 3 optimization opportunities
7. Implement fixes and re-measure
