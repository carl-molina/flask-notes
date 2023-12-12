"""Flask app for Flask Notes"""

import os

from flask import Flask, url_for, redirect, render_template, flash, jsonify, request
from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, User, bcrypt
from forms import RegisterForm, LoginForm

# from models import db, connect_db, Cupcake, DEFAULT_IMG_URL

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", 'postgresql:///flask_notes')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

app.config['SECRET_KEY'] = "I'LL NEVER TELL!!"

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)


@app.get("/")
def root():
    """Homepage: redirects to register page."""

    return redirect("/register")

@app.route("/register", methods=["GET", "POST"])
def create_user():
    """GET: Shows a form that when submitted, will register/create a user.
        Form accepts:
            username
            password
            email
            first_name
            last_name
        POST: Processes the registration form by adding a new user to database.
            Redirects the user to their user page.
    """

    form = RegisterForm()

    if form.validate_on_submit():

        data = {k: v for k, v in form.data.items() if k != "csrf_token"}
        new_user = User(**data)

        db.session.add(new_user)
        db.session.commit()

        flash(f"Welcome {data['username']}!")

        return redirect(url_for('show_user'))

    else:
        return render_template("user_register_form.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login_user():
    """GET: Shows a login form for user.
        Form accepts:
            username
            password
        POST: Processes the login form, authenticates user.
            Redirects user to their user page,
                or returns an invalid login message.
    """

    form = LoginForm()

    if form.validate_on_submit():
        name = form.username.data
        pwd = form.password.data

        user = User.query.filter_by(username=name).one_or_none()

        if user and user.password == pwd:
            # on successful login, redirect to secret page
            flash(f"Login successful! Welcome {user.username}!")
            return redirect(url_for('show_user'))

        else:
            # re-render the login page with an error
            form.username.errors = ["Bad name/password"]

    return render_template("user_login_form.html", form=form)

