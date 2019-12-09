import numpy as np

debug = False
filename = 'test-input' if debug else 'input'
dims = [2, 3] if debug else [6, 25]

with open(filename) as f:
    digits = list(map(int, list(f.read().strip())))

digits = np.array(digits).reshape(-1, dims[0], dims[1])

# the first image (index 0), at the second row (index 1)
# and third column (index 2):
digits[0][1][2]

n_layers = digits.shape[0]

smallest_n_zeros = dims[0] * dims[1]  # initialize with largest possible value

for i in range(n_layers):
    layer = digits[i]
    n_zeros = (layer == 0).sum()
    if n_zeros < smallest_n_zeros:
        target_layer = layer
        smallest_n_zeros = n_zeros

n_ones = (target_layer == 1).sum()
n_twos = (target_layer == 2).sum()

print(n_ones * n_twos)

