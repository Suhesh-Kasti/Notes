---
category: lab
tags:
  - training/web
  - vuln/idor
platform: portswigger
status: todo
completed_date:
created: 2025-06-18
aliases:
  - "Insecure direct object references"
---
# Lab: Insecure direct object references

## Objective
This lab stores user chat logs directly on the server's file system, and retrieves them using static URLs.
Solve the lab by finding the password for the user `carlos`, and logging into their account.

## Why This Works (The Principle)
- **The vulnerability:** The application uses user-supplied input (e.g., `id`, `user_id`, `uid`) to access resources without verifying ownership.
- **Root cause:** No server-side authorization check — the server trusts the client to provide a valid identifier.
- **Exploitation:** Modify the identifier to access another user's data.
- **Key insight:** IDOR is not about bypassing authentication; it is about bypassing authorization. Even authenticated users can exploit IDOR.

## Solution Reconstruction
- [ ] Step 1: The site had a live chat feature that had the option to download the chat transcript 
- [ ] Step 2: When i downloaded my chat transcript, it did that through `/download-transcript/2.txt`
- [ ] Step 3: Changed the location to `/download-transcript/1.txt` which downloaded the 1.txt transcript stored statically in server
![[chat_transcript_stored_statically.png]]
## Key Takeaway
*Write ONE principle I must remember:*
## Next-Day Blind Replay
- [ ] Solved entirely from memory
- [ ] Needed to look at: *(write the specific step forgotten)*
