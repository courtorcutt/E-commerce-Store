```
├── LICENSE
├── README.md                        ======> Read Me
├── DailyScrumA4.md                  ======> Notes from scrum meeting in week of A4
├── DailyScrumA5.md                  ======> Notes from scrum meeting in week of A5
├── DailyScrumA6-1.md                ======> Notes from scrum meeting 1 in week of A6 
├── DailyScrumA6-2.md                ======> Notes from scrum meeting 2 in week of A6
├── A0-contract.md                   ======> Team contract
├── filestructure.md                 ======> this file
├── pull_request_template.md         ======> PR template
├── Dockerfile                       ======> Docker setup file
├── Docker-compose.yml               ======> Docker setup file
├── wait-for-it.sh                   ======> Docker setup file
├── db_init.sql                      ======> Docker setup file
├── SQL_Injection_Report.md          ======> SQL Injection Security Report
├── SQL_Injection_Report_Answers.md  ======> SQL Injection Security Report
├── SQL Injection Report V2.md       ======> SQL Injection Security Report 2
├── XSS Report 2.md                  ======> XSS Security Report 2
├── XSS_Injection_Report_Answers.md  ======> XSS Security Report
├── .github
│   └── workflows
│       ├── pytest.yml       ======> CI settings for running test automatically (trigger test for commits/pull-requests)
@@ -14,29 +20,32 @@
├── qbay                  ======> Application source code
│   └── templates                ======> html source code
│       ├── base.html            ======> base page that other pages extend
│       ├── create_product.html  ======> create product page
│       ├── home.html            ======> website home page
│       ├── login.html           ======> login page
│       ├── products.html        ======> products display page
│       ├── profile.html         ======> profile display page
│       ├── register.html        ======> register user page
│       └── update_profile.html  ======> update user profile page
│   ├── __init__.py       ======> Initialization code
│   ├── __main__.py       ======> Program entry point
│   ├── controllers.py    ======> Controls app route's for FE integration
│   ├── productMethods.py ======> Business logic functions for product-related operations (create, update)
│   ├── userDataAccess.py ======> Database manipulation for user-related operations (insert, search, update)
│   ├── userMethods.py    ======> Business logic functions for user-related operations (register, login, update)
│   └── models.py         ======> Data models
├── qbay_test            ======> Testing code
│   └── frontend                 ======> front-end testing files
│       ├── test_login.py             ======> test login FE page
│       ├── test_product_zcreate.py   ======> test product create FE page
│       ├── test_product_zzbuy.py     ======> test product buy FE page
│       ├── test_product_update.py    ======> test product update FE page
|       ├── test_user_register.py     ======> test register FE page
│       └── test_user_update.py       ======> test user update FE page
│   ├── __init__.py             ======> Required for a python module (can be empty)
│   ├── conftest.py             ======> Code to run before/after all the testing
│   ├── test_models.py          ======> Testing code for models.py
│   ├── Sql_injection_log.txt   ======> SQL injection testing output log
│   ├── cookie_report_sql_3.txt ======> SQL injection testing output log
│   ├── SQL_Injection_Report.md  ======> SQL injection security answers
│   ├── XSS_Injection_Report.md ======> XSS injection security answers
│   └── pwnxss_logs.md          ======> XSS security logs
└── requirements.txt             ======> Dependencies
```
