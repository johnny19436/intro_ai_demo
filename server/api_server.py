import requests
import json
import os

from flask import Flask, jsonify
from flask import request
from flask_restful import Resource, Api
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

api = Api(app)


n = 0

@app.route("/")
def home():
    return "Home"

@app.route("/search", methods=["POST"])
def search():
  # Get the search string from the request
  # The POST request will send a json file:
  # {
  #     search_string: "the cheapest refrigerator in the appliance list",
  # }
  search_term = request.get_json().get("search_string")
  
  # Simulate some processing on the search term
  # (Replace this with your actual search logic)
  processed_term = search_term.upper()

  # Prepare a sample JSON response
  response = {
    "search_string": search_string,
    "top_three_items": [],
    "image_url": "https://www.google.com/",
  }

  return jsonify(response)


if __name__ == '__main__':
    app.run(host="localhost", port=4000, debug=True)