# skills

Private mirror of **Cursor Agent Skills** collected from this machine: global `~/.cursor/skills`, global `~/.agents/skills`, Cursor meta-skills (`~/.cursor/skills-cursor`), project skills under **Pronea** (`.agents/skills` and `.cursor/skills`).

Each skill is a folder that should contain a root **`SKILL.md`** (YAML frontmatter + instructions). Some bundles also include `references/`, `scripts/`, or `evals/`.

## Layout

| Directory | Source on disk | Role |
|-----------|----------------|------|
| `user-cursor-skills/` | `~/.cursor/skills/` | General-purpose skills (marketing, dev, audio, research, …) |
| `cursor-meta-skills/` | `~/.cursor/skills-cursor/` | Cursor tooling: create-skill, create-rule, settings, subagents |
| `pronea-agents-skills/` | `Pronea/.agents/skills/` | Social, pitch, paperclip, video, ads, etc. |
| `pronea-project-skills/` | `Pronea/.cursor/skills/` | **spndr**-specific brand / graphics / reels |
| `user-agents-skills/` | `~/.agents/skills/` | Extra agent skills not mirrored under `user-cursor-skills` / `pronea-*` (design, Obsidian, video tooling, …) |

**Duplicates:** The same skill name can appear in `user-cursor-skills` and `pronea-agents-skills` (e.g. `social-content`, `paperclip`). They may differ slightly — compare before merging.

## Quick inventory

- **`user-cursor-skills`** (32): ai-music-generation, ai-video-generation, base44-cli, builder, compose-outreach, designing-beautiful-websites, elevenlabs-music, elevenlabs-sound-effects, elevenlabs-sound-effects-official, elevenlabs-tts, framer-motion-animator, landing-page-copywriter, landing-page-design, marketing-ideas, marketing-psychology, memory, nextjs-app-router-patterns, paperclip, paperclip-ai-orchestration, paperclip-create-agent, presentations, product-marketing-context, researcher, scrapling, social-content, social-media-carousel, social-media-post-maker, social-reels-animator, studio, telegram-remote, ui-ux-pro-max, web-design-guidelines  

- **`cursor-meta-skills`** (6): create-rule, create-skill, create-subagent, migrate-to-skills, shell, update-cursor-settings  

- **`pronea-agents-skills`** (32): ads-copywriter, ai-avatar-video, ai-content-pipeline, ai-image-generation, ai-video-generation, canvas-design, content-research-writer, content-strategy, copywriter, document-pptx, explainer-video-guide, paperclip, paperclip-ai-orchestration, paperclip-create-agent, pitch-deck, pitch-deck-visuals, playwright-recording, post-bridge, postproxy, presentation-pitch-deck, realistic-ugc-video, screenshot, script-writer, social-content, social-media-carousel, social-media-management, social-publisher, text-to-speech, tiktok-captions, tiktok-marketing, video-prompting-guide, video-script  

- **`pronea-project-skills`** (4): jitter-motion-design, spndr-brand, spndr-graphics-agent, spndr-reels  

- **`user-agents-skills`** (34): 3d-visualizer, ai-slides, blitzreels-video-editing, brand-guidelines, chart-designer, chart-visualization, copy-editing, deep-research-pro, design-system, figma-design, figma-ui-skills, find-skills, frontend-design-system, google-material-design, html-slides, infographic, md-slides, obsidian, obsidian-master-skill, obsidian-vault-management, page-transitions, parallel-deep-research, ppt-visual, pptx-manipulation, presentation-builder, refero-design, remotion-best-practices, software-ui-ux-design, tailwindcss-animations, ui-ux-design-pro, video-edit, video-editing, video-processing-editing, videoagent-video-studio  

## Upstream mapping (subset)

Some skills from the Pronea agents tree were installed from GitHub; see **`provenance-skills-lock.json`** for `owner/repo` and content hashes (as recorded in the Pronea project).

## Use in Cursor

1. Copy one skill folder into your project, e.g. `.cursor/skills/<name>/`, **or** into `~/.cursor/skills/<name>/` for all projects.  
2. Ensure `SKILL.md` is at the skill root.  
3. Refresh / reopen the project so Cursor picks up the skill.

## License / attribution

Skills come from **multiple third-party repositories** and local edits. Respect each upstream license when redistributing; this repo is a **private convenience bundle** for one team.

## Refreshing this bundle (maintainer)

From a machine that has the same paths:

```bash
EXPORT=/path/to/skills   # this repo root
rsync -a --exclude node_modules --exclude .git ~/.cursor/skills/ "$EXPORT/user-cursor-skills/"
rsync -a --exclude node_modules --exclude .git ~/.cursor/skills-cursor/ "$EXPORT/cursor-meta-skills/"
rsync -a --exclude node_modules --exclude .git /path/to/Pronea/.agents/skills/ "$EXPORT/pronea-agents-skills/"
rsync -a --exclude node_modules --exclude .git /path/to/Pronea/.cursor/skills/ "$EXPORT/pronea-project-skills/"
# Optional: sync global agent skills (copy only skills you want; or rsync whole tree and prune duplicates)
rsync -a --exclude node_modules --exclude .git ~/.agents/skills/ "$EXPORT/user-agents-skills/"
```

Then commit and push.
