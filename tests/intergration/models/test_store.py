from tests.base_test import BaseTest
from models.store import StoreModel
from models.item import ItemModel

class StoreTest(BaseTest):
    def test_create_store_empty(self):
        with self.app_context():
            store = StoreModel('test')
            store.save_to_db()
            
            self.assertListEqual(store.items.all(), [])
    
    def test_crud(self):
        with self.app_context():
            store = StoreModel('test')
            
            self.assertIsNone(StoreModel.find_by_name('test'))
            
            store.save_to_db()
            
            self.assertIsNotNone(StoreModel.find_by_name('test'))
            
            store.delete_from_db()
            
            self.assertIsNone(StoreModel.find_by_name('test'))
        
    def test_store_relationships(self):
        with self.app_context():
            store = StoreModel('teststore')
            item = ItemModel('testitem', 19.99, 1)
            
            store.save_to_db()
            item.save_to_db()
            
            self.assertEqual(store.items.count(), 1)
            self.assertEqual(store.items.first().name, 'testitem')
    
    def test_store_json(self):
        with self.app_context():
            store = StoreModel('test')
            store.save_to_db()
            expected = {
                'name': 'test',
                'items': []
            }
            
            self.assertDictEqual(store.json(), expected)
            
    def test_store_json_with_items(self):
        with self.app_context():
            store = StoreModel('test')
            item = ItemModel('test', 19.99, 1)
            
            store.save_to_db()
            item.save_to_db()
            
            expected = {
                'name': 'test',
                'items': [{ 'name': 'test',
                           'price': 19.99}]
            }
            
            self.assertDictEqual(store.json(), expected)