from collections import namedtuple

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


def validate(n, validation):
    for v_row in validation:
        _, rules = v_row.split(': ')
        rules = rules.split(' or ')
        for rule in rules:
            mini, maxi = map(int, rule.split('-'))
            if mini <= n <= maxi:
                return True
    return False


################################################################
# Part 1

error_rate = 0
for ticket in tickets:
    for n in ticket:
        if not validate(n, validation):
            error_rate += n
print(error_rate)

################################################################
# Part 2

####
# Add your ticket
tickets = [my_ticket] + tickets

####
# Discard invalid tickets
ticket_valid = [True for _ in range(len(tickets))]
for i, ticket in enumerate(tickets):
    for n in ticket:
        if not validate(n, validation):
            ticket_valid[i] = False
tickets = [t for t, tv in zip(tickets, ticket_valid) if tv]


####
# Find out which fields are candidates for which column
Rule = namedtuple('Rule', ['mini', 'maxi'])


class Field:
    def __init__(self, s):
        self.name, rules = s.split(': ')
        self.rules = []
        rules = rules.split(' or ')
        for rule in rules:
            mini, maxi = map(int, rule.split('-'))
            self.rules.append(Rule(mini, maxi))

    def valid(self, list_of_numbers):
        for n in list_of_numbers:
            n_valid = False
            for r in self.rules:
                if r.mini <= n <= r.maxi:
                    n_valid = True
            if not n_valid:
                return False
        return True


fields = [Field(x) for x in validation]

# Transposed tickets, i.e. the first list contains the first entry for each ticket.
# https://stackoverflow.com/questions/21444338/transpose-nested-list-in-python
tickets_t = list(map(list, zip(*tickets)))

print(tickets)
print(tickets_t)

candidates = dict()
for field in fields:
    candidates[field.name] = []
    for i, column in enumerate(tickets_t):
        if field.valid(column):
            candidates[field.name].append(i)

print(candidates)
# For the test input, this gives:
# {'class': [0, 1], 'row': [0], 'seat': [2]}
# Now 'class' can be two columns, but because column 0 *must* be 'row', then the 'class' must be 1

####
# Resolve this dict to a field => column mapping

field_col = dict()

while len(field_col) < len(tickets_t):  # As long as we have unmapped tickets
    # Find a candidate that has only one possible column
    for field_name, cand_cols in candidates.items():
        if len(cand_cols) == 1:
            break
    # Add it to 'field_col'
    the_column = cand_cols[0]
    field_col[field_name] = the_column
    # Remove this candidate from 'candidates'
    del candidates[field_name]
    # Now remove this column ID from all other candidates
    for fn, cc in candidates.items():
        if the_column in cc:
            candidates[fn].remove(the_column)

print(field_col)

####
# Now get column IDs for all fields that start with 'departure'
the_IDs = [col for field, col in field_col.items() if field.startswith('departure')]

####
# And multiply those columns' values from your ticket:
print(my_ticket)
answer = 1
for col in the_IDs:
    answer *= my_ticket[col]

print(answer)
