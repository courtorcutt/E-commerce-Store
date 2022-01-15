from flask import request, \
    render_template, redirect, \
    flash, session
from . import db
from .models import User, Product
from .productMethods import update_product, create_product, buy_product
from .userDataAccess import search_user
from .userMethods import register, update, login
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import and_
# from datetime import datetime

from qbay import app


def authenticate(inner_function):
    def inner():
        # check did we store the key in the session
        if 'user_logged_in' in session:
            user_email = session['user_logged_in']
            try:
                user = search_user(user_email)
                if user:
                    # if the user exists, call the inner_function
                    # with user as parameter
                    return inner(user)
            except Exception:
                pass
        else:
            # else, redirect to the login page
            return redirect('/login')

        return inner_function(user)

    # return the wrapped version of the inner function:
    inner.__name__ = inner_function.__name__
    return inner


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    # If already logged in, return to profile page
    if 'user_logged_in' in session:
        return redirect('/profile', code=303)
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = login(email, password)

        if user:
            # Log in was successful, store the email in session
            session['user_logged_in'] = user.email

            # success! go to the user's index page
            # code 303 is to force a 'GET' request
            return redirect('/profile', code=303)
        else:
            return render_template('login.html', message='Login Failed.')

    # if this runs then its a get request.
    return render_template('login.html', message='Please Login:')


@app.route('/profile', methods=['GET'])
@authenticate
def profile_page(user):
    return render_template('profile.html', user=user)


@app.route('/update-profile', methods=['GET', 'POST'])
@authenticate
def update_profile_page(user):
    if request.method == 'GET':
        return render_template('update-profile.html', user=user)

    if request.method == 'POST':
        user_name = request.form.get("user_name")
        shipping_address = request.form.get("shipping_address")
        postal_code = request.form.get("postal_code")

        if not user_name and not shipping_address and not postal_code:
            flash('Nothing entered', category='error')
            return redirect("/update-profile")

        if update(email=user.email, user_name=user_name,
                  shipping_address=shipping_address,
                  postal_code=postal_code):
            flash('Update successful!')
        else:
            flash('Something went wrong', category='error')

        return redirect("/profile")


@app.route("/register", methods=['GET', 'POST'])
def register_page():
    if request.method == 'POST':

        # get all the needed form inputs
        # the rest don't need to be initialized
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        email = request.form.get("email")
        user_name = request.form.get("user_name")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        # first check if user entered an email
        # that already exists
        email_exists = User.query.filter_by(email=email).first()
        username_exists = User.query.filter_by(user_name=user_name).first()

        if not first_name:
            flash('First name required',
                  category='error')

        elif not last_name:
            flash('Last name required',
                  category='error')

        elif not email:
            flash('Email required',
                  category='error')

        elif not user_name:
            flash('Username required',
                  category='error')

        elif not last_name:
            flash('Last name required',
                  category='error')

        elif not password1:
            flash('Password required',
                  category='error')

        elif not password2:
            flash('Please confirm password',
                  category='error')

        elif email_exists:
            flash('Email is already connected to an account. '
                  'Please log in.',
                  category='error')

        elif username_exists:
            flash('Username is already connected to an account. '
                  'Please choose another.',
                  category='error')

        elif password1 != password2:
            flash('Passwords are not the same',
                  category='error')

        elif len(user_name) < 2 or len(user_name) > 20:
            flash('Username must be between 2 and 20 characters.',
                  category='error')

        elif len(password1) < 6:
            flash('The password must be at least 6 characters.',
                  category='error')

        else:
            # validate that email, password, and username
            # all meet customer wants such as:
            user_name_validated = User.validate_username(user_name)
            email_validated = User.validate_user_email(email)
            password_validated = User.validate_password(password1)

            if register(first_name=first_name, last_name=last_name,
                        email=email_validated, user_name=user_name_validated,
                        password=password_validated):
                flash('You have been successfully registered with Qbay!')
                session['user_logged_in'] = email_validated
                return redirect("/profile")
            else:
                flash('Something went wrong', category='error')
                return redirect("/register")

    # if method is GET, by default
    return render_template("register.html")


# get function for product page
@app.route('/products', methods=['GET'])
@authenticate
def product_home_get(user):
    # for testing purposes only
    # This will be fixed when create product is made
    if not (Product.query.filter_by(owner_email=user.email).first()):
        return redirect("/create_product")
    # find all products that current user is selling
    products = Product.query.filter_by(owner_email=user.email).all()
    products2 = Product.query.filter_by(buyer_email=user.email).all()
    if (Product.query.filter_by(buyer_email=user.email).first()):
        message2 = "Here are all the products you bought"
    else:
        message2 = ""
    message = "Here are all of your products"
    return render_template('products.html', user=user,
                           products=products, message=message,
                           products2=products2, message2=message2)


# post function for product page
@app.route('/products', methods=['POST'])
@authenticate
def product_home_post(user):
    # get the info from the form
    product_id = request.form.get("id")
    curr = Product.query.filter_by(id=product_id).first()
    product_email = session['user_logged_in']
    # if the id to update belongs to a user product proceed
    if curr and product_email == curr.owner_email and not curr.isSold:
        # get form fields
        title = request.form.get("title")
        description = request.form.get("description")
        p_type = request.form.get("type")
        price = request.form.get("price")
        up_status = None
        # update all
        if title and p_type and price and description:
            up_status = update_product(curr, str(title), str(p_type),
                                       float(price), str(description))
        else:
            # update individually
            if title:
                up_status = curr.set_title(str(title))
            if p_type:
                if not up_status:
                    up_status = curr.set_type(str(p_type))
                else:
                    up_status += curr.set_type(str(p_type))
            if description:
                if not up_status:
                    up_status = curr.set_description(str(description))
                else:
                    up_status += curr.set_description(str(description))
            if price:
                if not up_status:
                    up_status = curr.set_price(float(price))
                else:
                    up_status += curr.set_price(float(price))

        db.session.commit()
        # if no error is returned it worked
        if not up_status:
            flash('Update Successful')
            return redirect("/products")
        else:
            # return the error
            flash(up_status, category='error')
            return redirect("/products")
    else:
        # invalid id was entered
        flash('INVALID ID', category='error')
        return redirect("/products")


@app.route('/buy_product', methods=['GET'])
@authenticate
def product_buy_get(user):
    userMail = session['user_logged_in']
    # find all products that other users are selling
    check = False
    if not (Product.query.filter(and_(Product.owner_email != userMail,
                                      Product.isSold == check)).first()):
        message = "No Products for Sale :("
    else:
        message = "Products for Sale"
    products = Product.query.filter(and_(Product.owner_email != userMail,
                                         Product.isSold == check)).all()

    return render_template('buy_product.html', user=user,
                           products=products, message=message)


# post function for buying products
@app.route('/buy_product', methods=['POST'])
@authenticate
def product_buy_post(user):
    # get the info from the form

    product_id = request.form.get("id")
    curr = Product.query.filter_by(id=product_id).first()
    if (curr):
        buyer_email = session['user_logged_in']
        seller_email = curr.owner_email
        owner = User.query.filter_by(email=seller_email).first()
        buyer = User.query.filter_by(email=buyer_email).first()
        if owner.email != buyer.email:
            if(not curr.isSold):
                if owner.balance >= curr.price:
                    buy_product(curr, owner, buyer)
                    db.session.commit()
                else:
                    flash('Balance too low', category='error')
                    return redirect("/buy_product")
            else:
                flash('Product already sold! :|', category='error')
                return redirect("/buy_product")
        else:
            flash('You can\'t buy your own product :|', category='error')
            return redirect("/buy_product")
    else:
        flash('INVALID ID', category='error')
        return redirect("/buy_product")

    success = 'You bought product ' + product_id
    flash(success)

    return redirect("/products")


@app.route("/create_product", methods=['GET', 'POST'])
@authenticate
def creation_update(user):
    if request.method == 'GET':
        return render_template("create_product.html")
    if request.method == 'POST':
        title = request.form.get("title")
        price = request.form.get("price")

        # Note that owner_email is not
        # included since we pass owner_email as a parameter
        # using User class
        description = request.form.get("description")
        last_modified_date = request.form.get("date")
        user_email = session['user_logged_in']
        new_product = create_product(str(title), str(description),
                                     float(price), str(last_modified_date),
                                     user_email)
        if new_product is not False:
            flash('You have successfully created a new product!')
            db.session.add(new_product)
            db.session.commit()
            return redirect("/products")
        else:
            flash('TRY AGAIN WRONG INPUT', category='error')
            return redirect("/create_product")


@app.route('/product_update', methods=['GET'])
def product_update_get():
    product_id = session['product_selected']
    curr = Product.query.filter_by(id=product_id).first()
    message = "Update page loaded success"
    return render_template('product_update.html',
                           product_c=curr, message=message)


@app.route('/product_update', methods=['POST'])
def product_update_post():
    product_id = session['product_selected']
    curr = Product.query.filter_by(id=product_id).first()
    title = request.form.get("title")
    description = request.form.get("description")
    p_type = request.form.get("type")
    price = request.form.get("price")
    flash(curr.title, category='error')
    up_status = update_product(curr, str(title), str(p_type),
                               float(price), str(description))
    db.session.commit()
    return redirect('/products')


@app.route("/")
def redirect_to_home():
    return redirect('/home')


@app.route("/home")
def home():
    # Talia's & Brandon's Code here
    return render_template("home.html")


@app.route('/logout')
def logout():
    if 'user_logged_in' in session:
        session.pop('user_logged_in', None)
    return redirect('/home')
