---
name: Executive Enterprise
colors:
  surface: '#f9f9ff'
  surface-dim: '#d3daee'
  surface-bright: '#f9f9ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f1f3ff'
  surface-container: '#e9edff'
  surface-container-high: '#e2e8fc'
  surface-container-highest: '#dce2f6'
  on-surface: '#151b2a'
  on-surface-variant: '#434655'
  inverse-surface: '#2a3040'
  inverse-on-surface: '#edf0ff'
  outline: '#737686'
  outline-variant: '#c3c6d7'
  surface-tint: '#0053db'
  primary: '#004ac6'
  on-primary: '#ffffff'
  primary-container: '#2563eb'
  on-primary-container: '#eeefff'
  inverse-primary: '#b4c5ff'
  secondary: '#006a63'
  on-secondary: '#ffffff'
  secondary-container: '#99efe5'
  on-secondary-container: '#006f67'
  tertiary: '#00632b'
  on-tertiary: '#ffffff'
  tertiary-container: '#117e3b'
  on-tertiary-container: '#c4ffc9'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dbe1ff'
  primary-fixed-dim: '#b4c5ff'
  on-primary-fixed: '#00174b'
  on-primary-fixed-variant: '#003ea8'
  secondary-fixed: '#9cf2e8'
  secondary-fixed-dim: '#80d5cb'
  on-secondary-fixed: '#00201d'
  on-secondary-fixed-variant: '#00504a'
  tertiary-fixed: '#95f8a7'
  tertiary-fixed-dim: '#79db8d'
  on-tertiary-fixed: '#00210a'
  on-tertiary-fixed-variant: '#005323'
  background: '#f9f9ff'
  on-background: '#151b2a'
  surface-variant: '#dce2f6'
  page-bg-light: '#F6F8FC'
  surface-light: '#FFFFFF'
  elevated-light: '#F9FBFD'
  border-light: '#DCE3EC'
  text-secondary-light: '#5B6678'
  text-muted-light: '#7C8798'
  soft-blue-fill: '#EAF1FF'
  soft-teal-fill: '#E8F7F4'
  page-bg-dark: '#090D14'
  surface-dark: '#111722'
  elevated-dark: '#171F2C'
  border-dark: '#293243'
  primary-dark: '#60A5FA'
  secondary-dark: '#2DD4BF'
  text-primary-dark: '#F3F6FA'
  text-secondary-dark: '#9BA7B8'
typography:
  hero-lg:
    fontFamily: Manrope
    fontSize: 64px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  hero-lg-mobile:
    fontFamily: Manrope
    fontSize: 40px
    fontWeight: '700'
    lineHeight: '1.1'
  headline-page:
    fontFamily: Manrope
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.015em
  headline-page-mobile:
    fontFamily: Manrope
    fontSize: 34px
    fontWeight: '700'
    lineHeight: '1.2'
  headline-section:
    fontFamily: Manrope
    fontSize: 36px
    fontWeight: '600'
    lineHeight: '1.25'
    letterSpacing: -0.01em
  headline-card:
    fontFamily: Manrope
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-base:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-technical:
    fontFamily: IBM Plex Mono
    fontSize: 13px
    fontWeight: '500'
    lineHeight: 18px
    letterSpacing: 0.05em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  baseline: 8px
  section-v-desktop: 96px
  section-v-mobile: 64px
  card-padding-lg: 32px
  card-padding-sm: 24px
  container-max: 1240px
  gutter-desktop: 24px
  gutter-mobile: 18px
---

## Brand & Style

This design system is engineered for a premium, recruiter-focused portfolio that bridges the gap between high-level technology consultancy and rigorous enterprise software engineering. The brand personality is **authoritative, strategic, and outcome-oriented**, designed to evoke a sense of reliability and technical mastery. 

The aesthetic is a sophisticated mix of **Corporate Modern** and **Minimalism**. It utilizes a disciplined 8px grid-based layout and generous whitespace to ensure clarity, while employing thin 1px borders and refined typography to signal quality. The "Evidence over Claims" philosophy is manifested through data-focused components, monochrome partner strips, and technical micro-copy that frames the portfolio as a high-end product rather than a personal gallery.

## Colors

The system uses two distinct palettes to transition between a crisp, professional light theme and a premium, high-contrast dark theme. 

**Light Theme Strategy:**
Uses `#F6F8FC` as the page foundation to create a cool, institutional atmosphere. Main surfaces are pure white to provide maximum contrast for content. Primary accents use a precise blue (`#2563EB`) for actions and a deep teal (`#0F766E`) for thematic categorization.

**Dark Theme Strategy:**
Built on an obsidian foundation (`#090D14`) with deep slate surfaces (`#111722`). Accent colors are lightened for optimal accessibility and vibrancy against dark backgrounds, specifically utilizing `#60A5FA` for primary interactions.

**Functional Accents:**
Success states and impact metrics utilize a specialized green (`#15803D` light / `#4ADE80` dark) to highlight positive outcomes and data-driven achievements.

## Typography

The typographic strategy is built on a "Executive-meets-Developer" triad:
- **Manrope** provides geometric, authoritative headings that anchor the visual hierarchy.
- **Inter** ensures high readability for project narratives and technical documentation.
- **IBM Plex Mono** is used exclusively for technical micro-copy, metadata, and status badges to signal precision and engineering rigor.

For display headings (Hero and Page levels), use tight line heights and negative letter spacing to create a high-impact, modern editorial feel. Body text should maintain generous line heights (approx. 1.55x - 1.6x the font size) to ensure long-form case studies remain accessible and professional.

## Layout & Spacing

This design system follows a **Fixed Grid** philosophy within a max-width container of 1240px. The layout is underpinned by a strict 8px baseline rhythm, where all margins, paddings, and component heights are multiples of 8.

**Grid Architecture:**
- **Desktop:** A 12-column fluid grid for interior case studies, with 24px gutters.
- **Mobile:** Single-column stacking with 18px side margins.

**Spacing Rhythm:**
Vertical section spacing is exceptionally generous (96px+) to create a premium, calm pace. For internal card content, use a two-tiered padding system: 32px for primary showcase containers and 24px for secondary or nested information blocks.

## Elevation & Depth

Hierarchy is established through a **Tonal Layering** approach combined with **Subtle Shadows**. Instead of dramatic 3D effects, the system uses low-contrast background tiers to separate content.

- **Surface Tiers:** In light mode, `#FFFFFF` cards sit on a `#F6F8FC` background. In dark mode, `#111722` cards sit on a `#090D14` background.
- **Shadows:** Use extra-diffused, low-opacity ambient shadows only on interactive card elements. For example: `0 12px 24px -8px rgba(0,0,0,0.08)`.
- **Structural Outlines:** Every card and navigation element must have a 1px solid border using the respective theme's `border` token. This reinforces the grid-based, engineering-led aesthetic.
- **Backdrop Blur:** The top navigation bar uses an 80% opaque surface with a 12px backdrop blur to maintain context during scrolling.

## Shapes

The shape language is "Soft Professional." While the overall layout is rigid and grid-based, rounded corners are used to humanize the interface and prevent it from feeling overly "industrial."

- **Primary Cards:** 18px (`rounded-lg` equivalent).
- **Secondary Cards/Inputs:** 14px.
- **Buttons:** 10px.
- **Technical Tags/Badges:** 9999px (Pill-shaped) to distinguish them from structural containers.

All borders must be consistently 1px wide. Avoid rounded corners on the global page container; keep the edges of the viewport sharp.

## Components

**Buttons:**
Primary CTAs use a solid fill of the primary accent with 10px rounded corners. Secondary buttons should be "Ghost" style: a 1px border using the `border` token with `primary-text`. Active states should include a subtle scale-down (0.98) or a background shift.

**Technical Badges:**
Small pill-shaped tags using `label-technical` typography. Use `soft-blue-fill` with `primary-accent` text for general tech, and `soft-teal-fill` with `secondary-accent` text for strategy/process labels.

**Cards:**
Every card must feature a 1px border. Hovering on showcase cards should trigger a subtle 3px upward translation and an expansion of the ambient shadow.

**Asset Framing:**
All screenshots of software or code must be placed inside a custom "Browser Frame" or "App Window" component—a container with a top bar, three window control dots (rendered in secondary text color), and 1px borders.

**Credibility Strip:**
A horizontal flex container for institutional logos. Logos must be rendered as monochrome SVG vectors at 60% opacity using `secondary-text` to ensure they don't distract from the primary portfolio content.

**Input Fields:**
Large, 14px rounded fields with 1px borders. Focused states use a 2px `primary-accent` ring with 0% offset.