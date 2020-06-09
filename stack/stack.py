"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order.

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when
   implementing a Stack?
"""
from singly_linked_list import *


# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return len(self.storage)

#     def push(self, value):
#         self.storage.extend([value])

#     def pop(self):
#         if len(self.storage) > 0:
#             value = self.storage[-1]
#             self.storage.pop()

#             return value


class Stack:
    def __init__(self):
        self.head = None
        self.tail = None
        self.storage = LinkedList()

    def __len__(self):
        temp = self.head
        count = 0
      #   if count temp is > 1 then while loop will run and add one to count
        while (temp):
            count += 1
            temp = temp.next
            # return the count. to see how many items are in the node
        return count

    def push(self, value):
      #  if head is empty then we will add a new node to it
        if self.head is None:
            self.head = Node(value)
        else:
            newNode = Node(value)
            # else we add another node and call next
            newNode.next = self.head
            self.head = newNode

    def pop(self):
      #   if head is empty we just return None
        if self.head is None:
            return None
        else:
            popped = self.head
            self.head = self.head.next
            popped.next = None
            return popped.value
