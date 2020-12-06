def group_to_set(g):
    res = g.replace('\n', '')
    return set(list(res))


# Test

with open('test_input') as f:
    groups = f.read().split('\n\n')

print(groups)

groups = list(map(group_to_set, groups))
print(groups)

print(sum(map(len, groups)))

# Part 1

with open('input') as f:
    groups = f.read().split('\n\n')
groups = list(map(group_to_set, groups))
print(sum(map(len, groups)))
