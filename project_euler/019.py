import sys
until = int(sys.argv[1])
day = 1 #mon
sundays = 0

for y in range(1900, until+1):
    for m in range(1,13):
        if m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
            days_in_month = 31
        elif m==4 or m==6 or m==9 or m==11:
            days_in_month = 30
        elif m==2:
            if not y%400:
                days_in_month=29
            elif not y%100:
                days_in_month=28
            elif not y%4:
                days_in_month=29
            else:
                days_in_month=28
        #print m, "/", y, ":", days_in_month, "days, now:", day    
        day = (day + days_in_month) % 7
        if day==0:
            sundays += 1

print sundays, "sundays from 1.1.1900 until 31.12.", until
