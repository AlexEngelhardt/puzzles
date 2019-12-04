with open('input') as f:
    strpath = f.read()

locations = [[0, 0], [0, 0]]  # player 0 and 1, x, y
visited = dict()
visited[(0, 0)] = True
player = False  # is False if it's player 0's turn, True if player 1's turn.

for char in strpath:
    if char == '^':
        locations[player][1] += 1  # [1] is the y-coord, which you increase by 1
    elif char == 'v':
        locations[player][1] -= 1
    elif char == '<':
        locations[player][0] -= 1
    elif char == '>':
        locations[player][0] += 1
    else:
        raise ValueError('Wrong coord')
    visited[tuple(locations[player])] = True
    player = not player  # switch from player 1 to player 0 for next turn

print(len(visited))
