from app import application, db
from flask import request, jsonify, Response

from bson import json_util, objectid


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
