from flask_sqlalchemy import SQLAlchemy
from ..app import db


class Quote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teacher.id'),
                           nullable=False)
    teacher = db.relationship('Teacher',
                              backref=db.backref('quotes', lazy=True))

    quote = db.Column(db.String(1000), nullable=False)
    votes = db.Column(db.Integer, nullable=False, default=0)
