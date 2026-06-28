---
category: lab
tags:
  - training/web
  - vuln/path-traversal
platform: portswigger
status: todo
completed_date:
created: 2025-06-18
aliases:
  - "File path traversal, traversal sequences stripped non-recursively"
---
# Lab: File path traversal, traversal sequences stripped non-recursively

## Objective
*What is this lab trying to teach?*

## Why This Works (The Principle)
- **The vulnerability:** The application reads files based on user-supplied path without proper validation.
- **Root cause:** The server constructs a file path by concatenating a base directory with user input.
- **Exploitation:** Use `../` sequences to navigate outside the intended directory, or absolute paths to bypass prefix checks.
- **Key insight:** Path traversal is about file system navigation — each `../` moves one directory up. Filters can be bypassed by encoding, stripping tricks, or absolute paths.

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
