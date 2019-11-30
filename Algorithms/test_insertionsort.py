import unittest
from Algorithms.insertionsort import insertionSort

class TestInsertionSort(unittest.TestCase):
    def test_insertionSort(self):
        arr = ['Banana','Apple','Orange','Mango','Oranges']
        self.assertListEqual(['Apple','Banana','Mango','Orange','Oranges'], insertionSort(arr))


if __name__ == '__main__':
    unittest.main()
