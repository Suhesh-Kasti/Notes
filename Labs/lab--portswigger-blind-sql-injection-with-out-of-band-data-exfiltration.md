---
category: lab
tags:
  - training/web
  - vuln/sqli
platform: portswigger
status: todo
completed_date:
created: 2025-06-18
aliases:
  - "Blind SQL injection with out-of-band data exfiltration"
---
# Lab: Blind SQL injection with out-of-band data exfiltration

## Objective
*What is this lab trying to teach?*

## Why This Works (The Principle)
- **The vulnerability:** User input is concatenated into a SQL query without parameterization.
- **Root cause:** The application builds SQL statements by joining strings with user input.
- **Exploitation:** Break out of the query context (using `'`, `"`, or `)`) and inject SQL syntax to modify the query logic.
- **Key insight:** SQL injection is about changing the structure of a query, not just selecting extra data — it can subvert WHERE clauses, UNION in extra results, or exfiltrate data blind.

## Blind Attempt (15-20 min max)
*Try without any hints. Document everything.*
- **What I tried:**
- **Where I got stuck:**

## Hint Usage (if needed)
- [ ] Used lab hint
- [ ] Watched first 30s of video solution
- *Resume blind with new clue. Still stuck?*

## Solution Reconstruction
*After viewing full solution, close it immediately.*
- [ ] Step 1:
- [ ] Step 2:
- [ ] Step 3:
- [ ] Final payload / exploit:

## Key Takeaway
*Write ONE principle I must remember:*

## Next-Day Blind Replay
- [ ] Solved entirely from memory
- [ ] Needed to look at: *(write the specific step forgotten)*
