from tests.base_test import BaseTest
from models.item import ItemModel
from models.store import StoreModel

class ItemTest(BaseTest):
    def test_crud(self):
        with self.app_context():
            store = StoreModel('test')
            item = ItemModel('test', 19.99, 1)
            
            store.save_to_db()
            
            self.assertIsNone(ItemModel.find_by_name('test'),
                              'Item found where none had to be there')
            
            item.save_to_db()

            self.assertIsNotNone(ItemModel.find_by_name('test'),
                                 'Item not found in the database')
            
            item.delete_from_db()

            self.assertIsNone(ItemModel.find_by_name('test'),
                              'Item found after deletion, something went wrong')
    
    def test_store_relationship(self):
        with self.app_context():
            store = StoreModel('test')
            item = ItemModel('test', 19.99, 1)
            
            store.save_to_db()
            item.save_to_db()
            
            self.assertEqual(ItemModel.find_by_name('test').store, store,
                             'Store did not match with freshly inserted store')
            