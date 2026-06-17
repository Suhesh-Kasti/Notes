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

- Has the technical properties of a physical layer two network without the physical constraints
- Hosts in one VLAN cannot communicate with hosts in another without using a router or some other layer three device to route traffic between the two.
- Like any physical network, VLANs represents a single broadcast domain.
- VLANs are not dependent on network dedicated physical connections, member hosts can be located on any switch where that VLAN is available and trunked and a host can even belong to several VLANs.
#### **VLAN Tagging**
- Using VLANs adds a 32-bit (4 byte) sub header to Ethernet frames where necessary; typically internally within a switch and across switch to switch links (trunks) that carry multiple VLANs.
- That header is called a VLAN tag which identifies to which VLAN the frame belongs to.
#### **VLAN Trunking**
1. **Access mode (Untagged mode)**
   - Single VLAN in the port
   - When sending and receiving frames to and from connected host, no tag is used
   - A tag may still be added if the frames cross a trunk port
2. **Trunk mode (Tagged mode)**
   - Multiple VLANs on a single port
   - Each frame being sent or received with a tag to identify the VLAN it belongs to
   - A trunk ports on each switches will serve as a passage between them, identifying every VLAN used in the network
![[images/trunk_port_passage.png]]
**Note**: We could actually not use a trunk (and therefore VLAN tagging) but instead we’d need to use a dedicated port on each switch for every VLAN used across the two which would be very wasteful. In the above example we’d use three ports per switch instead of just one per switch
