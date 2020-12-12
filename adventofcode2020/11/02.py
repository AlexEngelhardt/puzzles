import itertools


debug = False

if debug:
    filename = 'test_input'
else:
    filename = 'input'

with open(filename) as f:
    seats = f.read().splitlines()


def neighbors(row, col, seats):
    """Returns between three and eight (we include diagonals) neighbor cells"""

    # (row, col)
    directions = (
        (-1, 0),  # up
        (1, 0),  # down
        (0, -1),  # left
        (0, 1),  # right
        (-1, -1),  # up-left
        (1, -1),  # down-left
        (-1, 1),  # up-right
        (1, 1)  # down-right
    )

    res = []

    for row_step, col_step in directions:
        # Start at (row, col) and walk into a specific direction until you hit a seat or the end of the grid
        cur_row, cur_col = row, col

        while True:
            cur_col += col_step  # was: x
            cur_row += row_step  # was: y

            if not 0 <= cur_row < len(seats):
                break
            if not 0 <= cur_col < len(seats[0]):
                break

            if seats[cur_row][cur_col] in ['#', 'L']:
                res.append((cur_row, cur_col))
                break

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
                for r, c in neighbors(row, col, seats):
                    if seats[r][c] == '#':
                        n_occupied += 1
                new_seats[row][col] = '#' if n_occupied == 0 else 'L'

            elif seats[row][col] == '#':  # full seat
                n_occupied = 0
                for r, c in neighbors(row, col, seats):
                    if seats[r][c] == '#':
                        n_occupied += 1
                new_seats[row][col] = 'L' if n_occupied >= 5 else '#'

    new_seats = [''.join(row) for row in new_seats]
    return new_seats


def pr(s):
    for r in s:
        print(r)
    print()


def n_seats_occupied(seats):
    return sum([row.count('#') for row in seats])


if debug:
    pr(seats)
    seats = step(seats)
    pr(seats)
    seats = step(seats)
    pr(seats)
else:
    old_seats = seats.copy()
    seats = step(seats)

    while seats != old_seats:
        old_seats = seats.copy()
        seats = step(seats)

    print(n_seats_occupied(seats))
