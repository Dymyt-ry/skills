---
name: social-reels-animator
description: "Create animated vertical video content (Reels, TikTok, Shorts) programmatically using Remotion or Python. Generates minimalistic motion-graphics-style animations following Pronea brand guidelines. Use when the user mentions 'reel,' 'animated reel,' 'social animation,' 'TikTok video,' 'YouTube Short,' 'Instagram Reel,' 'animated explainer,' 'motion graphics,' 'video content,' 'animate for social,' or wants to create short-form vertical video content."
---

# Social Reels Animator

Create minimalistic, branded animated videos for Reels / TikTok / Shorts. Style: clean motion graphics inspired by NotebookLM's whiteboard aesthetic — simple shapes, smooth reveals, bold typography on dark backgrounds.

## Brand Tokens (spndr)

```
BG:      #0a0a0a (black)
BG_ALT:  #080808 (deeper black)
ACCENT:  #f97316 (orange)
TEXT:    #ffffff (white)
LIGHT:   #f0f0f0 (body text)
MID:     #cccccc (subtitles)
MUTED:   #999999 (captions)
SURFACE: #444444 (cards)
DEEP:    #333333 (elevated surfaces)

FONT_HEADING: System sans-serif, weight 800-900
FONT_MONO:    System monospace, weight 500-700
FONT_BODY:    System sans-serif, weight 400

LOGO: "spndr." — dot is always orange #f97316
CANVAS: 1080 × 1920 px (9:16)
FPS: 30
```

For full brand system, see [references/brand-tokens.md](references/brand-tokens.md).

## Tooling

**Primary: Remotion (React)**
- Best ecosystem for programmatic video
- Spring physics, interpolation, frame-accurate
- TikTok template available: `npx create-video@latest --tiktok`
- Renders to MP4/WebM locally or via Lambda

**Alternative: Python (movis)**
- `pip install movis`
- Keyframe animation, layer compositing, easing
- Good for simpler animations without Node.js

**Content source: notebooklm-py** (optional)
- `pip install notebooklm-py`
- Generate video overviews from documents
- Use as content input, then animate with Remotion/movis

Setup script: `bash scripts/setup.sh` (bootstraps Remotion project with brand config)

## Reel Types & Templates

### 1. Stat Reveal
Single impactful number with context. 3-8 seconds.

```
[0.0s] Dark screen
[0.5s] Category label fades in (muted, uppercase, small)
[1.0s] Number scales up with spring (big, accent color, mono font)
[2.0s] Context line slides in from bottom
[3.0s] Logo fades in bottom-right
```

### 2. Tip / How-To (3-5 steps)
Educational content, one step per beat. 15-30 seconds.

```
[0-3s]   Hook text: bold question or statement (center, large)
[3-6s]   Step 1: number animates in + text slides right
[6-9s]   Step 2: same pattern
[9-12s]  Step 3: same pattern
[12-15s] CTA: "Follow for more" / logo
```

### 3. Before → After
Problem/solution comparison. 10-15 seconds.

```
[0-2s]  "Before" label + problem illustration (coral accents)
[2-5s]  Problem points appear one by one
[5-6s]  Transition: wipe or scale
[6-8s]  "After" label + solution (teal accents)
[8-11s] Solution points appear
[11-13s] CTA
```

### 4. Feature Spotlight
Single product feature demo. 8-15 seconds.

```
[0-2s]  Feature name (large, centered)
[2-4s]  Icon or minimal illustration animates in
[4-8s]  2-3 benefit points slide in
[8-10s] "Try it free" CTA + logo
```

### 5. Quote / Testimonial
Customer quote or founder insight. 5-10 seconds.

```
[0-1s]  Large quotation mark fades in (accent color)
[1-4s]  Quote text types in (typewriter effect)
[4-6s]  Attribution slides in (name, role)
[6-8s]  Logo + CTA
```

For Remotion code templates, see [references/remotion-templates.md](references/remotion-templates.md).
For animation style guide, see [references/animation-styles.md](references/animation-styles.md).

## Animation Principles

1. **Less is more** — max 3 elements moving at once
2. **Spring physics** — natural motion, no linear easing
3. **Stagger reveals** — elements appear sequentially, 200-400ms apart
4. **Consistent timing** — text stays readable for 2+ seconds
5. **Brand consistency** — always use brand colors and fonts
6. **Dark background** — navy `#0F1729`, never pure black
7. **Accent sparingly** — teal `#00D4AA` for emphasis only
8. **Safe zones** — keep text within 90px padding from edges (platform UI overlays)

## Workflow

1. **Content** — decide reel type and write copy (max 30 words per beat)
2. **Storyboard** — map timing: what appears at which second
3. **Build** — use Remotion template or movis script
4. **Preview** — `npx remotion preview` or render a test frame
5. **Render** — `npx remotion render src/index.ts ReelComp out/reel.mp4`
6. **Post** — upload to IG/TikTok/YT with caption from social-content skill

## Quick Start (Remotion)

```bash
# 1. Bootstrap project (one-time)
bash ~/.cursor/skills/social-reels-animator/scripts/setup.sh /path/to/project

# 2. Edit the composition in src/Reel.tsx

# 3. Preview
cd /path/to/project && npx remotion preview

# 4. Render
npx remotion render src/index.ts ReelComp out/reel.mp4 --codec h264
```

## Quick Start (Python / movis)

```python
import movis as mv

scene = mv.layer.Composition(size=(1080, 1920), duration=8.0)

bg = mv.layer.Rectangle(
    size=(1080, 1920),
    color=(15, 23, 41),  # #0F1729
    duration=8.0
)
scene.add_layer(bg)

title = mv.layer.Text(
    text="82% of SMBs fail\ndue to cash flow",
    font_family="Inter",
    font_size=72,
    font_weight=800,
    color=(0, 212, 170),  # #00D4AA
    duration=6.0,
)
title.transform.position.enable_motion().extend([0.0, 0.5], [(540, 1100), (540, 960)])
title.transform.opacity.enable_motion().extend([0.0, 0.5], [0.0, 1.0])
scene.add_layer(title, offset=1.0)

scene.write_video("reel.mp4")
```

## Related Skills

- **social-content** — copy, hooks, captions, scheduling
- **social-media-carousel** — static image carousels (complementary format)
- **landing-page-copywriter** — source copy for animation content
- **marketing-psychology** — persuasion principles for hooks
