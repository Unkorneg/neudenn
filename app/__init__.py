from flask import Flask
from config import Config

# from flask_sqlalchemy import SQLAlchemy

# create database connection object
# db = SQLAlchemy()

app = Flask(__name__)
app.config.from_object(Config)

from app import routes
