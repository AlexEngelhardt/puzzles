from collections import namedtuple
dude = namedtuple("Reindeer", ['name', 'speed_kms', 'running_seconds', 'resting_seconds'])


def parse_line(line):
    words = line.split()
    return dude(words[0], int(words[3]), int(words[6]), int(words[13]))


def distance_after(deer, seconds):
    # It's a kind of step function if you draw it.
    distance = 0
    iteration_time = deer.running_seconds + deer.resting_seconds
    # Full blocks:
    distance += (seconds // iteration_time) * deer.speed_kms * deer.running_seconds
    # Plus the last block:
    distance += min(seconds % iteration_time * deer.speed_kms, deer.running_seconds * deer.speed_kms)

    return distance


# Verify tests
with open('test_input') as f:
    test_lines = f.read().splitlines()
test_dudes = dict()
for test_line in test_lines:
    deer = parse_line(test_line)
    test_dudes[deer.name] = deer

print(distance_after(test_dudes['Comet'], 1000))
print(distance_after(test_dudes['Dancer'], 1000))


################################################################
# Part 1

with open('input') as f:
    lines = f.read().splitlines()
dudes = dict()
for line in lines:
    deer = parse_line(line)
    dudes[deer.name] = deer

max_distance = 0
for deer_name, deer in dudes.items():
    d = distance_after(deer, 2503)
    max_distance = max(max_distance, d)

print("Part 1:", max_distance)


################################################################
# Part 2

deer_names = dudes.keys()

deer_points = dict()
for dn in deer_names:
    deer_points[dn] = 0

for second in range(1, 2504):
    leading_deer = ''
    leading_distance = 0
    for dn in deer_names:
        this_deer_dist = distance_after(dudes[dn], second)
        if this_deer_dist > leading_distance:  # I'm assuming there will never be a tie
            leading_deer = dn
            leading_distance = this_deer_dist
    deer_points[leading_deer] += 1

print(deer_points)
