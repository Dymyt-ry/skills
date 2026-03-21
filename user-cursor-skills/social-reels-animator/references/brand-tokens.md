# Brand Tokens for Video

Design system extracted from Pronea landing page, optimized for 1080×1920 video canvas.

## Colors

### Core Palette
```json
{
  "navy":       "#0F1729",
  "navyLight":  "#1a2332",
  "teal":       "#00D4AA",
  "tealDim":    "rgba(0, 212, 170, 0.12)",
  "snow":       "#F8F9FC",
  "gray300":    "#c8d6e5",
  "gray500":    "#8395a7"
}
```

### Semantic Colors
```json
{
  "accent":     "#00D4AA",
  "warning":    "#F5A623",
  "danger":     "#FF4757",
  "success":    "#2ED573"
}
```

### Remotion Theme Object
```tsx
export const theme = {
  bg: '#0F1729',
  bgAlt: '#1a2332',
  accent: '#00D4AA',
  accentDim: 'rgba(0, 212, 170, 0.12)',
  text: '#F8F9FC',
  textMuted: '#8395a7',
  textSubtle: '#c8d6e5',
  warning: '#F5A623',
  danger: '#FF4757',
  success: '#2ED573',
} as const;
```

## Typography

### Font Stack
```css
--font-heading: 'Inter', -apple-system, sans-serif;
--font-mono: 'JetBrains Mono', 'SF Mono', monospace;
--font-body: 'Inter', -apple-system, sans-serif;
```

### Scale (at 1080px canvas width)

| Role | Font | Size | Weight | Tracking |
|------|------|------|--------|----------|
| Hero number | JetBrains Mono | 120-180px | 700-800 | -0.02em |
| Headline | Inter | 56-72px | 800 | -0.03em |
| Subheadline | Inter | 36-44px | 700 | -0.02em |
| Body | Inter | 24-28px | 400-500 | 0 |
| Label | Inter | 16-20px | 600 | 0.08em (uppercase) |
| Caption | Inter | 14-16px | 500 | 0.05em |
| Step number | JetBrains Mono | 64-96px | 800 | 0 |

### Google Fonts URL
```
https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;700;800&display=swap
```

## Canvas & Layout

### Dimensions
```
Width:  1080px
Height: 1920px
Aspect: 9:16
FPS:    30
```

### Grid
```
Padding:      90px horizontal, 90px top, 290px bottom (safe zone)
Content area: 900 × 1540px
Center axis:  x=540, y=960 (visual center at y=770 accounting for bottom safe zone)
```

### Spacing Scale
```
xs: 8px
sm: 16px
md: 24px
lg: 40px
xl: 64px
xxl: 96px
```

## Background Treatments

### Solid (default)
```css
background: #0F1729;
```

### With glow
```css
background: #0F1729;
/* Add radial glow behind focal point */
background-image: radial-gradient(ellipse at 50% 40%, rgba(0, 212, 170, 0.06) 0%, transparent 50%);
```

### With grid dots
```css
background: #0F1729;
background-image: radial-gradient(rgba(200, 214, 229, 0.04) 1px, transparent 1px);
background-size: 24px 24px;
```

### With gradient
```css
background: linear-gradient(180deg, #0F1729 0%, #1a2332 100%);
```

## Logo Usage

Logo files in `brand/logos/`:
- `spndr-logo-white.svg` — use on dark backgrounds
- `spndr-icon-dark-bg.svg` — compact icon version

Position logo in bottom-right corner of final frame:
- 90px from right, 320px from bottom (above caption safe zone)
- Size: ~120px width
- Opacity: 0.8, fades in during CTA beat

## Borders & Surfaces

### Card surface
```css
background: rgba(200, 214, 229, 0.04);
border: 1px solid rgba(200, 214, 229, 0.08);
border-radius: 12px;
```

### Highlighted card
```css
background: rgba(0, 212, 170, 0.04);
border: 1px solid rgba(0, 212, 170, 0.2);
border-radius: 12px;
```

### Pill / badge
```css
background: rgba(0, 212, 170, 0.12);
border: 1px solid rgba(0, 212, 170, 0.2);
border-radius: 100px;
padding: 6px 16px;
color: #00D4AA;
font-size: 16px;
font-weight: 600;
text-transform: uppercase;
letter-spacing: 0.08em;
```
