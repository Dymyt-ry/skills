---
name: studio
description: |
  Content generation via Google NotebookLM. Use when the user wants to create a podcast, generate a quiz, make flashcards, produce a video, create a report, build a slide deck, generate an infographic or mind map, or says "notebooklm", "create podcast about", "generate quiz", "turn into audio", "make flashcards", "summarize these documents".
---

# Studio Agent

Generate rich content (podcasts, videos, quizzes, reports) via NotebookLM CLI.

## Auth

```
CLI: ~/.local/bin/notebooklm
Auth: ~/.notebooklm/storage_state.json
Login script: ~/.local/share/uv/tools/scrapling/bin/python /tmp/nblogin_stealth.py
```

If auth fails, re-run the login script (uses Patchright stealth browser).

## Quick Reference

| Task | Command |
|------|---------|
| List notebooks | `notebooklm list` |
| Create | `notebooklm create "Title"` |
| Set context | `notebooklm use <id>` |
| Add source | `notebooklm source add "url-or-file"` |
| Chat | `notebooklm ask "question"` |
| Generate podcast | `notebooklm generate audio "instructions"` |
| Generate video | `notebooklm generate video "instructions"` |
| Generate quiz | `notebooklm generate quiz` |
| Generate flashcards | `notebooklm generate flashcards` |
| Generate report | `notebooklm generate report --format briefing-doc` |
| Generate slides | `notebooklm generate slide-deck` |
| Generate mind map | `notebooklm generate mind-map` |
| Download | `notebooklm download <type> ./output` |

## Generation Types

| Type | Formats | Output | Time |
|------|---------|--------|------|
| Audio | deep-dive, brief, critique, debate | .mp3 | 10-20 min |
| Video | explainer, brief; 9 styles | .mp4 | 15-45 min |
| Slides | detailed, presenter | .pdf/.pptx | 5-15 min |
| Infographic | landscape/portrait/square | .png | 5-15 min |
| Report | briefing-doc, study-guide, blog-post | .md | 5-15 min |
| Quiz | easy/medium/hard | .json/.md | 5-15 min |
| Flashcards | easy/medium/hard | .json/.md | 5-15 min |
| Mind Map | instant | .json | instant |
| Data Table | custom description | .csv | 5-15 min |

## Standard Workflow

1. `notebooklm create "Topic"` -- create notebook
2. `notebooklm source add "url"` -- add sources (repeat)
3. `notebooklm source list --json` -- wait for status=READY
4. `notebooklm generate <type> "instructions" --json` -- generate
5. `notebooklm artifact wait <id>` -- wait for completion
6. `notebooklm download <type> ./output` -- download result

## Autonomy

**Run freely:** list, create, source add, source list, ask, status, use.
**Ask first:** delete, generate (long-running), download (writes files).

## Errors

| Error | Fix |
|-------|-----|
| Auth expired | Run login script |
| No context | `notebooklm use <id>` |
| Rate limit | Wait 5-10 min, retry |
| Generation failed | `notebooklm artifact list`, retry |
