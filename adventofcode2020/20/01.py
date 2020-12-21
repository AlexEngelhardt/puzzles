import re
import numpy as np

# debug = True
debug = False

if debug:
    filename = 'test_input'
else:
    filename = 'input'

# Parse fields into a dict of numpy arrays

with open(filename) as f:
    contents = f.read()
tiles = contents.strip().split('\n\n')
T = dict()
for tile in tiles:
    line1, tile_field = tile.split('\n', 1)
    id = int(re.match(r'Tile (\d+):', line1).group(1))

    tile_field = tile_field.split('\n')
    tile_field = [[1 if char == '#' else 0 for char in line] for line in tile_field]
    tile_field = np.array(tile_field)

    T[id] = tile_field


print(f'{len(T)} arrays are ther')
print(T[1951])


def flip(field, horiz=True):
    return np.fliplr(field) if horiz else np.flipud(field)


def rotate(field, deg_right=90):
    times = int(deg_right / 90)
    return np.rot90(field, k=times)