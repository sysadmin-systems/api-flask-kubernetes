from flask import Flask
from flask.json import jsonify
app = Flask(__name__)

@app.route("/")
def hello_world():
    return jsonify(hello="world")