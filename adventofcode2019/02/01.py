debug = False

filename = 'test-input' if debug else 'input'

with open(filename) as f:
    codes = list(map(int, f.read().split(',')))

if debug:
    print(codes)
else:
    codes[1] = 12
    codes[2] = 2


for i in range(0, len(codes) - 4, 4):

    opcode = codes[i]
    if opcode == 99:
        print('99 encountered')
        break

    idx_left = codes[i+1]
    idx_right = codes[i+2]
    idx_target = codes[i+3]

    if debug:
        print(f'i: {i}')
        print(f'idx_left: {idx_left}')
        print(f'idx_right: {idx_right}')
        print(f'idx_target: {idx_target}')

    left = codes[idx_left]
    right = codes[idx_right]

    if opcode == 1:
        result = left + right
    elif opcode == 2:
        result = left * right
    else:
        raise ValueError('Wrong opcode')

    codes[idx_target] = result

print(codes[0])
