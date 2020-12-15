debug = False

if debug:
    filename = 'test_input'
    n_turns = 30000000  # 10
else:
    filename = 'input'
    n_turns = 30000000  # 2020 for part 1, 30000000 for part 2

with open(filename) as f:
    numbers = list(map(int, f.readline().split(",")))

len_input_numbers = len(numbers)
print(numbers)
prev_numbers = dict()  # key: the number; value: a list of turn IDs where this number was seen

# Fill prev_numbers:
for i, number in enumerate(numbers[:-1]):
    turn = i+1
    if number not in prev_numbers:
        prev_numbers[number] = list()
    prev_numbers[number].append(turn)

print(prev_numbers)

# Now generate new numbers until turn 2020:
for i in range(n_turns - len(numbers)):
    turn = i + len_input_numbers + 1

    last_number = numbers[-1]
    if last_number not in prev_numbers:
        prev_numbers[last_number] = [turn-1]
        new_number = 0
    else:
        prev_numbers[last_number].append(turn - 1)
        new_number = prev_numbers[last_number][-1] - prev_numbers[last_number][-2]

    numbers.append(new_number)


print(numbers[-1])
