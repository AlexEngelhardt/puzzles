def deparse(s):
    s = s.replace("\\", "\\\\")
    s = s.replace('"', '\\"')
    return '"' + s + '"'


with open('input') as f:
    strings = f.read().splitlines()

total_diff = 0

for s in strings:
    # print(s)
    # print(deparse(s))
    # print('----')
    total_diff += len(deparse(s)) - len(s)

print(total_diff)
