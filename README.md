# E-Commerce Store (used Python, Flask, and Bootstrap for the CSS. Everything was tested using black-box methods such as functionality, input-partitioning, output-partitioning, and boundary testing. All code met PEP8 standards, used a pull request template, and is well commented.)

Using Scrum - athe gile development methodology, this e-commerce store was created over the span of four months and is still continuing to be improved. Through six sprints focusing on the backend, frontend, security, and deployment of the store, a basic version of eBay was created. 

First the database models were created in the backend. This consisted of Users, Product, Transaction, and Review. For example, below is a snipet of the Users model.

<img width="496" alt="Screen Shot 2022-01-15 at 2 22 40 AM" src="https://user-images.githubusercontent.com/72311187/149605394-90a26cc7-ecfd-4ab1-ab10-9c6565578f4e.png">

Then the backend models were connected with the frontend. The frontend has a Base.html file which uses Bootstrap to create a navigation bar as seen in the photo below. 

<img width="179" alt="Screen Shot 2022-01-15 at 2 25 17 AM" src="https://user-images.githubusercontent.com/72311187/149605486-b548ac2f-27e9-4bf4-807c-f27c42f5668d.png">
<img width="510" alt="Screen Shot 2022-01-15 at 2 31 43 AM" src="https://user-images.githubusercontent.com/72311187/149605673-21e742a1-0728-4cd8-8af6-9a49d6324580.png">

The backend attributes were then connected with the frontend files using their IDs and the GET method.
<img width="771" alt="Screen Shot 2022-01-15 at 2 33 42 AM" src="https://user-images.githubusercontent.com/72311187/149605730-32bcc2dc-8a98-4ce5-bc8b-9d48afa0faf5.png">

All backend and frontend files were tested using black-box methods. Below is an example of input partitioning for the register.html file. There are 42 other tests in this file for register alone. All other frontend files were tested thouroughly.  
<img width="515" alt="Screen Shot 2022-01-15 at 2 36 11 AM" src="https://user-images.githubusercontent.com/72311187/149605819-e25756a9-4b99-4d01-a6c5-71453e05b202.png">

The backend models were tested rigourously as well to ensure the user had a complex enough password, the email format is valid, sections aren't left blank, there are no spaces in the username, etc.

<img width="564" alt="Screen Shot 2022-01-15 at 2 39 27 AM" src="https://user-images.githubusercontent.com/72311187/149605909-49515153-043c-4552-8a63-24864d9288a4.png">

The controllers.py has functions for all the webpage routes (navigation file). It defines which functions use GET and POST methods, validates login and registration input and flashes an error when something doesn't pass the testing. The productsMethods.py file checks to ensure the product inputs meet all requirements. The userDataAccess.py file contains 4 key functions of searching for a specific user, updating a users information, updating a users bank balance, as well as inserting the user into the database. 

Then the security of the store was tested. Reports of XSS attacks and SQL injection attacks are visible in the repository. As I update this repository, I will be focusing more on the security of the application. 

At the end Docker was used to create an image of the repository to deploy it. Here is the link:  
