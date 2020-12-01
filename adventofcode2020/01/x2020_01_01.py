with open('input') as f:
    numbers = list(map(int, f.read().splitlines()))


for i in range(len(numbers) - 1):
    for j in range(i, len(numbers)):
        if numbers[i] + numbers[j] == 2020:
            print(numbers[i], numbers[j])
            print(numbers[i] * numbers[j])
            exit(0)
