import math

#test = True
test = False

verbose = True
#verbose = False

if test:
    filename = 'test_input'
    #filename = 'my_test_input'
else:
    filename = 'input'

with open(filename) as f:
    lines = f.read().splitlines()


class Ship:
    def __init__(self):
        # Let's have "north" be 0 degrees, then "east" is 90 degrees

        # Remember: The waypoint's coordinates are *relative* to the ship position!
        self.waypoint_x = 10
        self.waypoint_y = 1
        self.x = 0
        self.y = 0

    def status(self):
        # return f"Ship: (x={self.x}, y={self.y}), Waypoint: (x={self.waypoint_x}, y={self.waypoint_y})"
        return f"Ship: ({self.x}, {self.y}), Waypoint: ({self.waypoint_x}, {self.waypoint_y})"

    def get_manhattan_dist(self):
        return abs(self.x) + abs(self.y)

    def rotate_waypoint(self, direction, degrees):
        # https://stackoverflow.com/questions/2259476/rotating-a-point-about-another-point-2d

        # If we have to rotate right by x degrees, instead rotate left by 360-x degrees :)
        if direction == 'R':
            degrees = 360 - degrees

        # 1. Subtract the pivot point (the ship) from the point to rotate (the waypoint)
        #    Because the waypoint coordinates are relative to the ship, we don't need to subtract the pivot

        # 2. Rotate the point around the origin (0, 0)
        degrees_rad = degrees / 360 * 2*math.pi
        new_x = self.waypoint_x * math.cos(degrees_rad) - self.waypoint_y * math.sin(degrees_rad)
        new_y = self.waypoint_x * math.sin(degrees_rad) + self.waypoint_y * math.cos(degrees_rad)

        self.waypoint_x = round(new_x)
        self.waypoint_y = round(new_y)

        # 3. Add the pivot point again
        #    This is also not necessary!

    def move_towards_waypoint(self, times):

        self.x += self.waypoint_x * times
        self.y += self.waypoint_y * times

    def move_waypoint(self, direction, length):
        if direction == 'N':
            self.waypoint_y += length
        elif direction == 'E':
            self.waypoint_x += length
        elif direction == 'S':
            self.waypoint_y -= length
        elif direction == 'W':
            self.waypoint_x -= length
        else:
            raise ValueError("Unexpected direction")

    def step(self, inst):
        """Parse any instruction string, e.g. "F10" or "R90"."""
        cmd = inst[0]
        arg = int(inst[1:])
        if cmd in ["R", "L"]:
            self.rotate_waypoint(cmd, arg)
        elif cmd == "F":
            self.move_towards_waypoint(arg)
        else:  # cmd in ['N', 'S', 'E', 'W']
            self.move_waypoint(cmd, arg)


boaty_mc_boatface = Ship()
if verbose: print(boaty_mc_boatface.status())
for i, inst in enumerate(lines):
    if verbose: print(f"i: {i}")
    if verbose: print(inst)
    boaty_mc_boatface.step(inst)
    if verbose: print(boaty_mc_boatface.status())
    if verbose: print(f"MHD: {boaty_mc_boatface.get_manhattan_dist()}")


print(f"Final MHD: {boaty_mc_boatface.get_manhattan_dist()}")
