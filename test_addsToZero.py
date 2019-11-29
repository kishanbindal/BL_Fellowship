import unittest
from addsToZero import *


class TestToZero(unittest.TestCase):

    @unittest.skip("Skipping Input Test")
    def test_takeInput(self):
        self.assertListEqual([1,2,3,4],takeInput())

    def test_addsToZero(self):
        self.assertEqual(1,addsToZero([-1,-2,3]))
        self.assertEqual(0,addsToZero([1,2,3]))


if __name__ == '__main__':
    unittest.main()
