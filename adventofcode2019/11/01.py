from collections import defaultdict

import os
os.chdir('/home/alexx/github/puzzles/adventofcode2019/11')

from computer import Computer, ExitOpcode


class Robot():
    def __init__(self, memory):
        self.brain = Computer(memory)
        self.position = (0, 0)  # x, y, NOT row, col
        self.looking = (0, 1)  # x, y, NOT row, col
        self.painted = set()
        self.colors = defaultdict(int)  # these will be the inputs

    def step(self):
        current_color = self.colors[(self.position)]  # default: black
        self.brain.inputs.append(current_color)

        try:
            new_color = self.brain.run_until_output()  # 0: black, 1: white
            turn_direction = self.brain.run_until_output()  # 0: left, 1: right
        except ExitOpcode:
            raise

        self.colors[self.position] = new_color
        self.painted.add(self.position)

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

# Answer to part 1:
print(len(robot.painted))
