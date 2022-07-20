
class Heap:
    def __init__(self) -> None:
        self.data = []

    def rootNode(self):
        return self.data[0]

    def lastNode(self):
        return self.data[-1]

    def left_child_index(index):
        return (index * 2) + 1

    def right_child_index(index):
        return (index * 2) + 2

    def parent_index(index):
        return (index - 1) / 2
    def insertion(self,value):
        self.data.append(value)
        new_node_index = len(self.data) - 1
        # parent_node = parent_index(new_node_index)

        while new_node_index > 0 and self.data[new_node_index] > self.data[parent_index(new_node_index)]:
            # Swap the new node with parent
            self.data[parent_index(new_node_index)],self.data[new_node_index] = self.data[new_node_index],self.data[parent_index(new_node_index)]
            # Update index of new node
            new_node_index = parent_index(new_node_index)
    
    def delete(self):
        self.data[0] = self.data.pop()
        # Track current index of the "trickle node"
        trickle_node_index = 0
        # Get right & left children
        left_child = self.data[left_child_index(trickle_node_index)]
        right_child = self.data[right_child_index(trickle_node_index)]
        larger_child = max(left_child,right_child)

        while has_greater_child(trickle_node_index):
            # Save larger child index in variable
            larger_child_index = calculate_larger_child_index( trickle_node_index)
            # Swap the trickle node index with its larger child
            self.data[trickle_node_index],self.data[larger_child_index]=self.data[larger_child_index],self.data[trickle_node_index]
            # Update trickle nodes index
            trickle_node_index = larger_child_index

    def has_greater_child(self,index):
        (self.data[left_child_index(index)] 
        and self.data[left_child_index(index)] > self.data[index]) or (self.data[right_child_index(index)]
         and self.data[right_child_index(index)] > self.data[index])

    def calculate_larger_child_index(self,index):
        # If no right child
        if not self.data[right_child_index(index)]:
            # Return left child
            return left_child_index(index)
        
        if self.data[right_child_index(index)] > self.data[left_child_index(index)]:
            return right_child_index(index)
        else:
            return left_child_index(index)


    