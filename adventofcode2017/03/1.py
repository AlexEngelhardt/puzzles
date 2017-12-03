class Grid:
    def get_ring(self, pos):
        if pos <= 1:
            return 0
        ring = 1
        while True:
            if pos >= (2*ring - 1) ** 2 + 1 and pos <= (2*ring + 1) ** 2:
                return ring
            else:
                ring += 1
                
    def get_diags(self, ring):
        return [(2*ring + 1) ** 2 - x * 2 * ring for x in range(4)]
    
    def get_crosses(self, ring):
        diags = self.get_diags(ring)
        return [d - ring for d  in diags]

    def get_distance(self, pos):
        ring = self.get_ring(pos)
        crosses = self.get_crosses(ring)
        to_cross = min([abs(pos - cross) for cross in crosses])
        
        return ring + to_cross

grid = Grid()
    
print(grid.get_ring(11))
print(grid.get_ring(368078))
print(grid.get_diags(303))

print(grid.get_diags(2))
print(grid.get_crosses(2))
print(grid.get_crosses(3))

print(grid.get_distance(3))
print(grid.get_distance(4))
print(grid.get_distance(26))
print(grid.get_distance(49))
print(grid.get_distance(368078))
