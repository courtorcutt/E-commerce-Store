from seleniumbase import BaseCase

from qbay_test.conftest import base_url


"""
This file contains the test for buying products (frontend)
Three black box testing methods will be used:
   - Functionality Testing
   - Input Partitioning Testing
   - Output Partitioning Testing
"""


class FrontEndBuyProductTesting(BaseCase):

    def test_buy_products_functionality(self, *_):
        # FUNCTIONALITY TESTING
        # testing if a user can place an order on products

        # register a user to be the seller
        self.open(base_url + '/register')
        self.type("#first_name", "Santa")
        self.type("#last_name", "Snow")
        self.type("#email", "santasnow@gmail.ca")
        self.type("#user_name", "NorthPoleLocal")
        self.type("#password1", "S@ntaL0vesGifts!")
        self.type("#password2", "S@ntaL0vesGifts!")

        self.click("#sign-up")
        self.assert_no_js_errors()

        # logout from profile
        self.click('a[id="logout-link"]')

        # register a second user to be the buyer
        self.open(base_url + '/register')
        self.type("#first_name", "Elf")
        self.type("#last_name", "Helper")
        self.type("#email", "presentsrule@gmail.ca")
        self.type("#user_name", "SantasHelper")
        self.type("#password1", "IL0veGiftsM0re!")
        self.type("#password2", "IL0veGiftsM0re!")

        self.click("#sign-up")
        self.assert_no_js_errors()

        # logout from profile
        self.click('a[id="logout-link"]')

        # Launch create products page but redirect to login
        self.open(base_url + '/create_product')

        # login with existing user
        self.type("#email", "santasnow@gmail.ca")
        self.type("#password", "S@ntaL0vesGifts!")

        # click enter button
        self.click('button[type="submit"]')

        # create some products
        self.open(base_url + '/create_product')
        self.type("#title", "Bicycle")
        self.type("#price", "70")
        self.type("#description", "What child doesn't want "
                                  "a bicycle as a present?")
        self.type("#date", "04-12-2021")
        self.click('button[type="submit"]')
        self.assert_no_js_errors()

        # Check to see if the bicycle product has been created
        self.open(base_url + '/products')
        self.assert_text("Here are all of your products Santa")
        self.assert_text("ID: 17")
        self.assert_text("Title: Bicycle")
        self.assert_text("Description: What child doesn't want "
                         "a bicycle as a present?")
        self.assert_text("Type: None")
        self.assert_text("Price: 70.0")
        self.assert_text("Buyer: None")

        # create a second product
        self.open(base_url + '/create_product')
        self.type("#title", "Dollhouse")
        self.type("#price", "200")
        self.type("#description", "Perfect opportunity "
                                  "to increase your imagination.")
        self.type("#date", "12-4-2021")
        self.click('button[type="submit"]')
        self.assert_no_js_errors()

        # Check to see if the dollhouse object has been created
        self.open(base_url + '/products')
        self.assert_text("Here are all of your products Santa")
        self.assert_text("ID: 18")
        self.assert_text("Title: Dollhouse")
        self.assert_text("Description: Perfect opportunity "
                         "to increase your imagination.")
        self.assert_text("Type: None")
        self.assert_text("Price: 200.0")
        self.assert_text("Buyer: None")

        # FUNCTIONALITY TESTING
        # USER (SANTA) CAN'T PLACE AN ORDER ON HIS OWN PRODUCTS
        self.open(base_url + '/buy_product')
        self.assert_text_not_visible("ID: 17")
        self.assert_text_not_visible("ID: 18")

        # navigate to profile and log out as the seller
        self.open(base_url + '/profile')
        self.click('a[id="logout-link"]')

        # navigate to the buy product page and login
        # as the buyer
        self.open(base_url + '/buy_product')
        self.type("#email", "presentsrule@gmail.ca")
        self.type("#password", "IL0veGiftsM0re!")
        self.click('button[type="submit"]')

        # update the shipping address and postal code
        # so that the elves can package them up for santa
        self.open(base_url + '/profile')
        self.click('a[id="update-profile-link"]')
        self.type("#shipping_address", "1 North Pole Dr")
        self.type("#postal_code", "K7L 1Z1")
        self.click("#update-button")

        # now navigate to the products page and the
        # products from other sellers should be listed
        self.open(base_url + '/buy_product')

        # click on the form_button
        self.click("#form_button")

        # FUNCTIONALITY TESTING
        # A USER CAN PLACE AN ORDER ON THE PRODUCTS
        self.type("#id", "17")
        self.click('button[type="submit"]')
        self.assert_no_js_errors()
        self.assert_text("You bought product 17")

        # FUNCTIONALITY TESTING
        # A sold product will not be shown on the
        # buyers user's user interface.
        self.open(base_url + '/buy_product')
        self.assert_text_not_visible("ID: 17")
        self.assert_text_not_visible("Title: Bicycle")
        self.assert_no_js_errors()

        # FUNCTIONALITY TESTING
        # A USER CAN'T BUY AN ITEM HIGHER THAN THEIR BALANCE
        self.open(base_url + '/buy_product')
        # click on the form_button
        self.click("#form_button")
        # choose the expensive item
        self.type("#id", "18")
        self.click('button[type="submit"]')
        self.assert_no_js_errors()
        assert (not self.assert_no_js_errors())
        self.assert_text("Balance too low")

        # navigate to profile and log out as the buyer
        self.open(base_url + '/profile')
        self.click('a[id="logout-link"]')

        # Launch create products page but redirect to login
        self.open(base_url + '/products')

        # login with existing user
        self.type("#email", "santasnow@gmail.ca")
        self.type("#password", "S@ntaL0vesGifts!")
        self.click('button[type="submit"]')

        # launch the page again
        self.open(base_url + '/products')

        # FUNTIONALITY TESTING
        # A sold product is shown in owner's user interface.
        # assert that the buyer is the elf
        # Check to see if the bicycle product has been created
        self.assert_text("Here are all of your products Santa")
        self.assert_text("ID: 17")
        self.assert_text("Title: Bicycle")
        self.assert_text("Description: What child doesn't want "
                         "a bicycle as a present?")
        self.assert_text("Type: None")
        self.assert_text("Price: 70.0")
        self.assert_text("Buyer: presentsrule@gmail.ca")
        self.assert_no_js_errors()

        # NEXT BLACK-BOX TESTING METHOD
        # testing if a user can place an order...
        # valid order placing - (buyer, enough $)
        # invalid order placing - (seller, not enough $)

        # first Santa will create some more products
        self.open(base_url + '/create_product')
        self.type("#title", "Book")
        self.type("#price", "25")
        self.type("#description", "This is a nighttime story before bed.")
        self.type("#date", "04-12-2021")
        self.click('button[type="submit"]')
        self.assert_no_js_errors()

        self.open(base_url + '/create_product')
        self.type("#title", "Coal")
        self.type("#price", "10")
        self.type("#description", "This is rarely ever bought.")
        self.type("#date", "04-12-2021")
        self.click('button[type="submit"]')
        self.assert_no_js_errors()

        self.open(base_url + '/create_product')
        self.type("#title", "Candy")
        self.type("#price", "50")
        self.type("#description", "For those with a sweet tooth.")
        self.type("#date", "04-12-2021")
        self.click('button[type="submit"]')
        self.assert_no_js_errors()

        # INPUT PARTITION - test for being a buyer
        self.open(base_url + '/buy_product')
        self.assert_text_not_visible("ID: 17")
        self.assert_text_not_visible("Title: Bicycle")
        self.assert_text_not_visible("ID: 18")
        self.assert_text_not_visible("Title: Dollhouse")
        self.assert_text_not_visible("ID: 19")
        self.assert_text_not_visible("Title: Book")
        self.assert_text_not_visible("ID: 20")
        self.assert_text_not_visible("Title: Coal")
        self.assert_text_not_visible("ID: 21")
        self.assert_text_not_visible("Title: Candy")

        # so Santa will log out
        self.open(base_url + '/profile')
        self.click('a[id="logout-link"]')

        # and the elf will log in
        self.open(base_url + '/buy_product')
        self.type("#email", "presentsrule@gmail.ca")
        self.type("#password", "IL0veGiftsM0re!")
        self.click('button[type="submit"]')

        # the elf will navigate to buy products
        self.open(base_url + '/buy_product')

        # INPUT PARTITION - test for being a buyer
        self.assert_text("Products for Sale")
        self.assert_text("ID: 18")
        self.assert_text("Title: Dollhouse")
        self.assert_text("ID: 19")
        self.assert_text(("Title: Book"))
        self.assert_text("ID: 20")
        self.assert_text("Title: Coal")
        self.assert_text("ID: 21")
        self.assert_text("Title: Candy")
        self.assert_no_js_errors()

        # click on the form_button
        self.click("#form_button")

        self.type("#id", "19")
        self.click('button[type="submit"]')
        self.assert_no_js_errors()
        self.assert_text("You bought product 19")

        # INPUT PARTITION - test for being a buyer
        self.open(base_url + '/buy_product')

        # click on the form_button
        self.click("#form_button")

        self.type("#id", "20")
        self.click('button[type="submit"]')
        self.assert_no_js_errors()
        self.assert_text("You bought product 20")

        self.open(base_url + '/create_product')
        self.type("#title", "Sleigh")
        self.type("#price", "1000")
        self.type("#description", "All the reindeer are excited.")
        self.type("#date", "04-12-2021")
        self.click('button[type="submit"]')

        # INPUT PARTITION - test for being a buyer
        self.open(base_url + '/buy_product')
        # click on the form_button
        self.click("#form_button")

        # not buyer so can't purchase product
        self.type("#id", "22")
        self.click('button[type="submit"]')
        assert (not self.assert_no_js_errors())
        self.assert_text_not_visible("ID: 22")

        # INPUT PARTITION - enough $
        # click on the form_button
        self.click("#form_button")

        self.type("#id", "18")
        self.click('button[type="submit"]')
        assert (not self.assert_no_js_errors())
        self.assert_text("Balance too low")

        # INPUT PARTITION - enough $
        # click on the form_button
        self.click("#form_button")

        self.type("#id", "21")
        self.click('button[type="submit"]')
        self.assert_no_js_errors()
        self.assert_text("You bought product 21")

        # NEXT BLACK-BOX TESTING METHOD
        # OUTPUT PARTITIONING
        # successful purchase - (not visible for buyer
        # but will be visible for seller)
        # unsuccessful purchase - (still visible for buyer,
        # still visible for seller as unpurchased)

        # OUTPUT PARTITIONING - successful visible for buyer (the elf)
        self.assert_text("Here are all the products you bought")
        self.assert_text("ID: 17")
        self.assert_text("Title: Bicycle")
        self.assert_text("Description: What child doesn't want "
                         "a bicycle as a present?")
        self.assert_text("Type: None")
        self.assert_text("Price: 70.0")

        self.assert_text("ID: 19")
        self.assert_text("Title: Book")
        self.assert_text("Description: This is a nighttime "
                         "story before bed.")
        self.assert_text("Type: None")
        self.assert_text("Price: 25.0")

        # OUTPUT PARTITIONING - unsuccessful purchase visible
        # for seller as unpurchased (the elf)
        # self.assert_text("ID: 22")
        self.assert_text("Title: Sleigh")
        self.assert_text("Description: All the reindeer are excited.")
        self.assert_text("Type: None")
        self.assert_text("Price: 1000.0")
        self.assert_text("Buyer: None")

        # OUTPUT PARTITIONING - visible for buyer (the elf)
        # navigate to profile and log out as the buyer
        self.open(base_url + '/profile')
        self.click('a[id="logout-link"]')

        # Launch create products page but redirect to login
        self.open(base_url + '/products')

        # login with existing user
        self.type("#email", "santasnow@gmail.ca")
        self.type("#password", "S@ntaL0vesGifts!")
        self.click('button[type="submit"]')

        self.open(base_url + '/products')

        # OUTPUT PARTITION - successful purchase visible to seller
        self.assert_text("Here are all of your products Santa")
        self.assert_text("ID: 17")
        self.assert_text("Title: Bicycle")
        self.assert_text("Description: What child doesn't want "
                         "a bicycle as a present?")
        self.assert_text("Type: None")
        self.assert_text("Price: 70.0")
        self.assert_text("Sold: True")
        self.assert_text("Buyer: presentsrule@gmail.ca")

        self.assert_text("ID: 19")
        self.assert_text("Title: Book")
        self.assert_text("Description: This is a nighttime story "
                         "before bed.")
        self.assert_text("Type: None")
        self.assert_text("Price: 25.0")
        self.assert_text("Sold: True")
        self.assert_text("Buyer: presentsrule@gmail.ca")

        self.assert_text("ID: 20")
        self.assert_text("Title: Coal")
        self.assert_text("Description: This is rarely ever bought.")
        self.assert_text("Type: None")
        self.assert_text("Price: 10.0")
        self.assert_text("Sold: True")
        self.assert_text("Buyer: presentsrule@gmail.ca")

        # self.assert_text("ID: 21")
        self.assert_text("Title: Candy")
        self.assert_text("Description: For those with a sweet tooth.")
        self.assert_text("Type: None")
        self.assert_text("Price: 50.0")
        self.assert_text("Sold: True")
        self.assert_text("Buyer: presentsrule@gmail.ca")

        # OUTPUT PARTITIONING - unsuccessful purchase visible for
        # seller as unpurchased (santa)
        self.assert_text("ID: 18")
        self.assert_text("Title: Dollhouse")
        self.assert_text("Description: Perfect opportunity to increase "
                         "your imagination.")
        self.assert_text("Type: None")
        self.assert_text("Price: 200.0")
        self.assert_text("Sold: False")
        self.assert_text("Buyer: None")