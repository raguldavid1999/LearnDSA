def trailingZero(n):
    res = 0
    i = 5
    while(n>=i):
        res = res + int(n/i)
        i = i*5
    return res

n = 226

print(trailingZero(n))