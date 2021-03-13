import datetime

from flask import current_app as app
from sqlalchemy.orm import relationship

from app import db

from .User import User


class News(db.Model):
    __tablename__ = "news"

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    title = db.Column(db.String(255), unique=True, nullable=False)
    body = db.Column(db.String(255), nullable=False)
    # user_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now(), nullable=False)
    updated_at = db.Column(
        db.DateTime, default=datetime.datetime.now(), onupdate=datetime.datetime.now()
    )

    # user = relationship('User', foreign_keys='News.user_id')

    def save(self):
        """ Shorthand method to update User object """
        db.session.add(self)
        db.session.commit()
