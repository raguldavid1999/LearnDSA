import math
def posOfrmsb(n):
    return int(math.log2(n ^ (n-1))) + 1

print(posOfrmsb(40))

