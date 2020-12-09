# debug = True
debug = False

if debug:
    filename = 'test_input'
    preamble = 5
else:
    filename = 'input'
    preamble = 25

with open(filename) as f:
    numbers = list(map(int, f.read().splitlines()))


################################################################
# Part 1

def does_sum_exist(numbers, i, preamble):
    for num_1 in range(i-preamble, i-1):
        for num_2 in range(num_1+1, i):
            if numbers[num_1] + numbers[num_2] == numbers[i]:
                print(f'{numbers[num_1]} + {numbers[num_2]} == {numbers[i]}')
                return True
    return False


for i in range(preamble, len(numbers)):

    valid = does_sum_exist(numbers, i, preamble)
    if not valid:
        bad_number = numbers[i]
        print(f'iteration {i}, number is {bad_number}, does not compute')
        break


################################################################
# Part 2
# Go with a queue, somehow?

i_start = 0
i_end = 0  # the range sum including this index's number
range_sum = numbers[0]
target_sum = bad_number

while True:
    while range_sum < target_sum:
        i_end += 1
        range_sum += numbers[i_end]

        if range_sum == target_sum:
            print(f'The range from numbers[{i_start}]=={numbers[i_start]} to numbers[{i_end}]=={numbers[i_end]} gives {target_sum}')
            print(f'Their min/max are {min(numbers[i_start:i_end+1])} and {max(numbers[i_start:i_end+1])}')
            print(f'Their sum is {min(numbers[i_start:i_end+1]) + max(numbers[i_start:i_end+1])}')
            exit(0)

    i_start += 1
    range_sum -= numbers[i_start-1]

    while range_sum >= target_sum:
        i_end -= 1
        range_sum -= numbers[i_end+1]

# 52858841 is wrong