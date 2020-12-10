debug = True

if debug:
    filename = 'test_input'
else:
    filename = 'input'

with open(filename) as f:
    lines = f.read().splitlines()
