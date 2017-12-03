#!/usr/bin/python2

def derp():
    checkme = start
    while True:
        derp = True
        for div in range(9,21): # 1-8 (and 10) not necessary
            if not checkme % div == 0:
                derp = False
                break
        if derp == True:
            return checkme
        checkme += 1


a = derp()
print a
