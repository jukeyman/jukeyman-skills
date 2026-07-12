# Design System — Luxury Default

Use this token set unless the user gives you a brand kit. Ship the tokens as `tailwind.config.ts` extensions AND CSS variables in `app/globals.css` (so runtime theming works).

## Color palette

### Primary — Rich Gold / Amber (main accent)
```typescript
primary: {
  50:  '#FFFBEB',
  100: '#FEF3C7',
  200: '#FDE68A',
  300: '#FCD34D',
  400: '#FBBF24',
  500: '#F59E0B',   // main
  600: '#D97706',
  700: '#B45309',
  800: '#92400E',
  900: '#78350F',
  950: '#451A03',
}
```

### Neutral — Sophisticated Grays
```typescript
neutral: {
  50: '#FAFAFA', 100: '#F5F5F5', 200: '#E5E5E5', 300: '#D4D4D4',
  400: '#A3A3A3', 500: '#737373', 600: '#525252', 700: '#404040',
  800: '#262626', 900: '#171717', 950: '#0A0A0A',
}
```

### Accent — Deep Navy
```typescript
accent: {
  50: '#EFF6FF', 100: '#DBEAFE', 200: '#BFDBFE', 300: '#93C5FD',
  400: '#60A5FA', 500: '#3B82F6', 600: '#2563EB', 700: '#1D4ED8',
  800: '#1E40AF', 900: '#1E3A8A', 950: '#172554',
}
```

## Typography

```typescript
fontFamily: {
  display: ['Playfair Display', 'Georgia', 'serif'],   // headlines
  sans:    ['Inter', 'system-ui', 'sans-serif'],       // body
  mono:    ['JetBrains Mono', 'Consolas', 'monospace'] // code
}

fontSize: {
  'display-2xl': ['4.5rem',   { lineHeight: '1.1', letterSpacing: '-0.02em' }],
  'display-xl':  ['3.75rem',  { lineHeight: '1.1', letterSpacing: '-0.02em' }],
  'display-lg':  ['3rem',     { lineHeight: '1.2', letterSpacing: '-0.01em' }],
  'display-md':  ['2.25rem',  { lineHeight: '1.2', letterSpacing: '-0.01em' }],
  'display-sm':  ['1.875rem', { lineHeight: '1.3' }],
  'body-xl':     ['1.25rem',  { lineHeight: '1.75' }],
  'body-lg':     ['1.125rem', { lineHeight: '1.75' }],
  'body-md':     ['1rem',     { lineHeight: '1.75' }],
  'body-sm':     ['0.875rem', { lineHeight: '1.5' }],
}
```

Load fonts via `next/font/google` — never external `<link>` tags. Preload display + sans; lazy-load mono.

## Signature effect — Glassmorphism 3.0

Use for hero overlays, floating cards, nav on scroll, modal chrome. Don't spam it — 2–3 glass surfaces per page max.

```css
.glass-morphism-3 {
  background: linear-gradient(
    135deg,
    rgba(255, 255, 255, 0.10) 0%,
    rgba(255, 255, 255, 0.05) 50%,
    rgba(255, 255, 255, 0.10) 100%
  );
  backdrop-filter: blur(20px) saturate(180%);
  -webkit-backdrop-filter: blur(20px) saturate(180%);
  border: 1px solid rgba(255, 255, 255, 0.18);
  box-shadow:
    0 8px 32px rgba(0, 0, 0, 0.12),
    inset 0 0 0 1px rgba(255, 255, 255, 0.10);
  border-radius: 24px;
}
```

## Additional design patterns to reach for

- **Bento grid layouts** — asymmetric compositions, CSS Grid + subgrid, dynamic card sizing
- **Kinetic typography** — GSAP SplitText, scroll-triggered reveals, character-by-character, variable-font animations
- **3D & spatial** — CSS 3D transforms, perspective/depth, parallax layers, optional React Three Fiber for hero backgrounds
- **Micro-interactions** — hover transforms, click feedback, progress indicators, form-field affordances

## Spacing / radii / shadow scales

Stay on the Tailwind default 4px scale unless the brand demands otherwise. Radii: `sm 8px · md 12px · lg 16px · xl 24px · 2xl 32px`. Shadows: use the glass-morphism shadow above for glass surfaces; standard `shadow-lg` / `shadow-2xl` elsewhere.

## Dark mode

Wire `next-themes` from the start. Test both palettes side-by-side — a luxury site without a functioning dark mode reads as 2019.
