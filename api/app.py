from flask import Flask, render_template, make_response, g
from flask_restful import Api

from api.api_models.teacher import TeacherList
from api.auth import check_cookie
from api.models.base import db

from api.api_models.quote import QuoteQuery, NewQuote
from api.approve_bot import init_approve_bot

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///demo.db'

db.init_app(app)

init_approve_bot(app.app_context())

api = Api(app, prefix='/api')
api.add_resource(QuoteQuery, '/quote')
api.add_resource(NewQuote, '/new_quote')
api.add_resource(TeacherList, '/teacher_list')


@app.route('/')
@check_cookie
def home(instance_id):
    resp = make_response(render_template('index.html'))
    return resp


@app.route('/senden')
@check_cookie
def senden():
    resp = make_response(render_template('senden.html'))
    return resp


if __name__ == '__main__':
    app.run()
