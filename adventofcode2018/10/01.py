import re
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull

debug = False

filename = 'test-input' if debug else 'input'
frames = 10 if debug else 20000

figures_only_at = [0, 10] if debug else [10580, 10680]

points = np.ndarray(shape=(0, 2))
velocities = np.ndarray(shape=(0, 2))

with open(filename) as f:
    for line in f:
        x1, x2, v1, v2 = re.findall(r'(-?\d+)', line)
        points = np.vstack((points, [int(x1), int(x2)]))
        velocities = np.vstack((velocities, [int(v1), int(v2)]))

areas = np.empty(frames)
the_max = frames

for i in range(frames):
    if not i % 1000:
        print(f'iteration {i}')
    # print(f'After {i} steps')
    areas[i] = ConvexHull(points).area
    # print(f'Convex hull: {areas[i]}')

    if i in range(figures_only_at[0], figures_only_at[1]):
        # For some reason, we have to flip the y axis, i.e. use
        # the negative of points[:, 1] for plotting
        plt.scatter(points[:, 0], -points[:, 1])
        plt.savefig(f'img/{i}.jpg')
        plt.close()

    if (areas[i] > areas[i-1]) and (areas[i-2] > areas[i-1]):
        print(f'Local minimum found at i={i-1}')
        # If you found a minimum of the convex hull, run this loop for
        # 10 more steps, then abort.
        the_max = i + 10
    if i > the_max:
        break

    points += velocities  # advance one frame
