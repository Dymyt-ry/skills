---
name: telegram-remote
description: |
  Remote control via Telegram using Cursor Autopilot extension. At the end of every chat turn, write a JSON summary to ./tmp/ so the extension can push it to Telegram. The user can then reply from Telegram to continue the session. Always follow the summary rule.
---

# Telegram Remote Control

The Cursor Autopilot extension bridges this agent with Telegram. At the end of every chat turn, a summary is written to `./tmp/` which the extension picks up and sends to Telegram.

## How It Works

1. Agent completes a task
2. Agent writes a JSON summary to `./tmp/summary-<timestamp>.json`
3. Extension detects the file and sends it to Telegram
4. User replies in Telegram: `1` = continue, or custom text = new instructions
5. Extension injects the reply back into Cursor chat

## Summary Format

At the end of every chat turn, write:

```bash
mkdir -p tmp
```

Then create a JSON file:

```json
{
  "summary": "One-paragraph recap of this chat turn (decisions, blockers, next steps)",
  "current_status": "Brief snapshot of overall project progress"
}
```

Save to: `tmp/summary-YYYYMMDD-HHmmss.json`

## Configuration

File: `.autopilot.json` in project root.

```json
{
  "enabled": true,
  "adapters": ["telegram"],
  "telegram": {
    "token": "<bot-token>",
    "chatId": "<user-id>"
  }
}
```

## Telegram Bot

- Bot Token: configured in `.autopilot.json`
- User ID: configured in `.autopilot.json`

## User Replies

| Reply | Action |
|-------|--------|
| `1` | Continue with current task |
| Any text | Send as new instructions to the agent |
