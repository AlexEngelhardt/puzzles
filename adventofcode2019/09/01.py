from computer import Computer

with open('input') as f:
    memory = list(map(int, f.read().split(',')))

computer = Computer(memory, debug=True)
computer.run()
