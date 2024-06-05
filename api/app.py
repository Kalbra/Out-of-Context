from flask import Flask, render_template, make_response
from flask_restful import Resource, Api

app = Flask(__name__)


@app.before_request
def check_cookie():
    pass


@app.route('/')
def home():
    resp = make_response(render_template('index.html'))
    resp.set_cookie('ooc_auth_indicator', "test")
    return resp

@app.route('/senden')
def home():
    resp = make_response(render_template('index.html'))


if __name__ == '__main__':
    app.run()
