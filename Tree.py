class tree():
    def __init__(self, data):
        self.data = data
        self.left_node = None
        self.right_node = None

    def inorder_traversal(root):
        if root.left_node != None:
            inorder_traversal(root.left_node)
        print(root.data)
        if root.right_node != None:
            inorder_traversal(root.right_node)

    def preorder_traversal(root):
        print(root.data)
        if root.left_node != None:
            preorder_traversal(root.left_node)
        if root.right_node != None:
            preorder_traversal(root.right_node)
    
    def postorder_traversal(root):
        if root.left_node != None:
            postorder_traversal(root.left_node)
        if root.right_node != None:
            postorder_traversal(root.right_node)
        print(root.data)

root = tree(5)
root.left_node = tree(4)
root.left_node.left_node = tree(9)
root.right_node = tree(8)
root.right_node.left_node = tree(7)
root.right_node.right_node = tree(6)
inorder_traversal(root)
preorder_traversal(root)
postorder_traversal(root)