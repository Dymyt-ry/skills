---
name: spndr-reels
description: Create on-brand AI-generated reels and short-form videos for spndr (AI finance agent). Covers scripting, AI video generation, voiceover, avatar lipsync, motion graphics, and assembly into Reels/TikTok/Shorts. Uses inference.sh CLI, Jitter, and browser canvas. Triggers include "reel", "reels", "short video", "TikTok", "YouTube Shorts", "video content", "spndr video", "spndr reel", "motion", "animate post", "video ad", "promo video", "explainer reel", "product demo video", "talking head", "avatar video".
---

# spndr Reels Agent

You create on-brand AI-generated reels and short-form videos for **spndr** — the AI finance agent for high-income professionals.

## Brand Quick Reference

| | |
|---|---|
| **Background** | `#0a0a0a` (primary), `#080808` (alt) |
| **Accent** | `#f97316` (orange) — CTAs, numbers, highlights, the dot in `spndr.` |
| **Text** | `#ffffff` (headings), `#f0f0f0` (body), `#cccccc` (subtitles), `#999999` (muted) |
| **Font** | System sans-serif, weight 900 headings, 400 body |
| **Watermark** | `spndr.` with orange dot — present in every video |

For full brand assets see `branding/spndr-branding-guide.md` and `branding/spndr-brand/`.

## Video Specs

| Platform | Dimensions | Duration | Format |
|----------|-----------|----------|--------|
| Instagram Reels | 1080 x 1920 (9:16) | 15-90s | MP4 |
| TikTok | 1080 x 1920 (9:16) | 15-60s | MP4 |
| YouTube Shorts | 1080 x 1920 (9:16) | 15-60s | MP4 |
| LinkedIn Video | 1080 x 1350 (4:5) or 1080 x 1920 | 30-120s | MP4 |

Default to **1080 x 1920 (9:16)** unless specified.

## Reel Types

### 1. Hook Reel (15-30s)
Fast-cut attention-grabber. Bold text + lifestyle footage + orange accents.
- 0-3s: Hook text on dark bg with kinetic type
- 3-15s: 2-3 quick scenes proving the hook
- 15-20s: `spndr.` brand reveal + CTA
- Last frame: logo hold (2s)

### 2. Explainer Reel (30-60s)
Problem → Agitate → Solve using the PAS formula.
- 0-3s: Hook (problem question)
- 3-12s: Agitate (show pain, stats)
- 12-30s: Solution (spndr demo/features, 3 quick steps)
- 30-35s: Social proof stat
- 35-40s: CTA with logo

### 3. Feature Spotlight (15-30s)
Single-feature deep dive. Clean motion graphics on dark bg.
- 0-3s: Surprising stat or question
- 3-20s: Feature demo with text overlays
- 20-25s: Outcome/benefit
- 25-30s: CTA

### 4. Avatar / Talking Head (30-90s)
AI-generated presenter delivering a finance tip.
- Generate portrait still → lipsync with OmniHuman or Fabric
- Lower-third: `spndr.` branding bar + speaker name
- B-roll cuts every 8-12s to maintain attention

### 5. Trending Format Reel (15-30s)
Adapt trending audio/formats to spndr messaging.
- Match trending structure but use spndr hooks and colors
- Always end with branded CTA frame

## Production Pipeline

### Step 1: Script

Write the script first. Rules:
- Max 150 words for 60s (2.5 words/sec)
- Short sentences (max 12 words)
- Active voice, conversational tone
- One idea per scene
- Start with the hook — no preamble

Use hooks from [hooks.md](hooks.md).

### Step 2: Generate Visuals

Choose the right model based on scene needs:

```bash
# Cinematic lifestyle footage (highest quality)
infsh app run google/veo-3-1-fast --input '{
  "prompt": "Cinematic close-up, person checking phone with glowing finance dashboard, dark moody lighting, orange accent glow from screen, shallow depth of field, 9:16 vertical format"
}'

# Fast/economical drafts
infsh app run pruna/p-video --input '{
  "prompt": "Abstract data visualization, flowing orange particles on dark background, finance aesthetic, smooth motion, vertical 9:16"
}'

# Animate a still image (brand visual → video)
infsh app run falai/wan-2-5-i2v --input '{
  "prompt": "Subtle camera push in, soft ambient light shift, gentle parallax",
  "image": "branding/Branding/AI Visuals - Website _ Landing Page/visual.png"
}'
```

**Prompt formula for spndr scenes:**
`[Camera movement], [subject], [environment], dark moody lighting with orange accent glow, professional fintech aesthetic, cinematic depth of field, 9:16 vertical`

See [prompts.md](prompts.md) for pre-built prompt library.

### Step 3: Generate Voiceover

```bash
infsh app run falai/dia-tts --input '{
  "prompt": "[S1] Your script here. Keep it conversational... punchy. One idea per sentence."
}'
```

Pacing control: `.` = medium pause, `...` = dramatic pause, `,` = short pause.

### Step 4: Generate Avatar (if needed)

```bash
# AI talking head from portrait + voiceover
infsh app run bytedance/omnihuman-1-5 --input '{
  "image_url": "portrait.jpg",
  "audio_url": "voiceover.mp3"
}'

# Or lipsync on existing image
infsh app run falai/fabric-1-0 --input '{
  "image_url": "face.jpg",
  "audio_url": "voiceover.mp3"
}'
```

### Step 5: Assemble

```bash
# Merge scenes
infsh app run infsh/media-merger --input '{
  "media": ["hook-scene.mp4", "feature-scene.mp4", "cta-scene.mp4"],
  "transition": "cut"
}'

# Add voiceover to merged video
infsh app run infsh/video-audio-merger --input '{
  "video": "merged.mp4",
  "audio": "voiceover.mp3"
}'

# Add captions (85% of social video watched muted)
infsh app run infsh/caption-videos --input '{
  "video": "final.mp4",
  "caption_file": "captions.srt"
}'
```

### Step 6: Add Sound Effects (optional)

```bash
infsh app run infsh/hunyuanvideo-foley --input '{
  "video_url": "final.mp4",
  "prompt": "subtle tech UI sounds, soft whoosh transitions, ambient electronic"
}'
```

### Step 7: Upscale (optional)

```bash
infsh app run falai/topaz-video-upscaler --input '{"video_url": "final.mp4"}'
```

## Text Overlay Frames

For title cards, stat screens, and CTAs, render HTML via browser canvas then convert to video:

```html
<div style="width:1080px;height:1920px;background:#0a0a0a;font-family:system-ui,-apple-system,sans-serif;color:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;position:relative">
  <div style="font-size:96px;font-weight:900;line-height:1.05;letter-spacing:-0.03em;padding:0 60px">
    Stop guessing.<br>Start <span style="color:#f97316">knowing.</span>
  </div>
  <p style="font-size:28px;color:#ccc;margin-top:24px">Your finances deserve AI.</p>
  <div style="position:absolute;bottom:80px;font-size:24px;color:#999;font-weight:900;letter-spacing:-0.05em">spndr<span style="color:#f97316">.</span></div>
</div>
```

Animate text overlays in **Jitter** for kinetic typography (see jitter-motion-design skill).

## Motion Graphics via Jitter

For polished text animations and transitions:
1. Build text frames in Jitter at 1080x1920
2. Apply In/Out presets (Fade in, Slide in, Scale in)
3. Use custom text animation (by word or letter) for kinetic type
4. Export MP4 at 1080p 60fps
5. Merge with AI-generated footage via media-merger

## Brand Checklist

Before publishing any reel:
- [ ] Background `#0a0a0a` (not lighter, not pure black)
- [ ] Orange accent exactly `#f97316`
- [ ] `spndr.` watermark visible (with orange dot)
- [ ] Captions present (for silent viewing)
- [ ] Hook in first 3 seconds
- [ ] One core message per reel
- [ ] CTA in final 3-5 seconds
- [ ] 9:16 aspect ratio
- [ ] Audio mixed: music -6 to -12dB under voice

## Content Pillars

| Pillar | % | Reel Ideas |
|--------|---|------------|
| Financial insights | 30% | "3 subscriptions draining your account", tax tip of the week |
| Product value | 25% | Feature demo, "watch spndr find $2K in savings" |
| Social proof | 20% | Stats animation, before/after scenarios |
| Lifestyle | 15% | "day in the life" of someone who tracks vs doesn't |
| Direct CTA | 10% | App walkthrough, "try free today" |

## Related Skills

- **spndr-graphics-agent**: Static social posts and carousels
- **ai-video-generation**: Full model catalog for video generation
- **p-video**: Fast/economical Pruna video models
- **explainer-video-guide**: Script formulas and assembly pipeline
- **video-prompting-guide**: Prompt engineering for video models
- **ai-image-generation**: Generate stills for image-to-video
- **ai-avatar-video**: Talking head / lipsync generation
- **text-to-speech**: Voiceover generation
- **jitter-motion-design**: Motion graphics and text animation
- **social-content**: Hook formulas and content strategy
- **social-media-carousel**: Carousel structure (adapt for reel storyboards)
