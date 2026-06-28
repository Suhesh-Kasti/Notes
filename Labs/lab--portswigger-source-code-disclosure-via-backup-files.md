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
  - "Source code disclosure via backup files"
---
# Lab: Source code disclosure via backup files

## Objective
This lab leaks its source code via backup files in a hidden directory. To solve the lab, identify and submit the database password, which is hard-coded in the leaked source code.

## Why This Works (The Principle)
- **The vulnerability:** The application reveals sensitive information through error messages, debug pages, backup files, or version control history.
- **Root cause:** These endpoints/files are unintentionally exposed to unauthenticated or unauthorized users.
- **Exploitation:** Request the vulnerable endpoint to retrieve hidden data.
- **Key insight:** Information disclosure is rarely the end goal — it is a stepping stone to a bigger attack (e.g., finding credentials, API keys, or internal paths).

## Solution Reconstruction
*After viewing full solution, close it immediately.*
- [ ] Step 1: i just simply went to /backup
- [ ] Step 2:
![[backup_folder_found.png]]
- [ ] Step 3: Inside was the source code which had the database password
## Key Takeaway
Always look in source code and fuzz directories

## Next-Day Blind Replay
- [ ] Solved entirely from memory
- [ ] Needed to look at: *(write the specific step forgotten)*
