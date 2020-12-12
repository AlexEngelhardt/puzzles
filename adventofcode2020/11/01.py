import itertools


debug = False

if debug:
    filename = 'test_input'
else:
    filename = 'input'

with open(filename) as f:
    seats = f.read().splitlines()


def neighbors(row, col, nrow, ncol):
    """Returns between three and eight (we include diagonals) neighbor cells"""

    possible_rows = []
    if row > 0:
        possible_rows.append(row-1)
    possible_rows.append(row)
    if row < nrow-1:
        possible_rows.append(row+1)

    possible_cols = []
    if col > 0:
        possible_cols.append(col-1)
    possible_cols.append(col)
    if col < ncol-1:
        possible_cols.append(col+1)

    res = list(itertools.product(possible_rows, possible_cols))
    # Remove the tuple (row, col) again, s.t. you have *only* neighbors, not the current seat itself:
    res.remove((row, col))
    return res


def step(seats):
    nrow = len(seats)
    ncol = len(seats[0])
    new_seats = [['*' for _ in range(ncol)] for _ in range(nrow)]

    for row in range(nrow):
        for col in range(ncol):
            if seats[row][col] == '.':  # floor tile
                new_seats[row][col] = '.'
            elif seats[row][col] == 'L':  # empty seat
                n_occupied = 0
                for r, c in neighbors(row, col, nrow, ncol):
                    if seats[r][c] == '#':
                        n_occupied += 1
                new_seats[row][col] = '#' if n_occupied == 0 else 'L'

            elif seats[row][col] == '#':  # full seat
                n_occupied = 0
                for r, c in neighbors(row, col, nrow, ncol):
                    if seats[r][c] == '#':
                        n_occupied += 1
                new_seats[row][col] = 'L' if n_occupied >= 4 else '#'

    new_seats = [''.join(row) for row in new_seats]
    return new_seats


def pr(s):
    for r in s:
        print(r)
    print()


def n_seats_occupied(seats):
    return sum([row.count('#') for row in seats])


if debug: pr(seats)
old_seats = seats.copy()
seats = step(seats)

while seats != old_seats:
    old_seats = seats.copy()
    seats = step(seats)

if debug: pr(seats)
print(n_seats_occupied(seats))
