from flask import Flask, send_from_directory
import os
from flask_pymongo import pymongo
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("URL")
key = os.getenv("API_KEY")
client = pymongo.MongoClient(url)
db = client.livet


application = Flask(__name__)


# from app import views
# from app import userRoutes
from app import indexRoutes, userRoutes, recomendRoutes, citaRoutes
