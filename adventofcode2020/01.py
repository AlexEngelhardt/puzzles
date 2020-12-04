def parse_passport(p):
    key_val = p.split()
    res = {kv.split(':')[0]: kv.split(':')[1] for kv in key_val}
    return res


def passport_valid(p):
    must_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    optional_fields = ['cid']

    for mf in must_fields:
        if mf not in p:
            return False
    return True


with open('input') as f:
    lines = f.read()

passports = lines.split('\n\n')  # passports are separated by two newlines
passports = list(map(parse_passport, passports))

# print(passports)

print(sum(map(passport_valid, passports)))
