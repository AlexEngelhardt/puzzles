import numpy


f = open("067.txt", "r")
T = []
for line in f:
    mystring = line.strip()
    mylist = mystring.split(" ")
    #mylist = [int(x) for x in mylist]  # this, or
    mylist = map(int, mylist)           # this. 
    T.append(mylist)

for row in reversed(range(len(T)-1)):  # Starte in vorletzter Reihe
    for i in range(len(T[row])):
        T[row][i] += max(T[row+1][i], T[row+1][i+1])

print T[0]
