---
category: lab
tags:
  - training/web
  - vuln/xss
platform: portswigger
status: todo
completed_date:
created: 2025-06-18
aliases:
  - "Stored XSS into HTML context with nothing encoded"
---
# Lab: Stored XSS into HTML context with nothing encoded

## Objective
This lab contains a stored cross-site scripting vulnerability in the comment functionality.
To solve this lab, submit a comment that calls the `alert` function when the blog post is viewed.

## Why This Works (The Principle)
- **The vulnerability:** User-supplied input is embedded into a web page without proper escaping, allowing arbitrary JavaScript execution.
- **Root cause:** The application outputs attacker-controlled data into an HTML context, attribute, or JavaScript context without sanitization.
- **Exploitation:** Inject a payload that escapes the current context (e.g., `>` to break out of an HTML tag, `"` to break out of an attribute).
- **Key insight:** XSS is context-dependent — the same payload will not work in every injection point. Always identify the context first.

## Solution Reconstruction
- [ ] Final payload / exploit: Opened the site, went to a comment and in a comment section simply wrote the payload `<script>alert(1)</script>` 

## Key Takeaway
*Write ONE principle I must remember:*

## Next-Day Blind Replay
- [ ] Solved entirely from memory
- [ ] Needed to look at: *(write the specific step forgotten)*
