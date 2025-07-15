from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "<b>My first flask application in action!</b>"

@app.route('/json')
def json_route():
    return jsonify(message="Hello World")