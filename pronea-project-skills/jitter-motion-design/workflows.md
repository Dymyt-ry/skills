# Jitter Workflows

## 0. Figma MCP → Jitter → Code (Full Pipeline)

For animated UI components that need both code and motion:

```
Progress:
- [ ] Fetch Figma design context (figma skill)
- [ ] Build static component in code (implement-design skill)
- [ ] Import Figma frame into Jitter
- [ ] Animate in Jitter
- [ ] Export Lottie
- [ ] Integrate Lottie into coded component
```

### Steps

1. **Figma MCP**: Use `get_design_context` and `get_screenshot` to understand layout, tokens, typography
2. **Implement static**: Use `implement-design` skill workflow to build the component in project's framework
3. **Import to Jitter**: Copy the same Figma frame via plugin → paste in Jitter
4. **Animate**: Apply entrance/exit effects, micro-interactions, transitions
5. **Export Lottie**: Vector-only animations → export as Lottie JSON
6. **Integrate**: Add `<lottie-player>` or use `lottie-web` in the coded component

```html
<script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>
<lottie-player src="animation.json" background="transparent" speed="1" loop autoplay></lottie-player>
```

---

## 1. Figma → Jitter → Export (Standard Workflow)

```
Progress:
- [ ] Install Figma plugin
- [ ] Select and copy frames in Figma
- [ ] Paste into Jitter
- [ ] Apply animations
- [ ] Adjust timing on timeline
- [ ] Export
```

### Steps

1. **Figma plugin**: Install from [Figma Community](https://www.figma.com/community/plugin/961270034818256057/jitter-animation-for-figma)
2. **Copy**: Select frame(s) in Figma → Open plugin → Click **Copy**
3. **Paste**: In Jitter editor → `Cmd+V` (creates pixel-perfect layers)
4. **Animate**: Select layer → Right sidebar **Animate** tab → Choose In/Out preset or Custom
5. **Timeline**: Drag bars to adjust start time and duration, use staggering for sequences
6. **Export**: Click **Export** (top right) → Choose format → Download

### Sync Updates from Figma
If you change design in Figma after animating in Jitter:
1. Re-copy in Figma plugin
2. In Jitter: `Shift+Cmd+V` — updates layers, keeps all animations intact

---

## 2. Social Media Animation

### Instagram Post (4:5)
1. Create new file → Set artboard to **1080×1350** (4:5 preset)
2. Design or import content
3. Animate with bold entrance effects (Scale in + text stagger)
4. Keep total duration 3–6 seconds for engagement
5. Export as **MP4** (for Reels/Stories) or **GIF** (for static post with motion)

### Instagram Story / Reel (9:16)
1. Artboard: **1080×1920**
2. Use full vertical space, large text
3. Duration: 5–15s for stories, up to 60s for reels
4. Export as **MP4**

### LinkedIn Post (1:1 or 4:5)
1. Artboard: **1080×1080** or **1080×1350**
2. Professional easing (Slow down), clean transitions
3. Duration: 5–15s
4. Export as **MP4** or **GIF**

### Twitter/X (16:9)
1. Artboard: **1920×1080**
2. Snappy animations, keep under 2:20 for auto-play
3. Export as **MP4** or **GIF** (GIF max ~15MB for Twitter)

---

## 3. Logo Animation

```
Progress:
- [ ] Import logo (SVG preferred)
- [ ] Separate logo into layers (icon, wordmark, tagline)
- [ ] Animate each part with stagger
- [ ] Add easing
- [ ] Export
```

1. **Import**: SVG for best quality. Or copy from Figma
2. **Layer separation**: Ungroup (`Shift+Cmd+G`) to access individual parts
3. **Animate**:
   - Icon: Scale in + Overshoot easing
   - Wordmark: Slide in from left, letter-by-letter stagger
   - Tagline: Fade in with delay after wordmark
4. **Timeline**: Stagger each group's entrance by 200–400ms
5. **Export**: Lottie for web, MP4 for social, GIF for email signatures

---

## 4. Product UI Animation / Prototyping

1. Design screens in Figma → Import to Jitter
2. Animate transitions: screen slides, element reveals, micro-interactions
3. Use **Mask reveal** for content appearing, **Blur in** for depth focus
4. For button states: use **Click Animation** (select element → Custom action)
5. Export Lottie for developer handoff, or MP4 for stakeholder review

---

## 5. AI-Assisted Animation

### Quick Draft with AI Brainstorm
1. Import/design your static content
2. Click ✨ icon on artboard → Select mood
3. Review generated animation
4. Refine: adjust timing, swap presets, modify easing

### Image to Video
1. Select image layer
2. Animate tab → **Generate video**
3. Click "View and edit prompt" to customize motion description
4. Generated video replaces static image — adjust on timeline

---

## 6. Multi-Format Production (Infinite Canvas)

When you need the same animation in multiple sizes:

1. Create first artboard at primary size
2. Design and animate
3. Duplicate artboard on the infinite canvas (`Cmd+D`)
4. Resize duplicate to target format (e.g., 1080×1080 → 1080×1920)
5. Adjust layout for new aspect ratio — animations carry over
6. Export each artboard separately

---

## 7. Lottie for Web

```
Progress:
- [ ] Create animation (vector-only, no video/audio)
- [ ] Verify Lottie compatibility
- [ ] Export as Lottie
- [ ] Implement in code
```

### Design Constraints for Lottie
- Use only vector shapes, text (without text animation), solid colors, gradients
- Avoid: video layers, audio, animated masks, text-specific animations
- Use fade in/out instead of text animations for Lottie compatibility

### Export
1. Click Export → Select **Lottie**
2. Choose FPS (30 recommended for web)
3. Download `.json` file

### Implementation
```html
<script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>
<lottie-player src="animation.json" background="transparent" speed="1" loop autoplay></lottie-player>
```

---

## 8. Browser Automation Workflow

When controlling Jitter via browser automation (browser-use):

### Login and Navigate
```
1. browser_navigate → https://jitter.video
2. browser_snapshot → check if logged in
3. If not logged in → click Log in → authenticate
4. browser_navigate → https://jitter.video/files/ (dashboard)
```

### Create New File
```
1. browser_snapshot → find "New file" or "+" button
2. browser_click → create new file
3. Wait 2s → browser_snapshot → verify editor loaded
```

### Apply Animation to Layer
```
1. browser_snapshot → identify layer in layer list or canvas
2. browser_click → select the layer
3. browser_snapshot → find Animate tab in right sidebar
4. browser_click → switch to Animate tab
5. browser_snapshot → find animation presets (In/Out/Custom)
6. browser_click → select desired preset category (e.g., "In")
7. browser_click → select specific preset (e.g., "Fade in")
8. browser_snapshot → verify animation applied on timeline
```

### Export
```
1. browser_snapshot → find Export button (top right)
2. browser_click → Export button
3. Wait 2s → browser_snapshot → export options page
4. Select format, resolution, FPS
5. browser_click → Download/Export
6. Wait for render → browser_snapshot to check progress
```

### Tips
- Always snapshot before and after each interaction
- Use short incremental waits (1–3s) between actions
- The editor is highly dynamic — element refs change after interactions
- Timeline bars can be dragged — use browser_click + browser_drag for timing adjustments
- Layer list supports drag-reorder for z-ordering
