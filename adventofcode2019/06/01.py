# I think a Directed Acyclic Graph (DAG) makes this easy

import networkx as nx
from networkx.algorithms import resistance_distance

debug = False

filename = 'test-input' if debug else 'input'

graph = nx.DiGraph()

with open(filename) as f:
    for line in f:
        left, right = line.strip().split(')')
        if left not in graph:
            graph.add_node(left)
        if right not in graph:
            graph.add_node(right)
        graph.add_edge(left, right)


n_nodes = len(graph)

if debug:
    print(len(graph))
    print('should be same as')
    print(len(nx.transitive_reduction(graph)))

if not nx.is_directed_acyclic_graph(graph):
    raise ValueError('Circular connections found! This is not a DAG :(')

total_ancestors = 0

for node in graph:
    n_ancestors = len(nx.ancestors(graph, node))
    total_ancestors += n_ancestors
    if debug:
        print(f'Node {node} has {n_ancestors} ancestors')

print(f'Total orbitees: {total_ancestors}')
