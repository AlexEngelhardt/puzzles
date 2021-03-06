class ExitOpcode(Exception):
    pass


class Computer():
    def __init__(self, memory, debug=False):
        self.memory = memory
        self.debug = debug
        self.input = None
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
        elif opcode == 3:
            self.set_input()
        elif opcode == 4:
            self.get_output(modes)
        elif opcode == 5:
            self.jumpiftrue(modes)
        elif opcode == 6:
            self.jumpiffalse(modes)
        elif opcode == 7:
            self.lessthan(modes)
        elif opcode == 8:
            self.equals(modes)
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

    def get(self, pos, mode):
        if mode == 0:
            return self.memory[self.memory[pos]]
        elif mode == 1:
            return self.memory[pos]

    def add(self, modes):
        x1 = self.get(pos=self.iptr + 1, mode=modes % 10)
        x2 = self.get(pos=self.iptr + 2, mode=modes // 10 % 10)
        # Parameters that an instruction writes to will never be in immediate
        # mode, but only in position mode:
        target = self.memory[self.iptr + 3]
        if self.debug:
            print(f'adding {x1} + {x2} into position {target}')
        self.memory[target] = x1 + x2
        self.iptr += 4

    def multiply(self, modes):
        x1 = self.get(pos=self.iptr + 1, mode=modes % 10)
        x2 = self.get(pos=self.iptr + 2, mode=modes // 10 % 10)
        target = self.memory[self.iptr + 3]
        if self.debug:
            print(f'multiplying {x1} * {x2} into position {target}')
        self.memory[target] = x1 * x2
        self.iptr += 4

    def set_input(self):
        self.input = int(input('Set input: '))
        target = self.memory[self.iptr + 1]
        self.memory[target] = self.input
        self.iptr += 2

    def get_output(self, modes):
        output = self.get(pos=self.iptr + 1, mode=modes % 10)
        print(f'Output: {output}')
        self.iptr += 2

    def jumpiftrue(self, modes):
        """if the first parameter is non-zero, it sets the instruction
        pointer to the value from the second parameter. Otherwise, it does
        nothing.
        """
        check = self.get(pos=self.iptr + 1, mode=modes % 10)
        if check:
            self.iptr = self.get(pos=self.iptr + 2, mode=modes // 10 % 10)
        else:  # Only update the iptr if the jump did not happen!
            self.iptr += 3

    def jumpiffalse(self, modes):
        """if the first parameter is zero, it sets the instruction
        pointer to the value from the second parameter. Otherwise, it does
        nothing.
        """
        check = self.get(pos=self.iptr + 1, mode=modes % 10)
        if check == 0:
            self.iptr = self.get(pos=self.iptr + 2, mode=modes // 10 % 10)
        else:  # Only update the iptr if the jump did not happen!
            self.iptr += 3

    def lessthan(self, modes):
        """if the first parameter is less than the second parameter, it
        stores 1 in the position given by the third parameter. Otherwise,
        it stores 0.
        """
        p1 = self.get(pos=self.iptr + 1, mode=modes % 10)
        p2 = self.get(pos=self.iptr + 2, mode=modes // 10 % 10)
        p3 = self.memory[self.iptr + 3]
        self.memory[p3] = 1 if p1 < p2 else 0
        self.iptr += 4

    def equals(self, modes):
        """if the first parameter is equal to the second parameter, it
        stores 1 in the position given by the third parameter. Otherwise,
        it stores 0.
        """
        p1 = self.get(pos=self.iptr + 1, mode=modes % 10)
        p2 = self.get(pos=self.iptr + 2, mode=modes // 10 % 10)
        p3 = self.memory[self.iptr + 3]
        self.memory[p3] = 1 if p1 == p2 else 0
        self.iptr += 4


with open('input') as f:
    memory = list(map(int, f.read().split(',')))


computer = Computer(memory, debug=True)
computer.run()
