# Animation Library — Copy-Ready Presets

Two libraries, two roles:
- **Motion (Framer Motion 11+)** — component-level: hovers, taps, page transitions, orchestrated staggers
- **GSAP 3.13+** — scroll-linked, kinetic type, SplitText, DrawSVG, ScrollSmoother

Ship at least: scroll-reveal on primary sections, stagger on card grids, hero entrance, magnetic CTAs.

## GSAP presets

```typescript
// Scroll-triggered fade up
export const fadeUpOnScroll = {
  initial: { opacity: 0, y: 60 },
  animate: { opacity: 1, y: 0 },
  scrollTrigger: {
    trigger: 'self',
    start: 'top 85%',
    end: 'top 20%',
    toggleActions: 'play none none reverse'
  },
  duration: 0.8,
  ease: 'power3.out'
};

// Stagger children
export const staggerContainer = {
  initial: {},
  animate: {
    transition: {
      staggerChildren: 0.1,
      delayChildren: 0.2
    }
  }
};

// SplitText line reveal
export const textReveal = {
  initial: { y: '100%', opacity: 0 },
  animate: {
    y: 0,
    opacity: 1,
    transition: {
      duration: 0.8,
      ease: [0.33, 1, 0.68, 1]
    }
  }
};

// Parallax layer
export const parallax = (speed: number = 0.5) => ({
  scrollTrigger: { scrub: true },
  y: (_: number, target: Element) =>
    -ScrollTrigger.maxScroll(window) * speed
});
```

## Motion presets

```typescript
// Page transition
export const pageTransition = {
  initial: { opacity: 0, y: 20 },
  animate: {
    opacity: 1, y: 0,
    transition: { duration: 0.5, ease: [0.25, 0.46, 0.45, 0.94] }
  },
  exit: {
    opacity: 0, y: -20,
    transition: { duration: 0.3 }
  }
};

// Card hover
export const cardHover = {
  rest:  { scale: 1,    boxShadow: '0 4px 6px -1px rgba(0,0,0,0.1)' },
  hover: {
    scale: 1.02,
    boxShadow: '0 20px 25px -5px rgba(0,0,0,0.1)',
    transition: { duration: 0.3, ease: 'easeOut' }
  }
};

// Magnetic button
export const magneticButton = {
  whileHover: { scale: 1.05 },
  whileTap:   { scale: 0.95 },
  transition: { type: 'spring', stiffness: 400, damping: 17 }
};
```

## Rules

- **Respect `prefers-reduced-motion`.** Wrap heavy motion in a media query — never fight the user's OS setting.
- **Hardware-accelerate everything.** `transform` + `opacity` only for 60fps. Never animate `top` / `left` / `width` / `height`.
- **AnimatePresence for exits.** Any element that leaves the tree gets an exit animation, not a hard unmount.
- **ScrollTrigger cleanup on route change.** `ScrollTrigger.getAll().forEach(t => t.kill())` in the effect's cleanup, or the animations pile up.
- **Kinetic type is a garnish, not a course.** One SplitText hero + one section-header reveal per page. More than that = amateur hour.
