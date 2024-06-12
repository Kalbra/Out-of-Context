from flask_sqlalchemy import SQLAlchemy
from ..app import db


class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
