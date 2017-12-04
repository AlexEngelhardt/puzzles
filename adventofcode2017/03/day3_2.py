class Grid:
    
    def __init__(self, rings):
        self.rings = rings
        self.n_elems = (2*rings - 1) ** 2
        self.chain = [0 for i in range(self.n_elems)]
        self.make_coords()
        self.fill_chain()

    def fill_chain(self):
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
                x = self.coords[i-1][0]
                y = self.coords[i-1][1] + 1
                if x + 1 == y:
                    # switch walking direction from right to up in these
                    # "lower right" corners of the grid
                    direction = "up"
                    
            elif direction == "up":
                x = self.coords[i-1][0] - 1
                y = self.coords[i-1][1]
                if -x == y:
                    direction = "left"
                    
            elif direction == "left":
                x = self.coords[i-1][0]
                y = self.coords[i-1][1] - 1
                if x == y:
                    direction = "down"
                    
            elif direction == "down":
                x = self.coords[i-1][0] + 1
                y = self.coords[i-1][1] 
                if -x == y:
                    direction = "right"
                    
            self.coords.append([x, y])
            
    def get_coord_by_i(self, i):
        return self.coords[i]

    def get_neighboring_coords(self, coord):
        return [
            [coord[0]+dx, coord[1]+dy]
            for dx in range(-1, 2)
            for dy in range(-1, 2)
            if (not (dx==0 and dy==0))  # so that the field is not its own neighbor
            and (not abs(coord[0]+dx) >= self.rings)  # here we check that the fields are not outside of the outermost ring
            and (not abs(coord[1]+dy) >= self.rings)
        ]
        
    def fill_this_chain_elem(self, coord):
        neighbors = self.get_neighboring_coords(coord)
        total = 0
        for neighbor_coord in neighbors:
            this_val = self.get_elem_by_coord(neighbor_coord)
            # print("I got val=" + str(this_val) + " from coord " + str(neighbor_coord))
            total += this_val
        return total
        
    def get_chain(self, length):
        return self.chain[0:length]

    def get_elem_by_i(self, i):  # actually, only used for test code
        return self.chain[i]
    
    def get_elem_by_coord(self, coord):
        for i in range(self.n_elems):
            c_i = self.get_coord_by_i(i)
            if coord[0] == c_i[0] and coord[1] == c_i[1]:
                return self.chain[i]

    def get_first_greater_than(self, num):
        for i in range(self.n_elems):
            if self.chain[i] > num:
                return self.chain[i]
        return None

if __name__ == "__main__":    
    grid = Grid(rings=5)

    print(grid.get_chain(grid.n_elems))
    print(grid.get_first_greater_than(368078))
