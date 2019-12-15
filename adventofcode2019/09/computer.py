class ExitOpcode(Exception):
    pass


class Computer():
    def __init__(self, memory, inputs=[], relative_base=0, debug=False):
        self.memory = memory
        self.debug = debug
        self.inputs = inputs  # a *stack* that gets popped from left-to-right
        self.iptr = 0  # instruction pointer
        self.relative_base = relative_base

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
            self.set_input(modes)
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
        elif opcode == 9:
            self.shift_relative_base(modes)
        elif opcode == 99:
            raise ExitOpcode('buh-bye!')
        else:
            raise ValueError(f'Unknown opcode {opcode} '
                             f'in position {self.iptr}')
        return opcode

    def run(self):
        while self.iptr < len(self.memory):
            try:
                opcode = self.step()
            except ExitOpcode:
                if self.debug:
                    print('exit opcode reached')
                raise
            # if opcode == 4:
            #     # In case we reached a output, *pause* the computer.
            #     # This started to be important in day 7 part 2
            #     break
        return self.last_output

    def get_pos(self, pos, mode):
        if mode == 0:
            position = self.memory[pos]
        elif mode == 1:
            position = pos
        elif mode == 2:
            position = self.memory[pos] + self.relative_base
        return position

    def get_val(self, pos, mode):
        position = self.get_pos(pos, mode)
        if position > len(self.memory):
            return 0
        else:
            return self.memory[position]

    def set(self, pos, value):
        # the position is already the "final", absolute memory position

        if (pos + 1) > len(self.memory):
            # Writing out of bounds: Enlarge the memory
            self.memory.extend([0] * (pos - len(self.memory) + 1))

        self.memory[pos] = value

    def add(self, modes):
        x1 = self.get_val(pos=self.iptr + 1, mode=modes % 10)
        x2 = self.get_val(pos=self.iptr + 2, mode=modes // 10 % 10)
        # Parameters that an instruction writes to will never be in immediate
        # mode, but only in position mode:
        target = self.get_pos(self.iptr + 3, mode=modes // 100 % 10)
        if self.debug:
            print(f'adding {x1} + {x2} into position {target}')
        self.set(target, x1 + x2)
        self.iptr += 4

    def multiply(self, modes):
        x1 = self.get_val(pos=self.iptr + 1, mode=modes % 10)
        x2 = self.get_val(pos=self.iptr + 2, mode=modes // 10 % 10)
        target = self.get_pos(self.iptr + 3, mode=modes // 100 % 10)
        if self.debug:
            print(f'multiplying {x1} * {x2} into position {target}')
        self.set(target, x1 * x2)
        self.iptr += 4

    def set_input(self, modes):
        target = self.get_pos(self.iptr + 1, mode=modes % 10)
        if self.debug:
            print(f'Popping input value {self.inputs[0]}')
        if len(self.inputs) < 1:
            raise ValueError('Empty input stack!')
        self.set(target, self.inputs[0])
        del self.inputs[0]
        self.iptr += 2

    def get_output(self, modes):
        output = self.get_val(pos=self.iptr + 1, mode=modes % 10)
        print(f'Output: {output}')
        self.iptr += 2
        self.last_output = output
        return output

    def jumpiftrue(self, modes):
        """if the first parameter is non-zero, it sets the instruction
        pointer to the value from the second parameter. Otherwise, it does
        nothing.
        """
        check = self.get_val(pos=self.iptr + 1, mode=modes % 10)
        if check:
            self.iptr = self.get_val(pos=self.iptr + 2, mode=modes // 10 % 10)
        else:  # Only update the iptr if the jump did not happen!
            self.iptr += 3

    def jumpiffalse(self, modes):
        """if the first parameter is zero, it sets the instruction
        pointer to the value from the second parameter. Otherwise, it does
        nothing.
        """
        check = self.get_val(pos=self.iptr + 1, mode=modes % 10)
        if check == 0:
            self.iptr = self.get_val(pos=self.iptr + 2, mode=modes // 10 % 10)
        else:  # Only update the iptr if the jump did not happen!
            self.iptr += 3

    def lessthan(self, modes):
        """if the first parameter is less than the second parameter, it
        stores 1 in the position given by the third parameter. Otherwise,
        it stores 0.
        """
        p1 = self.get_val(pos=self.iptr + 1, mode=modes % 10)
        p2 = self.get_val(pos=self.iptr + 2, mode=modes // 10 % 10)
        target = self.get_pos(self.iptr + 3, mode=modes // 100 % 10)
        value = 1 if p1 < p2 else 0
        self.set(target, value)
        self.iptr += 4

    def equals(self, modes):
        """if the first parameter is equal to the second parameter, it
        stores 1 in the position given by the third parameter. Otherwise,
        it stores 0.
        """
        p1 = self.get_val(pos=self.iptr + 1, mode=modes % 10)
        p2 = self.get_val(pos=self.iptr + 2, mode=modes // 10 % 10)
        target = self.get_pos(self.iptr + 3, mode=modes // 100 % 10)
        value = 1 if p1 == p2 else 0
        self.set(target, value)
        self.iptr += 4

    def shift_relative_base(self, modes):
        """Opcode 9 adjusts the relative base by the value of its only
        parameter. The relative base increases (or decreases, if the value is
        negative) by the value of the parameter.
        """
        # 'modes' is needed here too!
        shift = self.get_val(self.iptr + 1, mode=modes % 10)
        self.relative_base += shift
        self.iptr += 2
