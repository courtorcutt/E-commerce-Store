from seleniumbase import BaseCase
from qbay_test.conftest import base_url
from unittest.mock import patch
from qbay.models import User
from selenium import webdriver


class FrontEndLoginTest(BaseCase):

    # the following 3 test functions use three blackbox testing methods:
    # - functionality testing
    # - input partitioning
    # - output partitioning
    # Note: requirement R2_1 is tested twice in order to demonstrate
    # three different blackbox methods as requested. (login only has
    # two requirements)

    def test_R2_1_user_login_success_fe(self, *_):

        # FUNCTIONALITY TESTING
        # testing for functionality as described "A user can log in using
        # her/his email address and the password"
        # Must register an account first
        self.open(base_url + '/register')

        # register
        self.type("#first_name", "Zac")
        self.type("#last_name", "Silva")
        self.type("#email", "fakemail@gmail.com")
        self.type("#user_name", "coolDood")
        self.type("#password1", "TestPassword24!")
        self.type("#password2", "TestPassword24!")

        self.click("#sign-up")

        # first, logout from profile
        self.click('a[id="logout-link"]')

        # navigate to login page
        self.open(base_url + '/login')

        # check that elements are there
        self.assert_element("#login-heading")
        self.assert_text("Log In", "#login-heading")

        # attempt to Login
        self.type("#email", "fakemail@gmail.com")
        self.type("#password", "TestPassword24!")

        self.click("#login-button")

        # check if login worked
        # should redirect to profile page, check for correct user message
        self.assert_element("#welcome-heading")
        self.assert_text("Welcome Zac Silva!", "#welcome-heading")
        # logout for next test
        self.click('a[id="logout-link"]')

    def test_R2_2_login_requirements_fe(self, *_):

        # INPUT PARTITIONING
        # test cases covering different possible inputs to login
        # inputs are partitioned as follows:
        # - valid login (registered user, should login)
        # - invalid email (email does not follow requirements)
        # - invalid password (password does not follow requirements)

        # open login page
        self.open(base_url + '/login')

        # valid login, one account already registered
        self.type("#email", "fakemail@gmail.com")
        self.type("#password", "TestPassword24!")
        self.click("#login-button")

        # check if login worked
        # should redirect to profile page, check for correct user message
        self.assert_no_js_errors()
        self.assert_element("#welcome-heading")
        self.assert_text("Welcome Zac Silva!", "#welcome-heading")

        # invalid email case
        # first, logout
        self.click('a[id="logout-link"]')
        # now attempt to log back in (with invalid email)
        self.open(base_url + '/login')
        self.type("#email", "inval_format")
        self.type("#password", "TestPassword24!")
        self.click("#login-button")
        # Should prompt a failure message, no js error because it checked
        # validity before attempting to access database
        self.assert_element("#message")
        self.assert_text("Login Failed.", "#message")
        self.assert_no_js_errors()

        # invalid password
        self.open(base_url + '/login')
        self.type("#email", "fakemail@gmail.com")
        self.type("#password", "invalformat")
        self.click("#login-button")
        # Should give a failure message, no js error because it checked
        # validity before attempting to access database
        self.assert_element("#message")
        self.assert_text("Login Failed.", "#message")
        self.assert_no_js_errors()

    def test_R2_1b_login_requirements_fe(self, *_):

        # OUTPUT PARTITIONING
        # test cases covering different possible oututs to login
        # inputs are partitioned as follows:
        # - successful login (result of a registered users data being input)
        # - unsuccessful login (caused by data which does not match a
        #                       registered user being input)

        # open login page
        self.open(base_url + '/login')

        # successful login output
        self.type("#email", "fakemail@gmail.com")
        self.type("#password", "TestPassword24!")
        self.click("#login-button")
        # check if login worked
        # should redirect to profile page, check for correct user message
        self.assert_no_js_errors()
        self.assert_element("#welcome-heading")
        self.assert_text("Welcome Zac Silva!", "#welcome-heading")

        # logout and test other output case
        self.click('a[id="logout-link"]')

        # return to login page
        self.open(base_url + '/login')

        # unsuccessful login output
        self.type("#email", "fakemail@gmail.com")
        self.type("#password", "IncorrectP@ssw0rd")
        self.click("#login-button")
        # Should give failure message and cause no js error
        self.assert_element("#message")
        self.assert_text("Login Failed.", "#message")
        self.assert_no_js_errors()
