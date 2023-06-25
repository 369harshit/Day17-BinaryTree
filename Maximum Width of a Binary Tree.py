from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def get_max_width(root):
    if not root:
        return 0

    max_width = 1
    queue = deque([(root, 0)])  # Tuple: (node, position)

    while queue:
        level_width = len(queue)
        _, first_position = queue[0]
        _, last_position = queue[-1]
        max_width = max(max_width, last_position - first_position + 1)

        for _ in range(level_width):
            node, position = queue.popleft()

            if node.left:
                queue.append((node.left, 2 * position))
            if node.right:
                queue.append((node.right, 2 * position + 1))

    return max_width

# Example usage:
# Create the binary tree
root = TreeNode(1)
root.left = TreeNode(3)
root.right = TreeNode(2)
root.left.left = TreeNode(5)
root.left.left.left = TreeNode(7)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(6)

# Get the maximum width of the binary tree
max_width = get_max_width(root)
print("Maximum width of the binary tree:", max_width)
