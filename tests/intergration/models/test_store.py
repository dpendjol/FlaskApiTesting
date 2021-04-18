from tests.base_test import BaseTest
from models.store import StoreModel
from models.item import ItemModel

class StoreTest(BaseTest):
    def test_create_store_empty(self):
        with self.app_context():
            store = StoreModel('test')
            store.save_to_db()
            
            self.assertListEqual(store.items.all(), [],
                                 'List wasn\'t empty where it was supose to be')
    
    def test_crud(self):
        with self.app_context():
            store = StoreModel('test')
            
            self.assertIsNone(StoreModel.find_by_name('test'),
                              'Already found a store, is not suppose to be there')
            
            store.save_to_db()
            
            self.assertIsNotNone(StoreModel.find_by_name('test'),
                                 'Did not found the created store')
            
            store.delete_from_db()
            
            self.assertIsNone(StoreModel.find_by_name('test'),
                              'Deletion did not went right, found the store')
        
    def test_store_relationships(self):
        with self.app_context():
            store = StoreModel('teststore')
            item = ItemModel('testitem', 19.99, 1)
            
            store.save_to_db()
            item.save_to_db()
            
            self.assertEqual(store.items.count(), 1,
                             f'List contains {store.items.count()}, where 1 was expected')
            self.assertEqual(store.items.first().name, 'testitem',
                             'List did not contain the item just inserted')
    
    def test_store_json(self):
        with self.app_context():
            store = StoreModel('test')
            store.save_to_db()
            expected = {
                'name': 'test',
                'items': []
            }
            
            self.assertDictEqual(store.json(), expected,
                                 'Got another json object back then expected')
            
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
            
            self.assertDictEqual(store.json(), expected,
                                 'Got another json object back then expected')