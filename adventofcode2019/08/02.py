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


def get_pixel(digits, row, col):
    first_nontransparent_idx = (digits[:, row, col] != 2).nonzero()[0][0]
    return digits[first_nontransparent_idx, row, col]


image = np.empty((dims[0], dims[1]))

for row in range(dims[0]):
    for col in range(dims[1]):
        image[row, col] = get_pixel(digits, row, col)

print(image)

import matplotlib.pyplot as plt

plt.imshow(image)
plt.show()
