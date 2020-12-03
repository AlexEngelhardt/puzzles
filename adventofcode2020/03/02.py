with open('input') as f:
    lines = f.read().splitlines()

height = len(lines)
width = len(lines[0])


def get_n_trees(right_step=3, down_step=1):
    rows = range(0, len(lines), down_step)
    columns = [(i * right_step) % width for i in range(len(rows))]
    coords = zip(rows, columns)

    fields = [lines[row][col] for row, col in coords]

    n_trees = sum([1 for field in fields if field == '#'])
    return n_trees


print(get_n_trees(3, 1))

print(get_n_trees(1, 1) * get_n_trees(3, 1) * get_n_trees(5, 1) * get_n_trees(7, 1) * get_n_trees(1, 2))
