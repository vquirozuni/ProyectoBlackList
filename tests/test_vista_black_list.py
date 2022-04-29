from email import header
import unittest
import json
from application import application
from src.modelos.modelos import *


def login_user(self, username, password):
        return self.client.post(
        '/auth/login',
        data=json.dumps(dict(
            username=username,
            password=password
        )),
        content_type='application/json',
    )

class TestVistaBlackList(unittest.TestCase):
    def setUp(self):        
        application.config['TESTING'] = True
        application.config['DEBUG'] = True
        application.config['APP_ENV'] = 'APP_ENV_TESTING'
        application.config['WTF_CSRF_ENABLED'] = False
        self.client = application.test_client()
        db.create_all()


    

    def test_vista_black_list_get_all_positive(self):
        with self.client:
            token = login_user(self, 'vquiroz', '1234')
            response = self.client.get(
                '/blacklists', 
                headers=dict(
                    Authorization = 'Bearer ' + json.loads(
                        token.data.decode()
                    )['token']
                )
            )
            #data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)

    def test_vista_blacklist_post_positive(self):
        with self.client:
            token = login_user(self, 'vquiroz', '1234')
            new_bloqueado = {
                "email": "prueba@uniandes.edu.co",
                "app_uuid": "sdd1234dsfsdf9abcdef",
               "blocked_reason": "Bloqueo de test"
            }
            response = self.client.post(
                '/blacklists', json=new_bloqueado, 
                headers=dict(
                    Authorization = 'Bearer ' + json.loads(
                        token.data.decode()
                    )['token']
                )
            )            
            code = response.status_code
            self.assertEqual(code, 200)

    def test_vista_black_list_get_one_positive(self):
        with self.client:
            token = login_user(self, 'vquiroz', '1234')
            response = self.client.get(
                '/blacklists/correoprueba@uniandes.edu.co', 
                headers=dict(
                    Authorization = 'Bearer ' + json.loads(
                        token.data.decode()
                    )['token']
                )
            )
            data = json.loads(response.data.decode())            
            self.assertTrue(data['email'] == 'correoprueba@uniandes.edu.co')
            self.assertEqual(response.status_code, 200)
