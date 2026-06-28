---
category: lab
tags:
  - training/web
  - vuln/ssti
platform: portswigger
status: todo
completed_date:
created: 2025-06-18
aliases:
  - "Server-side template injection using documentation"
---
# Lab: Server-side template injection using documentation

## Objective
*What is this lab trying to teach?*

## Why This Works (The Principle)
- **The vulnerability:** User input is embedded into a server-side template without sanitization.
- **Root cause:** The application passes user input to a template engine (e.g., Jinja2, Freemarker, Twig) which evaluates it as code.
- **Exploitation:** Inject template syntax (`{{ }}`, `${ }`, `<%= %>`) to execute code on the server.
- **Key insight:** SSTI is not XSS — it runs on the server, not the client. Confirming the template engine is the first step; then look up its specific syntax.

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
