def reverseBit(n):
    f = 31
    l = 0
    rev = 0
    while(l<f):
        if( n & (1<<f) != 0):
            rev = rev | (1<<l)
        if(n & (1<<l) != 0):
            rev = rev | (1<<f)
        f = f-1
        l = l+1
    return rev

print(reverseBit(1))