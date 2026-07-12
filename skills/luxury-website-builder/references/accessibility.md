# Accessibility — WCAG 2.2 Checklist

**Target: AA minimum, AAA where feasible.** Every site passes this checklist before it ships. `eslint-plugin-jsx-a11y` set to `error` for every rule. `axe-core` runs in Playwright on every page.

## Perceivable

- [ ] Text alternatives on all meaningful images (`alt`); decorative images use `alt=""`
- [ ] Captions on all video content
- [ ] Color contrast ≥ 4.5:1 for body text, ≥ 3:1 for large text and UI components
- [ ] Text resizable up to 200% without loss of content
- [ ] Content reflows cleanly at 320px viewport width

## Operable

- [ ] Full keyboard navigation on every interactive element
- [ ] Skip-to-content link on every page
- [ ] Focus indicators visible and never obscured (WCAG 2.2 — 2.4.11 minimum, 2.4.12 enhanced)
- [ ] Enhanced focus appearance (2.4.13) — indicators clearly perceivable
- [ ] No keyboard traps
- [ ] Sufficient time for time-dependent interactions
- [ ] Reduced-motion option honored (`prefers-reduced-motion`)
- [ ] Drag interactions have keyboard/click alternatives (2.5.7)
- [ ] Target size ≥ 24×24 CSS pixels for all interactive elements (2.5.8)

## Understandable

- [ ] Consistent navigation across pages
- [ ] Errors identified with clear suggestions
- [ ] Labels + instructions on every input (never placeholder-only)
- [ ] Predictable functionality — no surprise behavior on focus/input
- [ ] Consistent help location across pages (3.2.6)
- [ ] No redundant re-entry of information the user already provided (3.3.7)
- [ ] Accessible authentication — no cognitive-function tests like remembering a puzzle (3.3.8 / 3.3.9)

## Robust

- [ ] Valid HTML5 markup
- [ ] ARIA labels only where semantic HTML falls short — don't ARIA what a `<button>` already does
- [ ] Compatible with major assistive tech (NVDA, JAWS, VoiceOver)
- [ ] Progressive enhancement — core content works without JS

## Modals, dialogs, popovers

- [ ] Focus trap while open
- [ ] Escape key closes
- [ ] `aria-modal="true"` + role
- [ ] Focus returns to the trigger on close

## Forms

- [ ] Every input has a visible label programmatically associated
- [ ] Error messages inline, near the field, `aria-describedby` linked
- [ ] Required fields marked in both text and `aria-required`
- [ ] Submit button never disabled purely to enforce validation — show inline errors instead
