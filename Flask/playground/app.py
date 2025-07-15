from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "<b>My first flask application in action!</b>"