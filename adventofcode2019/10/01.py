# this attempt failed.
# The other x2020_01_01.py was smarter (where I computed angles between asteroids,
# and counted unique angles)

import numpy as np

import os
os.chdir('/home/alexx/github/puzzles/adventofcode2019/10')

debug = False

# test-input1 ok
# test-input2 ok
# test-input3 ok
# test-input4 I detect row6, col3 with 40 detected, but correct is row6, col3 with 41
# test-input5 I detect row14, col1 with 211 detected, but correct is row13, col11 with 210

filename = 'test-input4'

fieldlist = []

with open(filename) as f:
    for line in f:
        fieldlist.append([0 if c == '.' else 1 for c in line.strip()])

field = np.array(fieldlist)
print(field)


def visible(field, row_from, col_from, row_to, col_to):
    # Either: loop again over all other asteroids and determine
    # *for each asteroid* if it is blocking the path
    #
    # Or: Find all integer coordinates between 'from' and 'to' and
    # check if any one of them contains an asteroid
    #  - There is a mathematical formula for this
    #  - Alternatively, bruteforce it

    # Remember:
    #  row == y-axis
    #  col == x-axis

    if row_from > row_to:
        row_from, row_to = row_to, row_from
    if col_from > col_to:
        col_from, col_to = col_to, col_from

    if row_from == row_to:  # straight horizontal line
        if debug:
            print('horizontal line')
        int_coords_between = [(x, row_from) for x in range(col_from+1, col_to)]
    elif col_from == col_to:  # straight vertical line
        if debug:
            print('vertical line')
        # this does not work for lines that go e.g. from 7 to 5.
        # That's why we swap the coords in the beginning of this fct
        int_coords_between = [(col_from, y) for y in range(row_from+1, row_to)]
    else:
        if debug:
            print('fucky line')
        int_coords_between = list()
        slope = (row_to - row_from) / (col_to - col_from)
        intercept = row_to - slope * col_to
        passing_cols = range(col_from + 1, col_to)
        for passing_col in passing_cols:  # these are x-coords, remember!
            passing_row = slope * passing_col + intercept
            if float(passing_row).is_integer():
                int_coords_between += [(int(passing_col), int(passing_row))]

    if debug:
        print('Coordinates inbetween:')
        print(int_coords_between)

    for y, x in int_coords_between:
        # (y, x) because it's (row, col)
        if field[x][y] == 1:
            if debug:
                print(f'Found obstructing asteroid at row {y}, col {x}')
            return False
    if debug:
        print(f'({row_from}, {col_from}) can see ({row_to}, {col_to})!')

    return True


# if debug:
#     print(visible(field, 7, 2, 3, 2))  # expect False
#     print(visible(field, 7, 2, 5, 2))  # expect True

can_see = dict()
max_visible = 0

for row_from, col_from in zip(*np.where(field)):
    # The row and col of the candidate asteroids in the field
    n_visible = 0
    for row_to, col_to in zip(*np.where(field)):
        if (row_from == row_to) and (col_from == col_to):
            # Don't count you seeing yourself
            continue

        if debug:
            print(f'Can ({row_from}, {col_from}) see ({row_to}, {col_to})?')
        if visible(field, row_from, col_from, row_to, col_to):
            n_visible += 1
    can_see[(row_from, col_from)] = n_visible
    max_visible = max(max_visible, n_visible)

print(max_visible)
# 233 is too high
