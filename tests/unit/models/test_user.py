from tests.unit.unit_base_test import UnitBaseTest
from models.user import UserModel

class UserTest(UnitBaseTest):
    def test_create_user(self):
        user = UserModel('testUser', 'testPasswd')
        
        self.assertEqual(user.username, 'testUser',
                         'Username did not match after creation')
        self.assertEqual(user.passwd, 'testPasswd',
                         'Paasword did not match after creation')