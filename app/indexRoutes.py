from app import application, db, key
from flask import request, jsonify, Response, make_response, send_from_directory
import datetime


@application.route("/", methods=["GET"])
def home():
    return "<h1>404 Not Found</h1>"


@application.route("/staticFiles/<path:path>", methods=["GET"])
def send_static(path):

    return send_from_directory("../static", path)
