from tests.unit.unit_base_test import UnitBaseTest
from models.item import ItemModel

class ItemTest(UnitBaseTest):
    def test_create(self):
        item = ItemModel('test', 19.99, 1)
        
        self.assertEqual(item.name, 'test',
                         f'Expected \'test\', got {item.name}')
        self.assertEqual(item.price, 19.99,
                         f'Expected 19.99, got {item.price}')
    
    def test_json(self):
        item = ItemModel('test', 19.99, 1)
        
        expected = {'name': 'test', 'price': 19.99}
        result = item.json()
        
        self.assertEqual(result, expected,
                         f"Expected {expected}, got {result}")