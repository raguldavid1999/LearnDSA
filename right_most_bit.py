# def posOfrmsb(n):
#     m = 1
#     position = 0
#     if n==0:
#         return -1
#     while((n & m)==0):
#         m = m << 1
#         position = position + 1
#     return position + 1

import math
def posOfrmsb(n):
    return int(math.log2(n ^ (n-1))) + 1

print(posOfrmsb(40))

