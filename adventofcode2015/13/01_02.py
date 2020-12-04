from itertools import permutations

with open('input') as f:
    lines = f.read().splitlines()

# Parse lines to scores dict:

scores = dict()

for line in lines:
    words = line[:-1].split()
    person = words[0]
    other_person = words[-1]
    score = int(words[3])
    if words[2] == 'lose':
        score *= -1

    if person not in scores:
        scores[person] = dict()
    scores[person][other_person] = score

print(scores)


# Test all permutations and compute their scores:

def compute_score(order, scores):
    score = 0

    for i, person in enumerate(order):
        # left (previous) neighbor:
        left_neighbor = order[(i-1) % len(order)]
        # In Python, modulo of negative numbers works just like that! neat!
        # https://torstencurdt.com/tech/posts/modulo-of-negative-numbers/

        score += scores[person][left_neighbor]

        # right neighbor:
        right_neighbor = order[(i+1) % len(order)]

        score += scores[person][right_neighbor]

    return score


def get_best(scores):

    perms = list(permutations(scores.keys()))

    max_score = float('-inf')
    for perm in perms:
        this_score = compute_score(perm, scores)
        if this_score > max_score:
            max_score = this_score

    return max_score


print(get_best(scores))

################################################################
# Part 2:

scores['Alexx'] = dict()
for person in scores.keys():
    if person == 'Alexx':
        continue

    scores[person]['Alexx'] = 0
    scores['Alexx'][person] = 0

print(get_best(scores))