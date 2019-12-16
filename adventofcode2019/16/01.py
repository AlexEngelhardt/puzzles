import os
os.chdir('/home/alexx/github/puzzles/adventofcode2019/16')

debug = False

filename = 'test-input' if debug else 'input'

with open(filename) as f:
    numbers = list(map(int, f.read().strip()))

numbers


def rep_each(input, times):
    output = []
    for elem in input:
        for i in range(times):
            output.append(elem)
    return output


def phase(input, pattern):
    output = []
    for i, char in enumerate(input):
        this_pattern = rep_each(pattern, i+1)
        this_pattern = this_pattern[1:] + this_pattern[:1]
        this_pattern = this_pattern[:len(input)]
        if len(this_pattern) < len(input):
            this_pattern = (
                this_pattern * int(1+(len(input) / len(this_pattern)))
            )[:len(input)]
        newchar = abs(sum([a*b for a, b in zip(input, this_pattern)])) % 10
        output += [newchar]
    return output


n_phases = 100

this_numbers = numbers.copy()
for p in range(n_phases):
    this_numbers = phase(this_numbers, pattern=[0, 1, 0, -1])
    str_out = ''.join(list(map(str, this_numbers)))
    # print(f'After {p+1} phases: {str_out}')

print(''.join(map(str, this_numbers))[:8])
