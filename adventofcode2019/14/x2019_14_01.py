import math
from collections import defaultdict, Counter

# import os
# os.chdir("/home/alexx/github/puzzles/adventofcode2019/14")

class Recipe:
    def __init__(self, name, inputs, output_quantity):
        self.name = name
        self.input_substances = [x.split()[1] for x in inputs.split(', ')]
        self.input_quantities = [int(x.split()[0]) for x in inputs.split(', ')]
        self.output_quantity = int(output_quantity)
        self.ore_recipe = True if self.input_substances[0] == 'ORE' else False

    def __str__(self):
        iq = [str(q) for q in self.input_quantities]
        inputs = [" ".join(x) for x in zip(iq, self.input_substances)]
        inputs = ", ".join(inputs)
        return f'{inputs} => {self.output_quantity} {self.name}'


with open('test_input2') as file:
    data = file.read().splitlines()

reactions = []
recipes = dict()
ore_recipes = dict()

for line in data:
    print(line)
    inputs, output = line.split(' => ')
    out_quantity, out_substance = output.split()

    r = Recipe(name=out_substance, inputs=inputs, output_quantity=out_quantity)
    # if r.ore_recipe:
    #     ore_recipes[out_substance] = r
    # else:
    #     recipes[out_substance] = r
    recipes[out_substance] = r

# print(substances['FUEL'])

print('*' * 60)

################################################################

for k, r in ore_recipes.items():
    print(r)

print('*' * 60)

for k, r in recipes.items():
    print(r)

################################################################
# Resolve "2 FUEL"

target_substance = 'FUEL'
target_quantity = 1

print('*' * 60)


def resolve_1(recipes, target_substance, target_quantity):
    if target_substance not in recipes:
        return Counter({target_substance: target_quantity})

    r = recipes[target_substance]
    ingredients = r.input_substances
    quantities = [math.ceil(c * target_quantity / r.output_quantity) for c in r.input_quantities]

    ctr = Counter()
    for i, q in zip(ingredients, quantities):
        ctr += resolve_1(recipes, i, q)

    return ctr


print(resolve_1(recipes, target_substance, target_quantity))
