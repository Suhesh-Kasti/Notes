---
category:
  - Networking
  - CCNA
  - f5
tags:
  - direct_server_return
published: false
date: 2024-09-30T14:17:00
excalidraw-plugin: parsed
excalidraw-open-md: true
---
In **Direct Server Return (DSR)**, the load balancer forwards client requests to the server, but the **server responds directly to the client** without routing the response back through the load balancer. This method is often used to improve performance and reduce the load on the load balancer by avoiding unnecessary forwarding of responses in a [[Half Proxy]] setup.
##### **Example**
1. **Client IP:** `192.168.1.10`
2. **Load Balancer VIP (Virtual IP):** `192.168.2.1`
3. **Server IP:** `192.168.3.5`
##### **Step-by-Step Breakdown:**
1. **Client sends a request to the Load Balancer:**
    - The client sends a request to the load balancer’s **Virtual IP** (VIP) at **192.168.2.1**.
    - **Client Request:**
        - Source IP: `192.168.1.10`
        - Destination IP: `192.168.2.1` (Load Balancer VIP)
2. **Load Balancer forwards the request to the Server:**
    - The load balancer receives the request but does not modify the **IP header** (it keeps the original source and destination IPs).
    - The load balancer forwards the packet to the server by altering the **Layer 2 (MAC address)** so the server receives the packet.
    - **Forwarded Request to the Server:**
        - Source IP: `192.168.1.10` (Client)
        - Destination IP: `192.168.2.1` (VIP)
        - [[#Why would server recognize VIP as its own IP?|Server processes the request because it recognizes the VIP as one of its assigned IPs]].
3. **Server responds directly to the Client:**
    - Instead of sending the response back to the load balancer, [[#Can i use this technique to perform Man-In-The-Middle Attacks? | the server responds directly to the client]].
    - The server uses the **client’s IP** as the destination IP in the response.
    - **Server Response:**
        - Source IP: `192.168.3.5` (Server)
        - Destination IP: `192.168.1.10` (Client)

This means the **response bypasses the load balancer**, improving performance by reducing the load balancer's involvement in the return path.

---
### **How Half Proxy Works with Only a Switch**
In a **[[Half Proxy|half proxy]]** setup, the load balancer handles client requests but allows the server to respond directly to the client. If there's only a **switch** between the load balancer, client, and server, the network layer (IP) is unchanged by the switch. A **switch** operates at Layer 2 (Ethernet), forwarding frames based on **MAC addresses**.

|**Step**|**Source IP**|**Destination IP**|**Source MAC**|**Destination MAC**|**Action**|
|---|---|---|---|---|---|
|**1. Client sends request**|`192.168.1.10`|`192.168.2.1`|`MAC_C` (Client)|`MAC_LB` (Load Balancer)|The client sends a request to the load balancer (VIP).|
|**2. Load Balancer forwards to Server**|`192.168.1.10`|`192.168.3.5`|`MAC_LB` (Load Balancer)|`MAC_S` (Server)|Load balancer forwards the request to the server.|
|**3. Server responds directly to Client**|`192.168.3.5`|`192.168.1.10`|`MAC_S` (Server)|`MAC_C` (Client)|The server sends the response **directly** to the client, bypassing the load balancer.|

### **Traffic Breakdown**
- **Step 1: Client to Load Balancer**
    - The client (`192.168.1.10`) sends a request to the **Virtual IP (VIP)** of the load balancer (`192.168.2.1`).
    - The client uses the **MAC address** of the load balancer (`MAC_LB`) as the **destination MAC** since the load balancer is the next-hop.
- **Step 2: Load Balancer to Server**
    - The load balancer forwards the request to the backend **server** (`192.168.3.5`) using the server's **MAC address** (`MAC_S`) at the Layer 2 level.
    - The IP header remains unchanged, meaning the **source IP** remains the client’s IP (`192.168.1.10`), and the **destination IP** stays the same (`192.168.3.5`).
- **Step 3: Server responds directly to Client**
    - The server receives the request, processes it, and sends the **response directly to the client** (`192.168.1.10`).
    - The server sets its own **MAC address** (`MAC_S`) as the **source MAC** and the client's **MAC address** (`MAC_C`) as the **destination MAC**.
### **How the Switch Works**
- The **switch** simply forwards Ethernet frames based on **MAC addresses**.
- It doesn’t modify IP addresses, so the Layer 3 (IP) traffic remains intact.
- **Asymmetric routing** happens because the switch routes packets at Layer 2 between the client, load balancer, and server, while the **IP flow** changes when the server responds directly to the client.
### **Configuration Example on the Server (Linux)**:
In a DSR setup, a server might have the VIP (`192.168.2.1`) configured as a loopback interface:
`sudo ifconfig lo:0 192.168.2.1 netmask 255.255.255.255 up`
This ensures that when the load balancer forwards packets with `192.168.2.1` as the destination IP, the server recognizes it as its own IP and processes the request.
### **How the DSR Process Works**:
1. **Client Request:**
    - Client (`192.168.1.10`) sends a request to the VIP (`192.168.2.1`).
2. **Load Balancer Forwards Request:**
    - The load balancer forwards the request to the server (`192.168.3.5`), keeping the VIP as the destination IP.
3. **Server Recognizes VIP:**
    - The server, with the VIP (`192.168.2.1`) configured on its loopback interface, recognizes the packet as meant for itself and processes the request.
4. **Server Responds Directly:**
    - The server responds directly to the client using the client’s IP address (`192.168.1.10`), bypassing the load balancer.

---
## Why would server recognize VIP as its own IP? 
In a **Direct Server Return (DSR)** setup, the **server recognizes the Virtual IP (VIP)** as one of its own IPs because the VIP is **configured on the server** as a **loopback** or **secondary IP address**. This configuration is crucial for DSR to function properly, allowing the server to respond directly to client requests while keeping the VIP intact.
1. **VIP Configuration on the Server**:
    - In DSR, the **Virtual IP (VIP)** (e.g., `192.168.2.1`) is usually assigned to the load balancer to receive incoming traffic from clients. However, the **same VIP is also configured on the server**, typically as a **loopback address** (a virtual network interface).
    - This setup allows the server to receive and process traffic sent to the VIP without needing to forward responses back through the load balancer.
2. **How the Server Uses the VIP**:
    - When the load balancer forwards the packet to the server, the **destination IP** in the packet remains the VIP (e.g., `192.168.2.1`).
    - Since the server has the VIP configured as a local loopback IP, it recognizes this as its own address and accepts the packet, even though the original request was made to the load balancer.
3. **Loopback Interface**:
    - The server is configured to respond from the VIP, but instead of routing traffic back through the load balancer, it responds directly to the client using its own **real IP address** (e.g., `192.168.3.5`).
    - The **VIP is not tied to a physical network interface** on the server. It’s typically assigned to a loopback interface (e.g., `lo:0`), allowing the server to handle traffic directed at the VIP.

---
### How Does the Client Accept the Response?
The client will accept a response from `192.168.3.5` (the real server) in a **Direct Server Return (DSR)** or **half proxy** setup because the **source IP in the response matches the original request’s destination IP** (the VIP). 
1. **Client Request:**
    - The client sends a request to the **Virtual IP (VIP)**, which is `192.168.2.1` (the Load Balancer's VIP).
    - The client expects a response from `192.168.2.1`, as it believes this is the server's IP.
    **Request Packet:**
    - Source IP: `192.168.1.10` (Client)
    - Destination IP: `192.168.2.1` (VIP on Load Balancer)
2. **What Happens at the Load Balancer (DSR/Half Proxy Setup):**
    - The load balancer forwards the request to the real server (`192.168.3.5`) but **does not change the destination IP** in the packet. The IP remains as `192.168.2.1`.
    - The server is configured to recognize the VIP (`192.168.2.1`) as one of its own addresses (usually on a loopback interface), so it processes the request.
3. **Server Response:**
    - When the server (`192.168.3.5`) sends the response **directly to the client**, it keeps the **source IP** as the VIP (`192.168.2.1`), not its own real IP (`192.168.3.5`).
    **Response Packet:**
    - Source IP: `192.168.2.1` (VIP, which the client expects)
    - Destination IP: `192.168.1.10` (Client)
### **Why Does the Client Accept This?**
- The client **does not care** about the server's actual IP address (`192.168.3.5`).
- The client only looks at the **source IP** in the response packet. If the source IP in the response matches the **VIP** (`192.168.2.1`) that the client originally requested, the response appears valid to the client.
- The server ensures that the response packet has the **source IP as the VIP (`192.168.2.1`)**, so the client believes it is communicating with the original destination (VIP), even though the response is coming directly from the real server.
### **Why Doesn’t the Real Server’s IP Matter?*
In DSR and half-proxy setups:
- The server’s **real IP** (`192.168.3.5`) is only used internally between the load balancer and the server.
- For the client, the connection always appears to be with the **VIP** (`192.168.2.1`), as the client only sees the VIP in both the request and the response.
- The **server never exposes its real IP** (`192.168.3.5`) to the client directly. The client always receives the response with the VIP (`192.168.2.1`) as the source IP.

### **Asymmetric Routing in DSR/Half Proxy**
- **Request Path:** Client → Load Balancer (VIP) → Server
- **Response Path:** Server → Client (directly)
- The **key detail** is that, even though the server sends the response directly to the client, it uses the **VIP (`192.168.2.1`)** as the **source IP** in the response packet.

### Can i use this technique to perform Man-In-The-Middle Attacks?
The answer is **NO**. In theory, the scenario you describe — using a **loopback address** to reply as someone else — might seem similar to how **Direct Server Return (DSR)** works in a **half-proxy** setup. However, there are several important differences and limitations that prevent this method from being used to impersonate another service (like Google) for malicious purposes or **Man-in-the-Middle (MITM)** attacks.
1. **Traffic Routing and Control**:
    - In the **half-proxy/DSR** scenario, the reason the server can respond using the **VIP (loopback address)** is because:
        - The **load balancer** controls the initial routing, ensuring the client's request reaches the server.
        - The **VIP** is assigned to the loopback interface on the server **intentionally** as part of a **trusted setup**.
    - **If you were to assign a public IP (like Google’s)** to your loopback interface, the **internet's global routing infrastructure** would still direct traffic to the **real Google servers**, not your machine. You **cannot control external routing** in this way, so you wouldn't receive the initial traffic to respond to.
2. **Source IP Validation (Anti-Spoofing)**:
    - Modern networks and servers implement **anti-spoofing measures**. This means that if you try to send a response from a loopback address pretending to be another IP (like Google’s), routers, firewalls, and other devices on the network will likely **detect the spoofed IP address** and **discard the packet**.
    - **ISPs** and **network devices** typically block traffic that claims to come from public IP ranges unless it is correctly routed from the owner of those IP addresses.
3. **No Real MITM Capability**:
    - In a **half-proxy/DSR setup**, the server **legitimately receives** the client’s request from the load balancer. The server is **authorized** to handle and respond to that request.
    - If you were trying to spoof traffic from another source (like Google), you’d have to somehow intercept or control the flow of requests intended for Google’s servers, which is extremely difficult without access to the underlying network.
    - Simply assigning the same IP to your loopback interface won’t cause external traffic to be routed to your machine. Routers, DNS servers, and ISPs will ensure that the real Google IP traffic goes to the **correct destination**.
4. **TLS/SSL Encryption**:
    - **HTTPS traffic** (used by almost all major services like Google) is encrypted using **TLS/SSL**. Even if you were able to somehow intercept requests, you wouldn’t be able to impersonate the server because you wouldn’t have access to the required **private keys** to decrypt the traffic or properly respond. The client would detect this and **reject the response** as invalid.
5. **Network Security Protections (IP Source Guard)**:
    - Many network devices use features like **IP Source Guard** and **Unicast Reverse Path Forwarding (uRPF)**, which verify that the source IP address in a packet matches the expected interface or network path. These mechanisms would flag and drop traffic from a **spoofed IP** (like using a loopback address to pretend to be another entity).
So, in the **spoofing scenario**:
- We have no way to get the initial traffic intended for a public service like Google unless you **compromise network routing**, which is not feasible without deep access to network infrastructure.
- Even if we spoof the source IP to try to impersonate Google or any other service, **network security mechanisms** and **TLS encryption** will prevent this from being successful.

%%
# Excalidraw Data
## Text Elements
Client ^NjNLufA1

Load Balancer ^YITYNLHs

Server ^F6nFKRRp

202.15.77.94 ^lAk2tQN6

147.233.87.14 ^YfyhpUd9

10.1.0.1 ^Y4fVcrIY

lo: 147.233.87.14 ^rIPXdpQ2

202.15.77.94 ^x1P422PT

147.233.87.14 ^ti8RNQ9H

202.15.77.94 ^LlxlKzTE

lo: 147.233.87.14 ^9YkzHhT3

lo: 147.233.87.14 ^KjjcdZXG

202.15.77.94 ^fBS27c5j

## Drawing
```compressed-json
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
```
%%