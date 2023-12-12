"""Flask app for Flask Notes"""

import os

from flask import Flask, redirect, render_template, flash, jsonify, request
from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db

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
    """Homepage: redirects to resgiter page."""

    return redirect("/register")

@app.route("/register")
def create_user():
    """GET: Shows a form that when submitted, will register/create a user.
        Form accepts:
            username
            password
            email
            first_name
            last_name
        POST: Processes the registration form by adding a new user.
            Redirects the user to their user page.
    """

    

@app.route("/login")
def login_user():
    """GET: Shows a login form for user.
        Form accepts:
            username
            password
        POST: Processes the login form, authenticates user.
            Redirects user to their user page, 
                or returns an invalid login message.
    """

