
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
    
    def delete(self,index):
        # If deleting first  node
        if index == 0:
            self.head = self.head.next
        current_node = self.head
        current_index = 0

        while current_index < index-1 :
            current_node = current_node.next
            current_index += 1
        
        node_after_deleted_node = current_node.next.next
        current_node.next = node_after_deleted_node

    def print_all(self):
        current_node = self.head
        while current_node:
            print(current_node.item)
            current_node = current_node.next
    def return_last_node(self):
        current_node = self.head

        while current_node.next:
            current_node = current_node.next
        print(current_node.item)
    def reverse_ll(self):
        new_ll = LinkedList()
        first_node = self.head
        next_node = first_node.next

        while next_node:
            new_ll.head = next_node
            new_ll.next = first_node


ll = LinkedList()
# Assign item values
ll.head = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)
five = Node(5)
six = Node(6)
seven = Node(7)

# link the nodes

ll.head.next = second
second.next = third
third.next = fourth
fourth.next = five
five.next = six
six.next = seven


# Print the linked list item
# while ll.head != None:
#     print(ll.head.item, end=" ")
#     ll.head = ll.head.next

# print(ll.read(3))
# # print(ll.index_of(3))
# ll.delete(3)
# print(ll.read(3))
# print(len(ll))
# ll.print_all()
ll.return_last_node()