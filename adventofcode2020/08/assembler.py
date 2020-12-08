class Computer:
    def __init__(self):
        self.accumulator = 0
        self.iptr = 0  # Instruction pointer
        self.ectr = []  # Execution counter: How often has each program line been executed so far?
        self.commands = None  # List of assembler commands

    def _parse_op(self, line):
        """Parses one code line into an execution command"""
        words = line.split()
        command = words[0]
        arguments = words[1:]  # If the line is just one word, `arguments` will be an empty list
        return command, arguments

    def load(self, lines):
        """Loads a program as a list of instruction strings"""
        # TODO I can load a program in __init__ too. Maybe that's cleaner. But then an instantiated Computer can't
        #  reload a new program...
        cmds = [self._parse_op(line) for line in lines]
        self.commands = cmds

    def run(self):
        """Runs the currently loaded program from the beginning"""
        # TODO: Do iptr and accumulator have to be set in __init__() or at the beginning of run()?
        #  Which one is smarter?
        self.iptr = 0
        self.accumulator = 0
        self.ectr = [0 for _ in range(len(self.commands))]

        while True:
            self.ectr[self.iptr] += 1
            if self.ectr[self.iptr] > 1:
                print('This execution is visited for the second time!')
                print(f'Accumulator: {self.accumulator}')
                # Exit code 1: Infinite loop (at least for now, with this limited set of commands)
                return 1

            cmd, args = self.commands[self.iptr]
            if cmd == 'nop':
                self.iptr += 1
            elif cmd == 'acc':
                self.accumulator += int(args[0])
                self.iptr += 1
            elif cmd == 'jmp':
                self.iptr += int(args[0])

            if self.iptr == len(self.commands):
                # End of program reached
                # "Process finished with exit code 0 :)"
                return 0

        raise Exception('This statement should never be reached')
