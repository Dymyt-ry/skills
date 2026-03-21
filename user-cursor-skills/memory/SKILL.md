---
name: memory
description: |
  Persistent memory and knowledge management via Obsidian vault. Use when the user asks to remember, save, note, store information, recall something, search knowledge, or says "remember this", "save this", "note this down", "what did we find about", "write to vault". Also use proactively to save important research findings, decisions, and project context.
---

# Memory Agent

Read, write, and organize persistent knowledge in the local Obsidian vault.

## Vault: `~/Documents/Vault/`

```
~/Documents/Vault/
├── Business/       # WebFlex.cz — firma, produkty, procesy
├── Content/        # Content ideas, texty, calendar
├── Knowledge/      # Research, poznatky, zdroje
│   └── <topic>/    # Podslozky podle tematu
├── Leads/          # Zakaznici, potencialni klienti
└── .obsidian/      # Config (nemenil)
```

## Save Knowledge

Write .md files with frontmatter:

```markdown
---
created: YYYY-MM-DD
tags: [tag1, tag2]
source: url nebo kontext
---

# Nazev

Obsah v Markdown.
```

### Naming

- Lowercase kebab-case: `ai-code-assistants.md`
- Descriptive: `react-server-components.md` not `note1.md`
- Place in the right folder based on content type

### Where to Save

| Content Type | Path |
|-------------|------|
| Research findings | `Knowledge/<topic>/` |
| Competitor analysis | `Knowledge/<project>/competitors/` |
| Business info | `Business/` |
| Content ideas | `Content/` |
| Client/lead info | `Leads/YYYY-MM-DD-firma.md` |

## Recall / Search

```bash
# Search by content
rg "keyword" ~/Documents/Vault/ --type md

# Find by filename
find ~/Documents/Vault -name "*keyword*" -type f

# List a topic folder
ls ~/Documents/Vault/Knowledge/<topic>/
```

## Rules

- **Never overwrite** without reading first -- append or update
- **Always date** -- include `created:` in frontmatter
- **Use tags** -- Obsidian uses them for graph view
- **Link notes** -- use `[[note-name]]` wiki-link syntax
- **One topic per file** -- split large topics
- **Proactively save** when important decisions/findings emerge
