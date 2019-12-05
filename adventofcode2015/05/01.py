import re


def is_nice(s):
    # print('Trying ' + s)

    # At least three vowels:
    if not re.search('[aeiou].*[aeiou].*[aeiou]', s):
        # print('  no three vowels found')
        return False
    # At least one double-letter:
    if not re.search(r'(.)\1', s):
        # print('  no double letter found')
        return False
    # No bad strings:
    if re.search('ab|cd|pq|xy', s):
        # print('  bad string found')
        return False

    return True


nice_lines = 0

with open('input') as f:
    for line in f:
        if is_nice(line.strip()):
            nice_lines += 1

print(nice_lines)
