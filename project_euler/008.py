f = open("008.txt", "r")
l = f.readlines()
s = ''.join(l)  # <- the character that joins the elements is the one upon which the function is called
s = s.replace('\n', '')

max_prod = 0

for start in xrange(0, len(s)-4):
    these_five = s[start:start+5]
    prod = int(these_five[0]) * int(these_five[1]) * int(these_five[2]) * int(these_five[3]) * int(these_five[4])
    if prod > max_prod:
        best_five = these_five
        max_prod = prod

print best_five, max_prod
