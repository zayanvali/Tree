class tree():
    def __init__(self, data):
        self.data = data
        self.left_node = None
        self.right_node = None

def preorder_traversal(root):
    print(root.data)
    if root.left_node != None:
        preorder_traversal(root.left_node)
    if root.right_node != None:
        preorder_traversal(root.right_node)

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

def add_new_node(root, value):
    if root == None:
        return tree(value)
    if value > root.data:
        root.right_node = add_new_node(root.right_node, value)
    else:
        root.left_node = add_new_node(root.left_node, value)
    return root

root = tree(9)
for value in [7, 1, 4, 8, 6, 5, 3]:
    root = Insert(root, value)

number = int(input("Please enter a number from 1-3:"))

if number == 1:
    preorder_traversal(root)

elif number == 2:
    value = int(input("Enter the value to insert: "))
    root = Insert(root, value)
    preorder_traversal(root)
    print()

elif number == 3:
    key = int(input("Enter the value to delete: "))
    answer = delete(root, key)
    print(f"\n Tree after deleting {key}: ")
    preorder_traversal(answer)
    print()

else:
    print("Invalid answer")