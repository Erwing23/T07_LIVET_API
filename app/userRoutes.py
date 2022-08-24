from app import application, db
from flask import request, jsonify, Response
from bson import json_util, objectid


@application.route("/users", methods=["POST"])
def create_User():
    # Recieving Data
    name = request.json["name"]
    rol = request.json["rol"]
    email = request.json["email"]
    gender = request.json["gender"]
    age = request.json["age"]

    if name and rol and email and gender and age:
        user = {"name": name, "rol": rol, "email": email, "gender": gender, "age": age}
        response = json_util.dumps(user)
        db.users.insert_one(user)

        return response
    else:
        return {"message": "Failed"}


@application.route("/users", methods=["GET"])
def get_Users():

    # Recieving Data
    users = db.users.find()
    response = json_util.dumps(users)
    return Response(response=response, mimetype="application/json")


@application.route("/users/<id>", methods=["GET"])
def get_User(id):
    user = db.users.find_one({"_id": objectid.ObjectId(id)})
    response = json_util.dumps(user)
    return Response(response=response, mimetype="application/json")


@application.route("/users/<id>", methods=["DELETE"])
def delete_User(id):
    db.users.delete_one({"_id": objectid.ObjectId(id)})
    response = jsonify({"message": "User " + id + "Was Deleted"})
    return response
