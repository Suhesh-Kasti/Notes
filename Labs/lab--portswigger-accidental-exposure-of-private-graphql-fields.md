---
category: lab
tags:
  - training/web
  - vuln/graphql
platform: portswigger
status: todo
completed_date:
created: 2025-06-18
aliases:
  - "Accidental exposure of private GraphQL fields"
---
# Lab: Accidental exposure of private GraphQL fields

## Objective
*What is this lab trying to teach?*

## Why This Works (The Principle)
- **The vulnerability:** The GraphQL endpoint exposes more data or functionality than intended.
- **Root cause:** Introspection is enabled (leaking schema), authorization checks are missing on specific queries, or brute-force protections are absent.
- **Exploitation:** Query introspection to discover hidden fields, craft batched queries to brute-force, or access private resources directly.
- **Key insight:** GraphQL is a single endpoint — security depends on schema design and resolver-level authorization, not endpoint-level access control.

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
