import math

def is_prime(n):
    for divisor in xrange(2, int(round(math.sqrt(n)+1))):
        if n % divisor == 0:
            return False
    return True

def sum_up_to(n):
    check = 1
    summ = 0
    while check < n:
        check += 1
        if is_prime(check):
            summ += check

    return str(summ)

print "upto 10: " + sum_up_to(10)
print "upto 2e6: " + sum_up_to(2e6)
