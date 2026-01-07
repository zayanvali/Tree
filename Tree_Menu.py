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
        root.left_node = Insert(root.left_node, k)
    else:
        root.right_node = Insert(root.right_node, k)
    return root

def InorderSuccesor(root):
    current = root
    while current.left_node is not None:
        current = current.left_node
    return current

def delete(root, key):
    if root is None:
        return root
    if key < root.data:
        root.left_node = delete(root.left_node, key)
    elif key > root.data:
        root.right_node = delete(root.right_node, key)
    else:
        #Root has only 1 child
        if root.left_node is None:
            return root.right_node
        #Root has only 1 child
        elif root.right_node is None:
            return root.left_node
        #Root has 2 children
        else:
            temp = InorderSuccesor(root.right_node)
            print("Hello", temp.data)
            root.data = temp.data
            root.right_node = delete(root.right_node, temp.data)
    return root

def search(root, value):
    if root is None:
        return False
    if root.data == value:
        return True
    elif root.data > value and root.left_node != None:
        return search(root.left_node, value)
    elif root.data < value and root.right_node != None:
        return search(root.right_node, value)
    else:
        return False
root = tree(9)
for value in [7, 1, 4, 8, 6, 9, 3]:
    root = Insert(root, value)

number = int(input("Please enter a number from 1-4:\n 1. inorder_traversal \n 2. Insertion \n 3. Deletion \n 4. Searching \n Enter your answer: "))

if number == 1:
    inorder_traversal(root)

elif number == 2:
    value = int(input("Enter the value to insert: "))
    root = Insert(root, value)

elif number == 3:
    key = int(input("Enter the value to delete: "))
    answer = delete(root, key)
    print(answer)
    
elif number == 4:
    value = int(input("Enter the value to search"))
    answer = search(root, value)
    print(f"found:{answer}")

else:
    print("Invalid answer")
