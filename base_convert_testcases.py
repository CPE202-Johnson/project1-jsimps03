import unittest
from  base_convert import *

class TestBaseConvert(unittest.TestCase):

    def test_base2(self):
        self.assertEqual(convert(45,2),"101101")

    def test_base4(self):
        self.assertEqual(convert(30,4),"132")

    def test_base16(self):
        self.assertEqual(convert(316,16),"13C")
    
    def test_base16_letters(self):
        self.assertEqual(convert(65535, 16), "FFFF")
        self.assertEqual(convert(61166, 16), "EEEE")
        self.assertEqual(convert(56797, 16), "DDDD")
        self.assertEqual(convert(52428, 16), "CCCC")
        self.assertEqual(convert(48059, 16), "BBBB")
        self.assertEqual(convert(43690, 16), "AAAA")

if __name__ == "__main__":
        unittest.main()