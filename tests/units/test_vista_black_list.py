import json
from unittest import TestCase
from unittest.mock import patch, Mock

from application import application as app
from src.modelos.modelos import db
from src.vistas.vistas import VistaBlackList


def mock_jwt_required(realn):
    return


class TestVistaBlackList(TestCase):
    def setUp(self) -> None:
        with open('./data/devops_public_bloqueado.json', 'r') as file:
            requests = json.load(file)

        self.requests = requests

        app.config['TESTING'] = True
        app.config['DEBUG'] = True
        app.config['APP_ENV'] = 'APP_ENV_TESTING'
        app.config['WTF_CSRF_ENABLED'] = False
        self.client = app.test_client()
        db.create_all()

    def test_vista_black_list_get_positive(self):
        request = self.client.get('/blacklists')
        code = request.status_code
        response = request.get_json()

        self.assertEqual(code, 401)
