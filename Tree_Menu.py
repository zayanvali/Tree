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

def Insert(root, k):
    if root == None:
        return tree(k)
    if root.data > k:
        root.leftChild = Insert(root.rightChild, k)
    else:
        root.rightCHild = Insert(root.rightChild, k)
    return root

def InorderSuccesor(root):
    current = root
    while current.leftChild is not None:
        current = current.leftChild
    return current

def delete(root, key):
    if root is None:
        return root
    if key < root.data:
        root.leftChild = delete(root.leftChild, key)
    elif key > root.data:
        root.rightChild = delete(root.rightChild, key)
    else:
        #Root has only 1 child
        if root.leftChild is None:
            temp = root.rightChild
            root = None
            return temp
        #Root has only 1 child
        elif root.rightChild is None:
            temp = root.leftChild
            root = None
            return temp
        #Root has 2 children
        else:
            temp = InorderSuccesor(root)
            print("Hello", temp.data)
            t = root.data
            root.data = temp.data
            temp.data = t
            root.rightChild = delete(root.rightChild, temp.data)

def search(root, value):
    if root.data == value:
        return True
    elif root.data > value and root.left_node != None:
        return search(root.left_node, value)
    elif root.data < value and root.right_node != None:
        return search(root.right_node, value)
    else:
        return False
root = tree(9)
root.left_node = tree(5)
root.left_node.left_node = tree(4)
root.right_node = tree(20)
root.right_node.left_node = tree(17)
root.right_node.right_node = tree(23)
root = Insert(root, 3)
inorder_traversal(root)

number = int(input("Please enter a number from 1-4: "))

if number == 1:
    inorder_traversal(root)

elif number == 2:
    root = Insert(root, 3)

elif number == 3:
    root = delete(root, key)

elif number == 4:
    root = search(root, value)

else:
    print("Invalid answer")