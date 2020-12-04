import re


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

    # validate byr
    if not re.compile(r'^\d{4}$').match(p['byr']):  # `match` starts at beginning of string, `search` starts anywhere
        return False
    if not 1920 <= int(p['byr']) <= 2002:
        return False

    # validate iyr
    if not re.compile(r'^\d{4}$').match(p['iyr']):
        return False
    if not 2010 <= int(p['iyr']) <= 2020:
        return False

    # validate eyr
    if not re.compile(r'^\d{4}$').match(p['eyr']):
        return False
    if not 2020 <= int(p['eyr']) <= 2030:
        return False

    # validate hgt
    if not re.compile(r'^\d{2,3}(cm|in)$').match(p['hgt']):
        return False
    if p['hgt'].endswith('in'):
        if not 59 <= int(p['hgt'][:-2]) <= 76:
            return False
    if p['hgt'].endswith('cm'):
        if not 150 <= int(p['hgt'][:-2]) <= 193:
            return False

    # validate hcl
    if not re.compile(r'^#[0123456789abcdef]{6}$').match(p['hcl']):
        return False

    # validate ecl
    if p['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return False

    # validate pid
    if not re.compile(r'^\d{9}$').match(p['pid']):
        return False

    return True


with open('input') as f:
    lines = f.read()

passports = lines.split('\n\n')  # passports are separated by two newlines
passports = list(map(parse_passport, passports))

# print(passports)

print(sum(map(passport_valid, passports)))
