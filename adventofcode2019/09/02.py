from computer import Computer

with open('input') as f:
    memory = list(map(int, f.read().split(',')))

computer = Computer(memory, inputs=[2], debug=False)
computer.run()
