import math

def old_is_prime(n):
    if n <= 1:  # 0 and 1 aren't
        return False
    if n <= 3:  # 2 and 3 are
        return True
    for divisor in xrange(2, int(round(math.sqrt(n))+1)):
        if n % divisor == 0:
            return False
    return True

def is_prime(n):
    if n <= 1:  # 0 and 1 aren't
        return False
    if n <= 3:  # 2 and 3 are
        return True
    for k in xrange(2, math.floor(n/6)):
        

    for divisor in xrange(2, int(round(math.sqrt(n))+1)):
        if n % divisor == 0:
            return False
    return True

def sieve(up_to):
    # Sieve of Eratosthenes
    primes = range(1, up_to+1)
    i = 1
    while i < up_to:
        i +=1 
        
