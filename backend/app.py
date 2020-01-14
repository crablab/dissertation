from flask import Flask, request, jsonify
from flask_cors import CORS

# Flask Set Up
app = Flask(__name__)
CORS(app)

@app.route("/ping")
def handlePing():
    return jsonify({"ping": "pong"})

if __name__ == '__main__':
    app.run(host='0.0.0.0')