with open('input') as f:
    lines = f.read().splitlines()

height = len(lines)
width = len(lines[0])


rows = range(len(lines))
columns = [(row * 3) % width for row in rows]
coords = zip(rows, columns)

fields = [lines[row][col] for row, col in coords]

n_trees = sum([1 for field in fields if field == '#'])
print(n_trees)
