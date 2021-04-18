from tests.base_test import BaseTest
from models.user import UserModel
import json

class UserTest(BaseTest):
    def test_register(self):
        with self.app() as client:
            with self.app_context():
                request = client.post('/register', data={'username': 'testUser', 'passwd': 'testPasswd'})

                self.assertEqual(request.status_code, 201)
                self.assertIsNotNone(UserModel.find_by_name('testUser'))
                self.assertDictEqual(json.loads(request.data), {'message': 'User created'})
    
    def test_login(self):
        with self.app() as client:
            with self.app_context():
                request = client.post('/register', data={'username': 'testUser', 'passwd': 'testPasswd'})
                user = UserModel.find_by_name('testUser')
                auth_req = client.post('/auth', data=json.dumps({'username': 'testUser', 'passwd': 'testPasswd'}),
                                       headers={'Content-Type': 'application/json'})
                
                self.assertIn('access_token', json.loads(auth_req.data).keys(), 'Access token not found in response')
    
        def test_register_duplicate(self):
        pass