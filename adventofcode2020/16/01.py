debug = False

if debug:
    filename = 'test_input'
else:
    filename = 'input'

with open(filename) as f:
    inp = f.read()
    validation, my_ticket, tickets = inp.split('\n\n')
my_ticket = list(map(int, my_ticket.split('\n')[1].split(',')))
tickets = tickets.strip().split('\n')[1:]
tickets = [list(map(int, x.split(','))) for x in tickets]
validation = validation.split('\n')

# print('validation:')
# print(validation)
# print('--')
# print('my_ticket:')
# print(my_ticket)
# print('--')
# print('tickets:')
# print(tickets)


def validate(n, validation):
    for v_row in validation:
        _, rules = v_row.split(': ')
        rules = rules.split(' or ')
        for rule in rules:
            mini, maxi = map(int, rule.split('-'))
            if mini <= n <= maxi:
                return True
    return False


error_rate = 0
for ticket in tickets:
    for n in ticket:
        if not validate(n, validation):
            error_rate += n
print(error_rate)
