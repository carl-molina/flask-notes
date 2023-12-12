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
    """Homepage: redirect to /###."""

    return redirect("/###")



# TODO: Part 3: Make routes for register/login