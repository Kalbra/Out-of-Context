from flask_restful import Resource, Api
from app import app

api = Api(app, prefix='/api')

class Test(Resource):
    def get(self):
        return [{
            "teacher_name": "Jörg Geßner",
            "quote": "Es irrt der Mensch solang er strebt.",
            "votes": 4,
            "creation_date": "13.12.2005",
            "voted": "down"
        },
            {
                "teacher_name": "Sabine Schulze",
                "quote": "Verpisst euch.",
                "votes": 300,
                "creation_date": "13.12.2335",
                "voted": "up"
            },
        ]


api.add_resource(Test, '/test')
