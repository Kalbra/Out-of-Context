from flask import request, jsonify
from flask_restful import Resource, Api

from api.auth import check_cookie
from api.models.models import Quote, Teacher
from api.models.base import db


class QuoteQuery(Resource):
    @check_cookie
    def get(self, instance_id):
        quotes = Quote.query.filter(Quote.approved == True).limit(100).all()
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
    @check_cookie
    def post(self, instance_id):
        try:
            data = request.get_json()
        except Exception as e:
            response = jsonify({"message": "Invalid JSON data", "error": str(e)})
            response.status = 400
            return response

        try:
            teacher_id = int(data["teacher_id"])
            quote = data["quote"]
            print(quote)

            if teacher_id and quote:
                teacher = Teacher.query.get(teacher_id)

                db.session.add(Quote(teacher_id=teacher_id, quote=quote, teacher=teacher, instance_id=instance_id))
                db.session.commit()

        except KeyError as e:
            response = jsonify({"message": "Not all parameters are provided correctly", "error": str(e)})
            response.status = 400
            return response
        except ValueError as e:
            response = jsonify({"message": "Not all paraemters are provided as correct type", "error": str(e)})
            response.status = 400
            return response

        response = jsonify({
            'message': 'Data received',
            'data': data
        })
        response.status = 201
        return response
