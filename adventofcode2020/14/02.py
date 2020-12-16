import re

debug = False
# debug = True  # Don't run this script with debug==True. The test_input mask contains a ton of 'X's, the recursion will be insane.

if debug:
    filename = 'test_input'
else:
    filename = 'input'

with open(filename) as f:
    lines = f.read().splitlines()


def set_bit(decimal_number, bit, value):
    """Sets the bit at position `bid` (zero-based count) to `value`"""
    # https://stackoverflow.com/questions/47981/how-do-you-set-clear-and-toggle-a-single-bit
    if value == 0:
        return decimal_number & ~(1 << bit)
    elif value == 1:
        return decimal_number | (1 << bit)
    else:
        raise ValueError('value must be 0 or 1')


def mask_address(address, mask):
    # All positions (counted from the end) that need to be set to 1
    ones = [i for i, c in enumerate(mask[::-1]) if c == '1']
    for one_pos in ones:
        address = set_bit(address, one_pos, 1)

    if 'X' not in mask:
        return [address]
    else:
        bit_pos_from_right = mask[::-1].index('X')
        new_mask = mask[::-1].replace('X', '0', 1)[::-1]  # replace first occurrence from the right
        address_0 = set_bit(address, bit_pos_from_right, 0)
        address_1 = set_bit(address, bit_pos_from_right, 1)
        result_0 = mask_address(address_0, new_mask)
        result_1 = mask_address(address_1, new_mask)
        return result_0 + result_1


# Test mask function:
print('Masking 58 with X00000, should be 26, 58:')
print(mask_address(58, '00X00000'))

print('Masking 42 with X1001X, should be 26, 27, 58, 59:')
print(mask_address(42, '0000X1001X'))

# Part 2
mem = dict()  # an array would take too much space!
mask = '0' * 36

for i, line in enumerate(lines):
    cmd, arg = line.split(' = ')
    if cmd == 'mask':
        mask = arg
    elif cmd.startswith('mem'):
        mem_i = re.search(r"\[(\d+)\]", cmd).group(1)
        masked_addresses = mask_address(int(mem_i), mask)
        for addr in masked_addresses:
            mem[addr] = int(arg)

mem_sum = 0
for k, v in mem.items():
    mem_sum += v

print(mem_sum)
