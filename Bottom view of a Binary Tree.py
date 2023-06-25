# Node class
class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None
        self.hd = 0

# Function to perform level order traversal and find the bottom view of a binary tree
def findBottomView(root):
    if root is None:
        return

    # Dictionary to store the last node encountered at each horizontal distance
    node_dict = {}

    # Queue for level order traversal
    queue = []
    root.hd = 0
    queue.append(root)

    while queue:
        node = queue.pop(0)
        hd = node.hd

        # Update the last node encountered at the current horizontal distance
        node_dict[hd] = node.data

        if node.left is not None:
            node.left.hd = hd - 1
            queue.append(node.left)

        if node.right is not None:
            node.right.hd = hd + 1
            queue.append(node.right)

    # Print the bottom view nodes
    print("Bottom view of the binary tree:")
    for hd in sorted(node_dict.keys()):
        print(node_dict[hd], end=" ")


# Create the binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right= Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.right.left = Node(8)
root.left.right.right= Node(9)

# Find and print the bottom view
findBottomView(root)
