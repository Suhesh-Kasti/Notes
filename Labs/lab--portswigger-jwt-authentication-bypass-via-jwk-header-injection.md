---
category: lab
tags:
  - training/web
  - vuln/jwt
platform: portswigger
status: todo
completed_date:
created: 2025-06-18
aliases:
  - "JWT authentication bypass via jwk header injection"
---
# Lab: JWT authentication bypass via jwk header injection

## Objective
*What is this lab trying to teach?*

## Why This Works (The Principle)
- **The vulnerability:** The server trusts the JWT without verifying its signature, uses a weak secret, or misconfigures the algorithm.
- **Root cause:** The JWT library/implementation has a flaw — algorithm confusion (`alg: none`), weak HMAC secret, or signing key injection (`jwk`, `jku`, `kid`).
- **Exploitation:** Forge a valid JWT by either setting `alg: none`, cracking the secret, or injecting a crafted key into the header.
- **Key insight:** A JWT is only as secure as its verification logic. If the server trusts the header's algorithm choice, it can be subverted.

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
