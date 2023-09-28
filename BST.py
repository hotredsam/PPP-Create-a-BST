class BSTNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
    
    def __str__(self):
        return str(self.data)
    
    def __repr__(self):
        return str(self.data)

class BST:
    def __init__(self, root=None):
        self.root = root
        self.contents = []
        self.output = ""
        
    def __str__(self):
        self.output = ""
        if self.root is None:
            return "The tree is empty"
        self.print_tree(self.root)
        return self.output
    
    def __repr__(self):
        return self.__str__()
    
    def print_tree(self, node, level=0):
        if node:
            self.print_tree(node.right, level + 1)
            self.output += ' ' * 4 * level + '-> ' + str(node.data) + '\n'
            self.print_tree(node.left, level + 1)

    def add(self, value):
        if not isinstance(value, (int, BSTNode)):
            raise ValueError("Invalid input type.")
        
        new_node = value if isinstance(value, BSTNode) else BSTNode(value)
        
        if new_node.data in self.contents:
            return
        
        self.contents.append(new_node.data)
        
        if not self.root:
            self.root = new_node
            return
        
        self.add_node(self.root, new_node)
        
    def add_node(self, current, new_node):
        if new_node.data > current.data:
            if current.right:
                self.add_node(current.right, new_node)
            else:
                current.right = new_node
        else:
            if current.left:
                self.add_node(current.left, new_node)
            else:
                current.left = new_node

# Test the code
node1 = BSTNode(3)
print(node1)

node2 = BSTNode(4, left=node1)
print(node2)

node3 = BSTNode()
print(node3)
node3.data = 5
print(node3)

bst = BST()
print(bst)

bst.root = node2
print(bst)

node2.right = node3
print(bst)

# Adding elements to the tree
node8 = BSTNode(8)
node3 = BSTNode(3)
node10 = BSTNode(10)
node1 = BSTNode(1)
node6 = BSTNode(6)
node14 = BSTNode(14)
node4 = BSTNode(4)
node7 = BSTNode(7)
node13 = BSTNode(13)

bst = BST()
bst.add(node8)
bst.add(node3)
bst.add(node10)
bst.add(node1)
bst.add(node6)
bst.add(node14)
bst.add(node4)
bst.add(node7)
bst.add(node13)
print(bst)
