# def gcd(a, b):
#     min = 0
#     if(a>b):
#         min = b 
#     else:
#         min = a

#     for i in range(min,0,-1):
#         if(a%i==0 and b%i==0):
#             return i
#     return 1

# def eqlid_gcd(a, b):
#     while(a!=b):
#         if(a>b):
#             a = a-b
#         else: 
#             b = b-a
#     return a

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
        
a = 20
b = 15
print(gabriel_gcd(a,b))
