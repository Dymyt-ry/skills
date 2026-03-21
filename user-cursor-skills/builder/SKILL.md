---
name: builder
description: |
  Skill discovery, installation, and creation agent. Use when the user asks to find a skill, install a skill, create a new skill, manage skills, or when a task would benefit from a specialized skill that isn't installed yet. Also triggers on "find skill for", "install skill", "create skill", "npx skills", "add capability".
---

# Builder Agent

Find, install, create, and manage Cursor agent skills.

## Skill Locations

| Type | Path |
|------|------|
| Personal skills | `~/.cursor/skills/<name>/` |
| Project skills | `.cursor/skills/<name>/` |
| Built-in (read-only) | `~/.cursor/skills-cursor/` |

## Find Skills

### 1. npx skills (preferred)

```bash
npx skills find <query>                          # Search by keyword
npx skills add <owner/repo> --list               # List skills in a repo
```

Browse: https://skills.sh/

### 2. GitHub search

```bash
# Use WebSearch
WebSearch: "SKILL.md" <topic> site:github.com
```

### Known Registries

- `vercel-labs/agent-skills` -- React, Next.js, web design
- `anthropics/skills` -- Frontend design, document processing
- `tavily-ai/skills` -- Web search/research
- `teng-lin/notebooklm-py` -- NotebookLM automation
- `D4vinci/Scrapling` -- Web scraping

## Install Skills

```bash
# From GitHub via npx (auto-detects Cursor)
npx skills add <owner/repo> -a cursor -g -y

# Specific skill from a repo
npx skills add <owner/repo> --skill <name> -a cursor -g -y

# Manual: clone + copy
git clone https://github.com/<owner>/<repo> /tmp/<repo>
mkdir -p ~/.cursor/skills/<name>/
cp /tmp/<repo>/SKILL.md ~/.cursor/skills/<name>/SKILL.md
cp -r /tmp/<repo>/references/ ~/.cursor/skills/<name>/references/ 2>/dev/null
rm -rf /tmp/<repo>
```

## Create Skills

Template for `~/.cursor/skills/<name>/SKILL.md`:

```markdown
---
name: <name>
description: |
  <What it does>. Use when <triggers>.
---

# <Title>

## Setup
<Install steps>

## Quick Reference
<Commands/patterns>
```

Rules:
- name: max 64 chars, lowercase, hyphens
- description: specific, third-person, includes WHAT and WHEN
- Body: under 500 lines, concise
- Put detailed docs in `references/` subdirectory

## Manage Skills

```bash
ls ~/.cursor/skills/                    # List installed
npx skills check                        # Check for updates
npx skills update                       # Update all
rm -rf ~/.cursor/skills/<name>/         # Remove
```

## Proactive Behavior

When encountering a task that could benefit from a skill:
1. Check `ls ~/.cursor/skills/`
2. Search with `npx skills find <topic>`
3. If found, offer to install
4. If not found, offer to create one
