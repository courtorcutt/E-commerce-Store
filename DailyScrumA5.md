## Daily Scrum Meeting

![Screen Shot 2021-11-19 at 3 08 19 PM](https://user-images.githubusercontent.com/59934073/142685355-0c638150-56ec-4b18-a698-a801ad8d7eaa.png)


### Name of team member: Courtney
**Branch worked on:**
courtney_shipping

What is the progress so far? 
- made docker repo
- added and modified files as needed to ship entire system
- basically done

Any difficulties?
- small errors

What is the plan for the days before the deadline?
- will hopefully be done within the next few hours (and pushed)

### Name of team member: Talia
**Branch worked on:**
sql_injection_report

What is the progress so far?
-I have both logs collected for SQL injection. 
- I used these commands: 
python3 qbay_test/sqlmap-master/sqlmap.py -u http://127.0.0.1:8081/ --forms --batch --crawl=10

python3 qbay_test/sqlmap-master/sqlmap.py -u http://127.0.0.1:8081/ --forms --batch --crawl=10 --cookie=eyJ1c2VyX2xvZ2dlZF9pbiI6InRhbGlhLmwuZWR3YXJkc0BnbWFpbC5jb20ifQ.YZcsMw.wEuMhOe9f1NtDeZLdAJLaJQnF8I 

Any difficulties?
- I had a strange issue trying to log in 
- It resolved itself on its own

What is the plan for the days before the deadline?
- compile a SQL injection scanning report by filling a table
- create PR 
- approve team members PR


### Name of team member: Zac
**Branch worked on:**
XSS_Report (not a branch yet, will be named this when report is done)

What is the progress so far?
- installed PwnXSS
- installed dependencies

Any difficulties?
- PwnXSS not working

What is the plan for the days before the deadline?
- email Dr. Ding to try to find solution
- troubleshoot "internal error when trying to run PwnXSS"

### Name of team member: Brandon
**Branch worked on:**


What is the progress so far? 
- 

Any difficulties?
- 

What is the plan for the days before the deadline?
- 

### Name of team member: Nathan
**Branch worked on:**
ship_the_container

What is the progress so far? (at least some test cases written, more than 2)
- set up docker repo
- added files to ship container from web option repo
- pushed files to docker
- seems to be running well

Any difficulties?
- sometimes not running/pulling from docker as expected on other machines
- docker error or error in our code?

What is the plan for the days before the deadline?
- merge PR
- possibly troubleshoot error of not running on other machines



