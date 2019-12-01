import math

# b muss prim sein (for n=0)

def is_prime(n):
    if n < 2:
        return False
    for divisor in xrange(2, int(round(math.sqrt(n))+1)):
        if n % divisor == 0:
            return False
    return True


def length(a, b):
    n = 0
    while is_prime(n**2 + a * n + b):
        n += 1
    return n-1


bs = []
for b in xrange(1001):
    if is_prime(b):
        bs.append(b)

max_len = 0
argmax_a = 0
argmax_b = 0
for b in bs:
    for a in xrange(-1000, 1001):
        l = length(a, b)
        if l > max_len:
            argmax_a = a
            argmax_b = b
            max_len = l

print argmax_a, argmax_b, max_len
print argmax_a * argmax_b
