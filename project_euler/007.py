import math

def is_prime(n):
    for divisor in xrange(2, int(round(math.sqrt(n)+1))):
        if n % divisor == 0:
            return False
    return True

def nth_prime(n):
    check = 1
    i = 1
    while i <= n:
        check += 1
        if is_prime(check):
            i += 1

    return str(check)

print "2nd: " + nth_prime(2)
print "6th: " + nth_prime(6)
print "10001th: " + nth_prime(10001)
