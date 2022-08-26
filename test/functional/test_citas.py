import json
from app import application


def test_get_citas():
    flask_app = application

    with flask_app.test_client() as test_client:
        response = test_client.get("/citas")
        assert response.status_code == 200


def test_post_citas_sucess():
    flask_app = application

    with flask_app.test_client() as test_client:
        response = test_client.post(
            "/citas",
            json={
                "doctor": "TestDoctor",
                "paciente": "TestPatient",
                "timeStart": "14:00",
                "timeEnd": "16:00",
                "area": "TestArea",
                "date": "10-10-22",
            },
        )
        assert response.status_code == 200

        assert response.json["doctor"] == "TestDoctor"
        assert response.json["paciente"] == "TestPatient"
        assert response.json["timeStart"] == "14:00"
        assert response.json["timeEnd"] == "16:00"
        assert response.json["area"] == "TestArea"
        assert response.json["date"] == "10-10-22"


def test_get_citas_byPaciente_sucess():
    flask_app = application

    with flask_app.test_client() as test_client:
        response = test_client.get(
            "/citas/Erwing",
        )
        assert response.status_code == 200

        assert response.json[0]["paciente"] == "Erwing"
