from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# create database connection object
db = SQLAlchemy()


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object("config.Config")

    db.init_app(app)

    # a simple page that says hello
    @app.route("/hello")
    def hello():
        return "Hello, World!"

    return app
