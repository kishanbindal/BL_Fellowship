import unittest
from vendingmachine import userInput, vendingMachine


class TestVending(unittest.TestCase):
    @unittest.skip
    def test_userInput(self):
        self.assertRaises(TypeError,userInput,'Kishan')

    def test_vendingMachine(self):
        self.assertDictEqual({1000:1,500:1,100:1,50:1,10:1,5:1,2:1,1:1},vendingMachine(1668))
        self.assertDictEqual({100:4,10:2,5:1},vendingMachine(425))


if __name__ == '__main__':
    unittest.main()
