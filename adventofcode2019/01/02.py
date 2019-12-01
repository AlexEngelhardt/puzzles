# Do it recursively!
def get_fuel(weight):  # break condition
    initial_fuel = int(weight) // 3 - 2
    if initial_fuel <= 0:
        return 0
    total_fuel = initial_fuel + get_fuel(initial_fuel)
    return total_fuel


with open('input', 'r') as f:
    # initial fuel requirement
    total_fuel = sum([get_fuel(int(module)) for module in f])

print(total_fuel)
