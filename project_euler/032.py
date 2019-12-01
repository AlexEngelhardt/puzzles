import math

def is_pd(a, b, c):
    digits = []
    while c:
        digits.append(c%10)
        c /= 10
    while a:
        digits.append(a%10)
        a /= 10
    while b:
        digits.append(b%10)
        b /= 10
    digits.sort()
    return digits == range(1, 10)

def factorize(n):
    factors = []
    for i in range(1, int(math.sqrt(n))+1):
        if not n%i:
            factors.append(i)
    return factors


pans = []
for c in range(98766):
    all_as = factorize(c)
    for a in all_as:
        b = c/a
        if is_pd(a,b,c):
            pans.append(c)

print sum(set(pans))
            

#print factorize(144)

# pans = []
# for a in range(1, 987654):
#     for b in range(1, a):
#         if is_pd(a,b):
#             pans.append(a*b)

# print set(pans)
# print sum(set(pans))


