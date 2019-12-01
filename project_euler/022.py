f = open("022.txt", "r")
s = f.readline()
s = s.split(",")
s = [d.strip('"') for d in s]
s = sorted(s)

mysum = 0
for i in range(len(s)):
    name = s[i]
    score = 0
    for c in range(len(name)):
        score += ord(name[c])-64
    score *= (i+1)
    mysum += score
    #print name, i+1, score

print mysum
