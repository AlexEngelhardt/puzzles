mysum = 1  # die 1 in der mitte

for i in xrange(1, 500+1):
    mysum += (2*i + 1) ** 2
    mysum += (2*i)**2 + 1
    mysum += (2*i)**2 - (2*i - 1)
    mysum += (2*i + 1) ** 2 - 2*i


print mysum
