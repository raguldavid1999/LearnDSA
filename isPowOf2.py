def isPowOf2(n):
    if(n == 0):
        return False
    return (n & (n-1))==0;

print(isPowOf2(62))