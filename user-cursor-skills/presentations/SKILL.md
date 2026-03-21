---
name: presentations
description: |
  Create AI presentations, slide decks, and documents. Use when the user asks to create a presentation, pitch deck, slide deck, slides, or says "make a presentation", "create slides", "pitch deck", "export as pptx/pdf". Supports two engines: Presenton (AI-powered, free, open-source, self-hosted or cloud) and Marp (markdown-to-slides, offline, zero dependencies).
---

# Presentations Agent

Generate polished presentations via **Presenton** (AI-powered) or **Marp CLI** (markdown-to-slides).

## Engine Selection

| Need | Use |
|------|-----|
| AI-generated content from a topic/prompt | Presenton |
| Full control over content (markdown) | Marp CLI |
| Offline, no Docker, no API | Marp CLI |
| Custom templates, branding | Presenton |
| Quick one-off slides from existing text | Marp CLI |

---

## Presenton (AI-Powered)

Free, open-source AI presentation generator. Self-hosted via Docker or use the cloud API.

### Setup — Self-Hosted (recommended)

```bash
docker run -it --name presenton -p 5000:80 \
  -e LLM="google" \
  -e GOOGLE_API_KEY="$GOOGLE_API_KEY" \
  -v "./app_data:/app_data" \
  ghcr.io/presenton/presenton:latest
```

Supports LLM providers: `openai`, `google`, `anthropic`, `ollama`, `custom` (OpenAI-compatible).

UI available at `http://localhost:5000`.

### Setup — Cloud API

1. Sign up at https://presenton.ai/auth/login
2. Get API key at https://presenton.ai/api-key (looks like `sk-presenton-xxxxx`)
3. Add to `~/.zshrc`: `export PRESENTON_API_KEY="sk-presenton-xxxxx"`

### Generate (Cloud API)

```bash
curl -s -X POST https://api.presenton.ai/api/v3/presentation/generate \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $PRESENTON_API_KEY" \
  -d '{
    "content": "Topic or outline here",
    "n_slides": 8,
    "language": "English",
    "standard_template": "general",
    "export_as": "pptx"
  }'
```

### Generate (Self-Hosted)

```bash
curl -s -X POST http://localhost:5000/api/v3/presentation/generate \
  -H "Content-Type: application/json" \
  -d '{
    "content": "Topic or outline here",
    "n_slides": 8,
    "language": "English",
    "standard_template": "general",
    "export_as": "pptx"
  }'
```

### Response

```json
{
  "presentation_id": "d3000f96-...",
  "path": "https://api.presenton.ai/static/user_data/.../file.pptx",
  "edit_path": "https://presenton.ai/presentation?id=d3000f96-...",
  "credits_consumed": 5
}
```

- `path` — download the PPTX/PDF
- `edit_path` — open in Presenton editor for manual tweaks

### Full Parameters

```json
{
  "content": "Topic or full text",
  "instructions": "Additional AI instructions",
  "n_slides": 8,
  "language": "English",
  "standard_template": "general",
  "tone": "professional",
  "verbosity": "standard",
  "web_search": false,
  "image_type": "ai-generated",
  "include_title_slide": true,
  "include_table_of_contents": false,
  "export_as": "pptx"
}
```

| Parameter | Values | Default |
|-----------|--------|---------|
| `tone` | `professional`, `educational`, `sales_pitch`, `casual`, `funny`, `default` | `default` |
| `verbosity` | `text-heavy`, `standard`, `concise` | `standard` |
| `image_type` | `ai-generated`, `stock` | `ai-generated` |
| `export_as` | `pptx`, `pdf` | `pptx` |
| `n_slides` | 1-50 | 8 |
| `web_search` | `true`, `false` | `false` |
| `standard_template` | `general`, `modern`, `swift`, etc. | `general` |

### Docker with Ollama (fully offline)

```bash
docker run -it --name presenton -p 5000:80 \
  -e LLM="ollama" \
  -e OLLAMA_MODEL="llama3.2:3b" \
  -e OLLAMA_URL="http://host.docker.internal:11434" \
  -e IMAGE_PROVIDER="pexels" \
  -e PEXELS_API_KEY="your_key" \
  -v "./app_data:/app_data" \
  ghcr.io/presenton/presenton:latest
```

### MCP Integration

Presenton has an MCP server at `/mcp` endpoint:
- Cloud: `https://api.presenton.ai/mcp`
- Self-hosted: `http://localhost:5000/mcp`
- Protocol: Streamable HTTP (not stdio)
- Tool: `generate_presentation` (accepts `content`, `instructions`)

---

## Marp CLI (Markdown to Slides)

Free, open-source, offline. Write Markdown, get slides.

### Install

```bash
brew install marp-cli
```

Or without install: `npx @marp-team/marp-cli@latest`

### Markdown Format

```markdown
---
marp: true
theme: default
paginate: true
---

# Slide 1 Title

Content here

---

# Slide 2 Title

- Bullet point
- Another point

![bg right](https://example.com/image.jpg)

---

# Slide 3

| Column A | Column B |
|----------|----------|
| Data 1   | Data 2   |
```

Each `---` separator creates a new slide.

### Convert

```bash
marp slides.md                    # -> HTML
marp slides.md --pdf              # -> PDF
marp slides.md --pptx             # -> PowerPoint
marp slides.md --images png       # -> PNG per slide
marp slides.md -o output.pptx     # custom output name
```

### Themes

Built-in: `default`, `gaia`, `uncover`

```markdown
---
marp: true
theme: gaia
class: lead
---
```

### Background Images

```markdown
![bg](image.jpg)           <!-- full background -->
![bg left](image.jpg)      <!-- left split -->
![bg right:40%](image.jpg) <!-- right 40% -->
![bg contain](image.jpg)   <!-- contain -->
![bg blur](image.jpg)      <!-- blurred background -->
```

### Styling

```markdown
---
marp: true
style: |
  section {
    background-color: #1a1a2e;
    color: #eaeaea;
  }
  h1 { color: #e94560; }
---
```

### Watch Mode

```bash
marp -w slides.md    # auto-rebuild on changes
marp -s slides.md    # start dev server with live reload
```

---

## Workflow

### AI-powered (Presenton)

1. Understand the topic/content from user
2. Call Presenton API with appropriate params
3. Download the file from `path` in response
4. Share `edit_path` for manual edits if needed

### Markdown-based (Marp)

1. Write slides in Markdown (use `---` as separators)
2. Save as `.md` file in project
3. Convert with `marp slides.md --pptx`
4. Deliver the output file

## Autonomy

**Run freely:** generate presentations, convert markdown, list templates.
**Ask first:** sharing externally, large slide counts (>30), Docker operations.

## Docs

- Presenton: https://docs.presenton.ai/
- Presenton GitHub: https://github.com/presenton/presenton
- Marp: https://marp.app/
- Marp CLI: https://github.com/marp-team/marp-cli
