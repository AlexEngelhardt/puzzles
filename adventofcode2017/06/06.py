import math
import copy

with open("input.txt", "r") as f:
    starting_bank = list(map(int, f.read().strip().split("\t")))

steps = 0
bank = starting_bank
bank_size = len(bank)

print(starting_bank)

history = [copy.copy(starting_bank)]

while True:
    # print("iter: ", steps)
    the_max = max(bank)
    the_index = bank.index(the_max)  # first index if multiple
    bank[the_index] = 0
    add_me = math.floor(the_max / bank_size)  # integer division if max > bank_size
    bank = [i + add_me for i in bank]
    
    add_me_remainder = the_max % bank_size
    add_me_remainder_positions = range(the_index + 1, the_index + add_me_remainder + 1)
    for i in add_me_remainder_positions:
        bank[i % bank_size] = bank[i % bank_size] + 1
    steps += 1

    # print("bank:", bank)

    if bank in history:
        
        break

    # print("i am appending", bank)
    history.append(copy.copy(bank))
    # print("last 3 of history:", history[-3:])
    
    # if steps > 100:
    #     break

print("number of steps:", steps)

print("size of loop:", steps - history.index(bank))  # part 2
