import imp
import os
from flask import Flask


db_host = os.getenv('DB_HOST', 'rds-blacklist.cco378ibyevv.us-east-1.rds.amazonaws.com')
db_port = os.getenv('DB_PORT', 5432)
db_name = os.getenv('DB_NAME', 'rdsblacklist')
db_user = os.getenv('DB_USER', 'postgres')
db_password = os.getenv('DB_PASSWORD', 'postgres')

def create_app():
    app = Flask(__name__)    
    app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.config['JWT_SECRET_KEY']='blacklist'

    app.config['PROPAGATE_EXCEPTIONS']=True

    return app
