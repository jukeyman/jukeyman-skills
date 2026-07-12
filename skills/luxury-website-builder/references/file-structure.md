# File Structure — Match Exactly

Every site scaffolds to this tree. Include every directory even if some start empty — the skeleton signals a real build.

```
project-name/
├── app/                                    # Next.js 16 App Router
│   ├── layout.tsx                          # Root layout w/ providers
│   ├── page.tsx                            # Homepage
│   ├── loading.tsx                         # Global loading state
│   ├── error.tsx                           # Error boundary
│   ├── not-found.tsx                       # 404
│   ├── globals.css                         # Design system + base animations
│   ├── about/page.tsx
│   ├── services/
│   │   ├── page.tsx                        # Listing
│   │   └── [slug]/page.tsx                 # Detail
│   ├── portfolio/
│   │   ├── page.tsx
│   │   └── [slug]/page.tsx
│   ├── blog/
│   │   ├── page.tsx
│   │   └── [slug]/page.tsx
│   ├── contact/page.tsx
│   └── api/
│       ├── contact/route.ts                # Contact form handler
│       └── newsletter/route.ts             # Newsletter signup
│
├── components/
│   ├── ui/                                 # Base UI (shadcn/ui)
│   │   ├── button.tsx card.tsx input.tsx textarea.tsx select.tsx
│   │   ├── badge.tsx avatar.tsx spinner.tsx kbd.tsx
│   │   ├── dialog.tsx sheet.tsx toast.tsx tooltip.tsx
│   │   └── navigation-menu.tsx
│   │
│   ├── layout/
│   │   ├── header.tsx footer.tsx sidebar.tsx
│   │   ├── mobile-nav.tsx breadcrumb.tsx
│   │
│   ├── sections/                           # Page sections
│   │   ├── hero-section.tsx
│   │   ├── features-section.tsx
│   │   ├── services-section.tsx
│   │   ├── portfolio-section.tsx
│   │   ├── testimonials-section.tsx
│   │   ├── team-section.tsx
│   │   ├── stats-section.tsx
│   │   ├── pricing-section.tsx
│   │   ├── faq-section.tsx
│   │   ├── cta-section.tsx
│   │   ├── about-section.tsx
│   │   ├── contact-section.tsx
│   │   ├── blog-section.tsx
│   │   └── newsletter-section.tsx
│   │
│   ├── effects/                            # Signature visual effects
│   │   ├── glass-morphism.tsx
│   │   ├── particle-background.tsx
│   │   ├── gradient-blur.tsx
│   │   ├── scroll-reveal.tsx               # GSAP ScrollTrigger wrapper
│   │   ├── text-reveal.tsx
│   │   ├── cursor-follower.tsx
│   │   ├── magnetic-button.tsx
│   │   └── parallax-layer.tsx
│   │
│   ├── forms/
│   │   ├── contact-form.tsx
│   │   ├── newsletter-form.tsx
│   │   ├── quote-form.tsx
│   │   └── search-form.tsx
│   │
│   ├── cards/
│   │   ├── service-card.tsx
│   │   ├── portfolio-card.tsx
│   │   ├── team-card.tsx
│   │   ├── testimonial-card.tsx
│   │   ├── blog-card.tsx
│   │   └── pricing-card.tsx
│   │
│   ├── theme-provider.tsx                  # next-themes context
│   ├── theme-toggle.tsx
│   └── providers.tsx                       # All providers wrapper
│
├── lib/
│   ├── utils.ts constants.ts animations.ts validations.ts
│   └── hooks/
│       ├── use-scroll-progress.ts
│       ├── use-media-query.ts
│       ├── use-intersection.ts
│       └── use-local-storage.ts
│
├── styles/
│   └── animations.css                      # Extra CSS keyframes
│
├── public/
│   ├── images/ icons/ fonts/ animations/   # animations/ = Lottie
│
├── types/
│   └── index.ts
│
├── tailwind.config.ts
├── next.config.js
├── tsconfig.json
├── package.json
├── postcss.config.js
├── .eslintrc.json
├── .gitignore
├── .env.example                            # NEVER commit .env
└── README.md
```

## Rules

- **App Router only.** No `pages/` directory.
- **`proxy.ts` (not `middleware.ts`)** for edge middleware in Next 16.
- **Every section is a self-contained component** — no giant `page.tsx` files. Pages compose sections.
- **Every card and form has its own file.** Even if it feels like a lot of files, this is how agency codebases actually look — makes iteration and design-review sane.
- **`.env.example` is committed. `.env` and `.env.local` are gitignored from the first commit.**
