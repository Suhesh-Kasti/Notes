---
category:
  - CCNA
  - Networking
tags:
  - defaultroute
  - nullip
published: false
date: 2024-07-11T12:20:00.000Z
excalidraw-plugin: parsed
excalidraw-open-md: true
---

A default route is a setting on a router that tells it where to send packets if it doesn't know the destination. Its a catch-all path for any unknown destination. It provides:
- **Simplicity:** Instead of having a route for every possible destination, a default route provides a simple way to handle unknown destinations.
- **Efficiency:** Reduces the size of the routing table, making routing decisions faster and simpler.
# 0.0.0.0/0  
The IP address **0.0.0.0** is a special address with multiple uses depending on the context:
1. **Default Route:** When used in a routing table, it signifies "any IP address" or "all unknown destinations."
2. **Unspecified Address:** When a device or software uses 0.0.0.0, it means it doesn't have an assigned IP address yet or is not specified.
## Why use 0.0.0.0?
In the context of a default route, 0.0.0.0/0 means any IP address that isn't otherwise specified in the routing table. This allows routers to have a simple and efficient way to handle packets destined for unknown addresses by sending them to a designated next hop (usually the gateway to another network or the internet).

**What if we use something else for default route**
If we use a specific IP address or [[subnet]] instead of 0.0.0.0 for the default route:
- **Specific IP Address:** The router would only forward packets destined for that exact IP address, not any unknown address.
- **Specific Subnet:** The router would forward packets only for that specific subnet, not for all unknown destinations.
### Creating a Default Route
#### 1. F5 BIG-IP
1. **Access the Configuration Utility:** Log in to the F5 BIG-IP Configuration Utility.
2. **Go to Network Configuration:** Navigate to Network > Routes > Route List.
3. **Create a New Route:**
   - Click on "Create."
   - Set the **Destination** to `0.0.0.0/0` (IPv4) or `::/0` (IPv6).
   - Enter the **Gateway Address** (the next hop IP address).
4. **Save the Configuration:** Click "Finished."
#### 2. Cisco
1. **Access the Router's CLI:** Connect to the router via console, SSH, or Telnet.
2. **Enter Global Configuration Mode:**
   ```
   configure terminal
   ```
3. **Create the Default Route:**
   - For IPv4:
   ```
   ip route 0.0.0.0 0.0.0.0 <gateway-ip>
   ```

> Note: 
   >**First 0.0.0.0**: This represents the destination network and is equivalent to saying "anywhere." It's shorthand for 0.0.0.0/0, which means any IP address.
   > **Second 0.0.0.0**: This is the subnet mask. In this context, 0.0.0.0 means "match all bits," indicating that no specific bits of the destination address need to match. This creates a route that applies to all IP addresses.

   - For IPv6:
   ```
   ipv6 route ::/0 <gateway-ipv6>
   ```
4. **Exit Configuration Mode:**
   ```
   end
   ```
   
### Consequences of Incorrect Default Route Configuration
Using a specific IP address or subnet as a default route limits the catch-all nature of the default route. This can lead to packets being dropped if they don't match any entry in the routing table.

#### Example:
Imagine a router's routing table: 

| Destination | Subnet Mask   | Gateway       |
| ----------- | ------------- | ------------- |
| 192.168.1.0 | 255.255.255.0 | 192.168.1.254 |
| 172.16.0.0  | 255.240.0.0   | 172.16.0.1    |
| 0.0.0.0     | 0.0.0.0       | 192.168.1.1   |
- **Specific Route:** For a packet destined to 192.168.1.10, it matches the first route and goes to 192.168.1.254.
- **Default Route:** For a packet destined to 8.8.8.8 (not matching any specific routes), it uses the default route (`0.0.0.0/0`) and goes to 192.168.1.1.
###### **Packet Journey**
1. **Laptop to Router:** L1 sends the packet to R1, the default gateway.
2. **Router Checks Routing Table:**
    - No specific route for 8.8.8.8.
    - Matches the default route `0.0.0.0/0`.
3. **Router to ISP Gateway:** R1 forwards the packet to the ISP gateway (203.0.113.1).
4. **ISP to Internet:** ISP routes the packet to its destination (8.8.8.8).


# Excalidraw Data
## Text Elements
hello ^UOrr7yxn

%%
## Drawing
```compressed-json
N4KAkARALgngDgUwgLgAQQQDwMYEMA2AlgCYBOuA7hADTgQBuCpAzoQPYB2KqATLZMzYBXUtiRoIACyhQ4zZAHoFAc0JRJQgEYA6bGwC2CgF7N6hbEcK4OCtptbErHALRY8RMpWdx8Q1TdIEfARcZgRmBShcZQUebTiADho6IIR9BA4oZm4AbXAwUDAiiBJuCABVAHlSUgB2GEwufmLYRDKoLChkoshMbmcATgA2bQTagFZmyBh+gGYeEcn8yAoS

dW4AFjiNgEYBgfGeWYGecdqEndOpqQRCZWluK+WIa2Vg7gAGa+YoUjYAawQAGE2Pg2KQygBiHYIGEw7rFTS4bD/ZR/IQcYggsEQiS/azMOC4QKZBGQABmhHw+AAyrB3hJBB4yRAfn9AQB1NaSR7fX4AhB0mAM9BM0rXdH3DjhbJoHbXNhE7BqGZyj5fZ5o4RwACSxFlqByAF1ruTyOk9dwOEJqddCJisGVcDsWejMdLmAbrbbnmEEMRuLVZpcPsG

dglrowWOwuGrI0xWJwAHKcMTcIbjIbBj4JAYbO3MAAiqQ6AbQ5IIYWummEmIAosF0pkvTb8NchHBiLhS9wdrUeB8hvtBxscwNrkQOP8ra2J2wUf7uBX8FXnh1MF0JJIgmDXZQACqdMrb6lsFnkzhQGmEIziXganoQC+ZABiuH0VNVqHla86AEEiGUWN0GCckunjUgoHMAgALuYDoEVFk9EyXB7SYS00G9NtnnBO57QIQ8N2PHcz2uXAhCgNgACVw

hvO9fiEBAJzQgAJW57k3b94nGfIAF9mkKFp4DvCBAmwKIODeJAIMTYDLhkmMUw4NM0CGIYPg2IYxnDO0HT6CRcA+FlCCLEtFzQBimOeUoJB4QsNhgMCAA1YAAGQABQQQtC2UZQkyBHh/iMc8qVpekRLFAM+XZBAuWIdY0D4X1+UBIURVZUFxWeSVJA9A0f0fRVkRVXt1TIySRQfYp9NQZweB2cZuOuL86pOaKBWxcEoThWFpOeJEUS1DEsVBLq8X

IDhCWJDJwOeVZ4p5RLxgK4ptzuB5EtDb4EHM78NL7cYc1mfNNXRXV9VyE1njNd8EAw1AsIlWtiDy7hBKEto0FmZZ+P656GzSGaDWNdtO27Xa+wHIcBg+cYEnqk7H0nadMNnZ4wQXMtUGXMI+PAK7IFwOA4DpcG3vyaBt3SMpAIeZoGEIBAKAAIWRVE3RGnEoXJHneYRCBsBEEkoB1Dp9DpGLOtxdBoV6+F6cFmoZtFtJWcGjmpfaCapuF/nFeFlX

9BfUK0oizKoop/XlbFiWBTihLeAVoXrbSW3UvCspIr153MkNqjhClGVeydpXfbFyolRKtUqoFn2RbFl9LzfD98C/FbY9D+O0kTzJr1vR4Y6tsO0kIqBYKAmmEDA73M8N0nIL/Go2AobdcCxx7Lbjw260xRu/hbkIsZeJuqHp5hsD+aknM2DTtEuJZinHyf8AATU2HgNm0BfICMNgDHJx96AIRjHj4kODbF/3hteiQOf5tESDzu8O+KB/ObG1B3og

ZnQSHyEgQGAAgBL4XwshosoG0xIoR1kLDAmBICIBn07pnN2CAI5QU4C2H0xQ4CBDMMIZgABxUgj86IzmwRSc0CAaIOhIZJA+xQMi4E0MELGllrjYCIHAbg7DngcFujw0gjEFQUUnPRIRCAkHFDsAAKwQOJZgNJ+FwAALJsGIAgHuzDWFLkrJIsAv0KRUnCG9XiIBeJAA
```
%%