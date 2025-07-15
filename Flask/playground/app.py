from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "<b>My first flask application in action!</b>"

@app.route('/json')
def json_route():
    return jsonify(message="Hello World")

@app.route('/request')
def request():
    course = request.args["course"]
    rating = request.args.get("rating")
    return {"message": f"{course} with rating {rating}"}