def valid(line):
    rule, passwd = line.split(': ')
    n_range, char = rule.split(' ')
    n1, n2 = map(int, n_range.split('-'))

    xor1 = passwd[n1-1] == char
    xor2 = passwd[n2-1] == char
    is_valid = int(xor1) + int(xor2) == 1

    return 1 if is_valid else 0


with open('input') as f:
    passes = f.read().splitlines()

# print(passes)

print(sum(map(valid, passes)))
