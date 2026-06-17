---
category: bugbounty
tags:
  - bounty/target
platform: bugcrowd
scope: 
status: active
created: {{date}}
---

# {{title}}

## Scope
- Wildcard: 
- In-scope URLs: 
- Out of scope: 

## Recon Checklist
- [ ] Subdomain enumeration (Subfinder, Amass, crt.sh)
- [ ] Port scanning (naabu, nmap)
- [ ] Technology stack identification (Wappalyzer, WhatWeb)
- [ ] Wayback Machine / gau / hakrawler endpoint discovery
- [ ] GitHub dorking and exposed secrets
- [ ] Parameter mining (Arjun, x8, ParamSpider)

## Application Mapping
*Browse the target with Burp and map every endpoint.*
- [ ] Authentication flow (login, register, password reset, 2FA)
- [ ] Core business logic features
- [ ] User roles and privilege levels
- [ ] API endpoints (REST, GraphQL)
- [ ] File upload / image handling functions
- [ ] Search and filter functionality

## Parameter Checklist
*For every parameter discovered, test systematically.*
- [ ] IDOR / UUID manipulation
- [ ] SQLi ( ' , " , -- , ; , boolean, time-based)
- [ ] NoSQLi ( $ne, $gt, $regex )
- [ ] XSS ( <>", ', \`, ${}, {{}} )
- [ ] SSTI ( {{7*7}}, ${7*7}, <%= 7*7 %> )
- [ ] Command injection ( ; , | , & , \` )
- [ ] Path traversal ( ../../../etc/passwd )
- [ ] File inclusion (LFI/RFI)
- [ ] SSRF (webhooks, internal IPs, metadata endpoints)
- [ ] Open redirect
- [ ] CSRF (token presence, SameSite)
- [ ] Rate limiting / brute force
- [ ] Mass assignment
- [ ] Insecure deserialization
- [ ] JWT attacks (none algorithm, key confusion)
- [ ] Cache poisoning / deception

## Findings Log
| Vulnerability | Endpoint | Parameter | Severity | Status |
| --- | --- | --- | --- | --- |
| | | | | |

## Active Leads
- [ ]
