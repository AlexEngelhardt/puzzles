
test_input = "1"
real_input = "1321131112"
real_input_2 = "1321131112"

# I think we need RLE (run-length encoding) here.


def step(s):

    new_s = ''
    counter = 1
    current_char = s[0]
    prev_char = current_char

    for current_char in s[1:]:

        if current_char == prev_char:
            counter += 1
        else:
            new_s += str(counter)
            new_s += prev_char
            counter = 1
            prev_char = current_char

    new_s += str(counter)
    new_s += current_char

    return new_s


print(test_input)
for i in range(5):
    test_input = step(test_input)
    print(test_input)

# part 1:

for i in range(40):
    real_input = step(real_input)

print(len(real_input))

# part 2:

for i in range(50):
    real_input_2 = step(real_input_2)

print(len(real_input_2))
