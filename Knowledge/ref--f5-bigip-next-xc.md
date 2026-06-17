---
category: knowledge
tags:
  - f5
platform: n/a
status: done
created: 2026-06-17
aliases:
  - Full proxy architecture
---

**traffic-group-local-only:** self ip
**traffic-group-1:** floating ip
# Full proxy architecture
![[images/full_proxy.png]]
1. BigIP can modify various HTTP headers, data etc
2. The connection to BigIP can be secured with SSL and the connection to server can be unencrypted
3.  To reduce load on servers, the connection to BigIP can be compressed and the connection to server can be uncompressed
4. Different HTTP versions compatible with the web servers can be used in BigIP
# BigIP architecture
![[images/bigIparchi.png]]
# BigIP components
![[images/bigIpcomponent.png]]
**Process:**
![[images/bigIpsteps.png]]

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

![[images/monolithic_microservices.png]]

Multicloud: Use multiple cloud providers as well as on-prem for sensitive stuffs


![[images/microservices_infra.png]]

1. Collaborate across teams with a centralized SaaS console to simplify planning and streamline execution

2. Automate network configs and security deployment to reduce effort, errors, and gaps in coverage

3. Advanced security filters out bad traffic before it hits customer networks, stays up to date

4. Full stack observability of network, security, and application performance, cloud-agnostic and exportable

![[images/what_f5_XC_is_solving.png]]

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


![[images/Bot_defence_ML_BigIPXC.png]]


# WAF
False positive suppression engine

Cloud Scrubbing

Gartner Report
