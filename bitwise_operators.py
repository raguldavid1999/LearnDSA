# print(~-2)

# or mask or switch on the i'th position
n = 36
i = 5
onMask = 1<<i

print(n | onMask)

# and mask or switch off the i'th position

offMask = ~(1<<i)

print(n & offMask)

# xor mask or switch off the i'th position

tmask = 1 << i

print(n ^ tmask)

# check on or off operations

cMask = 1 << i
if(n & cMask == 0):
    print('off')
else:
    print('on')