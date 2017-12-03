import math
from collections import Counter

def primefactors(n):
    factors = []
    factor = 2
    while factor <= n:
        if n % factor == 0:
            n = n / factor
            factors.append(factor)
            factor = 1
        factor += 1
    return factors

# def ndiv(n):
#     PF = primefactors(n)
#     pf = Counter(PF)
#     print pf
#     number = math.factorial(len(PF))
#     for val in pf.values():
#         number = number / math.factorial(val)
#     return number + 2

def ndiv(n):
    PF = primefactors(n)
    pf = Counter(PF)
    number = 1
    for val in pf.values():
        number *= (val+1)
    return number

triangular = 1
i = 1

while ndiv(triangular) <= 500:
    i += 1
    triangular += i
    print i, triangular, ndiv(triangular)
