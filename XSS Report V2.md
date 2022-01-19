# XSS Report V2

**Logs that helped create the following XSS tables can be seen in the folder, [qbay](https://github.com/nathank77/CMPE327-Group7/tree/main/qbay)**
**The commands used to initiate the XSS via pwnxss.py are namely,**
```
python pwnxss.py -u http://127.0.0.1:8081/
python pwnxss.py -u http://192.168.2.20:8081/ --cookie='{"session":"session=eyJ1c2VyX2xvZ2dlZF9pbiI6IkJydWNlV2F5bmUyM0BnbWFpbC5jb20ifQ.YbI36g.dcVuzmrZsGZPe0v9V7zVWL3Ul-E"}'
```

### Table of pwnxss.py results with cmd 1 above (without authentication, or before cookie)

|      |            Route/URL           | Parameter |       XSS successful?      |
|------|--------------------------------|-----------|----------------------------|
| Scan | http://127.0.0.1:8081/register | first_name|             YES            |
| Scan | http://127.0.0.1:8081/register | last_name |             YES            |
| Scan | http://127.0.0.1:8081/register | email     |             YES            |          
| Scan | http://127.0.0.1:8081/register | user_name |             YES            |
| Scan | http://127.0.0.1:8081/register | password1 |             YES            |
| Scan | http://127.0.0.1:8081/register | password2 |             YES            | 
| Scan | http://127.0.0.1:8081/register | shipping_address |      YES            |
| Scan | http://127.0.0.1:8081/register | postal_code |           YES            |
| Scan | http://127.0.0.1:8081/register | balance   |             YES            |
| Scan | http://127.0.0.1:8081/login    | email     |             YES            | 
| Scan | http://127.0.0.1:8081/login    | password  |             YES            |                       
| Scan | http://127.0.0.1:8081/profile  | email     |             NO             | 
| Scan | http://127.0.0.1:8081/profile  | password  |             NO             | 
| Scan | http://127.0.0.1:8081/products | email     |             NO             |
| Scan | http://127.0.0.1:8081/products | password  |             NO             |
| Scan | http://127.0.0.1:8081/buy_product | email  |             NO             |
| Scan | http://127.0.0.1:8081/buy_product | password |           NO             |      
| Scan | http://127.0.0.1:8081/create_product | email |           NO             |          
| Scan | http://127.0.0.1:8081/create_product | password |        NO             |

### Table of sqlmap.py results with cmd 2 above (with authentication, after cookie was collected from request header)

|      |            Route/URL           | Parameter |       XSS successful?      |
|------|--------------------------------|-----------|----------------------------|
| Scan | http://192.168.2.20:8081/create_product | title |             YES       |
| Scan | http://192.168.2.20:8081/create_product | price |             YES       |
| Scan | http://192.168.2.20:8081/create_product | description |       YES       |          
| Scan | http://192.168.2.20:8081/create_product | date |              YES       |
| Scan | http://192.168.2.20:8081/products | title |                   NO        |
| Scan | http://192.168.2.20:8081/products | price |                   NO        |
| Scan | http://192.168.2.20:8081/products | description |             NO        |          
| Scan | http://192.168.2.20:8081/products | date |                    NO        |
| Scan | http://192.168.2.20:8081/register | first_name |              YES       |
| Scan | http://192.168.2.20:8081/register | last_name |               YES       | 
| Scan | http://192.168.2.20:8081/register | email |                   YES       |                       
| Scan | http://192.168.2.20:8081/register | user_name |               YES       | 
| Scan | http://192.168.2.20:8081/register | password1 |               YES       | 
| Scan | http://192.168.2.20:8081/register | password2 |               YES       |
| Scan | http://192.168.2.20:8081/register | shipping_address |        YES       |
| Scan | http://192.168.2.20:8081/register | postal_code |             YES       |
| Scan | http://192.168.2.20:8081/register | balance |                 YES       |      
| Scan | http://192.168.2.20:8081/buy_product | id |                   NO        |    
| Scan | http://192.168.2.20:8081/update-profile | user_name |         NO        |          
| Scan | http://192.168.2.20:8081/update-profile | shipping_address |  NO        |
| Scan | http://192.168.2.20:8081/update-profile | postal_code |       NO        |

📖 Questions:

🚢 Are all the user input fields in your application covered in all the test cases above? Are there any successful exploits?

All input fields are covered in the application. The first round of XSS scanning consisted of analyzing route pages, and the second round consisted of utilizing a cookie corresponding to a session ID, which would cover the additional case of updating a product with a registered user, already logged in, who has created a product (passing three routes). It is important to note that the significane difference between this report and the one from Assignment #5 is that the buy_product function was also scanned!

There are successful exploits. In terms of the first round, XSS is successful in login and register functions. This means that an attacker is capable of sending a malicious script, accessing browser information such as passwords, usernames, email addresses, and other parameters associated with these functions. For the second round, the same applies, but the create_product function can also be exploited. Because this second round has cookies being used, an attacker can initiate first-order CSS, where a snippet can reflect any user that creates a product. Intuitively, this demonstrates that mitigation strategies were not implemented to protect the user’s information, such as sanitizing the HTML inputs and local fields for create product (title, description, price, date). As such, preventative measures such as using an HttpOnly flag or a secure cookie would benefit the frontend vulnerability.

🚢 What type of XSS is covered? Stored or reflected, and why?

The type of XSS seen from the exploitations would be reflected XSS since the non-persistent data are not escaped. For example, for the login page, where a registered user must input their username and password, the queries might produce alert boxes in which the attacker can analyze what the page displays and can create their own URL. This means that the malicious script comes from the HTTP request information and embeds input into the webpage.

🚢 Summarize the malicious script/crafted request (URL) used based on logs, and discuss its purpose?

PwnXSS is an open-source tool designed to locate cross-site scripting vulnerabilities in code. It consists of crawler functionality as well as POST and GET forms. Initially, the crawler essentially spiders the target where PwnXSS identifies all pages, including injectable parameters in forms, URLs, headers, etc. Next, the scanner injects a string in the tested parameter and checks for a reflection. If a certain set of HTML characters are returned, then the page is vulnerable since it lacks sanitization. Intuitively, the test string did not survive input validation. Systematically, this means custom data injections and other corresponding parameters were not double-checked.
