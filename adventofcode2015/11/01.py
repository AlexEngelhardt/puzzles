test_input = "abcdefgh"
real_input = "vzbxkghb"


def increase_password(p):
    new_p = p
    return new_p


def password_valid(p):

    return True


def next_valid_password(p):
    new_p = increase_password(p)
    while not password_valid(new_p):
        new_p = increase_password(new_p)
    return new_p


print(test_input)
print(next_valid_password(test_input))

print(real_input)
print(next_valid_password(real_input))
