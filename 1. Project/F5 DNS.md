---
category:
  - f5
tags:
  - f5_dns
  - gtm
  - dns
published: false
date: 2024-11-05T12:26:00
excalidraw-plugin: parsed
excalidraw-open-md: true
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



%%
# Excalidraw Data
## Text Elements
## Drawing
```compressed-json
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=
```
%%