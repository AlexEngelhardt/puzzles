with open('input') as f:
    line = f.read()

floor = 0

for i, c in enumerate(line):
    if c == '(':
        floor += 1
    elif c == ')':
        floor -= 1
    else:
        raise ValueError('Weird character encountered')
    if floor == -1:
        print(i+1)
        break


