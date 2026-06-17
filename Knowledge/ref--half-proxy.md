---
category: knowledge
tags:
  - networking
platform: n/a
status: done
created: 2026-06-17
aliases:
  - Untitled
---

In a **half proxy** setup, the load balancer intercepts the client's request, forwards it to the server, but the response from the server **bypasses the load balancer** and is sent directly to the client. This setup is used in specific scenarios where performance gains are desired, but it introduces challenges like [[#Asymmetric Routing Problem|asymmetric routing]] .
### **Half Proxy Connection Example with IPs**
1. **Client IP:** `192.168.1.10`
2. **Load Balancer IP (VIP):** `192.168.2.1`
3. **Server IP:** `192.168.3.5`
#### **Step 1: Client sends request to Load Balancer**
- **Client (192.168.1.10)** wants to connect to a service hosted behind the load balancer. The client sends a request to the **Virtual IP (VIP)** of the load balancer: **192.168.2.1**.
- **Client Request:**
    - Source IP: `192.168.1.10`
    - Destination IP: `192.168.2.1`
#### **Step 2: Load Balancer forwards request to Server**
- The load balancer, operating in **half proxy** mode, forwards the request to the backend server **192.168.3.5** without altering the source IP address (which is important for the server's direct response).
- **Forwarded Request:**
    - Source IP: `192.168.1.10` (Client)
    - Destination IP: `192.168.3.5` (Server)

Here, the load balancer only modifies the destination IP address of the packet to forward it to the server, while keeping the source IP intact.
#### **Step 3: Server responds directly to Client**
- In a half proxy setup, instead of routing the response back through the load balancer, the **server responds directly to the client** using the original source IP it saw in the packet (client’s IP).
- **Server Response:**
    - Source IP: `192.168.3.5` (Server)
    - Destination IP: `192.168.1.10` (Client)
### Asymmetric Routing Problem
This setup causes an **asymmetric routing issue** because:
1. **Request Path:** Client → Load Balancer → Server
2. **Response Path:** Server → Client (bypassing the load balancer)
When traffic takes **different paths** on the way to and from the client, the network devices (e.g., firewalls or routers) may discard the packets, as they expect traffic to follow the same route (both request and response via the load balancer).
**Why would the packet be discarded?**
- Firewalls, NAT devices, or [[#Stateful Inspection]] devices maintain a connection table for every session, associating request and response packets. If the response bypasses the original path (the load balancer), the return packets won’t match the expected flow, leading to **packet drops**.
### **Solutions to Asymmetric Routing Issue**
#### 1. [[Direct Server Return (DSR)]]
A more optimized version of the half proxy, [[Direct Server Return (DSR)]], allows the server to send responses directly to the client but works under specific conditions:
- The load balancer passes the client’s request **without altering** the Layer 3 information (like the source IP address), but **may modify Layer 2 information** (MAC addresses).
- **Requirements:**
    - The load balancer and server must be in the same Layer 2 domain.
    - The server must respond directly to the client by using the client’s IP address as the destination IP, but the server doesn’t change the VIP as the destination MAC address.
    **Flow in DSR:**
    - Request: Client (192.168.1.10) → Load Balancer (192.168.2.1) → Server (192.168.3.5)
    - Response: Server (192.168.3.5) → Client (192.168.1.10)
Since the server sends the response directly to the client, **firewalls** or **routers** between the server and client must be configured to handle this traffic properly to avoid stateful inspection issues.
#### 2. **Source NAT (SNAT)**
In a half-proxy setup, you can use **Source Network Address Translation (SNAT)** to rewrite the source IP of the client's request. This ensures the server always sends the response back through the load balancer, preventing asymmetric routing. This is full proxy.
- **How it works:**
    - The load balancer rewrites the source IP of incoming requests to its own IP (e.g., **192.168.2.1**).
    - When the server responds, it sends the response back to the load balancer (since that’s the source IP of the request).
    - The load balancer then forwards the response to the original client.
    **Flow with SNAT:**
    - Request (after SNAT): Client (192.168.1.10) → Load Balancer (SNAT to 192.168.2.1) → Server (192.168.3.5)
    - Response: Server (192.168.3.5) → Load Balancer → Client (192.168.1.10)
#### 3. **Firewall and Network Configuration Adjustments**
If using half-proxy or DSR, network devices like firewalls and routers need to be configured to allow **asymmetric traffic**. This can be done by:
- **Disabling [[#Stateful Inspection]]** on the firewalls, so they don’t track connection states and allow traffic that comes from different paths.
- **Configuring policy routing** to make sure return traffic from the server to the client is allowed even if it bypasses the load balancer.

---
### Stateful Inspection
**Stateful inspection** (also called **stateful packet filtering**) is a type of firewall technology that keeps track of the **state of active connections**. It monitors the entire session (both incoming and outgoing packets) and only allows responses to packets that are part of an established connection.
- **How it works:**
    - When a client makes a request, the firewall checks that packet and records the session details in a **state table**.
    - When the server responds, the firewall checks if the response matches an existing entry in the state table (i.e., it’s part of an established connection).
    - If the response doesn't match, it’s blocked; if it matches, it's allowed.
This behavior ensures that only expected traffic flows through the firewall, providing an additional layer of security.

---
### **Is a Firewall Necessary for Half Proxy?**
A **firewall** is not strictly necessary for a **half proxy** setup, but it’s recommended for **security reasons**. In half proxy, the load balancer handles the forwarding of client requests to the server, while the server responds directly to the client. This creates an **asymmetric routing** scenario, where firewalls may need specific configuration adjustments:
- **Without a firewall:**
    - Traffic flows freely between the client, load balancer, and server.
    - This could leave the network vulnerable to attacks like unauthorized access or traffic interception.
- **With a firewall:**
    - A firewall can inspect and control traffic between different components (client, load balancer, and server).
    - However, you need to ensure the firewall is configured to handle **asymmetric traffic** (since responses from the server won’t pass through the load balancer).
