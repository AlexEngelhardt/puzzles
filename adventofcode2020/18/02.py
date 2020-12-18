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


def compute_string(s):
    """Compute a final (i.e. without parentheses) string left-to-right"""
    assert '(' not in s and ')' not in s

    if '*' not in s:
        return eval(s)  # This is just a str without multiplications or parentheses, i.e. a long sum
    else:
        first_star = s.index('*')
        left = s[:first_star].strip()
        right = s[first_star+1:].strip()
        return compute_string(left) * compute_string(right)


print(compute_string('6 + 9 * 8 + 6'))  # should be 210 now


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


print(compute_expression('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'))  # should be 23340 now

################################################################
# Part 2

total = 0
for line in lines:
    total += compute_expression(line)
print(total)
