from seleniumbase import BaseCase

from qbay_test.conftest import base_url
from unittest.mock import patch
from qbay.models import User
from selenium import webdriver


class FrontEndUserUpdateTest(BaseCase):

    # the following four test functions use three blacbox testing methods:
    # - functionality testing
    # - input partitioning
    # - output partitioning

    def test_R3_1_user_update_success(self, *_):

        # FUNCTIONALITY TESTING
        # testing for functionality as described "A user is only able to update
        # his/her user name, shipping_address, and postal_code."

        # open register page
        self.open(base_url + '/register')

        # register a new user
        self.type("#first_name", "Nathan")
        self.type("#last_name", "Kowal")
        self.type("#email", "nathankowal@yahoo.ca")
        self.type("#user_name", "nathank77")
        self.type("#password1", "TestPassword47!")
        self.type("#password2", "TestPassword47!")

        self.click("#sign-up")

        # navigates to update profile page
        self.click('a[id="update-profile-link"]')

        # check that elements are there
        self.assert_element("#update-profile-heading")
        self.assert_text("UPDATE", "#update-profile-heading")

        # update user
        self.type("#user_name", "bobMcBob")
        self.type("#shipping_address", "123 anywhere st")
        self.type("#postal_code", "M2A 5L8")

        self.click("#update-button")

        # check if update worked
        self.assert_element("#user_name")
        self.assert_text("bobMcBob", "#user_name")

        self.assert_element("#shipping_address")
        self.assert_text("123 anywhere st", "#shipping_address")

        self.assert_element("#postal_code")
        self.assert_text("M2A 5L8", "#postal_code")

    def test_R3_2_shipping_address_fe(self, *_):

        # INPUT PARTITIONING
        # this test case is for the shipping address requirement
        # inputs are partitioned as follows:
        # - valid shipping address (alphanumeric only,
        #                           no special characters, non-empty)
        # - invalid shipping address (special characters)
        # - invalid shipping address (empty)

        # open login page
        self.open(base_url + '/login')

        # log in so that authenticate is passed and user can be updated
        self.type("#email", "nathankowal@yahoo.ca")
        self.type("#password", "TestPassword47!")

        self.click("#login-button")

        # valid shipping address
        self.click('a[id="update-profile-link"]')
        self.type("#shipping_address", "123 anywhere")
        self.click("#update-button")
        self.assert_no_js_errors()

        # non alphanumeric characters
        self.click('a[id="update-profile-link"]')
        self.type("#shipping_address", "123 anywhere!!")
        self.click("#update-button")

        assert(not self.assert_no_js_errors())

        # empty shipping address
        self.click('a[id="update-profile-link"]')
        self.type("#shipping_address", "")
        self.click("#update-button")

        assert(not self.assert_no_js_errors())

    def test_R3_3_postal_code_fe(self, *_):
        # OUTPUT PARTITIONING
        # this test case is for the shipping address requirement
        # outputs are partitioned as follows:
        # - successful update of postal code (caused
        #                                       by valid Canadian postal code)
        # - unsuccessful update of postal code (caused by invalid postal code)

        # open login page
        self.open(base_url + '/login')

        # log in so that authenticate is passed and user can be updated
        self.type("#email", "nathankowal@yahoo.ca")
        self.type("#password", "TestPassword47!")

        self.click("#login-button")

        # successful output
        self.click('a[id="update-profile-link"]')
        self.type("#postal_code", "M6C 2H4")
        self.click("#update-button")
        self.assert_no_js_errors()

        # unsuccessful output
        self.click('a[id="update-profile-link"]')
        self.type("#postal_code", "Z4H 8T7")
        self.click("#update-button")

        assert(not self.assert_no_js_errors())

    def test_R3_4_user_name_fe(self, *_):

        # INPUT PARTITIONING
        # this test case is for the username requirement
        # inputs are partitioned as follows:
        # - valid username (non-empty, alphanumeric-only,
        #                   space allowed only if it is not
        #                   as the prefix or suffix,
        #                   must be between 2 and 20 characters)
        # - invalid username (non alphanumeric characters)
        # - invalid username (empty)
        # - invalid username (illegal spaces at front and end)
        # - invalid username (too short, <2 characters)
        # - invalid username (too long, >20 characters)

        # open login page
        self.open(base_url + '/login')

        # log in so that authenticate is passed and user can be updated
        self.type("#email", "nathankowal@yahoo.ca")
        self.type("#password", "TestPassword47!")

        self.click("#login-button")

        # valid
        self.click('a[id="update-profile-link"]')
        self.type("#user_name", "validUser23")
        self.click("#update-button")
        self.assert_no_js_errors()

        # not alphanumeric
        self.click('a[id="update-profile-link"]')
        self.type("#user_name", "not alpha !")
        self.click("#update-button")

        assert(not self.assert_no_js_errors())

        # empty
        self.click('a[id="update-profile-link"]')
        self.type("#user_name", "")
        self.click("#update-button")

        assert(not self.assert_no_js_errors())

        # illegal spaces
        self.click('a[id="update-profile-link"]')
        self.type("#user_name", " illegal spaces ")
        self.click("#update-button")

        assert(not self.assert_no_js_errors())

        # too short
        self.click('a[id="update-profile-link"]')
        self.type("#user_name", "d")
        self.click("#update-button")

        assert(not self.assert_no_js_errors())

        # too long
        self.click('a[id="update-profile-link"]')
        self.type("#user_name", "tooooooooooooooooooooooooooooooo long")
        self.click("#update-button")

        assert(not self.assert_no_js_errors())
