---
name: test-coverage
description: Analyze and improve test coverage
---

# Test Coverage Protocol

1. Run: pnpm test --coverage
2. Identify files below 80% coverage
3. Prioritize: API routes > auth logic > form handlers > UI components
4. Write missing unit tests (Jest + React Testing Library)
5. Write missing integration tests for untested API endpoints
6. Write E2E tests for critical user flows (Playwright)
7. Re-run coverage. Target: ≥80% overall
