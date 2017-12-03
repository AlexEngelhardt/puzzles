# solution: 248860

ex = 5 # test:4

def check(D):
    mysum = 0
    d = D
    while d:
        mysum += (d%10)**ex
        d /= 10
    return D==mysum

up_to = 6* (9**5)
print "Max:", up_to

good_nums = []
for d in range(11, up_to + 1):
    if check(d):
        print "found", d
        good_nums.append(d)

print "Sum:", sum(good_nums)
