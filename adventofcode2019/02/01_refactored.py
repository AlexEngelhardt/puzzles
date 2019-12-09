class ExitOpcode(Exception):
    pass


class Computer():
    def __init__(self, memory, debug=False):
        self.memory = memory
        self.debug = debug
        self.iptr = 0  # instruction pointer

    def step(self):
        instruction = self.memory[self.iptr]
        opcode = instruction % 100
        modes = instruction // 100

        if self.debug:
            print(f'\niptr: {self.iptr}, opcode: {opcode}, modes: {modes}')

        if opcode == 1:
            self.add(modes)
        elif opcode == 2:
            self.multiply(modes)
        elif opcode == 99:
            raise ExitOpcode('buh-bye!')
        else:
            raise ValueError(f'Unknown opcode {opcode} '
                             f'in position {self.iptr}')

    def run(self):
        while self.iptr < len(self.memory):
            try:
                self.step()
            except ExitOpcode:
                print('exit opcode reached')
                break

    def add(self, modes):
        x1 = self.memory[self.memory[self.iptr + 1]]
        x2 = self.memory[self.memory[self.iptr + 2]]
        target = self.memory[self.iptr + 3]
        if self.debug:
            print(f'adding {x1} + {x2} into position {target}')
        self.memory[target] = x1 + x2
        self.iptr += 4

    def multiply(self, mode):
        x1 = self.memory[self.memory[self.iptr + 1]]
        x2 = self.memory[self.memory[self.iptr + 2]]
        target = self.memory[self.iptr + 3]
        if self.debug:
            print(f'multiplying {x1} * {x2} into position {target}')
        self.memory[target] = x1 * x2
        self.iptr += 4


with open('input') as f:
    memory = list(map(int, f.read().split(',')))


memory[1] = 12
memory[2] = 2

computer = Computer(memory, debug=True)
computer.run()
print("computer.memory[0]: " + str(computer.memory[0]))
