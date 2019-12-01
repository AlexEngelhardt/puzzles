"""
Solution for the second part of this puzzle:
http://adventofcode.com/2017/day/3
"""

class Grid:
    """
    Creates a grid with a specified number of rings
    """
    def __init__(self, rings):
        self.rings = rings
        self.n_elems = (2*rings - 1) ** 2
        self.chain = [0 for _ in range(self.n_elems)]  # SO review!
        self.make_coords()
        self.fill_chain()

    def fill_chain(self):
        """
        Fills the entire chain subsequently with values
        """
        self.chain[0] = 1
        for i in range(1, self.n_elems):
            coord = self.get_coord_by_i(i)
            new_val = self.fill_this_chain_elem(coord)
            # print("I'ma fill number " + str(i) + " with " + str(new_val))
            self.chain[i] = new_val

    def make_coords(self):
        """
        Coordinates are in [row, col] format and start at the center
        of the chain at [0, 0]. For a grid with 4 rings (i.e. 49 elements),
        the coordinates then go from [-3, -3] to [3, 3]
        """
        self.coords = [[0, 0]]
        direction = "right"
        for i in range(1, self.n_elems):
            if direction == "right":
                x_val = self.coords[i-1][0]
                y_val = self.coords[i-1][1] + 1
                if x_val + 1 == y_val:
                    # switch walking direction from right to up in these
                    # "lower right" corners of the grid
                    direction = "up"

            elif direction == "up":
                x_val = self.coords[i-1][0] - 1
                y_val = self.coords[i-1][1]
                if -x_val == y_val:
                    direction = "left"

            elif direction == "left":
                x_val = self.coords[i-1][0]
                y_val = self.coords[i-1][1] - 1
                if x_val == y_val:
                    direction = "down"

            elif direction == "down":
                x_val = self.coords[i-1][0] + 1
                y_val = self.coords[i-1][1]
                if -x_val == y_val:
                    direction = "right"

            self.coords.append([x_val, y_val])

    def get_coord_by_i(self, i):
        """
        Are you serious, pylint?
        """
        return self.coords[i]

    def get_neighboring_coords(self, coord):
        """
        Finds all 8 neighboring coordinates of the supplied coord.
        If the coord is close to the border of the grid, it will skip these coords.
        """
        return [
            [coord[0]+dx, coord[1]+dy]
            for dx in range(-1, 2)
            for dy in range(-1, 2)
            if not (dx == 0 and dy == 0)  # so that the field is not its own neighbor
            # here we check that the fields are not outside of the outermost ring:
            and (not abs(coord[0]+dx) >= self.rings)
            and (not abs(coord[1]+dy) >= self.rings)
        ]

    def fill_this_chain_elem(self, coord):
        """
        Fills one chain element with the sum of all neighboring
        elements' values.
        """
        neighbors = self.get_neighboring_coords(coord)
        return sum(self.get_elem_by_coord(neighbor_coord)  # SO review!
                   for neighbor_coord in neighbors)

    def get_chain(self, length):
        """
        Returns the first 'length' elements of the chain.
        """
        return self.chain[:length]  # SO review!

    def get_elem_by_coord(self, coord):
        """
        Gets an element specified by coordinates
        """
        for i in range(self.n_elems):
            c_i = self.get_coord_by_i(i)
            if coord[0] == c_i[0] and coord[1] == c_i[1]:
                return self.chain[i]

    def get_first_greater_than(self, num):
        """
        Returns the answer for the puzzle!
        """
        for i in range(self.n_elems):
            if self.chain[i] > num:
                return self.chain[i]
        return None

if __name__ == "__main__":
    GRID = Grid(rings=5)

    print(GRID.get_chain(GRID.n_elems))
    print(GRID.get_first_greater_than(368078))
