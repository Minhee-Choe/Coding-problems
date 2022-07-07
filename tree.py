class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data=data
        self.left=left
        self.right=right
        
class Tree:
    def __init__(self, root=None):
        self.root = root

    def insert(self, node):
        cur = self.root
        prev = None
        
        while cur != None:
            prev=cur
            if cur.data > node.data:                
                cur = prev.left
            else:                
                cur = prev.right

        cur = node
        if prev.data > cur.data:
            prev.left=cur
        else:
            prev.right=cur

    def preOrderTraversal(self, node):
        if node == None:
            return
        print(node.data, end=" ")
        self.preOrderTraversal(node.left)
        self.preOrderTraversal(node.right)
        
    def inOrderTraversal(self, node):
        if node == None:
            return
        self.inOrderTraversal(node.left)
        print(node.data, end=" ")
        self.inOrderTraversal(node.right)

    def postOrderTraversal(self, node):
        if node == None:
            return
        self.postOrderTraversal(node.left)
        self.postOrderTraversal(node.right)
        print(node.data, end=" ")
        
if __name__ == '__main__':
    tree = Tree(Node(34))
    tree.insert(Node(50))
    tree.insert(Node(20))
    tree.insert(Node(37))
    tree.insert(Node(45))
    tree.insert(Node(13))
    tree.insert(Node(15))
    tree.insert(Node(34))
    tree.insert(Node(79))
    tree.preOrderTraversal(tree.root)
    print()
    tree.inOrderTraversal(tree.root)
    print()
    tree.postOrderTraversal(tree.root)
    
    
