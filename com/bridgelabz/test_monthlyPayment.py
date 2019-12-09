import unittest
from com.bridgelabz.utility import utility


class TestMonthlyPayment(unittest.TestCase):

    def test_monthlyPayment(self):
        self.assertEqual(utility.monthlyPayment(100,5,1.5), 1.73)
        self.assertEqual(utility.monthlyPayment(15000,3,8),470.05)
        self.assertEqual(utility.monthlyPayment(250000,10,3),2414.02)


if __name__ == '__main__':
    unittest.main()
