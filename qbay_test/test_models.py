"""
Testing code needs to go here

Example from template:
"""

from qbay.models import *
from qbay.userDataAccess import *
from qbay.userMethods import login, update, register
from qbay.productMethods import update_product, buy_product

# initialize objects
seller_1 = User(email='test@test.com', password='YooIAmCool23!',
                user_name="supsup", first_name="Hi", last_name="Dude")

buyer_1 = User(email='scroogemc@duckmail.com', password='M0n3yB4g5!',
               user_name="GoldDuck", first_name="Scrooge",
               last_name="McDuck", balance=1500.00)

product_1 = Product(id=1, price=300.02, title="test",
                    description="This is a test",
                    last_modified_date=datetime.utcnow(),
                    owner_email=seller_1.email)

product_expensive = Product(id=2, price=1200.00, title="test_exp",
                            description="This is to test buyer having \
                            insufficient funds",
                            last_modified_date=datetime.utcnow(),
                            owner_email=seller_1.email, isSold=False)

product_cheap = Product(id=3, price=12.99, title="test_chp",
                        description="This is to test user buying own product",
                        last_modified_date=datetime.utcnow(),
                        owner_email=seller_1.email, isSold=False)

transaction_1 = Transaction(batch_id="1", user_email=seller_1.email,
                            seller_email=seller_1.email, status="Done",
                            date=datetime.utcnow(),
                            product_id=product_1.id, price=product_1.price)

transaction_2 = Transaction(batch_id="1", user_email=seller_1.email,
                            seller_email=seller_1.email, status="Failed",
                            date=datetime.utcnow(),
                            product_id=product_1.id, price=product_1.price)

# add objects to database
db.create_all()
db.session.add(product_1)
db.session.add(product_expensive)
db.session.add(product_cheap)
db.session.add(transaction_1)
db.session.add(transaction_2)
db.session.commit()


# test that empty password is validated as false
def test_R1_1_user_password():
    assert User.validate_password("") is False


# test that empty username is validated as false
def test_R1_1_user_email():
    assert User.validate_user_email("") is False


def test_R1_2_email_format():
    assert User.validate_user_email("helpme") is False
    assert User.validate_user_email("marys40@gmail.com") is "marys40@gmail.com"


# test that email validation works
def test_R1_3_email_format():
    assert User.validate_user_email("yooo") is False
    assert User.validate_user_email(seller_1.email) is seller_1.email


# test that password format works
def test_R1_4_password_format():
    assert User.validate_password("43d") is False
    assert User.validate_password("YoIAmCool23!") is "YoIAmCool23!"


def test_R1_5_user_name():
    assert User.validate_username(" ") is False
    assert User.validate_username("abc ") is False
    assert User.validate_username(" abc") is False
    assert User.validate_username("abc$") is False
    assert User.validate_username("abc13") is "abc13"


def test_R1_6_user_name():
    assert User.validate_username("a") is False
    assert User.validate_username("abcdefghijklmnopqrstuvwxymz12345") is False
    assert User.validate_username("abcd1") is "abcd1"


def test_R1_7_email_format():
    assert register(email='test@test.com', password='YooIAmCool23!',
                    user_name="supsup", first_name="Hi",
                    last_name="Dude") is True
    assert register(email='test@gmail.com', password='YooIAmCool23!',
                    user_name="supsup", first_name="Hi",
                    last_name="Dude") is False


def test_R1_8_shipping_addres():
    user = search_user('test@test.com')
    assert user.shipping_address is None


def test_R1_9_postal_code():
    user = search_user('test@test.com')
    assert user.postal_code is None


def test_R1_10_balance():
    user = search_user('test@test.com')
    assert user.balance == 100.0


# test user login
def test_R2_1_login():
    user = login("test@test.com", "YooIAmCool23!")
    assert user is not None

    # verify that the user returned is the same as the seller_1 User above
    assert user == seller_1
    assert user.user_name == seller_1.user_name


def test_R2_2_login():
    # email and password do not meet validation requirements, so user is None
    user = login("yo", "sup")
    assert user is None

    # email and passowrd meet requirements, but the
    # password is incorrect for the email given
    user = login("test@test.com", "YooIAmCool23!!")
    assert user is None


# test user update
def test_R3_1_user_update():
    assert update(email="test@test.com", user_name="hellodude",
                  shipping_address="yo im on the street",
                  postal_code="M5M 1S4") is True

    # email not in database, so fails update
    assert update(email="sf@gmail.com", user_name="hellodude",
                  shipping_address="yo im on the street",
                  postal_code="M5M 1S4") is False


def test_R3_2_shipping_address_update():
    # invalid shipping address, fails update
    assert update(email="test@test.com", user_name="hellodude",
                  shipping_address="yo!!! im on the street",
                  postal_code="M5M 1S4") is False

    # valid shipping address, so update is valid
    assert update(email="test@test.com", user_name="hellodude",
                  shipping_address="yo im alphanumeric",
                  postal_code="M5M 1S4") is True


def test_R3_3_postal_code_update():
    # postal code is valid, so update is valid
    assert update(email="test@test.com", user_name="hellodude",
                  shipping_address="yo im alphanumeric",
                  postal_code="M5M 1S4") is True

    # postal code starts with Z, so invalid update
    assert update(email="test@test.com", user_name="hellodude",
                  shipping_address="yo im alphanumeric",
                  postal_code="Z5M 1Z3") is False

    # postal code in incorrect format, so invalid update
    assert update(email="test@test.com", user_name="hellodude",
                  shipping_address="yo im alphanumeric",
                  postal_code="not a postal code") is False


def test_R3_4_user_name_update():
    # username is empty, so invalid update
    assert update(email="test@test.com",
                  user_name="", shipping_address="yo im alphanumeric",
                  postal_code="M5M 1S4") is False

    # username has leading and trailing spaces, so invalid update
    assert update(email="test@test.com",
                  user_name=" illegal format  ",
                  shipping_address="yo im alphanumeric",
                  postal_code="M5M 1S4") is False

    # username is too long, so invalid update
    assert update(email="test@test.com",
                  user_name="way tooooooooooooo longgggg",
                  shipping_address="yo im alphanumeric",
                  postal_code="M5M 1S4") is False

    # username is valid, so valid update
    assert update(email="test@test.com", user_name="valid username",
                  shipping_address="yo im alphanumeric",
                  postal_code="M5M 1S4") is True


def test_postal_code_validation():
    assert User.validate_postal_code("M5M 2A1") == "M5M 2A1"
    assert User.validate_postal_code("fbs") is False
    assert User.validate_postal_code("Z5Z 3Z1") is False


def test_shipping_address_validation():
    assert User.validate_shipping_address("I am a shipping address!") is False
    assert User.validate_shipping_address("235 Brock St Kingston ON") \
           is "235 Brock St Kingston ON"


def test_user_queries():
    # retrieve first user
    assert User.query.first() == seller_1


# All required attributes can be updated, excluding
# owner_email and last_modified_date.
def test_r5_1_update_product():
    # Legally update all attributes allowed
    update_status = update_product(product_1, "Another Test", "Testing",
                                   349.99, "This is still a test")
    # Must have returned none, and changed the fields within product_1
    assert not update_status
    assert product_1.title == "Another Test"
    assert product_1.product_type == "Testing"
    assert product_1.price == 349.99
    assert product_1.description == "This is still a test"


# Price can be only increased but cannot be decreased
def test_r5_2_update_product():
    # set price to new price
    product_1.set_price(1000)
    assert product_1.price == 1000
    # fail to set lower cost than before
    product_1.set_price(34)
    assert product_1.price == 1000


# last_modified_date should be updated
# when the update operation is successful.
def test_r5_3_update_product():
    # product_1 last modified date
    old_date = product_1.last_modified_date
    # set title to new title
    product_1.set_title("test2")
    assert product_1.title == "test2"
    # check if last modified date was updated
    assert product_1.last_modified_date > old_date
    # failed set because the ! is not alphanumeric
    old_date = product_1.last_modified_date
    product_1.set_title("test2!")
    # title should not have changed
    assert product_1.title == "test2"
    # product_1 should not have an updated date
    assert product_1.last_modified_date == old_date
    # check if description date updates
    # set new description
    product_1.set_description("this is a description")
    assert product_1.description == "this is a description"
    # check if last modified date was updated
    assert product_1.last_modified_date > old_date
    # failed set because description too short
    old_date = product_1.last_modified_date
    product_1.set_description("this is ")
    assert product_1.description == "this is a description"
    # product_1 should not have an updated date
    assert product_1.last_modified_date == old_date
    # product_1 last modified date
    old_date = product_1.last_modified_date
    # set title to new title
    product_1.set_price(1000)
    assert product_1.price == 1000
    # check if last modified date was updated
    assert product_1.last_modified_date > old_date
    # fail to set lower cost than before
    old_date = product_1.last_modified_date
    product_1.set_price(34)
    assert product_1.price == 1000
    # product_1 should not have an updated date
    assert product_1.last_modified_date == old_date


#  When updating an attribute, one has to make sure
#  that it follows the same requirements as above
def test_r5_4_update_product():
    # fail because price too small
    assert product_1.set_price(2) is not False
    # check if title has already been set
    # fails because test2 is already a title
    assert product_1.set_title("test2") is not False
    # this fails because test2! contains non alphanumeric characters
    assert product_1.set_title("test2!") is not False
    # this fails because its too long
    check = product_1.set_title(" veeeeeerrrryyyyy lonngggggggggggg" +
                                "veeeeeerrrryyyyy lonngggggggggggg" +
                                " veeeeeerrrryyyyy lonngggggggggggg" +
                                " veeeeeerrrryyyyy lonngggggggggggg" +
                                " veeeeeerrrryyyyy lonngggggggggggg" +
                                " veeeeeerrrryyyyy lonngggggggggggg" +
                                " veeeeeerrrryyyyy lonngggggggggggg" +
                                " veeeeeerrrryyyyy lonngggggggggggg" +
                                " veeeeeerrrryyyyy lonngggggggggggg")

    assert check
    # this sets the title without whitespaces at end or front
    product_1.set_title(" test 4 space space at end and beginning ") is False
    assert product_1.title == "test 4 space space at end and beginning"
    # set description
    product_1.set_description("this is a description" +
                              "yay yay yay yay yay yay")
    assert product_1.description == "this is a description" +\
                                    "yay yay yay yay yay yay"
    # failed set because description too short
    product_1.set_description("this is ")
    assert product_1.description == "this is a description" +\
                                    "yay yay yay yay yay yay"
    # failed set because description shorter than title
    product_1.set_description("this is shorter than title")
    assert product_1.description == "this is a description" +\
                                    "yay yay yay yay yay yay"
    # fail to set lower cost than before
    product_1.set_price(34)
    assert product_1.price == 1000
    # fail because not a integer or float
    product_1.set_price("bloop")
    assert product_1.price == 1000
    # fail because too big
    product_1.set_price(1000000)
    assert product_1.price == 1000


# The title of the product has to be alphanumeric-only,
# and space allowed only if it is not as prefix and suffix.
def test_r4_1_create_product():
    # this fails because test2! contains non alphanumeric characters
    assert check_title("test2!") is False
    assert check_title("test2##&") is False
    # this returns the title without spaces in front or end
    assert check_title(" test 4 ") == "test 4"


# The title of the product is no longer than 80 characters.
def test_r4_2_create_product():
    # this fails because it's too long
    check = check_title(" veeeeeerrrryyyyy lonngggggggggggg" +
                        "veeeeeerrrryyyyy lonngggggggggggg" +
                        " veeeeeerrrryyyyy lonngggggggggggg" +
                        " veeeeeerrrryyyyy lonngggggggggggg" +
                        " veeeeeerrrryyyyy lonngggggggggggg" +
                        " veeeeeerrrryyyyy lonngggggggggggg" +
                        " veeeeeerrrryyyyy lonngggggggggggg" +
                        " veeeeeerrrryyyyy lonngggggggggggg" +
                        " veeeeeerrrryyyyy lonngggggggggggg")

    assert check is False


# The description of the product can be arbitrary characters,
# with a minimum length of 20 characters and a maximum of 2000 characters.
def test_r4_3_create_product():
    # this fails because description <20
    assert check_description(" test 4 ", " I love desc") is False
    # this fails because description >2000
    assert check_description("product1 is good",
                             " veeeeeerrrryyyyy lonngggggggggggg" +
                             "veeeeeerrrryyyyy lonngggggggggggg" +
                             " veeeeeerrrryyyyy lonngggggggggggg" +
                             " veeeeeerrrryyyyy lonngggggggggggg" +
                             " veeeeeerrrryyyyy lonngggggggggggg" +
                             " veeeeeerrrryyyyy lonngggggggggggg" +
                             " veeeeeerrrryyyyy lonngggggggggggg" +
                             " veeeeeerrrryyyyy lonngggggggggggg" +
                             " veeeeeerrrryyyyy lonngggggggggggg" +
                             " veeeeeerrrryyyyy lonngggggggggggg" +
                             "veeeeeerrrryyyyy lonngggggggggggg" +
                             " veeeeeerrrryyyyy lonngggggggggggg" +
                             " veeeeeerrrryyyyy lonngggggggggggg" +
                             " veeeeeerrrryyyyy lonngggggggggggg" +
                             " veeeeeerrrryyyyy lonngggggggggggg" +
                             " veeeeeerrrryyyyy lonngggggggggggg" +
                             " veeeeeerrrryyyyy lonngggggggggggg" +
                             " veeeeeerrrryyyyy lonngggggggggggg" +
                             " veeeeeerrrryyyyy lonngggggggggggg" +
                             "veeeeeerrrryyyyy lonngggggggggggg" +
                             " veeeeeerrrryyyyy lonngggggggggggg" +
                             " veeeeeerrrryyyyy lonngggggggggggg" +
                             " veeeeeerrrryyyyy lonngggggggggggg" +
                             " veeeeeerrrryyyyy lonngggggggggggg" +
                             " veeeeeerrrryyyyy lonngggggggggggg" +
                             " veeeeeerrrryyyyy lonngggggggggggg" +
                             " veeeeeerrrryyyyy lonngggggggggggg" +
                             " veeeeeerrrryyyyy lonngggggggggggg" +
                             "veeeeeerrrryyyyy lonngggggggggggg" +
                             " veeeeeerrrryyyyy lonngggggggggggg" +
                             " veeeeeerrrryyyyy lonngggggggggggg" +
                             " veeeeeerrrryyyyy lonngggggggggggg" +
                             " veeeeeerrrryyyyy lonngggggggggggg" +
                             " veeeeeerrrryyyyy lonngggggggggggg" +
                             " veeeeeerrrryyyyy lonngggggggggggg" +
                             " veeeeeerrrryyyyy lonngggggggggggg" +
                             " veeeeeerrrryyyyy lonngggggggggggg" +
                             "veeeeeerrrryyyyy lonngggggggggggg" +
                             " veeeeeerrrryyyyy lonngggggggggggg" +
                             " veeeeeerrrryyyyy lonngggggggggggg" +
                             " veeeeeerrrryyyyy lonngggggggggggg" +
                             " veeeeeerrrryyyyy lonngggggggggggg" +
                             " veeeeeerrrryyyyy lonngggggggggggg" +
                             " veeeeeerrrryyyyy lonngggggggggggg" +
                             " veeeeeerrrryyyyy lonngggggggggggg" +
                             " veeeeeerrrryyyyy lonngggggggggggg" +
                             "veeeeeerrrryyyyy lonngggggggggggg" +
                             " veeeeeerrrryyyyy lonngggggggggggg" +
                             " veeeeeerrrryyyyy lonngggggggggggg" +
                             " veeeeeerrrryyyyy lonngggggggggggg" +
                             " veeeeeerrrryyyyy lonngggggggggggg" +
                             " veeeeeerrrryyyyy lonngggggggggggg" +
                             " veeeeeerrrryyyyy lonngggggggggggg" +
                             " veeeeeerrrryyyyy lonngggggggggggg" +
                             " veeeeeerrrryyyyy lonngggggggggggg" +
                             "veeeeeerrrryyyyy lonngggggggggggg" +
                             " veeeeeerrrryyyyy lonngggggggggggg" +
                             " veeeeeerrrryyyyy lonngggggggggggg" +
                             " veeeeeerrrryyyyy lonngggggggggggg" +
                             " veeeeeerrrryyyyy lonngggggggggggg" +
                             " veeeeeerrrryyyyy lonngggggggggggg" +
                             " veeeeeerrrryyyyy lonngggggggggggg" +
                             " veeeeeerrrryyyyy lonngggggggggggg"
                             ) is False


# Description has to be longer than the product's title.
def test_r4_4_create_product():
    # return description without whitespace first
    assert check_description("test 4 ", " I love to describe things") \
           == "I love to describe things"
    # this fails because title>description
    assert check_description("super long title hdiwfjef eowjfoj",
                             "shortgtftdhsgcbfndjejw") is False


# Price has to be of range [10, 10000].
def test_r4_5_create_product():
    # these both work
    assert check_price(100) == 100
    assert check_price(100.0) == 100.0
    # returns false too big
    assert check_price(100000.0) is False
    # returns false too small
    assert check_price(2.0) is False
    # returns false not a float
    assert check_price("tt") is False


# last_modified_date must be after 2021-01-02 and before 2025-01-02.
def test_r4_6_create_product():
    # valid date returns date object, not false
    assert check_date("12-10-2021") is not False
    # returns false because too early
    assert check_date("12-10-2020") is False
    # returns false because too late
    assert check_date("12-12-2027") is False
    # returns false not a date
    assert check_date("bloop") is False


# owner_email cannot be empty. The owner of the
# corresponding product must exist in the database.
def test_r4_7_create_product():
    # check owner email, returns email because email exists
    # in db
    assert check_owner(seller_1.email) == seller_1.email
    # returns false because empty
    assert check_owner("") is False
    # returns false because it is not an email in db
    assert check_owner("nkjdsnv") is False
    # returns false not a float
    assert check_price("tt") is False


# A user cannot create products that have the same title.
def test_r4_8_create_product():
    product_1.set_title("test2")
    # fails because test2 is already a title
    assert check_title("test2") is False

# Backend testing for Sprint 6


def test_r6_1_buy_product():
    # Add user to database
    db.session.rollback()
    db.session.add(buyer_1)
    db.session.commit()

    # User must be able to place an order on valid products
    buy_product(product_1, seller_1, buyer_1)
    # Buyer balance must be updated, and the product information as well
    assert buyer_1.balance == 500
    assert product_1.isSold
    assert product_1.buyer_email == "scroogemc@duckmail.com"


def test_r6_2_buy_product():
    # User cannot order their own product
    # The following call must return False, only condition that can
    # trigger this would be owner buying their own product.
    assert buy_product(product_cheap, seller_1, seller_1) is False
    # To be sure, make sure the product's status hasn't changed
    assert product_cheap.isSold is False


def test_r6_3_buy_product():
    # User cannot order anything that costs more than their balance
    # Only failure consition here is that the product is too expensive for
    # User object buyer_1 to purchase
    assert buy_product(product_expensive, seller_1, buyer_1) is False
    assert product_expensive.isSold is False
