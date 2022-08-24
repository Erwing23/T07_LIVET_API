import os
from flask import Flask, request, jsonify, Response

from app import application


if __name__ == "__main__":
    application.run(debug=True)
