import unittest
from leapyear import isLeapYear


class isLeapYearTest(unittest.TestCase):

    def test_isLeapYear(self):
        self.assertEqual(isLeapYear(2014),False)
        self.assertEqual(isLeapYear(2016),True)

    def test_inputvalues(self):
        self.assertRaises(ValueError,isLeapYear,1581)

if __name__ == '__main__':
    unittest.main()