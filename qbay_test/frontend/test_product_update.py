from seleniumbase import BaseCase

from qbay_test.conftest import base_url
from unittest.mock import patch
from qbay.models import User

"""
This file contains the test for the product update frontend
Three black box testing methods will be used:
   - Exhaustive testing (with input partitioning)
   - Boundary testing
   - Output testing
"""


class FrontEndProductPageTesting(BaseCase):

    def test_product_update(self, *_):
        """
        This is a sample front end unit test to login to home page
        and verify if the tickets are correctly listed.
        """
        # open update page
        # 3 possibilities
        # - product page
        # - no user - redirect to login
        # - no products - redirect to product creation
        # because of this a user must be registered
        # and a product must be created
        self.open(base_url + '/register')
        # register a user
        self.type("#email", "talia.l.edwards@gmail.com")
        self.type("#password1", "mbd!xgw9UZA!xkt7zpu")
        self.type("#password2", "mbd!xgw9UZA!xkt7zpu")
        self.type("#balance", "200")
        self.type("#first_name", "Talia")
        self.type("#last_name", "Edwards")
        self.type("#postal_code", "K1W 1K8")
        self.type("#shipping_address", "235 BeepBeep st")
        self.type("#user_name", "OOGAbooga")

        # click enter button
        self.click('button[type="submit"]')
        # logout
        self.open(base_url + '/logout')
        # open products page but get redirected to log in page
        self.open(base_url + '/products')
        # login with existing user
        self.type("#email", "talia.l.edwards@gmail.com")
        self.type("#password", "mbd!xgw9UZA!xkt7zpu")
        # click enter button
        self.click('button[type="submit"]')
        # open products page but get redirected to create object page
        self.open(base_url + '/products')
        self.type("#date", "10-10-2021")
        self.type("#description", "This is an AWESOME object WOOP WOOP")
        self.type("#price", "400")
        self.type("#title", "This is the first new object")
        # click enter button
        self.click('button[type="submit"]')

        # open products page
        self.open(base_url + '/products')
        # test if the page loads correctly
        self.assert_text("Here are all of your products Talia")
        self.assert_text("ID: 4")
        self.assert_text("Description: This is an AWESOME object WOOP WOOP")
        self.assert_text("Type: None")
        self.assert_text("Title: This is the first new object")
        self.assert_text("Price: 400.0")
        self.click('button[id="form_button"]')
        self.assert_text("Enter the id of the product you wish to update")

        # test method 1
        # begin partition testing
        # begin test 1.1
        # test for all fields entered correctly
        self.type("#id", "4")
        self.type("#price", "700")
        self.type("#title", "New Better Title")
        self.type("#description", "This is the first update")
        self.type("#type", "food item")
        self.click('button[type="submit"]')

        # check if update was a success
        self.assert_text("Update Successful")
        self.assert_text("ID: 4")
        self.assert_text("Description: This is the first update")
        self.assert_text("Type: food item")
        self.assert_text("Title: New Better Title")
        self.assert_text("Price: 700.0")
        # end of test 1.1

        # begin test 1.2
        # test for all fields entered incorrectly
        self.click('button[id="form_button"]')
        self.type("#id", "4")
        self.type("#price", "1")
        self.type("#title", "!!!")
        self.type("#description", "to")
        self.type("#type", "!!!")
        self.click('button[type="submit"]')

        # check if update was a success
        self.assert_text("This title is wrong The type is wrong "
                         "The price is wrong The description is wrong")
        self.assert_text("ID: 4")
        self.assert_text("Description: This is the first update")
        self.assert_text("Type: food item")
        self.assert_text("Title: New Better Title")
        self.assert_text("Price: 700.0")
        # end of test 1.2

        # begin test 1.3
        # test for wrong id entered
        self.click('button[id="form_button"]')
        self.type("#id", "24")
        self.click('button[type="submit"]')

        # check if update was a success
        self.assert_text("INVALID ID")
        self.assert_text("ID: 4")
        self.assert_text("Description: This is the first update")
        self.assert_text("Type: food item")
        self.assert_text("Title: New Better Title")
        self.assert_text("Price: 700.0")
        # end of test 1.3

        # begin test 1.4
        # test for only title entered
        self.click('button[id="form_button"]')
        self.type("#title", "New Better Title 2")
        self.type("#id", "4")
        self.click('button[type="submit"]')

        # check if update was a success
        self.assert_text("Update Successful")
        self.assert_text("ID: 4")
        self.assert_text("Description: This is the first update")
        self.assert_text("Type: food item")
        self.assert_text("Title: New Better Title 2")
        self.assert_text("Price: 700.0")
        # end of test 1.4

        # begin test 1.5
        # test for only type entered
        self.click('button[id="form_button"]')
        self.type("#type", "Fridge")
        self.type("#id", "4")
        self.click('button[type="submit"]')

        # check if update was a success
        self.assert_text("Update Successful")
        self.assert_text("ID: 4")
        self.assert_text("Description: This is the first update")
        self.assert_text("Type: Fridge")
        self.assert_text("Title: New Better Title 2")
        self.assert_text("Price: 700.0")
        # end of test 1.5

        # begin test 1.6
        # test for only description entered
        self.click('button[id="form_button"]')
        self.type("#description",
                  "Description: This is no longer "
                  "the first update")
        self.type("#id", "4")
        self.click('button[type="submit"]')

        # check if update was a success
        self.assert_text("Update Successful")
        self.assert_text("ID: 4")
        self.assert_text("Description: This is no longer"
                         " the first update")
        self.assert_text("Type: Fridge")
        self.assert_text("Title: New Better Title 2")
        self.assert_text("Price: 700.0")
        # end of test 1.6

        # begin test 1.7
        # test for only price entered
        self.click('button[id="form_button"]')
        self.type("#price", "999")
        self.type("#id", "4")
        self.click('button[type="submit"]')

        # check if update was a success
        self.assert_text("Update Successful")
        self.assert_text("ID: 4")
        self.assert_text("Description: This is no longer"
                         " the first update")
        self.assert_text("Type: Fridge")
        self.assert_text("Title: New Better Title 2")
        self.assert_text("Price: 999.0")
        # end of test 1.7

        # end of partition testing method 1

        # Test Method #2 : Boundary Testing
        # begin test 2.1
        # test limit of title

        # check if it works with space at beginning and end
        # and when title == 1 (low boundary)
        self.click('button[id="form_button"]')
        self.type("#title", " N ")
        self.type("#id", "4")
        self.click('button[type="submit"]')
        self.assert_text("Update Successful")
        self.assert_text("ID: 4")
        self.assert_text("Description: This is no longer"
                         " the first update")
        self.assert_text("Type: Fridge")
        self.assert_text("Title: N")
        self.assert_text("Price: 999.0")

        # check higher boundary when title == 80
        self.click('button[id="form_button"]')
        self.type("#title", "NewBetter Title 2 New New Better Title 2"
                            "NewBetter Title 2 New New Better Title 2")
        self.type("#id", "4")
        self.click('button[type="submit"]')
        self.assert_text("Update Successful")
        self.assert_text("ID: 4")
        self.assert_text("Description: This is no longer"
                         " the first update")
        self.assert_text("Type: Fridge")
        self.assert_text("Title: NewBetter Title 2 New New Better Title 2"
                         "NewBetter Title 2 New New Better Title 2")
        self.assert_text("Price: 999.0")

        # end test 2.1

        # begin test 2.2
        # test limit of description
        # check if description can be slightly bigger than title
        self.click('button[id="form_button"]')
        self.type("#description", "NewBetter Title 2 New New Better Title 2"
                                  "NewBetter Title 2 New New Better Title 21")
        self.type("#id", "4")
        self.click('button[type="submit"]')
        self.assert_text("Update Successful")
        self.assert_text("ID: 4")
        self.assert_text("Description: NewBetter Title 2 "
                         "New New Better Title 2"
                         "NewBetter Title 2 New New Better Title 21")
        self.assert_text("Type: Fridge")
        self.assert_text("Title: NewBetter Title 2 New New Better Title 2"
                         "NewBetter Title 2 New New Better Title 2")
        self.assert_text("Price: 999.0")

        # check higher boundary boundary of 2000
        self.click('button[id="form_button"]')
        self.type("#title", "Yes1")
        self.type("#description", "veeeeeerrrryyyyy lonngggggggggggg" +
                  " veeeeeerrrryyyyy lonngggggggggggg" +
                  " veeeeeerrrryyyyy lonngggggggggggg" +
                  " veeeeeerrrryyyyy lonngggggggggggg" +
                  " veeeeeerrrryyyyy lonngggggggggggg" +
                  " veeeeeerrrryyyyy lonngggggggggggg" +
                  " veeeeeerrrryyyyy lonngggggggggggg" +
                  " veeeeeerrrryyyyy lonngggggggggggg" +
                  " veeeeeerrrryyyyy lonngggggggggggg" +
                  " veeeeeerrrryyyyy lonngggggggggggg" +
                  " veeeeeerrrryyyyy lonngggggggggggg" +
                  " veeeeeerrrryyyyy lonngggggggggggg" +
                  " veeeeeerrrryyyyy lonngggggggggggg" +
                  " veeeeeerrrryyyyy lonngggggggggggg" +
                  " veeeeeerrrryyyyy lonngggggggggggg" +
                  " veeeeeerrrryyyyy lonngggggggggggg" +
                  " veeeeeerrrryyyyy lonngggggggggggg" +
                  " veeeeeerrrryyyyy lonngggggggggggg" +
                  " veeeeeerrrryyyyy lonngggggggggggg" +
                  " veeeeeerrrryyyyy lonngggggggggggg" +
                  " veeeeeerrrryyyyy lonngggggggggggg" +
                  " veeeeeerrrryyyyy lonngggggggggggg" +
                  " veeeeeerrrryyyyy lonngggggggggggg" +
                  " veeeeeerrrryyyyy lonngggggggggggg" +
                  " veeeeeerrrryyyyy lonngggggggggggg" +
                  " veeeeeerrrryyyyy lonngggggggggggg" +
                  " veeeeeerrrryyyyy lonngggggggggggg" +
                  " veeeeeerrrryyyyy lonngggggggggggg" +
                  " veeeeeerrrryyyyy lonngggggggggggg" +
                  " veeeeeerrrryyyyy lonngggggggggggg" +
                  " veeeeeerrrryyyyy lonngggggggggggg" +
                  " veeeeeerrrryyyyy lonngggggggggggg" +
                  " veeeeeerrrryyyyy lonngggggggggggg" +
                  " veeeeeerrrryyyyy lonngggggggggggg" +
                  " veeeeeerrrryyyyy lonngggggggggggg" +
                  " veeeeeerrrryyyyy lonngggggggggggg" +
                  " veeeeeerrrryyyyy lonngggggggggggg" +
                  " veeeeeerrrryyyyy lonngggggggggggg" +
                  " veeeeeerrrryyyyy lonngggggggggggg" +
                  " veeeeeerrrryyyyy lonngggggggggggg" +
                  " veeeeeerrrryyyyy lonngggggggggggg" +
                  " veeeeeerrrryyyyy lonngggggggggggg" +
                  " veeeeeerrrryyyyy lonngggggggggggg" +
                  " veeeeeerrrryyyyy lonngggggggggggg" +
                  " veeeeeerrrryyyyy lonngggggggggggg" +
                  " veeeeeerrrryyyyy lonngggggggggggg" +
                  " veeeeeerrrryyyyy lonngggggggggggg" +
                  " veeeeeerrrryyyyy lonngggggggggggg" +
                  " veeeeeerrrryyyyy lonngggggggggggg" +
                  " veeeeeerrrryyyyy lonngggggggggggg" +
                  " veeeeeerrrryyyyy lonngggggggggggg" +
                  " veeeeeerrrryyyyy lonngggggggggggg" +
                  " veeeeeerrrryyyyy lonngggggggggggg" +
                  " veeeeeerrrryyyyy lonngggggggggggg" +
                  " veeeeeerrrryyyyy lonngggggggggggg" +
                  " veeeeeerrrryyyyy lonngggggggggggg" +
                  " veeeeeerrrryyyyy lonngggggggggggg" +
                  "eeerrrryyyyy lonngggggggggggg" +
                  " veeeeeerrrryyyyy lonngggggggggggg")
        self.type("#id", "4")
        self.click('button[type="submit"]')
        self.assert_text("Update Successful")
        self.assert_text("ID: 4")
        self.assert_text("Description: veeeeeerrrryyyyy lonngggggggggggg" +
                         " veeeeeerrrryyyyy lonngggggggggggg" +
                         " veeeeeerrrryyyyy lonngggggggggggg" +
                         " veeeeeerrrryyyyy lonngggggggggggg" +
                         " veeeeeerrrryyyyy lonngggggggggggg" +
                         " veeeeeerrrryyyyy lonngggggggggggg" +
                         " veeeeeerrrryyyyy lonngggggggggggg" +
                         " veeeeeerrrryyyyy lonngggggggggggg" +
                         " veeeeeerrrryyyyy lonngggggggggggg" +
                         " veeeeeerrrryyyyy lonngggggggggggg" +
                         " veeeeeerrrryyyyy lonngggggggggggg" +
                         " veeeeeerrrryyyyy lonngggggggggggg" +
                         " veeeeeerrrryyyyy lonngggggggggggg" +
                         " veeeeeerrrryyyyy lonngggggggggggg" +
                         " veeeeeerrrryyyyy lonngggggggggggg" +
                         " veeeeeerrrryyyyy lonngggggggggggg" +
                         " veeeeeerrrryyyyy lonngggggggggggg" +
                         " veeeeeerrrryyyyy lonngggggggggggg" +
                         " veeeeeerrrryyyyy lonngggggggggggg" +
                         " veeeeeerrrryyyyy lonngggggggggggg" +
                         " veeeeeerrrryyyyy lonngggggggggggg" +
                         " veeeeeerrrryyyyy lonngggggggggggg" +
                         " veeeeeerrrryyyyy lonngggggggggggg" +
                         " veeeeeerrrryyyyy lonngggggggggggg" +
                         " veeeeeerrrryyyyy lonngggggggggggg" +
                         " veeeeeerrrryyyyy lonngggggggggggg" +
                         " veeeeeerrrryyyyy lonngggggggggggg" +
                         " veeeeeerrrryyyyy lonngggggggggggg" +
                         " veeeeeerrrryyyyy lonngggggggggggg" +
                         " veeeeeerrrryyyyy lonngggggggggggg" +
                         " veeeeeerrrryyyyy lonngggggggggggg" +
                         " veeeeeerrrryyyyy lonngggggggggggg" +
                         " veeeeeerrrryyyyy lonngggggggggggg" +
                         " veeeeeerrrryyyyy lonngggggggggggg" +
                         " veeeeeerrrryyyyy lonngggggggggggg" +
                         " veeeeeerrrryyyyy lonngggggggggggg" +
                         " veeeeeerrrryyyyy lonngggggggggggg" +
                         " veeeeeerrrryyyyy lonngggggggggggg" +
                         " veeeeeerrrryyyyy lonngggggggggggg" +
                         " veeeeeerrrryyyyy lonngggggggggggg" +
                         " veeeeeerrrryyyyy lonngggggggggggg" +
                         " veeeeeerrrryyyyy lonngggggggggggg" +
                         " veeeeeerrrryyyyy lonngggggggggggg" +
                         " veeeeeerrrryyyyy lonngggggggggggg" +
                         " veeeeeerrrryyyyy lonngggggggggggg" +
                         " veeeeeerrrryyyyy lonngggggggggggg" +
                         " veeeeeerrrryyyyy lonngggggggggggg" +
                         " veeeeeerrrryyyyy lonngggggggggggg" +
                         " veeeeeerrrryyyyy lonngggggggggggg" +
                         " veeeeeerrrryyyyy lonngggggggggggg" +
                         " veeeeeerrrryyyyy lonngggggggggggg" +
                         " veeeeeerrrryyyyy lonngggggggggggg" +
                         " veeeeeerrrryyyyy lonngggggggggggg" +
                         " veeeeeerrrryyyyy lonngggggggggggg" +
                         " veeeeeerrrryyyyy lonngggggggggggg" +
                         " veeeeeerrrryyyyy lonngggggggggggg" +
                         " veeeeeerrrryyyyy lonngggggggggggg" +
                         "eeerrrryyyyy lonngggggggggggg" +
                         " veeeeeerrrryyyyy lonngggggggggggg")

        self.assert_text("Type: Fridge")
        self.assert_text("Title: Yes1")
        self.assert_text("Price: 999.0")

        # check lower boundary of 20
        self.click('button[id="form_button"]')
        self.type("#title", "Yes")
        self.type("#description", "NeBetter Title 2 New")
        self.type("#id", "4")
        self.click('button[type="submit"]')
        self.assert_text("Update Successful")
        self.assert_text("ID: 4")
        self.assert_text("Description: NeBetter Title 2 New")
        self.assert_text("Type: Fridge")
        self.assert_text("Title: Yes")
        self.assert_text("Price: 999.0")

        # end test 2.2

        # begin test 2.3
        # test limit of type

        # check lower boundary of 1
        self.click('button[id="form_button"]')
        self.type("#type", "A")
        self.type("#id", "4")
        self.click('button[type="submit"]')
        self.assert_text("Update Successful")
        self.assert_text("ID: 4")
        self.assert_text("Description: NeBetter Title 2 New")
        self.assert_text("Type: A")
        self.assert_text("Title: Yes")
        self.assert_text("Price: 999.0")

        # check higher boundary
        self.click('button[id="form_button"]')
        self.type("#type", "a very big object 10")
        self.type("#id", "4")
        self.click('button[type="submit"]')
        self.assert_text("Update Successful")
        self.assert_text("ID: 4")
        self.assert_text("Description: NeBetter Title 2 New")
        self.assert_text("Type: a very big object 10")
        self.assert_text("Title: Yes")
        self.assert_text("Price: 999.0")
        # end test 2.3

        # begin test 2.4
        # test limit of price
        # create new object with lower price
        self.open(base_url + '/create_product')
        self.type("#date", "10-12-2021")
        self.type("#description", "This is an AWESOME object WOOP WOOP")
        self.type("#price", "10")
        self.type("#title", "object lower price")
        # click enter button
        self.click('button[type="submit"]')
        self.open(base_url + '/products')

        # check if price can be set to lower boundary of 10
        self.click('button[id="form_button"]')
        self.type("#id", "5")
        self.type("#price", "10")
        self.click('button[type="submit"]')
        self.assert_text("Update Successful")
        self.assert_text("ID: 5")
        self.assert_text("Description: This is an AWESOME object WOOP WOOP")
        self.assert_text("Type: None")
        self.assert_text("Title: object lower price")
        self.assert_text("Price: 10.0")

        # check if price can be set to higher boundary of 10000
        self.click('button[id="form_button"]')
        self.type("#id", "5")
        self.type("#price", "10000")
        self.click('button[type="submit"]')
        self.assert_text("Update Successful")
        self.assert_text("ID: 5")
        self.assert_text("Description: This is an AWESOME object WOOP WOOP")
        self.assert_text("Type: None")
        self.assert_text("Title: object lower price")
        self.assert_text("Price: 10000.0")
        # end test 2.4

        # end Test Method #2

        # Test Method #3 : Output Testing
        # begin test 3.1
        # output successful case
        self.click('button[id="form_button"]')
        self.type("#id", "4")
        self.type("#price", "1000")
        self.type("#title", "New Better Title 3")
        self.type("#description", "This is the first update of "
                                  "this method")
        self.type("#type", "Oversized")
        self.click('button[type="submit"]')

        # check if update was a success
        self.assert_text("Update Successful")
        self.assert_text("ID: 4")
        self.assert_text("Description: This is the first update of "
                         "this method")
        self.assert_text("Type: Oversized")
        self.assert_text("Title: New Better Title 3")
        self.assert_text("Price: 1000.0")
        # end test 3.1

        # begin test 3.2
        # output incorrect case
        self.click('button[id="form_button"]')
        self.type("#id", "4")
        self.type("#price", "100")
        self.type("#title", "New Better Title 3!")
        self.type("#description", "1")
        self.type("#type", "Oversized!")
        self.click('button[type="submit"]')

        # check if update was a success
        self.assert_text("This title is wrong The type is wrong "
                         "The price is wrong The description is wrong")
        self.assert_text("ID: 4")
        self.assert_text("Description: This is the first update of "
                         "this method")
        self.assert_text("Type: Oversized")
        self.assert_text("Title: New Better Title 3")
        self.assert_text("Price: 1000.0")
        # end test 3.2

        # begin test 3.3
        # output incorrect ID
        self.click('button[id="form_button"]')
        self.type("#id", "")
        self.click('button[type="submit"]')

        # check if update was a success
        self.assert_text("INVALID ID")
        self.assert_text("ID: 4")
        self.assert_text("Description: This is the first update of "
                         "this method")
        self.assert_text("Type: Oversized")
        self.assert_text("Title: New Better Title 3")
        self.assert_text("Price: 1000.0")
        # end test 3.3

        # begin test 3.4
        # output incorrect title
        self.click('button[id="form_button"]')
        self.type("#id", "4")
        self.type("#title", "New Better Title 3!")
        self.click('button[type="submit"]')

        # check if update was a success
        self.assert_text("The title is not valid")
        self.assert_text("ID: 4")
        self.assert_text("Description: This is the first update of "
                         "this method")
        self.assert_text("Type: Oversized")
        self.assert_text("Title: New Better Title 3")
        self.assert_text("Price: 1000.0")
        # end test 3.4

        # begin test 3.5
        # output incorrect description
        self.click('button[id="form_button"]')
        self.type("#id", "4")
        self.type("#description", "1")
        self.click('button[type="submit"]')

        # check if update was a success
        self.assert_text("The description is not valid")
        self.assert_text("ID: 4")
        self.assert_text("Description: This is the first update of "
                         "this method")
        self.assert_text("Type: Oversized")
        self.assert_text("Title: New Better Title 3")
        self.assert_text("Price: 1000.0")
        # end test 3.5

        # begin test 3.6
        # output incorrect type
        self.click('button[id="form_button"]')
        self.type("#id", "4")
        self.type("#type", "Oversized!")
        self.click('button[type="submit"]')

        # check if update was a success
        self.assert_text("The type is not valid")
        self.assert_text("ID: 4")
        self.assert_text("Description: This is the first update of "
                         "this method")
        self.assert_text("Type: Oversized")
        self.assert_text("Title: New Better Title 3")
        self.assert_text("Price: 1000.0")
        # end test 3.6

        # begin test 3.7
        # output incorrect price
        self.click('button[id="form_button"]')
        self.type("#id", "4")
        self.type("#price", "10")
        self.click('button[type="submit"]')

        # check if update was a success
        self.assert_text("The price can't be lower than before")
        self.assert_text("ID: 4")
        self.assert_text("Description: This is the first update of "
                         "this method")
        self.assert_text("Type: Oversized")
        self.assert_text("Title: New Better Title 3")
        self.assert_text("Price: 1000.0")
        # end test 3.7
        # end Test Method #3