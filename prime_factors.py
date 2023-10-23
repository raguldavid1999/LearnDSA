def findPrimeFactors(n):
    i = 2
    while(i*i < n):
        if(n%i==0):
            print(i)
            n = int(n/i)
        else:
            i = i+1
    if(n>1):
        print(n)
findPrimeFactors(17)