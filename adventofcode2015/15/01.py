def parse_ingredients(lines):
    res = dict()
    for line in lines:
        ingred, scores = line.split(': ')
        scores = scores.split(', ')
        res[ingred] = dict()
        for score in scores:
            name, s = score.split()
            res[ingred][name] = int(s)
    return res


with open('test_input') as f:
    test_lines = f.read().splitlines()
    test_ingredients = parse_ingredients(test_lines)

print(test_ingredients)


def get_score(recipe, ingredients):
    scores = dict()
    for k, v in recipe.items():
        ingredients[k]


recipe = {'Butterscotch': 44, 'Cinnamon': 56}
print(get_score(recipe, test_ingredients))
