
class TreeNode:
    def __init__(self,val,left=None,right=None) -> None:
        self.val = val
        self.leftChild = left
        self.rightChild = right


class Tree:
    def __init__(self,root=None) -> None:
        self.root = root


def search(value):
        current_node = root
        if current_node.val == value:
            return value
        if value < current_node.val:
            # search left subtree
            root = current_node.leftChild
            return search(value)
        if value > current_node.val:
            # search right subtree
            root = current_node.rightChild
            return search(value)
        else:
            return None


def delete(value,node):
    # base case node is none
    if node is None:
        return None
    elif value < node.val:
        node.leftChild = delete(value,node.leftChild)
        return node
    elif value > node.val:
        node.rightChild = delete(value,node.rightChild)
        return node
    
    # current node the one to delete
    elif value == node.val:
        if node.leftChild is None:
            return node.rightChild
        elif node.rightChild is None:
            return node.leftChild
        else:
            node.rightChild = lift(node.rightChild,node)
            return node

def lift(node,nodeToDelete):
    if node.leftChild:
        node.leftChild = lift(node.leftChild,nodeToDelete)
        return node
    else:
        nodeToDelete.val = node.val
        return node.rightChild

def traverse_and_print(node):
    if node is None:
        return
    traverse_and_print(node.leftChild)
    print(node.val)
    traverse_and_print(node.rightChild)

def find_greatest_value(node):
    if node.rightChild:
        return find_greatest_value(node.rightChild)
    else:
        return node.val
    

node1 = TreeNode(1)
node2 = TreeNode(4)
rootNode = TreeNode(3,node1,node2)

# traverse_and_print(rootNode)

print(find_greatest_value(rootNode))


