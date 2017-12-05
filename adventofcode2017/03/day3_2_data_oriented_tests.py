import unittest
from day3_2_data_oriented import *

class GridUnitTests(unittest.TestCase):

    def test_get_n_elems(self):
        self.assertEqual(get_n_elems(rings = 0), 1)
        self.assertEqual(get_n_elems(rings = 1), 1)
        self.assertEqual(get_n_elems(rings = 2), 9)
        self.assertEqual(get_n_elems(rings = 3), 25)

    def test_make_coords(self):
        self.assertEqual(make_coords(1), [[0, 0]])
        self.assertEqual(make_coords(3), [[0, 0], [0, 1], [-1, 1]])
        self.assertEqual(make_coords(8),
                         [[0, 0], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1], [1, 0]]
        )

    def test_get_neighbor_coords(self):
        pass  # TODO :)

    def test_get_elem_by_coord(self):
        pass  # TODO 
    
if __name__ == "__main__":
    unittest.main()
