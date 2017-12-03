
def derp():
    for c in xrange(333, 998): # bis 997!
        for b in xrange(2, c+1):
            a = 1000 - c - b
            if a*a + b*b == c*c:
                return a* b* c # 200, 375, 425

print derp()
