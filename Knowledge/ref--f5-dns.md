---
category: knowledge
tags:
  - dns
platform: n/a
status: done
created: 2026-06-17
aliases:
  - Decision Flow
---

# Decision Flow
We configure a listener on BigIP where the query arrives (*lets:10.1.20.20* )
1. Is there any Wide IP/ [[Fully Qualified Domain Name(FQDN) ]] configured against the query?
2. Is the name in DNS Express Zone? (AD DNS is configured as primary DNS server and F5 is configured as secondary where every entry is replicated to)
3. Checks on F5 DNS cache
4. Checks the master DNS cache which we assign in F5 DNS. Here, F5 will work as a recursive resolver. But, if resolving cache is not configured
5. Is there any pool attached to the listener
	Pool: We do not setup any secondary servers but rather when a DNS query is received at F5 we configure F5 to direct it to the AD DNS
	But if pool is not configured, then
6. In F5 DNS a local BIND DNS can be configured where it is checked next
7. Checks if listener is a Self-IP. If it is then the query fails and if not then the query is sent to that IP and the answer is cached

# Zone Transfer
Verify if DNS zone transfer is occured. To make F5 DNS make a DNS zone transfer request to already present primary DNS server we can simply *change the DNS express zone state to DISABLE and re-ENABLE again*
- dnsxdump
- tail -f "/var/log/ltm"
-
