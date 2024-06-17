from .base import db, ma


class Quote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teacher.id'),
                           nullable=False)
    teacher = db.relationship('Teacher',
                              backref=db.backref('quotes', lazy=True))

    quote = db.Column(db.String(1000), nullable=False)
    votes = db.Column(db.Integer, nullable=False, default=0)

    def __repr__(self):
        return f'<Quote {self.quote}>'


class LittleQuoteSchema(ma.Schema):
    class Meta:
        fields = ('id', 'teacher_id', 'quote', 'votes')
        model = Quote


little_quotes_schema = LittleQuoteSchema(many=True)
