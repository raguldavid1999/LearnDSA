li = [5,6,7,9,11,13,17,21,25]
findValue = 15
first = 0
last = len(li) - 1

def binarySearch(li,first,last,value):
    if(last>=first):
        mid = int((first + last)/2)
        if(li[mid]==value):
            return mid
        elif(value > li[mid]):
            first = mid + 1
            return binarySearch(li,first,last,value)
        else:
            last = mid - 1
            return binarySearch(li,last,first,value)
    else:
        return -1
    
print(binarySearch(li,first, last, findValue))