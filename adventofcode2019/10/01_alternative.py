import math
import numpy as np

import os
os.chdir('/home/alexx/github/puzzles/adventofcode2019/10')

debug = False
filename = 'input'

fieldlist = []
with open(filename) as f:
    for line in f:
        fieldlist.append([0 if c == '.' else 1 for c in line.strip()])
field = np.array(fieldlist)
print(field)

max_visible = 0

# for from_row, from_col in [(4, 3)]:
for from_row, from_col in zip(*np.where(field)):
    print(f'from_row: {from_row}, from_col: {from_col}')
    angles = set()
    for to_row, to_col in zip(*np.where(field)):
        if from_row == to_row and from_col == to_col:
            # from and to are same asteroids
            continue
        angle = math.atan2(to_row - from_row, to_col - from_col)

        # angle = round(
        #     math.atan2(to_row - from_row, to_col - from_col),
        #     4
        # )
        # print(f'({from_row}, {from_col}) -> ({to_row}, {to_col}): {angle}')
        # if angle in angles:
        #     print('OLD angle!')
        # else:
        #     print('new angle!')
        angles.add(angle)
    n_visible = len(angles)
    print(f'from_row: {from_row}, from_col: {from_col}: {len(angles)} visible')
    max_visible = max(max_visible, n_visible)

print(max_visible)
