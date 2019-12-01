with open('input') as f:
    number = f.read()

number = number + number[0]  # hack to make it circular

# The list is sure to have an even number of elements
offset = int(len(number) / 2)

total_sum = 0

for i in range(round(len(number) / 2)):
    print("checking " + str(number[i]) + " + " + str(number[i + offset]))
    if number[i] == number[i + offset]:
        total_sum += int(number[i])

print(total_sum * 2)  # double it because you check in "both directions"
    

123456
