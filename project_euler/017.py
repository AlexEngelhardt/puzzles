def l(n):
    if n==1 or n==2 or n==6 or n==10:
        return 3
    elif n==3 or n==7 or n==8:
        return 5
    elif n==4 or n==5 or n==9:
        return 4
    elif n==11 or n==12:
        return 6
    elif n==13 or n==14 or n==18 or n==19:
        return 8
    elif n==15 or n==16:
        return 7
    elif n==17:
        return 9
    
    if n==20 or n==30 or n==80 or n==90:
        return 6
    elif n==50 or n==60 or n==40:
        return 5
    elif n==70:
        return 7

    if n>=100 and not n%100: # 100, 200, ..., 900
        return l(n/100) + 7 # hundred
        
    if n==1000:
        return 3+8

    if n>20 and n<100 and n%10: # 21, 22, 23, ..., 29, 31, 32, ..., 99
        return l(n/10 * 10) + l(n%10)

    if n>100:
        return l(n/100 * 100) + 3 + l(n%100)


sum=0
for i in range(1, 1001):
    sum += l(i)

print sum

def s(n):
    if n==1:
        return "one"
    elif n==2:
        return "two"
    elif n==3:
        return "three"
    elif n==4:
        return "four"
    elif n==5:
        return "five"
    elif n==6:
        return "six"
    elif n==7:
        return "seven"
    elif n==8:
        return "eight"
    elif n==9:
        return "nine"
    elif n==10:
        return "ten"
    elif n==11:
        return "eleven"
    elif n==12:
        return "twelve"
    elif n==13:
        return "thirteen"
    elif n==14:
        return "fourteen"
    elif n==15:
        return "fifteen"
    elif n==16:
        return "sixteen"
    elif n==17:
        return "seventeen"
    elif n==18:
        return "eighteen"
    elif n==19:
        return "nineteen"
    elif n==20:
        return "twenty"
    elif n==30:
        return "thirty"
    elif n==40:
        return "forty"
    elif n==50:
        return "fifty"
    elif n==60:
        return "sixty"
    elif n==70:
        return "seventy"
    elif n==80:
        return "eighty"
    elif n==90:
        return "ninety"
    elif n==1000:
        return "onethousand"
    elif n>=100 and not n%100:
        return s(n/100) + "hundred"
    elif n>=100 and n%100:
        return s(n - n%100) + "and" + s(n%100)
    elif n>=10 and n%10:
        return s(n - n%10) + s(n%10)

mysum = 0
for i in range(1,1001):
    mysum += len(s(i))
print mysum

print 342, s(342), len(s(342))
print 115, s(115), len(s(115))
