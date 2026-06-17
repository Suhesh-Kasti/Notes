---
category: knowledge
tags:
  - dns
platform: n/a
status: done
created: 2026-06-17
aliases:
  - How DNSSEC works
---

Dig command for querying with DNSSEC
dig @server query +dnssec

# How DNSSEC works
## Resource Record SET (RRSET)
The first step towards securing a zone with DNSSEC is to group all the records with the same type into a resource record set (RRset). For example, if you have three AAAA records in your zone on the same label (i.e. label.example.com), they would all be bundled into a single AAAA RRset. published
![[images/rrset_Allocation.png]]

DNSSEC doesn't work on individual records but on sets of records thus the RRSETs.
## Zone-Signing Keys
Each zone in DNSSEC has a zone-signing key pair (ZSK): the private portion of the key digitally signs each RRset in the zone, while the public portion verifies the signature. To enable DNSSEC, a zone operator creates digital signatures for each RRset using the private ZSK and stores them in their name server as [RRSIG records](##RRSIG). This is like saying, “These are my DNS records, they come from my server, and they should look like this.”
## RRSIG
It stores the digital signature of RRSET using public and private keys
# The How
First we take the RRSET (Plain Text). We run it through signing process, which uses the private part of the ZSK to create a signature. This output, the signature is stored alongside the plain text RRSET using the same name with record type RRSIG.
Normal clients will only see teh RRSET whereas DNSSEC clients will see RRSIG as well
- If RRSET changes, RRSIG has to be regenerated in order to be valid
- If RRSET changes without corresponding change in RRSIG, the signature is considered invalid
![[images/howDNSSECworks.png]]

## How is RRSIG verified
