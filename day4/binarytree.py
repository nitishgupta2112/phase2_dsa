class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
# A function to do inorder tree traversal
def Inorder(root):
    if root:
        Inorder(root.left)
        print(str(root.val) + "->" ,end='')
        Inorder(root.right)

def Preorder(root):
    if root:
        print(str(root.val) + "->" ,end='')
        Preorder(root.left)
        Preorder(root.right)

def Postorder(root):
    if root:
        Postorder(root.left)
        Postorder(root.right)
        print(str(root.val) + "->" ,end='')

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print("Inorder")
Inorder(root)
print()
print("post Order")
Postorder(root)
print()
print("Preorder")
Preorder(root)