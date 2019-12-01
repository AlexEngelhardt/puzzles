import re

class Tree:
    def __init__(lines):
        lines = [l.strip() for l in lines]
        lines = [line.replace(",", "").replace("(", "").replace(")", "") for line in lines]
    
class Program:
    pass

class Disc:
    pass

    
with open("input_mock.txt", "r") as f:
    lines = f.readlines()

tree = Tree(lines)


# make a dictionary of {program: weight}
weights = {}
total_weights = {}
for line in lines:
    l = line.split(" ")
    weights[l[0]] = int(l[1])
    # if it's a leaf node (i.e. has no children), then its weight is also its total weight:
    if len(l) == 2:
        total_weights[l[0]] = int(l[1])

print(weights)

# 
