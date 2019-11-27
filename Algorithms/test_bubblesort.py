import unittest
import bubblesort


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertListEqual([1,2,3], bubblesort.bubbleSort([2,3,1]))
        self.assertListEqual([10,15,30,40,45,50],bubblesort.bubbleSort([15,40,10,45,50,30]))


if __name__ == '__main__':
    unittest.main()
