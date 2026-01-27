---
category: 
tags: 
published: false
date: ""
excalidraw-plugin: parsed
excalidraw-open-md: true
---
# Positive security model
1. Positive: Only allow positive(good) request and block all other
   eg. allowed filetypes, allowed url, allowed parameter and allowed responses
2. Negative: Allow all traffic except known negative(bad) request
   eg. attack signatures, malware hidden behind legitimate traffic, data guard
# Policy Templates
1. Rapid
   - Minimal configuration
   - Relies on negative security
   - Learning mode - Manual
   - Enforcement mode - Transparent
   - 
1. Fundamental 




# Security policy
1. Transparent - Do not block let traffic pass and learn 
2. Blocking - Blocks request if the policy is attached
# Signature 
1. Learn - Appears in traffic learning page
2. Alarm - Appears in event log if policy is in transparent. If security policy is in blocking the alarm will be generated even if alarm flag is not ticked 
3. Block - Block requests belonging to selected signature sets
## Signature sets
1. Staging - This signature set is learning and will not block anything
2. Enforced - Block traffic from this signature set

Slide 1: Introduction to F5 BIG-IP WAF

- Definition: Advanced web application firewall solution
- Purpose: Protects web applications from various attacks
- Key features: Security policies, learning mode, templates, attack signatures

Slide 2: Security Policies

- Customizable rule sets for application protection
- Define allowed and blocked traffic
- Combine multiple security features
- Tailored to specific application needs

Slide 3: Positive Security Model

- Whitelist approach: explicitly defines allowed traffic
- Blocks everything not specifically allowed
- Highly effective against unknown threats
- Requires thorough understanding of application

Slide 4: Negative Security Model

- Blacklist approach: explicitly defines and blocks known malicious traffic
- Allows everything not specifically blocked
- Easier to implement and maintain
- Effective against known threats

Slide 5: Learning Mode

- Observes traffic patterns without blocking
- Suggests policy adjustments based on observed behavior
- Helps fine-tune security policies
- Reduces false positives and improves accuracy

Slide 6: Rapid Deployment with Templates

- Pre-configured security policy templates
- Fundamental: Basic protection for common web attacks
- Comprehensive: Advanced protection for complex applications
- Rapid deployment: Quick start with industry best practices

Slide 7: Staging vs. Enforced Mode

- Staging: Test policies without affecting traffic
- Enforced: Actively block threats based on defined policies
- Gradual transition from staging to enforced
- Ensures policy effectiveness before full implementation

Slide 8: DataGuard

- Prevents data leakage
- Masks sensitive information (e.g., credit card numbers, SSNs)
- Customizable data patterns
- Helps maintain compliance (PCI DSS, HIPAA)

Slide 9: Attack Signatures

- Pre-defined patterns to identify known threats
- Regular updates from F5 Labs
- Customizable signatures for specific applications
- Protects against OWASP Top 10 and emerging threats

Slide 10: Signature Sets

- Grouped attack signatures for specific protection needs
- Examples: SQL injection, cross-site scripting (XSS), remote file inclusion
- Can be enabled/disabled as sets or individually
- Allows for granular control of threat detection

Slide 11: SSL Offloading and Certificates

- Terminates SSL/TLS connections at the WAF
- Reduces load on backend servers
- Centralized certificate management
- Enables inspection of encrypted traffic

Slide 12: Exceptions and Whitelisting

- Create exceptions for specific URLs, parameters, or IP addresses
- Whitelist trusted sources
- Customize rules for unique application requirements
- Balance security and functionality

Slide 13: Geolocation and Bot Protection

- Geolocation-based access control
- Bot detection and mitigation
- Protects against automated attacks and content scraping
- Customizable bot detection methods

Slide 14: API Protection

- Secures APIs against specific threats
- Schema validation
- Access control and rate limiting
- Protects against API-specific attacks (e.g., parameter tampering)

Slide 15: Reporting and Integration

- Comprehensive logging and reporting capabilities
- Integration with SIEM systems
- Real-time threat analytics
- Integration with other F5 security solutions

Presentation Script:

Slide 1: Welcome to our presentation on F5 BIG-IP Web Application Firewall, or WAF. Today, we'll explore this advanced security solution designed to protect web applications from various attacks. We'll cover key features and concepts crucial to understanding and implementing this powerful tool.

Slide 2: Let's start with security policies. These are customizable rule sets that define how the WAF protects your applications. You can specify allowed and blocked traffic, combining multiple security features to create a tailored defense for your specific application needs.

Slide 3: The positive security model is a whitelist approach that explicitly defines allowed traffic and blocks everything else. This model is highly effective against unknown threats but requires a thorough understanding of your application.

Slide 4: In contrast, the negative security model is a blacklist approach that explicitly defines and blocks known malicious traffic. It's easier to implement and maintain, making it effective against known threats.

Slide 5: One of the most powerful features of F5 BIG-IP WAF is its learning mode. This observes traffic patterns without blocking, suggesting policy adjustments based on observed behavior. This helps fine-tune security policies, reducing false positives and improving overall accuracy.

Slide 6: F5 offers rapid deployment options through pre-configured templates. These include fundamental templates for basic protection against common web attacks, and comprehensive templates for more advanced protection of complex applications. These templates allow for quick implementation of industry best practices.

Slide 7: The WAF operates in two primary modes: staging and enforced. Staging mode allows you to test policies without affecting traffic, while enforced mode actively blocks threats based on defined policies. This allows for a gradual transition, ensuring policy effectiveness before full implementation.

Slide 8: DataGuard is a crucial feature that prevents data leakage. It can mask sensitive information like credit card numbers or social security numbers. This feature is customizable and helps maintain compliance with regulations like PCI DSS and HIPAA.

Slide 9: Attack signatures are pre-defined patterns that identify known threats. F5 Labs regularly updates these signatures, and they can be customized for specific applications. This feature protects against OWASP Top 10 vulnerabilities and emerging threats.

Slide 10: Signature sets are grouped attack signatures for specific protection needs. Examples include sets for SQL injection, cross-site scripting, and remote file inclusion. These can be enabled or disabled as sets or individually, allowing for granular control of threat detection.

Slide 11: SSL offloading and certificate management are key capabilities of the WAF. It can terminate SSL/TLS connections, reducing load on backend servers. This also allows for centralized certificate management and enables inspection of encrypted traffic.

Slide 12: Exceptions and whitelisting provide flexibility in policy enforcement. You can create exceptions for specific URLs, parameters, or IP addresses, and whitelist trusted sources. This allows you to balance security needs with application functionality.

Slide 13: Geolocation and bot protection features allow you to control access based on geographic location and protect against automated attacks. This includes customizable bot detection methods to prevent content scraping and other malicious bot activities.

Slide 14: API protection is a critical feature in today's application landscape. The WAF provides specific protections for APIs, including schema validation, access control, rate limiting, and defenses against API-specific attacks like parameter tampering.

Slide 15: Finally, let's touch on reporting and integration capabilities. The WAF offers comprehensive logging and reporting, integration with SIEM systems, real-time threat analytics, and seamless integration with other F5 security solutions. These features provide valuable insights and enhance your overall security posture.


%%
# Excalidraw Data
## Text Elements
%%
## Drawing
```compressed-json
N4KAkARALgngDgUwgLgAQQQDwMYEMA2AlgCYBOuA7hADTgQBuCpAzoQPYB2KqATLZMzYBXUtiRoIACyhQ4zZAHoFAc0JRJQgEYA6bGwC2CgF7N6hbEcK4OCtptbErHALRY8RMpWdx8Q1TdIEfARcZgRmBShcZQUebTiADho6IIR9BA4oZm4AbXAwUDAiiBJuCAAxAEYeAFEAGSEAaQAlTShiAC0ASQBrAHkAYQoARyFiADZkoshYRDKAM0CETyp+

YsxuHgB2AGZtLYBWNcgYbmcdhK3jiAoSdW4ABm0Hl8rryQRCZWlH59fr6zKYKPa7MKCkNg9BADNj4NikMoAYkqCBRKKmxU0uGwPWUEKEHGIMLhCIk4OszDguECmQxkHmhHw+AAyrBgRJBB46RAwRCoQB1O6STag8GQhCsmDs9Cc0rXfHfDjhbJoN75SBsKnYNSnVUva544RwLrEFWoHIAXWui1w6RN3A4QiZ10IhKwZVwD25+MJSuYZsdzvVPIQy

24lUOCQALJUdgdKuNrowWOwuGgjsHk6xOAA5ThiTZRqM7ACcWwjfGDhGYABFUlAw2hwUIENdNMJCTVgulMgGnfhrkI4MRcA3iOGtjxYwl41txlGHmrphAiBweg7+9c4TjG6h5gQwtc4GxXVlcuqwHlpkUHscbxerRer9eni9F3ewK/Xg/1Y/l3BAn9ERwlyP9ilYfQnVHBAAAVAOYYDuGbVtg3wUIoBhfR9DUMcYJPWk0GfG8/nfC8v0XX98gAXz

WQpilKCQhB4DpnAAQXGYZWNwHgowAITEGBmQACQADWcGoAH1uVmcR0EWUMVm5DY0C2BJxn2DNl11VBnCjA4EmuW5iHuNByKXYoPi+H5TJI8zIEBaVb2DXlxWJeEkTRVEkDbbFcR9IlYXcslyA4SlqQyKBuQZJlJWlHlYTlZyxQFIURSSvkJTZWT4q5eVhEVZVw2uTVsR1cN9WDQ0hxNM1LWtcg7XHNBAwHKs3WU9BcEqb0O2IP0+yDZcwl3HgHhL

KNxhLA4Sx4pMmGzNNUE04os1TPMOALNAdkqB4EkqGddpdWt613ZC216rs0gigbWuXIcRzHCcpwueMEh2csdi3V112azdULYHcmr3A8UP/fCz0Ip8L0/D8HgfO8iOIt87KR79rwtX8j3g4DarAgRCEgtCGzg5VEKbUgWy3dDMOwmRljw09zxfWy7zMyiiio8A/wgXA4DgVloO4OjoA+dIyiIb5IrWBhCAQCheN8qrCTc0l0EReYNc1jEIGwEQaSgL

oG30VkMpVjyvPRaXddIfXDbSBWcSVgKSTKclQqpfXtet22jfKRkWSyspZXHK29Yiu3jeShBBWM4U0ErYpvfDo2TfFWLsuDr2w8yCPmnyyR+qK/Idezg2jb6LUyr1JzE9LiPyk4KByltRltPMkubeTtIG8yZlCCMWTRtDzuc6NgAVLAoFYiXFpXBB5il4uk9HtIBdIKebbYCgPlwIGWuHn20hqQlWM37eQiBnmz+15hsAhJkRO4VT1MOaXb/v/AAE

1uAmgzi6MNgBghaZgIC2cM1ED5d30HnAkfVCoSH8trPEJA+4Dw3INSAyDnZBVQHRSAvFYSX0RAMEsJCSHlHKNyZoCBlBQVVhARENQaxMKYRQiAECl6l1TlCCuUBUw3WlgBBAZhhDMAAOKkBQf3WS+9i42nSNQt0kiODKGAcuDIuBNDBCBmdYM2AiBwCQhTUGxQOC2lkro5cwgoCrgscYjhxQ7AACsEDYCyMyMxcAACybBiAIGPpo7R3B9z4DCOAG

idBoogTQMATmVEgA
```
%%