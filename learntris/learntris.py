#!/usr/bin/python3

import sys
import pdb  # pdb.set_trace()
import copy

class Tetramino(object):
    def __init__(self, shape=None):
        self.shape = shape
        
        if shape == "I":
            self.diag = 4
            self.spawncol = 3            
            initstring = "....cccc........"
        if shape == "O":
            self.diag = 2
            self.spawncol = 4
            initstring = "yyyy"
        if shape == "Z":
            self.diag = 3
            self.spawncol = 3
            initstring = "rr..rr..."
        if shape == "S":
            self.diag = 3
            self.spawncol = 3
            initstring = ".gggg...."
        if shape == "J":
            self.diag = 3
            self.spawncol = 3
            initstring = "b..bbb..."
        if shape == "L":
            self.diag = 3
            self.spawncol = 3
            initstring = "..oooo..."
        if shape == "T":
            self.diag = 3
            self.spawncol = 3
            initstring = ".m.mmm..."
            
        self.pos11 = [0, self.spawncol]
        
        self.grid = [["." for j in range(self.diag)] for i in range(self.diag)]
        for i in range(self.diag):
            for j in range(self.diag):
                self.grid[i][j] = initstring[i*self.diag + j]
        
    def printit(self):
        for i in range(self.diag):
            print(" ".join(self.grid[i]))
            
    def rotate_cw(self):
        newmx = [["." for j in range(self.diag)] for i in range(self.diag)]
        for i in range(self.diag):
            for j in range(self.diag):
                newmx[j][self.diag-i-1] = self.grid[i][j]
        self.grid = newmx

           

class Matrix(object):
    def __init__(self, width=10, height=22):
        self.width = width
        self.height = height
        self.state = [["." for j in range(width)] for i in range(height)]
        self.score = 0
        self.n_cleared = 0
        self.active_tetr = None
        
    def clear(self):
        self.state = [["." for j in range(self.width)] for i in range(self.height)]

    def clear_row(self, row):
        self.state[row] = ["." for j in range(self.width)]
        
    def printit(self):
        for row in range(self.height):
            for col in range(self.width):
                print(self.state[row][col], end=" ")
            print()  # plain newline

    def print_w_active(self):
        state = self.state
        curr_pos = self.active_tetr.pos11
        for row_i in range(self.active_tetr.diag):
            for col_i in range(self.active_tetr.diag):
                state[curr_pos[0] + row_i][curr_pos[1] + col_i] = self.active_tetr.grid[row_i][col_i].upper()
        for row in range(self.height):  # printit() copied
            for col in range(self.width):
                print(state[row][col], end=" ")
            print()  

    def set_row(self, i, lst):
        self.state[i] = lst

    def step(self):
        self.clear_full_lines()

    def clear_full_lines(self):
        for row in range(self.height):
            if not "." in self.state[row]:
                self.clear_row(row)
                self.n_cleared += 1
                self.score += 100

    def spawn(self, shape):
        self.active_tetr = Tetramino(shape)

    def nudge(self, direction):
        if direction == "<":
            if self.active_tetr.pos11[1] != 0:
                addme = [0, -1]
            else:  # hit left wall
                addme = [0, 0]
        elif direction == ">":
            if self.active_tetr.pos11[1] + self.active_tetr.diag < self.width:
                addme = [0, +1]
            else:  # hit left wall
                addme = [0, 0]

        elif direction == "v":
            addme = [+1, 0]

        self.active_tetr.pos11[0] += addme[0]
        self.active_tetr.pos11[1] += addme[1]


        
if __name__ == "__main__":                
    matrix = Matrix()
    
    while True:
        inp = input()
        cmds = list(inp)

        i = -1
        while i < (len(cmds)-1):
            i += 1
            x = cmds[i]

            if x == " ":
                continue
            
            elif x == "q":
                sys.exit(0)

            elif x == ";":
                print()
                
            elif x == "p":
                matrix.printit()
                
            elif x == "g":
                for row in range(matrix.height):
                    row_str = input()
                    matrix.set_row(row, row_str.rsplit(" "))
                    
            elif x == "c":
                matrix.clear()

            elif x == "?":
                i += 1
                x = cmds[i]
                if x == "s":  # ?s
                    print(matrix.score)
                elif x == "n":  # ?n
                    print(matrix.n_cleared)
                
            elif x == "s":
                matrix.step()
                
            elif x in ["I", "O", "Z", "S", "J", "L", "T"]:
                matrix.spawn(x)
                
            elif x == "t":
                matrix.active_tetr.printit()
                
            elif x == ")":
                matrix.active_tetr.rotate_cw()
            elif x == "(":
                matrix.active_tetr.rotate_cw()
                matrix.active_tetr.rotate_cw()
                matrix.active_tetr.rotate_cw()

            elif x == "P":
                matrix.print_w_active()

            elif x in [">", "<", "v"]:
                matrix.nudge(x)
            
            else:
                print("OMG UNRECOGNIZED COMMAND")
                sys.exit(0)
