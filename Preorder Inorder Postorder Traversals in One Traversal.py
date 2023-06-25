# Node class
class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

# Function to perform a combined traversal of preorder, inorder, and postorder
def combinedTraversal(root):
    if root is None:
        return [], [], []

    preorder = []   # List to store preorder traversal
    inorder = []    # List to store inorder traversal
    postorder = []  # List to store postorder traversal

    # Helper function for combined traversal
    def traverse(node):
        nonlocal preorder, inorder, postorder

        if node is None:
            return

        # Preorder: Append the current node to the preorder list
        preorder.append(node.data)

        # Recurse on the left subtree
        traverse(node.left)

        # Inorder: Append the current node to the inorder list
        inorder.append(node.data)

        # Recurse on the right subtree
        traverse(node.right)

        # Postorder: Append the current node to the postorder list
        postorder.append(node.data)

    # Perform the combined traversal
    traverse(root)

    return preorder, inorder, postorder

# Example binary tree
#       1
#     /   \
#    2     3
#   / \   / \
#  4   5 6   7

# Create the binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

# Perform the combined traversal
preorder, inorder, postorder = combinedTraversal(root)

# Print the combined traversal output
print("Preorder traversal:", preorder)
print("Inorder traversal:", inorder)
print("Postorder traversal:", postorder)
