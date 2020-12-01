with open('input') as f:
    numbers = list(map(int, f.read().splitlines()))


for i in range(len(numbers) - 2):
    for j in range(i, len(numbers) - 1):
        for k in range(j, len(numbers)):
            if numbers[i] + numbers[j] + numbers[k] == 2020:
                print(numbers[i], numbers[j], numbers[k])
                print(numbers[i] * numbers[j] * numbers[k])
                exit(0)
