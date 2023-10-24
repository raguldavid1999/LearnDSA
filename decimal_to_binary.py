def decimalToBinary(n):
    b = ''
    while(n>=1):
        x = n%2
        n = int(n/2)
        b = str(x) + b
    return b

def binaryToDecimal(n):
    res = 0;
    powOf2 = 1
    for i in range(len(n)-1,-1,-1):
        if(n[i]=='1'):
            res = res + powOf2
        powOf2 = powOf2 * 2
    return res

n = decimalToBinary(45)
print(binaryToDecimal(n))