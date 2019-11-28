import unittest
from powerof2 import powerOf2


class test_powerOfTwo(unittest.TestCase):

    def test_powerof2(self):
        self.assertListEqual([1,2,4,8,16,32],powerOf2(5))
        self.assertListEqual([1],powerOf2(0))
        self.assertListEqual([],powerOf2(-1))


if __name__ == '__main__':
    unittest.main()
