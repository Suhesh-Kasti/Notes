---
category: knowledge
tags:
  - networking
platform: n/a
status: done
created: 2026-06-17
aliases:
  - Headers in Network Layer
---

# Headers in Network Layer
- Version – four bits
- Internet Header Length (IHL) – four bits
- Differentiated Services Code Point (DSCP) – six bits
- Explicit Congestion Notification (ECN) – two bits
- Total Length – two Bytes
- Identification – two Bytes
- Flags – three bits
- Fragment Offset – 13 bits
- Time to Live (TTL) – one Byte
- Protocol – one Byte
- Header Checksum – two Bytes
- Source IP Address – four Bytes
- Destination IP Address – four Bytes
- One or more optional Options headers – variable length
# IP Addressing
- Used to identify a network interface on a logical IP network
- IP addresses make it possible for any host to communicate with any other, regardless of location or physical network type
- An IPv4 address is composed of **32-bits (4 bytes)** and has both *a host portion, which identifies a specific host* and *a network portion which identifies which network the host belongs to*.
- A **subnet mask** is used to differentiate *what portion of the address is the host portion and what portion is the network*.

#### Addressing Classes
| **IP Address Class**               | **Class A** | **Class B** | **Class C** |
| ---------------------------------- | ----------- | ----------- | ----------- |
| First bit values (binary)          | 0           | 10          | 110         |
| First byte value (decimal)         | 0-127       | 128-191     | 192-223     |
| Number of network identifiers bits | 8           | 16          | 24          |
| Number of host identifier bits     | 24          | 16          | 8           |
| Number of possible networks        | 126         | 16,384      | 2,097,152   |
| Number of possible hosts           | 16,777,214  | 65,534      | 254         |
 There is also a Class D which is used for multicast and a Class E which is used for experimental purposes.
