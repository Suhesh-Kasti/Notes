---
category: lab
tags:
  - training/web
  - vuln/nosql
platform: portswigger
status: todo
completed_date:
created: 2025-06-18
aliases:
  - "Detecting NoSQL injection"
---
# Lab: Detecting NoSQL injection

## Objective
*What is this lab trying to teach?*

## Why This Works (The Principle)
- **The vulnerability:** User input is passed to a NoSQL query (e.g., MongoDB) without proper type checking or sanitization.
- **Root cause:** NoSQL databases accept operators (`$ne`, `$gt`, `$regex`) in query parameters — the application passes URL parameters directly.
- **Exploitation:** Submit JSON or URL-encoded operators to subvert the query logic.
- **Key insight:** NoSQL injection is logic subversion — `{"username": "admin", "password": {"$ne": ""}}` bypasses password checks by making the condition always true.

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
