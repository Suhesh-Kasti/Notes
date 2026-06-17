---
category: lab
tags:
  - training/web
  - vuln/sqli
platform: hackthebox
status: done
completed_date:
created: 2026-06-17
aliases:
  - SQLi Lab
---

## Lab: [[vuln--sql-injection]] UNION attack, finding a column containing text](https://portswigger.net/web-security/learning-paths/sql-injection/sql-injection-finding-columns-with-a-useful-data-type/sql-injection/union-attacks/lab-find-column-containing-text)

> This lab contains a SQL injection vulnerability in the product category filter. The results from the query are returned in the application's response, so you can use a UNION attack to retrieve data from other tables. To construct such an attack, you first need to determine the number of columns returned by the query. You can do this using a technique you learned in a previous lab. The next step is to identify a column that is compatible with string data.
	The lab will provide a random value that you need to make appear within the query results. To solve the lab, perform a SQL injection UNION attack that returns an additional row containing the value provided. This technique helps you determine which columns are compatible with string data.

*This lab teaches to find the datatypes of columns in a table ....*

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

## Attack theory:
#### UNION
1. `select a,b,c from table1 UNION select 'a', NULL, NULL`
	- Error -> the first column is not of datatype text
	- No error -> the first column is of datatype text
2.  `select a,b,c from table1 UNION select NULL, 1, NULL`
	- Error -> the second column is not of datatype int
	- No error -> the second column is of datatype int
### Finding if vulnerability exists
Using the SQLi `category='` in filter results in **Internal Server Error**.
### Attacking
- **Using ORDER BY to find number of columns:**
	Using ORDER BY 1, does nothing to column one is probably SN *(not displayed in the page)*
	Using ORDER BY 2, sorts the products in alphabetical order
	Using ORDER BY 3, sorts the price in ascending order
	Using ORDER BY 4, gives error. Most certainly because the table has only three columns
	**Used payload->**  `/filter?category=Gifts' ORDER BY 4--`

- **Using UNION select to insert data to find datatypes:**
	First we have to find which column among the three has datatype of string and inject the payload -> *Second column*
	**Used Payload ->**`/filter?category=Gifts' UNION select NULL, 'WgOsIR', NULL`

---
# Pythonizing for Automating
```python

```
