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

    # Check for two equal adjacent digits:
    two_equal_digits = False
    for i in range(len(int_list)-1):
        if int_list[i] == int_list[i+1]:
            two_equal_digits = True
            break
    if not two_equal_digits:
        return False

    return True


for i in range(start, stop+1):
    if eligible(i):
        n_eligible += 1


print(n_eligible)
