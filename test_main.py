# test_main.py
import unittest
from main import add_numbers

class TestMain(unittest.TestCase):
    
    def test_add_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)
        self.assertEqual(add_numbers(-1, 1), 0)
        self.assertEqual(add_numbers(0, 0), 0)
        self.assertEqual(add_numbers(100, 200), 300)

if __name__ == "__main__":
    unittest.main()
