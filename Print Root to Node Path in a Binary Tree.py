# Node class
class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

# Function to print the root-to-node path
def printRootToNodePath(root, target):
    # Base case: if the tree is empty
    if root is None:
        return False

    # Append the current node to the path list
    path.append(root.data)

    # If the target node is found, print the path and return True
    if root.data == target:
        print("Root-to-Node path:", path)
        return True

    # Recursively check the left and right subtrees
    if (printRootToNodePath(root.left, target) or printRootToNodePath(root.right, target)):
        return True

    # If the target node is not found in the current subtree, remove the current node from the path list
    path.pop()
    return False

# Create the binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.left = Node(6)
root.left.right.right = Node(7)

# Initialize an empty list to store the path
path = []

# Specify the target node
target_node = 7

# Call the function to print the root-to-node path
printRootToNodePath(root, target_node)
