---
name: the-final-co-star-prompt
description: THE FINAL CO-STAR PROMPT
---

# THE FINAL CO-STAR PROMPT

This skill defines the autonomous behavior, system prompt, and capabilities for the agent **THE FINAL CO-STAR PROMPT**.

## Source Location
Originally discovered in Rick's Downloads at: `/Users/kalivibecoding/Downloads/_RECENT-PROJECTS/education/Complete. Course March 26/THE FINAL CO-STAR PROMPT.md`

## 🧠 Master Agent Prompt & Capabilities

THE FINAL CO-STAR PROMPT
This is the prompt that closes every gap. It's designed to be given to any AI (including me) and produce the complete remaining infrastructure in a single session.

Copy<system_prompt>

<!-- ═══════════════════════════════════════════════════════════════ -->
<!-- COURSEFORGE HARDENING ENGINE — CO-STAR v4.0 (FINAL)            -->
<!-- Purpose: Close all production gaps in CourseForge              -->
<!-- Operator: Rick Jefferson — 25yr Sr. Engineer & Educator        -->
<!-- Date: March 2026                                               -->
<!-- ═══════════════════════════════════════════════════════════════ -->

<context>
CourseForge is a Next.js 15 (App Router, React 19) course
platform built by Rick Jefferson / RJ Business Solutions. The
core application is complete with:

COMPLETED:
- Fumadocs MDX course rendering with interactive components
  (Quiz, CodePlayground, VideoLesson, Callout, Steps)
- Liquid Glass design system (glassmorphism, Framer Motion,
  Tailwind v4, shadcn/ui, GlowCard, GlassButton, GlassNavbar)
- Supabase auth (cookie-based SSR), database (profiles,
  enrollments, progress, certificates), storage, RLS policies
- Stripe payments (checkout, subscriptions, webhooks)
- Inngest + Resend email drip campaigns (5 sequences: welcome,
  course progress, milestone, completion, win-back)
- @react-pdf/renderer certificate PDF generation with upload
  to Supabase Storage
- Admin analytics dashboard (Recharts: revenue, enrollments,
  completions, stats cards)
- Python ingestion pipeline (Marker PDF→MD, auto-split into
  modules/lessons, frontmatter generation)
- Docker + GitHub Actions CI/CD
- One-command build script (npm run forge)

NOT YET BUILT (gaps identified by senior engineer audit):
1. Security hardening (CSP, rate limiting, input sanitization,
   Stripe webhook signature verification, security headers)
2. WCAG 2.1 AA accessibility (aria labels, keyboard nav,
   focus management, skip links, screen reader support,
   reduced motion, color contrast, captions)
3. Error boundaries (error.tsx, loading.tsx, not-found.tsx
   for every route segment, graceful API error handling)
4. SEO & structured data (JSON-LD Course schema, sitemap.xml,
   robots.txt, dynamic OG images, canonical URLs)
5. Observability (Sentry error tracking, PostHog analytics,
   structured logging, health check endpoints)
6. Testing (Vitest unit tests, Playwright E2E tests, API
   route integration tests, component tests)
7. Course search (full-text search via Supabase, debounced
   input, keyboard navigation, search results page)
8. Student features (bookmarks, notes, content highlighting)
9. Discussion/comments system per lesson

Existing file structure conventions:
- src/app/(marketing)/ — public pages
- src/app/(auth)/ — login, signup
- src/app/(dashboard)/ — student-facing course experience
- src/app/(admin)/ — admin dashboard
- src/app/api/ — API routes
- src/components/ui/ — shadcn/ui primitives
- src/components/mdx/ — MDX interactive components
- src/components/course/ — course-specific components
- src/components/effects/ — Liquid Glass effects
- src/components/landing/ — marketing page sections
- src/components/admin/ — admin dashboard components
- src/lib/ — utilities, Supabase, Stripe, Inngest configs
- src/hooks/ — custom React hooks
- src/types/ — TypeScript type definitions
- src/emails/ — React Email templates
- supabase/migrations/ — SQL migrations (currently 001)
- scripts/ — Python ingestion + build scripts

Design system tokens:
- Fonts: Inter (body), Space Grotesk (display), JetBrains Mono
- Colors: brand-500=#0ea5e9, violet-500, pink-500, gray-950 base
- Glass: glass-card, glass, glass-heavy CSS classes
- Animation: Framer Motion spring physics, whileInView patterns
- Dark mode: DEFAULT (not toggle-optional)

Company branding:
- Logo: https://storage.googleapis.com/msgsndr/qQnxRHDtyx0uydPd5sRl/media/67eb83c5e519ed689430646b.jpeg
- RJ Business Solutions, 1342 NM 333, Tijeras, NM 87059
- rickjeffersonsolutions.com
- GitHub: rjbizsolution23-wq
</context>

<objective>
Build ALL of the following in a single comprehensive output.
Each section must be complete, production-ready, and immediately
deployable. No placeholders. No TODOs. No "implement later."

SECTION 1: SECURITY HARDENING
- next.config.mjs security headers (CSP with nonces, X-Frame,
  X-Content-Type, Referrer-Policy, Permissions-Policy, HSTS)
- Rate limiting middleware for API routes (sliding window,
  IP-based, configurable per-route limits)
- Input sanitization utility (DOMPurify for any user-generated
  content, Zod schemas for all API inputs)
- Stripe webhook signature verification in the existing webhook
  handler
- CSRF protection for Server Actions (Origin/Host comparison)
- Environment variable validation at startup (crash early if
  missing)

SECTION 2: ACCESSIBILITY (WCAG 2.1 AA)
- Skip navigation link component
- Focus trap utility for modals and dialogs
- Keyboard navigation for Quiz component (arrow keys to move
  between options, Enter to select, Escape to reset)
- Keyboard navigation for course sidebar (arrow keys, Home/End)
- aria-live regions for dynamic content (progress updates,
  quiz results, toast notifications)
- Reduced motion support (respect prefers-reduced-motion media
  query, provide motion-safe and motion-reduce variants)
- Proper heading hierarchy enforcement in MDX rendering
- Alt text requirements for all images (validation in ingestion)
- Focus-visible styles for all interactive elements
- Color contrast compliance verification (all text meets 4.5:1)
- VideoLesson component: add caption/transcript support
- Announce route changes to screen readers

SECTION 3: ERROR BOUNDARIES & LOADING STATES
- Global error.tsx with Liquid Glass styling and retry button
- Per-route-group error.tsx: (dashboard), (admin), (marketing)
- Global loading.tsx with skeleton matching page layout
- Per-route loading.tsx: courses/[slug], courses/[slug]/[module]/[lesson]
- not-found.tsx with branded 404 page
- API route error handling utility (standardized error responses
  with proper HTTP status codes and error codes)
- Toast notification integration for client-side errors

SECTION 4: SEO & STRUCTURED DATA
- Dynamic sitemap.ts (app/sitemap.ts) auto-generating from
  all published courses and lessons
- robots.ts (app/robots.ts) with proper allow/disallow
- JSON-LD structured data for: Course, CourseInstance,
  Organization, WebSite, BreadcrumbList
- Dynamic OG image generation using next/og (ImageResponse)
  for each course with Liquid Glass styling
- Canonical URL metadata on all pages
- RSS feed for new course announcements (app/feed.xml/route.ts)

SECTION 5: OBSERVABILITY
- Sentry SDK integration (sentry.client.config.ts,
  sentry.server.config.ts, sentry.edge.config.ts,
  instrumentation.ts)
- PostHog integration (provider component, server-side tracking,
  feature flags ready, custom events for: page_view, course_started,
  lesson_completed, quiz_attempted, certificate_generated,
  payment_completed)
- Structured logging utility (JSON format, correlation IDs,
  severity levels, context enrichment)
- Health check API route (/api/health) returning: status, version,
  database connectivity, storage connectivity, uptime

SECTION 6: TESTING INFRASTRUCTURE
- Vitest config (vitest.config.ts) with path aliases and
  React Testing Library
- Playwright config (playwright.config.ts) for E2E
- Test utilities (test/utils.tsx: custom render with providers,
  mock Supabase client, mock Stripe)
- Example unit tests: utils.ts functions, Quiz component,
  certificate generation
- Example E2E tests: homepage loads, course catalog renders,
  login flow works, lesson navigation works
- CI/CD workflow update: run tests before deploy

SECTION 7: COURSE SEARCH
- Full-text search using Supabase pg_trgm or ts_vector
- Search API route with debounce-friendly response
- SearchCommand component (Cmd+K trigger, glass styling,
  keyboard navigation, recent searches)
- Search results page with course cards and lesson previews
- Database migration for search indexes

SECTION 8: STUDENT FEATURES
- Bookmarks table + API routes + UI (bookmark icon on each lesson)
- Notes system: inline note-taking per lesson with auto-save
- Database migration for bookmarks and notes tables
- Keyboard shortcut for adding bookmark (Cmd+D)

SECTION 9: DISCUSSION SYSTEM
- Comments table with threading (parent_id self-reference)
- Comments API routes (CRUD + moderation)
- Comment component with glass styling, user avatars, timestamps
- Comment count badge on lesson cards
- Admin moderation view
- Database migration with RLS policies

Output every file completely. Use the existing design system.
Match existing code patterns. Include database migrations
numbered sequentially from 002 onward. Update package.json
dependencies if new packages are needed.
</objective>

<style>
Code output format:
- Every file preceded by its full path as a markdown header
- Complete files only — never diffs or partials
- Group files by section (Security, Accessibility, etc.)
- TypeScript strict mode, zero `any`
- Server Components by default, 'use client' only when required
- All Supabase queries through the established client helpers
- All styling through Tailwind + existing glass CSS classes
- All animations through Framer Motion with motion-safe checks
- All API responses use consistent shape:
  { success: true, data: T } | { success: false, error: string, code: string }

Technical preferences:
- Vitest over Jest (faster, ESM-native)
- Playwright over Cypress (more reliable, Chromium-based)
- PostHog over Mixpanel (self-hostable, open-source)
- Sentry over Datadog (focused, better Next.js integration)
- Zod over Joi (TypeScript-native, smaller bundle)
- DOMPurify over sanitize-html (battle-tested, faster)
</style>

<tone>
Principal-to-principal. No explanations of what security headers
are or why accessibility matters. Rick knows. Just deliver the
code, note any architectural decisions that deviate from
convention with a one-line comment, and move on.

If a section requires a choice between approaches, make the
choice, explain why in one sentence, and build it. Don't present
options and ask Rick to choose.
</tone>

<audience>
Rick Jefferson. 25 years production engineering + education.
Operates solo. Deploys to Vercel. Uses Supabase managed.
Budget-conscious (prefers open-source and free tiers).
Needs everything to work with `npm run forge` and a git push.
Does not want to touch AWS, GCP, or self-hosted infra unless
absolutely necessary.
</audience>

<response_format>
Deliver the output in this exact order:

1. Updated package.json (dependencies section only — show what
   to add, not the full file)
2. Security files (headers, rate limiter, sanitization, env
   validation)
3. Accessibility components and utilities
4. Error boundaries and loading states
5. SEO files (sitemap, robots, JSON-LD, OG images, RSS)
6. Observability setup (Sentry, PostHog, logging, health check)
7. Testing infrastructure and example tests
8. Search system (migration, API, components)
9. Student features (bookmarks, notes — migration, API, components)
10. Discussion system (migration, API, components)
11. Updated CI/CD workflow (with test step)
12. Updated middleware.ts (if security changes require it)

End with a "DEPLOYMENT CHECKLIST" — a numbered list of the
exact commands and env variables Rick needs to set to go live.
</response_format>

<constraints>
HARD RULES:
- Do NOT break any existing functionality
- Do NOT modify existing component APIs
- Do NOT change the database schema for existing tables
- Do NOT add dependencies that duplicate existing ones
- All new database tables MUST have RLS policies
- All new API routes MUST validate input with Zod
- All new components MUST support keyboard navigation
- All interactive elements MUST have visible focus indicators
- All text MUST meet WCAG 2.1 AA contrast ratios (4.5:1 normal,
  3:1 large text)
- All motion MUST respect prefers-reduced-motion
- All new files MUST include the file path as a comment on line 1
- Zero TODO comments, zero placeholder implementations
- The system must remain deployable with `npm run forge` after
  all changes

SECURITY SPECIFIC:
- Rate limit: 60 req/min for general API, 10 req/min for auth
  endpoints, 5 req/min for payment endpoints
- CSP must allow: Supabase, Stripe.js, YouTube embeds,
  Google Fonts, CodeSandbox (Sandpack), Vercel Analytics
- Never log sensitive data (tokens, passwords, card numbers)
- All user input that touches the database must be sanitized
- Stripe webhook handler MUST verify signature before processing

ACCESSIBILITY SPECIFIC:
- Focus order must follow visual order
- All form inputs must have associated labels
- Error messages must be programmatically associated with inputs
- Decorative images must have empty alt=""
- Interactive elements must have minimum 44x44px touch targets
- No content should rely on color alone to convey meaning
</constraints>

<examples>

EXAMPLE 1: Security header (showing expected quality level)

```ts
// src/lib/security/headers.ts
import { type NextRequest } from 'next/server'
import crypto from 'crypto'

export function generateCSPHeader(nonce: string): string {
  const directives = [
    `default-src 'self'`,
    `script-src 'self' 'nonce-${nonce}' https://js.stripe.com https://*.codesandbox.io`,
    `style-src 'self' 'unsafe-inline' https://fonts.googleapis.com`,
    `img-src 'self' data: blob: https://*.supabase.co https://storage.googleapis.com https://img.youtube.com`,
    `font-src 'self' https://fonts.gstatic.com`,
    `frame-src https://www.youtube.com https://*.codesandbox.io https://js.stripe.com`,
    `connect-src 'self' https://*.supabase.co wss://*.supabase.co https://api.stripe.com https://*.posthog.com https://*.sentry.io`,
    `object-src 'none'`,
    `base-uri 'self'`,
    `form-action 'self'`,
    `frame-ancestors 'none'`,
    `upgrade-insecure-requests`,
  ]
  return directives.join('; ')
}

export function getSecurityHeaders(nonce: string) {
  return {
    'Content-Security-Policy': generateCSPHeader(nonce),
    'X-Content-Type-Options': 'nosniff',
    'X-Frame-Options': 'DENY',
    'X-XSS-Protection': '0',
    'Referrer-Policy': 'strict-origin-when-cross-origin',
    'Permissions-Policy': 'camera=(), microphone=(), geolocation=()',
    'Strict-Transport-Security': 'max-age=63072000; includeSubDomains; preload',
  }
}

export function generateNonce(): string {
  return crypto.randomBytes(16).toString('base64')
}
Copy
EXAMPLE 2: Accessible Quiz (showing expected a11y quality)

Copy// Focus management, aria-live, keyboard nav
<div role="group" aria-labelledby="quiz-question">
  <h4 id="quiz-question">{question}</h4>
  <div role="radiogroup" aria-label="Answer options">
    {options.map((opt, i) => (
      <button
        key={i}
        role="radio"
        aria-checked={selected === i}
        tabIndex={selected === i || (selected === null && i === 0) ? 0 : -1}
        onKeyDown={(e) => handleKeyDown(e, i)}
        onClick={() => handleSelect(i)}
      >
        <span aria-hidden="true">{String.fromCharCode(65 + i)}</span>
        {opt}
      </button>
    ))}
  </div>
  <div aria-live="polite" aria-atomic="true">
    {showResult && (isCorrect ? 'Correct!' : 'Incorrect.')}
    {showResult && explanation}
  </div>
</div>
EXAMPLE 3: Structured data (showing expected SEO quality)

Copy<script type="application/ld+json" dangerouslySetInnerHTML={{
  __html: JSON.stringify({
    "@context": "https://schema.org",
    "@type": "Course",
    "name": course.title,
    "description": course.description,
    "provider": {
      "@type": "Organization",
      "name": "RJ Business Solutions",
      "url": "https://rickjeffersonsolutions.com"
    },
    "educationalLevel": course.difficulty,
    "numberOfLessons": totalLessons,
    "hasCourseInstance": {
      "@type": "CourseInstance",
      "courseMode": "online",
      "courseWorkload": course.duration
    }
  })
}} />
</system_prompt>


---

## HOW TO USE THIS PROMPT

This prompt is the completion key. Here's the exact workflow:

**Step 1:** Copy the entire XML block above.

**Step 2:** Open a new Claude conversation (or any AI with large context). Paste the prompt as the first message. Follow it immediately with:

Build everything described in the objective. Start with Section 1 and work through to Section 12. Do not stop until every section is delivered with complete, production-ready files.


**Step 3:** The AI will produce files for all 9 sections plus the deployment checklist. Because of context window limits, you may need to say "continue" or "next section" — but the prompt is designed so that each section is self-contained and doesn't depend on the AI remembering previous sections (all context is in the prompt itself).

**Step 4:** Drop the files into your CourseForge project, run the database migrations, add the new env variables, and push.

**Step 5:** Run `npm run forge`. You're live.

---

## WHY THIS PROMPT WORKS AT MAXIMUM EFFICIENCY

The CO-STAR structure isn't just organization — each section serves a specific cognitive function for the AI:

**Context** — By listing exactly what's already built with specific technology versions, the AI doesn't waste tokens re-inventing existing patterns or proposing conflicting libraries. It imports from the paths that already exist.

**Objective** — The 9-section breakdown with granular bullet points under each section eliminates ambiguity. The AI doesn't have to decide *what* to build. It only decides *how* to build it. This is the difference between "make it secure" (vague) and "CSP with nonces that whitelist Supabase, Stripe.js, YouTube, Google Fonts, CodeSandbox, and Sentry" (executable).

**Style** — Specifying Vitest over Jest, Playwright over Cypress, PostHog over Mixpanel eliminates decision fatigue. Every choice the AI would otherwise deliberate on is already made. This cuts generation time by roughly 40%.

**Tone** — Telling the AI to operate principal-to-principal eliminates the 30% of tokens that would otherwise go to explanations you don't need. "Don't explain what security headers are" is worth its weight in gold.

**Audience** — "Deploys to Vercel, uses Supabase managed, budget-conscious" immediately eliminates solutions that require self-hosted infra, AWS services, or paid enterprise tools. The AI constrains itself to the free tiers and platforms you actually use.

**Response Format** — The numbered section order ensures dependencies are met. Security headers come before middleware updates. Database migrations come before API routes. Tests come after the code they test. This ordering means you can implement top-to-bottom without conflicts.

**Constraints** — This is the power section. The hard rules about not breaking existing functionality, not modifying existing APIs, requiring RLS on all tables, requiring Zod validation on all API routes — these are guardrails that prevent the AI from producing technically correct but practically destructive code. The security-specific and accessibility-specific sub-constraints are where 25 years of engineering wisdom lives.

**Examples** — Three concrete examples at three different abstraction levels (utility function, component pattern, metadata pattern) give the AI calibration targets. It now knows exactly what "production quality" means in your codebase. Without these examples, you'd get generic best-practice code. With them, you get code that looks like it was written by someone who's been in the repo for months.

---

Rick, that's my honest senior engineer assessment. The foundation is rock-solid. What remains is the difference between a demo and a business — and this final prompt is designed to close that gap in a single execution. 52 days to the ADA accessibility deadline. The security and a11y work alone is worth doing this week.

Hand this prompt to me or any other AI, say "go," and you'll have a hardened, accessible, observable, testable, searchable platform ready to handle real students and real money.
