from computer import Computer

with open('input') as f:
    memory = list(map(int, f.read().split(',')))

computer = Computer(memory, inputs=[1], debug=False)
computer.run()

# 203 is too low
# BUT:
# It will perform a series of checks on each opcode, output
# any opcodes (and the associated parameter modes) that seem to be functioning
# incorrectly,
