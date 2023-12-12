"""Models for Flask Notes app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """User."""

    __tablename__ = "users"

    __table_args__ = (
        db.UniqueConstraint("name", "description"),
    )

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True,
    )

    name = db.Column(
        db.String(50),
        nullable=False,
        unique=True,
    )

    description = db.Column(
        db.Text,
        nullable=False,
        default='',
    )

    def __repr__(self):
        return f"<{self.__class__.__name__} playlist.id={self.id}>"