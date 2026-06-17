---
category: knowledge
tags:
  - networking
platform: n/a
status: done
created: 2026-06-17
aliases:
  - Two tier / Collapsed Core
---

- Redundancy is important while building a network
- Two is one, one is none
# Two tier / Collapsed Core
- Core switch is collapsed into distributed switch
- Used by businesses of smaller scale or business in budget
- Its not about how many employees we have its about how many buildings a business has
- Does all kinds of routing, packet switching, QOS
![[images/two_tier.png]]
# Three tier
- Network spans around multiple buildings
- Does nothing expect than transfer data as fast as possible
- In case of just couple of buildings we can use LAG/Ether channels but as the number of buildings grow it makes the network more messy so we use three tier architecture
![[images/three_tier.png]]
# Spine-Leaf Architecture(Easy-West traffic)
- Mostly used in data centers
- Spine is the backbone, servers connect to leaves
- Full mesh between spine and leaf
- Very fast traffic flow - combines traffic
![[images/spine_leaf.png]]



LAG(link aggregation) interface/Ether channel - Taking bandwidth from multiple links and bundles them together
ASIC - Application-Specific Integrated Circuit
