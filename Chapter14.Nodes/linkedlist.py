
from pickle import NONE


class Node:
    def __init__(self,item) -> None:
        self.item = item
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def read(self,index):
        current_node = self.head
        current_index = 0

        while current_index < index:
            current_node = current_node.next
            current_index += 1
            if not current_node:
                return None
        return current_node.item

    def index_of(self,item):
        current_node = self.head
        current_index = 0

        while True:
            if current_node.next == None:
                return None
            if current_node.item == item:
                return current_index
            current_node = current_node.next
            current_index += 1



ll = LinkedList()
# Assign item values
ll.head = Node(1)
second = Node(2)
third = Node(3)

# link the nodes

ll.head.next = second
second.next = third
# third.next = None

# Print the linked list item
# while ll.head != None:
#     print(ll.head.item, end=" ")
#     ll.head = ll.head.next

# print(ll.read(5))
print(ll.index_of(4))

# print(len(ll))