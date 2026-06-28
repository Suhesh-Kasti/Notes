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
  - "User ID controlled by request parameter with data leakage in redirect"
---
# Lab: User ID controlled by request parameter with data leakage in redirect

## Objective
This lab contains an access control vulnerability where sensitive information is leaked in the body of a redirect response.
To solve the lab, obtain the API key for the user `carlos` and submit it as the solution.
You can log in to your own account using the following credentials: `wiener:peter`

## Why This Works (The Principle)
- **The vulnerability:** The application uses user-supplied input (e.g., `id`, `user_id`, `uid`) to access resources without verifying ownership.
- **Root cause:** No server-side authorization check — the server trusts the client to provide a valid identifier.
- **Exploitation:** Modify the identifier to access another user's data.
- **Key insight:** IDOR is not about bypassing authentication; it is about bypassing authorization. Even authenticated users can exploit IDOR.

## Solution Reconstruction
- [ ] Step 1: Simple changed the id from my user to carlos 
![[information_exposed_in_302_redirection_found.png]]

## Key Takeaway
*Write ONE principle I must remember:*

## Next-Day Blind Replay
- [ ] Solved entirely from memory
- [ ] Needed to look at: *(write the specific step forgotten)*
