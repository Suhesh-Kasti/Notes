---
category:
  - CCNA
  - Networking
tags:
  - cables
  - ethernet
  - fiber
published: false
date: 2024-07-19T16:18:00
excalidraw-plugin: parsed
excalidraw-open-md: true
---
# Copper cable / Ethernet
100 meters is maximum ethernet cable can support without attenuation. Comes in a lot of colors not for aesthetic purpose but color coding that can be used to avoid confusion 
**Types of Ethernet:**
1. CAT 5E
2. CAT 6
**Grades of ethernet cable:**
1. Plenum cable: Cables made with more resistance capability cuz they run through plenum space
2. Riser cable: Normal ethernet cable that we use
   
   ![[cabling.png]]
1. **Spool cables** are long ethernet cables that run through the entire building through a plenum space(Ghar mathi ko ceiling ko area)
2. **Patch panel** is a junction point where the end of the spool cable meet and with a lot of network jacks in the facade. This is usually used for the flexibility of the switch
3. **Patch cables** are riser grade cables that aren't used in plenum space but through patch panels to switch and servers

# Fiber optics cables
### Fiber diameters
**Core**(Glass) + **Cladding**(Glass) + **Buffer**(Plastic)
![[fiber.png]]
Core is where light travels, cladding makes sure the light rays doesn't leave the inside of the cable
Most fiber is around 125 microns(millionth of a meter)
## Types of fiber cables:

| Single Mode Fiber(SMF)            | Multi Mode Fiber(MMF)              |
| --------------------------------- | ---------------------------------- |
| Small, glass core                 | Thicker, plastic core              |
| Long distance                     | Short distance                     |
| More expensive                    | Cheaper, easier to handle          |
| More bandwidth                    | Less bandwidth                     |
| Yellow color                      | Aqua or Orange colored             |
| Usually 9/125 microns at the core | Usually 50/125 microns at the core |
## Fiber Interfaces
![[fiber_interfaces.png]]
Fiber can not perform anything except data transfer thus the two ends in which one is send and another one is receive.  
Fiber splicing is pretty complex and requires specialized technicians.
![[fiber_splicing.png]]


%%
## Drawing
```compressed-json
N4IgLgngDgpiBcIYA8DGBDANgSwCYCd0B3EAGhADcZ8BnbAewDsEAmcm+gV31TkQAswYKDXgB6MQHNsYfpwBGAOlT0AtmIBeNCtlQbs6RmPry6uA4wC0KDDgLFLUTJ2lH8MTDHQ0YNMWHRJMRZFEIAOMiRPVRhGMBoEAG0AXXJ0KCgAZQCwPlBJfDxM7A0+Rk5MTHIdGCIAIXRUAGsCrkZcAGF6THp8BBAAYgAzEdGQAF9xoA===
```
%%