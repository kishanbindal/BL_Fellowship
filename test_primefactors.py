import unittest
from primefactors import primeFactors


class testPrimeFactors(unittest.TestCase):

    def test_primefactors(self):
        self.assertListEqual([2],primeFactors(2))
        self.assertListEqual([3], primeFactors(3))
        self.assertListEqual([2,2], primeFactors(4))
        self.assertListEqual([5],primeFactors(5))
        self.assertListEqual([2,3], primeFactors(6))
        self.assertListEqual([7], primeFactors(7))
        self.assertListEqual([2,2,2], primeFactors(8))
        self.assertListEqual([3,3], primeFactors(9))
        self.assertListEqual([3,5,5], primeFactors(75))
        self.assertListEqual([2,2,3,5,7,11,13],primeFactors(2*2*3*5*7*11*13))




if __name__ == '__main__':
    unittest.main()
