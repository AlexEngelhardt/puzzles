import math

digits = 1000

fibn2 = 1
fibn1 = 1
fibn = 2
i = 3 # 3rd fib number
d = 1
while d < digits:
    fibn2 = fibn1
    fibn1 = fibn
    fibn = fibn1+fibn2
    d = int(math.log10(fibn))+1
    i += 1
    # print i, fibn

print "First fib with >= ", str(digits), "digits: ", str(i)
