def create_grid(x, y, init_with=False):
    return [[init_with for y_i in range(y)] for x_i in range(x)]


def print_grid(grid):
    print('-' * (len(grid[0]) + 2))
    for line in grid:
        chars = ['X' if lamp else ' ' for lamp in line]
        print('-' + ''.join(chars) + '-')

    print('-' * (len(grid[0]) + 2))
    print()


def parse_op(line):
    operation = line.split(" ")
    if operation[0] == 'turn':
        opcode = operation[0] + ' ' + operation[1]
        ptr = 2
    else:
        opcode = operation[0]
        ptr = 1
    x_start, y_start = map(int, operation[ptr].split(","))
    x_stop, y_stop = map(int, operation[ptr + 2].split(","))
    # print(f"In this operation I will {opcode} from {x_start}, {y_start} to {x_stop}, {y_stop}")
    return opcode, x_start, x_stop, y_start, y_stop


def op_step(operation, grid):
    opcode, x_start, x_stop, y_start, y_stop = operation
    for x in range(x_start, x_stop+1):
        for y in range(y_start, y_stop+1):
            if opcode == 'turn on':
                grid[x][y] = True
            elif opcode == 'turn off':
                grid[x][y] = False
            elif opcode == 'toggle':
                grid[x][y] = not grid[x][y]
    return grid


def op_step2(operation, grid):
    opcode, x_start, x_stop, y_start, y_stop = operation
    for x in range(x_start, x_stop+1):
        for y in range(y_start, y_stop+1):
            if opcode == 'turn on':
                grid[x][y] = grid[x][y] + 1
            elif opcode == 'turn off':
                grid[x][y] = max(grid[x][y] - 1, 0)
            elif opcode == 'toggle':
                grid[x][y] = grid[x][y] + 2
    return grid


def get_n_on(grid):
    n_on = sum([x for row in grid for x in row])
    print(f"There's {n_on} on lights")
    return n_on