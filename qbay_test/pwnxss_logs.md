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

Second (Cookie) Scan:
|      | Route/URL                      | Parameter | XSS successful?            |
|:----:|--------------------------------|:---------:|:--------------------------:|
| Scan | http://127.0.0.1:8081/update-profile| user_name|             "Not 100% yet"|
|      |                                | shipping_address |             "Not 100% yet"|
|      |                                | postal_code |             "Not 100% yet"|
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
| Scan | http://127.0.0.1:8081/products | title     |        "Not 100% yet"      |
|      |                                | price	    |        "Not 100% yet"      |
|      |                                | description|        "Not 100% yet"     |
|      |                                | date	    |        "Not 100% yet"      |
|      |                                |           |                            |
| Scan | http://127.0.0.1:8081/create_product| title     |        YES            |
|      |                                | price	    |        YES                 |
|      |                                | description|        YES                |
|      |                                | date	    |        YES                 |