from collections import defaultdict

start = 178416
stop = 676461

n_eligible = 0


def eligible(num):
    # To save even more time, we could join the two for-loops into one.
    # Maybe that becomes relevant in part 2.

    int_list = list(map(int, list(str(num))))

    # Check for non-decreasing digits first, this might save time:
    for i in range(len(int_list)-1):
        if int_list[i] > int_list[i+1]:
            return False

    # Ha! Transform into Run-length encoding!
    # If you have one char with a run-length of exactly 2, you're done!
    d = defaultdict(int)
    for char in str(num):
        d[char] += 1
    for k, v in d.items():
        if v == 2:
            return True
    # OK, using a dict works here because we have a special case of
    # non-decreasing numbers, i.e. the digits (i.e. dict keys) are
    # unique by design. If any key has a value of 2, we're done
    # (*after* checking for non-decreasing digits)

    return False


for i in range(start, stop+1):
    if eligible(i):
        n_eligible += 1


print(n_eligible)
# 753 is too low.
