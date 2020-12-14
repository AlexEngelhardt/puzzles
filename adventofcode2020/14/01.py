import re

debug = False
# debug = True

if debug:
    filename = 'test_input'
else:
    filename = 'input'

with open(filename) as f:
    lines = f.read().splitlines()


def mask_number(mask, number):
    or_mask = int(mask.replace('X', '0'), 2)
    and_mask = int(mask.replace('X', '1'), 2)
    return (number | or_mask) & and_mask


# Test the masking function:
mask = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X'
number = 101
print(mask_number(mask, number))

# Part 1
mem = dict()  # an array would take too much space!
mask = 'X' * 36

for line in lines:
    cmd, arg = line.split(' = ')
    if cmd == 'mask':
        mask = arg
    elif cmd.startswith('mem'):
        mem_i = re.search(r"\[(\d+)\]", cmd).group(1)
        mem[mem_i] = mask_number(mask, int(arg))

mem_sum = 0
for k, v in mem.items():
    mem_sum += v

print(mem_sum)
