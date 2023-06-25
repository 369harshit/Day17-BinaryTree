class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def left_view(root, depth=0, result=[]):
    if not root:
        return

    if depth == len(result):
        result.append(root.val)

    left_view(root.left, depth + 1, result)
    left_view(root.right, depth + 1, result)


def right_view(root, depth=0, result=[]):
    if not root:
        return

    if depth == len(result):
        result.append(root.val)

    right_view(root.right, depth + 1, result)
    right_view(root.left, depth + 1, result)


# Example usage:
# Creating a binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(5)
root.right.right = TreeNode(6)

# Getting the left view of the tree
left_view_nodes = []
left_view(root, 0, left_view_nodes)
print("Left view:", left_view_nodes)  # Output: [1, 2, 4]

# Getting the right view of the tree
right_view_nodes = []
right_view(root, 0, right_view_nodes)
print("Right view:", right_view_nodes)  # Output: [1, 3, 6]
