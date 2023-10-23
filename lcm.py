# def findLCM(a,b):
#     res = max(a,b)
#     while(True):
#         if(res%a == 0 and res%b == 0):
#             break
#         res = res+1
#     return res

def gabriel_gcd(a, b):
    while(a!=0 and b!=0):
        if(a>b):
            a = a%b
        else: 
            b = b%a
    if(a!=0):
        return a
    else:
        return b
    
def euclidLCM(a,b):
    return int((a*b)/gabriel_gcd(a, b))

a = 15
b = 20

print(euclidLCM(a,b))