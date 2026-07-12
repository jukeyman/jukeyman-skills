---
name: twilio-omni-agent-build-call-center-for-credit-repair-co-2026-05-04
description: twilio-omni-agent-build-call-center-for-credit-repair-co-2026-05-04
---

# twilio-omni-agent-build-call-center-for-credit-repair-co-2026-05-04

This skill defines the autonomous behavior, system prompt, and capabilities for the agent **twilio-omni-agent-build-call-center-for-credit-repair-co-2026-05-04**.

## Source Location
Originally discovered in Rick's Downloads at: `/Users/kalivibecoding/Downloads/twilio-omni-agent-build-call-center-for-credit-repair-co-2026-05-04.md`

## 🧠 Master Agent Prompt & Capabilities

# /build-call-center  for credit repair co...

**Model:** Claude Sonnet 4  
**Date:** 2026-05-04  
**Provider:** Anthropic  

---

## You

/build-call-center  for credit repair company 

---

## Omni-Agent

# Complete Call Center Build — Credit Repair Company
### RJ Business Solutions | Twilio Omni-Agent v3.0

---

## DISCOVERY & ARCHITECTURE OVERVIEW

**Use Case:** Inbound/Outbound call center for a credit repair company  
**Features:**
- Multi-level IVR (new clients, existing clients, billing, disputes)
- Call queuing with position announcements
- Agent routing with skills-based distribution
- Call recording with consent disclosure (mandatory for credit services)
- Voicemail with transcription
- Outbound campaign dialer (appointment reminders, follow-ups)
- Supervisor dashboard (live monitoring, whisper coaching, barge-in)
- AMD (Answering Machine Detection) for outbound
- 10DLC SMS integration (appointment confirmations, status updates)
- Webhook status pipeline + observability

**Stack:** Node.js (Express) + React dashboard + PostgreSQL + Redis

---

## PROJECT STRUCTURE

```
credit-repair-call-center/
├── server/
│   ├── src/
│   │   ├── index.ts                    # Express app entry
│   │   ├── config.ts                   # Env + Twilio client
│   │   ├── middleware/
│   │   │   ├── twilioSignature.ts      # Webhook signature validation
│   │   │   ├── rateLimiter.ts          # Rate limiting
│   │   │   └── logger.ts              # Structured logging
│   │   ├── routes/
│   │   │   ├── voice/
│   │   │   │   ├── inbound.ts          # Main IVR entry
│   │   │   │   ├── ivr.ts              # IVR menu handlers
│   │   │   │   ├── queue.ts            # Queue management
│   │   │   │   ├── voicemail.ts        # Voicemail flow
│   │   │   │   ├── transfer.ts         # Agent transfer
│   │   │   │   ├── recording.ts        # Recording callbacks
│   │   │   │   └── status.ts          # Call status callbacks
│   │   │   ├── outbound/
│   │   │   │   ├── dialer.ts           # Outbound campaign dialer
│   │   │   │   ├── amd.ts             # AMD callback handler
│   │   │   │   └── reminder.ts        # Appointment reminders
│   │   │   ├── conference/
│   │   │   │   ├── bridge.ts          # Conference creation
│   │   │   │   ├── moderator.ts       # Supervisor controls
│   │   │   │   └── callback.ts        # Conference events
│   │   │   ├── token/
│   │   │   │   └── accessToken.ts     # Agent browser token minting
│   │   │   ├── sms/
│   │   │   │   ├── inbound.ts         # SMS inbound handler
│   │   │   │   └── outbound.ts        # SMS send + campaigns
│   │   │   ├── dashboard/
│   │   │   │   ├── calls.ts           # Live call data API
│   │   │   │   ├── agents.ts          # Agent status API
│   │   │   │   └── reports.ts         # Historical reports
│   │   │   └── health.ts              # Health check
│   │   ├── services/
│   │   │   ├── twilioClient.ts        # Twilio REST wrapper
│   │   │   ├── queueService.ts        # Redis queue state
│   │   │   ├── agentService.ts        # Agent availability
│   │   │   ├── crmService.ts          # CRM lookup
│   │   │   ├── recordingService.ts    # Recording management
│   │   │   └── smsService.ts         # SMS service layer
│   │   ├── db/
│   │   │   ├── client.ts              # Postgres connection
│   │   │   ├── migrations/
│   │   │   │   └── 001_initial.sql    # Database schema
│   │   │   └── queries/
│   │   │       ├── calls.ts
│   │   │       ├── agents.ts
│   │   │       └── campaigns.ts
│   │   └── utils/
│   │       ├── businessHours.ts       # Hours + holiday logic
│   │       ├── phoneUtils.ts          # E.164 validation
│   │       └── idempotency.ts        # Duplicate webhook guard
├── dashboard/
│   ├── src/
│   │   ├── App.tsx
│   │   ├── pages/
│   │   │   ├── LiveQueue.tsx          # Real-time queue monitor
│   │   │   ├── AgentPanel.tsx         # Agent softphone UI
│   │   │   ├── SupervisorView.tsx     # Supervisor controls
│   │   │   ├── Reports.tsx            # Historical analytics
│   │   │   └── Campaigns.tsx          # Outbound campaign manager
│   │   ├── components/
│   │   │   ├── CallCard.tsx
│   │   │   ├── AgentStatus.tsx
│   │   │   ├── QueueMetrics.tsx
│   │   │   └── SoftPhone.tsx          # Browser dial pad
│   │   └── hooks/
│   │       ├── useTwilioDevice.ts     # Voice SDK device
│   │       └── useSocket.ts           # WebSocket live updates
├── scripts/
│   └── provision.sh                   # Twilio CLI setup
├── .env.example
├── package.json
├── tsconfig.json
└── README.md
```

---

## ARCHITECTURE DIAGRAM

```mermaid
graph TD
    PSTN[PSTN Caller] --> TN[Twilio Phone Number]
    TN --> IVR[Inbound IVR Handler\n/voice/inbound]

    IVR --> |Press 1 - New Client| Q_NEW[Queue: new-client]
    IVR --> |Press 2 - Existing Client| LOOKUP[CRM Lookup\nby CallerID]
    IVR --> |Press 3 - Billing| Q_BILL[Queue: billing]
    IVR --> |Press 4 - Disputes| Q_DISP[Queue: disputes]
    IVR --> |No Answer / After Hours| VM[Voicemail Flow]

    LOOKUP --> |Found| Q_EXIST[Queue: existing-client\nwith context]
    LOOKUP --> |Not Found| Q_NEW

    Q_NEW --> AGENT[Available Agent\nBrowser Softphone]
    Q_EXIST --> AGENT
    Q_BILL --> AGENT
    Q_DISP --> AGENT

    AGENT --> CONF[Conference Bridge\nSupervisor-Ready]
    CONF --> |Supervisor Joins| SUP[Supervisor\nWhisper / Barge]

    AGENT --> TRANSFER[Blind/Warm Transfer]
    AGENT --> REC[Recording +\nConsent Disclosure]

    OB[Outbound Dialer] --> AMD[AMD Detection]
    AMD --> |Human| AGENT
    AMD --> |Machine| VM_MSG[Leave Voicemail Message]

    IVR --> SMS[SMS Confirmation\n10DLC Registered]
    AGENT --> SMS

    subgraph Dashboard
        LQ[Live Queue Monitor]
        AP[Agent Panel + Softphone]
        SV[Supervisor View]
        RPT[Reports]
    end

    CONF --> Dashboard
    Q_NEW --> Dashboard
```

---

## 1. PACKAGE.JSON

```json
// filename: package.json
{
  "name": "credit-repair-call-center",
  "version": "1.0.0",
  "description": "Full-featured call center for credit repair - RJ Business Solutions",
  "private": true,
  "workspaces": ["server", "dashboard"],
  "scripts": {
    "dev": "concurrently \"npm run dev --workspace=server\" \"npm run dev --workspace=dashboard\"",
    "build": "npm run build --workspace=server && npm run build --workspace=dashboard",
    "provision": "bash scripts/provision.sh"
  },
  "devDependencies": {
    "concurrently": "9.1.2"
  }
}
```

```json
// filename: server/package.json
{
  "name": "credit-repair-server",
  "version": "1.0.0",
  "scripts": {
    "dev": "tsx watch src/index.ts",
    "build": "tsc",
    "start": "node dist/index.js",
    "db:migrate": "psql $DATABASE_URL -f src/db/migrations/001_initial.sql"
  },
  "dependencies": {
    "twilio": "5.4.0",
    "express": "4.21.2",
    "express-rate-limit": "7.5.0",
    "ioredis": "5.4.1",
    "pg": "8.13.3",
    "jsonwebtoken": "9.0.2",
    "dotenv": "16.4.7",
    "winston": "3.17.0",
    "cors": "2.8.5",
    "helmet": "8.0.0",
    "uuid": "11.1.0",
    "date-fns": "4.1.0",
    "socket.io": "4.8.1",
    "zod": "3.23.8"
  },
  "devDependencies": {
    "@types/express": "5.0.0",
    "@types/pg": "8.11.11",
    "@types/cors": "2.8.17",
    "@types/node": "22.13.10",
    "@types/jsonwebtoken": "9.0.9",
    "@types/uuid": "10.0.0",
    "tsx": "4.19.3",
    "typescript": "5.7.3"
  }
}
```

```json
// filename: dashboard/package.json
{
  "name": "credit-repair-dashboard",
  "version": "1.0.0",
  "scripts": {
    "dev": "vite",
    "build": "tsc && vite build",
    "preview": "vite preview"
  },
  "dependencies": {
    "@twilio/voice-sdk": "2.18.0",
    "react": "19.0.0",
    "react-dom": "19.0.0",
    "react-router-dom": "7.2.0",
    "socket.io-client": "4.8.1",
    "axios": "1.8.4",
    "zustand": "5.0.3",
    "@tanstack/react-query": "5.67.3",
    "lucide-react": "0.475.0",
    "date-fns": "4.1.0",
    "clsx": "2.1.1",
    "recharts": "2.15.1"
  },
  "devDependencies": {
    "@types/react": "19.0.10",
    "@types/react-dom": "19.0.4",
    "@vitejs/plugin-react": "4.3.4",
    "typescript": "5.7.3",
    "vite": "6.2.0",
    "tailwindcss": "4.0.0",
    "autoprefixer": "10.4.20"
  }
}
```

---

## 2. ENVIRONMENT TEMPLATE

```bash
# filename: .env.example

# ─── Twilio Core ───────────────────────────────────────────────────────────
TWILIO_ACCOUNT_SID=ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
TWILIO_API_KEY_SID=SKxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
TWILIO_API_KEY_SECRET=your_api_key_secret_here

# ─── Twilio Resources ──────────────────────────────────────────────────────
TWILIO_TWIML_APP_SID=APxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
TWILIO_MAIN_PHONE_NUMBER=+15051234567
TWILIO_MESSAGING_SERVICE_SID=MGxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# ─── Queue Names (match exactly in TwiML) ─────────────────────────────────
QUEUE_NEW_CLIENT=new-client
QUEUE_EXISTING_CLIENT=existing-client
QUEUE_BILLING=billing
QUEUE_DISPUTES=disputes

# ─── Business Hours (Mountain Time) ───────────────────────────────────────
BUSINESS_HOURS_START=08:00
BUSINESS_HOURS_END=18:00
BUSINESS_TIMEZONE=America/Denver
BUSINESS_PHONE=5051234567

# ─── Server ────────────────────────────────────────────────────────────────
SERVER_URL=https://your-domain.com
PORT=3001
NODE_ENV=production
JWT_SECRET=replace_with_strong_random_secret_64_chars

# ─── Database ──────────────────────────────────────────────────────────────
DATABASE_URL=postgresql://user:password@localhost:5432/creditrepair_cc
REDIS_URL=redis://localhost:6379

# ─── Compliance ────────────────────────────────────────────────────────────
RECORDING_ENABLED=true
RECORDING_CONSENT_REQUIRED=true
RECORDING_ENCRYPTION_KEY=your_recording_encryption_key

# ─── Notifications ─────────────────────────────────────────────────────────
SLACK_WEBHOOK_URL=https://hooks.slack.com/services/xxx/yyy/zzz
SUPERVISOR_EMAIL=supervisor@yourcompany.com
ALERT_EMAIL=alerts@yourcompany.com

# ─── Optional: CRM ─────────────────────────────────────────────────────────
CRM_API_URL=https://your-crm.com/api
CRM_API_KEY=your_crm_api_key
```

---

## 3. SERVER CONFIGURATION

```typescript
// filename: server/src/config.ts
import twilio from 'twilio';
import dotenv from 'dotenv';
dotenv.config();

function requireEnv(key: string): string {
  const val = process.env[key];
  if (!val) throw new Error(`Missing required env var: ${key}`);
  return val;
}

export const config = {
  twilio: {
    accountSid: requireEnv('TWILIO_ACCOUNT_SID'),
    apiKeySid: requireEnv('TWILIO_API_KEY_SID'),
    apiKeySecret: requireEnv('TWILIO_API_KEY_SECRET'),
    twimlAppSid: requireEnv('TWILIO_TWIML_APP_SID'),
    mainPhoneNumber: requireEnv('TWILIO_MAIN_PHONE_NUMBER'),
    messagingServiceSid: requireEnv('TWILIO_MESSAGING_SERVICE_SID'),
  },
  queues: {
    newClient: process.env.QUEUE_NEW_CLIENT || 'new-client',
    existingClient: process.env.QUEUE_EXISTING_CLIENT || 'existing-client',
    billing: process.env.QUEUE_BILLING || 'billing',
    disputes: process.env.QUEUE_DISPUTES || 'disputes',
  },
  server: {
    url: requireEnv('SERVER_URL'),
    port: parseInt(process.env.PORT || '3001', 10),
    jwtSecret: requireEnv('JWT_SECRET'),
  },
  business: {
    hoursStart: process.env.BUSINESS_HOURS_START || '08:00',
    hoursEnd: process.env.BUSINESS_HOURS_END || '18:00',
    timezone: process.env.BUSINESS_TIMEZONE || 'America/Denver',
  },
  recording: {
    enabled: process.env.RECORDING_ENABLED === 'true',
    consentRequired: process.env.RECORDING_CONSENT_REQUIRED === 'true',
  },
  slack: {
    webhookUrl: process.env.SLACK_WEBHOOK_URL,
  },
};

// Production uses API Key pair (NOT Auth Token)
// https://www.twilio.com/docs/iam/api-keys
export const twilioClient = twilio(
  config.twilio.apiKeySid,
  config.twilio.apiKeySecret,
  { accountSid: config.twilio.accountSid }
);
```

---

## 4. MIDDLEWARE

```typescript
// filename: server/src/middleware/twilioSignature.ts
import { Request, Response, NextFunction } from 'express';
import twilio from 'twilio';
import { config } from '../config';

/**
 * Validates X-Twilio-Signature on every inbound Twilio webhook.
 * https://www.twilio.com/docs/usage/webhooks/webhooks-security
 * NEVER skip this — protects against spoofed requests.
 */
export function validateTwilioSignature(
  req: Request,
  res: Response,
  next: NextFunction
): void {
  const twilioSignature = req.headers['x-twilio-signature'] as string;

  if (!twilioSignature) {
    res.status(403).json({ error: 'Missing Twilio signature' });
    return;
  }

  // Reconstruct full URL exactly as Twilio sees it
  const url = `${config.server.url}${req.originalUrl}`;

  // Auth token required for signature validation
  const authToken = process.env.TWILIO_AUTH_TOKEN;
  if (!authToken) {
    console.error('TWILIO_AUTH_TOKEN not set — cannot validate signature');
    res.status(500).json({ error: 'Server configuration error' });
    return;
  }

  const params = req.body || {};

  const isValid = twilio.validateRequest(
    authToken,
    twilioSignature,
    url,
    params
  );

  if (!isValid) {
    console.warn(`Invalid Twilio signature for ${url} from ${req.ip}`);
    res.status(403).json({ error: 'Invalid Twilio signature' });
    return;
  }

  next();
}
```

```typescript
// filename: server/src/middleware/logger.ts
import winston from 'winston';

export const logger = winston.createLogger({
  level: process.env.LOG_LEVEL || 'info',
  format: winston.format.combine(
    winston.format.timestamp(),
    winston.format.errors({ stack: true }),
    winston.format.json()
  ),
  defaultMeta: { service: 'credit-repair-call-center' },
  transports: [
    new winston.transports.Console({
      format: winston.format.combine(
        winston.format.colorize(),
        winston.format.simple()
      ),
    }),
    new winston.transports.File({ filename: 'logs/error.log', level: 'error' }),
    new winston.transports.File({ filename: 'logs/combined.log' }),
  ],
});
```

```typescript
// filename: server/src/middleware/rateLimiter.ts
import rateLimit from 'express-rate-limit';

export const webhookRateLimiter = rateLimit({
  windowMs: 60 * 1000,       // 1 minute
  max: 200,                  // max 200 Twilio webhook hits/min
  standardHeaders: true,
  legacyHeaders: false,
  skip: (req) => {
    // Only rate-limit non-Twilio IPs
    const twilioHeader = req.headers['x-twilio-signature'];
    return !!twilioHeader;    // let Twilio requests through, still validated by middleware
  },
  message: { error: 'Too many requests' },
});

export const apiRateLimiter = rateLimit({
  windowMs: 60 * 1000,
  max: 100,
  standardHeaders: true,
  legacyHeaders: false,
  message: { error: 'Rate limit exceeded' },
});
```

---

## 5. UTILITIES

```typescript
// filename: server/src/utils/businessHours.ts
import { config } from '../config';

const HOLIDAYS_2026 = [
  '2026-01-01', // New Year's Day
  '2026-05-25', // Memorial Day
  '2026-07-04', // Independence Day
  '2026-09-07', // Labor Day
  '2026-11-26', // Thanksgiving
  '2026-12-25', // Christmas
];

export function isBusinessHours(): boolean {
  const now = new Date();
  const options: Intl.DateTimeFormatOptions = {
    timeZone: config.business.timezone,
    hour: '2-digit',
    minute: '2-digit',
    hour12: false,
    weekday: 'short',
  };

  const formatter = new Intl.DateTimeFormat('en-US', options);
  const parts = formatter.formatToParts(now);
  const weekday = parts.find(p => p.type === 'weekday')?.value;
  const timeStr = `${parts.find(p => p.type === 'hour')?.value}:${parts.find(p => p.type === 'minute')?.value}`;

  // Check weekend
  if (weekday === 'Sat' || weekday === 'Sun') return false;

  // Check holiday
  const dateStr = now.toLocaleDateString('en-CA', { timeZone: config.business.timezone });
  if (HOLIDAYS_2026.includes(dateStr)) return false;

  // Check business hours
  const start = config.business.hoursStart;
  const end = config.business.hoursEnd;
  return timeStr >= start && timeStr < end;
}

export function getNextBusinessDayMessage(): string {
  return 'Our office is currently closed. Business hours are Monday through Friday, 8 AM to 6 PM Mountain Time.';
}
```

```typescript
// filename: server/src/utils/phoneUtils.ts
import { z } from 'zod';

const E164_REGEX = /^\+[1-9]\d{1,14}$/;

export function isValidE164(phone: string): boolean {
  return E164_REGEX.test(phone);
}

export function toE164(phone: string, defaultCountryCode = '1'): string {
  const digits = phone.replace(/\D/g, '');
  if (digits.length === 10) return `+${defaultCountryCode}${digits}`;
  if (digits.length === 11 && digits.startsWith('1')) return `+${digits}`;
  return `+${digits}`;
}

// Server-side allowlist — validate ALL outbound To numbers
// Never trust client-submitted To numbers without this check
const ALLOWED_COUNTRY_CODES = ['+1']; // US + Canada only

export function isAllowedDestination(phone: string): boolean {
  if (!isValidE164(phone)) return false;
  return ALLOWED_COUNTRY_CODES.some(code => phone.startsWith(code));
}

export const PhoneSchema = z.string().refine(isValidE164, {
  message: 'Must be E.164 format (e.g. +15051234567)',
});
```

```typescript
// filename: server/src/utils/idempotency.ts
import { redis } from '../db/client';

/**
 * Prevents duplicate webhook processing.
 * Twilio guarantees at-least-once delivery — always use this.
 */
export async function isProcessed(sid: string): Promise<boolean> {
  const key = `processed:${sid}`;
  const result = await redis.set(key, '1', 'NX', 'EX', 86400); // 24h TTL
  return result === null; // null = key existed = already processed
}
```

---

## 6. DATABASE

```sql
-- filename: server/src/db/migrations/001_initial.sql

-- Agents table
CREATE TABLE agents (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone E.164 VARCHAR(20),
  client_identity VARCHAR(255) UNIQUE NOT NULL, -- matches Twilio AccessToken identity
  skills TEXT[] DEFAULT '{}',
  status VARCHAR(50) DEFAULT 'offline', -- offline, available, on-call, wrap-up
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Calls table
CREATE TABLE calls (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  call_sid VARCHAR(34) UNIQUE NOT NULL,          -- CA...
  parent_call_sid VARCHAR(34),                   -- for child legs
  direction VARCHAR(20) NOT NULL,                -- inbound, outbound-api
  from_number VARCHAR(20) NOT NULL,
  to_number VARCHAR(20) NOT NULL,
  status VARCHAR(50),                            -- Twilio call status
  queue_name VARCHAR(100),
  agent_id UUID REFERENCES agents(id),
  wait_time_seconds INTEGER,
  duration_seconds INTEGER,
  recording_sid VARCHAR(34),
  recording_url TEXT,
  transcription_text TEXT,
  ivr_path TEXT[],                               -- audit trail of IVR selections
  amd_result VARCHAR(50),                        -- human, machine, fax, unknown
  created_at TIMESTAMPTZ DEFAULT NOW(),
  answered_at TIMESTAMPTZ,
  ended_at TIMESTAMPTZ
);

-- SMS messages table
CREATE TABLE sms_messages (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  message_sid VARCHAR(34) UNIQUE NOT NULL,       -- SM...
  direction VARCHAR(20) NOT NULL,
  from_number VARCHAR(20) NOT NULL,
  to_number VARCHAR(20) NOT NULL,
  body TEXT,
  status VARCHAR(50),
  media_urls TEXT[],
  created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Outbound campaigns
CREATE TABLE campaigns (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  name VARCHAR(255) NOT NULL,
  type VARCHAR(50) NOT NULL,                     -- reminder, follow-up, payment-due
  status VARCHAR(50) DEFAULT 'draft',            -- draft, active, paused, completed
  contact_list JSONB NOT NULL DEFAULT '[]',
  message_template TEXT,
  scheduled_at TIMESTAMPTZ,
  created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Queue events for analytics
CREATE TABLE queue_events (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  call_sid VARCHAR(34) NOT NULL,
  queue_name VARCHAR(100) NOT NULL,
  event_type VARCHAR(50) NOT NULL,               -- enqueued, dequeued, abandoned
  position INTEGER,
  wait_time_seconds INTEGER,
  created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Recordings audit log
CREATE TABLE recording_audit (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  recording_sid VARCHAR(34) UNIQUE NOT NULL,
  call_sid VARCHAR(34) NOT NULL,
  consent_obtained BOOLEAN NOT NULL DEFAULT FALSE,
  consent_timestamp TIMESTAMPTZ,
  status VARCHAR(50),
  duration_seconds INTEGER,
  transcription_text TEXT,
  created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Indexes
CREATE INDEX idx_calls_call_sid ON calls(call_sid);
CREATE INDEX idx_calls_from_number ON calls(from_number);
CREATE INDEX idx_calls_created_at ON calls(created_at);
CREATE INDEX idx_calls_status ON calls(status);
CREATE INDEX idx_queue_events_queue_name ON queue_events(queue_name);
CREATE INDEX idx_sms_from_number ON sms_messages(from_number);
```

```typescript
// filename: server/src/db/client.ts
import { Pool } from 'pg';
import { Redis } from 'ioredis';

export const db = new Pool({
  connectionString: process.env.DATABASE_URL,
  max: 20,
  idleTimeoutMillis: 30000,
  connectionTimeoutMillis: 2000,
});

export const redis = new Redis(process.env.REDIS_URL || 'redis://localhost:6379', {
  retryStrategy: (times) => Math.min(times * 50, 2000),
  lazyConnect: true,
});

redis.on('error', (err) => console.error('Redis error:', err));

export async function connectDb() {
  await db.connect();
  await redis.connect();
  console.log('✅ Database and Redis connected');
}
```

---

## 7. VOICE ROUTES — INBOUND IVR

```typescript
// filename: server/src/routes/voice/inbound.ts
import { Router, Request, Response } from 'express';
import twilio from 'twilio';
import { validateTwilioSignature } from '../../middleware/twilioSignature';
import { isBusinessHours, getNextBusinessDayMessage } from '../../utils/businessHours';
import { config } from '../../config';
import { db } from '../../db/client';
import { crmService } from '../../services/crmService';
import { logger } from '../../middleware/logger';

const router = Router();
const VoiceResponse = twilio.twiml.VoiceResponse;

/**
 * Main entry point for all inbound calls.
 * Twilio Phone Number Voice URL → POST /voice/inbound
 * https://www.twilio.com/docs/voice/twiml
 */
router.post('/', validateTwilioSignature, async (req: Request, res: Response) => {
  const { CallSid, From, To, Direction } = req.body;

  logger.info('Inbound call received', { CallSid, From, To, Direction });

  // Log call to database
  await db.query(
    `INSERT INTO calls (call_sid, direction, from_number, to_number, status, ivr_path)
     VALUES ($1, $2, $3, $4, 'ringing', $5)
     ON CONFLICT (call_sid) DO NOTHING`,
    [CallSid, Direction, From, To, ['entry']]
  );

  const twiml = new VoiceResponse();

  // Check business hours
  if (!isBusinessHours()) {
    twiml.say(
      { voice: 'Polly.Joanna-Neural', language: 'en-US' },
      getNextBusinessDayMessage() +
      ' Please leave a voicemail and we will return your call the next business day. ' +
      'You can also reach us online at R J Business Solutions dot org.'
    );
    twiml.redirect({ method: 'POST' }, `${config.server.url}/voice/voicemail?reason=after-hours`);
    res.type('text/xml').send(twiml.toString());
    return;
  }

  // Consent disclosure BEFORE any recording — required for credit repair (FCRA compliance)
  // https://www.twilio.com/docs/voice/twiml/record
  if (config.recording.consentRequired) {
    const gather = twiml.gather({
      numDigits: '1',
      timeout: 8,
      action: `${config.server.url}/voice/ivr/main-menu`,
      method: 'POST',
    });
    gather.say(
      { voice: 'Polly.Joanna-Neural', language: 'en-US' },
      'Thank you for calling our credit repair team. ' +
      'This call may be recorded for quality assurance and compliance purposes. ' +
      'By continuing, you consent to this recording. ' +
      'For new clients, press 1. ' +
      'For existing clients, press 2. ' +
      'For billing questions, press 3. ' +
      'For credit dispute status, press 4. ' +
      'To repeat this menu, press 9.'
    );
    // Fallback if no input
    twiml.redirect({ method: 'POST' }, `${config.server.url}/voice/ivr/main-menu`);
  }

  res.type('text/xml').send(twiml.toString());
});

export { router as inboundRouter };
```

```typescript
// filename: server/src/routes/voice/ivr.ts
import {

---

*Generated by Twilio Omni-Agent · RJ Business Solutions · 2026-05-04*

