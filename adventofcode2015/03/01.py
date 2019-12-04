with open('input') as f:
    strpath = f.read()

location = [0, 0]  # x, y
visited = dict()
visited[tuple(location)] = True

for char in strpath:
    if char == '^':
        location[1] += 1  # [1] is the y-coord, which you increase by 1
    elif char == 'v':
        location[1] -= 1
    elif char == '<':
        location[0] -= 1
    elif char == '>':
        location[0] += 1
    else:
        raise ValueError('Wrong coord')
    visited[tuple(location)] = True

print(len(visited))
