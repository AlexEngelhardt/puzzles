import numpy as np

M_list = []
with open('input') as f:
    for line in f:
        three_ints = list(map(int, line.strip().split('x')))
        M_list.append(sorted(three_ints))

M = np.array(M_list)

areas = (2 * M[:, 0] * M[:, 1] +
         2 * M[:, 0] * M[:, 2] +
         2 * M[:, 1] * M[:, 2] +
         M[:, 0] * M[:, 1]
         )

areas.sum()

