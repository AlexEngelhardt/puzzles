with open('input') as f:
    strings = f.read().splitlines()

total_diff = 0

for s in strings:
    # print(s)
    # print(eval(s))
    # print('----')
    total_diff += len(s) - len(eval(s))  # haha thx python :D

print(total_diff)
