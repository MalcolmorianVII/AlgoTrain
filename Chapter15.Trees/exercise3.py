#  find greatest value in bst

def find_greatest_value(node):
    if not node.leftChild and not node.rightChild:
        return node.val
    find_greatest_value(node.rightChild)