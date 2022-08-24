import os
from flask import Flask, request, jsonify, Response, send_from_directory
from flask_swagger_ui import get_swaggerui_blueprint

from app import application

SWAGGER_URL = "/docs"
API_URL = "/staticFiles/swagger.json"
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL, API_URL, config={"app_name": "Seans-Python-Flask-REST-Boilerplate"}
)


application.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)


if __name__ == "__main__":
    application.run(debug=True)
