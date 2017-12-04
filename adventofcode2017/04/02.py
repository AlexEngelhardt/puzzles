valid = 0

with open("input.txt", "r") as f:
    for line in f:
        words = line[:-1].split(" ")
        # https://stackoverflow.com/questions/13464152/typeerror-unhashable-type-list-when-using-built-in-set-function
        letters = list(map(lambda word: tuple(sorted(list(word))), words))
        if len(letters) == len(set(letters)):
            valid += 1
        
print(valid)


## An alternative could go something like this:
# "".join(sorted(s)) for s in l.split(" ")
## Here, you compare sorted words instead of lists of chars
