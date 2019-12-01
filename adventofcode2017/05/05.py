numbers = []
with open("input.txt", "r") as f:
    # for num in f:
    #     numbers.append(int(num))
    numbers = list(map(int, [boop for boop in f.read().split("\n") if boop != ""]))

print(numbers)

n_steps = 0
i = 0
while i < len(numbers):
    forward_steps = numbers[i]
    # if numbers[i] >= 3:  # comment out for part 1
    #     numbers[i] -= 1  # comment out for part 1
    # else:                # comment out for part 1
    numbers[i] += 1

    n_steps += 1
    i = i + forward_steps

print(n_steps)
