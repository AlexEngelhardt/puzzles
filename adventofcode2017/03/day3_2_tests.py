# Just run this file with 'python 2_tests.py'
import unittest
from day3_2 import Grid

class GridIntegrationTests(unittest.TestCase):
    
    def setUp(self):
        self.grid = Grid(rings=4)

    def test_get_coord_by_id(self):
        self.assertEqual(self.grid.get_coord_by_i(0), [0, 0])
        self.assertEqual(self.grid.get_coord_by_i(17), [-1, -2])        
    
    def test_first_element(self):
        """
        This tests that the first element in the Ulam spiral is 1
        """
        self.assertEqual(self.grid.chain[0], 1)

    def test_get_elem_by_i(self):
        self.assertEqual(self.grid.chain[1], 1)
        self.assertEqual(self.grid.chain[2], 2)
        self.assertEqual(self.grid.chain[3], 4)
        self.assertEqual(self.grid.chain[4], 5)
        self.assertEqual(self.grid.chain[5], 10)
        self.assertEqual(self.grid.chain[6], 11)
        self.assertEqual(self.grid.chain[7], 23)

    def test_get_chain(self):
        self.assertEqual(self.grid.get_chain(1), [1])
        self.assertEqual(self.grid.get_chain(5), [1, 1, 2, 4, 5])        

    def test_get_first_greater_than(self):
        self.assertEqual(self.grid.get_first_greater_than(8), 10)
        self.assertEqual(self.grid.get_first_greater_than(122), 133)
        self.assertEqual(self.grid.get_first_greater_than(1234), 1968)
        self.assertEqual(self.grid.get_first_greater_than(99999999), None)
        
if __name__ == "__main__":
    unittest.main()
