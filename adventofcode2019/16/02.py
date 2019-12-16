import numpy as np
import os
os.chdir('/home/alexx/github/puzzles/adventofcode2019/16')

debug = False

filename = 'test-input' if debug else 'input'

with open(filename) as f:
    numbers = np.array(list(map(int, f.read().strip())))


# OK, nothing with the "normal" approach works here, but there are a few hacks:

# - The pattern grid is a upper triangular matrix, i.e. for the "bottom half"
#   of the numbers, the "first half" doesn't even count.
# - Also, if you write out a 16x16 pattern matrix [0, 1, 0, -1], you'll see that
#   in the lower half of digits, we just sum() the last few digits in each row
# - Thus, a cumsum() (with a modulo 10) of the reverse of the input list will
#   produce the output list! Because we skip like 5.5 million of the 6.5 million
#   input digits, we don't care about the "hard" part at the beginning of the
#   input numbers.


def phase(input):
    output = input[::-1].cumsum()[::-1] % 10
    return output


n_phases = 100

numbers = np.tile(numbers, 10000)
skip_this_many = int(''.join(map(str, numbers[:7])))
numbers = numbers[skip_this_many:]

for p in range(n_phases):
    print(f'Phase {p+1}')
    numbers = phase(numbers)

''.join(map(str, numbers[:8]))

# 24162634 is too low
# 57920757 is right!
