# I think a Directed Acyclic Graph (DAG) makes this easy

import networkx as nx
from networkx.algorithms import resistance_distance

debug = False

filename = 'test-input' if debug else 'input'

# The only change: For Part 2, networkx needs an *undirected* graph:
graph = nx.Graph()

with open(filename) as f:
    for line in f:
        left, right = line.strip().split(')')
        if left not in graph:
            graph.add_node(left)
        if right not in graph:
            graph.add_node(right)
        graph.add_edge(left, right)


n_nodes = len(graph)

# Minus two because the steps from YOU and to SAN are not counted
print(resistance_distance(graph, 'YOU', 'SAN') - 2)
