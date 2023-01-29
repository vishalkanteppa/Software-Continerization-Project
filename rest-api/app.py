"""
from pymongo import MongoClient

def post_post(post_content):

def get_post(post_id):
"""

import time
import os
from pymongo import MongoClient
from flask import Flask, request, jsonify
from bson import json_util
import logging

mongodb_username = os.getenv("MONGO_INITDB_ROOT_USERNAME")
mongodb_password = os.getenv("MONGO_INITDB_ROOT_PASSWORD")

CONNECTION_STRING = "mongodb://" + mongodb_username + ":" + mongodb_password + "@db:27017"

print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")

client = MongoClient(CONNECTION_STRING, serverSelectionTimeoutMS=5000)

try:
    print(client.server_info())
    print("success connecting to db server")
except Exception:
    print("Unable to connect to the server.")

db = client["posts_db"]
posts_collection = db["posts"]

app = Flask(__name__)

gunicorn_error_logger = logging.getLogger('gunicorn.error')
app.logger.handlers.extend(gunicorn_error_logger.handlers)
app.logger.setLevel(logging.INFO)

@app.get("/new_posts")
def list_top_posts():
	#TODO sort

	result = []

	print(1)

	for post in posts_collection.find().sort("time", -1):
		print(post)
		result.append(post)

	return json_util.dumps(result)

@app.post("/create_new_post")
def create_new_post():
	request_data = request.get_json()

	print("AAAAAAAAAAAAAA")
	print(request_data)


	#TODO data validation

	post_data = {
		"name": request_data["name"],
		"content": request_data["content"],
		"time": time.time()
	}

	post_id = posts_collection.insert_one(post_data).inserted_id

	print(post_id)

	return jsonify({"success": True, "post_id": str(post_id)})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=1337, debug=True, threaded=True)