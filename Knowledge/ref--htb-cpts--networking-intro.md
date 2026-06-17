---
category: knowledge
tags:
  - dns
platform: n/a
status: done
created: 2026-06-17
aliases:
  - Introduction to Networking
---

# Introduction to Networking

Tags: #🧑‍🎓
Related to:
See also:
Previous: [[HTB Academy]]

![[images/logo_introduction_to_networking.png]]

As an information security professional, a firm grasp of networking fundamentals and the required components is necessary. Without a strong foundation in networking, it will be tough to progress in any area of information security. Understanding how a network is structured and how the communication between the individual hosts and servers takes place using the various protocols allows us to understand the entire network structure and its network traffic in detail and how different communication standards are handled. This knowledge is essential to create our tools and to interact with the protocols.

### Module Summary

This module covers core networking concepts that are fundamental for any IT professional.

This module will cover the following topics:

-   The structure and design of the Internet
-   Which topologies are used
-   What for and what role the proxies play in the networks
-   Internet communication models and concepts
-   The difference between the OSI model and TCP/IP
-   How IPv4/IPv6 addressing is done in various networks

You can start and stop the module at any time and pick up where you left off. There is no time limit or "grading," but you must complete all sections to receive the maximum number of cubes and have this module marked as complete in any paths you have chosen.

The module is classified as "Fundamental," and the information taught within is crucial to be successful in any technical field.

# Introduction

## Networking Overview

* * * * *

A network enables two computers to communicate with each other. There is a wide array of `topologies` (mesh/tree/star), `mediums` (ethernet/fiber/coax/wireless), and `protocols` (TCP/UDP/IPX) that can be used to facilitate the network. It is important as security professionals to understand networking because when the network fails, the error may be silent, causing us to miss something.

Setting up a large, flat network is not extremely difficult, and it can be a reliable network, at least operationally. However, a flat network is like building a house on a land plot and considering it secure because it has a lock on the door. By creating lots of smaller networks and having them communicate, we can add defense layers. Pivoting around a network is not difficult, but doing it quickly and silently is tough and will slow attackers down. Back to the house scenario, let's walk through the following examples:

#### Example No. 1

Building smaller networks and putting Access Control Lists around them is like putting a fence around the property's border that creates specific entry and exit points. Yes, an attacker could jump over the fence, but this looks suspicious and is not common, allowing it to be quickly detected as malicious activity. Why is the printer network talking to the servers over HTTP?

#### Example No. 2

Taking the time to map out and document each network's purpose is like placing lights around the property, making sure all activity can be seen. Why is the printer network talking to the internet at all?

#### Example No. 3

Having bushes around windows is a deterrent to people attempting to open the window. Just like Intrusion Detection Systems like Suricata or Snort are a deterrent to running network scans. Why did a port scan originate from the printer network?

These examples may sound silly, and it is common sense to block a printer from doing all of the above. However, if the printer is on a "flat /24 network" and gets a DHCP address, it can be challenging to place these types of restrictions on them.

* * * * *

### Story Time - A Pentesters Oversight
-----------------------------------

Most networks use a `/24` subnet, so much so that many Penetration Testers will set this subnet mask (255.255.255.0) without checking. The /24 network allows computers to talk to each other as long as the first three octets of an IP Address are the same (ex: 192.168.1.xxx). Setting the subnet mask to `/25` divides this range in half, and the computer will be able to talk to only the computers on "its half." We have seen Penetration Test reports where the assessor claimed a Domain Controller was offline when it was just on a different network in reality. The network structure was something like this:

-   Server Gateway: 10.20.0.1/25
-   Domain Controller: 10.20.0.10/25
-   Client Gateway: 10.20.0.129/25
-   Client Workstation: 10.20.0.200/25
-   Pentester IP: 10.20.0.252/24 (Set Gateway to 10.20.0.1)

The Pentester communicated with the Client Workstations and thought they did an excellent job because they managed to steal a workstation password via Impacket. However, due to a failure to understand the network, they never managed to get off the Client Network and reach more "high value" targets such as database servers. Hopefully, if this sounds confusing to you, you can come back to this statement at the end of the module and understand it!

* * * * *

### Basic Information
-----------------

Let us look at the following high-level diagram of how a Work From Home setup may work.

![[images/net_overview.png]]

* * * * *

The entire internet is based on many subdivided networks, as shown in the example and marked as "`Home Network`" and "`Company Network`." We can imagine `networking` as the delivery of mail or packages sent by one computer and received by the other.

Suppose we imagine as a scenario that we want to visit a company's website from our "`Home Network`." In that case, we exchange data with the company's website located in their "`Company Network`." As with sending mail or packets, we know the address where the packets should go. The website address or `Uniform Resource Locator` (`URL`) which we enter into our browser is also known as `Fully Qualified Domain Name` (`FQDN`).

The difference between `URL`s and `FQDN`s is that:

-   an `FQDN` (`www.hackthebox.eu`) only specifies the address of the "building" and
-   an `URL` (`https://www.hackthebox.eu/example?floor=2&office=dev&employee=17`) also specifies the "`floor`," "`office`," "`mailbox`" and the corresponding "`employee`" for whom the package is intended.

We will discuss the exact representations and definitions more clearly and precisely in other sections.

The fact is that we know the address, but not the exact geographical location of the address. In this situation, the post office can determine the exact location, which then forwards the packets to the desired location. Therefore, our post office forwards our packets to the main post office, representing our `Internet Service Provider` (`ISP`).

Our post office is our `router` which we utilize to connect to the "`Internet`" in networking.

As soon as we send our packet through our post office (`router`), the packet is forwarded to the `main post office` (`ISP`). This main post office looks in the `address register`/`phonebook` (`Domain Name Service`) where this address is located and returns the corresponding geographical coordinates (`IP address`). Now that we know the address's exact location, our packet is sent directly there by a direct flight via our main post office.

After the web server has received our packet with the request of what their website looks like, the webserver sends us back the packet with the data for the presentation of the website via the post office (`router`) of the "`Company Network`" to the specified return address (`our IP address`).

* * * * *

### Extra Points
------------

In that diagram, I would hope the company network shown consists of five separate networks!

1.  The Web Server should be in a DMZ (Demilitarized Zone) because clients on the internet can initiate communications with the website, making it more likely to become compromised. Placing it in a separate network allows the administrators to put networking protections between the web server and other devices.

2.  Workstations should be on their own network, and in a perfect world, each workstation should have a Host-Based Firewall rule preventing it from talking to other workstations. If a Workstation is on the same network as a Server, networking attacks like `spoofing` or `man in the middle` become much more of an issue.

3.  The Switch and Router should be on an "Administration Network." This prevents workstations from snooping in on any communication between these devices. I have often performed a Penetration Test and saw `OSPF` (Open Shortest Path First) advertisements. Since the router did not have a `trusted network`, anyone on the internal network could have sent a malicious advertisement and performed a `man in the middle` attack against any network.

4.  IP Phones should be on their own network. Security-wise this is to prevent computers from being able to eavesdrop on communication. In addition to security, phones are unique in the sense that latency/lag is significant. Placing them on their own network can allow network administrators to prioritize their traffic to prevent high latency more easily.

5.  Printers should be on their own network. This may sound weird, but it is next to impossible to secure a printer. Due to how Windows works, if a printer tells a computer authentication is required during a print job, that computer will attempt an `NTLMv2` authentication, which can lead to passwords being stolen. Additionally, these devices are great for persistence and, in general, have tons of sensitive information sent to them.

* * * * *

### Fun Story
---------

During COVID, I was tasked to perform a `Physical Penetration Test` across state lines, and my state was under a `stay at home` order. The company I was testing had minimal staff in the office. I decided to purchase an expensive printer and exploited it to put a [[vuln--reverse-shell-bind-shell]] in it, so when it connected to the network, it would send me a shell (remote access). Then I shipped the printer to the company and sent a phishing email thanking the staff for coming in and explaining that the printer should allow them to print or scan things more quickly if they want to bring some stuff home to WFH for a few days. The printer was hooked up almost instantly, and their domain administrator's computer was kind enough to send the printer his credentials!

If the client had designed a secure network, this attack probably would not have been possible for many reasons:

-   Printer should not have been able to talk to the internet
-   Workstation should not have been able to communicate to the printer over port 445
-   Printer should not be able to initiate connections to workstations. In some cases, printer/scanner combinations should be able to communicate to a mail server to email scanned documents.

# Networking Structure

## Network Types

* * * * *

Each network is structured differently and can be set up individually. For this reason, so-called `types` and `topologies` have been developed that can be used to categorize these networks. When reading about all the types of networks, it can be a bit of information overload as some network types include the geographical range. We rarely hear some of the terminologies in practice, so this section will be broken up into `Common Terms` and `Book Terms`. Book terms are good to know, as there has been a single documented case of an email server failing to deliver emails longer than 500 miles but don't be expected to be able to recite them on demand unless you are studying for a networking exam.

#### Common Terminology

| Network Type | Definition |
| --- | --- |
| Wide Area Network (WAN) | Internet |
| Local Area Network (LAN) | Internal Networks (Ex: Home or Office) |
| Wireless Local Area Network (WLAN) | Internal Networks accessible over Wi-Fi |
| Virtual Private Network (VPN) | Connects multiple network sites to one `LAN` |

* * * * *

### WAN
---

The WAN (Wide Area Network) is commonly referred to as `The Internet`. When dealing with networking equipment, we'll often have a WAN Address and LAN Address. The WAN one is the address that is generally accessed by the Internet. That being said, it is not inclusive to the Internet; a WAN is just a large number of LANs joined together. Many large companies or government agencies will have an "Internal WAN" (also called Intranet, Airgap Network, etc.). Generally speaking, the primary way we identify if the network is a WAN is to use a WAN Specific routing protocol such as BGP and if the IP Schema in use is not within RFC 1918 (10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16).

* * * * *

### LAN / WLAN
----------

LANs (Local Area Network) and WLANs (Wireless Local Area Network) will typically assign IP Addresses designated for local use (RFC 1918, 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16). In some cases, like some colleges or hotels, you may be assigned a routable (internet) IP Address from joining their LAN, but that is much less common. There's nothing different between a LAN or WLAN, other than WLAN's introduce the ability to transmit data without cables. It is mainly a security designation.

* * * * *

### VPN
---

There are three main types `Virtual Private Networks` (`VPN`), but all three have the same goal of making the user feel as if they were plugged into a different network.

#### Site-To-Site VPN

Both the client and server are Network Devices, typically either `Routers` or `Firewalls`, and share entire network ranges. This is most commonly used to join company networks together over the Internet, allowing multiple locations to communicate over the Internet as if they were local.

#### Remote Access VPN

This involves the client's computer creating a virtual interface that behaves as if it is on a client's network. Hack The Box utilizes `OpenVPN`, which makes a TUN Adapter letting us access the labs. When analyzing these VPNs, an important piece to consider is the routing table that is created when joining the VPN. If the VPN only creates routes for specific networks (ex: 10.10.10.0/24), this is called a `Split-Tunnel VPN`, meaning the Internet connection is not going out of the VPN. This is great for Hack The Box because it provides access to the Lab without the privacy concern of monitoring your internet connection. However, for a company, `split-tunnel` VPN's are typically not ideal because if the machine is infected with malware, network-based detection methods will most likely not work as that traffic goes out the Internet.

#### SSL VPN

This is essentially a VPN that is done within our web browser and is becoming increasingly common as web browsers are becoming capable of doing anything. Typically these will stream applications or entire desktop sessions to your web browser. A great example of this would be the HackTheBox Pwnbox.

* * * * *

### Book Terms
----------

| Network Type | Definition |
| --- | --- |
| Global Area Network (GAN) | Global network (the Internet) |
| Metropolitan Area Network (MAN) | Regional network (multiple LANs) |
| Wireless Personal Area Network (WPAN) | Personal network (Bluetooth) |

#### GAN

A worldwide network such as the `Internet` is known as a `Global Area Network` (`GAN`). However, the Internet is not the only computer network of this kind. Internationally active companies also maintain isolated networks that span several `WAN`s and connect company computers worldwide. `GAN`s use the glass fibers infrastructure of wide-area networks and interconnect them by international undersea cables or satellite transmission.

#### MAN

`Metropolitan Area Network` (`MAN`) is a broadband telecommunications network that connects several `LAN`s in geographical proximity. As a rule, these are individual branches of a company connected to a `MAN` via leased lines. High-performance routers and high-performance connections based on glass fibers are used, which enable a significantly higher data throughput than the Internet. The transmission speed between two remote nodes is comparable to communication within a `LAN`.

Internationally operating network operators provide the infrastructure for `MAN`s. Cities wired as `Metropolitan Area Networks` can be integrated supra-regionally in `Wide Area Networks` (`WAN`) and internationally in `Global Area Networks` (`GAN`).

#### PAN / WPAN

Modern end devices such as smartphones, tablets, laptops, or desktop computers can be connected ad hoc to form a network to enable data exchange. This can be done by cable in the form of a `Personal Area Network` (`PAN`).

The wireless variant `Wireless Personal Area Network` (`WPAN`) is based on Bluetooth or Wireless USB technologies. A `wireless personal area network` that is established via Bluetooth is called `Piconet`. `PAN`s and `WPAN`s usually extend only a few meters and are therefore not suitable for connecting devices in separate rooms or even buildings.

In the context of the `Internet of Things` (`IoT`), `WPAN`s are used to communicate control and monitor applications with low data rates. Protocols such as Insteon, Z-Wave, and ZigBee were explicitly designed for smart homes and home automation.

## Networking Topologies

* * * * *

A `network topology` is a typical arrangement and `physical` or `logical` connection of devices in a network. Computers are `hosts`, such as `clients` and `servers`, that actively use the network. They also include `network components` such as `switches`, `bridges`, and `routers`, which we will discuss in more detail in later sections, which have a distribution function and ensure that all network hosts can establish a logical connection with each other. The network topology determines the components to be used and the access methods to the transmission media.

The `transmission medium layout` used to connect devices is the physical topology of the network. For conductive or glass fiber media, this refers to the cabling plan, the positions of the `nodes`, and the connections between the nodes and the cabling. In contrast, the `logical topology` is how the signals act on the network media or how the data will be transmitted across the network from one device to the devices' physical connection.

* * * * *

We can divide the entire network topology area into three areas:

#### 1. Connections

| `Wired connections` | `Wireless connections` |
| --- | --- |
| Coaxial cabling | Wi-Fi |
| Glass fiber cabling | Cellular |
| Twisted-pair cabling | Satellite |
| and others | and others |

* * * * *

#### 2. Nodes - Network Interface Controller (NICs)

|  |  |  |  |
| --- | --- | --- | --- |
| Repeaters | Hubs | Bridges | Switches |
| Router/Modem | Gateways | Firewalls |  |

Network nodes are the `transmission medium's connection points` to transmitters and receivers of electrical, optical, or radio signals in the medium. A node may be connected to a computer, but certain types may have only one microcontroller on a node or may have no programmable device at all.

* * * * *

#### 3. Classifications

We can imagine a topology as a virtual form or `structure of a network`. This form does not necessarily correspond to the actual physical arrangement of the devices in the network. Therefore these topologies can be either `physical` or `logical`. For example, the computers on a `LAN` may be arranged in a circle in a bedroom, but it is very unlikely to have an actual ring topology.

Network topologies are divided into the following eight basic types:

|  |  |
| --- | --- |
| Point-to-Point | Bus |
| Star | Ring |
| Mesh | Tree |
| Hybrid | Daisy Chain |

More complex networks can be built as hybrids of two or more of the basic topologies mentioned above.

* * * * *

### Point-to-Point
--------------

The simplest network topology with a dedicated connection between two hosts is the `point-to-point` topology. In this topology, a direct and straightforward physical link exists only between `two hosts`. These two devices can use these connections for mutual communication.

`Point-to-point` topologies are the basic model of traditional telephony and must not be confused with `P2P` (`Peer-to-Peer` architecture).

#### Point-To-Point Topology

![[images/topo_p2p.png]]

* * * * *

### Bus
---

All hosts are connected via a transmission medium in the bus topology. Every host has access to the transmission medium and the signals that are transmitted over it. There is no central network component that controls the processes on it. The transmission medium for this can be, for example, a `coaxial cable`.

Since the medium is shared with all the others, only `one host can send`, and all the others can only receive and evaluate the data and see whether it is intended for itself.

#### Bus Topology

![[images/topo_bus.png]]

* * * * *

### Star
----

The star topology is a network component that maintains a connection to all hosts. Each host is connected to the `central network component` via a separate link. This is usually a router, a hub, or a switch. These handle the `forwarding function` for the data packets. To do this, the data packets are received and forwarded to the destination. The data traffic on the central network component can be very high since all data and connections go through it.

#### Star Topology

![[images/topo_star.png]]

* * * * *

### Ring
----

The `physical` ring topology is such that each host or node is connected to the ring with two cables:

-   One for the `incoming` signals and
-   the another for the `outgoing` ones.

This means that one cable arrives at each host and one cable leaves. The ring topology typically does not require an active network component. The control and access to the transmission medium are regulated by a protocol to which all stations adhere.

A `logical` ring topology is based on a physical star topology, where a distributor at the node simulates the ring by forwarding from one port to the next.

The information is transmitted in a predetermined transmission direction. Typically, the transmission medium is accessed sequentially from station to station using a retrieval system from the central station or a `token`. A token is a bit pattern that continually passes through a ring network in one direction, which works according to the `claim token process`.

#### Ring Topology

![[images/topo_ring.png]]

* * * * *

### Mesh
----

Many nodes decide about the connections on a `physical` level and the routing on a `logical` level in meshed networks. Therefore, meshed structures have no fixed topology. There are two basic structures from the basic concept: the `fully meshed` and the `partially meshed` structure.

Each host is connected to every other host in the network in a `fully meshed structure`. This means that the hosts are meshed with each other. This technique is primarily used in `WAN` or `MAN` to ensure high reliability and bandwidth.

In this setup, important network nodes such as routers could be networked together. If one router fails, the others can continue to work without problems, and the network can absorb the failure due to the many connections.

Each node of a fully meshed topology has the same routing functions and knows the neighboring nodes it can communicate with proximity to the network gateway and traffic loads.

In the `partially meshed structure`, the endpoints are connected by only one connection. In this type of network topology, specific nodes are connected to exactly one other node, and some other nodes are connected to two or more other nodes with a point-to-point connection.

#### Mesh Topology

![[images/topo_mesh.png]]

* * * * *

### Tree
----

The tree topology is an extended star topology that more extensive local networks have in this structure. This is especially useful when several topologies are combined. This topology is often used, for example, in larger company buildings.

There are both logical tree structures according to the `spanning tree` and physical ones. Modular modern networks, based on structured cabling with a hub hierarchy, also have a tree structure. Tree topologies are also used for `broadband networks` and `city networks` (`MAN`).

#### Tree Topology

![[images/topo_tree.png]]

* * * * *

### Hybrid
------

Hybrid networks combine two or more topologies so that the resulting network does not present any standard topologies. For example, a tree network can represent a hybrid topology in which star networks are connected via interconnected bus networks. However, a tree network that is linked to another tree network is still topologically a tree network. A hybrid topology is always created when `two different` basic network topologies are interconnected.

#### Hybrid Topology

![[images/topo_hybrid.png]]

* * * * *

### Daisy Chain
-----------

In the daisy chain topology, multiple hosts are connected by placing a cable from one node to another.

Since this creates a chain of connections, it is also known as a daisy-chain configuration in which multiple hardware components are connected in a series. This type of networking is often found in automation technology (`CAN`).

Daisy chaining is based on the physical arrangement of the nodes, in contrast to token procedures, which are structural but can be made independent of the physical layout. The signal is sent to and from a component via its previous nodes to the computer system.

#### Daisy Chain Topology

![[images/topo_daisy-chain..png]]

## Proxies

* * * * *

Many people have different opinions on what a proxy is:

-   Security Professionals jump to `HTTP Proxies` (BurpSuite) or pivoting with a `SOCKS/SSH Proxy` (`Chisel`, `ptunnel`, `sshuttle`).

-   Web Developers use proxies like Cloudflare or ModSecurity to block malicious traffic.

-   Average people may think a proxy is used to obfuscate your location and access another country's Netflix catalog.

-   Law Enforcement often attributes proxies to illegal activity.

Not all the above examples are correct. A proxy is when a device or service sits in the middle of a connection and acts as a mediator. The `mediator` is the critical piece of information because it means the device in the middle must be able to inspect the contents of the traffic. Without the ability to be a `mediator`, the device is technically a `gateway`, not a proxy.

Back to the above question, the average person has a mistaken idea of what a proxy is as they are most likely using a VPN to obfuscate their location, which technically is not a proxy. Most people think whenever an IP Address changes, it is a proxy, and in most cases, it's probably best not to correct them as it is a common and harmless misconception. Correcting them could lead to a more extended conversation that trails into tabs vs. spaces, `emacs` vs. `vim`, or finding out they are a `nano` user.

If you have trouble remembering this, proxies will almost always operate at Layer 7 of the OSI Model. There are many types of proxy services, but the key ones are:

-   `Dedicated Proxy` / `Forward Proxy`
-   `Reverse Proxy`
-   `Transparent Proxy`

* * * * *

### Dedicated Proxy / Forward Proxy
-------------------------------

The `Forward Proxy`, is what most people imagine a proxy to be. A Forward Proxy is when a client makes a request to a computer, and that computer carries out the request.

For example, in a corporate network, sensitive computers may not have direct access to the Internet. To access a website, they must go through a proxy (or web filter). This can be an incredibly powerful line of defense against malware, as not only does it need to bypass the web filter (easy), but it would also need to be `proxy aware` or use a non-traditional C2 (a way for malware to receive tasking information). If the organization only utilizes `FireFox`, the likelihood of getting proxy-aware malware is improbable.

Web Browsers like Internet Explorer, Edge, or Chrome all obey the "System Proxy" settings by default. If the malware utilizes WinSock (Native Windows API), it will likely be proxy aware without any additional code. Firefox does not use `WinSock` and instead uses `libcurl`, which enables it to use the same code on any operating system. This means that the malware would need to look for Firefox and pull the proxy settings, which malware is highly unlikely to do.

Alternatively, malware could use DNS as a c2 mechanism, but if an organization is monitoring DNS (which is easily done using [Sysmon](https://medium.com/falconforce/sysmon-11-dns-improvements-and-filedelete-events-7a74f17ca842) ), this type of traffic should get caught quickly.

Another example of a Forward Proxy is Burp Suite, as most people utilize it to forward HTTP Requests. However, this application is the swiss army knife of HTTP Proxies and can be configured to be a reverse proxy or transparent!

#### Forward Proxy

![[images/forward_proxy.png]]

* * * * *

### Reverse Proxy
-------------

As you may have guessed, a `reverse proxy`, is the reverse of a `Forward Proxy`. Instead of being designed to filter outgoing requests, it filters incoming ones. The most common goal with a `Reverse Proxy`, is to listen on an address and forward it to a closed-off network.

Many organizations use CloudFlare as they have a robust network that can withstand most DDOS Attacks. By using Cloudflare, organizations have a way to filter the amount (and type) of traffic that gets sent to their webservers.

Penetration Testers will configure reverse proxies on infected endpoints. The infected endpoint will listen on a port and send any client that connects to the port back to the attacker through the infected endpoint. This is useful to bypass firewalls or evade logging. Organizations may have `IDS` (`Intrusion Detection Systems`), watching external web requests. If the attacker gains access to the organization over SSH, a reverse proxy can send web requests through the SSH Tunnel and evade the IDS.

Another common Reverse Proxy is `ModSecurity`, a `Web Application Firewall` (`WAF`). Web Application Firewalls inspect web requests for malicious content and block the request if it is malicious. If you want to learn more about this, we recommend reading into the [ModSecurity Core Rule Set](https://owasp.org/www-project-modsecurity-core-rule-set/), as its a great starting point. Cloudflare, also can act as a WAF but doing so requires letting them decrypt HTTPS Traffic, which some organizations may not want.

#### Reverse Proxy

![[images/reverse_proxy.png]]

* * * * *

### (Non-) Transparent Proxy
------------------------

All these proxy services act either `transparently` or `non-transparently`.

With a `transparent proxy`, the client doesn't know about its existence. The transparent proxy intercepts the client's communication requests to the Internet and acts as a substitute instance. To the outside, the transparent proxy, like the non-transparent proxy, acts as a communication partner.

If it is a `non-transparent proxy`, we must be informed about its existence. For this purpose, we and the software we want to use are given a special proxy configuration that ensures that traffic to the Internet is first addressed to the proxy. If this configuration does not exist, we cannot communicate via the proxy. However, since the proxy usually provides the only communication path to other networks, communication to the Internet is generally cut off without a corresponding proxy configuration.

# Networking Workflow

## Networking Models

* * * * *

Two networking models describe the communication and transfer of data from one host to another, called `ISO/OSI model` and the `TCP/IP model`. This is a simplified representation of the so-called `layers` representing transferred Bits in readable contents for us.

![[01 HTB/Academy/01. Pre-Engagement/04. Introduction to Networking/images/net_models4.png]]

* * * * *

## The OSI Model
-------------

The `OSI` model, often referred to as `ISO/OSI` layer model, is a reference model that can be used to describe and define the communication between systems. The reference model has `seven` individual layers, each with clearly separated tasks.

The term `OSI` stands for `Open Systems Interconnection` model, published by the `International Telecommunication Union` (`ITU`) and the `International Organization for Standardization` (`ISO`). Therefore, the `OSI` model is often referred to as the `ISO/OSI` layer model.

* * * * *

## The TCP/IP Model
----------------

`TCP/IP` (`Transmission Control Protocol`/`Internet Protocol`) is a generic term for many network protocols. The protocols are responsible for the switching and transport of data packets on the Internet. The Internet is entirely based on the `TCP/IP` protocol family. However, `TCP/IP` does not only refer to these two protocols but is usually used as a generic term for an entire protocol family.

For example, `ICMP` (`Internet Control Message Protocol`) or `UDP` (`User Datagram Protocol`) belongs to the protocol family. The protocol family provides the necessary functions for transporting and switching data packets in a private or public network.

* * * * *

### ISO/OSI vs. TCP/IP
------------------

`TCP/IP` is a communication protocol that allows hosts to connect to the Internet. It refers to the `Transmission Control Protocol` used in and by applications on the Internet. In contrast to `OSI`, it allows a lightening of the rules that must be followed, provided that general guidelines are followed.

`OSI`, on the other hand, is a communication gateway between the network and end-users. The OSI model is usually referred to as the reference model because it is older. It is also known for its strict protocol and limitations.

* * * * *

### Packet Transfers
----------------

In a layered system, devices in a layer exchange data in a different format called a `protocol data unit` (`PDU`). For example, when we want to browse a website on the computer, the remote server software first passes the requested data to the application layer. It is processed layer by layer, each layer performing its assigned functions. The data is then transferred through the network's physical layer until the destination server or another device receives it. The data is routed through the layers again, with each layer performing its assigned operations until the receiving software uses the data.

![[01 HTB/Academy/01. Pre-Engagement/04. Introduction to Networking/images/net_models_pdu2.png]]

During the transmission, each layer adds a `header` to the `PDU` from the upper layer, which controls and identifies the packet. This process is called `encapsulation`. The header and the data together form the PDU for the next layer. The process continues to the `Physical Layer` or `Network Layer`, where the data is transmitted to the receiver. The receiver reverses the process and unpacks the data on each layer with the header information. After that, the application finally uses the data. This process continues until all data has been sent and received.

![[images/packet_transfer.png]]

For us, as penetration testers, both reference models are useful. With `TCP/IP`, we can quickly understand how the entire connection is established, and with `ISO`, we can take it apart piece by piece and analyze it in detail. This often happens when we can listen to and intercept specific network traffic. We then have to analyze this traffic accordingly, going into more detail in the `Network Traffic Analysis` module. Therefore, we should familiarize ourselves with both reference models and understand and internalize them in the best possible way.

### The OSI Model

* * * * *

The goal in defining the `ISO/OSI` standard was to create a reference model that enables the communication of different technical systems via various devices and technologies and provides compatibility. The `OSI` model uses `seven` different layers, which are hierarchically based on each other to achieve this goal. These layers represent phases in the establishment of each connection through which the sent packets pass. In this way, the standard was created to trace how a connection is structured and established visually.

| Layer | Function |
| --- | --- |
| `7.Application` | Among other things, this layer controls the input and output of data and provides the application functions. |
| `6.Presentation` | The presentation layer's task is to transfer the system-dependent presentation of data into a form independent of the application. |
| `5.Session` | The session layer controls the logical connection between two systems and prevents, for example, connection breakdowns or other problems. |
| `4.Transport` | Layer 4 is used for end-to-end control of the transferred data. The Transport Layer can detect and avoid congestion situations and segment data streams. |
| `3.Network` | On the networking layer, connections are established in circuit-switched networks, and data packets are forwarded in packet-switched networks. Data is transmitted over the entire network from the sender to the receiver. |
| `2.Data Link` | The central task of layer 2 is to enable reliable and error-free transmissions on the respective medium. For this purpose, the bitstreams from layer 1 are divided into blocks or frames. |
| `1.Physical` | The transmission techniques used are, for example, electrical signals, optical signals, or electromagnetic waves. Through layer 1, the transmission takes place on wired or wireless transmission lines. |

* * * * *

The layers `2-4` are `transport oriented`, and the layers `5-7` are `application oriented` layers. In each layer, precisely defined tasks are performed, and the interfaces to the neighboring layers are precisely described. Each layer offers services for use to the layer directly above it. To make these services available, the layer uses the services of the layer below it and performs the tasks of its layer.

If two systems communicate, all seven layers of the `OSI` model are run through at least `twice`, since both the sender and the receiver must take the layer model into account. Therefore, a large number of different tasks must be performed in the individual layers to ensure the communication's security, reliability, and performance.

When an application sends a packet to the other system, the system works the layers shown above from layer `7` down to layer `1`, and the receiving system unpacks the received packet from layer `1` up to layer `7`.

### The TCP/IP Model

* * * * *

The `TCP/IP` model is also a layered reference model, often referred to as the `Internet Protocol Suite`. The term `TCP/IP` stands for the two protocols `Transmission Control Protocol` (`TCP`) and `Internet Protocol` (`IP`). `IP` is located within the `network layer` (`Layer 3`) and `TCP` is located within the `transport layer` (`Layer 4`) of the `OSI` layer model.

| Layer | Function |
| --- | --- |
| `4.Application` | The Application Layer allows applications to access the other layers' services and defines the protocols applications use to exchange data. |
| `3.Transport` | The Transport Layer is responsible for providing (TCP) session and (UDP) datagram services for the Application Layer. |
| `2.Internet` | The Internet Layer is responsible for host addressing, packaging, and routing functions. |
| `1.Link` | The Link layer is responsible for placing the TCP/IP packets on the network medium and receiving corresponding packets from the network medium. TCP/IP is designed to work independently of the network access method, frame format, and medium. |

* * * * *

With `TCP/IP`, every application can transfer and exchange data over any network, and it does not matter where the receiver is located. `IP` ensures that the data packet reaches its destination, and `TCP` controls the data transfer and ensures the connection between data stream and application. The main difference between `TCP/IP` and `OSI` is the number of layers, some of which have been combined.

![[images/http_auth_index2.png]]

The most important tasks of `TCP/IP` are:

| Task | Protocol | Description |
| --- | --- | --- |
| `Logical Addressing` | `IP` | Due to many hosts in different networks, there is a need to structure the network topology and logical addressing. Within TCP/IP, IP takes over the logical addressing of networks and nodes. Data packets only reach the network where they are supposed to be. The methods to do so are `network classes`, `subnetting`, and `CIDR`. |
| `Routing` | `IP` | For each data packet, the next node is determined in each node on the way from the sender to the receiver. This way, a data packet is routed to its receiver, even if its location is unknown to the sender. |
| `Error & Control Flow` | `TCP` | The sender and receiver are frequently in touch with each other via a virtual connection. Therefore control messages are sent continuously to check if the connection is still established. |
| `Application Support` | `TCP` | TCP and UDP ports form a software abstraction to distinguish specific applications and their communication links. |
| `Name Resolution` | `DNS` | DNS provides name resolution through Fully Qualified Domain Names (FQDN) in IP addresses, enabling us to reach the desired host with the specified name on the internet. |

# Addressing

## Network Layer

* * * * *

The `network layer` (`Layer 3`) of `OSI` controls the exchange of data packets, as these cannot be directly routed to the receiver and therefore have to be provided with routing nodes. The data packets are then transferred from node to node until they reach their target. To implement this, the `network layer` identifies the individual network nodes, sets up and clears connection channels, and takes care of routing and data flow control. When sending the packets, addresses are evaluated, and the data is routed through the network from node to node. There is usually no processing of the data in the layers above the `L3` in the nodes. Based on the addresses, the routing and the construction of routing tables are done.

In short, it is responsible for the following functions:

-   `Logical Addressing`
-   `Routing`

Protocols are defined in each layer of `OSI`, and these protocols represent a collection of rules for communication in the respective layer. They are transparent to the protocols of the layers above or below. Some protocols fulfill tasks of several layers and extend over two or more layers. The most used protocols on this layer are:

-   `IPv4` / `IPv6`
-   `IPsec`
-   `ICMP`
-   `IGMP`
-   `RIP`
-   `OSPF`

It ensures the routing of packets from source to destination within or outside a subnet. These two subnets may have different addressing schemes or incompatible addressing types. In both cases, the data transmission in each case goes through the entire communication network and includes routing between the network nodes. Since direct communication between the sender and the receiver is not always possible due to the different subnets, packets must be forwarded from nodes (routers) that are on the way. Forwarded packets do not reach the higher layers but are assigned a new intermediate destination and sent to the next node.

## IPv4 Addresses

* * * * *

Each host in the network located can be identified by the so-called `Media Access Control` address (`MAC`). This would allow data exchange within this one network. If the remote host is located in another network, knowledge of the `MAC` address is not enough to establish a connection. Addressing on the Internet is done via the `IPv4` and/or `IPv6` address, which is made up of the `network address` and the `host address`.

It does not matter whether it is a smaller network, such as a home computer network, or the entire Internet. The IP address ensures the delivery of data to the correct receiver. We can imagine the representation of `MAC` and `IPv4` / `IPv6` addresses as follows:

-   `IPv4` / `IPv6` - describes the unique postal address and district of the receiver's building.
-   `MAC` - describes the exact floor and apartment of the receiver.

It is possible for a single IP address to address multiple receivers (broadcasting) or for a device to respond to multiple IP addresses. However, it must be ensured that each IP address is assigned only once within the network.

* * * * *

### IPv4 Structure
--------------

The most common method of assigning IP addresses is `IPv4`, which consists of a `32`-bit binary number, combined into four `8`-bit groups (`octets`) ranging from `0-255`. These are converted into more easily readable decimal numbers, separated by dots and represented as dotted-decimal notation.

Thus an IPv4 address can look like this:

| Notation | Presentation |
| --- | --- |
|  Binary | 0111 1111.0000 0000.0000 0000.0000 0001 |
| Decimal | 127.0.0.1 |

Each network interface (network cards, network printers, or routers) is assigned a unique IP address.

The `IPv4` format allows 4,294,967,296 unique addresses. The IP address is divided into a `host part` and a `network part`. The `router` assigns the `host part` of the IP address at home or by an administrator. The respective `network administrator` assigns the `network part`. On the Internet, this is `IANA`, which allocates and manages the unique IPs.

In the past, further classification took place here. The IP network blocks were divided into `classes A - E`. The different classes differed in the host and network shares' respective lengths.

| `Class` | Network Address | First Address | Last Address | Subnetmask | CIDR | Subnets | IPs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `A` | 1.0.0.0 | 1.0.0.1 | 127.255.255.255 | 255.0.0.0 | /8 | 127 | 16,777,214 + 2 |
| `B` | 128.0.0.0 | 128.0.0.1 | 191.255.255.255 | 255.255.0.0 | /16 | 16,384 | 65,534 + 2 |
| `C` | 192.0.0.0 | 192.0.0.1 | 223.255.255.255 | 255.255.255.0 | /24 | 2,097,152 | 254 + 2 |
| `D` | 224.0.0.0 | 224.0.0.1 | 239.255.255.255 | Multicast | Multicast | Multicast | Multicast |
| `E` | 240.0.0.0 | 240.0.0.1 | 255.255.255.255 | reserved | reserved | reserved | reserved |

* * * * *

### Subnet Mask
-----------

A further separation of these classes into small networks is done with the help of `subnetting`. This separation is done using the `netmasks`, which is as long as an IPv4 address. As with classes, it describes which bit positions within the IP address act as `network part` or `host part`.

| Class | Network Address | First Address | Last Address | `Subnetmask` | CIDR | Subnets | IPs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A | 1.0.0.0 | 1.0.0.1 | 127.255.255.255 | `255.0.0.0` | /8 | 127 | 16,777,214 + 2 |
| B | 128.0.0.0 | 128.0.0.1 | 191.255.255.255 | `255.255.0.0` | /16 | 16,384 | 65,534 + 2 |
| C | 192.0.0.0 | 192.0.0.1 | 223.255.255.255 | `255.255.255.0` | /24 | 2,097,152 | 254 + 2 |
| D | 224.0.0.0 | 224.0.0.1 | 239.255.255.255 | `Multicast` | Multicast | Multicast | Multicast |
| E | 240.0.0.0 | 240.0.0.1 | 255.255.255.255 | `reserved` | reserved | reserved | reserved |

* * * * *

### Network and Gateway Addresses
-----------------------------

The `two` additional `IPs` added in the `IPs column` are reserved for the so-called `network address` and the `broadcast address`. Another important role plays the `default gateway`, which is the name for the IPv4 address of the `router` that couples networks and systems with different protocols and manages addresses and transmission methods. It is common for the `default gateway` to be assigned the first or last assignable IPv4 address in a subnet. This is not a technical requirement, but has become a de-facto standard in network environments of all sizes.

| Class | Network Address | `First Address` | Last Address | Subnetmask | CIDR | Subnets | `IPs` |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A | 1.0.0.0 | `1.0.0.1` | 127.255.255.255 | 255.0.0.0 | /8 | 127 | 16,777,214 `+ 2` |
| B | 128.0.0.0 | `128.0.0.1` | 191.255.255.255 | 255.255.0.0 | /16 | 16,384 | 65,534 `+ 2` |
| C | 192.0.0.0 | `192.0.0.1` | 223.255.255.255 | 255.255.255.0 | /24 | 2,097,152 | 254 `+ 2` |
| D | 224.0.0.0 | `224.0.0.1` | 239.255.255.255 | Multicast | Multicast | Multicast | Multicast |
| E | 240.0.0.0 | `240.0.0.1` | 255.255.255.255 | reserved | reserved | reserved | reserved |

* * * * *

### Broadcast Address
-----------------

The `broadcast` IP address's task is to connect all devices in a network with each other. `Broadcast` in a network is a message that is transmitted to all participants of a network and does not require any response. In this way, a host sends a data packet to all other participants of the network simultaneously and, in doing so, communicates its `IP address`, which the receivers can use to contact it. This is the `last IPv4` address that is used for the `broadcast`.

| Class | Network Address | First Address | `Last Address` | Subnetmask | CIDR | Subnets | IPs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A | 1.0.0.0 | 1.0.0.1 | `127.255.255.255` | 255.0.0.0 | /8 | 127 | 16,777,214 + 2 |
| B | 128.0.0.0 | 128.0.0.1 | `191.255.255.255` | 255.255.0.0 | /16 | 16,384 | 65,534 + 2 |
| C | 192.0.0.0 | 192.0.0.1 | `223.255.255.255` | 255.255.255.0 | /24 | 2,097,152 | 254 + 2 |
| D | 224.0.0.0 | 224.0.0.1 | `239.255.255.255` | Multicast | Multicast | Multicast | Multicast |
| E | 240.0.0.0 | 240.0.0.1 | `255.255.255.255` | reserved | reserved | reserved | reserved |

* * * * *

### Binary system
-------------

The binary system is a number system that uses only two different states that are represented into two numbers (`0` and `1`) opposite to the decimal-system (0 to 9).

An IPv4 address is divided into 4 octets, as we have already seen. Each `octet` consists of `8 bits`. Each position of a bit in an octet has a specific decimal value. Let's take the following IPv4 address as an example:

-   IPv4 Address: `192.168.10.39`

Here is an example of how the `first octet` looks like:

#### 1st Octet - Value: 192

```text
Values:         128  64  32  16  8  4  2  1
Binary:           1   1   0   0  0  0  0  0
```

If we calculate the sum of all these values for each octet where the bit is set to `1`, we get the sum:

| Octet | Values | Sum |
| --- | --- | --- |
| 1st | 128 + 64 + 0 + 0 + 0 + 0 + 0 + 0 | = `192` |
| 2nd | 128 + 0 + 32 + 0 + 8 + 0 + 0 + 0 | = `168` |
| 3rd | 0 + 0 + 0 + 0 + 8 + 0 + 2 + 0 | = `10` |
| 4th | 0 + 0 + 32 + 0 + 0 + 4 + 2 + 1 | = `39` |

The entire representation from binary to decimal would look like this:

#### IPv4 - Binary Notation

  IPv4 - Binary Notation

```text
Octet:             1st         2nd         3rd         4th
Binary:         1100 0000 . 1010 1000 . 0000 1010 . 0010 0111
Decimal:           192    .    168    .     10    .     39

```

-   IPv4 Address: `192.168.10.39`

This addition takes place for each octet, which results in a decimal representation of the `IPv4 address`. The subnet mask is calculated in the same way.

#### IPv4 - Decimal to Binary

  IPv4 - Decimal to Binary

```text
Values:         128  64  32  16  8  4  2  1
Binary:           1   1   1   1  1  1  1  1

```

| Octet | Values | Sum |
| --- | --- | --- |
| 1st | 128 + 64 + 32 + 16 + 8 + 4 + 2 + 1 | = `255` |
| 2nd | 128 + 64 + 32 + 16 + 8 + 4 + 2 + 1 | = `255` |
| 3rd | 128 + 64 + 32 + 16 + 8 + 4 + 2 + 1 | = `255` |
| 4th | 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 | = `0` |

#### Subnet Mask

```text
Octet:             1st         2nd         3rd         4th
Binary:         1111 1111 . 1111 1111 . 1111 1111 . 0000 0000
Decimal:           255    .    255    .    255    .     0
```

-   IPv4 Address: `192.168.10.39`

-   Subnet mask: `255.255.255.0`

* * * * *

### CIDR
----

`Classless Inter-Domain Routing` (`CIDR`) is a method of representation and replaces the fixed assignment between IPv4 address and network classes (A, B, C, D, E). The division is based on the subnet mask or the so-called `CIDR suffix`, which allows the bitwise division of the IPv4 address space and thus into `subnets` of any size. The `CIDR suffix` indicates how many bits from the beginning of the IPv4 address belong to the network. It is a notation that represents the `subnet mask` by specifying the number of `1`-bits in the subnet mask.

Let us stick to the following IPv4 address and subnet mask as an example:

-   IPv4 Address: `192.168.10.39`

-   Subnet mask: `255.255.255.0`

Now the whole representation of the IPv4 address and the subnet mask would look like this:

-   CIDR: `192.168.10.39/24`

The CIDR suffix is, therefore, the sum of all ones in the subnet mask.

```text
Octet:             1st         2nd         3rd         4th
Binary:         1111 1111 . 1111 1111 . 1111 1111 . 0000 0000 (/24)
Decimal:           255    .    255    .    255    .     0
```

## Subnetting

* * * * *

The division of an address range of IPv4 addresses into several smaller address ranges is called `subnetting`.

A subnet is a logical segment of a network that uses IP addresses with the same network address. We can think of a subnet as a labeled entrance on a large building corridor. For example, this could be a glass door that separates various departments of a company building. With the help of subnetting, we can create a specific subnet by ourselves or find out the following outline of the respective network:

-   `Network address`
-   `Broadcast address`
-   `First host`
-   `Last host`
-   `Number of hosts`

Let us take the following IPv4 address and subnet mask as an example:

-   IPv4 Address: `192.168.12.160`
-   Subnet Mask: `255.255.255.192`
-   CIDR: `192.168.12.160/26`

* * * * *

We already know that an IP address is divided into the `network part` and the `host part`.

#### Network Part

| Details of | 1st Octet | 2nd Octet | 3rd Octet | 4th Octet | Decimal |
| --- | --- | --- | --- | --- | --- |
| IPv4 | `1100 0000` | `1010 1000` | `0000 1100` | `10`10 0000 | 192.168.12.160`/26` |
| Subnet mask | `1111 1111` | `1111 1111` | `1111 1111` | `11`00 0000 | `255.255.255.192` |
| Bits | /8 | /16 | /24 | /32 |  |

In subnetting, we use the subnet mask as a template for the IPv4 address. From the `1`-bits in the subnet mask, we know which bits in the IPv4 address `cannot` be changed. These are `fixed` and therefore determine the "main network" in which the subnet is located.

#### Host Part

| Details of | 1st Octet | 2nd Octet | 3rd Octet | 4th Octet | Decimal |
| --- | --- | --- | --- | --- | --- |
| IPv4 | 1100 0000 | 1010 1000 | 0000 1100 | 10`10 0000` | 192.168.12.160/26 |
| Subnet mask | 1111 1111 | 1111 1111 | 1111 1111 | 11`00 0000` | 255.255.255.192 |
| Bits | /8 | /16 | /24 | /32 |  |

The bits in the `host part` can be changed to the `first` and `last` address. The first address is the `network address`, and the last address is the `broadcast address` for the respective subnet.

The `network address` is vital for the delivery of a data packet. If the `network address` is the same for the source and destination address, the data packet is delivered within the same subnet. If the network addresses are different, the data packet must be routed to another subnet via the `default gateway`.

The `subnet mask` determines where this separation occurs.

#### Separation Of Network & Host Parts

| Details of | 1st Octet | 2nd Octet | 3rd Octet | 4th Octet | Decimal |
| --- | --- | --- | --- | --- | --- |
| IPv4 | 1100 0000 | 1010 1000 | 0000 1100 | 10`|`10 0000 | 192.168.12.160/26 |
| Subnet mask | `1111 1111` | `1111 1111` | `1111 1111` | `11|`00 0000 | 255.255.255.192 |
| Bits | /8 | /16 | /24 | /32 |  |

* * * * *

#### Network Address

So if we now set all bits to `0` in the `host part` of the IPv4 address, we get the respective subnet's `network address`.

| Details of | 1st Octet | 2nd Octet | 3rd Octet | 4th Octet | Decimal |
| --- | --- | --- | --- | --- | --- |
| IPv4 | 1100 0000 | 1010 1000 | 0000 1100 | 10`|00 0000` | `192.168.12.128`/26 |
| Subnet mask | `1111 1111` | `1111 1111` | `1111 1111` | `11|`00 0000 | 255.255.255.192 |
| Bits | /8 | /16 | /24 | /32 |  |

* * * * *

#### Broadcast Address

If we set all bits in the `host part` of the IPv4 address to `1`, we get the `broadcast address`.

| Details of | 1st Octet | 2nd Octet | 3rd Octet | 4th Octet | Decimal |
| --- | --- | --- | --- | --- | --- |
| IPv4 | 1100 0000 | 1010 1000 | 0000 1100 | 10`|11 1111` | `192.168.12.191`/26 |
| Subnet mask | `1111 1111` | `1111 1111` | `1111 1111` | `11|`00 0000 | 255.255.255.192 |
| Bits | /8 | /16 | /24 | /32 |  |

Since we now know that the IPv4 addresses `192.168.12.128` and `192.168.12.191` are assigned, all other IPv4 addresses are accordingly between `192.168.12.129-190`. Now we know that this subnet offers us a total of `64 - 2` (network address & broadcast address) or `62` IPv4 addresses that we can assign to our hosts.

| Hosts | IPv4 |
| --- | --- |
| Network Address | `192.168.12.128` |
| First Host | `192.168.12.129` |
| Other Hosts | `...` |
| Last Host | `192.168.12.190` |
| Broadcast Address | `192.168.12.191` |

* * * * *

### Subnetting Into Smaller Networks
--------------------------------

Let us now assume that we, as administrators, have been given the task of dividing the subnet assigned to us into 4 additional subnets. Thus, it is essential to know that we can only divide the subnets based on the binary system.

| Exponent | Value |
| --- | --- |
| 2`^0` | = 1 |
| 2`^1` | = 2 |
| 2`^2` | = 4 |
| 2`^3` | = 8 |
| 2`^4` | = 16 |
| 2`^5` | = 32 |
| 2`^6` | = 64 |
| 2`^7` | = 128 |
| 2`^8` | = 256 |

* * * * *

Therefore we can divide the `64 hosts` we know by `4`. The `4` is equal to the exponent 2`^2` in the binary system, so we find out the number of bits for the subnet mask by which we have to extend it. So we know the following parameters:

-   Subnet: `192.168.12.128/26`
-   Required Subnets: `4`

Now we increase/expand our subnet mask by `2 bits` from `/26` to `/28`, and it looks like this:

| Details of | 1st Octet | 2nd Octet | 3rd Octet | 4th Octet | Decimal |
| --- | --- | --- | --- | --- | --- |
| IPv4 | 1100 0000 | 1010 1000 | 0000 1100 | 1000`|` 0000 | 192.168.12.128`/28` |
| Subnet mask | `1111 1111` | `1111 1111` | `1111 1111` | `1111|` 0000 | `255.255.255.240` |
| Bits | /8 | /16 | /24 | /32 |  |

Next, we can divide the `64` IPv4 addresses that are available to us into `4 parts`:

| Hosts | Math | Subnets | Host range for each subnet |
| --- | --- | --- | --- |
| 64 | / | 4 | = `16` |

So we know how big each subnet will be. From now on, we start from the network address given to us (192.168.12.128) and add the `16` hosts `4` times:

| Subnet No. | Network Address | First Host | Last Host | Broadcast Address | CIDR |
| --- | --- | --- | --- | --- | --- |
| 1 | `192.168.12.128` | 192.168.12.129 | 192.168.12.142 | `192.168.12.143` | 192.168.12.128/28 |
| 2 | `192.168.12.144` | 192.168.12.145 | 192.168.12.158 | `192.168.12.159` | 192.168.12.144/28 |
| 3 | `192.168.12.160` | 192.168.12.161 | 192.168.12.174 | `192.168.12.175` | 192.168.12.160/28 |
| 4 | `192.168.12.176` | 192.168.12.177 | 192.168.12.190 | `192.168.12.191` | 192.168.12.176/28 |

* * * * *

### Mental Subnetting
-----------------

It may seem like there is a lot of math involved in subnetting, but each octet repeats itself, and everything is a power of two, so there doesn't have to be a lot of memorization. The first thing to do is identify what octet changes.

| 1st Octet | 2nd Octet | 3rd Octet | 4th Octet |
| --- | --- | --- | --- |
| /8 | /16 | /24 | /32 |

It is possible to identify what octet of the IP Address may change by remembering those four numbers. Given the Network Address: `192.168.1.1/25`, it is immediately apparent that 192.168.2.4 would not be in the same network because the `/25` subnet means only the fourth octet may change.

The next part identifies how big each subnet can be but by dividing eight by the network and looking at the `remainder`. This is also called `Modulo Operation (%)` and is heavily utilized in cryptology. Given our previous example of `/25`, `(25 % 8)` would be 1. This is because eight goes into 25 three times (8 * 3 = 24). There is a 1 leftover, which is the network bit reserved for the network mask. There is a total of eight bits in each octet of an IP Address. If one is used for the network mask, the equation becomes 2^(8-1) or 2^7, 128. The table below contains all the numbers.

| Remainder | Number | Exponential Form | Division Form |
| --- | --- | --- | --- |
| 0 | 256 | 2^8 | 256 |
| 1 | 128 | 2^7 | 256/2 |
| 2 | 64 | 2^6 | 256/2/2 |
| 3 | 32 | 2^5 | 256/2/2/2 |
| 4 | 16 | 2^4 | 256/2/2/2/2 |
| 5 | 8 | 2^3 | 256/2/2/2/2/2 |
| 6 | 4 | 2^2 | 256/2/2/2/2/2/2 |
| 7 | 2 | 2^1 | 256/2/2/2/2/2/2/2 |

By remembering the powers of two up to eight, it can become an instant calculation. However, if forgotten, it may be quicker to remember to divide 256 in half the number of times of the remainder.

The tricky part of this is getting the actual IP Address range because 0 is a number and not null in networking. So in our `/25` with 128 IP Addresses, the first range is `192.168.1.0-127`. The first address is the network, and the last is the broadcast address, which means the usable IP Space would become `192.168.1.1-126`. If our IP Address fell above 128, then the `usable ip space` would be 192.168.129-254 (128IPs the network and 255 is the broadcast).

#### Questions

>Submit the decimal representation of the subnet mask from the following CIDR: 10.200.20.0/27

>Submit the broadcast address of the following CIDR: 10.200.20.0/27

>Split the network 10.200.20.0/27 into 4 subnets and submit the network address of the 3rd subnet as the answer.

>Split the network 10.200.20.0/27 into 4 subnets and submit the broadcast address of the 2nd subnet as the answer.

## MAC Addresses

* * * * *

Each host in a network has its own `48`-bit (`6 octets`) `Media Access Control` (`MAC`) address, represented in hexadecimal format. `MAC` is the `physical address` for our network interfaces. There are several different standards for the MAC address:

-   Ethernet (IEEE 802.3)
-   Bluetooth (IEEE 802.15)
-   WLAN (IEEE 802.11)

This is because the `MAC` address addresses the physical connection (network card, Bluetooth, or WLAN adapter) of a host. Each network card has its individual MAC address, which is configured once on the manufacturer's hardware side but can always be changed, at least temporarily.

Let's have a look at an example of such a MAC address:

MAC address:

-   `DE:AD:BE:EF:13:37`
-   `DE-AD-BE-EF-13-37`
-   `DEAD.BEEF.1337`

| Representation | 1st Octet | 2nd Octet | 3rd Octet | 4th Octet | 5th Octet | 6th Octet |
| --- | --- | --- | --- | --- | --- | --- |
| Binary | 1101 1110 | 1010 1101 | 1011 1110 | 1110 1111 | 0001 0011 | 0011 0111 |
| Hex | DE | AD | BE | EF | 13 | 37 |

* * * * *

When an IP packet is delivered, it must be addressed on `layer 2` to the destination host's physical address or to the router / NAT, which is responsible for routing. Each packet has a `sender address` and a `destination address`.

The first half (`3 bytes` / `24 bit`) is the so-called `Organization Unique Identifier` (`OUI`) defined by the `Institute of Electrical and Electronics Engineers` (`IEEE`) for the respective manufacturers.

| Representation | 1st Octet | 2nd Octet | 3rd Octet | 4th Octet | 5th Octet | 6th Octet |
| --- | --- | --- | --- | --- | --- | --- |
| Binary | `1101 1110` | `1010 1101` | `1011 1110` | 1110 1111 | 0001 0011 | 0011 0111 |
| Hex | `DE` | `AD` | `BE` | EF | 13 | 37 |

* * * * *

The last half of the MAC address is called the `Individual Address Part` or `Network Interface Controller` (`NIC`), which the manufacturers assign. The manufacturer sets this bit sequence only once and thus ensures that the complete address is unique.

| Representation | 1st Octet | 2nd Octet | 3rd Octet | 4th Octet | 5th Octet | 6th Octet |
| --- | --- | --- | --- | --- | --- | --- |
| Binary | 1101 1110 | 1010 1101 | 1011 1110 | `1110 1111` | `0001 0011` | `0011 0111` |
| Hex | DE | AD | BE | `EF` | `13` | `37` |

If a host with the IP target address is located in the same subnet, the delivery is made directly to the target computer's physical address. However, if this host belongs to a different subnet, the Ethernet frame is addressed to the `MAC address` of the responsible router (`default gateway`). If the Ethernet frame's destination address matches the own `layer 2 address`, the router will forward the frame to the higher layers. `Address Resolution Protocol` (`ARP`) is used in IPv4 to determine the MAC addresses associated with the IP addresses.

As with IPv4 addresses, there are also certain reserved areas for the MAC address. These include, for example, the local range for the MAC.

| Local Range |
| --- |
| 0`2`:00:00:00:00:00 |
| 0`6`:00:00:00:00:00 |
| 0`A`:00:00:00:00:00 |
| 0`E`:00:00:00:00:00 |

Furthermore, the last two bits in the first octet can play another essential role. The last bit can have two states, 0 and 1, as we already know. The last bit identifies the MAC address as `Unicast` (`0`) or `Multicast` (`1`). With `unicast`, it means that the packet sent will reach only one specific host.

#### MAC Unicast

| Representation | 1st Octet | 2nd Octet | 3rd Octet | 4th Octet | 5th Octet | 6th Octet |
| --- | --- | --- | --- | --- | --- | --- |
| Binary | 1101 111`0` | 1010 1101 | 1011 1110 | 1110 1111 | 0001 0011 | 0011 0111 |
| Hex | D`E` | AD | BE | EF | 13 | 37 |

* * * * *

With `multicast`, the packet is sent only once to all hosts on the local network, which then decides whether or not to accept the packet based on their configuration. The `multicast` address is a unique address, just like the `broadcast` address, which has fixed octet values. `Broadcast` in a network represents a broadcasted call, where data packets are transmitted simultaneously from one point to all members of a network. It is mainly used if the address of the receiver of the packet is not yet known. An example is the `ARP` (`for MAC addresses`) and DHCP (`for IPv4 addresses`) protocols.

The defined values of each octet are marked `green`.

#### MAC Multicast

| Representation | 1st Octet | 2nd Octet | 3rd Octet | 4th Octet | 5th Octet | 6th Octet |
| --- | --- | --- | --- | --- | --- | --- |
| Binary | `0000 0001` | `0000 0000` | `0101 1110` | 1110 1111 | 0001 0011 | 0011 0111 |
| Hex | `01` | `00` | `5E` | EF | 13 | 37 |

#### MAC Broadcast

| Representation | 1st Octet | 2nd Octet | 3rd Octet | 4th Octet | 5th Octet | 6th Octet |
| --- | --- | --- | --- | --- | --- | --- |
| Binary | `1111 1111` | `1111 1111` | `1111 1111` | `1111 1111` | `1111 1111` | `1111 1111` |
| Hex | `FF` | `FF` | `FF` | `FF` | `FF` | `FF` |

* * * * *

The second last bit in the first octet identifies whether it is a `global OUI`, defined by the IEEE, or a `locally administrated` MAC address.

#### Global OUI

| Representation | 1st Octet | 2nd Octet | 3rd Octet | 4th Octet | 5th Octet | 6th Octet |
| --- | --- | --- | --- | --- | --- | --- |
| Binary | 1101 11`0`0 | 1010 1101 | 1011 1110 | 1110 1111 | 0001 0011 | 0011 0111 |
| Hex | D`C` | AD | BE | EF | 13 | 37 |

#### Locally Administrated

| Representation | 1st Octet | 2nd Octet | 3rd Octet | 4th Octet | 5th Octet | 6th Octet |
| --- | --- | --- | --- | --- | --- | --- |
| Binary | 1101 11`1`0 | 1010 1101 | 1011 1110 | 1110 1111 | 0001 0011 | 0011 0111 |
| Hex | D`E` | AD | BE | EF | 13 | 37 |

## IPv6 Addresses

* * * * *

`IPv6` is the successor of IPv4. In contrast to IPv4, the `IPv6` address is `128` bit long. The `prefix` identifies the host and network parts. The Internet Assigned Numbers Authority (`IANA`) is responsible for assigning IPv4 and IPv6 addresses and their associated network portions. In the long term, `IPv6` is expected to completely replace IPv4, which is still predominantly used on the Internet. In principle, however, IPv4 and IPv6 can be made available simultaneously (`Dual Stack`).

IPv6 consistently follows the `end-to-end` principle and provides publicly accessible IP addresses for any end devices without the need for NAT. Consequently, an interface can have multiple IPv6 addresses, and there are special IPv6 addresses to which multiple interfaces are assigned.

`IPv6` is a protocol with many new features, which also has many other advantages over IPv4:

-   Larger address space
-   Address self-configuration (SLAAC)
-   Multiple IPv6 addresses per interface
-   Faster routing
-   End-to-end encryption (IPsec)
-   Data packages up to 4 GByte

| Features | IPv4 | IPv6 |
| --- | --- | --- |
| Bit length | 32-bit | 128 bit |
| OSI layer | Network Layer | Network Layer |
| Adressing range | ~ 4.3 billion | ~ 340 undecillion |
| Representation | Binary | Hexadecimal |
| Prefix notation | 10.10.10.0/24 | fe80::dd80:b1a9:6687:2d3b/64 |
| Dynamic addressing | DHCP | SLAAC / DHCPv6 |
| IPsec | Optional | Mandatory |

* * * * *

There are four different types of IPv6 addresses:

| Type | Description |
| --- | --- |
| `Unicast` | Addresses for a single interface. |
| `Anycast` | Addresses for multiple interfaces, where only one of them receives the packet. |
| `Multicast` | Addresses for multiple interfaces, where all receive the same packet. |
| `Broadcast` | Do not exist and is realized with multicast addresses. |

* * * * *

### Hexadecimal System
------------------

The `hexadecimal system` (`hex`) is used to make the binary representation more readable and understandable. We can only show `10` (`0-9`) states with the decimal system and `2` (`0` / `1`) with the binary system by using a single character. In contrast to the binary and decimal system, we can use the hexadecimal system to show `16` (`0-F`) states with a single character.

| Decimal | Hex | Binary |
| --- | --- | --- |
| 1 | 1 | 0001 |
| 2 | 2 | 0010 |
| 3 | 3 | 0011 |
| 4 | 4 | 0100 |
| 5 | 5 | 0101 |
| 6 | 6 | 0110 |
| 7 | 7 | 0111 |
| 8 | 8 | 1000 |
| 9 | 9 | 1001 |
| 10 | A | 1010 |
| 11 | B | 1011 |
| 12 | C | 1100 |
| 13 | D | 1101 |
| 14 | E | 1110 |
| 15 | F | 1111 |

Let's look at an example with an IPv4, at how the IPv4 address (`192.168.12.160`) would look in hexadecimal representation.

| Representation | 1st Octet | 2nd Octet | 3rd Octet | 4th Octet |
| --- | --- | --- | --- | --- |
| Binary | 1100 0000 | 1010 1000 | 0000 1100 | 1010 0000 |
| `Hex` | `C0` | `A8` | `0C` | `A0` |
| Decimal | 192 | 168 | 12 | 160 |

* * * * *

Because of its length, an `IPv6` address is represented in `hexadecimal` notation. Therefore the `128 bits` are divided into `8 blocks` times 16 bits (or `4 hex` numbers). All 4 hex numbers are grouped and separated by a colon (`:`) instead of a simple dot (`.`) as in IPv4. To simplify the notation, we leave out leading at least `4` zeros in the blocks, and we can replace them with two colons (`::`).

An IPv6 address can look like this:

-   Full IPv6: `fe80:0000:0000:0000:dd80:b1a9:6687:2d3b/64`
-   Short IPv6: `fe80::dd80:b1a9:6687:2d3b/64`

An IPv6 address consists of two parts:

-   `Network Prefix` (network part)
-   `Interface Identifier` also called `Suffix` (host part)

The `Network Prefix` identifies the network, subnet, or address range. The `Interface Identifier` is formed from the `48-bit MAC` address (which we will discuss later) of the interface and is converted to a `64-bit address` in the process. The default prefix length is `/64`. However, other typical prefixes are `/32`, `/48`, and `/56`. If we want to use our networks, we get a shorter prefix (e.g. `/56`) than `/64` from our provider.

In RFC 5952, the aforementioned IPv6 address notation was defined:

-   All alphabetical characters are always written in lower case.
-   All leading zeros of a block are always omitted.
-   One or more consecutive blocks of `4 zeros` (hex) are shortened by two colons (`::`).
-   The shortening to two colons (`::`) may only be performed `once` starting from the left.
