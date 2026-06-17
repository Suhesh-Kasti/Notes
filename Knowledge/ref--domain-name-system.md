---
category: knowledge
tags:
  - dns
platform: n/a
status: done
created: 2026-06-17
aliases:
  - How DNS Works
---

The Domain Name System is a hierarchical, distributed naming system for computers, services, or any other resource connected to the internet or a private network. Whenever you need your browser to locate and connect to a computer service or device, the DNS works behind the scenes to translate an easily-memorized domain name into the numerical Internet Protocol (IP) address for that resource. You could think of the DNS as the internet’s phone book: It was created to enable people to easily identify by name all devices and services connected to the internet.

The DNS terminology

Domain Names

A domain name is a user-friendly name associated with an internet source. For example. www.f5.com is a domain name, and the URL is associated with the servers owned by F5.

The subdivision of a domain is known as a subdomain. For example, support.f5.com is the subdomain for support on F5.com. A subdomain is anything to the left of the domain name, followed by a dot.

DNS Lookup

DNS lookup is a process through which a client (such as a web browser) queries a DNS server for a particular domain. The DNS server then replies back with an IP address, which then leads the client to the desired destination.

Domain Name Space

Domain Name Space defines the overall naming structure of the internet. It is a tree-like structure of domain names, with a root domain name at the top. From that root domain, major domains such as .com, .net, .org, and other domains branch out.

Zones

A name space tree is subdivided into zones. It defines the resources available under a specific domain.

Name Servers

Name servers store information about a zone. There are two types of name servers: Primary and Secondary. Every zone has its data stored on both Primary and Secondary name servers.

DNS Resolvers

A DNS resolver is the client side of the DNS. It is responsible for initiating and sequencing the queries that ultimately lead to translation of a domain name into an IP address.

How does DNS Work?
- User tries connecting to suhesh.com.np
- User’s system looks in host ﬁle.
	- *Linux*: /etc/hosts
	- *Windows*: C:\Windows\System32\drivers\etc\hosts
- User’s system looks in local DNS cache.
- User’s system queries its local DNS server (LDNS) for suhesh.com.np. *For a home user it can be your router.*
- If still not found, user’s system queries the recursive DNS server for suhesh.com.np.
	- *This can your ISP's DNS server or if you have set a private DNS server like 1.1.1.1 or 8.8.8.8*
- Recursive looks in its cache.
	- *It is called recursive DNS server because from now on this server will reach various DNS servers to find the requested doman name*
- Recursive DNS queries root servers for server that is authoritative for .com.np
- Root server will return the nameserver of Mercantile (*A company responsible for managing .com.np domain*)
- Recursive DNS now queries nameserver of mercantile to provide the authoritative nameserver (*the nameserver that has zone file for the domain*) for suhesh.com.np
- Recursive DNS now queries the authoritative nameserver (in my case cloudflare) for the A record for the domain suhesh.com.np
- Recursive DNS caches the response, sends it to the user, who also caches the response, and connects to the IP address.

DNS Records and Its Common Types

DNS records are mapping files which tell the DNS server which IP address is associated with which domain name. It also tells the DNS server how to handle those requests. There are various types of DNS records, but all DNS records for a specific domain are contained in something called a DNS Zone. Think of the DNS Zone as a container which allows the internet to look up the IP address for one, and only one, particular domain.

The common DNS record types are as follows:

A and AAAA Records

Address or A records (also known as host records) are the central records of the DNS. These records link a domain to an IP Address. AAAA record is same as A record—but instead of a 32-bit IPv4 IP address, it returns a 128-bit IPv6 address.

NS Record

Name Server (NS) records determine which servers communicate DNS information for a domain. Generally, you will have primary and secondary name server records for your domain.

MX Record

Mail Exchange records direct email messages to the servers for a particular domain. Multiple MX records can be defined for a domain, each with a different priority. The lowest number is the highest priority. If mail can’t be delivered using the first priority record, the second priority record is used, and so on.

TXT Record

Text or TXT records may contain arbitrary text, but can also be used to define machine readable text.

CNAME Record

Canonical NAME or CNAME records link an alias name to another canonical domain name. For instance, alias.example.com might link to example.com.

DNS Importance and Limitations

The DNS is one of the primary technology enabling the internet. It is also a vital component in the networking infrastructure. Because having an available, intelligent, secure and scalable DNS infrastructure is critical, DNS doesn’t simply deliver content and applications: it manages a distributed and redundant architecture, ensuring high availability and quality user response time. If DNS fails, most web applications will fail to function properly. This not only makes DNS critical, but also a prime target for attacks. If you don’t have a proper DNS infrastructure, customers won’t be able to reach your applications or content—which might lead to them turning elsewhere for their needs.

However, there are certain limitations to the standard DNS services. First, even though DNS makes your application/website/content available, DNS doesn’t really care whether it’s up and running, or even exists.

In addition, DNS has no real ability to distribute load. It will continue to use all the IP addresses, even if the application supported by that IP is overloaded or down.

DNS also has no concept of stateful application: it cannot guarantee that a user goes back to the same IP address. For example, if you go to a particular data center and build a shopping cart that is maintained in that data center, there is no guarantee that next time you resolve the name, you will get the same IP.

Finally, standard DNS servers can only answer a limited number of DNS queries per second, making them vulnerable to distributed denial-of-service (DDoS) attacks.

Security Issues

DNS is the backbone of the internet, but it is also one of the most vulnerable points in your network—which makes it a high-value target. DDoS attacks can flood your DNS servers to the point of hijack or failure, leading to redirecting the requests to a malicious server. To prevent this, a high performing, distributed, secure, architecture must be integrated into the network. Companies should also add more DNS servers during DNS surges and DDoS attacks.

Even though DNS servers and cloud services can handle varying amounts of requests per second, with costs increasing as the queries increase, this solution often requires manual intervention when changes are needed. And since new vulnerabilities keep coming, traditional DNS servers require frequent maintenance and patching, making it even more costly.

- DNS types of record, how does master and slave dns server, dns synchronization
- Traditional server – existing vulnerabilities (dns server – BIND 9)
- DNS delegation, how does domain works behind the dns server
- DNS load-balancing, dns health monitoring
- Troubleshooting command – nslookup, dig command
- DNSSEC (how does it work, and how does it mitigate the traditional dns server working)
Resources:
- [https://clouddocs.f5.com/training/community/dns/html/](https://clouddocs.f5.com/training/community/dns/html/)
- [https://www.youtube.com/watch?v=WkXSx-Tuzlo&t=43s](https://www.youtube.com/watch?v=WkXSx-Tuzlo&t=43s) dnsperf tool

---

## How DNS Works

DNS (Domain Name System) runs primarily on **port 53** and is essential for translating human-readable domain names into IP addresses. Here's the process that occurs when you type a domain name into a browser:

1. **Local Cache Check (Stub Resolver)**:
   - When you type in a domain (e.g., `suhesh.com.np`), your device first checks its **stub resolver** (a local DNS client) to see if the IP address is cached.
   - If the IP is found, it returns the result immediately. If not, it proceeds to the next step.

2. **Query to Recursive DNS Server**:
   - If the IP isn’t cached, your device queries a **recursive DNS server**. This DNS server can be manually configured (like Cloudflare's, Google’s, or AdGuard’s DNS) or provided via your DHCP server.
   - If the recursive DNS server doesn’t have the IP, it begins a recursive query process to find it.

3. **Query to Root DNS Servers**:
   - The recursive DNS server queries one of the 13 **root DNS servers** spread globally, which have **1865 servers** in total.
   - **Root servers** don’t know the exact IP address but they point the query to the **authoritative DNS servers** managing the Top-Level Domain (TLD) of the requested domain.

   Here’s a list of some of the root DNS servers:

   | HOSTNAME           | IPV4 ADDRESS      | IPV6 ADDRESS          | OPERATOR                               |
   |--------------------|-------------------|-----------------------|----------------------------------------|
   | a.root-servers.net  | 198.41.0.4        | 2001:503:ba3e::2:30    | Verisign, Inc.                         |
   | b.root-servers.net  | 170.247.170.2     | 2801:1b8:10::b         | University of Southern California      |
   | c.root-servers.net  | 192.33.4.12       | 2001:500:2::c          | Cogent Communications                  |
   | d.root-servers.net  | 199.7.91.13       | 2001:500:2d::d         | University of Maryland                 |
   | e.root-servers.net  | 192.203.230.10    | 2001:500:a8::e         | NASA (Ames Research Center)            |
   | f.root-servers.net  | 192.5.5.241       | 2001:500:2f::f         | Internet Systems Consortium, Inc.      |
   | g.root-servers.net  | 192.112.36.4      | 2001:500:12::d0d       | US Department of Defense (NIC)         |
   | h.root-servers.net  | 198.97.190.53     | 2001:500:1::53         | US Army (Research Lab)                 |
   | i.root-servers.net  | 192.36.148.17     | 2001:7fe::53           | Netnod                                 |
   | j.root-servers.net  | 192.58.128.30     | 2001:503:c27::2:30     | Verisign, Inc.                         |
   | k.root-servers.net  | 193.0.14.129      | 2001:7fd::1            | RIPE NCC                               |
   | l.root-servers.net  | 199.7.83.42       | 2001:500:9f::42        | ICANN                                  |
   | m.root-servers.net  | 202.12.27.33      | 2001:dc3::35           | WIDE Project                           |

4. **TLD Authoritative DNS Server**:
   - The root server directs the recursive DNS to the **authoritative DNS servers** for the TLD of the requested domain (e.g., `.com.np` for `suhesh.com.np`).
   - In this case, the **Mercantile DNS** manages `.com.np`. The recursive DNS now queries Mercantile’s DNS servers.

5. **Nameserver Lookup**:
   - The TLD’s authoritative server points the query to the **nameservers** managing the specific domain (`suhesh.com.np`). For example, **Cloudflare** might be hosting the DNS records for `suhesh.com.np`.

6. **Final Query (Zone File)**:
   - Cloudflare’s nameserver has the **zone file** for `suhesh.com.np`. The zone file contains various DNS records like:
     - **SOA (Start of Authority) Record**: Contains administrative information about the domain.
     - **A Record**: Maps the domain to its IPv4 address.
     - **AAAA Record**: Maps the domain to its IPv6 address.
     - **CNAME Record**: Maps a domain name to another domain name (aliasing).
     - **NS Record**: Specifies the nameservers for the domain.
     - **MX Record**: Specifies the mail servers for the domain.
     - **TXT Record**: Used for miscellaneous text information (often for SPF, DKIM, or verification).

   - The recursive DNS queries the nameserver for the **A record** (or AAAA record) of `suhesh.com.np`, and Cloudflare responds with the IP address.

7. **Returning the IP**:
   - The recursive DNS server returns the final IP address to your device, and your browser uses this to establish a connection to the web server.

---

1. **Where does the DNS reply come back?**
   - The DNS reply comes back through the same path as the query. Once the recursive DNS server finds the IP address, it returns the response to your stub resolver (DNS client on your device), which then gives it to your browser to connect to the web server.

2. **Master and Slave DNS Server, DNS Synchronization:**
   - **Master DNS Server**: The authoritative DNS server that holds the primary zone file for a domain. Any changes to DNS records are made here.
   - **Slave DNS Server**: A secondary DNS server that holds a read-only copy of the zone file from the master server. It provides redundancy and load balancing.
   - **DNS Synchronization**: The slave server synchronizes with the master server through a process called **zone transfer**. The master sends a copy of the zone file to the slave server periodically or when changes are made.
   - This ensures that if the master server goes down, the slave can continue to answer DNS queries, making DNS services more resilient.

3. **DNS Delegation**:
   - **DNS Delegation** is the process of dividing the DNS namespace across multiple DNS servers.
   - For example, the `.com.np` zone is delegated to Mercantile’s DNS servers, and further, `suhesh.com.np` may be delegated to Cloudflare’s DNS servers.
   - The **authoritative server** for a parent zone (like `.com.np`) delegates the responsibility for a subdomain (like `suhesh.com.np`) to another set of DNS servers. These servers are listed in **NS (nameserver) records**.
   - The **domain behind the DNS server** is typically the server where the zone file is hosted and managed. This server handles requests for that domain’s IP address, email settings, and other DNS configurations based on the zone file.

---

`nslookup`
