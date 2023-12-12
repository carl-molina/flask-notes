"""Seed file for Flask Notes app."""

# noinspection PyUnresolvedReferences
from app import app
from models import db, User

db.drop_all()
db.create_all()

user_1 = User(
    username="test_user",
    password="test_pw",
    email="test_user@test.com",
    first_name="Bob",
    last_name="Test",
)

user_2 = User(
    username="test_user_2",
    password="test_pw",
    email="test_user_2@test.com",
    first_name="Hope",
    last_name="Test",
)


db.session.add_all([user_1, user_2])
db.session.commit()