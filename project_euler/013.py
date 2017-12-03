f = open("013.txt", "r")

summ = 0
for n in f.readlines():
    n0 = int(n[0:12])
    summ += n0

print summ
