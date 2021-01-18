import unittest
from perm_lex import *

class TestAssign1(unittest.TestCase):

    def test_perm_gen_lex(self):
        # Initial two tests just for basic, correct functionality
        self.assertEqual(perm_gen_lex('ab'),['ab','ba'])
        self.assertEqual(perm_gen_lex("abc"), ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
        # Testing empty string input
        self.assertEqual(perm_gen_lex(""), [])
        # Testing single character string input
        self.assertEqual(perm_gen_lex("a"), ['a'])

if __name__ == "__main__":
        unittest.main()
