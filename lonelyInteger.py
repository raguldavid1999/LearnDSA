def loneInteger(n):
    n = sorted(n)
    setMemory = set();
    for i in n:
        if(i in setMemory):
            setMemory.discard(i)
        else:
            setMemory.add(i)
    return list(setMemory)[0]

def lonelyInteger(n):
    m = 0
    for i in n:
        m = m^i
    return m

print(lonelyInteger([5,1,4,4,5,3,1]))

print(type(set({})))