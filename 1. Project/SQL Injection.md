---
category:
  - Hacking
tags:
  - sql
  - sql_injection
  - sqli
published: false
date: 2025-01-15T11:31:00
excalidraw-plugin: parsed
excalidraw-open-md: true
---
	# Techniques
![[sqli_types.png]]

## In band
- The attacker uses same channel to both launch an attack and gather the results
- Retrieved data is presented directly in the application webpage
- Comparatively easier to exploit than others
### Error based SQLi
- Forces the application to generate errors
- Attacks are refined according to the error
- Eg: `suhesh.com.np/app.php?id='` -> *You have an error in you SQL syntax, check the manual for your exact MySQL version......*
### Union Based SQLi
- Leverages UNION SQL operator to combine the result of each queries into single result set
- Eg:`suhesh.com.np/app.php?id=' UNION SELECT username, password FROM users--` ->
	```
	carlos
	pufpowjoasnxcano
	administrator
	opgq9u3fw9ejoajsda
	```
##### Database-specific syntax
On Oracle, every `SELECT` query must use the `FROM` keyword and specify a valid table. There is a built-in table on Oracle called `dual` which can be used for this purpose. So the injected queries on Oracle would need to look like:
`' UNION SELECT NULL FROM DUAL--`
The payloads described use the double-dash comment sequence `--` to comment out the remainder of the original query following the injection point. On MySQL, the double-dash sequence must be followed by a space. Alternatively, the hash character `#` can be used to identify a comment.

## Inferential (Blind) SQL injection
- No transfer of data via the web application
- Just as dangerous as In-Band SQLi as attackers might be able to reconstruct the information by sending particular requests and observing resulting behaviors of DB server
-  Takes longer to exploit
### Boolean Based SQLi
- Takes into account the behavior of whether the DB query generates TRUE or FALSE as a result
- Eg: 
```
URL: suhesh.com.np/app.php?id=1
Backend Query: select title from product where id=1
Payload 1 (FALSE):
suhesh.com.np/app.php?id=1 and 1=2
:=> Since the above query will result in false statement, no title will be displayed
Payload 2 (TRUE):
suhesh.com.np/app.php?id=1 and 1=1
:=> Since the above query will result in true statement, title will be displayed which will confirm the presence of a blind based SQLi
```
- Use case
-> Users Table:

| Username | Password |
| -------- | -------- |
| admin    | default  |
 
```
PAYLOAD: suhesh.com.np/app.php?id=1 and SUBSTRING((SELECT Password FROM Users WHERE Username="admin"),1,1)="a"
QUERY: select title from product where id=1 and SUBSTRING((SELECT Password FROM Users WHERE Username="admin"),1,1)="a"
```
What the above query does is checks if the first character  from the output of the query `SELECT Password FROM Users WHERE Username="admin"` is "a". The first character is not "a" thus no title is displayed on the page 
```
The output can be looped 
PAYLOAD: suhesh.com.np/app.php?id=1 and SUBSTRING((SELECT Password FROM Users WHERE Username="admin"),1,1)="d"
QUERY: select title from product where id=1 and SUBSTRING((SELECT Password FROM Users WHERE Username="admin"),1,1)="d"
```
Since the first element of the pasword is d, the title will be displayed.
### Time based SQLi
- Relies on database pausing for specified amount of time to output the results 
- Eg: If first character of admin's hashed password is "a", wait for 10seconds
		response takes 10sec -> the first character is "a" otherwise not
## Out-of-band (OAST) SQL Injection
- Consists of triggerring an out-of-band network connection to system attacker controls
- A variety of protocols can be used (common HTTP/DNS)

# Find How to??
## Black Box Testing
- Map the application (Burp proxy enabled)
- Fuzz the application with SQL characters
	- Submit characters like " or ' or # or -- and observe for errors or anomalies
	- Submit Boolean conditions like OR 1=1 and OR 1=2 observing application response
	- Submit payload to trigger time delays
	- Submit OAST payloads to trigger out-of-band network interaction if the server seems to have external connection
## White Box Testing
- Enable web server logging (helps to detect if SQL injection exists as errors will be logged in server)
- Enable database logging (helps to see what characters made it through)
- Map the application 
	- Visible functionality of application
	- Regex search all instances of code that talk to database
- Code review
	- Follow code path -> Fuzz the application with SQL characters
- Test potential SQLi 

# Exploit How To?
### Error based 
- Try out SQL-specific characters
- Different characters can generate different types of errors
### Union based
- The number and the order of the columns must be same in all queries
- Data types must be compatible
- **Exploitation:** 
	- Figure out number of columns the query is making
		- Use ORDER BY clause:
			- `select title, cost from product where id=1 ORDER BY 1` -> incrementally inject the ORDER BY value until you get an error or anomaly in application behaviour
			- `order by 1-- / order by 2-- / order by 3--` -> Position of 3 is out of range of number in list
		- Use NULL values:
			- `select title, cost from product where id=1 UNION SELECT NULL--` -> incrementally inject the number of NULL values until no error is received
			- `' UNION SELECT NULL--` -> All queries combined using UNION, INTERSECT and EXCEPT operator must have equal number of expressions in target list
			- `' UNION SELECT NULL, NULL--` -> This wont show any errors as there are only two columns *title and cost* which is equal to number of NULL 
	- Figure out datatypes of columns (Interested in strings)
		- Using UNION Based SQLi
			- Test whether the column can hold string data by probing it with a series of UNION SELECT payloads that places a string value to each column
			- `' UNION SELECT 'a', NULL--` -> Conversion failed converting varchar value 'a'  to datatype int
	**Union based exploitation**
	- Use union operator to output information from database
	**Boolean based exploitation**
	- Submit a Boolean expression that evaluates to *FALSE*, then an expression that evaluates to *TRUE* and note the response
	- Automate the process somehow to the database a series of TRUE/FALSE questions and monitor the response
	**Time based Blind exploitation**
	- Submit a payload that pauses the application for a specific amount of time 
	- Automate the process somehow to the database a series of TRUE/FALSE questions and monitor the response
	**Out-of-band exploitation**
	- Submit OAST payloads designed to trigger out of bank network connection when executed within a SQL query 
	- Use a variety of methods (HTTP or DNS) to exfil data

> **Warning**
	*Take care when injecting the condition OR 1=1 into a SQL query. Even if it appears to be harmless in the context you're injecting into, it's common for applications to use data from a single request in multiple different queries. If your condition reaches an UPDATE or DELETE statement, for example, it can result in an accidental loss of data.*

# Automated Exploitation Tools
1. [[SQLMAP]]
2. Web application vulnarability scanners *(Burpsuite, ZAP, Acutenix, Wapiti, arachni, w3af)*

# Prevention 
- Primary Defenses:
	 1. **Use of Prepared Statements (Parameterized Queries)**
		- The application specifies the query's structure with placeholders for each user input
		- The application specifies the content of each placeholder
	 2. **Use of Stored Procedures (Partial)**
		- A stored procedure is a batch of statements grouped together and stored in the database
		- Not always safe from SQL injection, still need to be called in a parameterized way
	 3. **Whitelist Input Validation (Partial)** 
		 - Defining what values are authorized. Everything else is considered unauthorized 
		 - Useful for values that cannot be specified as parameter placeholders, such as the table name.
	 4. **Escaping All User Supplied Input (Partial)**
		 - Only as a last resort 
- Additional Defenses:
	1. **Enforcing Least Privilege**
		- The application should use the lowest possible level of privileges when accessing the database
		- Any unnecessary default functionality in the database should be removed or disabled 
		- Ensure CIS benchmark for the database in use is applied
	2. **Performing Whitelist Input Validation as a Secondary Defense**

# Resources
1. [Web Security Academy - SQL Injection](https://portswiqqer.net/web-securitv/sq/-iniection)
2. Web Application Hacker's Handbook  ->  Chapter 9 - Attacking Data Stores
3. [OWASP - SQL Injection](https://_owasp.orq/www-community/attacks/SQL_Injection)
4. [OWASP — SQL Prevention Cheat Sheet](https://cheatsheetseries.owasp.orq/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html)
5. [PentestMonkey — SQL Injection](http://pentestmonkey.net/cateqory/cheat-sheet/sql-iniection)
  


%%
# Excalidraw Data
## Text Elements
SQL Injection ^6ZG7KNw8

In band (classic) ^OxI6MGX1

Inferential (blind) ^YqC0UePU

Out-of-band ^zGYCi79d

Error based ^FJets9mv

Union based ^bsUPXkvA

Boolean ^8RPOajdd

Time based ^fGWxAK3f

## Drawing
```compressed-json
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=
```
%%