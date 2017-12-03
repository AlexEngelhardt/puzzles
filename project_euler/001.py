#!/usr/bin/python2
import sys

below = int(sys.argv[1])

total = 0

for i in range(1, below):
    if not i % 3:
        total = total + i
    elif not i % 5: 
        total = total + i

print total
