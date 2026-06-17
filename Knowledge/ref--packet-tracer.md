---
category: knowledge
tags:
  - networking
platform: n/a
status: done
created: 2026-06-17
aliases:
  - 1. Building a simple network
---

# 1. Building a simple network
1. Drag and drop a PC, an access layer switch, core switches and a router
2. Connect them using "Automatically connect option ⚡️"
3. Click on multilayered switches and drag and drop the power supply
4. Configuring the router using the CLI
   - Enable privilege level 15 mode using command: `enable 15`
   - Turn on configuration mode on the current terminal with command: `configure terminal`
   - Goto a specific interface using the command: `interface $INTERFACE` eg. `interface gig 0/0`
   - Activate the interface using the command `no shutdown`
![[images/packettracer-basic.png]]
# 2. Getting physical view
1. Click on the physical tab
2. Click on 🧭 and select the view you want and select jump to selected location or click on 🏠️ to access the rack
   ![[images/packettracer-rack.png]]
# 3. Simulating Traffic
1. Assign ip address to interface of router using the command: `ip address $IP_ADDRESS $NETMASK`
   > We can check for interface using command `show ip interface brief`
2. Configure the endpoint device IP and subnet mask
   > We can ping the router from the device using the command prompt
3. We can use the 'SIMULATION' tab to simulate individual traffics
4. Simulating requests
 -   ICMP request
    -  Click on the ✉️ icon then choose the source and destination device to simulate a ICMP echo request
  - ARP
    -  Use the command prompt to send a ping to host that doesn't exist and inspect the packet
  - HTTP
    - Add a web server then connect it using a fast ethernet
    - Enable web services in the server
    - Browse the website from the host endpoint
    - Inspect the packet
