def make(amount, coins):
    #print "In make(", amount, ", ", coins, ")"

    if amount==0:  # last level of recursion reached: amount is fully composed with coins
        return 1

    if amount==min(coins):  # there is only one way left (i.e. amount == 1ct mostly)
        return 1

    if len(coins)==1:
        if amount % coins[0] == 0:
            return 1  # total: 33ct, coins: [1ct], then modulo == 0
        else:  # in this case, e.g. coins = [2ct] but total = 33ct, i.e. 0 ways.
            return 0   # This will never happen when smallest coin is 1ct

    coins.sort()
    while coins[-1] > amount:
        coins.pop()
    
    #print coins
    #print "Now calling make(", amount - coins[-1], ",",  coins, ") + make(", amount,",", coins[:-1], ")"

    # The following two statements yield TWO DIFFERENT RESULTS!
    #return make(amount - coins[-1], coins) +make(amount, coins[:-1])  # wrong: 60017
    return make(amount, coins[:-1]) + make(amount - coins[-1], coins)  # correct: 73682



coins = [1, 2, 5, 10, 20, 50, 100, 200]
amount = 200
print make(amount, coins)


