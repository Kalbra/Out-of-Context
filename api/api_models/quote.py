from flask import jsonify
from flask_restful import Resource, Api

from api.models.models import Quote


class QuoteQuery(Resource):
    def get(self):
        quotes = Quote.query.limit(100).all()
        quotes_list = []
        for quote in quotes:
            quotes_list.append(
                {
                    "id": quote.id,
                    "teacher_name": quote.teacher.name,
                    "quote": quote.quote,
                    "votes": quote.votes,
                    "voted": "down"
                }
            )
        return jsonify(
            {
                "quotes": quotes_list
            }
        )
