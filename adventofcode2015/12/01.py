import re

with open('input') as f:
    lines = f.read().splitlines()

matches = re.compile(r'-?\d+').findall(lines[0])

print(sum(map(int, matches)))
