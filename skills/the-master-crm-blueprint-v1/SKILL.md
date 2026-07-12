---
name: the-master-crm-blueprint-v1
description: 🔥 THE MASTER CRM BLUEPRINT v1
---

# 🔥 THE MASTER CRM BLUEPRINT v1

This skill defines the autonomous behavior, system prompt, and capabilities for the agent **🔥 THE MASTER CRM BLUEPRINT v1**.

## Source Location
Originally discovered in Rick's Downloads at: `/Users/kalivibecoding/Downloads/trust site/🔥 THE MASTER CRM BLUEPRINT v1.md`

## 🧠 Master Agent Prompt & Capabilities

🔥 THE MASTER CRM BLUEPRINT v1.0
Built by RJ Business Solutions | Authored 2026-05-23 | Truth-Engine Verified

⏰ TEMPORAL CHECK: 2026-05-23 (runtime metadata) | Cutoff drift: ~4mo 🚦 RISK TIER: 🟢 GREEN (documentation only — no money, no deploys) 🎯 SCOPE: Complete CRM specification — every module, table, route, page, integration, and function you need to build a Salesforce-class system on the RJ stack.

⚡ THE NORTH STAR
A CRM is not a database with forms bolted on. It's a revenue nervous system — every signal (lead, click, call, email, payment) routes through it, every action (assign, nudge, follow-up, close) fires from it, every decision (forecast, hire, scale) is grounded in it. Build it like that, or don't build it.

The system below is what Salesforce, HubSpot, Zoho, Pipedrive, Close, Attio, and Folk all converge on — abstracted, deduped, and modernized for 2026 edge-native architecture.

📐 PART 1 — THE 18 CORE MODULES (every CRM must have these)
Every CRM in the wild is a recombination of these eighteen. Anything else is a feature, not a module.

1. Identity & Access — auth, RBAC, territories, teams, SSO, MFA, audit log 2. Contacts — people (B2C primary entity, B2B secondary) 3. Accounts / Companies — organizations (B2B primary entity) 4. Leads — unqualified inbound, pre-conversion holding tank 5. Deals / Opportunities — revenue-bearing records, pipeline citizens 6. Pipelines & Stages — workflow state machines for deals 7. Activities — calls, emails, meetings, tasks, notes (the timeline fuel) 8. Products & Pricebooks — SKUs, line items, discounts, currencies 9. Quotes, Orders, Invoices — CPQ + billing handshake 10. Campaigns & Marketing — segments, sequences, attribution 11. Cases / Tickets / Service — post-sale support 12. Knowledge Base — articles, macros, internal wiki 13. Documents & Files — storage, e-sign, version control 14. Automations & Workflows — triggers, conditions, actions, sequences 15. Reports & Analytics — dashboards, forecasts, KPIs 16. Integrations — API, webhooks, marketplace, MCP servers 17. Communications — email, SMS, voice, chat, in-app 18. Admin & Settings — fields, layouts, validations, sandboxes, billing

🗄️ PART 2 — THE COMPLETE DATA MODEL (Postgres 17 + RLS)
Anchored to Salesforce's standard object reference [1] — battle-tested for 25+ years. Every table gets: id uuid pk, tenant_id uuid, created_at, updated_at, created_by, updated_by, deleted_at (soft delete), external_id, custom_fields jsonb.

2.1 Identity Layer
Copytenants            -- multi-tenant root
users              -- platform users (sales reps, admins)
roles              -- RBAC role definitions
permissions        -- granular permission strings (deals:read, contacts:write)
role_permissions   -- M2M
user_roles         -- M2M (with territory scope)
teams              -- groupings of users
team_members       -- M2M
territories        -- geo/segment/named-account scoping
audit_logs         -- every mutation, append-only
sessions           -- KV-backed, JWT refresh tracking
api_keys           -- per-integration tokens, scoped
2.2 People & Orgs
Copyaccounts           -- companies: name, domain, industry, size, revenue, tier, owner_id, parent_account_id
contacts           -- people: first/last, email, phone, title, account_id, owner_id, lifecycle_stage
leads              -- pre-conversion: name, email, source, status, score, owner_id, converted_at
                   -- on convert: spawns contact + (optional) account + (optional) opportunity [4]
contact_emails     -- multiple emails per contact, primary flag
contact_phones     -- multiple phones, type (mobile/work/home)
contact_addresses  -- billing, shipping, other
contact_socials    -- linkedin, twitter, github handles
relationships      -- contact-to-contact edges (referred_by, reports_to)
2.3 Revenue Layer
Copyopportunities      -- deals: name, account_id, amount, currency, close_date, stage, probability, owner_id, pipeline_id
opportunity_contacts   -- roles: decision-maker, champion, blocker
opportunity_products   -- line items
opportunity_competitors
opportunity_history    -- stage transitions, amount changes (audit)
pipelines          -- named pipelines (Sales, Renewal, Partner, etc.)
pipeline_stages    -- stage_name, position, probability_default, win/loss flag
products           -- SKU, name, family, description, active
pricebooks         -- named price lists (Standard, Enterprise, Reseller)
pricebook_entries  -- product × pricebook × currency × price
quotes             -- name, opp_id, status, expires_at, total
quote_line_items   -- product, qty, unit_price, discount
orders             -- placed_at, status, total
invoices           -- billing handshake, stripe_invoice_id
payments           -- stripe events, status
subscriptions      -- recurring revenue records
2.4 Engagement Layer
Copyactivities         -- polymorphic: type (call/email/meeting/task/note), subject, body, due_at, completed_at, owner_id, related_to_type, related_to_id
emails             -- thread_id, message_id, from, to[], cc[], bcc[], subject, html, plain, opened_at, clicked_at
email_templates    -- named templates, merge tags, ab_variant
email_sequences    -- multi-step drip cadences [5]
sequence_steps     -- step_number, delay_days, template_id, exit_conditions
sequence_enrollments  -- contact_id, sequence_id, current_step, status
calls              -- duration, recording_url, transcript, sentiment, direction (in/out)
meetings           -- start, end, attendees[], location, video_url, agenda, notes
tasks              -- title, due_date, priority, status, assignee_id
notes              -- markdown body, pinned, mentions[]
timeline_events    -- denormalized feed of all activity per record
2.5 Service Layer
Copycases              -- subject, description, status, priority, type, account_id, contact_id, owner_id, sla_id
case_comments      -- threaded
case_attachments
slas               -- name, first_response_minutes, resolution_minutes
sla_events         -- breach tracking
knowledge_articles -- title, body, category, status (draft/published), helpful_count
macros             -- canned actions agents apply with one click
2.6 Marketing Layer
Copycampaigns          -- name, type (email/event/ads), status, budget, actual_cost
campaign_members   -- contact/lead × campaign × status (sent/responded/converted)
segments           -- saved filter definitions, dynamic vs static
forms              -- web-to-lead, embedded form definitions
form_submissions
landing_pages      -- if you bundle the funnel layer
utm_attribution    -- first_touch, last_touch, multi_touch
2.7 Files & Docs
Copyfiles              -- name, mime, size, r2_key, virus_scanned, related_to
folders            -- nested via parent_id
documents          -- contracts, proposals, generated PDFs
document_versions  -- immutable history
signatures         -- e-sign envelopes, status, signed_at
templates          -- proposal/contract templates with mergefields
2.8 Automation Layer
Copyworkflows          -- name, trigger_type, status (active/paused), version
workflow_triggers  -- record_created, record_updated, field_changed, time_based, webhook
workflow_conditions   -- if-branches with operators
workflow_actions   -- update_field, send_email, create_task, call_webhook, run_ai
workflow_runs      -- execution log: started, finished, status, error
approvals          -- multi-step approval chains for deals/quotes
approval_steps
2.9 Analytics Layer
Copyreports            -- definition: object, filters, groupings, columns, chart_type
report_runs        -- materialized snapshots
dashboards         -- collection of reports + layout
dashboard_widgets  -- KPI cards, charts, tables
forecasts          -- period, owner_id, committed, best_case, pipeline, closed
forecast_history   -- changes over time
goals              -- quota: user_id, period, target, type (revenue/count)
2.10 Integration Layer
Copyintegrations       -- installed apps: name, status, config (encrypted), tenant_id
webhooks           -- url, events[], secret, retry_policy
webhook_deliveries -- attempt log
oauth_tokens       -- per-user-per-app refresh tokens
mcp_servers        -- registered MCP endpoints
event_bus          -- internal pub/sub log
🌐 PART 3 — THE COMPLETE FRONT-END (every page, every tab)
3.1 Global Shell
Top nav: global search (cmd+K), create-new menu, notifications, settings, profile/avatar, tenant switcher
Left sidebar: module nav with badge counts, favorites, recently viewed (last 10)
Right rail (contextual): activity feed, AI assistant, related records
Footer: sync status, version, support, RJ branding
3.2 Page Inventory (every URL in the app)
Auth & Onboarding /login /register /forgot-password /reset-password/[token] /verify-email/[token] /mfa-setup /sso/[provider]/callback /onboarding/welcome /onboarding/import /onboarding/invite-team

Home & Dashboard / (home: my-day view) — today's tasks, hot deals, recent activity, AI brief /dashboards (list) /dashboards/[id] (view) /dashboards/[id]/edit /dashboards/new

Contacts /contacts (list + filters + saved views + bulk actions) /contacts/new /contacts/[id] (record view with tabs)

Tab: Overview — vitals, owner, lifecycle stage, score
Tab: Activity — timeline of calls/emails/meetings/notes
Tab: Emails — thread view
Tab: Deals — related opportunities
Tab: Cases — support history
Tab: Files — attachments
Tab: Campaigns — enrollment history
Tab: Related — contacts at same account, referrals
Tab: Audit — who changed what when /contacts/import (CSV mapper) /contacts/export /contacts/merge (duplicate resolution)
Accounts (mirror contacts structure) /accounts /accounts/[id] with tabs: Overview, Contacts, Deals, Activity, Cases, Files, Hierarchy (parent/child), Notes

Leads /leads /leads/[id] /leads/[id]/convert (the conversion modal → spawns contact + account + opportunity) [4]

Pipeline & Deals /deals (toggleable: list / kanban / forecast / calendar) /deals/kanban — drag-drop stages [3] /deals/[id] with tabs: Overview, Activity, Products/Line Items, Quotes, Contacts (roles), Competitors, Files, Stage History /deals/[id]/quote/new /pipelines (manage pipeline definitions) /pipelines/[id]/stages (CRUD stages)

Activities /calendar — week/month/day, all activities /tasks — my tasks, team tasks, overdue /calls — call log, click-to-dial, recordings /emails — unified inbox, sent, drafts /meetings — upcoming, past, scheduler link

Marketing /campaigns /campaigns/[id] (overview, members, performance) /sequences /sequences/[id] (steps editor, enrollments, analytics) /templates/email /templates/email/[id] (visual editor) /segments /segments/[id] (filter builder + preview) /forms /forms/[id] (form builder + embed code) /landing-pages (if bundled)

Service /cases /cases/[id] (ticket detail with SLA timer) /knowledge /knowledge/[id] /knowledge/new /macros

Products & Billing /products /products/[id] /pricebooks /pricebooks/[id] /quotes /quotes/[id]/pdf (rendered PDF view) /orders /invoices /subscriptions

Reports /reports (list) /reports/new (drag-drop builder) /reports/[id] (run view) /forecasts (rollup forecast view) [analytics layer]

Automations /workflows /workflows/[id]/edit (visual builder: triggers → conditions → actions) /workflows/[id]/runs (execution history) /approvals /approvals/[id]

Documents /files (drive view, folders, search) /documents/[id] /signatures /signatures/[id]/sign/[token]

Integrations /integrations (marketplace + installed) /integrations/[slug]/configure /webhooks /webhooks/[id] /api-keys /mcp-servers

Admin / Settings /settings/profile /settings/notifications /settings/security (MFA, sessions, API keys) /settings/team (users, roles, invitations) /settings/roles (RBAC matrix editor) [6] /settings/territories /settings/objects/[name]/fields (custom fields) /settings/objects/[name]/layouts (page layout editor) /settings/objects/[name]/validations (rules) /settings/pipelines /settings/automations /settings/email (sending domain, DKIM, SPF, bounce handling) /settings/telephony (numbers, IVR, routing) /settings/billing (your CRM's own Stripe portal) /settings/audit-log /settings/data (import, export, dedupe, mass-delete, sandbox) /settings/compliance (GDPR DSAR portal, retention, consent log)

3.3 Universal UX Patterns (every list page gets these)
Saved views per user, bulk-edit, bulk-delete with undo, inline edit, column chooser, CSV/Excel export, infinite scroll or paginated, sticky filter bar, server-side sort, side-peek detail (no full nav), keyboard shortcuts (j/k navigate, e edit, / search), command palette (cmd+K), optimistic UI with rollback, skeleton loaders, empty states with CTA, error boundaries.

3.4 The 8 Critical Detail-Record Components
Header (name, owner, key metric, action menu), tabs, activity timeline, related-records sidebar, AI summary card, next-best-action card, recent files, presence indicators (who else is viewing).

⚙️ PART 4 — THE BACKEND (Workers + Hono + FastAPI)
4.1 API Surface (REST + tRPC, OpenAPI 3.1 spec)
Auth /auth/register /auth/login /auth/logout /auth/refresh /auth/mfa/enroll /auth/mfa/verify /auth/sso/[provider] /auth/password-reset

Generic CRUD pattern (apply to every object): GET /api/v1/{object} (list with filter/sort/page), POST /api/v1/{object}, GET /api/v1/{object}/{id}, PATCH /api/v1/{object}/{id}, DELETE /api/v1/{object}/{id}, POST /api/v1/{object}/bulk, POST /api/v1/{object}/search, GET /api/v1/{object}/{id}/history

Specialty endpoints: POST /leads/{id}/convert, POST /deals/{id}/transition, POST /quotes/{id}/send, POST /workflows/{id}/run, POST /emails/send, POST /calls/dial, POST /sms/send, GET /reports/{id}/run, POST /forecasts/lock, POST /import/jobs, POST /export/jobs, POST /merge, GET /search?q= (cross-object), GET /me, POST /files/upload-url (presigned R2)

4.2 Background Job Queues (Cloudflare Queues / Celery)
Email send, sequence step dispatcher, sequence step executor, webhook delivery, webhook retry, import processor, export generator, report materializer, forecast roller, lead scorer, dedupe scanner, cleanup soft-deletes, sla-breach checker, calendar sync, email IMAP fetcher, AI summary generator, embedding indexer.

4.3 Real-Time Layer
Cloudflare Durable Objects per active record for collaborative editing presence, WebSocket channels for notifications, server-sent events for live dashboards.

🤖 PART 5 — AI LAYER (the 2026 differentiator) [feature]
Lead scoring (predictive, ML model trained on historic conversions) [feature 2] Next-best-action suggestions per record AI email drafting with tone/intent controls Call transcription + sentiment + summary (Whisper + Claude) [feature 7] Meeting recap auto-generated, action items extracted Deal-health diagnostics ("stalled 14 days, no champion email, risk: high") Auto-enrichment (domain → company data via Clearbit-class) Duplicate detection (vector similarity on contacts) Forecast assist (anomaly detection on pipeline) Search (semantic over all CRM data via Vectorize) Agent skills exposed via MCP for external orchestration Auto-categorization of cases/leads via embeddings Smart compose in every text field

🔌 PART 6 — INTEGRATIONS (the must-haves)
Email: Gmail OAuth, Outlook OAuth, IMAP/SMTP fallback, SendGrid/Resend for transactional Calendar: Google, Microsoft, CalDAV Telephony: Twilio (voice, SMS, WhatsApp), Aircall, RingCentral [feature 8] Payments: Stripe (subs, invoices, payment links), QuickBooks/Xero E-signature: DocuSign, native via PDF + audit trail [feature 9] Storage: R2 native, Google Drive, Dropbox, OneDrive Chat: Slack, Microsoft Teams (notifications, slash commands) [feature 4] Video: Zoom, Google Meet, Teams (auto-join + record) Marketing: Mailchimp, Klaviyo, ActiveCampaign Ads: Google Ads, Meta Ads, LinkedIn Ads (lead-form sync) Analytics: GA4, Segment, Mixpanel, PostHog Enrichment: Clearbit, Apollo, ZoomInfo Helpdesk: Zendesk, Intercom Webhooks: inbound + outbound with HMAC, retries (exp backoff), dead-letter queue Zapier/Make/n8n: hosted recipes MCP servers: every integration exposed as a tool

📱 PART 7 — MOBILE APP (Expo SDK 52+) [feature 10]
Offline-first SQLite cache with conflict resolution, biometric login (FaceID/Touch), push notifications for assignments/mentions/replies, business card scanner (OCR → contact), click-to-call/SMS/email, voice notes auto-transcribed, geo-tagged check-ins (field sales), map view of accounts, badge counts on app icon, deep links from email/Slack into records, share extension (forward email → log activity).

🔐 PART 8 — SECURITY & COMPLIANCE
Auth: RS256 JWT (15m access / 7d refresh), argon2id passwords, MFA TOTP, SSO SAML/OIDC, IP allowlists per tenant. RBAC: role-based with row-level Postgres RLS, territory scoping, field-level security, sharing rules [tier 6]. Object-level → record-level → field-level → action-level. Encryption: TLS 1.3 transit, AES-256 at rest, secrets in Cloudflare/Vault, field-level encryption for SSN/PCI fields. Audit: immutable append-only log of every mutation, every login, every export, every permission change. Compliance: GDPR (DSAR portal, right-to-erasure, consent log, lawful basis tagging), CCPA (opt-out, data sale flag), SOC 2 Type II (CC1-CC9 controls), HIPAA (BAA + PHI tagging if healthcare), CAN-SPAM/CASL (unsub on every email, sender ID) [tier 11]. Data retention: per-object policies, auto-purge schedules, legal hold flags. Pen-test cadence: quarterly + on major release.

📊 PART 9 — REPORTING & ANALYTICS [tier 12]
Standard reports (ship 30+ out of the box): pipeline by stage, deals closing this month, win rate by source, avg sales cycle, rep leaderboard, activity per rep, conversion funnel, lead source ROI, account penetration, churn by cohort, NPS by segment, ticket volume by category, MRR/ARR, expansion vs new, CAC payback.

Custom report builder: drag-drop fields, filters (and/or nested), groupings (up to 4 levels), aggregations (sum/avg/min/max/count/distinct), 12 chart types, schedule + email delivery, embed in dashboard.

Forecasting: weighted pipeline, commit/best-case/worst-case, rep rollups → manager rollups → org, forecast lock per period, vs-quota tracking, AI-suggested forecast adjustment with reasoning.

KPIs every CRM tracks: pipeline coverage, deal velocity, win rate, avg deal size, time-in-stage, slip rate, activity per opp, response time, source attribution, lifetime value, customer health score.

🛠️ PART 10 — ADMIN POWER (the platform layer)
Field builder — text, number, currency, date, picklist, multi-picklist, lookup, formula, rollup-summary, geolocation, encrypted text, file. Page layout editor — drag-drop, conditional visibility per profile. Validation rules — Zod-like expressions, error messages, severity. Workflow builder — visual canvas: trigger → conditions → actions, branching, loops, wait steps, human-approval steps. Approval processes — multi-step, parallel, escalations, recall. Sandbox environments — full, partial, dev (copy from prod). Data tools — import wizard (CSV/Excel mapper, dedupe-on-import), export, mass-update, mass-transfer-owner, mass-delete with undo, dedupe scanner. Sharing model — org defaults, role hierarchy, sharing rules, manual share. API tools — key management, scopes, rate-limit display, logs. Audit & monitoring — login history, setup audit trail, API call log, integration health. Billing & licensing — seat management, plan upgrade/downgrade portal.

🏗️ PART 11 — RECOMMENDED RJ STACK MAPPING
Frontend: Next.js 16.2 App Router · TypeScript 5.8 strict · Tailwind 4.2.4 · shadcn/ui · Zustand 5 · TanStack Query 5 · React Hook Form + Zod · Motion 12 · next-themes Backend (edge): Cloudflare Workers · Hono 4.12+ · Durable Objects (per-record presence + workflow state) · KV (sessions, cache, rate-limit) · Queues (jobs) · R2 (files) Backend (AI): FastAPI 0.136+ on Python 3.13 · Celery + Upstash Redis · SQLAlchemy 2 async Database: Supabase Postgres 17 + RLS · D1 for edge reads · Vectorize for semantic search Auth: Supabase Auth + NextAuth v5 · argon2id · Turnstile · TOTP AI: Cloudflare AI Gateway · Workers AI (Llama 3.3 70B fp8-fast) · Claude Opus orchestrator · Claude Sonnet workers · CrewAI 1.14+ · LangGraph · MCP for tools Payments: Stripe (subs + usage-based for AI features) Infra: Cloudflare Pages + Workers · Terraform · Wrangler · GitHub Actions · Sentry Mobile: Expo SDK 52+ with shared types package

📋 PART 12 — THE 12 DOCS THIS BUILD NEEDS
Vision Statement · Business Case · PRD · System Architecture · ERD · OpenAPI 3.1 Spec · ADRs · Design System · Test Plan · Deployment Guide · Runbook · README+CHANGELOG+SECURITY+CONTEXT.md+AUTORESEARCH-MANIFEST.md+data-flows.yaml. 
