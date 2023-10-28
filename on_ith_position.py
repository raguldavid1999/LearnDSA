def onIthPos(n,i):
    return n | 1<<i

def offIthPos(n,i):
    return n & ~(1<<i)

def flipIthPos(n,i):
    return n ^ 1<<i

def checkOnOff(n,i):
    if((n & 1<<i)==0):
        print('Off')
    else:
        print('On')
print(checkOnOff(36,2))