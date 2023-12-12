from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length, Email


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
        validators=[InputRequired(), Email()]
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
        validators=[InputRequired(), Length(min=4, max=20)]
    )

    password = PasswordField(
        "Password",
        validators=[InputRequired(), Length(min=10, max=100)]
    )


class CSRFProtectForm(FlaskForm):
    """Form just for CSRF Protection"""
    