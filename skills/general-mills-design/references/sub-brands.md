# General Mills Sub-Brand Design References

This document provides color palettes and design adaptations for major General Mills brands.
When building for a specific sub-brand, start with the corporate foundation from SKILL.md
and layer these brand-specific overrides on top.

---

## Cheerios

**Personality:** Wholesome, family-oriented, bright, uplifting
**Tone:** Warm, cheerful, community-focused

```css
:root {
  --cheerios-yellow:    #FFD700;
  --cheerios-gold:      #DAA520;
  --cheerios-brown:     #8B6914;
  --cheerios-cream:     #FFF8DC;
}
```

- Use `--cheerios-yellow` as the primary accent instead of `--gm-red`.
- Backgrounds can lean into warm creams and soft yellows.
- Typography stays corporate (Montserrat + Source Sans 3).
- Rounded corners: increase to `12px` for a friendlier feel.

---

## Nature Valley

**Personality:** Outdoor, wholesome, earthy, adventurous
**Tone:** Fresh, grounded, natural

```css
:root {
  --nv-forest:          #2D6A2E;
  --nv-leaf:            #5A9E3F;
  --nv-earth:           #8B6F47;
  --nv-wheat:           #D4A843;
  --nv-sky:             #87CEEB;
  --nv-cream:           #F5F0E1;
}
```

- Green replaces blue as the dominant brand color.
- Background textures with subtle grain or paper effects work well.
- Photography: outdoor landscapes, trails, granola close-ups.
- Keep the corporate blue in the footer and secondary nav elements.

---

## Betty Crocker

**Personality:** Home-cooking, trusted, warm, classic American
**Tone:** Confident, welcoming, domestic warmth

```css
:root {
  --bc-red:             #CC0000;
  --bc-cream:           #FFF5EB;
  --bc-warm-white:      #FAF3E8;
  --bc-brown:           #5C3317;
  --bc-gold:            #B8860B;
}
```

- Red becomes more prominent (but still balanced with neutral tones).
- Background shifts to warm whites and creams.
- Use the iconic red spoon motif as a decorative element.
- Serif fonts (like Playfair Display) can supplement Montserrat for editorial recipe content.

---

## Pillsbury

**Personality:** Playful, comforting, family fun, baking joy
**Tone:** Soft, approachable, slightly whimsical

```css
:root {
  --pb-blue:            #004B87;
  --pb-white:           #FFFFFF;
  --pb-soft-blue:       #B8D4E8;
  --pb-warm-cream:      #FFF7E6;
  --pb-dough:           #F0E4C8;
}
```

- Softer blue tones than the corporate palette.
- Border-radius increases: `12–16px` for buttons and cards.
- UI elements should feel "puffy" — generous padding, soft shadows.
- Maintain the white + blue core of the Pillsbury Doughboy aesthetic.

---

## Häagen-Dazs

**Personality:** Premium, luxurious, sophisticated, indulgent
**Tone:** Elegant, refined, grown-up

```css
:root {
  --hd-burgundy:        #722F37;
  --hd-gold:            #C5A55A;
  --hd-cream:           #F5ECD7;
  --hd-charcoal:        #1A1A1A;
  --hd-dark:            #0D0D0D;
}
```

- Dark, rich backgrounds are standard (deep burgundy or near-black).
- Gold accents for dividers, borders, and highlights.
- Typography: switch headlines to a refined serif like `'Playfair Display', serif`.
- Generous whitespace, minimal UI chrome, focus on imagery.
- Photography: dramatic close-ups with shallow depth of field.

---

## Old El Paso

**Personality:** Bold, festive, Tex-Mex fun, family dinner excitement
**Tone:** Vibrant, energetic, warm

```css
:root {
  --oep-red:            #C41E3A;
  --oep-yellow:         #FFB800;
  --oep-green:          #3A7728;
  --oep-terracotta:     #CC7A3E;
  --oep-cream:          #FFF5E0;
}
```

- Warm, saturated color palette inspired by Southwestern aesthetics.
- Use textured backgrounds (subtle paper or fabric).
- Bold, large headlines with tight leading.
- Photography: vibrant overhead shots of prepared dishes.

---

## Annie's Homegrown

**Personality:** Organic, playful, kid-friendly, wholesome
**Tone:** Fun, responsible, natural

```css
:root {
  --annies-purple:      #6B3FA0;
  --annies-green:       #4CAF50;
  --annies-yellow:      #FFD600;
  --annies-cream:       #FFF8E7;
}
```

- Purple is the signature color — use as primary CTA and header accent.
- Green indicates organic / natural messaging.
- More playful illustration style is acceptable here.
- Border-radius: `16px` for a friendly, rounded aesthetic.
- The bunny mascot can appear as a small decorative element.

---

## Blue Buffalo (Pet)

**Personality:** Premium pet nutrition, caring, trustworthy
**Tone:** Warm but authoritative, pet-parent focused

```css
:root {
  --bb-blue:            #003DA5;
  --bb-light-blue:      #5B9BD5;
  --bb-tan:             #C9B98E;
  --bb-brown:           #6B4226;
  --bb-white:           #FAFAF5;
}
```

- Blue is dominant — aligns with corporate palette naturally.
- Warm tan/brown accents create pet-friendly warmth.
- Photography: happy pets, outdoor scenes, close-ups of food ingredients.
- Clean, informational layout — pet parents research carefully.
