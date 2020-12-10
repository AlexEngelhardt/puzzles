from collections import Counter

# debug = True
debug = False

if debug:
    filename = 'test_input'
else:
    filename = 'input'

with open(filename) as f:
    jolts = list(sorted(map(int, f.read().splitlines())))

# add the starting joltage 0 and the last joltage of max() + 3:
jolts = [0] + jolts + [max(jolts) + 3]

diffs = [jolts[i] - jolts[i-1] for i in range(1, len(jolts))]

print(diffs)

ctr = Counter(diffs)

print(ctr[1])
print(ctr[3])
print(ctr[3] * ctr[1])
