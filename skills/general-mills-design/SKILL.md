---
name: general-mills-design
description: Apply General Mills corporate brand design language to frontend interfaces, artifacts, dashboards, presentations, and web components. Use this skill whenever the user mentions General Mills, asks for something in the "General Mills style," references the Champions intranet, Big G branding, or any General Mills sub-brand (Cheerios, Nature Valley, Betty Crocker, Pillsbury, etc.). Also trigger when building internal tools, dashboards, landing pages, or any UI intended for General Mills employees or partners. This skill covers typography, color palettes, layout patterns, component styling, and overall brand-aligned aesthetics.
---

# General Mills Corporate Design Skill

This skill applies General Mills' corporate brand design language to any frontend output — HTML pages, React components, dashboards, internal tools, presentations, and artifacts.

## When to Use

- Any UI, page, or component styled for General Mills
- Internal tools or dashboards for General Mills employees
- Content referencing the Champions intranet portal
- Landing pages, reports, or marketing materials in the General Mills brand
- Sub-brand work that needs to align with corporate parent identity

## Brand Foundation

### Brand Identity

General Mills' visual identity is built around three pillars:
1. **Heritage & Trust** — A 100+ year legacy in American food. Design should feel established, reliable, and warm.
2. **Making Food People Love** — The brand tagline. Design should communicate care, approachability, and quality.
3. **The Big G** — The iconic cursive "G" emblem with a red heart. It is the primary brand symbol.

### Color Palette

Use CSS custom properties for all colors. The palette is rooted in deep blue and vibrant red:

```css
:root {
  /* Primary */
  --gm-blue:          #234291;   /* Primary brand blue — headers, nav, CTAs */
  --gm-red:           #E32123;   /* Brand red — accents, hearts, alerts */

  /* Secondary */
  --gm-navy:          #0B1F4A;   /* Deep navy — dark backgrounds, footer */
  --gm-light-blue:    #4A7FD4;   /* Lighter blue — links, hover states */
  --gm-sky:           #D6E4F7;   /* Pale sky — card backgrounds, tints */

  /* Neutrals */
  --gm-white:         #FFFFFF;
  --gm-off-white:     #F7F8FA;   /* Page backgrounds */
  --gm-warm-gray:     #E8E5E0;   /* Borders, dividers */
  --gm-mid-gray:      #8C8C8C;   /* Secondary text */
  --gm-charcoal:      #2D2D2D;   /* Body text */

  /* Accent */
  --gm-gold:          #C5972C;   /* Awards, highlights, premium feel */
  --gm-green:         #3A7D3E;   /* Success, sustainability messaging */
  --gm-heart-red:     #DC3545;   /* Heart icon accent, warmer red */

  /* Functional */
  --gm-success:       #3A7D3E;
  --gm-warning:       #C5972C;
  --gm-error:         #E32123;
  --gm-info:          #4A7FD4;
}
```

**Usage rules:**
- `--gm-blue` is the dominant brand color. Use for primary navigation, headers, and key CTAs.
- `--gm-red` is an accent — never dominant. Use sparingly for emphasis, alerts, the heart icon, and hover accents.
- Blue-to-white gradients are preferred over flat blocks for hero sections.
- Dark backgrounds should use `--gm-navy`, never pure black.
- Body text is `--gm-charcoal` on `--gm-off-white` or `--gm-white`.

### Typography

General Mills uses **Gotham Bold** for its official wordmark and tagline. For web implementations, use the closest freely available alternatives:

| Role | Font Family | Weight | Fallback |
|------|------------|--------|----------|
| **Headlines / H1-H2** | `'Montserrat', sans-serif` | 700–800 | Gotham substitute |
| **Subheadings / H3-H5** | `'Montserrat', sans-serif` | 600 | — |
| **Body text** | `'Source Sans 3', 'Source Sans Pro', sans-serif` | 400 | Clean readability |
| **Captions / labels** | `'Source Sans 3', sans-serif` | 400–600 | — |
| **Data / tables** | `'Source Sans 3', sans-serif` | 400 | Monospace fallback for numbers |

**Google Fonts import:**
```html
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800&family=Source+Sans+3:wght@300;400;500;600;700&display=swap" rel="stylesheet">
```

**Typography rules:**
- Headlines are bold and uppercase or title case — never all-lowercase.
- Letter-spacing on uppercase headlines: `0.05em` to `0.08em`.
- Line-height for body: `1.6`. For headings: `1.2`.
- Avoid thin or ultralight weights — General Mills communicates confidence and strength.

### Layout Patterns

#### Navigation
- **Top nav bar:** `--gm-blue` background, white text, red accents on active/hover.
- Height: 64–72px desktop, 56px mobile.
- Logo (Big G or wordmark) always left-aligned.
- Search bar integrated center or right.
- Champions-style: horizontal nav with dropdown mega-menus.

#### Page Structure
- **Hero sections:** Full-width, often with a subtle blue gradient or lifestyle photography background with text overlay on a semi-transparent blue panel.
- **Content width:** Max 1200px centered, with generous 24–40px padding.
- **Card grids:** 3-column on desktop, 2 on tablet, 1 on mobile. Cards use white backgrounds with subtle `box-shadow: 0 2px 8px rgba(0,0,0,0.08)` and `border-radius: 8px`.
- **Sections** alternate between white and `--gm-off-white` backgrounds.

#### Component Patterns

**Buttons:**
```css
.btn-primary {
  background: var(--gm-blue);
  color: white;
  font-family: 'Montserrat', sans-serif;
  font-weight: 600;
  padding: 12px 28px;
  border-radius: 6px;
  border: none;
  letter-spacing: 0.02em;
  transition: background 0.2s, transform 0.1s;
}
.btn-primary:hover {
  background: #1a3477;
  transform: translateY(-1px);
}
.btn-secondary {
  background: transparent;
  color: var(--gm-blue);
  border: 2px solid var(--gm-blue);
  /* Same padding, font, radius as primary */
}
.btn-accent {
  background: var(--gm-red);
  color: white;
  /* Use sparingly — for urgent CTAs only */
}
```

**Cards:**
```css
.gm-card {
  background: var(--gm-white);
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  padding: 24px;
  transition: box-shadow 0.2s, transform 0.2s;
}
.gm-card:hover {
  box-shadow: 0 4px 16px rgba(0,0,0,0.12);
  transform: translateY(-2px);
}
```

**Tables (data-heavy layouts):**
```css
.gm-table th {
  background: var(--gm-blue);
  color: white;
  font-family: 'Montserrat', sans-serif;
  font-weight: 600;
  text-transform: uppercase;
  font-size: 0.85rem;
  letter-spacing: 0.04em;
  padding: 12px 16px;
}
.gm-table tr:nth-child(even) {
  background: var(--gm-off-white);
}
```

**Form inputs:**
```css
.gm-input {
  border: 1px solid var(--gm-warm-gray);
  border-radius: 6px;
  padding: 10px 14px;
  font-family: 'Source Sans 3', sans-serif;
  font-size: 1rem;
  transition: border-color 0.2s;
}
.gm-input:focus {
  border-color: var(--gm-blue);
  outline: none;
  box-shadow: 0 0 0 3px rgba(35, 66, 145, 0.15);
}
```

### Iconography & Visual Elements

- Prefer clean, outlined icons (Lucide, Heroicons style).
- The **heart** motif is central to the brand — use as a decorative accent, in "favorites" features, or to punctuate key messages.
- Avoid overly playful or cartoon-style icons in corporate contexts.
- Photography should be warm, well-lit, showing food, people, and community.

### Motion & Interaction

- Transitions are smooth and professional: `0.2s ease` default.
- Page load: subtle fade-in with stagger (`animation-delay`) for cards and sections.
- No flashy or bouncy animations — motion should feel confident and intentional.
- Hover states: gentle lift (`translateY(-2px)`) + shadow deepening.

### Responsive Approach

- Mobile-first with breakpoints at 768px (tablet) and 1024px (desktop).
- Navigation collapses to a hamburger menu on mobile.
- Cards stack single-column on mobile with full-width.
- Typography scales down ~15% on mobile.

## Champions Intranet Style

When building interfaces that reference the Champions intranet specifically:
- Use a **sidebar navigation** pattern (collapsible) with `--gm-navy` background.
- Include a top utility bar with user avatar, search, and quick links.
- Content area has a white background with generous padding.
- News/announcement cards use a featured image + title + excerpt pattern.
- Dashboard tiles use the card pattern with KPI numbers in `--gm-blue` and trend indicators.

## Sub-Brand Adaptations

When work involves a specific General Mills brand, layer that brand's personality on top of the corporate foundation:
- **Cheerios:** Add warm yellow (`#FFD700`) as an accent alongside the corporate blue.
- **Nature Valley:** Incorporate earthy greens and outdoor photography vibes.
- **Betty Crocker:** Red becomes more prominent; use warmer tones.
- **Pillsbury:** Softer, rounder UI elements; playful but polished.
- **Häagen-Dazs:** Premium/luxury feel; darker palette, elegant serif headings.

For detailed sub-brand palettes, consult `references/sub-brands.md`.

## Implementation Checklist

Before delivering any General Mills branded output, verify:

- [ ] Primary colors are `--gm-blue` and `--gm-red` (not generic blues/reds)
- [ ] Headlines use Montserrat Bold (700+)
- [ ] Body text uses Source Sans 3
- [ ] No pure black text — use `--gm-charcoal`
- [ ] No pure black backgrounds — use `--gm-navy`
- [ ] Cards have proper shadow and hover states
- [ ] Buttons follow the primary/secondary/accent pattern
- [ ] Red is used as an accent, never as the dominant color
- [ ] Layout has proper max-width (1200px) and padding
- [ ] Navigation bar uses `--gm-blue` background
- [ ] Responsive breakpoints are implemented
- [ ] Motion is subtle and professional
