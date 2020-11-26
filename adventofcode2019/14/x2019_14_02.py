import math
from collections import defaultdict, Counter, deque

# import os
# os.chdir("/home/alexx/github/puzzles/adventofcode2019/14")


class Recipe:
    def __init__(self, line):
        self.line = line
        inputs, output = line.split(' => ')
        output_quantity, output_substance = output.split()

        self.name = output_substance
        self.input_substances = [x.split()[1] for x in inputs.split(', ')]
        self.input_quantities = [int(x.split()[0]) for x in inputs.split(', ')]
        self.output_quantity = int(output_quantity)

    def __str__(self):
        return self.line


with open('input') as file:
    data = file.read().splitlines()

recipes = dict()
DAG = dict()

for line in data:
    print(line)
    r = Recipe(line)
    recipes[r.name] = r

    # The DAG must be built inversely: The key must be the input substance.
    # Otherwise finding a sink is harder (we'd have to find a source instead)
    for inp_sub in r.input_substances:
        if inp_sub in DAG:
            DAG[inp_sub].append(r.name)
        else:
            DAG[inp_sub] = [r.name]
DAG['FUEL'] = []  # add the final sink, FUEL, to the DAG

print('*' * 60)

# Now I have a Directed Acyclic Graph, represented as
# Node v: [List of all nodes this node v depends on].
# Let's create a topological sort to find out in which order to resolve the FUEL to its ingredients,
# and ultimately to ORE.


def find_sink(dag):
    current_key = next(iter(dag))  # any random key from the dict is good
    while dag[current_key]:  # while the current node (i.e. substance) is not a sink, i.e. is a non-resolved ingredient
        current_key = dag[current_key][0]  # just take any, e.g. the first dependent substance

    return current_key


topo_order = deque()

while DAG:
    some_sink = find_sink(DAG)
    topo_order.appendleft(some_sink)
    del DAG[some_sink]
    # you also must delete all "DAG edges" that lead to this resulting substance:
    if some_sink != 'ORE':
        for inp_sub in recipes[some_sink].input_substances:
            DAG[inp_sub].remove(some_sink)

print(topo_order)

# Now we can traverse the deque backwards and fill out how many of each we need

we_need = defaultdict(int)
# 79938321 is too high
we_need['FUEL'] = 7993831  # Brute force binary search :3

while topo_order:
    substance = topo_order.pop()
    if substance == 'ORE':
        break

    r = recipes[substance]
    for inp_sub_quantity, inp_sub_name in zip(r.input_quantities, r.input_substances):

        # We might need more than we_need[substance] amount. E.g. if we need 23 B, but the recipe says 8 ORE => 3 B,
        # then we have to produce 24 B.
        amount_needed = math.ceil(we_need[substance] / r.output_quantity) * r.output_quantity
        we_need[inp_sub_name] += inp_sub_quantity / r.output_quantity * amount_needed

print(we_need['ORE'])
