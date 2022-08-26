import json
from app import application


def test_get_users():
    flask_app = application

    with flask_app.test_client() as test_client:
        response = test_client.get("/users")
        assert response.status_code == 200


def test_post_users_sucess():
    flask_app = application

    with flask_app.test_client() as test_client:
        response = test_client.post(
            "/users",
            json={
                "name": "TestName",
                "rol": "rolTest",
                "email": "email@test.com",
                "gender": "testGender",
                "age": "25",
            },
        )
        assert response.status_code == 200

        assert response.json["name"] == "TestName"

        assert response.json["rol"] == "rolTest"
        assert response.json["email"] == "email@test.com"
        assert response.json["gender"] == "testGender"
        assert response.json["age"] == "25"


def test_get_users_byName_sucess():
    flask_app = application

    with flask_app.test_client() as test_client:
        response = test_client.get(
            "/users/Erwing",
        )
        assert response.status_code == 200

        assert response.json["name"] == "Erwing"
