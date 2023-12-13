"""Flask app for Flask Notes"""

import os

from flask import Flask, url_for, redirect, render_template, flash, session
from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, User
from forms import RegisterForm, LoginForm, CSRFProtectForm

from sqlalchemy.exc import IntegrityError

# from models import db, connect_db, Cupcake, DEFAULT_IMG_URL TODO: remove

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", 'postgresql:///flask_notes')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
# app.config['WTF_CSRF_ENABLED'] = False

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
        # TODO: too opaque, better to be more explicit 
        # - username = form.data['username']
        data = {k: v for k, v in form.data.items() if k != "csrf_token"}
        print("user_signup_data: ", data)
        new_user = User.register(**data)
        
        try:
            #TODO: pinpoint where Int error may happen, and then only include in t/c 
            db.session.add(new_user)
            db.session.commit()
            session["user_id"] = new_user.username #TODO: change user_id to be GLOBAL_CONST = "user_id/username"
            flash(f"Welcome {new_user.username}!")
            return redirect(url_for('show_user', username=new_user.username))

        except IntegrityError:
            flash("Username/Email already exists.")
            return render_template("user_register_form.html", form=form)

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
        name = form.username.data #TODO: name -> username
        pwd = form.password.data

        user = User.authenticate(name, pwd)

        if user:
            # on successful login, redirect to user page

            session["user_id"] = user.username

            flash(f"Login successful! Welcome {user.username}!")
            return redirect(url_for('show_user', username=user.username))

        else:
            # re-render the login page with an error
            form.username.errors = ["Bad name/password"]

    return render_template("user_login_form.html", form=form)


@app.get("/users/<username>")
def show_user(username):
    """Show information about the given user"""

    if 'user_id' not in session or session['user_id'] != username:
        flash("You must be logged in to view!") #TODO: Do we want to show this? if user is trying 
        return redirect("/")

    else:
        user = User.query.get_or_404(username)
        form = CSRFProtectForm()

        return render_template("user_detail.html", user=user, form=form)


@app.post('/logout')
def logout():
    """Logs user out and redirects to homepage."""

    form = CSRFProtectForm()

    if form.validate_on_submit():
        # Remove "user_id" if present, but no errors if it wasn't
        session.pop("user_id", None) 

    return redirect("/")
