from flask import Flask

# from flask_sqlalchemy import SQLAlchemy

# create database connection object
# db = SQLAlchemy()

app = Flask(__name__)

from app import routes
