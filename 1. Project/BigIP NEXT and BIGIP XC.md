---
category:
  - BigIP
  - f5
  - WAF
tags:
  - architecture
  - component
  - ucs
published: false
date: 2024-07-22T11:16:00
excalidraw-plugin: parsed
excalidraw-open-md: true
---
**traffic-group-local-only:** self ip
**traffic-group-1:** floating ip
# Full proxy architecture
![[full_proxy.png]]
1. BigIP can modify various HTTP headers, data etc
2. The connection to BigIP can be secured with SSL and the connection to server can be unencrypted
3.  To reduce load on servers, the connection to BigIP can be compressed and the connection to server can be uncompressed
4. Different HTTP versions compatible with the web servers can be used in BigIP
# BigIP architecture
![[bigIparchi.png]]
# BigIP components
![[bigIpcomponent.png]]
**Process:**
![[bigIpsteps.png]]

# User configuration Set(UCS)
- Compressed archive
- Can be encrypted
- Can include or exclude public keys
- Can be downloaded
- Backups are stored in `/var/local/ucs`
- Contains configuration files, licenses, user account and passwords, SSL certs and keys
> We can goto System> Support> QKView snapshot for support and import the file into ihealth


# Day 2
# F5 Distributed Cloud

![[monolithic_microservices.png]]

Multicloud: Use multiple cloud providers as well as on-prem for sensitive stuffs


![[microservices_infra.png]]

1. Collaborate across teams with a centralized SaaS console to simplify planning and streamline execution

2. Automate network configs and security deployment to reduce effort, errors, and gaps in coverage

3. Advanced security filters out bad traffic before it hits customer networks, stays up to date

4. Full stack observability of network, security, and application performance, cloud-agnostic and exportable

![[what_f5_XC_is_solving.png]]

## API Security
Discover — Continuous detection of new/unknown APIs,
schema, characterization of data exposed, authentication
status and API vulnerabilities

Monitor — Continuous traffic inspection, analysis and
anomaly detection

Secure — Continuous enforcement of schemas, rate limiting,
and blocking of undesirable and malicious traffic

Customer Edge based solution -> Customer has more granular control over their traffic except metadata(Name of waf policies, name of WAF)

[OWASP API Top 10](https://owasp.org/API-Security/editions/2023/en/0x11-t10/)

| Shadow API                                                                 | Zombie API                                                                                                  |
| -------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| A shadow API is an unmanaged API that is actively being used               | A zombie API is an API that has been deprecated or abandoned.<br>Maybe used for test purposes.              |
| Shadow APIs are not necessarily APIs that are used for malicious purposes. | Zombie APIs may already be identified and managed by an organization, but they are not actively being used. |

1. 
Automatically learns the app API
surface

Using Al/ML, models are built to
baseline and track API behavior

For each API leaf, a model is built
for errors, latency, and request
metrics

Detect outliers and shadow APIs

Export swagger to improve API
definitions/update inventory

2. Discovery and validation of APIs
+ Discover and view
authentication status, details
and risk scoring for all API
endpoints

« Easily create protection rules
(e.g. Blocking, rate limiting
etc.)

3. Behavioral
Analysis of API
Endpoints

Monitor and baseline API
behavior continuously with
machine learning (ML) engine
Easily identify anomalies (e.g.,
spikes in request rates, latency,
response size, etc.)

Identify any PII in API
communications


![[Bot_defence_ML_BigIPXC.png]]


# WAF
False positive suppression engine

Cloud Scrubbing

Gartner Report

%%
# Excalidraw Data
## Text Elements
## Drawing
```compressed-json
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
```
%%