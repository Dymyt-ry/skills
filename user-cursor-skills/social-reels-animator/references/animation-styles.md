# Animation Style Guide

Minimalistic motion graphics inspired by NotebookLM's whiteboard/explainer aesthetic. Think: clean, dark, typography-driven, subtle motion.

## Core Aesthetic

- **Dark canvas** with subtle radial gradient glow behind focal elements
- **Typography-first** — text is the main visual, not illustrations
- **Geometric accents** — thin lines, rounded rectangles, circles as decorative elements
- **Monochromatic + one accent** — navy + snow + teal, with amber/coral only for emphasis
- **Negative space** — at least 40% of each frame should be empty

## Motion Language

### Entrances
| Type | Use For | Timing |
|------|---------|--------|
| **Fade up** | Body text, labels | 300-500ms, ease-out |
| **Scale spring** | Numbers, key stats | 400-600ms, spring(config={damping: 12}) |
| **Slide from bottom** | Sequential items | 300ms, ease-out, staggered 200ms |
| **Typewriter** | Quotes, short sentences | 40-60ms per character |
| **Draw on** | Lines, underlines, borders | 500-800ms, ease-in-out |

### Exits
| Type | Use For | Timing |
|------|---------|--------|
| **Fade out** | Any element | 200-300ms |
| **Scale down** | Transitioning between sections | 300ms |
| **Slide out left** | Making room for next content | 250ms |

### Transitions Between Beats
| Type | Description |
|------|-------------|
| **Cross-fade** | Default. 300ms overlap between sections |
| **Wipe** | Teal-colored bar sweeps across screen |
| **Scale zoom** | Current content scales up and fades, new content scales up from small |

## Decorative Elements

### Glow
Soft radial gradient behind key numbers or headlines:
```css
background: radial-gradient(circle at center, rgba(0, 212, 170, 0.08) 0%, transparent 60%);
```

### Grid dots
Subtle background pattern for texture:
```css
background-image: radial-gradient(rgba(200, 214, 229, 0.06) 1px, transparent 1px);
background-size: 24px 24px;
```

### Accent line
Thin animated line that draws on before text appears:
- Color: `#00D4AA` at 40% opacity
- Width: 2px
- Animated with draw-on effect

### Corner badge
Small pill in top-left with category label:
- Background: `rgba(0, 212, 170, 0.12)`
- Border: `1px solid rgba(0, 212, 170, 0.2)`
- Text: teal, uppercase, 0.7rem, 600 weight

## Typography Compositions

### Hero Number
```
[category label — small, muted, uppercase, spaced]
[BIG NUMBER — 120-180px, JetBrains Mono, teal, bold]
[context — 24-28px, Inter, snow, regular]
```

### Statement
```
[hook — 48-64px, Inter, snow, 800 weight, centered]
[subtext — 22-26px, Inter, gray, 400 weight, centered]
```

### Step Card
```
[step number — 64px, JetBrains Mono, teal, left-aligned]
[step title — 36px, Inter, snow, 700 weight]
[step description — 20px, Inter, gray, 400 weight]
```

## Safe Zones (1080×1920)

```
┌──────────────────────────┐
│ 90px                     │ ← Platform UI (username, etc.)
│  ┌──────────────────┐    │
│  │                  │    │
│  │  CONTENT AREA    │    │
│  │  900 × 1540 px   │    │
│  │                  │    │
│  └──────────────────┘    │
│                     90px │ ← Like/comment/share buttons
│ 200px                    │ ← Caption overlay area
└──────────────────────────┘
```

Keep all important text within the 900×1540 content area (90px padding on sides, 90px top, 290px bottom).

## Do / Don't

| Do | Don't |
|----|-------|
| Use spring easing for number reveals | Use linear easing (feels robotic) |
| Keep text on screen 2+ seconds | Flash text faster than reading speed |
| Use consistent stagger delays | Randomize animation timing |
| Animate max 3 elements at once | Animate everything simultaneously |
| Use teal for 1-2 accent elements | Make everything teal |
| Leave breathing room between beats | Rush from one beat to the next |
| Use JetBrains Mono for numbers | Use decorative/script fonts |
| Dark navy background | Pure black (#000) background |
