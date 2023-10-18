import math

# def checkPrime(n):
#     if(n==1):
#         return False
#     if(n==2 or n==3):
#         return True
#     if(n%2==0 or n%3==0):
#         return False
#     for i in range(5, int(math.sqrt(n))+1, 6):
#         if(n%i==0 or n%(i+2)==0):
#             return False
#     return True

n = 50

# for i in range(n+1):
#     if(checkPrime(i)):
#         print(i)

import numpy as np

array = np.array([0]*(n+1), dtype=bool)

for i in range(2, int(math.sqrt(n))+1):
    if(array[i] == False):
        for j in range(i*i, n+1, i):
            array[j] = True
for i in range(2,n+1):
    if(array[i]==False):
        print(i)