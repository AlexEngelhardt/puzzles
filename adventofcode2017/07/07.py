import re

with open("input.txt", "r") as f:
    lines = [l.strip().replace(",", "") for l in f.readlines() if re.match("(.*)->", l)]

# print(lines)

fathers = {}

for line in lines:
    elems = line.split(" ")
    father = elems[0]
    kids = elems[3:]
    # print("dad ", father, ", kids ", kids)
    for kid in kids:
        fathers[kid] = father

# dict fathers: key is kid, value is father. take any kid and ascend until
# person is no key anymore (i.e. has no father in tree)

# start with any kid (here, the last line in the file)
while kid in fathers:
    kid = fathers[kid]  # ascend the pedigree one step

print(kid)
