import unittest
from com.bridgelabz.utility import utility


class TestTempConversion(unittest.TestCase):

    def test_temperaturConversion(self):
        self.assertAlmostEqual(37.7778,utility.temperaturConversion(100,'F'))
        self.assertAlmostEqual(122,utility.temperaturConversion(50,'C'))
        self.assertAlmostEqual(None,utility.temperaturConversion(50,'a'))


if __name__ == '__main__':
    unittest.main()
