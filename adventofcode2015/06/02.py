import functions as f

grid = f.create_grid(1000, 1000, init_with=0)
instructions = open('input', 'r')
for line in instructions:
    operation = f.parse_op(line)
    grid = f.op_step2(operation, grid)

f.get_n_on(grid)  # this function still works even though it was designed to count the number of on lights :)
