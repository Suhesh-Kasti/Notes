---
category: lab
tags:
  - training/web
  - vuln/unassigned
platform: hackthebox
status: done
completed_date:
created: 2026-06-17
aliases:
  - pass
---

Machine : 10.10.200.234
My : 10.17.8.222


Note:
Any users with passwords in this list:
love
sex
god
secret
will be subject to an immediate disciplinary hearing.
Any users with other weak passwords will be complained at, loudly.
These users are:
rcampbell:Robert M. Campbell:Weak password
gcrawford:Gerard B. Crawford:Exposing crypto keys, weak password
Exposing the company's cryptographic keys is a disciplinary offense.
Eugene Belford, CSO

# pass
rcampbell -> tamara  (FTP)
by hydra

# Privesc
/usr/bin/python3.6 = cap_setuid+ep
/usr/bin/python3.6m = cap_setuid+ep
