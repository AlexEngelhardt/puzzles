
def parse_line(line):
    command, target = line.split(' -> ')
    cmd = command.split(' ')

    if len(cmd) == 1:
        if command.isdigit():
            function = 'ASSIGN_INT'
        else:
            function = 'ASSIGN_WIRE'
        parameters = [command]
    elif cmd[1] in ['AND', 'OR', 'LSHIFT', 'RSHIFT']:
        function = cmd[1]
        parameters = [cmd[0], cmd[2]]
    elif cmd[0] == 'NOT':
        function = 'NOT'
        parameters = [cmd[1]]
    else:
        raise ValueError("Unknown command!")

    return target, function, parameters


class BitComputer:
    def __init__(self, commands):
        self.wire_signals = dict()  # final integers
        self.commands = dict()  # commands

        for cmd in commands:
            target, function, parameters = parse_line(cmd)
            self.commands[target] = (function, parameters)

        # TODO Not pretty, but quick :)
        self.commands['b'] = ('ASSIGN_INT', ['956'])

    def ASSIGN_INT(self, value):
        return int(value)

    def ASSIGN_WIRE(self, value):
        return int(value)  # I think it's already processed at this point

    def AND(self, a, b):
        return a & b

    def OR(self, a, b):
        return a | b

    def NOT(self, a):
        return ~a % (2**16)

    def LSHIFT(self, a, by):
        return a << by

    def RSHIFT(self, a, by):
        return a >> by

    def resolve_command(self, function, parameters):
        fct = getattr(self, function)
        parameters = [
            int(p) if p.isdigit() else self.get_wire_value(p) for p in parameters
        ]
        res = fct(*parameters)
        return res

    def get_wire_value(self, wire):
        if wire not in self.wire_signals:
            function, parameters = self.commands[wire]
            res = self.resolve_command(function, parameters)
            self.wire_signals[wire] = res
        return self.wire_signals[wire]


if __name__ == '__main__':
    # create a dict of {wire: fct(params)}
    # find the command that writes to wire a
    # recursively evaluate all necessary commands

    # with open('test_input') as file:
    with open('input') as file:
        commands = map(str.strip, file.readlines())

    bc = BitComputer(commands)

    # for wire in list('defghixya'):
    #     print(f"{wire}: {bc.get_wire_value(wire)}")

    wire = 'a'
    print(f"{wire}: {bc.get_wire_value(wire)}")
