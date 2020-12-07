test = False

inputfile = 'test_input' if test else 'input'
with open(inputfile) as f:
    lines = f.read().splitlines()


# First, parse the rules into something easier

def parse_line(l):
    bag, contains = l.split(' contain ')
    bag = bag.replace(' bags', '')

    if contains == 'no other bags.':
        contains = []
    else:
        contains = contains.replace('.', '').split(', ')
        contains = [(int(x.split()[0]), ' '.join(x.split()[1:3])) for x in contains]

    rule = bag, contains
    return rule


rules = [parse_line(l) for l in lines]
color_names = [x[0] for x in rules]

# Now, create a DAG of the rules (represented as an adjacency list)

graph = dict()
for r in rules:
    graph[r[0]] = list()
    for c in r[1]:
        graph[r[0]].append(c)


# Part 1: Find, then count all nodes *from* which you can reach "shiny gold".
# I could loop over all bag colors and for each color, explore() the graph and see if you can reach "shiny gold".
# BUT:
# It seems easier to *invert* the graph's edges and explore() *only once*, from "shiny gold".
# Then just count all nodes you reach from there.

def invert_graph(graph):
    """Invert a DAG (and forget the weights for now; we don't need them)"""
    inv_graph = dict()
    for key in graph:
        inv_graph[key] = []

    for key, val in graph.items():
        for edge in val:
            dest_col = edge[1]  # edge[0] is the edge weight
            inv_graph[dest_col].append(key)

    return inv_graph


def explore(graph, start_node, visited=None):
    if visited is None:
        visited = {col: False for col in graph.keys()}
    visited[start_node] = True
    for destination in graph[start_node]:
        if not visited[destination]:
            visited = explore(graph, destination, visited)
    return visited


print(graph)
print(invert_graph(graph))
print(explore(invert_graph(graph), 'shiny gold'))

visited = explore(invert_graph(graph), 'shiny gold')
n_bags = sum([visited[x] for x in visited.keys()]) - 1  # subtract one because 'shiny gold' itself is in there
print('Part 1:', n_bags)


# Part 2: Aggregate "top-down" recursively, starting from "shiny gold": For each outgoing node in the
# original (not the inverted one from Part 1) DAG, sum up its constituent bags and multiply them with
# the edge weight.

def aggregate(graph, node):
    print(f'aggregating {node}')
    count = 1
    # if `node` is a sink node (i.e. contains no other bags), we'll return 1 (because it's still one bag)

    for edge in graph[node]:
        weight, target_node = edge
        count += aggregate(graph, target_node) * weight

    print(f'{node} has {count} bags within')
    return count


print(aggregate(graph, 'shiny gold') - 1)  # again subtract 1 to remove the beginning "shiny gold" bag
