def reverseBit(n, len):
    f = len - 1
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

def nthPalindromeBinary(n):
    count = 0
    l = 0
    while(count<n):
        l = l + 1
        count = count + int(pow(2, (l-1)/2))
    count = count - int(pow(2,(l-1)/2))
    ele = n - count -1
    ans = 1 << (l-1) | ele << int((l/2))
    ans = ans | reverseBit(ans, l)
    return bin(ans).replace("0b", "")

print(nthPalindromeBinary(12))