import os
from flask import Flask
from sqlalchemy import false

def create_app():
    app = Flask(__name__)    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@rds-blacklist.cco378ibyevv.us-east-1.rds.amazonaws.com/blacklist'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.config['JWT_SECRET_KEY']='blacklist'

    app.config['PROPAGATE_EXCEPTIONS']=True

    return app