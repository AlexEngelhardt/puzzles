with open('test_input') as f:
    test_lines = f.read().splitlines()
with open('input') as f:
    lines = f.read().splitlines()


def parse_code(code):
    code = code.replace('B', '1')
    code = code.replace('F', '0')
    code = code.replace('R', '1')
    code = code.replace('L', '0')
    return int(code, 2)


for c in test_lines:
    print(c, parse_code(c))

# Part 1
max_seat = max(map(parse_code, lines))
print(max_seat)

# Part 2
assigned_seats = set()
for c in lines:
    assigned_seats.add(parse_code(c))
min_seat = min(assigned_seats)

for seat_id in range(min_seat, max_seat):
    if seat_id not in assigned_seats:
        print(seat_id)
        break

