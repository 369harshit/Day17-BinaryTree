# Node class
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def verticalOrderTraversal(root):
    if not root:
        return []

    # Dictionary to store nodes at each horizontal distance
    node_dict = {}

    # Queue for level order traversal
    queue = [(root, 0)]

    # Perform level order traversal and populate the node_dict
    while queue:
        node, hd = queue.pop(0)

        if hd in node_dict:
            node_dict[hd].append(node.val)
        else:
            node_dict[hd] = [node.val]

        if node.left:
            queue.append((node.left, hd - 1))
        if node.right:
            queue.append((node.right, hd + 1))

    # Sort the dictionary keys to maintain the vertical order
    sorted_hds = sorted(node_dict.keys())

    # Extract the nodes in vertical order
    vertical_order = []
    for hd in sorted_hds:
        vertical_order.append(node_dict[hd])

    return vertical_order


# Create the binary tree
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

# Perform vertical order traversal
vertical_order = verticalOrderTraversal(root)

# Print the vertical order traversal
print(vertical_order)
