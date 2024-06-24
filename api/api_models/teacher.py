from flask import jsonify
from flask_restful import Resource

from api.auth import check_cookie
from api.models.models import Quote, Teacher


class TeacherList(Resource):
    @check_cookie
    def get(self, instance_id):
        teachers = Teacher.query.limit(10000).all()
        teacher_list = []
        for teacher in teachers:
            teacher_list.append(
                {
                    "id": teacher.id,
                    "teacher_name": teacher.name,
                }
            )
        return jsonify(
            {
                "quotes": teacher_list
            }
        )
