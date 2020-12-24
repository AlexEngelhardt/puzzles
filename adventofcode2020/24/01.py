debug = False

if debug:
    filename = 'test_input'
else:
    filename = 'input'

with open(filename) as f:
    lines = f.read().splitlines()


def to_coords(s):
    # uses hex coordinates like here:
    # https://catlikecoding.com/unity/tutorials/hex-map/part-1/hexagonal-coordinates/axial-diagram.png
    coords = [0, 0]  # (x, y), or (red, blue) in the above image

    while s:
        if s[0] in ['s', 'n']:
            step, s = s[:2], s[2:]
        else:
            step, s = s[:1], s[1:]

        if step == 'e':
            coords[0] += 1
        elif step == 'w':
            coords[0] -= 1
        elif step == 'ne':
            coords[1] += 1
        elif step == 'nw':
            coords[0] -= 1
            coords[1] += 1
        elif step == 'se':
            coords[0] += 1
            coords[1] -= 1
        elif step == 'sw':
            coords[1] -= 1

    return tuple(coords)


black_tiles = set()
for line in lines:
    coords = to_coords(line)
    # black_tiles ^= set(coords)  # set XOR :) but doesn't work. Why?
    if coords in black_tiles:
        black_tiles.remove(coords)  # flip to white
    else:
        black_tiles.add(coords)  # flip to black

print(len(black_tiles))

