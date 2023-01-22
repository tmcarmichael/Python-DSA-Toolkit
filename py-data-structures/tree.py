# Implement a Tree with methods for traversing the tree in preorder, postorder, and inorder.

# Tree Node class
class Node:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data

# Preorder traversal
# Root -> Left subtree -> Right subtree
def preorderTraversal(root):
    res = []
    if root:
        res.append(root.data)
        res = preorderTraversal(root.left)
        res = res + preorderTraversal(root.right)
    return res

# Inorder traversal
# Left subtree -> Root -> Right subtree
def inorderTraversal(root):
    res = []
    if root:
        res = inorderTraversal(root.left)
        res.append(root.data)
        res = res + inorderTraversal(root.right)
    return res

# Postorder traversal
# Left subtree -> Right subtree -> Root
def postorderTraversal(root):
    res = []
    if root:
        res = postorderTraversal(root.left)
        res = res + postorderTraversal(root.right)
        res.append(root.data)
    return res

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    treePtr = root
    treePtr = root.left
    treePtr.left = Node(4)

    print('Inorder Traversal:')
    inorderTraversal(root)
    print('Preorder Traversal:')
    preorderTraversal(root)
    print('Postorder Traversal:')
    postorderTraversal(root)