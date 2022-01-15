from qbay.models import (Product, check_title, check_description,
                         check_price, check_date, check_owner, check_buyer)
from qbay.userMethods import update_balance


def create_product(title, description,
                   price, last_modified_date, owner):
    """
    Creates a Product object given the non-nullable input parameters.
    Relies on the use of functions written in models.py which check values
    and ensure they meet requirements. Requirements which each check function
    tests for are included in comments above each function. The functions
    return False if the parameter does not meet requirements, and returns the
    requirement if it is acceptable.

    If all parameters are acceptable, create_product returns a Product object
    with attributes equal to the parameters passed to this function. If any
    parameter is deemed invalid, according to project requirements, this
    function returns False.
    """
    # R4-1: Title must be alphanumerical with no leading or trailing spaces.
    # R4-2: Title must be no more than 80 characters.
    # R4-8: A user cannot create products that have the same title.
    title = check_title(title)
    if not title:
        print("\n Title is invalid.")
        return False

    # R4-3: The length of description must be in range [20, 2000].
    # R4-4: Description has to be longer than the product's title.
    description = check_description(title, description)
    if not description:
        print("\n Description is invalid.")
        return False

    # R4-5: Price must be in range [10, 10000].
    price = check_price(price)
    if not price:
        print("\n Price is invalid.")
        return False

    # R4-6: last_modified_date must be after 2021-01-02 and before 2025-01-02.
    last_modified_date = check_date(last_modified_date)
    if not last_modified_date:
        print("\n Date is invalid.")
        return False

    # R4-7: owner_email cannot be empty. Owner must exist in the database.
    owner_email = check_owner(owner)
    if not owner_email:
        print("\n Owner email is invalid.")
        return False

    # If no return has been called, all values are valid.
    # Product will be initialized with all of the given parameters:

    this_product = Product(title=title, price=price,
                           description=description,
                           last_modified_date=last_modified_date,
                           owner_email=owner_email)

    return this_product


def update_product(self, title, product_type,
                   price, description):
    """
    Function updates the attributes of the Product given as the "self"
    parameter. This is done by calling set_[attribute] functions written
    in models.py. Attribute-setting functions check for input data that
    violates requirements. These functions return False if the given value
    is in violation of a requirement, or True if could successfully set the
    attribute to its new value.

    The owner_email, last_modified_date, average_rating, product_review, and
    transactions attributes cannot be modified by this function, as these are
    to be regulated by changes to, or the creation of, other objects.

    If any attribute is deemed invalid, update_product returns False without
    updating the attribute, or any attributes afterwards. Otherwise,
    update_product returns True.
    """

    # Update title, set_title in models.py calls check, so it will still be
    # checked for validity before the attribute is set to the new value.
    error_message = None
    title_success = self.set_title(title)
    if title_success:
        error_message = "\nThis title is wrong"

    # Update product_type.
    type_success = self.set_type(product_type)
    if type_success:
        if error_message is not None:
            error_message += "\nThe type is wrong"
        else:
            error_message = "\nThe type is wrong"

    # Update price of product. The set_price function checks for validity,
    # so just call that and check the result.
    price_success = self.set_price(price)
    if price_success:
        if error_message is not None:
            error_message += "\nThe price is wrong"
        else:
            error_message = "\nThe price is wrong"

    # Update description of the product. The set_description function checks
    # for validity, so just call that and check the result.
    description_success = self.set_description(description)
    if description_success:
        if error_message is not None:
            error_message += "\nThe description is wrong"
        else:
            error_message = "\nThe description is wrong"

    # With all changes accomplished without failure, return False
    return error_message


def buy_product(self, owner, buyer):
    """
    Owner and Buyer are user-type objects passed into the function.
    This is useful to verify emails and check if the buyer has
    enough money to buy the product.
    """

    # product can't be sold twice
    if self.isSold is True:
        print("\n Product cannot be sold twice")
        return False

    # R4-7: owner_email cannot be empty. Owner must exist in the database.
    owner_email = check_owner(owner.email)
    if not owner_email:
        print("\n Owner email is invalid.")
        return False

    # R4-7: buyer_email cannot be empty. Buyer must exist in the database.
    buyer_email = check_buyer(buyer.email)
    if not buyer_email:
        print("\n Buyer email is invalid.")
        return False

    if buyer_email == owner_email:
        print("\n Cannot buy your own product")
        return False

    # modifies the buyer user object to have
    # a new balance based on how much they are spending
    if not update_balance(buyer.email, buyer.balance - self.price):
        print("\n Updating balance failed")
        return False

    # modifies the product to be "sold" and adds the buyer email to it
    self.sell(buyer.email)
