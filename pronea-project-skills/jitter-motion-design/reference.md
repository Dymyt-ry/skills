# Jitter Reference

## Complete Keyboard Shortcuts

### General
| Shortcut | Action |
|----------|--------|
| `⌘ Z` / `Ctrl Z` | Undo |
| `⇧ ⌘ Z` / `⇧ Ctrl Z` | Redo |
| `⌘ C` / `Ctrl C` | Copy |
| `⌘ X` / `Ctrl X` | Cut |
| `⌘ V` / `Ctrl V` | Paste |
| `⇧ ⌘ V` / `⇧ Ctrl V` | Sync paste from Figma (preserves animations) |
| `Delete` / `⌫` | Delete |
| `⌘ D` / `Ctrl D` | Duplicate (also works in timeline) |
| `M` | Toggle Design ↔ Animate mode |

### Tools
| Shortcut | Tool |
|----------|------|
| `T` | Text |
| `R` | Rectangle |
| `O` | Ellipse |
| `H` / Middle click | Pan |

### View
| Shortcut | Action |
|----------|--------|
| `1` or `)` | Zoom to 100% |
| `+` or `=` | Zoom in |
| `-` | Zoom out |
| `⇧ 2` | Pan and zoom to show selected layer(s) |

### Timeline
| Shortcut | Action |
|----------|--------|
| `Space` | Play / Pause |
| `,` `.` | Move time cursor ±10ms |
| `⇧ + ,` `⇧ + .` | Move time cursor ±100ms |
| `⌥ + ,` `⌥ + .` | Jump to previous/next animation |
| `⇧ ⌥ + ,` `⇧ ⌥ + .` | Jump to beginning/end of scene |
| `← →` | Move animation ±10ms |
| `⇧ + ← →` | Move animation ±100ms |
| `⌥` / `Alt` + drag | Resize timeline operation symmetrically |

### Layers
| Shortcut | Action |
|----------|--------|
| `← → ↑ ↓` | Move element 1px |
| `⇧ + ← → ↑ ↓` | Move element 10px |
| `⌘ G` / `Ctrl G` | Group |
| `⇧ ⌘ G` / `⇧ Ctrl G` | Ungroup |
| `⌃ ⌘ M` | Create mask |
| `⌥ L` / `Alt L` | Collapse all layer groups |

## Editor UI Layout

```
┌──────────────────────────────────────────────────────┐
│  Toolbar: [Select] [T] [R] [O] [Pen]  ...  [Export] │
├────────────┬─────────────────────┬───────────────────┤
│            │                     │  Right Sidebar:    │
│  Layer     │                     │  ┌──────┬────────┐ │
│  List      │      Canvas         │  │Design│Animate │ │
│            │                     │  ├──────┴────────┤ │
│  - Layer 1 │   (artboards with   │  │ Position      │ │
│  - Layer 2 │    design elements)  │  │ Size          │ │
│  - Group   │                     │  │ Color/Fill    │ │
│    - Child │                     │  │ Opacity       │ │
│            │                     │  │ Blend Mode    │ │
│            │                     │  │ Font          │ │
│            │                     │  │ Corner Radius │ │
├────────────┴─────────────────────┴───────────────────┤
│  Timeline (horizontal bars per layer/animation)       │
│  [▶ Play] ──────|████████|──────|████|──────────────  │
└──────────────────────────────────────────────────────┘
```

## Animation Actions Detail

### In (Entrance) Presets
- **Fade in** — opacity 0→1
- **Slide in** — from direction (top, bottom, left, right) with distance
- **Scale in** — from smaller/larger to original size
- **Blur in** — from blurred to sharp
- **Mask reveal** — clip-based entrance
- **Rotate in** — rotation-based entrance
- **Custom** — combine any properties

### Out (Exit) Presets
Mirror of In presets: Fade out, Slide out, Scale out, Blur out, Mask hide, Rotate out, Custom.

### Custom Animation Properties
Each custom action can control:
- **Position** (X, Y) — with optional curved Bezier paths
- **Rotation** (degrees)
- **Scale** (X, Y independently or uniform)
- **Opacity** (0–100%)
- **Blur** (0–∞px)
- **Color/Fill** transitions
- **Duration** (ms)
- **Delay** (ms)
- **Easing** (preset or custom curve)

### Text-Specific Animation
- Animate by: **Line**, **Word**, **Letter**
- Stagger: Delay between each unit
- Custom text effects (since March 2026): Define movement, rotation, scale, opacity, acceleration per character unit — reusable across files

## Easing Reference

| Preset | Behavior | Best For |
|--------|----------|----------|
| Slow down | Fast start, gentle stop | Natural movement |
| Accelerate | Slow start, fast end | Elements leaving |
| Elastic | Springy overshoot | Playful UI |
| Bounce | Bouncing at end | Landing effects |
| Overshoot | Goes past, then settles | Snappy entrances |
| Linear | Constant speed | Mechanical motion |
| Custom | User-defined cubic bezier | Brand-specific timing |

Intensity slider (0–100%) controls how pronounced the easing is.

## Blend Modes

Available in Design tab → Opacity section:
- Normal, Multiply, Screen, Overlay, Darken, Lighten, Color Dodge, Color Burn, Hard Light, Soft Light, Difference, Exclusion, Hue, Saturation, Color, Luminosity

## Export Specifications

### Video
| Setting | Free | Pro | Team |
|---------|------|-----|------|
| Max Resolution | 720p | 1080p | 2160p (4K) |
| Max FPS | 30 | 60 | 120 |
| Formats | MP4 | MP4, MOV, WebM | MP4, MOV, WebM, ProRes 4444 |
| Transparent | No | No | Yes (ProRes 4444, WebM) |

### GIF
All plans. Optimized for email and social.

### Lottie
All plans. Infinitely scalable vector format.

**Lottie-supported features**: Position, scale, rotation, opacity, color, blur, masks (static), gradients, shapes, groups.

**Lottie unsupported**: Text animations (use fade), animated masks (use fade), donuts/pies, video layers, audio layers.

### PNG Frame Export
Team plan only. Exports each frame as individual PNG — useful for sprite sheets or advanced compositing.

## Pricing Tiers (as of 2026)

| Feature | Free | Pro | Team | Enterprise |
|---------|------|-----|------|------------|
| Files | 3 workspace files | Unlimited | Unlimited | Unlimited |
| Editors | — | Up to 10 | Up to 50 | Unlimited |
| AI Credits | Limited | Increased | Maximum | Custom |
| Collaboration | Real-time | Real-time | Real-time + priority support | SAML/SSO |
| Libraries | — | — | Team libraries | Team libraries |

## AI Features Detail

### AI Brainstorm
1. Open file, click ✨ icon (top-right of artboard)
2. Choose mood: **Playful**, **Bold**, **Soft**, **Elegant**, **Cinematic**
3. AI assistant "Oli" generates a fully editable animation draft
4. Customize, tweak timing, swap presets as needed

### Image to Video
1. Select an image layer on canvas
2. Go to Animate tab → click **Generate video**
3. Optionally: Click "View and edit prompt" to customize
4. Oli generates a short video clip replacing the image

## Figma Plugin Variants

| Plugin | Purpose | Since |
|--------|---------|-------|
| Jitter for Figma | Import standard Figma designs | 2021 |
| Jitter for Figma Buzz | Import Figma Buzz designs | Oct 2025 |
| Jitter for Figma Draw | Import Figma Draw (patterns, brushes, variable strokes) | Feb 2026 |

## Recent Feature Timeline (2025–2026)

| Date | Feature |
|------|---------|
| Mar 2026 | Custom text effects |
| Mar 2026 | Multi-layer hide and lock |
| Mar 2026 | Prompting: Image to video |
| Feb 2026 | Figma Draw plugin |
| Feb 2026 | Image to video (AI) |
| Jan 2026 | Formulas in input fields |
| Nov 2025 | AI Brainstorm |
| Nov 2025 | Blend modes |
| Oct 2025 | Figma Buzz plugin |
| Sep 2025 | Gradients on strokes |
| Aug 2025 | 5x faster export |
| Jul 2025 | Pen tool and morphing |
| Feb 2025 | Custom easings |
| Feb 2025 | Infinite canvas |
