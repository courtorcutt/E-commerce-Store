## SQL Injection Report

*Both logs that helped create this report can be found in qbay_test

### Table of the SQL injection scanning results for the sql_injection_log.txt logs

|                 | Route/URL | Parameter | Number of Injection Trials |Number of Successful Trials |
| ----------- | ----------- |----------- |----------- |----------- |
| Scan    | http://127.0.0.1:8081/login    | email |   14  |   0  |
| Scan    | http://127.0.0.1:8081/login    | password  |  14   |  0   |
| Scan    | http://127.0.0.1:8081/register   | first_name  |  14   |  0  |
| Scan    | http://127.0.0.1:8081/register   | last_name    |   14  |  0   |
| Scan    | http://127.0.0.1:8081/register   | email |  14   |  0  |
| Scan    | http://127.0.0.1:8081/register   | user_name   |   14  |  0   |
| Scan    | http://127.0.0.1:8081/register   | password1 |  14   |  0  |
| Scan    | http://127.0.0.1:8081/register   | password2    |   14  |  0   |
| Scan    | http://127.0.0.1:8081/register   | shipping_address   |   14  |  0   |
| Scan    | http://127.0.0.1:8081/register   | postal_code   |   14  |  0   |
| Scan    | http://127.0.0.1:8081/register   | balance  |   14  |  0   |


### Table of the SQL injection scanning results for the cookie_report_sql_3.txt logs

|                 | Route/URL | Parameter | Number of Injection Trials |Number of Successful Trials |
| ----------- | ----------- |----------- |----------- |----------- |
| Scan    | http://127.0.0.1:8081/create_product   | title  |   17  |   0  |
| Scan    | http://127.0.0.1:8081/create_product   | price  |   17  |   0  |
| Scan    | http://127.0.0.1:8081/create_product   | description  |   16  |   0  |
| Scan    | http://127.0.0.1:8081/create_product   | date  |   16  |   0  |
| Scan    | http://127.0.0.1:8081/products   | id  |   16  |   0  |
| Scan    | http://127.0.0.1:8081/products   | title  |   16  |   0  |
| Scan    | http://127.0.0.1:8081/products  | description  |   16  |   0  |
| Scan    | http://127.0.0.1:8081/products   | type  |   16  |   0  |
| Scan    | http://127.0.0.1:8081/products   | price  |   16  |   0  |
| Scan    | http://127.0.0.1:8081/register   | first_name  |  17  |  0  |
| Scan    | http://127.0.0.1:8081/register   | last_name    |   17  |  0   |
| Scan    | http://127.0.0.1:8081/register   | email |  17   |  0  |
| Scan    | http://127.0.0.1:8081/register   | user_name   |   17  |  0   |
| Scan    | http://127.0.0.1:8081/register   | password1 |  17   |  0  |
| Scan    | http://127.0.0.1:8081/register   | password2    |   17  |  0   |
| Scan    | http://127.0.0.1:8081/register   | shipping_address   |   17  |  0   |
| Scan    | http://127.0.0.1:8081/register   | postal_code   |   17  |  0   |
| Scan    | http://127.0.0.1:8081/register   | balance  |   17  |  0   |
| Scan    | http://127.0.0.1:8081/update-profile   | user_name |   16  |   0  |
| Scan    | http://127.0.0.1:8081/update-profile   | shipping_address |   16  |   0  |
| Scan    | http://127.0.0.1:8081/update-profile   | postal_code |   16  |   0  |
| Scan    | http://127.0.0.1:8081/update-profile   | shipping_address |   16  |   0  |
| Scan    | http://127.0.0.1:8081/update-profile   | shipping_address |   16  |   0  |

*Both logs that helped create this report can be found in qbay_test


The following commands were used:

python3 qbay_test/sqlmap-master/sqlmap.py -u http://127.0.0.1:8081/ --forms --batch --crawl=10

python3 qbay_test/sqlmap-master/sqlmap.py -u http://127.0.0.1:8081/ --forms --batch --crawl=10 --cookie=eyJ1c2VyX2xvZ2dlZF9pbiI6InRhbGlhLmwuZWR3YXJkc0BnbWFpbC5jb20ifQ.YZgreA.3N_VUMGOeTiLhawSn4RQqBYu0c4



📖 Questions:

🚢 Are all the user input fileds in your application covered in all the test cases above? Any successful exploit?

All fields are covered in the application. Although the assignment instructions indicate that the “register” and “create_product” functions should be tested, the security report outlines scanning results for all input parameters of every function, which are different than others (e.g., “product” has ID associated with it but “create_product” does not). 

There are no successful exploits, since a successful one can read sensitive data. As indicated by the last column of the sql_injection_log.txt table, there are 0 successful exploits in all trials. Also note the commands used to perform SQL injection: “--forms,” “--batch,” and “--crawl.” “—form” was used to parse the pages (e.g., login, create product, etc.) to test specific fields. “--batch” bypasses interactive session requirements such that sqlmap.py uses a default value to proceed without asking the user to input one. We included --crawl” at the end of them. This is helpful in exposing vulnerabilities as Crawl searches the website for root locations. The depth we defined was 10, so sqlmap.py was instructed to crawl up to 10 directories, and none were excluded. By integrating all three commands, crafted inputs are less likely to pass through as this checks pages with larger numbers of form fields (e.g., create product has many more fields than login) via non-interactive and interactive sessions.


🚢 We did two rounds of scanning. Why the results are different? What is the purpose of adding in the session id?

In terms of successful exploits, there are no differences seen in the results. However, the second round consisted of testing more functions, not just login and register like the first round did. This meant more parameters were being tested, and ultimately increased the number of injection trials. This increase in trials is also proportional using cookies and retrieving session IDs.

In terms of session objects, a new ID is generated for each page request until the session object is accessed. The reason we have a session ID is to identify that a user has logged in, where this information is stored via a cookie. Recall that a cookie is simply data in text format, stored by the browser on the computer. This is all the information a black-hat hacker requires to gain SSO access. If the hacker can access the user’s cookie inserted, they can “steal” their session token by inserting their own cookie. If for example the session ID was changed to a statement that consisted of “OR 1=1,” the hacker would be authenticated as a valid user. This means that variables used for cookies should be added to list of parameters to be checked. As a result, it is always bad to create a query by concatenating variables as the structure of the attacker’s SQL command can select all person rows rather than one specific user. 

🚢 Summarize the injection payload used based on the logs, and breifly discuss the purpose.

The injection payload is based on an open-source, automated, SQL penetration testing tool called sqlmap.py. This file is able to execute commands on an OS through out-of-band connections (remote control via secure connection through secondary interface). It also incorporates many, if not all, of the SQL injection techniques from the CISC/CMPE 327 course material. This includes out-of-band, UNION (query-based), stacked queries, boolean-based, time-based, and error-based. The two most important (susceptible for qbay) would be UNION and stacked queries. UNION, where SELECT statements are used to combine two queries into a single result. For stacked queries, attackers aren’t restricted by preceding query roes, so they can modify data and call stored procedures by terminating original query and subsequently adding a new one. 
