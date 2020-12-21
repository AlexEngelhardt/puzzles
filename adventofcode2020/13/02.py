import math

debug = False

if debug:
    filename = 'test_input_2'
else:
    filename = 'input'

with open(filename) as f:
    _ = int(f.readline().strip())
    line2 = f.readline().strip().split(',')
bus_IDs = list(map(int, [d for d in line2 if d.isdigit()]))
print(bus_IDs)

# Example problem:
# Find t, such that
#  t % 7 = 0
#  t % 13 = 12
#  t % 59 = 55
#  t % 31 = 25
#  t % 19 = 12

# same as

#  t = 0 (mod 7)
#  t = 12 (mod 13)
#  t = 55 (mod 59)
#  t = 25 (mod 31)
#  t = 12 (mod 19)

# - Hmm, the bus IDs are all primes, even in the other examples and my input

# OK, looks like the Chinese Remainder Theorem:
# https://math.stackexchange.com/a/1108148/166656
# https://crypto.stanford.edu/pbc/notes/numbertheory/crt.html
#   - q^(-1) means this: https://en.wikipedia.org/wiki/Modular_multiplicative_inverse


def mod_mult_inv(a, m):
    """Modular multiplicative inverse, as defined here: https://en.wikipedia.org/wiki/Modular_multiplicative_inverse
    We're seeking an a^-1 s.t. a * a^-1 == 1 (mod m)
    I'm using a naive algorithm though."""

    for candidate in range(1, m):
        if (a * candidate) % m == 1:
            return candidate

    raise ValueError('No modular multiplicative inverse exists')


print(mod_mult_inv(3, 10))  # should be 7 because 3 * 7 (mod 10) == 1


# Create the arrays a, b, and b_prime as defined in https://crypto.stanford.edu/pbc/notes/numbertheory/crt.html

def prod(x):
    res = 1
    for x_i in x:
        res *= x_i
    return res


a = [i for i, x in enumerate(line2) if x != 'x']
a = [(m - i) % m for m, i in zip(bus_IDs, a)]  # see 01_02.py, I'm flipping the modulo remainders around s.t. e.g. 2 (mod 13) becomes 11

M = prod(bus_IDs)
b = [M / m_i for m_i in bus_IDs]
b_prime = [mod_mult_inv(b[i], bus_IDs[i]) for i in range(len(b))]

print(a)
print(b)
print(b_prime)

# Then the solution according to the formula is

x = sum([a[i] * b[i] * b_prime[i] for i in range(len(a))]) % M
print(x)

# All test cases pass, but for the real input, I get the wrong answer:
# 756261495957905 is too low :-(
