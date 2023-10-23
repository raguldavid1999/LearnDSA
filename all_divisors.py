import math

def allDevisors(n):
    i = 1
    for i in range(i,int(math.sqrt(n))+1):
        if(n%i==0):
            print(i)
    for i in range(i,0,-1):
        if(n%i==0 and i != int(n/i)):
            print(int(n/i))


n = 40
allDevisors(n)