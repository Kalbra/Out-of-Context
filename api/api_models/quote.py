from flask_restful import Resource, Api

from api.models.teacher import Teacher
from api.models.quote import Quote, little_quotes_schema


class QuoteQuery(Resource):
    def get(self):
        quotes = Quote.query.limit(100).all()
        return little_quotes_schema.dump(quotes)
