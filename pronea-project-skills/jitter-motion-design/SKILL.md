---
name: jitter-motion-design
description: Control and guide motion design workflows in Jitter (jitter.video) — a browser-based animation tool. Use when the user mentions Jitter, motion design, animating Figma designs, Lottie export, video animation, text animation, social media animation, or creating animated content. Covers design, animation, export, Figma import, AI features, and browser automation of the Jitter editor.
---

# Jitter Motion Design

Jitter is a fast, browser-based motion design tool at **https://jitter.video**. It replaces After Effects for most web/social animation work. No install — runs entirely in the browser.

## Core Concepts

- **Infinite canvas**: Multiple artboards (scenes) in one file — different sizes, formats, languages side by side
- **Action-based animation**: No keyframes. You tell layers what to do using In/Out/Custom actions
- **Figma-first workflow**: Import from Figma pixel-perfect via plugin, sync changes without losing animations
- **Timeline**: Horizontal bar-based, supports staggering, snapping, grouping — NOT traditional keyframe tracks

## Quick Workflow

1. **Design** → Import from Figma (plugin) or build directly in Jitter (shapes, text, images, video, SVG)
2. **Animate** → Apply In/Out presets or build custom actions. Use AI Brainstorm for quick drafts
3. **Export** → Video (MP4/MOV/WebM), GIF, Lottie, PNG frames. Up to 4K 120fps on Team plan

## Browser Automation

Jitter runs at `https://jitter.video/files/` (dashboard) and `https://jitter.video/editor/<file-id>` (editor). When automating via browser:

1. Navigate to `https://jitter.video` and ensure logged in
2. Open or create a file from the dashboard
3. Use the editor's UI panels:
   - **Left panel**: Layer list (reorder, group, hide, lock)
   - **Right sidebar**: Design tab (position, size, color, opacity, blend modes, fonts) and Animate tab (In/Out/Custom actions, easing, duration)
   - **Bottom**: Timeline (drag bars to adjust timing, stagger, snap)
   - **Top toolbar**: Tools (Selection, Text `T`, Rectangle `R`, Ellipse `O`, Pen), plus Undo/Redo, Zoom, Play

### Automation Tips

- Always `browser_snapshot` before interacting — the UI is dynamic
- Switch between **Design** and **Animate** tabs in the right sidebar (shortcut `M`)
- Play/pause with `Space`
- To apply animation: select layer → Animate tab → choose In or Out → pick preset → adjust timing on timeline
- Export: click Export button (top right) → select format → download

## Animation System

### Preset Categories

| Category | Purpose | Examples |
|----------|---------|---------|
| **In** | Entrance effects | Fade in, Slide in, Scale in, Blur in, Mask reveal |
| **Out** | Exit effects | Fade out, Slide out, Scale out, Blur out |
| **Custom** | Build from scratch | Combine move, rotate, scale, opacity, blur actions |

### Text Animation

Text can animate by **line**, **word**, or **letter**. Custom text effects (March 2026) let you define movement, rotation, scale, opacity, acceleration, duration — reusable across files.

### Easing Presets

Slow down, Accelerate, Elastic, Bounce, Overshoot — each with intensity slider. Custom easings are also supported and reusable across files.

### AI Features

- **AI Brainstorm**: Select artboard → click ✨ → choose mood (playful, bold, soft, elegant, cinematic) → generates editable animation draft
- **Image to Video**: Select image → Animate tab → Generate video. Supports custom prompts (March 2026)

## Figma → Jitter Pipeline

For Figma design context and assets, use the **implement-design** and **figma** skills (Figma MCP integration). The pipeline:

1. **Figma MCP**: Fetch design context (`get_design_context`) and screenshot (`get_screenshot`) for the target node
2. **Figma plugin**: Install [Jitter Figma plugin](https://www.figma.com/community/plugin/961270034818256057/jitter-animation-for-figma)
3. **Copy**: Select frame in Figma → Open plugin → Click **Copy**
4. **Paste into Jitter**: `Cmd+V` / `Ctrl+V` — pixel-perfect import
5. **Sync updates**: Edit in Figma → `Shift+Cmd+V` in Jitter (preserves all animations)

Also supports Figma Draw (patterns, brushes, variable strokes) and Figma Buzz plugins.

### Combined Workflow: Figma MCP + Jitter
When implementing animated UI from Figma:
1. Use `figma` skill to get design context and tokens
2. Use `implement-design` skill to build the static component in code
3. Import the same Figma frame into Jitter for animation
4. Export Lottie from Jitter → integrate into the coded component

## Export Reference

| Format | Free | Pro | Team |
|--------|------|-----|------|
| Video (MP4) | 720p 30fps | 1080p 60fps | 4K 120fps |
| GIF | Yes | Yes | Yes |
| Lottie | Yes | Yes | Yes |
| ProRes 4444 | — | — | Yes (transparent) |
| WebM | — | Yes | Yes (transparent) |
| PNG frames | — | — | Yes |

### Lottie Limitations

Lottie export does not support: text animations (use fade), mask animations (use fade), donuts/pies. All other vector animations export cleanly.

## Keyboard Shortcuts

See [reference.md](reference.md) for the complete shortcuts list. Key ones:

- `Space` — Play/Pause
- `T` — Text tool | `R` — Rectangle | `O` — Ellipse
- `M` — Toggle Design/Animate modes
- `Cmd+G` — Group | `Shift+Cmd+G` — Ungroup
- `,` `.` — Move time cursor ±10ms
- `Shift+,` `Shift+.` — ±100ms
- `←→↑↓` — Move element 1px | `Shift+arrows` — 10px

## Design Features

- **Blend modes**: Multiply, Screen, Overlay, etc. — in Design tab → Opacity section
- **Masks**: Vector and alpha masks (`Ctrl+Cmd+M`) — image reveals, gradient fades
- **Gradients**: Linear and radial, animatable — on fills and strokes
- **Blur**: Per-layer, animatable depth of field
- **Corner radius**: Per-element
- **Custom fonts**: Google Fonts or upload own
- **SVG import**: Sharp, scalable vectors
- **Media**: Images, GIFs, video, audio (with waveform visualization)
- **Curved paths**: Bezier-based motion paths
- **Formulas in fields**: Type `+10`, `*2`, `/2` in any numeric input

## Custom Animation Instructions

Beyond presets, Jitter's custom animation system uses **instructions** (not keyframes):

- **Move** — position X/Y (with optional Bezier curved paths)
- **Rotate** — angle
- **Resize** — width/height
- **Scale** — uniform or independent X/Y
- **Opacity** — 0–100%
- **Color** — fill transitions
- **Shadow** — animated shadows
- **Corner radius** — animated rounding
- **Stroke** — animated strokes and gradients on strokes
- **Arc** — animate ellipses, donuts, pie charts
- **Star** — animate spikes/thickness

Combine freely for complex branded animations. Each instruction has its own timing, easing, and delay.

## Additional Resources

- Full keyboard shortcuts and detailed features: [reference.md](reference.md)
- Step-by-step workflows: [workflows.md](workflows.md)
- Related skills: `implement-design` (Figma→code), `figma` (Figma MCP)
- Help Center: https://help.jitter.video/
- Changelog: https://jitter.video/changelog/
- Templates: https://jitter.video/templates/
- Video tutorials: https://youtu.be/toUrF4TH4JI (UI animation basics), https://youtu.be/UMIr2InlWpQ
