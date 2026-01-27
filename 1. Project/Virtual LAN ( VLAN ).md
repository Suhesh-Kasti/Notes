---
category:
  - BigIP
  - f5
  - LTM
  - Networking
tags:
  - virtual_local_area_network
  - vlan_tagging
  - vlan_trunking
  - vlan
published: false
date: 2024-09-30T14:32:00
excalidraw-plugin: parsed
excalidraw-open-md: true
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
![[trunk_port_passage.png]]
**Note**: We could actually not use a trunk (and therefore VLAN tagging) but instead we’d need to use a dedicated port on each switch for every VLAN used across the two which would be very wasteful. In the above example we’d use three ports per switch instead of just one per switch





%%
# Excalidraw Data
## Text Elements
%%
## Drawing
```compressed-json
N4KAkARALgngDgUwgLgAQQQDwMYEMA2AlgCYBOuA7hADTgQBuCpAzoQPYB2KqATLZMzYBXUtiRoIACyhQ4zZAHoFAc0JRJQgEYA6bGwC2CgF7N6hbEcK4OCtptbErHALRY8RMpWdx8Q1TdIEfARcZgRmBShcZQUebTiADho6IIR9BA4oZm4AbXAwUDAiiBJuCAAxAEYeAFEAGSEAaQAlTShiAC0ASQBrAHkAYQoARyFiADZkoshYRDKAM0CETyp+

YsxuHgB2AGZtLYBWNcgYbmcdhK3jiAoSdW4ABm0Hl8rryQRCZWlH59fr6zKYKPa7MKCkNg9BADNj4NikMoAYkqCBRKKmxU0uGwPWUEKEHGIMLhCIk4OszDguECmQxkHmhHw+AAyrBgRJBB46RAwRCoQB1O6STag8GQhCsmDs9Cc0rXfHfDjhbJoN75SBsKnYNSnVUva544RwLrEFWoHIAXWui1w6RN3A4QiZ10IhKwZVwD25+MJSuYZsdzvVPIQy

24lUOCQALJUdgdKuNrowWOwuGgjsHk6xOAA5ThiTZRqM7ACcWwjfGDhGYABFUlAw2hwUIENdNMJCTVgulMgGnfhrkI4MRcA3iOGtjxYwl41txlGHmrphAiBweg7+9c4TjG6h5gQwtc4GxXVlcuqwHlpkUHscbxerRer9eni9F3ewK/Xg/1Y/l3BAn9ERwlyP9ilYfQnVHBAAAVAOYYDuGbVtg3wUIoBhfR9DUMcYJPWk0GfG8/nfC8v0XX98gAXz

WQpilKCQhB4DpnAAQXGYZWNwHgowAITEGBmQACQADWcGoAH1uVmcR0EWUMVm5DY0C2BJxn2DNl11VBnCjA4EmuW5iHuNByKXYoPi+H5TJI8zIEBaVb2DXlxWJeEkTRVEkDbbFcR9IlYXcslyA4SlqQyKBuQZJlJWlHlYTlZyxQFIURSSvkJTZWT4q5eVhEVZVw2uTVsR1cN9WDQ0hxNM1LWtcg7XHNBAwHKs3WU9BcEqb0O2IP0+yDZcwl3HgHhL

KNxhLA4Sx4pMmGzNNUE04os1TPMOALNAdkqB4EkqGddpdWt613ZC216rs0gigbWuXIcRzHCcpwueMEh2csdi3V112azdULYHcmr3A8UP/fCz0Ip8L0/D8HgfO8iOIt87KR79rwtX8j3g4DarAgRCEgtCGzg5VEKbUgWy3dDMOwmRljw09zxfWy7zMyiiio8A/wgXA4DgVloO4OjoA+dIyiIb5IrWBhCAQCheN8qrCTc0l0EReYNc1jEIGwEQaSgL

oG30VkMpVjyvPRaXddIfXDbSBWcSVgKSTKclQqpfXtet22jfKRkWSyspZXHK29Yiu3jeShBBWM4U0ErYpvfDo2TfFWLsuDr2w8yCPmnyyR+qK/Idezg2jb6LUyr1JzE9LiPyk4KByltRltPMkubeTtIG8yZlCCMWTRtDzuc6NgAVLAoFYiXFpXBB5il4uk9HtIBdIKebbYCgPlwIGWuHn20hqQlWM37eQiBnmz+15hsAhJkRO4VT1MOaXb/v/AAE

1uAmgzi6MNgBghaZgIC2cM1ED5d30HnAkfVCoSH8trPEJA+4Dw3INSAyDnZBVQHRSAvFYSX0RAMEsJCSHlHKNyZoCBlBQVVhARENQaxMKYRQiAECl6l1TlCCuUBUw3WlgBBAZhhDMAAOKkBQf3WS+9i42nSNQt0kiODKGAcuDIuBNDBCBmdYM2AiBwCQhTUGxQOC2lkro5cwgoCrgscYjhxQ7AACsEDYCyMyMxcAACybBiAIGPpo7R3B9z4DCOAG

idBoogTQMATmVEgA
```
%%