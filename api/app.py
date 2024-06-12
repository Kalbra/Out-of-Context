from flask import Flask, render_template, make_response
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

from api.api_models.quote import Quote

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///demo.db'
db = SQLAlchemy(app)

api = Api(app, prefix='/api')
api.add_resource(Quote, '/quote')

"""
@app.before_request
def check_cookie():
    pass
"""

@app.route('/')
def home():
    resp = make_response(render_template('index.html'))
    resp.set_cookie('ooc_auth_indicator', "test")
    return resp

@app.route('/senden')
def senden():
    resp = make_response(render_template('senden.html'))
    return resp


if __name__ == '__main__':
    app.run()

