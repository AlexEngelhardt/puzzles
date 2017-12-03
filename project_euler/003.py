#!/usr/bin/python2

# This is *very* ugly code. Non-optimized, I have no idea why it works.

import math
import sys

def isprime(n):
    "Some string to describe the function"
    for divisor in range(2,int(round(math.sqrt(n))+1)):
        if n/divisor == float(n)/divisor:
            return False
    return True

number = int(sys.argv[1])

factors = list()

while not isprime(number):
    divisor = 1
    while divisor <= number:
        divisor += 1
        if number / divisor == float(number) / divisor:
            factors.append(divisor)
            number = number / divisor

print factors
