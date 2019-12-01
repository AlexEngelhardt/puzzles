valid = 0
with open("input.txt", "r") as f:
    for line in f:
        words = line[:-1].split(" ")
        if len(words) == len(set(words)):
            print(words)
            valid += 1
print(valid)
