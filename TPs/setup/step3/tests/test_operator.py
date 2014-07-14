import unittest
import calculatrice.operateur as op

class testOperator(unittest.TestCase):
    def setUp(self):
        self.a = 4
        self.b = 5

    def testAdd(self):
        self.assertEqual(op.addition(self.a, self.b), 9.)

    def testSous(self):
        self.assertEqual(op.soustraction(self.a, self.b), -1.)

    def testMult(self):
        self.assertEqual(op.multiplication(self.a, self.b), 20.)

    def testDiv(self):
        self.assertEqual(op.division(self.a, self.b), .8)
