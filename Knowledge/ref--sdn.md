---
category: knowledge
tags:
  - networking
platform: n/a
status: done
created: 2026-06-17
aliases:
  - Planes
---

# Planes
1. **Management Plane**
   How we manage our devices
   Telnet, SSH, SNMP, APIs
2. **Control Plane**
   The BRAIN. Control everything that happens within the switch or router specially how data flows. Everything that decides how packet flows in network devices
   [[OSPF]], NAT, ACL, STP, CDP, VTP, QOS, Mac Address Table
3. **Data Plane**
   Everything in control plane controls how entities in data plane act. Anything and everything that's sending, receiving, processing data.
   Encapsulation/Decapsulation, Matching Layer 2 data with Mac Address Table(Mac Address table is still formed and filled by control plane but data plane is incharge of matching it up when frames come in), Dropping Traffic

   ![[images/Data_Control_Management_Planes.png]]

Distributed Control Plane
Every device calls the shots for their own control planes
![[images/Distributed_Control_Plane.png]]

Controller Based Networking
SDN Controller controls the control plane of each device as a centralized control plane
![[images/Controller_Based_Networking_Zombie.png]]
SDN is all about going from distributed control plane to centralized control plane... removing brain from our network devices and putting in a SDN controller

South Bound Interface (SBI) control devices using
OpenFlow
OpFLex
CLI/SNMP
NETCONF

North Bound Interface(NBI) is how we access our network
GUI we can use
Rest API
### Need of SDN Controllers

## Software Defined Architecture
- All link are made Layer 3 routed link
- Everything is setup using OSPF. We are creating an underlay
- All we care about is creating redundant layer 3 links
- Underlay: physical network that provides connectivity for the overlay
- Overlay: virtual network tunneled over our underlay devices
- The Technology used for tunneling is VXLAN(Virtual Extensible LAN) and it tries to make every communication in the network virtually one hop away
- Fabric: Overlay + Underlay + Every devices used

### ACI (Application CentricInfrastructure)
Data Center automation
Spine/Leaf
![[images/Spine_Leaf_in_data_center.png]]
Everything is connected with Layer 3 connections all running some kinds of routing connection making it redundant with equal cost
The SDN Controller is called the APIC(Application Policy Infrastructure Controller)
In Data Centers, this spine-leaf architecture is the underlay and APIC provides the overlay for us to interact with and control everything with intent

3 tier web application
DB -> Apps -> Web
And they will be placed in their own end point groups
Policy in ACI are what rules dictate how they communicate and rules apply in the logic
I just decide which servers are which like which servers are database servers and put them in DBs endpoint groups accordingly. (Intent Based)

[Learn ACI](https://developer.cisco.com/site/aci/)
[Always on DevNet ACI Sandbox](https://devnetsandbox.cisco.com/DevNet/catalog/ACI-Simulator-Always-On)
[Cisco Dcloud Labs](https://dcloud2-sng.cisco.com/)
