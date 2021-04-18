from tests.base_test import BaseTest
from models.store import StoreModel
import json

class StoreTest(BaseTest):
    def test_create_store(self):
         with self.app() as client:
            with self.app_context():
                response = client.post('/store/test')

                self.assertEqual(response.status_code, 201)
                self.assertDictEqual(json.loads(response.data),
                                    {
                                        'name': 'test',
                                        'items': []
                                    })
                
    def test_create_duplicate_store(self):
        with self.app() as client:
            with self.app_context():
                client.post('/store/test')
                response = client.post('/store/test')
                
                self.assertEqual(response.status_code, 400)
                self.assertDictEqual(json.loads(response.data),
                                    {
                                        'message': 'A store with name \'test\' already exists.'
                                    })
    
    def test_delete_store(self):
        pass
    
    def test_find_store(self):
        pass
    
    def test_store_not_found(self):
        pass
    
    def test_store_found_with_items(self):
        pass

    def test_store_list(self):
        pass
    
    def test_store_list_with_items(self):
        pass
    