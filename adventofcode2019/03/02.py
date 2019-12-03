# Don't model the playing field as a 2d-array,
# the memory won't suffice.

# Instead, create a list of 2-tuples that reflect the sequential
# coordinates.

# Then, find identical coordinates.

# No! Use a dict with a 2-tuple key. Where the value is 2, the paths collide!

debug = False

if debug:
    filename = 'test-input'
else:
    filename = 'input'

with open(filename) as f:
    path1 = f.readline().strip().split(',')
    path2 = f.readline().strip().split(',')

if debug:
    print(path1)
    print(path2)


def create_coord_set(path):
    # The current position:
    path_pos = [0, 0]

    # The dict containing the travelled path and distances:
    path_dict = dict()

    # No, don't add the first coord, because that would count as an
    # intersection with minimal distance :)
    # path_set.add((0, 0))

    steps_travelled = 0

    for steps in path:
        if steps[0] == 'R':
            axis, delta = 0, 1
        elif steps[0] == 'L':
            axis, delta = 0, -1
        elif steps[0] == 'U':
            axis, delta = 1, 1
        elif steps[0] == 'D':
            axis, delta = 1, -1

        nsteps = int(steps[1:])

        for i in range(nsteps):
            path_pos[axis] += delta
            steps_travelled += 1
            path_dict[tuple(path_pos)] = steps_travelled

    return(path_dict)


path_set_1 = create_coord_set(path1)
path_set_2 = create_coord_set(path2)

if debug:
    print(path_set_1)

intersections = list()
distances = list()

for key, value in path_set_1.items():
    if key in path_set_2.keys():
        intersections.append(key)
        distances.append(path_set_1[key] + path_set_2[key])

if debug:
    print(intersections)

print(min(distances))
