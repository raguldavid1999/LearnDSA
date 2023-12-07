# import heapq

# class Node:

#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkedList:

#     def __init__(self):
#         self.head = None

#     def printList(self):
#         temp = self.head
#         print(temp)
#         while(temp):
#             print(temp.data)
#             temp = temp.next

# print(__name__)

# if(__name__ == '__main__'):
#     llist = LinkedList()
#     llist.head = Node(1)
#     second = Node(2)
#     third = Node(3)

#     llist.head.next = second
#     second.next = third

#     print(llist.head.next, third.next)
#     llist.printList()
# li = [5,7, 9, 1, 3]

# heapq.heapify(li)
# heapq.heappush(li,4)
# print(li)

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def add_before(self, data):
        new_node = Node(data)
        first_node = self.head
        self.head = new_node
        self.head.next = first_node

    def delete_before(self):
        if self.head:
            self.head = self.head.next
            return
        return None
    
    def delete_end(self):
        current = self.head
        if current is None:
            print('List is empty')
        elif current.next is None:
            current = None
        else:
            while current.next.next:
                current = current.next
            current.next = None
    def delete_by_value(self, data):
        if self.head is None:
            print('Linked list is empty')
            return
        elif self.head.data == data:
            self.head = self.head.next
            return
        else:
            current = self.head
            while current.next is not None:
                if current.next.data == data:
                    current.next = current.next.next
                    return
                current = current.next
            print('Not in the list')
            # while current.next is not None:
            #     if data == current.next.data:
            #         break
            #     current = current.next
            # if current.next is None:
            #     print('Not in list')
            # else:
            #     current.next = current.next.next
            
        
            
            

    def get_node(self,value):
        current_node = self.head

        while current_node:
            if current_node.data == value:
                return current_node
            current_node = current_node.next
        return None
    
    def insert_node(self, before_node, value):
        new_node = Node(value)
        new_node.next = before_node.next
        before_node.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
        print("None")

mylist = Linkedlist()
mylist.append(1)
mylist.append(2)
mylist.append(3)
mylist.add_before(5)
mylist.display()
# mylist.delete_before()
mylist.insert_node(mylist.get_node(2), 4)
mylist.display()
mylist.delete_by_value(5)
# mylist.delete_end()

mylist.display()