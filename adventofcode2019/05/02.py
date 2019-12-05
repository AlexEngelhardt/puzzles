import os
os.chdir('/home/alexx/github/puzzles/adventofcode2019/05')

debug = True
INPUT = 5


def get_value(memory, mode, address):
    if mode == 0:  # position mode
        return memory[address]
    elif mode == 1:
        return address
    else:
        raise ValueError('Invalid mode')


def parse_instruction(instruction):
    print(f'instruction: {instruction}')
    opcode = instruction % 100
    print(f'opcode: {opcode}')

    if opcode in [1, 2, 7, 8]:
        instruction_length = 4
    elif opcode in [3, 4]:
        instruction_length = 2
    elif opcode in [5, 6]:
        instruction_length = 3
    else:
        raise ValueError('Invalid opcode')

    n_parameters = instruction_length - 1
    parameters = [instruction // 10 ** (2+x) % 10 for x in range(n_parameters)]

    return opcode, parameters, instruction_length


with open('input') as f:
    memory = list(map(int, f.read().split(',')))

mem_size = len(memory)
if debug:
    print(f'Memory size: {mem_size}')

instruction_pointer = 0

while instruction_pointer < mem_size:

    instruction = memory[instruction_pointer]

    opcode, parameters, instruction_length = parse_instruction(instruction)

    if debug:
        print(memory[
            instruction_pointer:
            (instruction_pointer+instruction_length)
        ])

    if opcode == 99:
        print('99 encountered')
        break

    if opcode in [1, 2, 7, 8]:
        left = memory[
            get_value(memory, parameters[0], instruction_pointer + 1)
        ]
        right = memory[
            get_value(memory, parameters[1], instruction_pointer + 2)
        ]
        # TODO: target_addr could have a fixed 0 instead of parameters[2],
        # because write locations are always in position mode.
        target_addr = get_value(memory, parameters[2],
                                instruction_pointer + 3)

        if debug:
            print(f'target_addr = {target_addr}')

        if opcode == 1:
            memory[target_addr] = left + right
        elif opcode == 2:
            memory[target_addr] = left * right
        elif opcode == 7:
            memory[target_addr] = int(left < right)
        elif opcode == 8:
            memory[target_addr] = int(left == right)
    elif opcode == 3:
        target_addr = get_value(memory, parameters[0],
                                instruction_pointer + 1)
        memory[target_addr] = INPUT
    elif opcode == 4:
        target_addr = get_value(memory, parameters[0],
                                instruction_pointer + 1)

        output = memory[target_addr]
        if output == 0:
            # Per problem statement, this means the program is running okay
            # until now
            continue
        else:
            print(f"Problem answer: {output}")
            break
    elif opcode in [5, 6]:
        if opcode == 5:
            thebool = memory[
                get_value(memory, parameters[0], instruction_pointer + 1)
            ]

            if thebool != 0:
                instruction_pointer = memory[
                    get_value(memory, parameters[1], instruction_pointer + 2)
                ]
                continue  # i.e., don't increase the instruction pointer
        elif opcode == 6:
            thebool = memory[
                get_value(memory, parameters[0], instruction_pointer + 1)
            ]

            if thebool == 0:
                instruction_pointer = memory[
                    get_value(memory, parameters[1], instruction_pointer + 2)
                ]
                continue  # i.e., don't increase the instruction pointer
    else:
        raise ValueError('Invalid opcode')

    instruction_pointer += instruction_length


