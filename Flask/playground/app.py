from flask import Flask, jsonify, request
import requests

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

@app.route('/sampleapicall')
def sample_api_call():
    response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
    if response.status_code == 200:
        print("SUCCESS")
        return jsonify(response.json())
    elif response.status_code == 404:
        return jsonify(message="something went wrong"), 404
    else:
        return jsonify(message="server error"), 500