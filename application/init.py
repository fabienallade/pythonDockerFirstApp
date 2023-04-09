import os
from flask import Flask, jsonify
from flask_migrate import Migrate
from application import routes
from application import models
from flask_mysqldb import MySQL


def create_app(test_config=None):

    # creates an application that is named after the name of the file
    app = Flask(__name__)
    
    app.config["SECRET_KEY"] = "some_dev_key"
    app.config['MYSQL_HOST'] = os.getenv("MYSQL_HOST")
    app.config['MYSQL_USER'] =  os.getenv("MYSQL_USER")
    app.config['MYSQL_PASSWORD'] =  os.getenv("MYSQL_PASSWORD")
    app.config['MYSQL_DB'] =  os.getenv("MYSQL_DB")
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")


    # initializing routes
    routes.init_routes(app)

    return app