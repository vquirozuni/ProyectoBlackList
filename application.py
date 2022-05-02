from src import create_app
from src.modelos.modelos import db
from flask_restful import Api
from src.vistas.vistas import VistaBlackList, VistaBloqueado, VistaLogIn
from src.vistas.vistas import Health
from flask_jwt_extended import JWTManager


application = create_app()
app_context = application.app_context()
app_context.push()

db.init_app(application)
db.create_all()

api = Api(application)
api.add_resource(Health, '/health')
api.add_resource(VistaBlackList, '/blacklists')
api.add_resource(VistaBloqueado, '/blacklists/<string:email_bloqueado>')
api.add_resource(VistaLogIn, '/auth/login')


jwt = JWTManager(application)