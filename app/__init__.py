from email.mime import application
from flask import Flask

application = Flask(__name__)

from app import views
