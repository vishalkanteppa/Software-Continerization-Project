"""
from pymongo import MongoClient

def post_post(post_content):

def get_post(post_id):
"""

import time
import os
# from pymongo import MongoClient
from flask import Flask, request, jsonify, render_template
from bson import json_util

# mongodb_username = os.getenv("MONGODB_USERNAME")
# mongodb_password = os.getenv("MONGODB_PASSWORD")

# CONNECTION_STRING = "mongodb://" + mongodb_username + ":" + mongodb_password + "@database:27017"

print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")

# client = MongoClient(CONNECTION_STRING, serverSelectionTimeoutMS=5000)

# try:
#     print(client.server_info())
# except Exception:
#     print("Unable to connect to the server.")

# db = client["posts_db"]
# posts_collection = db["posts"]

api = Flask(__name__)

@api.get("/new_posts")
def list_top_posts():
	#TODO sort

	result = []

	print(1)

	# for post in posts_collection.find().sort("time", -1):
	# 	print(post)
	# 	result.append(post)
	return render_template("new_posts.html")
	return json_util.dumps(result)


@api.get('/all_posts')
def show_all_posts():
	return "A work in progress"

@api.post("/create_new_post")
def create_new_post():
	request_data = request.form()

	print("AAAAAAAAAAAAAA")
	print(request_data)


	#TODO data validation

	post_data = {
		"name": request_data["name"],
		"content": request_data["content"],
		"time": time.time()
	}

	# post_id = posts_collection.insert_one(post_data).inserted_id

	# print(post_id)

	return jsonify({"success": True, "post_id": str(post_id)})

if __name__ == "__main__":
    api.run(host='0.0.0.0', port=1337, debug=True, threaded=True)
