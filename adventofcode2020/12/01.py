debug = False

if debug:
    filename = 'test_input'
else:
    filename = 'input'

with open(filename) as f:
    lines = f.read().splitlines()


class Ship:
    def __init__(self):
        # Let's have "north" be 0 degrees, then "east" is 90 degrees:
        self.facing = 90
        self.x = 0
        self.y = 0

    def get_position(self):
        return self.x, self.y

    def get_manhattan_dist(self):
        return abs(self.x) + abs(self.y)

    def turn(self, direction, degrees):
        if direction == 'L':
            self.facing = (self.facing - degrees) % 360
        elif direction == 'R':
            self.facing = (self.facing + degrees) % 360
        else:
            raise ValueError('Wrong direction specified!')

    def forward(self, length):
        """Luckily, the L and R commands are all in multiples of 90, so we only ever face directly in one
        of the 4 directions N, E, S, W.
        """
        if self.facing == 0:
            self.y += length
        elif self.facing == 90:
            self.x += length
        elif self.facing == 180:
            self.y -= length
        elif self.facing == 270:
            self.x -= length
        else:
            raise ValueError("We're facing in an unexpected direction")

    def move_compass(self, direction, length):
        if direction == 'N':
            self.y += length
        elif direction == 'E':
            self.x += length
        elif direction == 'S':
            self.y -= length
        elif direction == 'W':
            self.x -= length
        else:
            raise ValueError("Unexpected direction")

    def step(self, inst):
        """Parse any instruction string, e.g. "F10" or "R90"."""
        cmd = inst[0]
        arg = int(inst[1:])
        if cmd in ["R", "L"]:
            self.turn(cmd, arg)
        elif cmd == "F":
            self.forward(arg)
        else:  # cmd in ['N', 'S', 'E', 'W']
            self.move_compass(cmd, arg)


boaty_mc_boatface = Ship()
for inst in lines:
    boaty_mc_boatface.step(inst)

print(boaty_mc_boatface.get_manhattan_dist())
