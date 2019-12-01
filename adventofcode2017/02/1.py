import csv

tsvfile = open('input', "r")
tsv = csv.reader(tsvfile, delimiter='\t')
ll = list(tsv)

sum = 0

for row in ll:
    nums = list(map(lambda x: int(x), row))
    diff = max(nums) - min(nums)
    sum += diff

print(sum)
    

