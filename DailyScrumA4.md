## Daily Scrum Meeting

<img width="800" alt="Screen Shot 2021-11-03 at 1 36 41 PM" src="https://user-images.githubusercontent.com/59934073/140168962-44d0ba1d-08ea-4a02-a0ce-acaafe274f9d.png">
<img width="800" alt="Screen Shot 2021-11-03 at 1 36 45 PM" src="https://user-images.githubusercontent.com/59934073/140168964-244cbed2-cec1-4e5e-b45d-ec0831fc3366.png">


### Name of team member: Courtney
**Branch worked on:**
courtney_register_frontent_testing_in_progress

What is the progress so far? (at least some test cases written, more than 2)
- written all test cases
- black box testing methods are:
  - input partitioning
  - shotgun + input partitioning
  - output partitioning
- have not tested yet (development of test cases done, testing needs to be done)

Any difficulties?
- no difficulties

What is the plan for the days before the deadline?
- it will be done tonight
- needs to be tested locally using pytest
- then PR

### Name of team member: Talia
**Branch worked on:**
product_update_test

What is the progress so far? (at least some test cases written, more than 2)
- written all test cases
- black box testing methods are:
  - input partitioning
  - boundary testing
  - output partitioning

Any difficulties?
- I could have split my tests into clearer sections 
  using functions
- However, I could not because some of my tests
  depended on earlier parts of the code 

What is the plan for the days before the deadline?
- approve teammates PRs
- merge my own PR (still waiting on one approval)


### Name of team member: Zac
**Branch worked on:**
login_fe_test

What is the progress so far? (at least some test cases written, more than 2)
- testing login
- wrote test cases
- black box testing methods are:
  - functionality
  - input partitioning
  - output partitioning
- updating html files to add IDs to certain elements for reference from FE testing
- ran tests which failed

Any difficulties?
- only two requirements for login, hard to figure out how to make 3 different kinds of blackbox testing with few requirements
- general difficulty in understanding how it works

What is the plan for the days before the deadline?
- fix tests that have been failing
- seek help if needed (via teammates or prof)
- try to finish by tomorrow (thursday)
- then PR

### Name of team member: Brandon
**Branch worked on:**
BBtesting_product_creation

What is the progress so far? (at least some test cases written, more than 2)
- black box testing methods are:
  - hybrid input partitioning and shotgun
  - model based testing
  - output partitioning
- finished the first test and halfway thru second
- need to be tested (untested so far)

Any difficulties?
- no difficulties of note

What is the plan for the days before the deadline?
- finish tonight
- do PR

### Name of team member: Nathan
**Branch worked on:**
test_user_update

What is the progress so far? (at least some test cases written, more than 2)
- written all test cases 
- black box testing methods are:
  - used input partitioning
  - output partitioning
  - functionality testing
- all test cases tested and completed
- completely finished

Any difficulties?
- virtual environment not working (pytest arg error) "conflicting option string"
- had to create new venv and activate to get pytest to work
- figuring out how to assert JS messages using selenium
- decided to use assert(not self.assert_no_JS_errors) to get the test case where we WANT errors

What is the plan for the days before the deadline?
- approve teammates PRs
- merge my own PR
- document file structures
