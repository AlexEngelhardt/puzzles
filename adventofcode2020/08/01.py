from assembler import Computer

# Test input:

with open('test_input') as f:
    lines = f.read().splitlines()
cptr = Computer()
cptr.load(lines)
ret = cptr.run()
print(f'Exit code: {ret}')

# Part 1, real input:

with open('input') as f:
    lines = f.read().splitlines()
cptr = Computer()
cptr.load(lines)
ret = cptr.run()
print(f'Exit code: {ret}')
