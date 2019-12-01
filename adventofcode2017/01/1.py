with open('input') as f:
    number = f.read()

number = number + number[0]  # hack to make it circular

total_sum = 0

for i in range(len(number)-1):
    if number[i] == number[i+1]:
        total_sum += int(number[i])

print(total_sum)
    

