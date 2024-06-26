from datetime import datetime, timezone

from .base import db

viewed_instance = db.Table('viewed_instance',
                           db.Column('quote_id', db.Integer(), db.ForeignKey('quote.id'), primary_key=True),
                           db.Column('instance_id', db.Integer(), db.ForeignKey('instance.id'), primary_key=True)
                           )


class Quote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teacher.id'),
                           nullable=False)

    teacher = db.relationship("Teacher", backref="quote")

    quote = db.Column(db.String(1000), nullable=False)
    votes = db.Column(db.Integer, nullable=False, default=0)

    created_instance_id = db.Column(db.Integer, db.ForeignKey('instance.id'))
    viewed_instances = db.relationship("Instance", secondary=viewed_instance, back_populates="viewed_quotes")

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

    # created_quotes = db.relationship('Quote', backref='instance')

    viewed_quotes = db.relationship("Quote", secondary=viewed_instance, back_populates="viewed_instances")


class ReactionLink(db.Model):
    discord_message_id = db.Column(db.Integer, primary_key=True)
    quote_id = db.Column(db.Integer, db.ForeignKey("quote.id"), nullable=False)

    quote = db.relationship("Quote", backref="reaction_link")
