from tests.base_test import BaseTest
from models.user import UserModel

class UserTest(BaseTest):
    def test_crud_user(self):
        with self.app_context():
            user = UserModel('testUser', 'testPasswd')
            
            self.assertIsNone(UserModel.find_by_name('testUser'))
            self.assertIsNone(UserModel.find_by_id(1))
            
            user.save_to_db()
            
            self.assertIsNotNone(UserModel.find_by_name('testUser'))
            self.assertIsNotNone(UserModel.find_by_id(1))
            
            user.delete_from_db()
            
            self.assertIsNone(UserModel.find_by_name('testUser'))
            self.assertIsNone(UserModel.find_by_id(1))