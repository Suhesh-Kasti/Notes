---
category: knowledge
tags:
  - reference
platform: n/a
status: done
created: 2026-06-17
aliases:
  - NTLM Authentication
---

# NTLM Authentication
It is a **challenge response mechanism**
1. User sends his username and password to the server
2. Server responds with a challenge
3. User responds with the challenge and response to the challenge
4. Server forwards the user sent challenge and response to the domain controller
5. Domain controller verifies the response from a database
6. If the response is valid, the domain controller tells the server to allow the user to access the service
7. If the reponse is invalid, the domain controller denies the user's request
# Kerberos Authentication
It is ticket based authentication method
