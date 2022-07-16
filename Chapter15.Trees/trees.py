
class TreeNode:
    def __init__(self,val,left=None,right=None) -> None:
        self.val = val
        self.leftChild = left
        self.rightChild = right


class Tree:
    def __init__(self,root=None) -> None:
        self.root = root

    def search(self,value):
        current_node = self.root
        if current_node.val == value:
            return value
        if value < current_node.val:
            # search left subtree
            self.root = current_node.leftChild
            return search(self,value)
        if value > current_node.val:
            # search right subtree
            self.root = current_node.rightChild
            return search(self,value)
        else:
            return None
        



node1 = TreeNode(1)
node2 = TreeNode(4)
rootNode = TreeNode(3,node1,node2)



