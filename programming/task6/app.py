from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv
app = Flask(__name__)
load_dotenv()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("SQLALCHEMY_DATABASE_URI")
app.secret_key = os.environ.get("SECRET_KEY")
app.config['SESSION_TYPE'] = os.environ.get("SESSION_TYPE")
db = SQLAlchemy(app)
