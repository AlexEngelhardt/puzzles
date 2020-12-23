debug = False

if debug:
    order = list('389125467')
else:
    order = list('398254716')

current_label = order[0]


def step(order, current_label):
    print('cups: ', end='')
    for c in order:
        if c == current_label:
            print(f'({c}) ', end='')
        else:
            print(f'{c} ', end='')
    print()

    # Remove three clockwise cups
    removed_cups = []
    for _ in range(3):
        current_i = order.index(current_label)
        removed_cups.append(order.pop((current_i + 1) % len(order)))
    print(f'pick up: {" ".join(removed_cups)}')

    # Select the destination cup
    destination_label = str((int(current_label)-1-1 + 9) % 9 + 1)  # label minus one, wrapped around to 9
    while destination_label in removed_cups:
        destination_label = str((int(destination_label)-1-1 + 9) % 9 + 1)
    print(f'destination: {destination_label}')

    # Place cups at destination
    destination_i = order.index(destination_label) + 1
    order[destination_i:destination_i] = removed_cups  # wtf, but it works

    # Select new "current cup"
    current_i = order.index(current_label)
    new_i = (current_i + 1) % 9
    new_label = order[new_i]

    return order, new_label


n_moves = 10 if debug else 100

for move in range(1, n_moves+1):
    print(f'-- move {move} --')
    order, current_label = step(order, current_label)
    print()

print("".join(order))

# 47986253 is wrong
