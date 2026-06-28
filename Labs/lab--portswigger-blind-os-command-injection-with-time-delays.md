---
category: lab
tags:
  - training/web
  - vuln/command-injection
platform: portswigger
status: todo
completed_date:
created: 2025-06-18
aliases:
  - "Blind OS command injection with time delays"
---
# Lab: Blind OS command injection with time delays

## Objective
*What is this lab trying to teach?*

## Why This Works (The Principle)
- **The vulnerability:** User input is passed to a system shell command without sanitization.
- **Root cause:** The application calls shell functions (e.g., `exec()`, `system()`, `popen()`) with attacker-controlled arguments.
- **Exploitation:** Inject command separators (`;`, `|`, `&`, `` ` ``) to execute additional commands.
- **Key insight:** Blind command injection still works — use time delays (`sleep`), out-of-band callbacks (`curl`), or output redirection to confirm.

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
