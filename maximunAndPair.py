# def maximumAndPair(n):
#     res = 0
#     for i in range(len(n)-1):
#         for j in range(i+1,len(n)):
#             print(n[i],n[j], (n[i] & n[j]))
#             if((n[i] & n[j]) > res):
#                 res = n[i] & n[j]
#     return res

# print(maximumAndPair([16,9,6,13]))
def checkBit(n,m):
    count = 0
    for i in range(len(n)):
        if(m & n[i] == m):
            count = count + 1
    return count

def maxAndValue(n):
    mask = 0
    res = 0
    for i in range(31, -1, -1):
        mask = 1<<i | res
        count = checkBit(n,mask)
        if( count >= 2):
            res = res | mask
    return res

print(maxAndValue([16,9,6,13]))
