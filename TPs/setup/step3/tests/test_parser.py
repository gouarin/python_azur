import unittest
from calculatrice.parser import parser

class testParser(unittest.TestCase):
    def test1(self):
        self.assertEqual(parser('4+5'), ([4., 5.], ['+', '+']))

    def test2(self):
        self.assertEqual(parser('-4/5'), ([4., 5.], ['-', '/']))


if __name__ == '__main__':
    unittest.main()
