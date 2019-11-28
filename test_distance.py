import unittest
from distance import *
import math



class TestDistance(unittest.TestCase):

    def test_distance(self):
        self.assertEqual(math.sqrt(2**2+3**2),distance(2,3))


if __name__ == '__main__':
    unittest.main()
