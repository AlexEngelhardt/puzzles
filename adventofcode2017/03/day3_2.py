class Grid:
    
    def __init__(self, rings):
        self.rings = rings
        self.n_elems = (2*rings - 1) ** 2
        self.chain = [0 for i in range(self.n_elems)]

    def fill_chain(self):
        self.chain[0] = 1
        coord = [0, 0]
        for i in range(1, self.n_elems):
            coords = self.get_next_coord(coord)
            self.chain[i] = self.fill_next_chain_elem(coords)

    def get_next_coord(self, coord):
        pass
            
    def fill_next_chain_elem(self, coords):
        pass
        
    def get_chain(self, length):
        return self.chain[0:length]

    def get_elem_by_i(self, i):  # actually, only used for test code
        return self.chain[i]

grid = Grid(rings=4)
