First Scan:
|      | Route/URL                      | Parameter | XSS successful?            |
|:----:|--------------------------------|:---------:|:--------------------------:|
| Scan | http://127.0.0.1:8081/login    | email     |             YES            |
|      |                                | password  |             YES            |
|      |                                |           |                            |
|      | http://127.0.0.1:8081/register | first_name|             YES            |
|      |                                | last_name |             YES            |
|      |                                | email     |             YES            |
|      |                                | user_name |             YES            |
|      |                                | password1 |             YES            |
|      |                                | password2 |             YES            |
|      |                                | shipping_address |             YES     |
|      |                                | postal_code |             YES          |
|      |                                | balance   |             YES            |
|      |                                |           |                            |
| Scan | http://127.0.0.1:8081/profile  | email     |        "Not 100% yet"      |
|      |                                | password  |        "Not 100% yet"      |
|      |                                |           |                            |
| Scan | http://127.0.0.1:8081/products | email     |        "Not 100% yet"      |
|      |                                | password  |        "Not 100% yet"      |
|      |                                |           |                            |
| Scan | http://127.0.0.1:8081/create_product | email     |        "Not 100% yet"|
|      |                                | password  |        "Not 100% yet"      |

📖 Questions:

🚢 Are all the user input fields in your application covered in all the test cases above? Are there any successful exploits?

All input fields are covered in the application. The first round of XSS scanning consisted of analyzing route pages, and the second round consisted of utilizing a cookie corresponding to a session ID, which would cover the additional case of updating a product with a registered user, already logged in, who has created a product (passing three routes).

There are successful exploits. In terms of the first round, XSS is successful in login and register functions. This means that an attacker is capable of sending a malicious script, accessing browser information such as passwords, usernames, email addresses, and other parameters associated with these functions. For the second round, the same applies, but the create product function can also be exploited. Because this second round has cookies being used, an attacker can initiate first-order CSS, where a snippet can reflect any user that creates a product. Intuitively, this demonstrates that mitigation strategies were not implemented to protect the user’s information, such as sanitizing the HTML inputs and local fields for create product (title, description, price, date). As such, preventative measures such as using an HttpOnly flag or a secure cookie would benefit the frontend vulnerability

🚢 What type of XSS is covered? Stored or reflected, and why?

The type of XSS seen from the exploitations would be reflected XSS since the non-persistent data are not escaped. For example, for the login page, where a registered user must input their username and password, the queries might produce alert boxes in which the attacker can analyze what the page displays and can create their own URL. This means that the malicious script comes from the HTTP request information and embeds input into the webpage.

🚢 Summarize the malicious script/crafted request (URL) used based on logs, and discuss its purpose?

PwnXSS is an open-source tool designed to locate cross-site scripting vulnerabilities in code. It consists of crawler functionality as well as POST and GET forms. Initially, the crawler essentially spiders the target where PwnXSS identifies all pages, including injectable parameters in forms, URLs, headers, etc. Next, the scanner injects a string in the tested parameter and checks for a reflection. If a certain set of HTML characters are returned, then the page is vulnerable since it lacks sanitization. Intuitively, the test string did not survive input validation. Systematically, this means  custom data injections and other corresponding parameters were not double-checked.
