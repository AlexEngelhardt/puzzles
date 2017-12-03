def ndiv(n):
    number = 0
    for d in xrange(1, n+1):
        if n % d == 0:
            number += 1
    return number

triangular = 1
i = 1

while ndiv(triangular) <= 7:
    i += 1
    triangular += i
    print i, triangular, ndiv(triangular)


#print i, triangular
