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
🚢 We did two rounds of scanning. Why the results are different? What is the purpose of adding in the session id?
🚢 Summarize the injection payload used based on the logs, and breifly discuss the purpose.
