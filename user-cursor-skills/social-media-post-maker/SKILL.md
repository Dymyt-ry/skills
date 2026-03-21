---
name: social-media-post-maker
description: "Create social media posts (carousels, stat cards, singles) for spndr — the AI Finance Agent. Generates slides via infsh CLI, writes captions, and follows spndr brand guidelines. Use when asked to 'create posts', 'make carousel', 'social media content', 'Instagram post', 'IG content', 'spndr post', or any social content creation for spndr."
---

# Social Media Post Maker (spndr)

Create on-brand social media posts for **spndr** — AI Finance Agent for the US B2C market.

## Brand Quick Reference

- **Domain:** spndr.dev (NEVER spndr.app)
- **Colors:** bg `#0a0a0a`, accent orange `#f97316`, white `#ffffff` text
- **Typography:** system sans-serif, weight 900 headings, 400 body
- **Watermark:** `spndr.` (orange dot) on every slide, bottom-left
- **Target:** US millennials (28-43) & Gen Z (18-27)
- **Tone:** Confident, slightly sassy, relatable, no corporate jargon
- **Content mix:** 80% entertainment/education, 20% product (Cleo-inspired)

For full brand spec, see [brand-context.md](brand-context.md).

## Workflow

### 1. Determine post type

| Type | Format | When |
|------|--------|------|
| **Carousel** | 4-7 slides, 1080x1350px (4:5) | Educational, how-to, storytelling |
| **Single** | 1 slide, 1080x1350px (4:5) | Stat cards, quotes, brand intros |
| **Stat card** | 1 slide, bold number | Shocking statistics, data points |

### 2. Write copy first

Before generating visuals, draft:
- **Hook** (slide 1 / caption first line) — use formulas from `social-content` skill
- **Body slides** — one point per slide, max 30 words
- **CTA slide** — always end with spndr.dev
- **Caption** — hook + 2-3 sentences + hashtags + CTA

### 3. Generate slides via infsh

```bash
infsh app run infsh/html-to-image --input '{
  "html": "<YOUR_HTML_HERE>"
}'
```

#### Hook slide template

```html
<div style="width:1080px;height:1350px;background:#0a0a0a;display:flex;align-items:center;justify-content:center;padding:80px;font-family:system-ui,-apple-system,sans-serif;color:white;text-align:center;position:relative">
  <div style="position:absolute;top:40px;right:40px;font-size:18px;color:#999">1 / N</div>
  <div>
    <h1 style="font-size:64px;font-weight:900;line-height:1.15;margin:0;letter-spacing:-1px">HOOK TEXT HERE</h1>
    <p style="font-size:24px;color:#999;margin-top:32px">Swipe →</p>
  </div>
  <div style="position:absolute;bottom:40px;left:40px;font-size:20px;font-weight:900;color:white;letter-spacing:-0.5px">spndr<span style="color:#f97316">.</span></div>
</div>
```

#### Content slide template

```html
<div style="width:1080px;height:1350px;background:#0a0a0a;padding:80px;font-family:system-ui,-apple-system,sans-serif;color:white;display:flex;flex-direction:column;justify-content:center;position:relative">
  <div style="position:absolute;top:40px;right:40px;font-size:18px;color:#999">N / N</div>
  <p style="font-size:100px;font-weight:900;color:#f97316;margin:0;line-height:1">01</p>
  <h2 style="font-size:48px;font-weight:800;margin:24px 0 16px;line-height:1.2;letter-spacing:-0.5px">Headline</h2>
  <p style="font-size:26px;color:#cccccc;line-height:1.6;margin:0">Body text here. Keep it short and punchy.</p>
  <div style="position:absolute;bottom:40px;left:40px;font-size:20px;font-weight:900;color:white;letter-spacing:-0.5px">spndr<span style="color:#f97316">.</span></div>
</div>
```

#### Stat card template

```html
<div style="width:1080px;height:1350px;background:#0a0a0a;display:flex;align-items:center;justify-content:center;padding:80px;font-family:system-ui,-apple-system,sans-serif;color:white;text-align:center;position:relative">
  <div>
    <p style="font-size:140px;font-weight:900;color:#f97316;margin:0;line-height:1">$1,200</p>
    <p style="font-size:28px;color:#cccccc;margin-top:24px;line-height:1.5;max-width:700px">The average American wastes this much on forgotten subscriptions every year.</p>
  </div>
  <div style="position:absolute;bottom:40px;left:40px;font-size:20px;font-weight:900;color:white;letter-spacing:-0.5px">spndr<span style="color:#f97316">.</span></div>
</div>
```

#### CTA slide template

```html
<div style="width:1080px;height:1350px;background:#0a0a0a;display:flex;align-items:center;justify-content:center;padding:80px;font-family:system-ui,-apple-system,sans-serif;color:white;text-align:center;position:relative">
  <div>
    <h2 style="font-size:56px;font-weight:900;margin:0;line-height:1.2;letter-spacing:-1px">Stop guessing.<br>Start knowing.</h2>
    <p style="font-size:28px;color:#f97316;margin-top:32px;font-weight:700">spndr.dev</p>
    <p style="font-size:22px;color:#999;margin-top:16px">Free forever. No credit card.</p>
  </div>
  <div style="position:absolute;bottom:40px;left:40px;font-size:20px;font-weight:900;color:white;letter-spacing:-0.5px">spndr<span style="color:#f97316">.</span></div>
</div>
```

### 4. Batch generation

```bash
#!/bin/bash
SLIDES=("slide1.html" "slide2.html" "slide3.html")
for slide in "${SLIDES[@]}"; do
  infsh app run infsh/html-to-image --input "{\"html\": \"$(cat $slide)\"}"
done
```

## Caption Structure

```
[HOOK — first line that stops the scroll]

[BODY — 2-3 sentences expanding on the hook. Use line breaks.]

[CTA — "Link in bio" or "Try it free at spndr.dev"]

.
.
.
#personalfinance #fintech #moneymanagement #ai #budgeting
#spndr #moneytips #financialfreedom #savemoney #budgetingtips
```

## Content Pillars (for spndr)

| Pillar | % | Topics |
|--------|---|--------|
| Financial education | 35% | Tips, stats, myths, "did you know" |
| Product personality | 25% | Roast mode, AI chat examples, sassy takes |
| Pain points | 20% | Subscription waste, budgeting struggles, bank app complaints |
| Product showcase | 15% | Features, how it works, before/after |
| Social proof | 5% | Testimonials, milestones, user stories |

## Messaging Bank

- Hero: "Money talks. spndr talks back."
- CTA: "Stop guessing. Start knowing."
- Personality: "Your bank app shows you numbers. spndr gives you answers."
- Roast: "spndr: the financial advisor that roasts you into saving money."
- Stats: 12,000+ banks, 60s onboarding, $0 free tier, AI-powered
- Features: natural language queries, subscription detection, proactive alerts, roast/hype mode

## Design Rules

- Dark bg `#0a0a0a` — ALWAYS (brand identity)
- Orange `#f97316` for: numbers, CTAs, accent elements, the dot in `spndr.`
- White `#ffffff` for headings
- `#cccccc` for body text
- `#999999` for captions and metadata
- `spndr.` watermark bottom-left on EVERY slide
- Slide counter top-right on carousels (e.g., "1 / 5")
- "Swipe →" on hook slides
- No custom fonts — system sans-serif only
- 1080x1350px (4:5) for maximum IG feed real estate

## Related Skills

- `social-content` — strategy, engagement, analytics, platform guides
- `social-media-carousel` — carousel psychology, batch generation
- `marketing-psychology` — persuasion, hooks, behavioral triggers
- `landing-page-copywriter` — copy frameworks (PAS, AIDA)

## Reference Material

- [brand-context.md](brand-context.md) — full brand spec
- [post-ideas.md](post-ideas.md) — 20+ ready-to-use post concepts
- Google Drive visuals: https://drive.google.com/drive/folders/14Hdt1JYRHG_yg5p02-EuoDkrPUvnnDKF
- Existing posts: https://drive.google.com/drive/folders/1YAHev2OAzu8d-cbVE3H1gSXvDgTJTNKI
