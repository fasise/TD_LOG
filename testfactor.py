
import unittest
from factor import factoriel
class ArithmeticTest(unittest.TestCase):
    def test_factoriel(self):
        self.assertTrue(factoriel(3)==6)

if __name__ == '_main_':
    unittest.main()




