from flask import Flask, request, jsonify
from flask_cors import CORS

# Flask Set Up
app = Flask(__name__)
CORS(app)