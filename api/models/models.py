from .base import db


class Quote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teacher.id'),
                           nullable=False)

    teacher = db.relationship("Teacher", backref="quote")

    quote = db.Column(db.String(1000), nullable=False)
    votes = db.Column(db.Integer, nullable=False, default=0)

    def __repr__(self):
        return f'<Quote {self.quote}>'


class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Teacher {self.name}>'