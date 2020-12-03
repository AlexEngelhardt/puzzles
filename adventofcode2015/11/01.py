import re

test_input = "abcdefgh"
real_input = "vzbxkghb"


def increase_password(p):
    # this is essentially a number represented in base 26
    p = list(p)

    done = False
    position = len(p) - 1
    while not done:
        if position < 0:
            return 'a' + ''.join(p)
        p[position] = chr((ord(p[position]) - 97 + 1) % 26 + 97)
        if p[position] != 'a':
            done = True
        else:
            position -= 1
    return ''.join(p)


def password_valid(p):

    # not contain i, o, or l:
    rule1 = True
    if 'i' in p or 'o' in p or 'l' in p:
        rule1 = False

    if not rule1:
        return False

    # one increasing straight of 3 letters (e.g. abc, ghi)
    if len(p) < 3:
        return False
    rule2 = False
    for start_char in range(len(p)-2):
        if ord(p[start_char]) == ord(p[start_char+1]) - 1 and ord(p[start_char+1]) == ord(p[start_char+2]) - 1:
            rule2 = True
            break

    if not rule2:
        return False

    # at least two non-overlapping pairs of letters
    i = 0
    n_duplicates = 0
    while i <= len(p) - 2:
        if p[i] == p[i+1]:
            n_duplicates += 1
            i += 1  # this ensures non-overlappingness
        i += 1

    rule3 = n_duplicates >= 2
    if not rule3:
        return False

    return True


def next_valid_password(p):
    new_p = increase_password(p)
    while not password_valid(new_p):
        new_p = increase_password(new_p)
    return new_p


print(test_input)
print(next_valid_password(test_input))

print(real_input)
print(next_valid_password(real_input))  # answer to part 1
print(next_valid_password(next_valid_password(real_input)))  # answer to part 2

