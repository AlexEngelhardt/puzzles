with open('input', 'r') as f:
    total = sum([int(i) // 3 - 2 for i in f])

print(total)
