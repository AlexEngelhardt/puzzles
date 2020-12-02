def valid(line):

    rule, passwd = line.split(': ')
    n_range, char = rule.split(' ')
    n_min, n_max = map(int, n_range.split('-'))

    is_valid = n_max >= passwd.count(char) >= n_min

    return 1 if is_valid else 0
    

with open('input') as f:
    passes = f.read().splitlines()


# print(passes)

print(sum(map(valid, passes)))
