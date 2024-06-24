from flask import request, jsonify
from flask_restful import Resource, Api

from api.models.models import Quote, Teacher
from api.models.base import db


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


class NewQuote(Resource):
    def post(self):
        try:
            data = request.get_json()
        except Exception as e:
            return {"message": "Invalid JSON data", "error": str(e)}, 400

        try:
            teacher_id = int(data["teacher_id"])
            quote = data["quote"]

            if teacher_id and quote:
                teacher = Teacher.query.get(teacher_id)

                db.session.add(Quote(teacher_id=teacher_id, quote=quote, teacher=teacher))
                db.session.commit()
        except KeyError as e:
            return {"message": "Not all parameters are provided correctly", "error": str(e)}, 400
        except ValueError as e:
            return {"message": "Not all paraemters are provided as correct type", "error": str(e)}

        response = {
            'message': 'Data received',
            'data': data
        }
        return response, 201
