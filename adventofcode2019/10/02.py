import os
import math
import cmath
import numpy as np
from itertools import cycle
from collections import defaultdict

os.chdir('/home/alexx/github/puzzles/adventofcode2019/10')

debug = False
filename = 'test-input1'
filename = 'input'

fieldlist = []
with open(filename) as f:
    for line in f:
        fieldlist.append([0 if c == '.' else 1 for c in line.strip()])
field = np.array(fieldlist)
print(field)

max_visible = 0

for from_row, from_col in zip(*np.where(field)):
    angles = set()
    for to_row, to_col in zip(*np.where(field)):
        if from_row == to_row and from_col == to_col:
            # from and to are same asteroids
            continue
        angle = math.atan2(to_row - from_row, to_col - from_col)
        angles.add(angle)
    n_visible = len(angles)
    # print(f'from_row: {from_row}, from_col: {from_col}: {len(angles)} visible')
    if n_visible > max_visible:
        max_visible = n_visible
        best_asteroid = (from_row, from_col)

print(f'Best asteroid: ({best_asteroid[0]}, {best_asteroid[1]}) '
      f'with {max_visible} visible')

################################################################
# Now use the correct notation, because the directions will be important.
# X is the distance from the left edge
# Y is the distance from the top edge
#  so the top-left corner is 0,0
#  the position immediately to its right is 1,0

Y, X = best_asteroid

target_asteroids = [(x, y) for y, x in zip(*np.where(field))]
target_asteroids.remove((X, Y))
target_asteroids

roids = defaultdict(list)

for x, y in target_asteroids:
    # Careful with math here. We need some rotations.
    # e.g. the mathy y-axis goes up, while the AoC problem y-axis goes down:
    dist, angle = cmath.polar(complex(x-X, Y-y))

    # angle goes from -pi to +pi, but we need the clockwise rotational
    # direction starting from the (0, 1) vector

    if angle < 0:
        # transform from negative rotation downwards (range -pi to +pi)
        # to full-circle rotation from 0 to 2pi
        angle = 2 * math.pi + angle
    assert angle <= 2 * math.pi

    # Now instead of rotating ccw from (1, 0), rotate cw from (0, 1):
    angle = -angle  # rotate ccw
    angle = (angle + math.pi/2) % (2*math.pi)  # start rotation from (0, 1)

    angle = round(angle, 4)  # avoid float inequalities in dict keys

    roids[angle].append({'x': x, 'y': y, 'dist': dist})

    print(f'({x}, {y}): angle {angle} and dist {dist}')

# sort all values by distance:
for k, v in roids.items():
    roids[k] = sorted(roids[k], key=lambda x: x['dist'])

angles = sorted(roids.keys())
angle_cycle = cycle(angles)

i = 1
boom = 0
while True:
    angle = next(angle_cycle)

    if roids[angle]:
        boom += 1
        print(f"POW! ({roids[angle][0]['x']}, {roids[angle][0]['y']}) "
              f"destroyed! (nr. {boom})")
        roids[angle].pop(0)

    if boom == 200:
        break

    # Just an inf loop protection :)
    i += 1
    if i > 10000:
        break
