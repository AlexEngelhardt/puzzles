# -*- coding: utf-8 -*-

import sys
import numpy

pow = int(sys.argv[1]) - 1

def times_two(numlist): # numlsit ist rückwärts, 256 = [6, 5, 2]
    out = list(numpy.zeros_like(numlist))
    carry = 0
    for i in range(len(numlist)):
        new = numlist[i] * 2
        out[i] += new % 10
        if new/10:
            if len(out) > i+1:
                out[i+1] += new / 10
            else:
                out.append(1)
        
    return out

numb = [2]
for i in range(pow):
    numb = times_two(numb)
print numb

print sum(numb)
