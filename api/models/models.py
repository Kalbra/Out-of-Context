import random
import string
from datetime import datetime, timezone

from .base import db


class Quote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teacher.id'),
                           nullable=False)

    teacher = db.relationship("Teacher", backref="quote")

    quote = db.Column(db.String(1000), nullable=False)
    votes = db.Column(db.Integer, nullable=False, default=0)

    instance_id = db.Column(db.Integer, db.ForeignKey('instance.id'))

    creation_date = db.Column(db.DateTime, nullable=False, default=datetime.now(tz=timezone.utc))

    approved = db.Column(db.Boolean, nullable=False, default=False)

    def __repr__(self):
        return f'<Quote {self.quote}>'


class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Teacher {self.name}>'


class Instance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    auth_token = db.Column(db.String(100), nullable=False)
    creation_date = db.Column(db.DateTime, nullable=False, default=datetime.now(tz=timezone.utc))

    quotes = db.relationship('Quote', backref='instance')

