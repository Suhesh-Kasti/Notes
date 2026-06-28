---
category: dashboard
tags:
  - dashboard
  - dataview
created: 2025-06-18
---

# Cybersecurity Learning Dashboard

## Lab Progress

```dataview
TABLE platform, status, file.tags as Tags
FROM "Labs"
WHERE category = "lab"
SORT file.name ASC
```

## Bug Bounty Targets

```dataview
TABLE scope, status, platform
FROM "BugBounty"
SORT status ASC
```

## Vulnerability References

```dataview
TABLE file.tags as Tags
FROM "Knowledge"
WHERE contains(file.tags, "vuln/")
```

## Quick Links

- [[Labs/Pathway]] — master lab checklist
- [[Labs/Kanban]] — drag-and-drop Kanban board
- [[Knowledge/]] — all reference notes
- [[BugBounty/]] — all target writeups
