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

################################################################
# Idea: Find the number of paths in the DAG from source to target:
# https://stackoverflow.com/questions/5164719/number-of-paths-between-two-nodes-in-a-dag

# 1.) Create a DAG of possible jumps in the joltages
#     Create it as an *adjacency list*

dag = [[] for _ in range(len(jolts))]

for i in range(len(jolts)):
    for jump_i in [1, 2, 3]:
        if i + jump_i >= len(jolts):  # end of list reached
            continue
        if jolts[i+jump_i] - jolts[i] <= 3:  # this means we can move to jolts[i+jump_i] from jolts[i]
            dag[i].append(i+jump_i)

print(dag)

# 2.) Walk the DAG backward. For each node, store the number of ways you can reach the end.
#     (it's the sum of the ways of each node you can directly reach from this source node)

n_paths = [1 for _ in range(len(jolts))]  # the 1 is only important for the very last node.

for i in reversed(range(len(dag)-1)):
    total_paths = 0
    for next_node in dag[i]:
        total_paths += n_paths[next_node]
    n_paths[i] = total_paths

# Answer is the first number in this list:
print(n_paths)


