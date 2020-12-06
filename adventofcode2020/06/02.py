import functools


def group_to_set(g):
    persons = g.strip().split('\n')  # ['ab', 'ac']
    person_sets = map(lambda x: set(list(x)), persons)  # [{'a', 'b']}, {'a', 'c'}]

    return functools.reduce(set.intersection, person_sets)


# Test

with open('test_input') as f:
    groups = f.read().split('\n\n')

print(groups)

groups = list(map(group_to_set, groups))
print(groups)

print(sum(map(len, groups)))

# Part 2

with open('input') as f:
    groups = f.read().split('\n\n')
groups = list(map(group_to_set, groups))
print(sum(map(len, groups)))
