import time
import os
# from pymongo import MongoClient
from flask import Flask, request, jsonify, render_template
# from bson import json_util

print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")


api = Flask(__name__)

@api.get("/new_posts")
def list_top_posts():
	#TODO sort

	result = []

	print(1)

	return render_template("new_posts.html")


@api.get('/all_posts')
def show_all_posts():
	return "A work in progress"


if __name__ == "__main__":
    api.run(host='0.0.0.0', port=1338, debug=True, threaded=True)
