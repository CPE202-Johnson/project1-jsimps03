import unittest
from bears import *

class TestAssign1(unittest.TestCase):
    # Given test cases to check functionality
    def test_bear_01(self):
        self.assertTrue(bears(250))

    def test_bear_02(self):
        self.assertTrue(bears(42))

    def test_bear_03(self):
        self.assertFalse(bears(53))

    def test_bear_04(self):
        self.assertFalse(bears(41))

    def test_bear_05(self):
        result = bears(50000)
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()
