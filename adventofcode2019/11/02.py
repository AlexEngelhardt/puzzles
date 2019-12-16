import numpy as np
from collections import defaultdict

import os
os.chdir('/home/alexx/github/puzzles/adventofcode2019/11')

from computer import Computer, ExitOpcode


class Robot():
    def __init__(self, memory):
        self.brain = Computer(memory)
        self.position = (0, 0)  # x, y, NOT row, col
        self.looking = (0, 1)  # x, y, NOT row, col
        self.colors = defaultdict(int)  # these will be the inputs
        self.colors[(0, 0)] = 1  # start on a white panel

    def step(self):
        current_color = self.colors[(self.position)]  # default: black
        self.brain.inputs.append(current_color)

        try:
            new_color = self.brain.run_until_output()  # 0: black, 1: white
            turn_direction = self.brain.run_until_output()  # 0: left, 1: right
        except ExitOpcode:
            raise

        self.colors[self.position] = new_color

        if self.looking == (0, 1):
            self.looking = (1, 0) if turn_direction == 1 else (-1, 0)
        elif self.looking == (0, -1):
            self.looking = (-1, 0) if turn_direction == 1 else (1, 0)
        elif self.looking == (1, 0):
            self.looking = (0, -1) if turn_direction == 1 else (0, 1)
        elif self.looking == (-1, 0):
            self.looking = (0, 1) if turn_direction == 1 else (0, -1)

        self.position = (self.position[0] + self.looking[0],
                         self.position[1] + self.looking[1])

    def run(self):
        while True:
            try:
                self.step()
            except ExitOpcode:
                print('Done')
                break


with open('input') as f:
    memory = list(map(int, f.read().strip().split(',')))

print(memory)

robot = Robot(memory)

robot.run()

robot.colors

min_x = 0
min_y = 0
max_x = 0
max_y = 0
for x, y in robot.colors.keys():
    min_x = min(min_x, x)
    min_y = min(min_y, y)
    max_x = max(max_x, x)
    max_y = max(max_y, y)

min_x, max_x
min_y, max_y

x_range = max_x - min_x + 1
y_range = max_y - min_y + 1

grid = np.zeros((y_range, x_range), dtype=np.int8)
grid

for k, v in robot.colors.items():
    if v == 1:  # then paint this field white
        print(f'painting {k[0] - min_x}, {k[1] - min_y}')
        grid[k[1] - min_y][k[0] - min_x] = 1
    else:
        print('not painting')

grid

# It's horizontally mirrored, but who cares :)
print('\n'.join([''.join(['#' if d else '.' for d in row]) for row in grid]))
