def collatz_length(start):
    if start == 1:
        return 1
    if start % 2 == 0:
        return collatz_length(start/2) + 1
    else:
        return collatz_length(3*start + 1) + 1

max_len = 0
max_idx = 0
for i in xrange(1, int(1e6 + 1)):
    l = collatz_length(i)
    if l > max_len:
        max_len = l
        max_idx = i

print max_len, max_idx
