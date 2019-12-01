import math

total = 0

with open('input', 'r') as f:
    for line in f:
        i = int(line)
        total += i // 3 - 2

print(total)
