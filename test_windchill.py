import unittest
from windchill import *


class MyTestCase(unittest.TestCase):

    #@unittest.skip("Skipping ValueError")
    def test_userInput(self):
        self.assertRaises(ValueError,windChill(100,10))


    def test_windChill(self):
        self.assertEqual(25.43,windChill(35,15))
        self.assertEqual(39.76,windChill(48.5,31.8))



if __name__ == '__main__':
    unittest.main()
