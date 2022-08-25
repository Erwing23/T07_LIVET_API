from app import application, db
from flask import request, jsonify, Response

from bson import json_util, objectid


@application.route("/citas", methods=["GET"])
def list_Citas():
    citas = db.citas.find()
    response = json_util.dumps(citas)
    return Response(response=response, mimetype="application/json")


@application.route("/citas/<paciente>", methods=["GET"])
def get_Citas(paciente):
    citas = db.citas.find({"paciente": paciente})
    response = json_util.dumps(citas)
    return Response(response=response, mimetype="application/json")


@application.route("/citas", methods=["POST"])
def create_Cita():
    # Recieving Data
    doctor = request.json["doctor"]
    paciente = request.json["paciente"]
    timeStart = request.json["timeStart"]
    timeEnd = request.json["timeEnd"]
    area = request.json["area"]
    date = request.json["date"]

    if doctor and paciente and timeStart and timeEnd and area and date:

        db.citas.insert_one(
            {
                "doctor": doctor,
                "paciente": paciente,
                "timeStart": timeStart,
                "timeEnd": timeEnd,
                "area": area,
                "date": date,
            }
        )
        response = {
            "doctor": doctor,
            "paciente": paciente,
            "timeStart": timeStart,
            "timeEnd": timeEnd,
            "area": area,
            "date": date,
        }
        return response
    else:
        return {"message": "Failed"}
