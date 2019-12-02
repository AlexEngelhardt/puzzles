with open('input') as f:
    orig_codes = list(map(int, f.read().split(',')))


def try_inputs(orig_codes, left=12, right=2):

    codes = orig_codes.copy()

    codes[1] = left
    codes[2] = right

    for i in range(0, len(codes) - 4, 4):
        opcode = codes[i]
        if opcode == 99:
            break

        idx_left = codes[i+1]
        idx_right = codes[i+2]
        idx_target = codes[i+3]

        left = codes[idx_left]
        right = codes[idx_right]

        if opcode == 1:
            result = left + right
        elif opcode == 2:
            result = left * right
        else:
            raise ValueError('Wrong opcode')

        codes[idx_target] = result

    return(codes[0])


target = 19690720


# Brute force takes < 1 second
for left in range(100):
    for right in range(100):
        if try_inputs(orig_codes, left, right) == target:
            print(f'DONE! left = {left}, right = {right}')
