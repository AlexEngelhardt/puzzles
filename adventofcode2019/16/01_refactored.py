import numpy as np
import os
os.chdir('/home/alexx/github/puzzles/adventofcode2019/16')

debug = False

filename = 'test-input' if debug else 'input'

with open(filename) as f:
    numbers = np.array(list(map(int, f.read().strip())))

numbers

def create_pattern(i, length):
    output = np.repeat([0, 1, 0, -1], i)
    if len(output) < length:
        output = np.tile(output, int(1 + length / len(output)))
    output = np.roll(output, -1)
    return output[:length]


def phase(input):
    N = len(input)
    output = np.empty(N, dtype=np.int64)

    for i in range(len(input)):
        this_pattern = create_pattern(i+1, N)
        output[i] = abs((input * this_pattern).sum()) % 10
    return output


n_phases = 100

for p in range(n_phases):
    numbers = phase(numbers)

print(numbers[:8])
