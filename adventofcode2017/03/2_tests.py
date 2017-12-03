# Just run this file with 'python 2_tests.py'
import unittest
from day3_2 import Grid

class GridTest(unittest.TestCase):
    
    def setUp(self):
        self.grid = Grid(rings=4)

    ## These functions are not necessary to implement. (Keep it lean!)    
    # def test_get_coords(self):
    #     """
    #     Check that zero-based coordinates are computed correctly
    #     """
    #     self.assertEqual(self.grid.get_coords(0), [0, 0])
    #     self.assertEqual(self.grid.get_coords(3), [-1, 0])
    #     self.assertEqual(self.grid.get_coords(9), [1, 2])
    
    def test_first_element(self):
        """
        This tests that the first element in the Ulam spiral is 1
        """
        self.assertEqual(self.grid.get_elem_by_i(1), 1)

    def test_get_elem_by_n(self):
        self.assertEqual(self.grid.get_elem_by_i(2), 1)
        self.assertEqual(self.grid.get_elem_by_i(3), 2)
        self.assertEqual(self.grid.get_elem_by_i(4), 4)
        self.assertEqual(self.grid.get_elem_by_i(5), 5)
        self.assertEqual(self.grid.get_elem_by_i(6), 10)
        self.assertEqual(self.grid.get_elem_by_i(7), 11)

    def test_get_next_coord(self):
        self.assertEqual(self.grid.get_next_coord([0, 0]), [0, 1])
        self.assertEqual(self.grid.get_next_coord([0, 1]), [-1, 1])
        self.assertEqual(self.grid.get_next_coord([-1, 1]), [-1, 0])
        self.assertEqual(self.grid.get_next_coord([-1, 0]), [-1, -1])
        self.assertEqual(self.grid.get_next_coord([-1, -1]), [0, -1])
        self.assertEqual(self.grid.get_next_coord([0, -1]), [1, -1])
        self.assertEqual(self.grid.get_next_coord([1, -1]), [1, 0])
        self.assertEqual(self.grid.get_next_coord([1, 0]), [1, 1])
        self.assertEqual(self.grid.get_next_coord([1, 1]), [1, 2])

    def test_get_chain(self):
        self.assertEqual(self.grid.get_chain(1), [1])
        self.assertEqual(self.grid.get_chain(5), [1, 1, 2, 4, 5])        
        
if __name__ == "__main__":
    unittest.main()
