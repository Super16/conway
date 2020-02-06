from main import *

import unittest

import scipy, scipy.ndimage

small_test_board = [[0, 1, 0], 
                    [1, 1, 0], 
                    [0, 0, 0]]

class TestTask(unittest.TestCase):

    def test(self):
        self.assertEqual(cell_status(1, 0), 0)
        self.assertEqual(cell_status(1, 1), 0)
        self.assertEqual(cell_status(1, 2), 1)
        self.assertEqual(cell_status(1, 3), 1)
        self.assertEqual(cell_status(1, 4), 0)
        self.assertEqual(cell_status(0, 0), 0)
        self.assertEqual(cell_status(0, 1), 0)
        self.assertEqual(cell_status(0, 2), 0)
        self.assertEqual(cell_status(0, 3), 1)
        self.assertEqual(cell_status(0, 4), 0)
        self.assertEqual(neighbors(small_test_board, [0,0]), 3)

if __name__ == '__main__':
    unittest.main()
