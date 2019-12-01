import math
upto = 28123

def get_divisors(n):
    if n < 2:
        return []
    divisors = [1]
    for i in range(2, int(math.ceil(math.sqrt(n)))):
        if not n % i:
            divisors.append(i)
            divisors.append(n/i)
    if int(math.sqrt(n)) ** 2 == n:
        divisors.append(int(math.sqrt(n)))
    return divisors

def is_abundant(n):
    return sum(get_divisors(n)) > n

abundants = []
for n in range(1, upto+1):
    if is_abundant(n):
        abundants.append(n)

allnumbers = {}
for i in range(1, upto+1):
    allnumbers[str(i)] = True  # has to be summed (i.e. can not be expressed through sum)

for i in range(len(abundants)):
    for j in range(i, len(abundants)):
        if abundants[i] + abundants[j] <= upto:
            allnumbers[str(abundants[i] + abundants[j])] = False

mysum = 0
for k in allnumbers:
    v = allnumbers[k]
    if v==True:
        mysum += int(k)

print mysum
