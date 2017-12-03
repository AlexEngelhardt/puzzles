import math
upto=10000

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


def d(n):
    return sum(get_divisors(n))

dic = {}
for i in range(1, upto+1):
    dic[i] = d(i)

mysum = 0
for key in dic:
    if dic[key] in dic:
        if key == dic[dic[key]] and not key==dic[key]:
            print key, dic[key], dic[dic[key]]
            mysum += key

    # if dic[val] == key:
    #     print key, val
    #     mysum += val
print mysum
