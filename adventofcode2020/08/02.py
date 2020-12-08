from assembler import Computer
cptr = Computer()


def swap_statement(lines, nth_statement=0):
    """Swaps the `nth` occurrence of a 'jmp' or 'nop' statement into its opposite"""
    statement_ctr = 0
    for i in range(len(lines)):
        this_line_cmd = lines[i].split()[0]
        if this_line_cmd in ['jmp', 'nop']:
            if statement_ctr == nth_statement:
                if this_line_cmd == 'jmp':
                    lines[i] = 'nop' + lines[i][3:]
                elif this_line_cmd == 'nop':
                    lines[i] = 'jmp' + lines[i][3:]
                else:
                    raise Exception("Shouldn't reach this statement!")
                break
            else:
                statement_ctr += 1
    # TODO This has no checks whether a statement was swapped. If nth_statement is too large, nothing gets changed.

    return lines


# Test input:

with open('test_input') as f:
    lines = f.read().splitlines()
cptr.load(lines)
ret = cptr.run()
print(f'Exit code: {ret}')

# Test input, fixed manually:

with open('test_input_fixed') as f:
    lines = f.read().splitlines()
cptr.load(lines)
ret = cptr.run()
print(f'Exit code: {ret}')
print(f'Accumulator: {cptr.accumulator}')

# Test input, fixed automatically:

with open('test_input') as f:
    orig_lines = f.read().splitlines()

swap_statement_i = 0
while True:
    lines = orig_lines.copy()
    lines = swap_statement(lines, swap_statement_i)

    cptr.load(lines)
    ret = cptr.run()
    if ret == 0:  # i.e. program exited successfully, without an infinite loop
        print(f'Program exited successfully, accumulator = {cptr.accumulator}')
        break

    swap_statement_i += 1


# Part 2, real input:

with open('input') as f:
    orig_lines = f.read().splitlines()

swap_statement_i = 0
while True:
    lines = orig_lines.copy()
    lines = swap_statement(lines, swap_statement_i)

    cptr.load(lines)
    ret = cptr.run()
    if ret == 0:  # i.e. program exited successfully, without an infinite loop
        print(f'Program exited successfully, accumulator = {cptr.accumulator}')
        break

    swap_statement_i += 1
