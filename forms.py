from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length, Email
from email_validator import EmailNotValidError, EmailSyntaxError


class RegisterForm(FlaskForm):
    """Form for registering a user."""

    username = StringField(
        "Username",
        validators=[InputRequired(), Length(min=4, max=20)]
    )

    password = PasswordField(
        "Password",
        validators=[InputRequired(), Length(min=10, max=100)]
    )

    email = StringField(
        "Email",
        validators=[InputRequired(), Email()] #TODO: no longer than 50char
    )

    first_name = StringField(
        "First Name",
        validators=[InputRequired(), Length(min=1, max=30)]
    )

    last_name = StringField(
        "Last Name",
        validators=[InputRequired(), Length(min=1, max=30)]
    )


class LoginForm(FlaskForm):
    """Form for registering a user."""

    username = StringField(
        "Username",
        validators=[InputRequired(), Length(min=4, max=20)] #TODO: validators are a sec. issue if bots try to log in
    )

    password = PasswordField(
        "Password",
        validators=[InputRequired(), Length(min=10, max=100)]
    )


class CSRFProtectForm(FlaskForm):
    """Form just for CSRF Protection"""
