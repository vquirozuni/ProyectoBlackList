import unittest
from application import application
from src.modelos.modelos import *




class TestVistaBlackList(unittest.TestCase):
    def setUp(self):        
        application.config['TESTING'] = True
        application.config['DEBUG'] = True
        application.config['APP_ENV'] = 'APP_ENV_TESTING'
        application.config['WTF_CSRF_ENABLED'] = False
        self.client = application.test_client()
        db.create_all()

    def test_vista_black_list_get_positive(self):
        request = self.client.get('/blacklists')
        code = request.status_code
        #response = request.get_json()
        self.assertEqual(code, 200)

    def test_vista_blacklist_post_positive(self):
        new_bloqueado = {
            "email": "correoprueba@uniandes.edu.co",
            "app_uuid": "1234dsfsdf9abcdef",
            "blocked_reason": "Bloqueo de pruebas"
        }
        request = self.client.post("/blacklists", json=new_bloqueado)
        code = request.status_code
        #response = request.get_json()
        self.assertEqual(code, 200)