# the combined entities
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from email_validator import validate_email, EmailNotValidError
import re
from . import db

db.create_all()


# user class
class User(db.Model):
    # primary key, not set by user
    id = db.Column(db.Integer, primary_key=True)
    ''' the following attributes are able to be changed by the
        user on sign up or in account settings '''
    first_name = db.Column(db.String(80), unique=True, nullable=False)
    last_name = db.Column(db.String(80), unique=True, nullable=False)
    user_name = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)

    # address will likely need to be changed to
    # its own class later, modifiable by user
    shipping_address = db.Column(db.String(120), nullable=True)
    postal_code = db.Column(db.String(6), nullable=True)
    ''' the following attributes are not available from the
        front end for the user to modify on sign-up '''
    # i.e. if a user wants to be verified or create a seller account,
    # they must apply through a separate process
    userIsSeller = db.Column(db.Boolean, nullable=True, default=False)

    # verified buyer category for the rating system (default not verified)
    userIsVerified = db.Column(db.Boolean, nullable=True, default=False)

    # cannot be modified
    dateJoined = db.Column(db.DateTime, nullable=True,
                           default=datetime.utcnow)

    # user can add balance through a separate FE process
    balance = db.Column(db.Float, nullable=True, default=100)

    # seller rating will start as null, and only be initialized
    # to an integer once a user makes their first sale
    sellerRating = db.Column(db.Integer, nullable=True)

    # this relationship saves transaction for buyer users
    transactions_buyer = db.relationship(
        'Transaction',
        backref='buyer',
        lazy=True,
        foreign_keys="Transaction.user_email")

    # this relationship saves transaction for seller users
    transactions_seller = db.relationship(
        'Transaction',
        backref='seller',
        lazy=True,
        foreign_keys="Transaction.seller_email")

    user_emails = db.relationship(
        'Review',
        backref='user_review',
        lazy=True,
        foreign_keys="Review.user_email")

    def __repr__(self):
        return '<User %r: %r>' % (self.user_name, self.email)

    # alternate way of displaying
    # def __repr__(self):
    # return "<username {}, id {}>".format(self.username, self.id)

    def __str__(self):
        return 'User named {self.firstName} {self.lastName}'.format(self=self)

    def __eq__(self, other):
        return self.email == other.email

    def validate_password(password):
        # R1-4 Password has to meet the required complexity:
        # minimum length 6, at least one upper case,
        # at least one lower case, and at least one special character.
        if not password:
            return False

        if not re.fullmatch('^(?=.{6,}$)(?=.*?[a-z])(?=.*?[A-Z])'
                            '(?=.*?[#?!@$%^&*-]).*$', password):
            print("Password does not meet complexity requirements")
            return False

        length = len(password)
        if length < 6:
            print("\n The password must be at least 6 characters.")
            return False

        return password

    def validate_user_email(email):
        # R1-3 The email has to follow addr-spec defined in RFC 5322
        if not email:
            return False
        try:
            validate_email(email)
        except EmailNotValidError as e:
            print(str(e))
            return False

        return email

    # postal code must be valid Canadian postal code
    def validate_postal_code(postal_code):
        if not re.fullmatch('^[ABCEGHJ-NPRSTVXY]\d[ABCEGHJ-NPRSTV-Z]'
                            '[ -]?\d[ABCEGHJ-NPRSTV-Z]\d$', postal_code):
            print("Postal code not valid")
            return False

        return postal_code

    def validate_username(username):
        # R1-5 check if username is empty
        if not username:
            print("\n The username cannot be empty.")
            return False

        # R1-5 check if username has prefix of a space
        if username.startswith(" ", 0):
            print("\n Your username must not start with a space character")
            return False

        # R1-5 check if username has suffix of a space
        # GO OVER!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        if username.endswith(" "):
            print("\n Your username must not end with a space character")
            return False

        # R1-5 check if username is empty
        if (not (username and not username.isspace())):
            return False

        # R1-5 the username must be alphanumeric-only
        nospace = username.replace(" ", "")
        if not nospace.isalnum():
            print("\n This title can only contain alphabet "
                  "letters (a-z) and numbers (0-9)")
            return False

        # R1-6 must be of length between 2 and 20 characters
        length = len(username)
        if length < 2 or length > 20 or length == 0:
            print("\n The username must be between 2 and 20 characters long")
            return False

        return username

    def validate_shipping_address(shipping_address):
        # R1-5 check if shipping address is empty
        if not shipping_address:
            print("\n The shipping address cannot be empty.")
            return False

        nospace = shipping_address.replace(" ", "")
        # R1-5 the username must be alphanumeric-only
        if not nospace.isalnum():
            print("\n The shipping address can only contain "
                  "alphabet letters (a-z) and numbers (0-9)")
            return False

        return shipping_address

    def validate_balance(balance):
        # balance can't be negative or empty
        if not balance:
            print("\n The balance cannot be empty.")
            return False

        if balance < 0:
            print("\n Balance cannot be negative")
            return False

        return balance


"""    def set_username(self, value):
        value = self.validate_username(value)

        # R1-5 check if username is empty
        if not value:
            print("\n The username cannot be empty.")
            return False;"""

""" def set_email(self, value):
        # R1-3 the email must be of RFC 5322 standards
        # R1-7 email must be unique or it will fail
        value = validate_email(value)

        # R1-1 check if email is empty
        if not value:
            print("\n The email cannot be empty.")
            return False;"""

"""def set_password(self, value):
        # R1-4 meet the required complexity:
        minimum length 6, at least one upper case,
        # at least one lower case, and at least one special character.
        value = validate_password(value)

        # R1-1 check if email is empty
        if not value:
            print("\n The password cannot be empty.")
            return False"""


# product class
class Product(db.Model):
    """Data model for products being sold on the site"""
    id = db.Column(db.Integer, primary_key=True)
    # Explanations of the following attributes in order:
    # product_name - The name of the product being sold.
    # product_type - The type of product being sold.
    # owner_email - The email of the user who is selling the product.
    # buyer_email - The email of the buyer of the product
    # price - The listed price
    # isSold - Boolean that keeps track if the product was sold
    # average_rating - The average rating given by reviews.
    # description - A description of the product written by the seller.
    # product_review - A description of products from buyers
    title = db.Column(db.String(80), nullable=False, unique=True)
    product_type = db.Column(db.String(25), nullable=True)
    owner_email = db.Column(db.String(80), db.ForeignKey(
        'user.email'), nullable=False)
    buyer_email = db.Column(db.String(80), nullable=True)
    price = db.Column(db.Float, unique=False, nullable=False)
    isSold = db.Column(db.Boolean, nullable=False, default=False)
    average_rating = db.Column(db.Float, nullable=True)
    description = db.Column(db.String(2000), nullable=False)
    last_modified_date = db.Column(db.DateTime(80),
                                   unique=False,
                                   nullable=False)
    product_review = db.Column(db.String(2000), nullable=True)
    # the same product can have many transactions
    # this saves all transactions involving this product
    transactions = db.relationship(
        'Transaction',
        backref='product_transactions',
        lazy=True,
        foreign_keys="Transaction.product_id")

    def __repr__(self):
        """Returns basic identifying information of the Product"""
        return 'Product: ' + self.title \
               + '\nPrice: ' + str(self.price) \
               + '\nRating: ' + str(self.average_rating) \
               + '\nSold by: ' + self.owner_email

    # set title
    def set_title(self, value):
        # check if data is valid
        value = check_title(value)
        # if not return false
        if not value:
            return "\nThe title is not valid"
        # set the new title
        self.title = value
        # update last_modified_date
        self.last_modified_date = datetime.utcnow()
        db.session.commit()
        return False

    # set price
    def set_price(self, value):
        # check if it is a valid price
        value = check_price(value)
        if not value:
            return "\nThe price is not valid"
        # check if new price is bigger than the current price
        if self.price <= value:
            self.price = value
            # update last_modified_date
            self.last_modified_date = datetime.utcnow()
            db.session.commit()
            return False
        else:
            return "\nThe price can't be lower than before"

    def set_type(self, value):
        if not isinstance(value, str):
            return "\nThe type is not valid"
            # remove whitespaces at beginning and end

        value = value.strip()
        # Check if too long or too short. Maximum length is 25 instead.
        if len(value) > 25 or len(value) == 0:
            return "\nThe type is not valid"
        # remove whitespaces to check if everything that remains
        # is alphanumeric
        nospace = value.replace(" ", "")
        if not nospace.isalnum():
            return "\nThe type is not valid"
        self.product_type = value
        self.last_modified_date = datetime.utcnow()
        return False

    # set description
    def set_description(self, value):
        # take in title to compare lengths
        value = check_description(self.title, value)
        if not value:
            return "\nThe description is not valid"
        self.description = value
        # update last_modified_date
        self.last_modified_date = datetime.utcnow()
        db.session.commit()
        return False

    # function to sell a product
    def sell(self, value):
        # set to sold
        self.isSold = True

        # set buyer email
        self.buyer_email = value

        # update last_modified_date
        self.last_modified_date = datetime.utcnow()
        db.session.commit()
        return True


# check title
def check_title(title1):
    # check if input is string type
    if not isinstance(title1, str):
        print("\nThis title is not a string")
        return False
    # remove whitespaces at beginning and end
    title1 = title1.strip()
    length = len(title1)
    # check if too long or too short
    if length > 80 or length == 0:
        print("\nTitle must be <=80 and >0")
        return False
    # remove whitespaces to check if everything that remains
    # is alphanumeric
    nospace = title1.replace(" ", "")
    if not nospace.isalnum():
        print("\nThis title can contain spaces" +
              " alphanumerical characters only")
        return False
    # check if this title already exists
    if Product.query.filter_by(title=title1).all():
        print("\nThis title already exists.")
        return False
    return title1


# check description
def check_description(title, description):
    # check if input is string type
    if not isinstance(description, str):
        print("\nDescription not a string")
        return False
    # remove whitespaces at beginning and end
    description = description.strip()
    title = title.strip()
    length1 = len(title)
    length2 = len(description)
    # check if too long
    if length1 > length2:
        print("\nTitle is longer than description")
        return False
    # check length boundaries
    if length2 < 20 or length2 > 2000:
        print("\nDescription must be <=2000 and >=20")
        return False
    # if it passed everything return the description
    return description


# check price
def check_price(cost):
    # check if input is string type
    if not isinstance(cost, float) and not isinstance(cost, int):
        print("\nPrice is not a float")
        return False
    # check boundaries
    if cost < 10 or cost > 10000:
        print("\nPrice must be >=10 and <=10000")
        return False
    return cost


# check date
def check_date(date):
    try:
        # take in string input dd-mm-yyyy
        date_object = datetime.strptime(date, '%d-%m-%Y')
        date1 = "02-01-2025"
        date2 = "02-01-2021"
        # create upper and lower boundaries
        upperb = datetime.strptime(date1, '%d-%m-%Y')
        lowerb = datetime.strptime(date2, '%d-%m-%Y')
        # if date is below or above boundaries, false
        if date_object < lowerb or date_object > upperb:
            print("\nDate is too early or too late")
            return False
        # return datetime object if it worked
        return date_object
    # catch any formatting error or string that does not make sense
    except (ValueError, TypeError):
        print("\nNot a valid date")
        return False


# for owner email
def check_owner(owner_email):
    # remove any whitespaces from end or start
    owner_email = owner_email.strip()
    # if empty, no good
    if owner_email == "":
        print("\nempty owner email")
        return False
    # if it does not exist, bad email
    if not User.query.filter_by(email=owner_email).all():
        print("\nOwner does not exist")
        return False
    return owner_email


# for buyer email
def check_buyer(buyer_email):
    # remove any whitespaces from end or start
    buyer_email = buyer_email.strip()
    # if empty, no good
    if buyer_email == "":
        print("\nempty buyer email")
        return False
    # if it does not exist, bad email
    if not User.query.filter_by(email=buyer_email).all():
        print("\nBuyer does not exist")
        return False
    return buyer_email


# Transaction entity
class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # this is used in case a customer has an order containing multiple
    # transactions. Transactions are for each product
    # all transactions in one order will have the same batch_id
    batch_id = db.Column(db.Integer, unique=False, nullable=False)
    # product retrieves product id from a product object
    product_id = db.Column(db.Integer, db.ForeignKey(
        'product.id'), nullable=False)
    # seller_id retrieves user id from a user object
    seller_email = db.Column(db.String, db.ForeignKey(
        'user.email'), nullable=False)
    # buyer_id retrieves user id from a user object
    user_email = db.Column(db.String, db.ForeignKey(
        'user.email'), nullable=False)
    date = db.Column(db.DateTime(80), unique=False, nullable=False)
    # cost retrieves cost amount from a Product object
    price = db.Column(db.Float(80), db.ForeignKey(
        'product.price'), nullable=False)
    status = db.Column(db.String(80), unique=False, nullable=False)
    # in order to leave a product review they must be a user
    verified_user = db.Column(db.String(80))
    # transaction review of purchase
    purchase_review = db.Column(db.String, db.ForeignKey(
        'product.product_review'), nullable=True)
        
    # this describes how the objects in this class are printed
    def __repr__(self):
        return "<Transaction ID {}, Batch ID {}, Product ID {}, " \
               "Cost {}, Seller Email {}, Buyer Email {}, >".format(
                   self.id, self.batch_id,
                   self.product_id, self.price,
                   self.seller_email,
                   self.user_email)


# Review entity
class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # Explanations of the following attributes in order:
    # user_email - The email of the user leaving the review
    # score - The review score
    # review - The review description.

    user_email = db.Column(db.String(80), db.ForeignKey(
        'user.email'), nullable=False)
    score = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(2000), nullable=False)

    # this describes how the objects in this class are printed
    def __repr__(self):
        return "<Review ID {}, Score {}, " \
               "Review {}, User Email {}>".format(
                   self.id,
                   self.score,
                   self.review,
                   self.user_email)


# testing
"""
db.create_all()
# initialize objects
seller_1 = User(id=1, firstName="bobby", lastName="moo",
                user_name="Seller1", userIsSeller=True,
                email="blabla@gmail.com", password="corndog")
buyer_1 = User(id=2, firstName="bob", lastName="Ye",
               user_name="Buyer1", userIsSeller=False,
               email="blabla2@gmail.com", password="pa$$word")
buyer_2 = User(id=3, firstName="Tiffany", lastName="Chantale",
               user_name="Buyer2", userIsSeller=False,
               email="blabla3@gmail.com", password="schooool")
product_1 = Product(id=1, price=300.02, title="test",
                    description="This is a test",
                    last_modified_date=datetime.utcnow(),
                    owner_email=seller_1.email,
                    product_review="This is a test review!")
product_2 = Product(id=2, price=500.13, title="couch",
                    description="This is a couch",
                    last_modified_date=datetime.utcnow(),
                    owner_email=seller_1.email,
                    product_review="Don't buy this couch!")

transaction_1 = Transaction(batch_id="1", user_email=buyer_1.email,
                            seller_email=seller_1.email, status="Done",
                            date=datetime.utcnow(),
                            product_id=product_1.id, price=product_1.price,
                            verified_user="Yes",
                            purchase_review=product_1.product_review)
transaction_2 = Transaction(batch_id="1", user_email=buyer_1.email,
                            seller_email=seller_1.email, status="Failed",
                            date=datetime.utcnow(),
                            product_id=product_1.id, price=product_1.price,
                            verified_user="Yes")
transaction_3 = Transaction(batch_id="2", user_email=buyer_2.email,
                            seller_email=seller_1.email, status="Done",
                            date=datetime.utcnow(),
                            product_id=product_2.id, price=product_2.price,
                            verified_user="Yes",
                            purchase_review=product_2.product_review)
                            owner_email=seller_1.email)
transaction_1 = Transaction(batch_id="1", user_email=buyer_1.email,
                            seller_email=seller_1.email, status="Done",
                            date=datetime.utcnow(),
                            product_id=product_1.id, price=product_1.price)
transaction_2 = Transaction(batch_id="1", user_email=buyer_1.email,
                            seller_email=seller_1.email, status="Failed",
                            date=datetime.utcnow(),
                            product_id=product_1.id, price=product_1.price)
# add objects to database
db.session.add(buyer_1)
db.session.add(buyer_2)
db.session.add(seller_1)
db.session.add(transaction_1)
db.session.add(transaction_2)
db.session.add(transaction_3)
db.session.add(product_1)
db.session.add(product_2)
db.session.add(product_1)
db.session.commit()
# retrieve first user
user1 = User.query.first()
# search for user using id
user2 = User.query.get(2)
# print all users and transactions
print("\nUsers:")
print(User.query.all())
print("\nTransactions:")
print(Transaction.query.all())
# print seller and buyer id for transaction 1
print("\nSeller and Buyer Emails for transaction 1:")
print(transaction_1.seller_email)
print(transaction_1.user_email)
print("\nAll Transactions for seller 1:")
print(seller_1.transactions_seller)
print("\nAll Transactions for buyer 1:")
print(buyer_1.transactions_buyer)
print("\nAll Transactions for buyer 2:")
print(buyer_2.transactions_buyer)
print("\nAll Transactions for Product 1:")
print(product_1.transactions)
print("\nCost for Transaction 1:")
print(transaction_1.price)
print("\nProduct Review for Transaction 3:")
print(transaction_3.purchase_review)
print("\nAll Transactions from the same batch (same order):")
print(Transaction.query.filter_by(batch_id=1).all())
"""
