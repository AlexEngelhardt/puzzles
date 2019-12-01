import csv

tsvfile = open('input', "r")
tsv = csv.reader(tsvfile, delimiter='\t')
ll = list(tsv)

sum = 0

for row in ll:
    nums = list(map(lambda x: int(x), row))
    for dividend in nums:
        for divisor in nums:
            if dividend % divisor == 0:
                if dividend != divisor:  # better: check if index is equal
                    # print(str(dividend) + " / " + str(divisor) + " passt!")
                    sum += dividend / divisor

print(int(sum))
    

