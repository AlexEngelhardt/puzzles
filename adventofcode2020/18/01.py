import re

debug = False

if debug:
    filename = 'test_input'
else:
    filename = 'input'

with open(filename) as f:
    lines = f.read().splitlines()

print(lines)

# This way probably makes sense:
# Step 1: While there are '(' or ')' characters:
#             Split expressions into groups with matching pairs of parentheses
# Step 2: Recursively evaluate contents of parentheses from left to right


def pop_number_left(s):
    """Takes a string like '123 + 456 * 789' and returns:
    - The integer 123
    - The remaining string '+ 456 * 789'
    """
    m = re.match(r'\d+', s)
    number = int(s[m.start():m.end()])
    rest = s[(m.end()+1):]  # The +1 gets rid of the following space character
    return number, rest


print(pop_number_left('123 + 456 * 789'))


def pop_operator_left(s):
    """Takes a string like ' + 456 * 789' and returns:
    - The operator '+'
    - The remaining string '456 * 789'
    """
    m = re.match(r'[\*\+]', s)
    op = s[m.start():m.end()]
    rest = s[(m.end()+1):]  # The +1 gets rid of the following space character
    return op, rest


print(pop_operator_left('+ 456 * 789'))


def compute_string(s):
    """Compute a final (i.e. without parentheses) string left-to-right"""
    assert '(' not in s and ')' not in s

    result, s = pop_number_left(s)  # the first number of the expression
    while s:
        op, s = pop_operator_left(s)
        next_number, s = pop_number_left(s)
        if op == '+':
            result += next_number
        elif op == '*':
            result *= next_number
        else:
            raise

    return result


print(compute_string('6 + 9 * 8 + 6'))


def compute_expression(s):
    if '(' not in s and ')' not in s:
        return compute_string(s)
    else:
        # Find the first "inner" parentheses-group:
        m = re.search(r'\([^()]+\)', s)
        # Compute its results:
        a_result = compute_string(s[m.start() + 1:m.end() - 1])
        # Replace the expression with the result, and iterate:
        new_s = s[:m.start()] + str(a_result) + s[m.end():]
        return compute_expression(new_s)


print(compute_expression('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'))  # should be 13632

################################################################
# Part 1

total = 0
for line in lines:
    total += compute_expression(line)
print(total)
