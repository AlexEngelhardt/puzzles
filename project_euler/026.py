# http://hr.userweb.mwn.de/numb/period.html

def div_out(n, factors):
    # divide out the list of factors from a digit.
    # e.g., div_out(300, [2, 5]) would return 3.
    # This does not change period length
    for f in factors:
        while n % f == 0:
            n /= f
    return n

def len_period(q):
    # length of period in fraction 1/n
    q = div_out(q, [2, 5])
    if q==1:
        return 0
    # The period of q now starts at the decimal point. Also, q ends in 1,3,7, or 9
    k=1  # will be period length
    # impose upper bound on period length, k <= 100
    while (10**k-1) % q != 0:
        k += 1
    return k


max_q = 1
max_period_len = 0
for q in range(1, 1001):
    if len_period(q) > max_period_len:
        max_period_len = len_period(q)
        max_q = q

print max_q
