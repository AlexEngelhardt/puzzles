#!/usr/bin/python2

def is_palindrome(n):
    reverse_n = str(n)[::-1]  # extended slice syntax [from:to:step]
    return str(n)==reverse_n



def search(until):
    for f1 in range(999, until, -1):
        for f2 in range(f1, until, -1):
            if is_palindrome(f1*f2):
                return {'f1': f1, 'f2':f2}

res = search(900)

print res

print res['f1']*res['f2']
