from app import application
from flask import request, jsonify, Response
from flask_pymongo import pymongo
from dotenv import load_dotenv

load_dotenv()
from bson import json_util, objectid
import os

url = os.getenv("URL")
client = pymongo.MongoClient(url)
db = client.livet


@application.route("/", methods=["GET"])
def home():
    return "<h1>404 Not Found</h1>"


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


@application.route("/recomendacion", methods=["POST"])
def create_Recomendación():
    # Recieving Data
    name = request.json["name"]
    recomendacion = request.json["recomendacion"]
    doctor = request.json["doctor"]
    area = request.json["area"]
    fecha = request.json["fecha"]

    if name and recomendacion:
        db.recomendacion.insert_one(
            {
                "name": name,
                "recomendacion": recomendacion,
                "doctor": doctor,
                "area": area,
                "fecha": fecha,
            }
        )
        response = {
            "name": name,
            "recomendacion": recomendacion,
            "doctor": doctor,
            "area": area,
            "fecha": fecha,
        }
        return response
    else:
        return {"message": "Failed"}


@application.route("/recomendacion/<name>", methods=["GET"])
def get_Recomendacion(name):
    user = db.recomendacion.find(
        {
            "name": name,
        }
    )
    response = json_util.dumps(user)
    return Response(response=response, mimetype="application/json")
