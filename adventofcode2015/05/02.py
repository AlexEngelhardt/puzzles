import re


def is_nice(s):
    # print('Trying ' + s)

    # pair of two letters
    if not re.search(r'(..).*\1', s):
        # print('  no pair of two letters found')
        return False
    # one letter repeating with one space
    if not re.search(r'(.).\1', s):
        # print('  no one repeating letter with one spacing found')
        return False

    return True


is_nice('qjhvhtzxzqqjkmpb')  # True
is_nice('xxyxx')  # True
is_nice('uurcxstgmygtbstg')  # False
is_nice('ieodomkazucvgmuy')  # False

nice_lines = 0

with open('input') as f:
    for line in f:
        if is_nice(line.strip()):
            nice_lines += 1

print(nice_lines)
