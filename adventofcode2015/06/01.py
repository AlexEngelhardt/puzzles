import functions as f

# Test everything

test_grid = f.create_grid(3, 3)
f.print_grid(test_grid)
instructions = open('test-input-3x3', 'r')
for line in instructions:
    operation = f.parse_op(line)
    test_grid = f.op_step(operation, test_grid)
    f.print_grid(test_grid)

print(f.get_n_on(test_grid))

# Real input

grid = f.create_grid(1000, 1000)
instructions = open('input', 'r')
for line in instructions:
    operation = f.parse_op(line)
    grid = f.op_step(operation, grid)

f.get_n_on(grid)
