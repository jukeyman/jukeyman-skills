# Deployment Configs — Copy-Ready

Vercel is the default (best Next.js support). Netlify + Amplify are fallbacks. All three include the mandatory security headers.

## Vercel (recommended)

`vercel.json`:

```json
{
  "framework": "nextjs",
  "buildCommand": "next build",
  "outputDirectory": ".next",
  "regions": ["iad1", "sfo1", "cdg1"],
  "headers": [
    {
      "source": "/(.*)",
      "headers": [
        { "key": "X-Content-Type-Options", "value": "nosniff" },
        { "key": "X-Frame-Options",        "value": "DENY" },
        { "key": "X-XSS-Protection",       "value": "1; mode=block" },
        { "key": "Strict-Transport-Security", "value": "max-age=63072000; includeSubDomains; preload" },
        { "key": "Referrer-Policy",        "value": "strict-origin-when-cross-origin" },
        { "key": "Permissions-Policy",     "value": "camera=(), microphone=(), geolocation=()" }
      ]
    }
  ]
}
```

Regions cover US East, US West, Europe. Add `hnd1` (Tokyo) or `syd1` (Sydney) if the audience is APAC-heavy.

## Netlify

`netlify.toml`:

```toml
[build]
  command = "npm run build"
  publish = ".next"

[[plugins]]
  package = "@netlify/plugin-nextjs"

[build.environment]
  NODE_VERSION = "20"

[[headers]]
  for = "/*"
  [headers.values]
    X-Content-Type-Options = "nosniff"
    X-Frame-Options = "DENY"
    Strict-Transport-Security = "max-age=63072000; includeSubDomains; preload"
    Referrer-Policy = "strict-origin-when-cross-origin"
```

## AWS Amplify

`amplify.yml`:

```yaml
version: 1
frontend:
  phases:
    preBuild:
      commands:
        - npm ci
    build:
      commands:
        - npm run build
  artifacts:
    baseDirectory: .next
    files:
      - '**/*'
  cache:
    paths:
      - node_modules/**/*
customHeaders:
  - pattern: '**/*'
    headers:
      - key: X-Content-Type-Options
        value: nosniff
      - key: X-Frame-Options
        value: DENY
      - key: Strict-Transport-Security
        value: 'max-age=63072000; includeSubDomains; preload'
```

## Security header rules (all platforms)

- **HSTS** with 2-year max-age + preload — enroll domain on hstspreload.org
- **X-Frame-Options: DENY** — no framing, no clickjacking
- **X-Content-Type-Options: nosniff** — no MIME sniffing
- **Referrer-Policy** — strict-origin-when-cross-origin at minimum
- **CSP** — set per-project since it depends on which third parties you loaded; never `unsafe-inline` in production
- **Permissions-Policy** — deny camera / mic / geolocation unless the site actually uses them

## Environment variables

- `.env.example` is committed with the KEYS but no values
- `.env.local` is gitignored from the first commit — verify with `git log --all -- .env.local` returns nothing
- Production secrets go in the platform's env-var UI, never in the repo
