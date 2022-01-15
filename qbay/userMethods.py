from qbay.models import User
from qbay.userDataAccess import insert_user, search_user, \
    update_user, update_user_balance


def register(first_name, last_name, user_name, email, password):
    # R1-3 the email must be of RFC 5322 standards
    # R1-7 email must be unique or it will fail
    email = User.validate_user_email(email)

    # R1-1 check if email is empty
    if not email:
        print("\n The email cannot be empty.")
        return False

    # R1-7 If the email has been used, the operation failed.
    # check if email has already been used
    if search_user(email):
        print("\nThis email already exists.")
        return False

    # R1-4 meet the required complexity: minimum
    # length 6, at least one upper case,
    # at least one lower case, and at least one special character.
    password = User.validate_password(password)

    user_name = User.validate_username(user_name)

    # R1-1 check if email is empty
    if not user_name:
        print("\n The username cannot be empty.")
        return False

    # R1-1 check if email is empty
    if not password:
        print("\n The password cannot be empty.")
        return False

    new_user = User(first_name=first_name, last_name=last_name,
                    email=email, user_name=user_name,
                    password=password, balance=100)

    # operation failed
    if insert_user(new_user) == 0:
        return False
    return True


# function for user login
def login(email, password):
    # search for user in db
    user = search_user(email)
    if user:
        # Found a User with the given email
        # check if the user password matches
        if user.password == password:
            return user
    # If we reach here, then either the user does not exist
    #  or the password was incorrect
    return None


def update(email, user_name, shipping_address, postal_code):
    # validate user name
    user_name = User.validate_username(user_name)
    if not user_name:
        return False

    # validate address
    shipping_address = User.validate_shipping_address(shipping_address)
    if not shipping_address:
        return False

    # validate postal code
    postal_code = User.validate_postal_code(postal_code)
    if not postal_code:
        return False

    # update user
    if not update_user(email, user_name, shipping_address, postal_code):
        # if it doesn't work, return false
        return False

    # it worked, return True!
    return True


def update_balance(email, balance):

    # validate balance (not negative)
    balance = User.validate_balance(balance)
    if not balance:
        return False

    # update user's balance
    if not update_user_balance(email, balance):
        # if it doesn't work, return false
        return False

    # it worked, return true!
    return True
