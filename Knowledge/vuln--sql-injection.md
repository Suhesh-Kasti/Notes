---
category: knowledge
tags:
  - vuln/sqli
  - reference
platform: n/a
status: done
created: 2026-06-17
aliases:
  - Techniques
---

# Techniques
![[images/sqli_types.png]]

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

## Inferential (Blind) [[vuln--sql-injection]]
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
