from seleniumbase import BaseCase
from qbay_test.conftest import base_url
from unittest.mock import patch
from selenium import webdriver
from qbay.models import User

# This code utilizes three different BB testing methods
# for the product creation element of the frontend development.
# Specifically, we are focusing on:
# 1. Hybrid input partitioning & shotgun
# 2. Output partitioning
# 3. Boundary testing


class FrontEndProductCreateTest(BaseCase):

    # We make a "testing" registered user to use in our BB testing
    # "Testing" is in quotations since it's technically an object
    # However, a user must be created to then navigate towards creating
    # product page

    def test_R4_5_6_7_price_date_email(self, *_):

        self.open(base_url + '/register')
        # Register user with following information
        self.type("#email", "BruceWayne@gmail.com")
        self.type("#password1", "B@tman23!")
        self.type("#password2", "B@tman23!")
        self.type("#balance", "198")
        self.type("#first_name", "Brandon")
        self.type("#last_name", "Lachhman")
        self.type("#postal_code", "K9K 1Y8")
        # Yes this is where Boris lives!
        self.type("#shipping_address", "10 Downing St")
        self.type("#user_name", "BPlachh")
        self.click('button[type="submit"]')
        # Logout having set up an account
        self.open(base_url + '/logout')
        # Launch create products page but redirect to login
        self.open(base_url + '/create_product')
        # Log in with existing user
        self.type("#email", "BruceWayne@gmail.com")
        self.type("#password", "B@tman23!")
        self.click('button[type="submit"]')

        # We're signed up, information updated, and now we need
        # to test CREATING a product

        # 1. Begin Hybrid input partitioning & shotgun
        # Note that the following partitions will be denoted PN &
        # PN.M, where N is the Nth partition, and M is the Mth shotgun
        # subpartition in the Nth partition

        # P1 Focuses on price input

        # P1.1 Prices below 10 (incorrect)
        self.open(base_url + '/create_product')
        self.type("#title", "OBJECT1")
        self.type("#price", "-5")
        self.type("#description", "DESCRIPTION OF OBJECT1")
        self.type("#date", "11-6-2021")
        self.click('button[type="submit"]')

        self.type("#title", "OBJECT1")
        self.type("#price", "2")
        self.type("#description", "DESCRIPTION OF OBJECT1")
        self.type("#date", "11-6-2021")
        self.click('button[type="submit"]')

        self.type("#title", "OBJECT1")
        self.type("#price", "7")
        self.type("#description", "DESCRIPTION OF OBJECT1")
        self.type("#date", "11-6-2021")
        self.click('button[type="submit"]')

        # P1.2 Prices above 10 000 (incorrect)
        self.type("#title", "OBJECT1")
        self.type("#price", "12245")
        self.type("#description", "DESCRIPTION OF OBJECT1")
        self.type("#date", "11-6-2021")
        self.click('button[type="submit"]')

        self.type("#title", "OBJECT1")
        self.type("#price", "19467")
        self.type("#description", "DESCRIPTION OF OBJECT1")
        self.type("#date", "11-6-2021")
        self.click('button[type="submit"]')

        self.type("#title", "OBJECT1")
        self.type("#price", "10246")
        self.type("#description", "DESCRIPTION OF OBJECT1")
        self.type("#date", "11-6-2021")
        self.click('button[type="submit"]')

        # P1.3 Prices between 10 & 10 000 (correct)
        self.type("#title", "OBJECT1")
        self.type("#price", "60")
        self.type("#description", "DESCRIPTION OF OBJECT1")
        self.type("#date", "11-6-2021")
        self.click('button[type="submit"]')

        # Check to see if OBJECT1 has been made (assert success message
        # and check fields on product page)
        self.assert_text("You have successfully created a " +
                         "new product!")
        self.open(base_url + '/products')
        self.assert_text("Here are all of your products Brandon")
        # self.assert_text("ID: 2")
        self.assert_text("Title: OBJECT1")
        self.assert_text("Description: DESCRIPTION OF OBJECT1")
        self.assert_text("Type: None")
        self.assert_text("Price: 60.0")

        self.open(base_url + '/create_product')
        self.type("#title", "OBJECT2")
        self.type("#price", "787")
        self.type("#description", "DESCRIPTION OF OBJECT2")
        self.type("#date", "11-6-2021")
        self.click('button[type="submit"]')

        # Check to see if OBJECT2 has been made (assert success message
        # and check fields on product page)
        self.assert_text("You have successfully created a " +
                         "new product!")
        self.open(base_url + '/products')
        self.assert_text("Here are all of your products Brandon")
        # self.assert_text("ID: 3")
        self.assert_text("Title: OBJECT2")
        self.assert_text("Description: DESCRIPTION OF OBJECT2")
        self.assert_text("Type: None")
        self.assert_text("Price: 787.0")

        self.open(base_url + '/create_product')
        self.type("#title", "OBJECT3")
        # Halloween spirit... ( •̀ᴗ•́ )
        self.type("#price", "666")
        self.type("#description", "DESCRIPTION OF OBJECT3")
        self.type("#date", "11-6-2021")
        self.click('button[type="submit"]')

        # Check to see if OBJECT3 has been made (assert success message
        # and check fields on product page)
        self.assert_text("You have successfully created a " +
                         "new product!")
        self.open(base_url + '/products')
        self.assert_text("Here are all of your products Brandon")
        # self.assert_text("ID: 4")
        self.assert_text("Title: OBJECT3")
        self.assert_text("Description: DESCRIPTION OF OBJECT3")
        self.assert_text("Type: None")
        self.assert_text("Price: 666.0")

        # P2 focuses on date input

        # P2.1 Dates before Jan. 2nd, 2021 (incorrect)
        self.open(base_url + '/create_product')
        self.type("#title", "OBJECT4")
        self.type("#price", "50")
        self.type("#description", "DESCRIPTION OF OBJECT4")
        self.type("#date", "10-3-2019")
        self.click('button[type="submit"]')

        self.type("#title", "OBJECT4")
        self.type("#price", "50")
        self.type("#description", "DESCRIPTION OF OBJECT4")
        self.type("#date", "8-7-2019")
        self.click('button[type="submit"]')

        self.type("#title", "OBJECT4")
        self.type("#price", "50")
        self.type("#description", "DESCRIPTION OF OBJECT4")
        self.type("#date", "6-6-2016")
        self.click('button[type="submit"]')

        # P2.2 Dates after Jan. 2nd, 2025 (incorrect)
        self.type("#title", "OBJECT4")
        self.type("#price", "50")
        self.type("#description", "DESCRIPTION OF OBJECT4")
        self.type("#date", "3-2-2026")
        self.click('button[type="submit"]')

        self.type("#title", "OBJECT4")
        self.type("#price", "50")
        self.type("#description", "DESCRIPTION OF OBJECT4")
        self.type("#date", "9-4-2025")
        self.click('button[type="submit"]')

        self.type("#title", "OBJECT4")
        self.type("#price", "50")
        self.type("#description", "DESCRIPTION OF OBJECT4")
        self.type("#date", "1-1-2057")
        self.click('button[type="submit"]')

        # P2.3 Dates between Jan. 2nd, 2021 & Jan. 2nd, 2025 (correct)
        self.type("#title", "OBJECT4")
        self.type("#price", "50")
        self.type("#description", "DESCRIPTION OF OBJECT4")
        self.type("#date", "5-7-2021")
        self.click('button[type="submit"]')

        # Check to see if OBJECT4 has been made (assert success message
        # and check fields on product page)
        self.assert_text("You have successfully created a " +
                         "new product!")
        self.open(base_url + '/products')
        self.assert_text("Here are all of your products Brandon")
        # self.assert_text("ID: 5")
        self.assert_text("Title: OBJECT4")
        self.assert_text("Description: DESCRIPTION OF OBJECT4")
        self.assert_text("Type: None")
        self.assert_text("Price: 50.0")

        self.open(base_url + '/create_product')
        self.type("#title", "OBJECT5")
        self.type("#price", "50")
        self.type("#description", "DESCRIPTION OF OBJECT5")
        self.type("#date", "9-4-2024")
        self.click('button[type="submit"]')

        # Check to see if OBJECT5 has been made (assert success message
        # and check fields on product page)
        self.assert_text("You have successfully created a " +
                         "new product!")
        self.open(base_url + '/products')
        self.assert_text("Here are all of your products Brandon")
        # self.assert_text("ID: 6")
        self.assert_text("Title: OBJECT5")
        self.assert_text("Description: DESCRIPTION OF OBJECT5")
        self.assert_text("Type: None")
        self.assert_text("Price: 50.0")

        self.open(base_url + '/create_product')
        self.type("#title", "OBJECT6")
        self.type("#price", "50")
        self.type("#description", "DESCRIPTION OF OBJECT6")
        self.type("#date", "1-1-2023")
        self.click('button[type="submit"]')

        # Check to see if OBJECT6 has been made (assert success message
        # and check fields on product page)
        self.assert_text("You have successfully created a " +
                         "new product!")
        self.open(base_url + '/products')
        self.assert_text("Here are all of your products Brandon")
        # self.assert_text("ID: 7")
        self.assert_text("Title: OBJECT6")
        self.assert_text("Description: DESCRIPTION OF OBJECT6")
        self.assert_text("Type: None")
        self.assert_text("Price: 50.0")

        # 2. Begin output partitioning
        # Note that the subsequent outputs for creating a product
        # are SUCCESSFUL & UNSUCCESSFUL. However, for UNSUCCESSFUL, we
        # can check subpartitions based on the "UNSUCCESSFULNESS"
        # (i.e., what is the error msg due to corresponding inputs)

        # P3 Focuses on title input

        # P3.1 Same title name exists
        self.open(base_url + '/create_product')
        self.type("#title", "Johnnie Walker Whiskey")
        self.type("#price", "30")
        self.type("#description", "Light amber colour," +
                  " nutty smell in classic blend")
        self.type("#date", "11-6-2021")
        self.click('button[type="submit"]')

        # Check to see if Johnnie Walker Whiskey has been
        # made (assert success message
        # and check fields on product page)
        self.assert_text("You have successfully created a " +
                         "new product!")
        self.open(base_url + '/products')
        self.assert_text("Here are all of your products Brandon")
        # self.assert_text("ID: 8")
        self.assert_text("Title: Johnnie Walker Whiskey")
        self.assert_text("Description: Light amber colour," +
                         " nutty smell in classic blend")
        self.assert_text("Type: None")
        self.assert_text("Price: 30.0")

        self.open(base_url + '/create_product')
        self.type("#title", "Johnnie Walker Whiskey")
        self.type("#price", "30")
        self.type("#description", "Light amber colour, " +
                  " nutty smell in classic blend")
        self.type("#date", "11-6-2021")
        self.click('button[type="submit"]')

        # P3.2 Title name is not alphanumeric
        self.type("#title", "Absinthe")
        self.type("#price", "70")
        self.type("#description", "Green in colour, classic french blend")
        self.type("#date", "11-6-2021")
        self.click('button[type="submit"]')

        # Check to see if Absinthe has been
        # made (assert success message
        # and check fields on product page)
        self.assert_text("You have successfully created a " +
                         "new product!")
        self.open(base_url + '/products')
        self.assert_text("Here are all of your products Brandon")
        # self.assert_text("ID: 9")
        self.assert_text("Title: Absinthe")
        self.assert_text("Description: Green in colour, classic french blend")
        self.assert_text("Type: None")
        self.assert_text("Price: 70.0")

        self.open(base_url + '/create_product')
        self.type("#title", "@b$inthe")
        self.type("#price", "70")
        self.type("#description", "Green in colour, classic french blend")
        self.type("#date", "11-6-2021")
        self.click('button[type="submit"]')

        # P3.3 Title name is too long
        self.type("#title", "Cecchi Chianti")
        self.type("#price", "15")
        self.type("#description", "This is a lovely dry red wine")
        self.type("#date", "11-6-2021")
        self.click('button[type="submit"]')

        # Check to see if Cecchi Chianti has been
        # made (assert success message
        # and check fields on product page)
        self.assert_text("You have successfully created a " +
                         "new product!")
        self.open(base_url + '/products')
        self.assert_text("Here are all of your products Brandon")
        # self.assert_text("ID: 10")
        self.assert_text("Title: Cecchi Chianti")
        self.assert_text("Description: This is a lovely dry red wine")
        self.assert_text("Type: None")
        self.assert_text("Price: 15.0")

        self.open(base_url + '/create_product')
        self.type("#title", "Cecchi Chianti Red Wine It Is" +
                  "Delicious Probably Better Than Other Red" +
                  "Wines Like Merlot Cabernet Sauvignon And Many Others")
        self.type("#price", "15")
        self.type("#description", "This is a lovely dry red wine")
        self.type("#date", "11-6-2021")
        self.click('button[type="submit"]')

        # 3. Begin Boundary Checks
        # Note that the last element of product creation not tested yet
        # is the decription. Since we are analyzing boundaries, the description
        # length coresponds to the the boundary partitions

        # P4 Focuses on description input

        # P4.1 Description is exactly 20 characters (correct)
        # self.open(base_url + '/create_product')
        self.type("#title", "Baileys")
        self.type("#price", "50")
        self.type("#description", "IrishCremeliqueurYum")
        self.type("#date", "11-6-2021")
        self.click('button[type="submit"]')

        # Check to see if Baileys has been
        # made (assert success message
        # and check fields on product page)
        self.assert_text("You have successfully created a " +
                         "new product!")
        self.open(base_url + '/products')
        self.assert_text("Here are all of your products Brandon")
        # self.assert_text("ID: 11")
        self.assert_text("Title: Baileys")
        self.assert_text("Description: IrishCremeliqueurYum")
        self.assert_text("Type: None")
        self.assert_text("Price: 50.0")

        # P4.2 Description is exactly 2000 characters (correct)
        self.open(base_url + '/create_product')
        self.type("#title", "Moscato White Wine")
        self.type("#price", "15")
        self.type("#description", "WhiteWhiteWhiteWhiteWhiteWhiteWhiteWhite" +
                  "WhiteWhiteWhiteWhiteWhiteWhiteWhiteWhite" +
                  "WhiteWhiteWhiteWhiteWhiteWhiteWhiteWhite" +
                  "WhiteWhiteWhiteWhiteWhiteWhiteWhiteWhite" +
                  "WhiteWhiteWhiteWhiteWhiteWhiteWhiteWhite" +
                  "WhiteWhiteWhiteWhiteWhiteWhiteWhiteWhite" +
                  "WhiteWhiteWhiteWhiteWhiteWhiteWhiteWhite" +
                  "WhiteWhiteWhiteWhiteWhiteWhiteWhiteWhite" +
                  "WhiteWhiteWhiteWhiteWhiteWhiteWhiteWhite" +
                  "WhiteWhiteWhiteWhiteWhiteWhiteWhiteWhite" +
                  "WhiteWhiteWhiteWhiteWhiteWhiteWhiteWhite" +
                  "WhiteWhiteWhiteWhiteWhiteWhiteWhiteWhite" +
                  "WhiteWhiteWhiteWhiteWhiteWhiteWhiteWhite" +
                  "WhiteWhiteWhiteWhiteWhiteWhiteWhiteWhite" +
                  "WhiteWhiteWhiteWhiteWhiteWhiteWhiteWhite" +
                  "WhiteWhiteWhiteWhiteWhiteWhiteWhiteWhite" +
                  "WhiteWhiteWhiteWhiteWhiteWhiteWhiteWhite" +
                  "WhiteWhiteWhiteWhiteWhiteWhiteWhiteWhite" +
                  "WhiteWhiteWhiteWhiteWhiteWhiteWhiteWhite" +
                  "WhiteWhiteWhiteWhiteWhiteWhiteWhiteWhite" +
                  "WhiteWhiteWhiteWhiteWhiteWhiteWhiteWhite" +
                  "WhiteWhiteWhiteWhiteWhiteWhiteWhiteWhite" +
                  "WhiteWhiteWhiteWhiteWhiteWhiteWhiteWhite" +
                  "WhiteWhiteWhiteWhiteWhiteWhiteWhiteWhite" +
                  "WhiteWhiteWhiteWhiteWhiteWhiteWhiteWhite" +
                  "WhiteWhiteWhiteWhiteWhiteWhiteWhiteWhite" +
                  "WhiteWhiteWhiteWhiteWhiteWhiteWhiteWhite" +
                  "WhiteWhiteWhiteWhiteWhiteWhiteWhiteWhite" +
                  "WhiteWhiteWhiteWhiteWhiteWhiteWhiteWhite" +
                  "WhiteWhiteWhiteWhiteWhiteWhiteWhiteWhite" +
                  "WhiteWhiteWhiteWhiteWhiteWhiteWhiteWhite" +
                  "WhiteWhiteWhiteWhiteWhiteWhiteWhiteWhite" +
                  "WhiteWhiteWhiteWhiteWhiteWhiteWhiteWhite" +
                  "WhiteWhiteWhiteWhiteWhiteWhiteWhiteWhite" +
                  "WhiteWhiteWhiteWhiteWhiteWhiteWhiteWhite" +
                  "WhiteWhiteWhiteWhiteWhiteWhiteWhiteWhite" +
                  "WhiteWhiteWhiteWhiteWhiteWhiteWhiteWhite" +
                  "WhiteWhiteWhiteWhiteWhiteWhiteWhiteWhite" +
                  "WhiteWhiteWhiteWhiteWhiteWhiteWhiteWhite" +
                  "WhiteWhiteWhiteWhiteWhiteWhiteWhiteWhite" +
                  "WhiteWhiteWhiteWhiteWhiteWhiteWhiteWhite" +
                  "WhiteWhiteWhiteWhiteWhiteWhiteWhiteWhite" +
                  "WhiteWhiteWhiteWhiteWhiteWhiteWhiteWhite" +
                  "WhiteWhiteWhiteWhiteWhiteWhiteWhiteWhite" +
                  "WhiteWhiteWhiteWhiteWhiteWhiteWhiteWhite" +
                  "WhiteWhiteWhiteWhiteWhiteWhiteWhiteWhite" +
                  "WhiteWhiteWhiteWhiteWhiteWhiteWhiteWhite" +
                  "WhiteWhiteWhiteWhiteWhiteWhiteWhiteWhite" +
                  "WhiteWhiteWhiteWhiteWhiteWhiteWhiteWhite" +
                  "WhiteWhiteWhiteWhiteWhiteWhiteWhiteWhite")
        self.type("#date", "11-6-2021")
        self.click('button[type="submit"]')

        # Check to see if Moscato White Wine has been
        # made (assert success message
        # and check fields on product page)
        self.assert_text("You have successfully created a " +
                         "new product!")
        self.open(base_url + '/products')
        self.assert_text("Here are all of your products Brandon")
        # self.assert_text("ID: 12")
        self.assert_text("Title: Moscato White Wine")
        self.assert_text("Description: WhiteWhiteWhiteWhiteWhiteWhite" +
                         "WhiteWhite" +
                         "WhiteWhiteWhiteWhiteWhiteWhiteWhiteWhite" +
                         "WhiteWhiteWhiteWhiteWhiteWhiteWhiteWhite" +
                         "WhiteWhiteWhiteWhiteWhiteWhiteWhiteWhite" +
                         "WhiteWhiteWhiteWhiteWhiteWhiteWhiteWhite" +
                         "WhiteWhiteWhiteWhiteWhiteWhiteWhiteWhite" +
                         "WhiteWhiteWhiteWhiteWhiteWhiteWhiteWhite" +
                         "WhiteWhiteWhiteWhiteWhiteWhiteWhiteWhite" +
                         "WhiteWhiteWhiteWhiteWhiteWhiteWhiteWhite" +
                         "WhiteWhiteWhiteWhiteWhiteWhiteWhiteWhite" +
                         "WhiteWhiteWhiteWhiteWhiteWhiteWhiteWhite" +
                         "WhiteWhiteWhiteWhiteWhiteWhiteWhiteWhite" +
                         "WhiteWhiteWhiteWhiteWhiteWhiteWhiteWhite" +
                         "WhiteWhiteWhiteWhiteWhiteWhiteWhiteWhite" +
                         "WhiteWhiteWhiteWhiteWhiteWhiteWhiteWhite" +
                         "WhiteWhiteWhiteWhiteWhiteWhiteWhiteWhite" +
                         "WhiteWhiteWhiteWhiteWhiteWhiteWhiteWhite" +
                         "WhiteWhiteWhiteWhiteWhiteWhiteWhiteWhite" +
                         "WhiteWhiteWhiteWhiteWhiteWhiteWhiteWhite" +
                         "WhiteWhiteWhiteWhiteWhiteWhiteWhiteWhite" +
                         "WhiteWhiteWhiteWhiteWhiteWhiteWhiteWhite" +
                         "WhiteWhiteWhiteWhiteWhiteWhiteWhiteWhite" +
                         "WhiteWhiteWhiteWhiteWhiteWhiteWhiteWhite" +
                         "WhiteWhiteWhiteWhiteWhiteWhiteWhiteWhite" +
                         "WhiteWhiteWhiteWhiteWhiteWhiteWhiteWhite" +
                         "WhiteWhiteWhiteWhiteWhiteWhiteWhiteWhite" +
                         "WhiteWhiteWhiteWhiteWhiteWhiteWhiteWhite" +
                         "WhiteWhiteWhiteWhiteWhiteWhiteWhiteWhite" +
                         "WhiteWhiteWhiteWhiteWhiteWhiteWhiteWhite" +
                         "WhiteWhiteWhiteWhiteWhiteWhiteWhiteWhite" +
                         "WhiteWhiteWhiteWhiteWhiteWhiteWhiteWhite" +
                         "WhiteWhiteWhiteWhiteWhiteWhiteWhiteWhite" +
                         "WhiteWhiteWhiteWhiteWhiteWhiteWhiteWhite" +
                         "WhiteWhiteWhiteWhiteWhiteWhiteWhiteWhite" +
                         "WhiteWhiteWhiteWhiteWhiteWhiteWhiteWhite" +
                         "WhiteWhiteWhiteWhiteWhiteWhiteWhiteWhite" +
                         "WhiteWhiteWhiteWhiteWhiteWhiteWhiteWhite" +
                         "WhiteWhiteWhiteWhiteWhiteWhiteWhiteWhite" +
                         "WhiteWhiteWhiteWhiteWhiteWhiteWhiteWhite" +
                         "WhiteWhiteWhiteWhiteWhiteWhiteWhiteWhite" +
                         "WhiteWhiteWhiteWhiteWhiteWhiteWhiteWhite" +
                         "WhiteWhiteWhiteWhiteWhiteWhiteWhiteWhite" +
                         "WhiteWhiteWhiteWhiteWhiteWhiteWhiteWhite" +
                         "WhiteWhiteWhiteWhiteWhiteWhiteWhiteWhite" +
                         "WhiteWhiteWhiteWhiteWhiteWhiteWhiteWhite" +
                         "WhiteWhiteWhiteWhiteWhiteWhiteWhiteWhite" +
                         "WhiteWhiteWhiteWhiteWhiteWhiteWhiteWhite" +
                         "WhiteWhiteWhiteWhiteWhiteWhiteWhiteWhite" +
                         "WhiteWhiteWhiteWhiteWhiteWhiteWhiteWhite" +
                         "WhiteWhiteWhiteWhiteWhiteWhiteWhiteWhite")
        self.assert_text("Type: None")
        self.assert_text("Price: 15.0")

        # P4.3 Description is exactly same
        # amount of characters as title (incorrect)
        self.open(base_url + '/create_product')
        self.type("#title", "SilverTequila")
        self.type("#price", "30")
        self.type("#description", "100%DeAgaveTQ")
        self.type("#date", "11-6-2021")
        self.click('button[type="submit"]')