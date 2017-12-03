import math
#which = 3  # third item in list
which = 1000000

which -= 1
ordered = []

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(10, 0, -1):
    index = which % math.factorial(i) / math.factorial(i-1)
    ordered.append(numbers.pop(index))

print ordered


# index0 = which % math.factorial(10) / math.factorial(9)
# ordered.append(numbers.pop(index0))

# index1 = which % math.factorial(9) / math.factorial(8)
# ordered.append(numbers.pop(index1))

