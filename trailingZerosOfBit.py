import math

def bitTrailingZeros(n):
    return int(math.log2((n & (n-1)) ^ n))
print(bitTrailingZeros(168))