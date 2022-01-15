from qbay.models import User, db


# inserts a user into the database, takes in a user type object
def insert_user(user):
    db.session.rollback()

    # number of users before insert
    before = len(User.query.all())

    db.session.add(user)
    try:
        db.session.commit()
    except Exception:
        return 0

    # number of users after insert
    after = len(User.query.all())

    # function will return 1 if insertion is successful and 0 if unsuccessful
    return after - before


def search_user(email):
    db.session.rollback()

    # simply return the user found by email
    user = User.query.filter_by(email=email).first()

    # note: will return None if user is None (not found)
    return user


def search_user_username(user_name):
    db.session.rollback()

    # simply return the user found by email
    user = User.query.filter_by(user_name=user_name).first()

    # note: will return None if user is None (not found)
    return user


def update_user(email, user_name, shipping_address, postal_code):
    db.session.rollback()

    # search for user to update
    currentUser = search_user(email)

    if currentUser is None:
        return False

    # only gives functionality to update the
    # three fields outlined in requirements
    currentUser.user_name = user_name
    currentUser.shipping_address = shipping_address
    currentUser.postal_code = postal_code

    db.session.commit()
    return True


def update_user_balance(email, new_balance):
    db.session.rollback()

    # search for user to update
    currentUser = search_user(email)

    if currentUser is None:
        return False

    # only updates balance
    currentUser.balance = new_balance

    db.session.commit()
    return True
