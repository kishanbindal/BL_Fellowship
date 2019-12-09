import unittest
from com.bridgelabz.utility import utility



class TestBinary(unittest.TestCase):

    def test_toBinary(self):

        self.assertEqual(utility.toBinary(106),'01101010')
        self.assertEqual(utility.toBinary(64), '01000000')


if __name__ == '__main__':
    unittest.main()
