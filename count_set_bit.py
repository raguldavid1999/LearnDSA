# char = '00101010'
# count = 0

# for i in range(len(char)):
#     if(char[i]=='1'):
#         count = count + 1
# print(count)

def countSetBit(n):
    count = 0
    while(n>0):
        n = n & (n-1)
        count = count + 1
    return count

print(countSetBit(4))
