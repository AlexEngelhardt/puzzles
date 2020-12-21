debug = True

if debug:
    filename = 'test_input'
else:
    filename = 'input'

with open(filename) as f:
    contents = f.read()
rules_pre, messages = contents.split('\n\n')
rules = dict()
for line in rules_pre.split('\n'):
    number, rule = line.split(': ')
    rules[number] = rule
messages = messages.strip().split('\n')

print(rules)


def match(message, rules, rule_id):
    rule_str = rules[rule_id]
    for rule in rule_str.split(' | '):
        pass


print('should be True:', match('ababbb', rules, '0'))
print('should be True:', match('abbbab', rules, '0'))
print('should be False:', match('bababa', rules, '0'))
print('should be False:', match('aaabbb', rules, '0'))
