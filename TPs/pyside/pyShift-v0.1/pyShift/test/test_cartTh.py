import pyShift.cartTh as CTH
import unittest

class CartThTestCase(unittest.TestCase):
    def setUp(self):
        self.n = 5
        n = self.n
        self.m = CTH.cartThPurePython1(n, n, n)

    def test_method(self):
        n = self.n
        self.assertTrue((self.m == CTH.cartThPurePython2(n, n, n)).all())
        self.assertTrue((self.m == CTH.cartThNumpy(n, n, n)).all())
        self.assertTrue((self.m == CTH.cartThCythonMV1(n, n, n)).all())
        self.assertTrue((self.m == CTH.cartThCythonMV2(n, n, n)).all())
        self.assertTrue((self.m == CTH.cartThCythonOB1(n, n, n)).all())
        self.assertTrue((self.m == CTH.cartThCythonOB2(n, n, n)).all())

if __name__ == '__main__':
    unittest.main()
