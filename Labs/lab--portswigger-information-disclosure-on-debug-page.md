---
category: lab
tags:
  - training/web
  - vuln/information-disclosure
platform: portswigger
status: todo
completed_date:
created: 2025-06-18
aliases:
  - "Information disclosure on debug page"
---
# Lab: Information disclosure on debug page

## Objective
This lab contains a debug page that discloses sensitive information about the application. To solve the lab, obtain and submit the `SECRET_KEY` environment variable.

## Why This Works (The Principle)
- **The vulnerability:** The application reveals sensitive information through error messages, debug pages, backup files, or version control history.
- **Root cause:** These endpoints/files are unintentionally exposed to unauthenticated or unauthorized users.
- **Exploitation:** Request the vulnerable endpoint to retrieve hidden data.
- **Key insight:** Information disclosure is rarely the end goal — it is a stepping stone to a bigger attack (e.g., finding credentials, API keys, or internal paths).

## Solution Reconstruction
- [ ] Step 1: used intruder to fire up directory scan using seclists' raft directories wordlist
- [ ] Step 2: the scan found cgi-bin/ 
- [ ] Step 3: cgi-bin/ had phpinfo.php file searching inside of which SECRET_KEY was found
## Key Takeaway
Always look out for debug pages / default pages

## Next-Day Blind Replay
- [ ] Solved entirely from memory
- [ ] Needed to look at: *(write the specific step forgotten)*
