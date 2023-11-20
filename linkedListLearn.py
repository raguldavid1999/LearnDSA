import heapq

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        print(temp)
        while(temp):
            print(temp.data)
            temp = temp.next

print(__name__)

if(__name__ == '__main__'):
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)

    llist.head.next = second
    second.next = third

    print(llist.head.next, third.next)
    llist.printList()
li = [5,7, 9, 1, 3]

heapq.heapify(li)
heapq.heappush(li,4)
print(li)