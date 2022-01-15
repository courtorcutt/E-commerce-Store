
from seleniumbase import BaseCase

from qbay_test.conftest import base_url
from unittest.mock import patch
from qbay.models import User
from selenium import webdriver

"""
This file contains the test for registering (frontend)
Three black box testing methods will be used:
   - Input Partitioning Testing
   - Boundary Value Robustness Testing
   - Output Partitioning Testing
"""


class FrontEndUserRegisterTest(BaseCase):

    def test_R1_5_6_user_name(self, *_):
        # INPUT PARTITIONING -> USER NAME
        # this test case is for the user name requirement
        # inputs are partitioned as follows:
        # - valid user name (non-empty (R1-5), alphanumeric only (R1-5),
        #       space only allowed only if at beginning or end (R1-5),
        #       longer than 2 characters, less than 20 (R1-6))
        # - invalid user name (empty, non-alphanumeric,
        #       space at beg or end, shorter than 2 char,
        #       more than 20)

        # open register page
        self.open(base_url + '/register')

        # test for illegal case - no user name
        self.type("#first_name", "Ariel")
        self.type("#last_name", "Swim")
        self.type("#email", "imamermaid@gmail.ca")
        self.type("#user_name", "")
        self.type("#password1", "Swimm1ing!")
        self.type("#password2", "Swimm1ing!")
        self.click("#sign-up")
        assert (not self.assert_no_js_errors())

        # test for legal case - entered user name
        self.type("#first_name", "Ariel")
        self.type("#last_name", "Swim")
        self.type("#email", "imamermaid@gmail.ca")
        self.type("#user_name", "ariel")
        self.type("#password1", "Swimm1ing!")
        self.type("#password2", "Swimm1ing!")
        self.click("#sign-up")
        self.assert_no_js_errors()

        # open register page
        self.open(base_url + '/register')

        # test for illegal case - non-alphanumeric
        self.type("#first_name", "Elsa")
        self.type("#last_name", "Snow")
        self.type("#email", "OlafIsBest@gmail.ca")
        self.type("#user_name", "e_lsa")
        self.type("#password1", "Sn0wFight$")
        self.type("#password2", "Sn0wFight$")
        self.click("#sign-up")
        assert (not self.assert_no_js_errors())

        # test for legal case - alphanumeric
        self.type("#first_name", "Elsa")
        self.type("#last_name", "Snow")
        self.type("#email", "OlafIsBest@gmail.ca")
        self.type("#user_name", "elsa")
        self.type("#password1", "Sn0wFight$")
        self.type("#password2", "Sn0wFight$")
        self.click("#sign-up")
        self.assert_no_js_errors()

        # open register page
        self.open(base_url + '/register')

        # test for illegal case - spacing at beg
        self.type("#first_name", "Rapunzel")
        self.type("#last_name", "Hair")
        self.type("#email", "myhairissooheavy@gmail.ca")
        self.type("#user_name", " Rapunzel")
        self.type("#password1", "H@irCare2")
        self.type("#password2", "H@irCare2")
        self.click("#sign-up")
        assert (not self.assert_no_js_errors())

        # test for illegal case - spacing at end
        self.type("#first_name", "Rapunzel")
        self.type("#last_name", "Hair")
        self.type("#email", "myhairissooheavy@gmail.ca")
        self.type("#user_name", "Rapunzel ")
        self.type("#password1", "H@irCare2")
        self.type("#password2", "H@irCare2")
        self.click("#sign-up")
        assert (not self.assert_no_js_errors())

        # test for legal case - spacing
        self.type("#first_name", "Cinderella")
        self.type("#last_name", "Running")
        self.type("#email", "midnightIsHere@gmail.ca")
        self.type("#user_name", "Cinder Ella")
        self.type("#password1", "fairyGodMotherRules!2")
        self.type("#password2", "fairyGodMotherRules!2")
        self.click("#sign-up")
        self.assert_no_js_errors()

        # open register page
        self.open(base_url + '/register')

        # test for illegal case - less than 2 char
        self.type("#first_name", "Tiana")
        self.type("#last_name", "Cook")
        self.type("#email", "Iamanamazingchef@gmail.ca")
        self.type("#user_name", "T")
        self.type("#password1", "Beignet$")
        self.type("#password2", "Beignet$")
        self.click("#sign-up")
        assert (not self.assert_no_js_errors())

        # test for illegal case - more than 20 char
        self.type("#first_name", "Tiana")
        self.type("#last_name", "Cook")
        self.type("#email", "Iamanamazingchef@gmail.ca")
        self.type("#user_name", "TianaOwnTheBestRestaurantInTown")
        self.type("#password1", "Beignet$")
        self.type("#password2", "Beignet$")
        self.click("#sign-up")
        assert (not self.assert_no_js_errors())

        # test for legal case - inbetween 2 and 20 char
        self.type("#first_name", "Tiana")
        self.type("#last_name", "Cook")
        self.type("#email", "Iamanamazingchef@gmail.ca")
        self.type("#user_name", "Tiana")
        self.type("#password1", "Beignet$")
        self.type("#password2", "Beignet$")
        self.click("#sign-up")
        self.assert_no_js_errors()

    def test_R1_1_2_3_7_email(self, *_):
        # BOUNDARY VALUE ROBUSTNESS TESTING -> EMAIL
        # this test case is for the email requirement
        # emails must be as follows:
        # - legal email (unique to a user (R1-2) (R1-7), non-empty (R1_1),
        #       email must be addr-spec defined in RFC 5322 (R1-3)
        # - illegal email (not unique to a user, empty,
        #       email isn't addr-spec in RFC 5322
        # Below each boundary test is explained in each case

        # UNIQUE USER (R1-2) (R1-7) TESTING:
        # open register page
        self.open(base_url + '/register')

        # establish a unique user
        self.type("#first_name", "Comp")
        self.type("#last_name", "Engineering")
        self.type("#email", "compwins@gmail.ca")
        self.type("#user_name", "Comp")
        self.type("#password1", "C0mputer1010!")
        self.type("#password2", "C0mputer1010!")
        self.click("#sign-up")
        self.assert_no_js_errors()

        # open register page
        self.open(base_url + '/register')

        # boundary case of one letter being upper case
        self.type("#first_name", "Comp1")
        self.type("#last_name", "Engineering1")
        self.type("#email", "compwiNs@gmail.ca")
        self.type("#user_name", "Comp1")
        self.type("#password1", "C0mputer10101!")
        self.type("#password2", "C0mputer10101!")
        self.click("#sign-up")
        self.assert_no_js_errors()

        # open register page
        self.open(base_url + '/register')

        # boundary case of one additional number
        self.type("#first_name", "Comp2")
        self.type("#last_name", "Engineering2")
        self.type("#email", "compwins1@gmail.ca")
        self.type("#user_name", "Comp2")
        self.type("#password1", "C0mputer101010!")
        self.type("#password2", "C0mputer101010!")
        self.click("#sign-up")
        self.assert_no_js_errors()

        # open register page
        self.open(base_url + '/register')

        # boundary case of space in front
        self.type("#first_name", "Comp3")
        self.type("#last_name", "Engineering3")
        self.type("#email", " compwins@gmail.ca")
        self.type("#user_name", "Comp3")
        self.type("#password1", "C0mputer01010!")
        self.type("#password2", "C0mputer01010!")
        self.click("#sign-up")
        assert (not self.assert_no_js_errors())

        # boundary case of different country ending
        self.type("#first_name", "Comp4")
        self.type("#last_name", "Engineering4")
        self.type("#email", " compwins@gmail.go")
        self.type("#user_name", "Comp4")
        self.type("#password1", "C0mpUter01010!")
        self.type("#password2", "C0mpUter01010!")
        self.click("#sign-up")
        assert (not self.assert_no_js_errors())

        # test same email fails for uniqueness
        self.type("#first_name", "Comp5")
        self.type("#last_name", "Engineering5")
        self.type("#email", "compwins@gmail.ca")
        self.type("#user_name", "Comp5")
        self.type("#password1", "C0mputer511010!")
        self.type("#password2", "C0mputer511010!")
        self.click("#sign-up")
        assert (not self.assert_no_js_errors())

        # boundary case of different email provider
        self.type("#first_name", "Comp6")
        self.type("#last_name", "Engineering6")
        self.type("#email", "compwins@hotmail.ca")
        self.type("#user_name", "Comp6")
        self.type("#password1", "C06mputer11010!")
        self.type("#password2", "C06mputer11010!")
        self.click("#sign-up")
        self.assert_no_js_errors()

        # NON-EMPTY REQUIREMENT (R1_1) TESTING
        # open register page
        self.open(base_url + '/register')

        # test register fails if no email entered
        self.type("#first_name", "Mining")
        self.type("#last_name", "Engineering")
        self.type("#email", "")
        self.type("#user_name", "Mining")
        self.type("#password1", "Cryst@lsWin!")
        self.type("#password2", "Cryst@lsWin!")
        self.click("#sign-up")
        assert (not self.assert_no_js_errors())

        # boundary case of multiple spaces
        self.type("#first_name", "Mining")
        self.type("#last_name", "Engineering")
        self.type("#email", "        ")
        self.type("#user_name", "Mining")
        self.type("#password1", "Cryst@lsWin!")
        self.type("#password2", "Cryst@lsWin!")
        self.click("#sign-up")
        assert (not self.assert_no_js_errors())

        # RFC 5322 REQUIREMENT (R1_3) TESTING
        # assert email registers to a user even
        # with a company provider such as miningeng
        self.type("#first_name", "Mining")
        self.type("#last_name", "Engineering")
        self.type("#email", "mining@miningeng.com")
        self.type("#user_name", "Mining")
        self.type("#password1", "Cryst@lsWin!")
        self.type("#password2", "Cryst@lsWin!")
        self.click("#sign-up")
        self.assert_no_js_errors()

        # open register page
        self.open(base_url + '/register')

        # boundary case for RFC 5322 email format
        # of no ending
        self.type("#first_name", "Geo")
        self.type("#last_name", "Engineering")
        self.type("#email", "abc123@")
        self.type("#user_name", "Rocks")
        self.type("#password1", "R0cksAreCool!")
        self.type("#password2", "R0cksAreCool!")
        self.click("#sign-up")
        assert (not self.assert_no_js_errors())

        # boundary case for RFC 5322 email format
        # of multiple periods in ending
        self.type("#first_name", "Geo")
        self.type("#last_name", "Engineering")
        self.type("#email", "HeyThere12@runn.ing.ca")
        self.type("#user_name", "Rocks")
        self.type("#password1", "R0cksAreCool!")
        self.type("#password2", "R0cksAreCool!")
        self.click("#sign-up")
        assert (not self.assert_no_js_errors())

        # boundary case for RFC 5322 email format
        # of multiple periods in ending
        self.type("#first_name", "Geo")
        self.type("#last_name", "Engineering")
        self.type("#email", "rocksAreCool1@0.LaLaLand.ca")
        self.type("#user_name", "Rocks")
        self.type("#password1", "R0cksAreCool!")
        self.type("#password2", "R0cksAreCool!")
        self.click("#sign-up")
        assert (not self.assert_no_js_errors())

        # boundary case for RFC 5322 email format
        # where just end country code is capital
        self.type("#first_name", "Geo")
        self.type("#last_name", "Engineering")
        self.type("#email", "rocks@gmail.CA")
        self.type("#user_name", "Rocks")
        self.type("#password1", "R0cksAreCool!")
        self.type("#password2", "R0cksAreCool!")
        self.click("#sign-up")
        assert (not self.assert_no_js_errors())

        # boundary case for RFC 5322 email format
        # where correct form but has capital at end
        self.type("#first_name", "Geo")
        self.type("#last_name", "Engineering")
        self.type("#email", "rocks@GMail.ca")
        self.type("#user_name", "Rocks")
        self.type("#password1", "R0cksAreCool!")
        self.type("#password2", "R0cksAreCool!")
        self.click("#sign-up")
        assert (not self.assert_no_js_errors())

        # boundary case for RFC 5322 email format
        # of no country code ending
        self.type("#first_name", "Geo")
        self.type("#last_name", "Engineering")
        self.type("#email", "rocks@rocks")
        self.type("#user_name", "Rocks")
        self.type("#password1", "R0cksAreCool!")
        self.type("#password2", "R0cksAreCool!")
        self.click("#sign-up")
        assert (not self.assert_no_js_errors())

        # boundary case for RFC 5322 email format
        # periods at start
        self.type("#first_name", "Geo")
        self.type("#last_name", "Engineering")
        self.type("#email", "r.0.c.k.@@gmail.com")
        self.type("#user_name", "Rocks")
        self.type("#password1", "R0cksAreCool!")
        self.type("#password2", "R0cksAreCool!")
        self.click("#sign-up")
        assert (not self.assert_no_js_errors())

        # assert a correct RFC 5322 format can register
        self.type("#first_name", "Geo")
        self.type("#last_name", "Engineering")
        self.type("#email", "rocks123@hotmail.com")
        self.type("#user_name", "Rocks")
        self.type("#password1", "R0cksAreCool!")
        self.type("#password2", "R0cksAreCool!")
        self.click("#sign-up")
        self.assert_no_js_errors()

    def test_R1_4_password(self, *_):
        # INPUT PARTITIONING -> PASSWORD
        # this test case is for the password requirement
        # inputs are partitioned as follows:
        # - legal user name (min 6 length, one upper case
        #       one lower case, one special character) (R1-4)
        # - illegal password (less than 6 length, no upper case,
        #       no lower case, no special characters) (R1-4)

        # open register page
        self.open(base_url + '/register')

        # test for illegal case - less than 6 characters
        self.type("#first_name", "Monica")
        self.type("#last_name", "Geller")
        self.type("#email", "cleaningIsLife@gmail.ca")
        self.type("#user_name", "monica")
        self.type("#password1", "C!ean")
        self.type("#password2", "C!ean")
        self.click("#sign-up")
        assert (not self.assert_no_js_errors())

        # test for legal case - more than 6 characters
        self.type("#first_name", "Monica")
        self.type("#last_name", "Geller")
        self.type("#email", "cleaningIsLife@gmail.ca")
        self.type("#user_name", "monica")
        self.type("#password1", "C!eaning")
        self.type("#password2", "C!eaning")
        self.click("#sign-up")
        self.assert_no_js_errors()

        # open register page
        self.open(base_url + '/register')

        # test for illegal case - no upper case
        self.type("#first_name", "Chandler")
        self.type("#last_name", "Bing")
        self.type("#email", "loveSarcasm@gmail.ca")
        self.type("#user_name", "chandler")
        self.type("#password1", "inlovewithjanice!")
        self.type("#password2", "inlovewithjanice!")
        self.click("#sign-up")
        assert (not self.assert_no_js_errors())

        # test for legal case - upper case
        self.type("#first_name", "Chandler")
        self.type("#last_name", "Bing")
        self.type("#email", "loveSarcasm@gmail.ca")
        self.type("#user_name", "chandler")
        self.type("#password1", "InLoveWithJanice!")
        self.type("#password2", "InLoveWithJanice!")
        self.click("#sign-up")
        self.assert_no_js_errors()

        # open register page
        self.open(base_url + '/register')

        # test for illegal case - no lower case
        self.type("#first_name", "Ross")
        self.type("#last_name", "Geller")
        self.type("#email", "loveDinosaur@gmail.ca")
        self.type("#user_name", "ross")
        self.type("#password1", "BONESARECOOL!")
        self.type("#password2", "BONESARECOOL!")
        self.click("#sign-up")
        assert (not self.assert_no_js_errors())

        # test for legal case - lower case
        self.type("#first_name", "Ross")
        self.type("#last_name", "Geller")
        self.type("#email", "loveDinosaur@gmail.ca")
        self.type("#user_name", "ross")
        self.type("#password1", "BonesAreCool!")
        self.type("#password2", "BonesAreCool!")
        self.click("#sign-up")
        self.assert_no_js_errors()

        # open register page
        self.open(base_url + '/register')

        # test for illegal case - no special case
        self.type("#first_name", "Rachel")
        self.type("#last_name", "Green")
        self.type("#email", "fashionforever@gmail.ca")
        self.type("#user_name", "rachel")
        self.type("#password1", "Bloomberg")
        self.type("#password2", "Bloomberg")
        self.click("#sign-up")
        assert(not self.assert_no_js_errors())

        # test for legal case - special case
        self.type("#first_name", "Rachel")
        self.type("#last_name", "Green")
        self.type("#email", "fashionforever@gmail.ca")
        self.type("#user_name", "rachel")
        self.type("#password1", "Bloomberg!")
        self.type("#password2", "Bloomberg!")
        self.click("#sign-up")
        self.assert_no_js_errors()

    def test_R1_8_shipping_address(self, *_):
        # OUTPUT PARTITIONING
        # this test case is for the shipping address requirement
        # outputs are partitioned as follows:
        # - successful registration of user with no shipping address
        #       (caused by no input) (R1-8)
        # - unsuccessful registration of user with a shipping address
        #       (caused by input of a shipping address) (R1-8)

        # open register page
        self.open(base_url + '/register')

        # successful user registration from no shipping address
        self.type("#first_name", "Simba")
        self.type("#last_name", "Lion")
        self.type("#email", "simba@gmail.ca")
        self.type("#user_name", "simba")
        self.type("#password1", "IamaLion!2")
        self.type("#password2", "IamaLion!2")
        self.click("#sign-up")
        self.assert_no_js_errors()

        # open register page
        self.open(base_url + '/register')

        # successful user registration from no shipping address
        self.type("#first_name", "Snow")
        self.type("#last_name", "White")
        self.type("#email", "snowwhite@yahoo.ca")
        self.type("#user_name", "SnowWhite")
        self.type("#password1", "IliketoSing2!")
        self.type("#password2", "IliketoSing2!")
        self.type("#shipping_address", "")
        self.click("#sign-up")
        self.assert_no_js_errors()

        # open register page
        self.open(base_url + '/register')

        # unsuccessful user registration from an entered shipping address
        self.type("#first_name", "Goofy")
        self.type("#last_name", "Dog")
        self.type("#email", "goofy@yahoo.ca")
        self.type("#user_name", "goofy")
        self.type("#password1", "IamaDog!2")
        self.type("#password2", "IamaDog!2")
        self.type("#shipping_address", "14 Disney Rd")
        self.click("#sign-up")
        assert (not self.assert_no_js_errors())

    def test_R1_9_postal_code(self, *_):
        # OUTPUT PARTITIONING
        # this test case is for the postal code requirement
        # outputs are partitioned as follows:
        # - successful registration of user with no postal code
        #       (caused by no input) (R1-9)
        # - unsuccessful registration of user with a postal code
        #       (caused by input of a postal code)

        # open register page
        self.open(base_url + '/register')

        # successful user registration from no postal code input
        self.type("#first_name", "Micky")
        self.type("#last_name", "Mouse")
        self.type("#email", "mickymouse@yahoo.ca")
        self.type("#user_name", "micky")
        self.type("#password1", "IamaMouse!2")
        self.type("#password2", "IamaMouse!2")
        self.click("#sign-up")
        self.assert_no_js_errors()

        # open register page
        self.open(base_url + '/register')

        # successful user registration from no postal code input
        self.type("#first_name", "Donald")
        self.type("#last_name", "Duck")
        self.type("#email", "donaldduck@hotmail.ca")
        self.type("#user_name", "Donald")
        self.type("#password1", "IamaDuck!2")
        self.type("#password2", "IamaDuck!2")
        self.type("#postal_code", "")
        self.click("#sign-up")
        self.assert_no_js_errors()

        # open register page
        self.open(base_url + '/register')

        # unsuccessful user registration from an entered postal code
        self.type("#first_name", "Goofy")
        self.type("#last_name", "Dog")
        self.type("#email", "goofy@yahoo.ca")
        self.type("#user_name", "goofy")
        self.type("#password1", "IamaDog!2")
        self.type("#password2", "IamaDog!2")
        self.type("#postal_code", "M4N1Z2")
        self.click("#sign-up")
        assert (not self.assert_no_js_errors())

    def test_R1_10_balance(self, *_):
        # OUTPUT PARTITIONING
        # this test case is for the balance requirement
        # outputs are partitioned as follows:
        # - successful registration of user with $100 balance
        #       (caused by no input) (R1_10)
        # - unsuccessful registration of user
        #       (caused by input of a balance)

        # open register page
        self.open(base_url + '/register')

        # successful user registration from balance of $100
        # from nothing entered (default)
        self.type("#first_name", "Winny")
        self.type("#last_name", "The-Pooh")
        self.type("#email", "winniethepooh@yahoo.ca")
        self.type("#user_name", "winnie")
        self.type("#password1", "IlovePiglet!20")
        self.type("#password2", "IlovePiglet!20")
        self.click("#sign-up")
        self.assert_no_js_errors()

        # open register page
        self.open(base_url + '/register')

        # unsuccessful user registration from an entered balance
        self.type("#first_name", "Tigger")
        self.type("#last_name", "TheGreat")
        self.type("#email", "tiggerthegreat@yahoo.ca")
        self.type("#user_name", "tiggerTheGreat")
        self.type("#password1", "IloveEeyore!23")
        self.type("#password2", "IloveEeyore!23")
        self.type("#balance", "200")
        self.click("#sign-up")
        assert(not self.assert_no_js_errors())
