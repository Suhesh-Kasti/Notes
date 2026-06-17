---
category: dashboard
tags:
  - dashboard
  - dataview
created: 2026-06-17
---

# Cybersecurity Learning Dashboard

## Lab Progress

```dataview
TABLE platform, status, tags
FROM "Labs"
WHERE category = "lab"
SORT status ASC
```

## Bug Bounty Targets

```dataview
TABLE scope, status, platform
FROM "BugBounty"
SORT status ASC
```

## Vulnerability References

```dataview
TABLE file.tags as "Tags"
FROM "Knowledge"
WHERE contains(file.tags, "vuln/")
```

## Quick Links

- [[Labs/]] — all lab writeups
- [[Knowledge/]] — all reference notes
- [[BugBounty/]] — all target writeups
- [[Kanban]] — lab Kanban board
