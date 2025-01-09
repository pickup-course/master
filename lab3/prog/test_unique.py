#test_unique.py

import unittest
from unique import Unique

class TestUnique(unittest.TestCase):
    
    def test1(self): # Тестирует на пропуск дупликатов
        items = [1, 2, 2, 3, 1, 4]
        unique = Unique(items)
        result = list(unique)
        self.assertEqual(result, [1, 2, 3, 4])
    
    def test2(self): # Тестирует IgnoreCase = False
        items = ["apple", "Apple", "banana", "APPLE"]
        unique = Unique(items, ignore_case = False)
        result = list(unique)
        self.assertEqual(result, ["apple", "Apple", "banana", "APPLE"])
    
    def test3(self): # Тестирует IgnoreCase = True
        items = ["apple", "Apple", "banana", "APPLE"]
        unique = Unique(items, ignore_case = True)
        result = list(unique)
        self.assertEqual(result, ["apple", "banana"])
        
if __name__ == "__main__":
    unittest.main()