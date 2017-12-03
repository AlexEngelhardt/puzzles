#!/usr/bin/python2

upto = 4000000
#upto = 90

fib = [1, 2]
mysum=0

while fib[len(fib)-1] <= upto:
    fib.append(fib[len(fib)-1] + fib[len(fib)-2])
    if not fib[len(fib)-1] % 2 and fib[len(fib)-1] < upto:
        print "found " + str(fib[len(fib)-1])
        mysum = mysum + fib[len(fib)-1]

print mysum + 2  # +2 wegen der initial 2
