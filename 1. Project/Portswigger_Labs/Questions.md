---
category:
  - Portswigger_Labs
tags:
  - portswigger
  - labs
  - sqli
  - sql_injection
published: false
date: 2025-05-31T09:56:00
excalidraw-plugin: parsed
excalidraw-open-md: true
---
Please complete the attached nginx labs, and for the dns, be prepared for the below topics.

  

**You also need to have concepts of F5 AFM for the dns mitigation as well.**

For the nginx labs, try to complete as much as you can for the labs which are not feasible due to the resource constraints then you must have the strong understanding on how it works.

  

  

DNS Query Types and Attack Vectors:

Concept: Understand common DNS query types (A, AAAA, ANY, NXDOMAIN) and how they’re exploited in attacks (e.g., amplification with ANY, water torture with NXDOMAIN)

  

  

Rate Limiting and Thresholds:

Concept: Use parameters like rateLimit, floor, and rateThreshold to cap query rates and detect spikes (e.g., 500 pps for A queries).

  

Protocol Error Handling:

Concept: Detect and mitigate malformed DNS queries using settings like protErrAtckRateLimit (e.g., 5000 pps) and protErrAtckRateIncr (e.g., 300%).

  

Blacklisting and Scrubbing:

Concept: Block malicious IPs (blacklistDuration, e.g., 3600–14400 seconds) and redirect traffic to scrubbing centers (scrubbingDuration, e.g., 600 seconds).

  

DNS Amplification Mitigation:

Concept: Prevent amplification attacks by limiting queries per source/destination IP (perSourceIpLimitPps, perDstIpLimitPps, e.g., 100–1000 pps).

  

Traffic Analysis and Monitoring:

Concept: Analyze DNS traffic using logs or tools (e.g., Infoblox or Wireshark) to set baselines for thresholds like floor (e.g., 100–1000 pps).

  

  

DNSSEC Basics:

Concept: Understand DNS Security Extensions (DNSSEC) to validate DNS responses and prevent cache poisoning.

  

Upstream DNS Configuration:

Concept: Configure reliable upstream DNS servers in NGINX (e.g., in resolver directive) to ensure fast and secure resolution.

  

  

Collaboration with DNS Mitigation Services:

Concept: Integrate with DDoS mitigation providers (e.g., Cloudflare).




# NGINX

192.168.180.181 Basic NGINX Web Server Setup and Static Content Delivery 

Description: Set up NGINX as a web server to serve static content (HTML, CSS, JavaScript) and configure virtual hosts for multiple domains. 

  

Objectives: 

Install NGINX on a Linux server (e.g., Ubuntu). 

Configure NGINX to serve static files from a designated directory. 

Set up virtual hosts for two domains (e.g., example1.com, example2.com). 

Test content delivery using a browser or curl. 

  

  

Configuring NGINX as a Reverse Proxy for a Simple Application 

Configuring NGINX as a Reverse Proxy for a Simple Application 

Description: Use NGINX as a reverse proxy to forward requests to a backend application (e.g., a Node.js or Flask app). 

  

Objectives: 

Set up a basic backend application (e.g., Flask app running on localhost:3000). 

Configure NGINX to proxy requests from port 80 to the backend. 

Test request forwarding and response handling. 

Enable basic logging to capture requests (access.log). 

  

  

Implementing NGINX as an API Gateway for Microservices 

Description: Configure NGINX as an API Gateway to route requests to multiple microservices, simulating a real-world microservices architecture. 

  

Objectives: 

 Create two simple microservices (e.g., Flask apps for /users and /orders endpoints). 

Configure NGINX to route requests based on URL paths (e.g., /api/users to service1, /api/orders to service2). 

Implement rate limiting to restrict API abuse. 

Enable API key authentication using NGINX Lua module or basic auth. 

  

 

Load Balancing Across Multiple Backend Servers 

Description: Set up NGINX as a load balancer to distribute traffic across multiple backend servers, optimizing resource utilization. 

  

Objectives: 

Deploy three identical backend servers (e.g., Node.js apps on ports 3001, 3002, 3003). 

Configure NGINX to load balance using the round-robin and least connections algorithms. 

Test load distribution using a tool like ab (Apache Benchmark). 

Enable session persistence (sticky sessions) for consistent user experience. 

  

  

 

Optimizing NGINX Performance with Caching and Compression 

Description: Optimize NGINX performance by implementing caching for static and dynamic content and enabling Gzip compression. 

  

Objectives: 

Configure caching for static assets (e.g., images, CSS) with a 30-day expiration. 

Set up proxy caching for dynamic API responses (e.g., /api/products). 

Enable Gzip compression for text-based responses (HTML, JSON). 

Measure performance improvements using tools like curl or browser DevTools. 

  

  

Securing NGINX with SSL/TLS and WAF 

Description: Secure NGINX with SSL/TLS for encrypted communication and implement basic Web Application Firewall (WAF) rules to protect against common attacks. 

  

Objectives: 

Obtain a free SSL certificate using Let’s Encrypt. 

Configure NGINX to serve HTTPS traffic with TLS 1.3. 

Implement WAF using NGINX ModSecurity or NGINX App Protect (NGINX Plus). 

Test protection against SQL injection and XSS attacks using a tool like OWASP ZAP. 

  

  

Advanced Logging and Monitoring for NGINX 

Description: Implement advanced logging and integrate NGINX with a monitoring solution to track performance and security events. 

  

Objectives: 

Configure custom log formats to capture detailed request data (e.g., response time, client IP, user agent). 

Set up log rotation to manage disk space. 

Integrate NGINX logs with a monitoring tool like ELK Stack (Elasticsearch, Logstash, Kibana) or Prometheus/Grafana. 

Create a dashboard to visualize traffic patterns and error rates. 

  

  

High-Availability NGINX Deployment with Health Checks 

Description: Deploy NGINX in a high-availability setup with active health checks to ensure backend reliability. 

  

Objectives: 

Set up two NGINX instances behind a load balancer (e.g., another NGINX or HAProxy). 

Configure health checks for backend servers using NGINX Plus or open-source modules. 

Simulate backend failure and verify failover. 

Monitor uptime using a tool like UptimeRobot. 

 

 