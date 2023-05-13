from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api


application = Flask(__name__)
application.secret_key = 'flask-VoterCRM-1234'
api = Api(application)  # Flask restful wraps Flask app around it.

application.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/sakila'
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(application)



