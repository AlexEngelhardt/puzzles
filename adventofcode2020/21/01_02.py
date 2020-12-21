from collections import defaultdict

debug = False

if debug:
    filename = 'test_input'
else:
    filename = 'input'

with open(filename) as f:
    lines = f.read().splitlines()


# Create a nice data structure

def get_d(lines):
    d = defaultdict(list)
    for line in lines:
        ingredients, allergens = line.split(' (contains ')
        ingredients = ingredients.split(' ')
        allergens = allergens.replace(')', '').split(', ')
        for allergen in allergens:
            d[allergen].append(ingredients)
    return d


d = get_d(lines)

if debug:
    for k, v in d.items():
        print(f'{k}: ')
        for l in v:
            print('  ', l)

# Iteratively: Find one ingredient<->allergen connection, then remove that allergen from the dict,
# and that ingredient from all other allergen's lists

# We find one of these connections when there is an allergen (e.g. dairy) which has only one ingredient in each
# of its lists (in the test input, for dairy that's mxmxvkd). Note: For fish, we have *two* candidates:
# mxmxvkd and sqjhc. We have to identify dairy<->mxmxvkd first, before we can identify fish<->sqjhc


def get_candidates(ing_list):
    """Finds the ingredients which appear in each sublist of ing_list"""
    ing_set = [set(f) for f in ing_list]
    res = list(set.intersection(*ing_set))
    return res


print(get_candidates(d['fish']))  # should be mxmxvkd, sqjhc

connections = []

while d:
    for allergen in list(d):
        ingredients_list = d[allergen]
        candidates = get_candidates(ingredients_list)
        if len(candidates) == 1:  # Then we found an ingredient<->allergen connection!
            ingredient = candidates[0]
            # Add that connection to the result set:
            connections.append((allergen, ingredient))
            # Remove the allergen from your dict `d`:
            del d[allergen]
            # Remove the ingredient from every sublist in your main dict `d`
            for a, ing_l in d.items():
                for ing_subl in ing_l:
                    if ingredient in ing_subl:
                        ing_subl.remove(ingredient)  # I hope this works, i.e. I hope lists are edited call-by-reference style
            # Reiterate
            break

print(connections)

# I bet the above already solves part 2 :)

################################################################
# Solve part 1:

# Which ingredients don't contain any allergen?
all_ingredients = set()
dirty_ingredients = set([c[1] for c in connections])
d = get_d(lines)  # rebuild it, cause we manipulated the original `d` in the while loop above
print(d)
for k, v in d.items():
    for v_i in v:
        for ingredient in v_i:
            all_ingredients.add(ingredient)

clean_ingredients = all_ingredients - dirty_ingredients

if debug:
    print(clean_ingredients)

# Count how often these clean ingredients appear in your entire list:
total = 0
for line in lines:
    ingredients = line.split(' (')[0].split(' ')
    for ingredient in ingredients:
        if ingredient in clean_ingredients:
            total += 1
print(total)

################################################################
# Part 2

print(connections)
sorted_connections = sorted(connections, key=lambda x: x[0])
print(sorted_connections)
cdil = [x[1] for x in sorted_connections]
print(",".join(cdil))
