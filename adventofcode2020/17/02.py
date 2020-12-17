from collections import defaultdict, namedtuple

debug = False

if debug:
    filename = 'test_input'
else:
    filename = 'input'

with open(filename) as f:
    lines = f.read().splitlines()

Point = namedtuple('Point', ['x', 'y', 'z', 'w'])
grid = set()

grid_border = {
    'x': {'min': 0, 'max': 0},
    'y': {'min': 0, 'max': 0},
    'z': {'min': 0, 'max': 0},
    'w': {'min': 0, 'max': 0}
}

for row_i, row in enumerate(lines):
    for col_i, col in enumerate(row):
        if lines[row_i][col_i] == '#':
            grid.add(Point(x=col_i, y=row_i, z=0, w=0))
            grid_border['x']['min'] = min(grid_border['x']['min'], col_i)
            grid_border['x']['max'] = max(grid_border['x']['max'], col_i)
            grid_border['y']['min'] = min(grid_border['y']['min'], row_i)
            grid_border['y']['max'] = max(grid_border['y']['max'], row_i)


def neighbors(x, y, z, w):
    for xx in [x-1, x, x+1]:
        for yy in [y-1, y, y+1]:
            for zz in [z-1, z, z+1]:
                for ww in [w-1, w, w+1]:
                    if [xx, yy, zz, ww] == [x, y, z, w]:
                        continue
                    yield xx, yy, zz, ww


def step(grid, grid_border):
    new_grid = set()
    new_border = grid_border.copy()
    for x in range(grid_border['x']['min'] - 1, grid_border['x']['max'] + 2):
        for y in range(grid_border['y']['min'] - 1, grid_border['y']['max'] + 2):
            for z in range(grid_border['z']['min'] - 1, grid_border['z']['max'] + 2):
                for w in range(grid_border['w']['min'] - 1, grid_border['w']['max'] + 2):
                    ngh = neighbors(x, y, z, w)
                    n_neighbors = 0
                    for n in ngh:
                        if n in grid:
                            n_neighbors += 1
                    # If a cube is active and exactly 2 or 3 of its neighbors are also active, the cube remains active.
                    # Otherwise, the cube becomes inactive.
                    if (x, y, z, w) in grid and n_neighbors in [2, 3]:
                        new_grid.add(Point(x, y, z, w))
                        new_border['x']['min'] = min(new_border['x']['min'], x)
                        new_border['x']['max'] = max(new_border['x']['max'], x)
                        new_border['y']['min'] = min(new_border['y']['min'], y)
                        new_border['y']['max'] = max(new_border['y']['max'], y)
                        new_border['z']['min'] = min(new_border['z']['min'], z)
                        new_border['z']['max'] = max(new_border['z']['max'], z)
                        new_border['w']['min'] = min(new_border['w']['min'], w)
                        new_border['w']['max'] = max(new_border['w']['max'], w)
                    # If a cube is inactive but exactly 3 of its neighbors are active, the cube becomes active.
                    # Otherwise, the cube remains inactive.
                    if (x, y, z, w) not in grid and n_neighbors == 3:
                        new_grid.add(Point(x, y, z, w))
                        new_border['x']['min'] = min(new_border['x']['min'], x)
                        new_border['x']['max'] = max(new_border['x']['max'], x)
                        new_border['y']['min'] = min(new_border['y']['min'], y)
                        new_border['y']['max'] = max(new_border['y']['max'], y)
                        new_border['z']['min'] = min(new_border['z']['min'], z)
                        new_border['z']['max'] = max(new_border['z']['max'], z)
                        new_border['w']['min'] = min(new_border['w']['min'], w)
                        new_border['w']['max'] = max(new_border['w']['max'], w)

    return new_grid, new_border


grid1, border1 = step(grid, grid_border)
print(grid1)
grid2, border2 = step(grid1, border1)
grid3, border3 = step(grid2, border2)
grid4, border4 = step(grid3, border3)
grid5, border5 = step(grid4, border4)
grid6, border6 = step(grid5, border5)

print(len(grid6))
