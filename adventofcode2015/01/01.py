with open('input') as f:
    line = f.read()

floor = 0
for c in line:
    if c == '(':
        floor += 1
    elif c == ')':
        floor -= 1
    else:
        raise ValueError('Weird character encountered')

print(floor)
