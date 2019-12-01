def get_n_elems(rings):
    return (2*rings - 1) ** 2

def make_coords(n_elems):
    coords = [[0, 0]]
    direction = "right"
    for i in range(1, n_elems):
        if direction == "right":
            row = coords[i-1][0]
            col = coords[i-1][1] + 1
            if row + 1 == col:
                # switch walking direction from right to up in these
                # "lower right" corners of the grid
                direction = "up"
                
        elif direction == "up":
            row = coords[i-1][0] - 1
            col = coords[i-1][1]
            if -row == col:
                direction = "left"
                
        elif direction == "left":
            row = coords[i-1][0]
            col = coords[i-1][1] - 1
            if row == col:
                direction = "down"
                    
        elif direction == "down":
            row = coords[i-1][0] + 1
            col = coords[i-1][1]
            if -row == col:
                direction = "right"
                
        coords.append([row, col])
    return coords

def get_neighbor_coords(coord, rings):
    return [
        [coord[0]+dx, coord[1]+dy]
        for dx in range(-1, 2)
        for dy in range(-1, 2)
        if not (dx == 0 and dy == 0)  # so that the field is not its own neighbor
        # here we check that the fields are not outside of the outermost ring:
        and (not abs(coord[0]+dx) >= rings)
        and (not abs(coord[1]+dy) >= rings)
    ]

def get_elem_by_coord(chain, coords, coord):
    for i in range(len(coords)):
        if coords[i]  == coord:
            return chain[i]

def fill_chain(rings):
    n_elems = get_n_elems(rings)
    chain = [0] * n_elems
    chain[0] = 1
    coords = make_coords(n_elems)
    for i in range(1, n_elems):
        new_elem = fill_this_chain_elem(coords[i], coords, chain)
        print("Filling chain at " + str(i) + " with " + str(new_elem))
        chain[i] = new_elem
    return chain

def fill_this_chain_elem(coord, coords, chain):
    neighbors = get_neighbor_coords(coord, rings)
    return sum(get_elem_by_coord(chain, coords, neighbor_coord)
               for neighbor_coord in neighbors)
        
def get_first_greater_than(chain, number):
    for elem in chain:
        if elem > number:
            return elem
                            
if __name__ == "__main__":
    rings = 5
    filled_chain = fill_chain(rings)
    print(get_first_greater_than(filled_chain, 368078))
    
