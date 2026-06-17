---
category: knowledge
tags:
  - f5
platform: n/a
status: done
created: 2026-06-17
aliases:
  - Header
---

The data link layer can be subdivided into two layers, the Media Access Control (MAC) Layer and the Logical Link Control (LLC) layer.
### Logical Link Layer(LLC)
- Frame Synchronization
- Provides a degree of error checking
### MAC Addressing
48 bits(6 bytes) where first 24 represent vendor and last 24 identify the device
#### MAC Address Table
MAC address table learns and stores mac address and port the device is connected to. When the switch receives a frame from a host it will forward the frames out of corresponding port in that table.
# Header
Are added to encapsulate the data
- Destination MAC Address: six bytes
- Source MAC Address: six bytes
- 802.1Q tag ([[Virtual LAN ( VLAN )#**VLAN Tagging**]] is used): four bytes
- Lenght of frame: two bytes
- Frame check sequence: four bytes
# Carrier Sense Multiple Access / Collision Detection (CSMA/CD)
### Carrier Sense Multiple Access
**Carrier Sense:** When a host needs to send out frames on ethernet, it begins by listening on the interface and sensing if there are any traffic being transmitted
**Multiple Access:**  Each host on the network shares the same medium
**HOW??** If the network is busy, the host waits for a random period and then listens again until the network is not idle to prevent collision
### Collision Detection
- Hosts can receive corrupted data if collsion occurs.
- It checks if there has been a collision on the network.
	- A **[[Switch]]** divides every port into a separate collision domain which means that every port acts as a dedicated layer two network, which significantly reduces, or even eliminates collisions. It does this using "Store and Forward" method where it stores and forwards request.
With collision detection, when a collision occurs the sending hosts detect it, immediately stop sending data and sends out a jam signal to alert other hosts on the network that a collision has taken place. When a receiving host gets the jam signal it drops all partial frames it has received. After a host has transmitted the jam signal it waits for a random period of time before attempting to re-transmit any data (and repeats the carrier sense phase). This is sometimes called a back off period. Both hosts involved in the collision have their own random time to wait before attempting to send the data again
## Broadcast Domain
- A layer two broadcast frame is sent to FF:FF:FF:FF:FF:FF which is accepted and inspected by every host.
- A **broadcast domain** is defined as the group of hosts that will receive a broadcast message transmitted by any one of the group’s members.
- A broadcast domain can contain multiple collision domains.
- [[Dividing a broadcast domain]] can improve network efficiency by reducing unnecessary broadcast traffic that all devices must process.
# Address Resolution Protocol (ARP)
ARP’s purpose is to glue together (or map) layer three IP addresses to layer two MAC addresses.
When a host wishes to send a packet to an IP address, layer two needs to know the MAC address of the destination host. In order to get it, the host sends an ARP request for the IP address, a broadcast to all the hosts on the local layer two network.
If the IP address is a remote address (on a different logical, layer three network) it will instead send an ARP request for the default gateway’s MAC address because that will handle the traffic.
![[images/arp_request_flow.png]]

1. The host sending data checks its own ARP table and if the address does not exist it generates an ARP request containing the following
	   a. Its own (source) IP address and MAC address
	   b. The IP address of the receiving host
	   c. Destination MAC address: FF:FF:FF:FF:FF:FF
2. The sending host sends out the ARP request as a broadcast within its broadcast domain.
3. The hosts within the broadcast domain that receive the ARP request examine it and check if it is requesting their own IP address and MAC address. If it isn’t, it discards the packet silently.
4. When the correct host picks up the packet it will send a reply back to the sender. This packet is called an ARP Reply (or response). The host will use its own IP address and MAC address in the reply and send the ARP reply back to the original sender.
5. When the sending host receives the MAC address of the requesting host, it stores this information in its ARP cache and then proceeds with sending the intended packet using the MAC address it just received.

# [[Virtual LAN ( VLAN ) ]]
A virtual LAN (VLAN) is a logical overlay network that groups together a subset of devices that share a physical LAN, isolating the traffic for each group.

# Link Aggregation Control Protocol (LACP)
Link Aggregation Control Protocol is a protocol that combines (or bundles) several physical Ethernet interfaces into a single logical link that operates using one MAC address, as if it were a single physical interface. This technology is known by many different names depending on which vendor provides it. For instance Cisco has called their link aggregation technology EtherChannel (but note use of LACP is optional) and other vendors use the names teaming or trunking. LACP is standardized under the IEEE standard, 802.3ad or 802.1ax.
> **Note:** An F5 device also uses trunk ports but it means something completely different. *In F5, a trunk port is the same as Link Aggregation Control Protocol (LACP)* which means that you combine several Ethernet connections into one logical link that operates under one MAC address.

The two main advantages of using LACP (or any similar technology) are *improved reliability* and *aggregated throughput*.
If one of the physical links in a bundle suffers from a failure, the device keeps transmitting and receiving both outgoing and incoming frames on the other physical links that are still active. This technology is so seamless that a user or an application will not usually experience any issues.
