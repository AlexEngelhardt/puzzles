#!/usr/bin/python3

import sys
import pdb  # pdb.set_trace()
import copy

class Tetramino(object):
    def __init__(self, shape=None):
        if shape == "I":
            self.diag = 4
            initstring = "....cccc........"
        if shape == "O":
            self.diag = 2
            initstring = "yyyy"
        if shape == "Z":
            self.diag = 3
            initstring = "rr..rr..."
        if shape == "S":
            self.diag = 3
            initstring = ".gggg...."
        if shape == "J":
            self.diag = 3
            initstring = "b..bbb..."
        if shape == "L":
            self.diag = 3
            initstring = "..oooo..."
        if shape == "T":
            self.diag = 3
            initstring = ".m.mmm..."
            
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
        self.active_tetramino = None
        
    def clear(self):
        self.state = [["." for j in range(self.width)] for i in range(self.height)]

    def clear_row(self, row):
        self.state[row] = ["." for j in range(self.width)]
        
    def printit(self):
        for row in range(self.height):
            for col in range(self.width):
                print(self.state[row][col], end=" ")
            print()  # plain newline
            
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


if __name__ == "__main__":                
    matrix = Matrix()
    
    while True:
        inp = input()
        cmds = inp.split(" ")
        for x in cmds:
            
            if x == "q":
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
                
            elif x == "?s":
                print(matrix.score)
                
            elif x == "?n":
                print(matrix.n_cleared)
                
            elif x == "s":
                matrix.step()
                
            elif x in ["I", "O", "Z", "S", "J", "L", "T"]:
                active = Tetramino(x)
                
            elif x == "t":
                active.printit()
                
            elif x == ")":
                active.rotate_cw()
                
            else:
                sys.exit(0)
