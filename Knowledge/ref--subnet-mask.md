---
category: knowledge
tags:
  - networking
platform: n/a
status: done
created: 2026-06-17
aliases:
  - IP Address:
---

Subnetting is the process of dividing a larger network into smaller, more manageable sub-networks, ie. subnets.
 **Why Subnet?**
1. **Efficient IP Address Management:** Helps manage IP addresses more efficiently by dividing large networks into smaller segments.
2. **Improved Performance:** Reduces network traffic and congestion by limiting the broadcast domains.
3. **Enhanced Security:** Isolates different segments of a network, improving security and management.
# IP Address:
A unique identifier for a device on a network, e.g., 192.168.1.1.
# [[Subnet Mask]]
A mask used to determine the subnet an IP address belongs to, e.g., 255.255.255.0.
# CIDR
**Classless Inter-Domain Routing** notation is a way to specify IP addresses and their associated routing prefix. It is written as an IP address, followed by a forward slash, and then a number (e.g., 192.168.1.0/24).
- The number after the slash (e.g., 24 in /24) represents the number of bits in the network prefix.
- The remaining bits (32 minus the prefix length) represent the host portion.
### Some common CIDR notations
- **/24:** 255.255.255.0
- **/20:** 255.255.240.0
- **/16:** 255.255.0.0
- **/8:** 255.0.0.0
- **/32:** 255.255.255.255 (single IP address)
- **/12:** 255.240.0.0
### Calculating Subnets and Hosts
1. **Subnets:** Divide the available host addresses into smaller groups.
2. **Hosts:** Determine the number of available IP addresses in each subnet.
#### Formula for Number of Hosts
$$ Number of Hosts = 2^{(32 - Prefix Length)}−2 $$
- The subtraction of 2 accounts for the network and broadcast addresses, which are not assignable to hosts.
#### Examples:
- **/24 (255.255.255.0):**
  - Hosts: $( 2^{(32-24)} - 2 = 2^8 - 2 = 254 )$
  - Subnets: 1 subnet (since /24 is the default subnet mask for Class C)

- **/20 (255.255.240.0):**
  - Hosts: $( 2^{(32-20)} - 2 = 2^{12} - 2 = 4094 )$
  - Subnets: \( 2^{(24-20)} = 2^4 = 16 \) subnets if starting from a /24 block

- **/16 (255.255.0.0):**
  - Hosts: $( 2^{(32-16)} - 2 = 2^{16} - 2 = 65,534 )$
  - Subnets: \( 2^{(24-16)} = 2^8 = 256 \) subnets if starting from a /24 block

- **/8 (255.0.0.0):**
  - Hosts: $( 2^{(32-8)} - 2 = 2^{24} - 2 = 16,777,214 )$
  - Subnets: \( 2^{(24-8)} = 2^{16} = 65,536 \) subnets if starting from a /24 block

- **/32 (255.255.255.255):**
  - Hosts: $( 2^{(32-32)} - 2 = 2^0 - 2 = 0 )$
  - Subnets: N/A (single IP address)

- **/12 (255.240.0.0):**
  - Hosts: $(2^{(32-12)} - 2 = 2^{20} - 2 = 1,048,574 )$
  - Subnets: \( 2^{(24-12)} = 2^{12} = 4,096 \) subnets if starting from a /24 block
# FlashCard
#flashcard
1. **Power of Two Rule:** Remember the powers of two. For example:
   - \( 2^8 = 256 \)
   - \( 2^{10} = 1024 \)
   - \( 2^{12} = 4096 \)

2. **Subnet Mask Patterns:**
   - /24: 255.255.255.0 (256 addresses, 254 usable hosts)
   - /20: 255.255.240.0 (4096 addresses, 4094 usable hosts)
   - /16: 255.255.0.0 (65,536 addresses, 65,534 usable hosts)

3. **Bit Counting:**
   - Every bit in the subnet mask reduces the number of host bits by one.
   - Each host bit remaining represents \( 2 \) potential addresses.

4. **Shortcut for Hosts Calculation:**
   - **/24:** 254 hosts
   - **/23:** 512 hosts (minus 2)
   - **/22:** 1024 hosts (minus 2)
   - Continue doubling hosts as we decrease prefix by 1.
### Subnetting Reference Table

| CIDR Notation | Subnet Mask       | # of Subnets | # of Hosts per Subnet | Network Address Example      | Broadcast Address Example    | Usable IP Range Example          |
|---------------|-------------------|--------------|-----------------------|------------------------------|------------------------------|----------------------------------|
| /8            | 255.0.0.0         | 1            | 16,777,214            | 10.0.0.0                     | 10.255.255.255               | 10.0.0.1 - 10.255.255.254        |
| /12           | 255.240.0.0       | 16           | 1,048,574             | 10.0.0.0                     | 10.15.255.255                | 10.0.0.1 - 10.15.255.254         |
| /16           | 255.255.0.0       | 256          | 65,534                | 192.168.0.0                  | 192.168.255.255              | 192.168.0.1 - 192.168.255.254    |
| /20           | 255.255.240.0     | 4096         | 4,094                 | 192.168.0.0                  | 192.168.15.255               | 192.168.0.1 - 192.168.15.254     |
| /24           | 255.255.255.0     | 1            | 254                   | 192.168.1.0                  | 192.168.1.255                | 192.168.1.1 - 192.168.1.254      |
| /26           | 255.255.255.192   | 4            | 62                    | 192.168.1.0                  | 192.168.1.63                 | 192.168.1.1 - 192.168.1.62       |
| /28           | 255.255.255.240   | 16           | 14                    | 192.168.1.0                  | 192.168.1.15                 | 192.168.1.1 - 192.168.1.14       |
| /30           | 255.255.255.252   | 64           | 2                     | 192.168.1.0                  | 192.168.1.3                  | 192.168.1.1 - 192.168.1.2        |
| /32           | 255.255.255.255   | N/A          | 1                     | 192.168.1.1                  | 192.168.1.1                  | 192.168.1.1                      |


%%
## Drawing
```compressed-json
N4IgLgngDgpiBcIYA8DGBDANgSwCYCd0B3EAGhADcZ8BnbAewDsEAmcm+gV31TkQAswYKDXgB6MQHNsYfpwBGAOlT0AtmIBeNCtlQbs6RmPry6uA4wC0KDDgLFLUTJ2lH8MTDHQ0YNMWHRJMRZFEIAOMiRPVRhGMBoEAG0AXXJ0KCgAZQCwPlBJfDxM7A0+Rk5MTHIdGCIAIXRUAGsCrkZcAGF6THp8BBAAYgAzEdGQAF9xoA===
```
%%
