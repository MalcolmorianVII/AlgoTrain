class Node:
    def __init__(self,item) -> None:
        self.item = item
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self,first_node=None,last_node=None) -> None:
        self.head = first_node
        self.tail = last_node

    def read(self,index):
        current_node = self.head
        current_index = 0

        while current_index < index:
            current_node = current_node.next
            current_index += 1
            if not current_node:
                return None
        return current_node.item
    
    def print_all_reverse(self):
        current_node = self.tail
        while current_node:
            print(current_node.item)
            current_node = current_node.prev
    

dl = DoublyLinkedList()

# Assign item values
dl.head = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)
five = Node(5)
six = Node(6)
dl.tail = Node(7)

# link the nodes
# Forward
dl.head.next = second
second.next = third
third.next = fourth
fourth.next = five
five.next = six
six.next = dl.tail

# link the nodes
# Backward
# dl.head.next = second
second.prev = dl.head
third.prev = second
fourth.prev = third
five.prev = fourth
six.prev = five
dl.tail.prev = six
# print(dl.read(6))
# print(seven.prev.item)
# print(dl.tail.item)
print(dl.print_all_reverse())